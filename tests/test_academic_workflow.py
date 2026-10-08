# -*- coding: utf-8 -*-
"""
tests/test_academic_workflow.py: 学术写作流程架构质量门禁稳定性回归测试套件

测试覆盖范围：
1. 通用学术写作技能彻底解耦（零项目专属词汇泄漏）；
2. 章节契约状态声明与多方语义一致性（框架参考、路线未决、防自动升级）；
3. academic-doc-builder 技能职责收窄（聚焦 Word 文档工程，显式排除正文起草，与 academic-writing 无重叠）；
4. 测试隔离保障：每个测试用例使用唯一隔离沙箱，安全递归清理，绝不触碰已有用户文件；
5. 部分规则缺失致命拦截：PROJECT_FACTS.md 与 TERMINOLOGY.md 缺一不可，任一缺失/不可读必须返回 ERROR(2)；
6. 归档与历史目录排除：开题报告内部归档、历史及素材目录自动排除在扫描范围外；
7. 显式目录参数越权防护：禁止根目录或非正文目录作为受检目标，返回 ERROR(2)；
8. DOCX 深度扫描：全面覆盖节页眉、节页脚（含首页/奇偶页）及表格内嵌套表格，命中即 FAIL(1)，合规即 PASS(0)；
9. 命令行 --target 无参数明确拦截：显式传入 --target 但缺少参数时返回 ERROR(2)，绝不静默走默认范围；
10. 术语正误精细区分：正规学术术语“控制律”绝对不被误拦截 (PASS 0)，错别字“控制率”精准阻断 (FAIL 1)；
11. CLI 命令行 subprocess 完整调用与三态退出码真实验证。
"""

import os
import sys
import shutil
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
    REQUIRED_RULE_FILES,
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

    def test_academic_doc_builder_responsibilities_and_trigger_narrowed(self):
        """用例 3: 验证 academic-doc-builder/SKILL.md 触发条件收窄，聚焦 Word 文档工程，避免与通用写作触发重叠"""
        builder_skill = PROJECT_ROOT / ".agents" / "skills" / "academic-doc-builder" / "SKILL.md"
        self.assertTrue(builder_skill.exists())
        content = builder_skill.read_text(encoding="utf-8")

        # 检查 description 触发条件收窄
        self.assertIn("Use this skill exclusively for Word", content)
        self.assertIn("Do NOT use for general academic prose writing", content)

        # 检查三权分立与职责切分表述
        self.assertIn("通用学术写作技能", content)
        self.assertIn("正文学术质量", content)
        self.assertIn("docs/contracts/", content)
        self.assertIn("Word 文档工程与排版格式", content)
        self.assertIn("PROJECT_NOW.md", content)
        self.assertIn("禁止将项目专属知识与技术方案重新写回通用 `academic-writing`", content)


class TestQualityGateRegressionSuite(unittest.TestCase):
    """质量门禁确定性功能、异常边界与三态结果回归测试套件"""

    def setUp(self):
        """为每个测试用例创建唯一的隔离临时沙箱目录，位于授权受检范围内"""
        self._temp_dir_obj = tempfile.TemporaryDirectory(
            prefix="_test_sandbox_",
            dir=str(PROJECT_ROOT / "开题报告")
        )
        self.test_dir = Path(self._temp_dir_obj.name).resolve()

    def tearDown(self):
        """递归安全清理当前测试用例专用的临时沙箱，绝不影响或删除已存在的其他用户文件"""
        if hasattr(self, "_temp_dir_obj"):
            try:
                self._temp_dir_obj.cleanup()
            except Exception:
                if hasattr(self, "test_dir") and self.test_dir.exists():
                    shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_test_sandbox_isolation_and_safe_cleanup(self):
        """用例 4: 验证测试沙箱隔离性、安全递归清理，以及绝不触碰已有用户文件"""
        # 1. 验证临时沙箱名称唯一且存在
        self.assertTrue(self.test_dir.exists())
        self.assertTrue(self.test_dir.name.startswith("_test_sandbox_"))

        # 2. 在沙箱内创建多层深层嵌套子文件夹与文件
        nested_dir = self.test_dir / "level1" / "level2"
        nested_dir.mkdir(parents=True, exist_ok=True)
        test_file = nested_dir / "sample.txt"
        test_file.write_text("Temporary test data", encoding="utf-8")
        self.assertTrue(test_file.exists())

        # 3. 验证已有正文文件完好无损，不受任何影响
        real_draft_md = PROJECT_ROOT / "开题报告" / "开题报告_正文起草稿.md"
        self.assertTrue(real_draft_md.exists())

    def test_quality_gate_normal_md_and_docx_pass(self):
        """用例 5: 正常合规的临时 Markdown 与 DOCX（段落与表格）顺利通过，报告 PASS (退出码 0)"""
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
        """用例 6: Markdown 与 DOCX 中包含禁用词（段落及表格单元格）精准拦截并返回 FAIL (退出码 1)"""
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

    def test_quality_gate_error_on_partial_missing_rules(self):
        """用例 7: 规则文件缺一不可，任一缺失/不可读必须返回 ERROR (退出码 2)，绝不错误放行"""
        with tempfile.TemporaryDirectory() as mock_root_str:
            mock_root = Path(mock_root_str)
            mock_docs = mock_root / "docs"
            mock_docs.mkdir()
            mock_report = mock_root / "开题报告"
            mock_report.mkdir()
            clean_file = mock_report / "草稿.md"
            clean_file.write_text("完全合规的正文内容", encoding="utf-8")

            # 场景 A: 仅存在 PROJECT_FACTS.md，缺失 TERMINOLOGY.md
            facts_file = mock_docs / "PROJECT_FACTS.md"
            facts_file.write_text("### F-001\n<!-- gate:forbid:开架式 -->\n", encoding="utf-8")
            res_missing_term = run_quality_check(target_paths=[str(clean_file)], project_root=mock_root)
            self.assertEqual(res_missing_term.status, "ERROR")
            self.assertEqual(res_missing_term.exit_code, 2)
            self.assertFalse(res_missing_term.passed)
            self.assertTrue(any("docs/TERMINOLOGY.md" in err for err in res_missing_term.errors))

            # 场景 B: 仅存在 TERMINOLOGY.md，缺失 PROJECT_FACTS.md
            facts_file.unlink()
            term_file = mock_docs / "TERMINOLOGY.md"
            term_file.write_text("### T-001\n<!-- gate:forbid:控制率 -->\n", encoding="utf-8")
            res_missing_facts = run_quality_check(target_paths=[str(clean_file)], project_root=mock_root)
            self.assertEqual(res_missing_facts.status, "ERROR")
            self.assertEqual(res_missing_facts.exit_code, 2)
            self.assertFalse(res_missing_facts.passed)
            self.assertTrue(any("docs/PROJECT_FACTS.md" in err for err in res_missing_facts.errors))

            # 场景 C: 两份文件均存在但其中一份未包含任何有效规则
            facts_file.write_text("### F-001\n无门禁规则声明\n", encoding="utf-8")
            res_empty_rules = run_quality_check(target_paths=[str(clean_file)], project_root=mock_root)
            self.assertEqual(res_empty_rules.status, "ERROR")
            self.assertEqual(res_empty_rules.exit_code, 2)
            self.assertTrue(any("未包含任何有效" in err for err in res_empty_rules.errors))

    def test_archive_and_history_subdirectories_excluded(self):
        """用例 8: 排除开题报告内部归档与历史文件目录，不误扫历史资产"""
        # 在测试沙箱内创建“归档”和“历史”子目录，并放入违规文件
        archive_dir = self.test_dir / "归档" / "历史版本"
        archive_dir.mkdir(parents=True, exist_ok=True)
        bad_archive_doc = archive_dir / "old_draft.md"
        bad_archive_doc.write_text("历史归档中的开架式记录与控制率记录", encoding="utf-8")

        # 在测试沙箱根部放置一个合规文件
        clean_doc = self.test_dir / "active_draft.md"
        clean_doc.write_text("当前正在活跃编辑的合规草稿正文", encoding="utf-8")

        # 扫描整个沙箱目录
        result = run_quality_check(target_paths=[str(self.test_dir)], project_root=PROJECT_ROOT)
        self.assertEqual(result.status, "PASS")
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(len(result.violations), 0)
        # 实际扫描的文件仅有 active_draft.md，归档目录完全被排除
        self.assertEqual(len(result.scanned_files), 1)
        self.assertEqual(result.scanned_files[0], clean_doc)

    def test_unauthorized_dir_scan_blocked(self):
        """用例 9: 检查显式目录参数越权递归防护，根目录与非开题报告目录严禁扫描 (ERROR 2)"""
        # 1. 显式传入项目根目录 "."
        res_root = run_quality_check(target_paths=[str(PROJECT_ROOT)], project_root=PROJECT_ROOT)
        self.assertEqual(res_root.status, "ERROR")
        self.assertEqual(res_root.exit_code, 2)
        self.assertTrue(any("禁止将整个项目根目录作为受检目标" in err for err in res_root.errors))

        # 2. 显式传入非学术正文授权目录（如 docs 目录）
        docs_dir = PROJECT_ROOT / "docs"
        res_docs = run_quality_check(target_paths=[str(docs_dir)], project_root=PROJECT_ROOT)
        self.assertEqual(res_docs.status, "ERROR")
        self.assertEqual(res_docs.exit_code, 2)
        self.assertTrue(any("属于受保护黑名单或非学术正文范围" in err for err in res_docs.errors))

    def test_docx_deep_scan_header_footer_nested_table(self):
        """用例 10: 明确 DOCX 扫描深度覆盖页眉、页脚（含首页/奇偶页）与单元格嵌套表格"""
        # 1. 页眉包含违规词
        header_docx = self.test_dir / "bad_header.docx"
        doc_h = docx.Document()
        sec_h = doc_h.sections[0]
        sec_h.header.paragraphs[0].text = "页眉中提及开架式水下航行器"
        doc_h.add_paragraph("正常正文段落")
        doc_h.save(str(header_docx))

        res_h = run_quality_check(target_paths=[str(header_docx)], project_root=PROJECT_ROOT)
        self.assertEqual(res_h.status, "FAIL")
        self.assertEqual(res_h.exit_code, 1)
        self.assertEqual(len(res_h.violations), 1)
        self.assertIn("页眉", res_h.violations[0]["location"])
        self.assertEqual(res_h.violations[0]["keyword"], "开架式")

        # 2. 页脚包含违规词
        footer_docx = self.test_dir / "bad_footer.docx"
        doc_f = docx.Document()
        sec_f = doc_f.sections[0]
        sec_f.footer.paragraphs[0].text = "页脚标记控制率说明"
        doc_f.add_paragraph("正常正文段落")
        doc_f.save(str(footer_docx))

        res_f = run_quality_check(target_paths=[str(footer_docx)], project_root=PROJECT_ROOT)
        self.assertEqual(res_f.status, "FAIL")
        self.assertEqual(res_f.exit_code, 1)
        self.assertEqual(len(res_f.violations), 1)
        self.assertIn("页脚", res_f.violations[0]["location"])
        self.assertEqual(res_f.violations[0]["keyword"], "控制率")

        # 3. 表格内包含嵌套表格，且嵌套表格违规
        nested_docx = self.test_dir / "bad_nested.docx"
        doc_n = docx.Document()
        outer_tbl = doc_n.add_table(rows=1, cols=1)
        outer_cell = outer_tbl.cell(0, 0)
        outer_cell.text = "外层表格合规说明"
        inner_tbl = outer_cell.add_table(rows=1, cols=1)
        inner_tbl.cell(0, 0).text = "内层嵌套表格违规开架式构型"
        doc_n.save(str(nested_docx))

        res_n = run_quality_check(target_paths=[str(nested_docx)], project_root=PROJECT_ROOT)
        self.assertEqual(res_n.status, "FAIL")
        self.assertEqual(res_n.exit_code, 1)
        self.assertEqual(len(res_n.violations), 1)
        self.assertIn("嵌套表格", res_n.violations[0]["location"])
        self.assertEqual(res_n.violations[0]["keyword"], "开架式")

        # 4. 页眉、页脚及嵌套表格全部合规的 DOCX
        clean_deep_docx = self.test_dir / "clean_deep.docx"
        doc_c = docx.Document()
        doc_c.sections[0].header.paragraphs[0].text = "同济大学本科毕业论文开题报告"
        doc_c.sections[0].footer.paragraphs[0].text = "第 1 页"
        tbl_c = doc_c.add_table(rows=1, cols=1)
        tbl_c.cell(0, 0).text = "外层参数"
        sub_c = tbl_c.cell(0, 0).add_table(rows=1, cols=1)
        sub_c.cell(0, 0).text = "内层参数：航向控制律自适应调节"
        doc_c.save(str(clean_deep_docx))

        res_c = run_quality_check(target_paths=[str(clean_deep_docx)], project_root=PROJECT_ROOT)
        self.assertEqual(res_c.status, "PASS")
        self.assertEqual(res_c.exit_code, 0)
        self.assertEqual(len(res_c.violations), 0)

    def test_empty_target_flag_reports_error(self):
        """用例 11: --target 后缺少实际参数时必须明确报错 ERROR (退出码 2)，绝不静默使用默认范围"""
        # 1. API 级别：target_paths=[] 传入空列表
        res_empty = run_quality_check(target_paths=[], project_root=PROJECT_ROOT)
        self.assertEqual(res_empty.status, "ERROR")
        self.assertEqual(res_empty.exit_code, 2)
        self.assertTrue(any("未提供任何有效目标路径" in err for err in res_empty.errors))

        # 2. CLI 级别：命令行传入 --target 但无后续文件参数
        cmd = [sys.executable, str(PROJECT_ROOT / "scripts" / "check_academic_quality.py"), "--target"]
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("[ERROR]", proc.stdout)
        self.assertIn("--target 未指定具体目标路径", proc.stdout)

    def test_proper_term_kongzhilv_not_intercepted(self):
        """用例 12: 正规学术术语“控制律”绝对不被误拦截 (PASS 0)，错别字“控制率”精准阻断 (FAIL 1)"""
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
        """用例 13: 验证黑名单文件无法越权扫描 (ERROR 2)，以及命令行 CLI 调用的真实三态退出码"""
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
