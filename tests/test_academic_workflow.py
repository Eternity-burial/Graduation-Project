# -*- coding: utf-8 -*-
"""
tests/test_academic_workflow.py: 学术写作流程架构第二轮质量修复与自动化回归测试套件

测试覆盖范围：
1. 通用学术写作技能彻底解耦（零项目专属词汇泄漏）；
2. 章节契约状态声明与多方语义一致性（框架参考、路线未决、防自动升级）；
3. academic-doc-builder 技能职责同步（通用写作、章节契约、排版工程三权分立，优先同步 PROJECT_NOW.md）；
4. 正常 Markdown 与正常 DOCX 顺利通过（PASS，退出码 0，并输出扫描清单）；
5. 包含禁用词的 Markdown 与 DOCX 精准拦截（FAIL，退出码 1，支持段落与表格定位）；
6. 规则缺失、目标不存在、空扫描范围的致命拦截（ERROR，退出码 2）；
7. 损坏 DOCX 文件、UTF-8 解码异常文件、越界路径的致命拦截（ERROR，退出码 2）；
8. 正确学术术语“控制律”绝对不被误拦截，与违规词“控制率”精准区分；
9. 规则文件、历史文档与黑名单防护，禁止误扫并拒绝越权传参；
10. CLI 命令行 subprocess 完整调用与三态退出码真实验证。
"""

import os
import sys
import tempfile
import unittest
import subprocess
from pathlib import Path

# 确保控制台 UTF-8 输出
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import docx
from scripts.check_academic_quality import (
    load_gate_rules,
    extract_file_lines,
    run_quality_check,
    is_blacklisted,
    QualityCheckResult,
)


class TestAcademicWorkflowArchitecture(unittest.TestCase):
    """学术写作流程架构解耦与规范性验证"""

    def test_academic_writing_skill_is_strictly_generic(self):
        """用例 1: 验证 academic-writing/SKILL.md 彻底解耦，不含任何本项目特定词汇"""
        skill_path = PROJECT_ROOT / ".agents" / "skills" / "academic-writing" / "SKILL.md"
        self.assertTrue(skill_path.exists(), f"文件不存在: {skill_path}")
        content = skill_path.read_text(encoding="utf-8")

        forbidden_project_words = [
            "PX4",
            "SwiftROV",
            "开架式",
            "Fossen",
            "八推进器",
            "吴均峰",
            "LIAS",
            "同济大学",
            "机械工程与机器人学院",
            "六自由度机理建模与低成本水动力参数辨识",
            "Smallwood",
            "Prestero",
        ]

        leaked_words = [w for w in forbidden_project_words if w in content]
        self.assertEqual(
            leaked_words,
            [],
            f"通用写作技能中泄漏了项目专属词汇: {leaked_words}",
        )

    def test_chapter_contract_status_and_reference_semantics(self):
        """用例 2: 验证开题契约顶部包含状态声明，且 AGENTS.md/PROJECT_NOW.md/academic-entry.md 语义一致无冲突"""
        target_contract = PROJECT_ROOT / "docs" / "contracts" / "opening_report_contracts_and_evidence.md"
        self.assertTrue(target_contract.exists(), f"单一可信源契约不存在: {target_contract}")
        contract_text = target_contract.read_text(encoding="utf-8")

        # 契约必须包含内容状态声明
        self.assertIn("当前内容状态声明", contract_text)
        self.assertIn("框架参考性", contract_text)
        self.assertIn("路线未决性", contract_text)
        self.assertIn("防自动升级", contract_text)

        # 检查各规则文档的引用语义
        agents_text = (PROJECT_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        now_text = (PROJECT_ROOT / "PROJECT_NOW.md").read_text(encoding="utf-8")
        entry_text = (PROJECT_ROOT / ".agents" / "rules" / "academic-entry.md").read_text(encoding="utf-8")

        # AGENTS.md 必须表达“参考章节功能与组织框架”而非死板锁定具体算法
        self.assertIn("章节功能与组织框架参考", agents_text)
        self.assertIn("未决假设", agents_text)

        # PROJECT_NOW.md 必须明确章节契约提供结构参考且具体路线暂缓
        self.assertIn("提供结构与功能参考，具体技术路线尚未最终确认", now_text)
        self.assertIn("维持 PROVISIONAL 状态", now_text)

        # academic-entry.md 必须提醒契约未决路线不得直接视为已确定决定
        self.assertIn("作为章节功能与结构参考", entry_text)
        self.assertIn("未决技术路线与任务细分不得直接升级为已确定的研究决定", entry_text)

    def test_academic_doc_builder_responsibilities_sync(self):
        """用例 3: 验证 academic-doc-builder/SKILL.md 职责切分严谨，明确优先同步 PROJECT_NOW.md"""
        builder_skill = PROJECT_ROOT / ".agents" / "skills" / "academic-doc-builder" / "SKILL.md"
        self.assertTrue(builder_skill.exists())
        content = builder_skill.read_text(encoding="utf-8")

        # 检查三权分立与职责切分表述
        self.assertIn("通用学术写作技能", content)
        self.assertIn("正文学术质量", content)
        self.assertIn("docs/contracts/", content)
        self.assertIn("文档工程与排版格式", content)
        self.assertIn("PROJECT_NOW.md", content)
        self.assertIn("禁止将项目专属知识与技术方案重新写回通用 `academic-writing`", content)


class TestQualityGateRegressionSuite(unittest.TestCase):
    """质量门禁确定性功能、异常边界与三态结果回归测试套件"""

    def setUp(self):
        """在开题报告目录下建立隔离的测试临时文件夹，确保在项目授权范围内且测试结束后清理"""
        self.test_dir = PROJECT_ROOT / "开题报告" / "_temp_quality_test_sandbox"
        self.test_dir.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        """清理临时测试沙箱及生成的文件"""
        if self.test_dir.exists():
            for f in self.test_dir.glob("*"):
                try:
                    f.unlink()
                except Exception:
                    pass
            try:
                self.test_dir.rmdir()
            except Exception:
                pass

    def test_quality_gate_normal_md_and_docx_pass(self):
        """用例 4: 正常合规的临时 Markdown 与 DOCX（段落与表格）顺利通过，报告 PASS (退出码 0)"""
        clean_md = self.test_dir / "clean_draft.md"
        clean_md.write_text(
            "# 正常开题报告草稿\n"
            "本研究针对水下航行器紧凑型实验平台开展动力学建模与模型控制方法研究。\n"
            "在水池实验中验证推力分配与姿态控制算法的有效性。\n",
            encoding="utf-8",
        )

        clean_docx = self.test_dir / "clean_draft.docx"
        doc = docx.Document()
        doc.add_heading("正常测试开题报告", level=1)
        doc.add_paragraph("本实验平台采用紧凑型双耐压舱结构集成。")
        tbl = doc.add_table(rows=2, cols=2)
        tbl.cell(0, 0).text = "参数名称"
        tbl.cell(0, 1).text = "标称数值"
        tbl.cell(1, 0).text = "航向控制律"
        tbl.cell(1, 1).text = "模型增益自适应"
        doc.save(str(clean_docx))

        result = run_quality_check(target_paths=[str(clean_md), str(clean_docx)], project_root=PROJECT_ROOT)

        self.assertEqual(result.status, "PASS")
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(result.passed)
        self.assertEqual(len(result.violations), 0)
        self.assertEqual(len(result.scanned_files), 2)
        self.assertEqual(len(result.errors), 0)

    def test_quality_gate_forbidden_words_detected_in_md_and_docx(self):
        """用例 5: Markdown 与 DOCX 中包含禁用词（段落及表格单元格）精准拦截并返回 FAIL (退出码 1)"""
        # 1. 包含禁用词的 Markdown
        bad_md = self.test_dir / "bad_draft.md"
        bad_md.write_text(
            "# 违规草稿\n"
            "本实验平台采用开架式结构搭建。\n"
            "控制器采用自整定控制率算法。\n",
            encoding="utf-8",
        )

        res_md = run_quality_check(target_paths=[str(bad_md)], project_root=PROJECT_ROOT)
        self.assertEqual(res_md.status, "FAIL")
        self.assertEqual(res_md.exit_code, 1)
        self.assertFalse(res_md.passed)
        self.assertEqual(len(res_md.violations), 2)
        kw_hits = [v["keyword"] for v in res_md.violations]
        self.assertIn("开架式", kw_hits)
        self.assertIn("控制率", kw_hits)

        # 2. 包含禁用词的 DOCX（分别测试段落违规与表格单元格违规）
        bad_docx = self.test_dir / "bad_draft.docx"
        doc = docx.Document()
        doc.add_paragraph("实验样机为开架式构型。")
        tbl = doc.add_table(rows=1, cols=1)
        tbl.cell(0, 0).text = "推力分配控制率"
        doc.save(str(bad_docx))

        res_docx = run_quality_check(target_paths=[str(bad_docx)], project_root=PROJECT_ROOT)
        self.assertEqual(res_docx.status, "FAIL")
        self.assertEqual(res_docx.exit_code, 1)
        self.assertEqual(len(res_docx.violations), 2)

        # 校验位置描述
        locations = [v["location"] for v in res_docx.violations]
        self.assertTrue(any("段落" in loc for loc in locations))
        self.assertTrue(any("表格" in loc for loc in locations))

    def test_quality_gate_error_on_missing_rules(self):
        """用例 6: 当规则文件不存在或无有效规则时，必须返回 ERROR (退出码 2)"""
        with tempfile.TemporaryDirectory() as empty_dir:
            empty_root = Path(empty_dir)
            result = run_quality_check(project_root=empty_root)
            self.assertEqual(result.status, "ERROR")
            self.assertEqual(result.exit_code, 2)
            self.assertFalse(result.passed)
            self.assertTrue(any("未在 docs/ 中发现任何有效的 gate:forbid 门禁规则" in err for err in result.errors))

    def test_quality_gate_error_on_missing_targets_and_empty_scope(self):
        """用例 7: 指定目标不存在或受检正文集合为空时，必须返回 ERROR (退出码 2)"""
        # 指定不存在的文件
        nonexistent = PROJECT_ROOT / "开题报告" / "nonexistent_target_12345.md"
        res_nonexistent = run_quality_check(target_paths=[str(nonexistent)], project_root=PROJECT_ROOT)
        self.assertEqual(res_nonexistent.status, "ERROR")
        self.assertEqual(res_nonexistent.exit_code, 2)
        self.assertTrue(any("指定的目标路径不存在" in err for err in res_nonexistent.errors))

        # 指定空目录（无学术正文文件）
        empty_sub = self.test_dir / "empty_folder"
        empty_sub.mkdir()
        res_empty = run_quality_check(target_paths=[str(empty_sub)], project_root=PROJECT_ROOT)
        self.assertEqual(res_empty.status, "ERROR")
        self.assertEqual(res_empty.exit_code, 2)
        self.assertTrue(any("未找到任何有效的正文文件" in err for err in res_empty.errors))

    def test_quality_gate_error_on_corrupt_files_encoding_and_oob_paths(self):
        """用例 8: 损坏的 DOCX、非 UTF-8 编码的 MD、以及越界路径，必须返回 ERROR (退出码 2)"""
        # 1. 损坏的 DOCX（伪造非 ZIP 二进制流）
        corrupt_docx = self.test_dir / "corrupt.docx"
        corrupt_docx.write_bytes(b"This is completely corrupted non-zip binary content.")
        res_corrupt = run_quality_check(target_paths=[str(corrupt_docx)], project_root=PROJECT_ROOT)
        self.assertEqual(res_corrupt.status, "ERROR")
        self.assertEqual(res_corrupt.exit_code, 2)
        self.assertTrue(any("无法读取或解析文件" in err for err in res_corrupt.errors))

        # 2. 损坏的编码（非法 UTF-8 字节）
        bad_encoding_md = self.test_dir / "bad_encoding.md"
        bad_encoding_md.write_bytes(b"\xff\xfe\x00\x80\xaa\xbb\xcc")
        res_encoding = run_quality_check(target_paths=[str(bad_encoding_md)], project_root=PROJECT_ROOT)
        self.assertEqual(res_encoding.status, "ERROR")
        self.assertEqual(res_encoding.exit_code, 2)
        self.assertTrue(any("无法读取或解析文件" in err for err in res_encoding.errors))

        # 3. 越界路径（位于 project_root 外部的临时文件）
        with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as oob_file:
            oob_path = Path(oob_file.name)
            oob_file.write(b"Normal text")

        try:
            res_oob = run_quality_check(target_paths=[str(oob_path)], project_root=PROJECT_ROOT)
            self.assertEqual(res_oob.status, "ERROR")
            self.assertEqual(res_oob.exit_code, 2)
            self.assertTrue(any("超出项目授权范围" in err for err in res_oob.errors))
        finally:
            if oob_path.exists():
                oob_path.unlink()

    def test_proper_term_kongzhilv_not_intercepted(self):
        """用例 9: 正规学术术语“控制律”绝对不被误拦截 (PASS 0)，且改写为“控制率”时精准阻断 (FAIL 1)"""
        # 合规文件：包含多个“控制律”表达
        good_file = self.test_dir / "term_check_good.md"
        good_file.write_text(
            "# 控制理论与方法\n"
            "针对八推进器紧凑型水下航行器设计非线性控制律与状态观测器。\n"
            "结合前馈补偿控制律与增益自适应状态反馈控制律，实现水下高精度轨迹跟踪。\n",
            encoding="utf-8",
        )

        res_good = run_quality_check(target_paths=[str(good_file)], project_root=PROJECT_ROOT)
        self.assertEqual(res_good.status, "PASS")
        self.assertEqual(res_good.exit_code, 0)
        self.assertEqual(len(res_good.violations), 0)

        # 违规对比文件：将“控制律”替换为错别字“控制率”
        bad_file = self.test_dir / "term_check_bad.md"
        bad_file.write_text(
            "# 控制理论与方法\n"
            "针对八推进器紧凑型水下航行器设计非线性控制率与状态观测器。\n",
            encoding="utf-8",
        )

        res_bad = run_quality_check(target_paths=[str(bad_file)], project_root=PROJECT_ROOT)
        self.assertEqual(res_bad.status, "FAIL")
        self.assertEqual(res_bad.exit_code, 1)
        self.assertEqual(len(res_bad.violations), 1)
        self.assertEqual(res_bad.violations[0]["keyword"], "控制率")

    def test_quality_gate_blacklist_and_cli_subprocess(self):
        """用例 10: 验证黑名单文件无法越权扫描 (ERROR 2)，以及命令行 CLI 调用的真实三态退出码"""
        # 1. 黑名单判定与显式传入拦截
        term_file = PROJECT_ROOT / "docs" / "TERMINOLOGY.md"
        self.assertTrue(is_blacklisted(term_file, PROJECT_ROOT))
        res_blacklisted = run_quality_check(target_paths=[str(term_file)], project_root=PROJECT_ROOT)
        self.assertEqual(res_blacklisted.status, "ERROR")
        self.assertEqual(res_blacklisted.exit_code, 2)
        self.assertTrue(any("属于受保护黑名单" in err for err in res_blacklisted.errors))

        # 2. CLI 默认运行：必须正常通过 (PASS 0)，并打印扫描清单及数量
        cmd_default = [sys.executable, str(PROJECT_ROOT / "scripts" / "check_academic_quality.py")]
        proc_default = subprocess.run(cmd_default, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc_default.returncode, 0, f"默认运行失败: {proc_default.stderr}")
        self.assertIn("[PASS] 质量门禁检查通过！", proc_default.stdout)
        self.assertIn("本次实际扫描正文文件", proc_default.stdout)
        self.assertIn("开题报告_正文起草稿.md", proc_default.stdout)

        # 3. CLI 指定不存在文件：必须返回退出码 2 (ERROR)
        cmd_err = [sys.executable, str(PROJECT_ROOT / "scripts" / "check_academic_quality.py"), "-t", "nonexistent.md"]
        proc_err = subprocess.run(cmd_err, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc_err.returncode, 2)
        self.assertIn("[ERROR]", proc_err.stdout)

        # 4. CLI 指定违规临时文件：必须返回退出码 1 (FAIL)
        bad_cli_file = self.test_dir / "bad_cli.md"
        bad_cli_file.write_text("本样机采用开架式结构构建。", encoding="utf-8")
        cmd_fail = [sys.executable, str(PROJECT_ROOT / "scripts" / "check_academic_quality.py"), "-t", str(bad_cli_file)]
        proc_fail = subprocess.run(cmd_fail, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc_fail.returncode, 1)
        self.assertIn("[FAIL]", proc_fail.stdout)
        self.assertIn("开架式", proc_fail.stdout)


if __name__ == "__main__":
    unittest.main()
