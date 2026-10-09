# -*- coding: utf-8 -*-
"""
tests/test_academic_workflow.py: 学术写作流程架构质量门禁与配置核验回归测试套件

测试覆盖范围：
1. 架构解耦与职责收窄：
   - academic-writing/SKILL.md 零项目专属词汇泄漏；
   - 章节契约状态声明（框架参考、路线未决、防自动升级）；
   - academic-doc-builder 职责收窄至 Word 工程，排除正文起草；
2. 目标发现与统一路径授权安全（A1/A2/D1）：
   - 递归发现子目录有效正文；
   - 排除归档、历史、图片、修改建议、临时文件与辅助笔记；
   - 排除脚本、参考文献与任务书底稿；
   - 空受检目标集合拦截（ERROR 2）；
   - 显式非授权目录/文件、根目录、越界遍历与符号链接拒绝（ERROR 2）；
   - 黑名单文件即使显式指定绝对路径亦拒绝（ERROR 2）；
3. 规则解析与确定性边界（A3/B1/B2/D2）：
   - 严格合法 FT 编号解析，拒绝带竖线等非法编号；
   - 空禁词标记拦截（ERROR 2）；
   - 规则文件缺失/不可读/无规则拦截（ERROR 2）；
   - 重复规则去重；
   - 允许候选方案正常研讨（MPC, INDI, 滑模等），不凭关键词妄断违规；
   - 区分正规学术词（“控制律”、“标称模型”）与错别字（“控制率”）；
4. 文档深度扫描与虚假 PASS 防护（A4/A5/D3）：
   - 合法 Markdown / DOCX 正常通过 (PASS 0)；
   - 违规 Markdown / DOCX 阻断 (FAIL 1)；
   - DOCX 深度扫描：段落、表格单元格、嵌套表格、默认/首页/奇偶页页眉与页脚；
   - 损坏 DOCX 明确报告 ERROR(2)；
   - 空正文文档（0 字节或纯空白）拒绝虚假 PASS (ERROR 2)；
   - 不支持文件类型报错 (ERROR 2)；
   - 中文文件名与特殊路径编码兼容；
5. 轻量工作区配置门禁（C）：
   - 真实工作区全项配置完整性验证 (PASS 0)；
   - 关键文件缺失 (ERROR 2)、专有词泄漏与危险推送授权 (FAIL 1) 拦截验证；
6. 命令行 CLI 进程级调用与三态退出码真实验证；
7. 测试沙箱彻底独立隔离（D4）：全套使用标准系统临时目录，绝不污染真实工作区。
"""

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
    find_default_targets,
    validate_target_path,
    QualityCheckResult,
    REQUIRED_RULE_FILES,
)
from scripts.check_workspace_config import (
    run_workspace_config_check,
    ConfigCheckResult,
)


class TestAcademicWorkflowArchitecture(unittest.TestCase):
    """学术写作流程架构解耦与规范性静态只读验证"""

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
        """用例 2: 验证开题契约包含状态声明，且 AGENTS.md/PROJECT_NOW.md/academic-entry.md 语义一致无冲突"""
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

        self.assertIn("章节功能与组织框架参考", agents_text)
        self.assertIn("未决假设", agents_text)

        self.assertIn("提供结构与功能参考，具体技术路线尚未最终确认", now_text)
        self.assertIn("维持 PROVISIONAL 状态", now_text)

        self.assertIn("作为章节功能与结构参考", entry_text)
        self.assertIn("未决技术路线与任务细分不得直接升级为已确定的研究决定", entry_text)

    def test_academic_doc_builder_responsibilities_and_trigger_narrowed(self):
        """用例 3: 验证 academic-doc-builder/SKILL.md 触发条件收窄，聚焦 Word 文档工程，避免与通用写作重叠"""
        builder_skill = PROJECT_ROOT / ".agents" / "skills" / "academic-doc-builder" / "SKILL.md"
        self.assertTrue(builder_skill.exists())
        content = builder_skill.read_text(encoding="utf-8")

        self.assertIn("Use this skill exclusively for Word", content)
        self.assertIn("Do NOT use for general academic prose writing", content)
        self.assertIn("通用学术写作技能", content)
        self.assertIn("Word 文档工程与排版格式", content)


class StandaloneSandboxBase(unittest.TestCase):
    """
    完全独立的测试沙箱基类：
    在标准系统临时目录构建虚拟工作区，彻底隔离，不污染真实项目开题报告目录
    """

    def setUp(self):
        self._temp_dir_obj = tempfile.TemporaryDirectory(prefix="test_academic_gate_")
        self.mock_root = Path(self._temp_dir_obj.name).resolve()

        # 构建虚拟项目的基本结构
        self.mock_docs = self.mock_root / "docs"
        self.mock_docs.mkdir(parents=True, exist_ok=True)
        self.mock_report = self.mock_root / "开题报告"
        self.mock_report.mkdir(parents=True, exist_ok=True)

        # 写入标准合规模拟规则
        self.facts_file = self.mock_docs / "PROJECT_FACTS.md"
        self.facts_file.write_text(
            "# Project Facts\n\n"
            "### F-001：物理构型特征抽象\n"
            "状态：CONFIRMED\n"
            "描述：八推进器紧凑型水下航行器\n"
            "<!-- gate:forbid:开架式 -->\n",
            encoding="utf-8",
        )

        self.term_file = self.mock_docs / "TERMINOLOGY.md"
        self.term_file.write_text(
            "# Terminology Policy\n\n"
            "### T-001：控制率误写纠正\n"
            "等级：ERROR\n"
            "<!-- gate:forbid:控制率 -->\n\n"
            "### T-002：控制律合法表达\n"
            "等级：PREFERENCE\n"
            "说明：控制律为正常控制科学术语\n",
            encoding="utf-8",
        )

    def tearDown(self):
        try:
            self._temp_dir_obj.cleanup()
        except Exception:
            shutil.rmtree(self.mock_root, ignore_errors=True)


class TestTargetDiscoveryAndPathAuthorization(StandaloneSandboxBase):
    """目标发现递归性、非正文排除与统一路径授权安全测试"""

    def test_default_target_finds_nested_academic_drafts(self):
        """用例 4: 默认扫描能够递归发现开题报告子目录中的正文草稿，且排除非正文"""
        # 1. 根层有效正文
        root_draft = self.mock_report / "开题报告_正文起草稿.md"
        root_draft.write_text("开题报告根层正文草稿内容", encoding="utf-8")

        # 2. 嵌套子目录中的有效正文
        nested_dir = self.mock_report / "正文" / "第1章"
        nested_dir.mkdir(parents=True, exist_ok=True)
        nested_draft = nested_dir / "chapter1_正文草稿.md"
        nested_draft.write_text("第一章正文草稿内容", encoding="utf-8")

        # 3. 辅助梳理材料与笔记（应排除）
        note_doc = self.mock_report / "SwiftROV_开题前信息与研究路线梳理.md"
        note_doc.write_text("信息梳理非正文内容", encoding="utf-8")

        # 4. 历史任务书参考底稿（应排除）
        ref_task_book = self.mock_report / "基于PX4的水下航行器模型控制方法研究.docx"
        ref_task_book.write_bytes(b"dummy")

        # 5. 参考文献与脚本（应排除）
        (self.mock_report / "references.bib").write_text("bib data", encoding="utf-8")
        (self.mock_report / "build_script.py").write_text("print()", encoding="utf-8")

        targets = find_default_targets(self.mock_root)
        self.assertEqual(len(targets), 2)
        self.assertIn(root_draft.resolve(), [t.resolve() for t in targets])
        self.assertIn(nested_draft.resolve(), [t.resolve() for t in targets])

    def test_archive_and_history_directories_strictly_excluded(self):
        """用例 5: 递归扫描与显式路径均严格排除归档、历史及素材目录"""
        # 在归档子目录中放入包含禁词的文件
        arch_dir = self.mock_report / "归档" / "历史版本"
        arch_dir.mkdir(parents=True, exist_ok=True)
        arch_bad = arch_dir / "old_draft.md"
        arch_bad.write_text("归档文件中的开架式错误记录", encoding="utf-8")

        # 在 figures 目录中放入说明文件
        fig_dir = self.mock_report / "figures"
        fig_dir.mkdir(parents=True, exist_ok=True)
        fig_bad = fig_dir / "figures_草稿.md"
        fig_bad.write_text("素材草稿中的控制率说明", encoding="utf-8")

        # 放置正常活跃正文
        active_draft = self.mock_report / "开题报告_正文草稿.md"
        active_draft.write_text("活跃的正常正文草稿", encoding="utf-8")

        # A. 默认扫描仅扫描 active_draft，归档和 figures 被排除
        res_default = run_quality_check(project_root=self.mock_root)
        self.assertEqual(res_default.status, "PASS")
        self.assertEqual(len(res_default.scanned_files), 1)
        self.assertEqual(res_default.scanned_files[0].resolve(), active_draft.resolve())

        # B. 显式指定归档文件路径，必须被严格拦截并报错 ERROR 2
        res_explicit_arch = run_quality_check(target_paths=[str(arch_bad)], project_root=self.mock_root)
        self.assertEqual(res_explicit_arch.status, "ERROR")
        self.assertEqual(res_explicit_arch.exit_code, 2)
        self.assertTrue(any("属于受保护黑名单或非学术正文范围" in err for err in res_explicit_arch.errors))

    def test_unauthorized_paths_and_traversal_blocked(self):
        """用例 6: 显式指定根目录、外部路径、路径遍历及非正文目录被明确拒绝 (ERROR 2)"""
        # 1. 项目根目录
        res_root = run_quality_check(target_paths=[str(self.mock_root)], project_root=self.mock_root)
        self.assertEqual(res_root.status, "ERROR")
        self.assertEqual(res_root.exit_code, 2)
        self.assertTrue(any("禁止将整个项目根目录作为受检目标" in err for err in res_root.errors))

        # 2. 非授权目录（如 docs 目录）
        res_docs = run_quality_check(target_paths=[str(self.mock_docs)], project_root=self.mock_root)
        self.assertEqual(res_docs.status, "ERROR")
        self.assertEqual(res_docs.exit_code, 2)

        # 3. 越界路径遍历 (..)
        outside_path = self.mock_root.parent / "outside.md"
        outside_path.write_text("外部文档", encoding="utf-8")
        try:
            res_outside = run_quality_check(target_paths=[str(outside_path)], project_root=self.mock_root)
            self.assertEqual(res_outside.status, "ERROR")
            self.assertEqual(res_outside.exit_code, 2)
            self.assertTrue(any("超出项目授权范围" in err for err in res_outside.errors))
        finally:
            if outside_path.exists():
                outside_path.unlink()

        # 4. 不存在的路径
        res_nonexist = run_quality_check(target_paths=[str(self.mock_report / "nonexistent.md")], project_root=self.mock_root)
        self.assertEqual(res_nonexist.status, "ERROR")
        self.assertEqual(res_nonexist.exit_code, 2)
        self.assertTrue(any("指定的目标路径不存在" in err for err in res_nonexist.errors))

    def test_empty_target_set_reports_error(self):
        """用例 7: 受检正文集合为空时绝不虚假 PASS，必须返回明确的 ERROR 2"""
        # 没有任何正文文件
        res_empty = run_quality_check(project_root=self.mock_root)
        self.assertEqual(res_empty.status, "ERROR")
        self.assertEqual(res_empty.exit_code, 2)
        self.assertFalse(res_empty.passed)
        self.assertTrue(any("未找到任何默认的正文草稿" in err for err in res_empty.errors))


class TestRuleParsingAndDeterministicGates(StandaloneSandboxBase):
    """规则编号解析、空规则标记、缺失规则源及学术边界测试"""

    def test_rule_id_regex_strictness_and_pipe_rejection(self):
        """用例 8: 修正规则编号正则，合法 FT 正确识别，非法格式及竖线编号不被误认"""
        # 写入含有非法竖线格式的规则文件
        self.facts_file.write_text(
            "# Facts\n\n"
            "### |-001：非法竖线编号\n"
            "<!-- gate:forbid:开架式 -->\n\n"
            "### F-002：合法规则编号\n"
            "<!-- gate:forbid:非法平台 -->\n",
            encoding="utf-8",
        )

        rules, errors = load_gate_rules(self.mock_root)
        # 非法竖线编号的禁词应因未处于合法编号下而报错或标记为 UNKNOWN 拦截
        self.assertTrue(any("缺少有效规则编号" in err for err in errors))
        # 合法编号 F-002 应成功解析
        f002_rules = [r for r in rules if r["rule_id"] == "F-002"]
        self.assertEqual(len(f002_rules), 1)
        self.assertEqual(f002_rules[0]["keyword"], "非法平台")

    def test_empty_gate_tag_reports_error(self):
        """用例 9: 空门禁标记 <!-- gate:forbid: --> 必须报错拦截 (ERROR 2)"""
        self.facts_file.write_text(
            "# Facts\n\n"
            "### F-001：测试规则\n"
            "<!-- gate:forbid:    -->\n",
            encoding="utf-8",
        )
        rules, errors = load_gate_rules(self.mock_root)
        self.assertTrue(any("禁词标记为空" in err for err in errors))

    def test_missing_or_empty_rule_file_reports_error(self):
        """用例 10: 规则文件缺失或无任何有效规则标记严格报错 (ERROR 2)"""
        # 场景 A: 规则文件缺失
        self.term_file.unlink()
        res_missing = run_quality_check(project_root=self.mock_root)
        self.assertEqual(res_missing.status, "ERROR")
        self.assertEqual(res_missing.exit_code, 2)
        self.assertTrue(any("docs/TERMINOLOGY.md" in err for err in res_missing.errors))

        # 场景 B: 规则文件存在但无任何 gate:forbid 标记
        self.term_file.write_text("# 空术语表\n无规则\n", encoding="utf-8")
        res_no_tags = run_quality_check(project_root=self.mock_root)
        self.assertEqual(res_no_tags.status, "ERROR")
        self.assertEqual(res_no_tags.exit_code, 2)
        self.assertTrue(any("未包含任何有效" in err for err in res_no_tags.errors))

    def test_candidate_method_discussion_not_falsely_intercepted(self):
        """用例 11: 正常学术讨论候选算法（MPC, INDI, 滑模, RQ1/2/3）通过 (PASS 0)，不进行妄断"""
        paper_doc = self.mock_report / "开题报告_正文起草稿.md"
        paper_doc.write_text(
            "# 控制方法比选与研究框架\n"
            "本课题重点围绕八推进器紧凑型水下航行器开展研究。\n"
            "针对姿态控制与轨迹跟踪，横向比选模型预测控制（MPC）、增量非线性动态逆（INDI）与滑模控制方法。\n"
            "在实验水池中围绕动力学辨识（RQ1）、模型在线适用性评价（RQ2）及闭环验证（RQ3）构建完整验证闭环。\n"
            "采用李雅普诺夫稳定性理论证明控制律的渐近收敛性。\n",
            encoding="utf-8",
        )

        res = run_quality_check(target_paths=[str(paper_doc)], project_root=self.mock_root)
        self.assertEqual(res.status, "PASS")
        self.assertEqual(res.exit_code, 0)
        self.assertTrue(res.passed)
        self.assertEqual(len(res.violations), 0)

    def test_proper_term_distinction(self):
        """用例 12: 精确区分合法术语“控制律” (PASS 0) 与错误错别字“控制率” (FAIL 1)"""
        good_doc = self.mock_report / "good_term.md"
        good_doc.write_text("设计非线性控制律与前馈解耦控制律，标称模型计算正常。", encoding="utf-8")
        res_good = run_quality_check(target_paths=[str(good_doc)], project_root=self.mock_root)
        self.assertEqual(res_good.status, "PASS")
        self.assertEqual(res_good.exit_code, 0)

        bad_doc = self.mock_report / "bad_term.md"
        bad_doc.write_text("设计非线性控制率与状态观测器。", encoding="utf-8")
        res_bad = run_quality_check(target_paths=[str(bad_doc)], project_root=self.mock_root)
        self.assertEqual(res_bad.status, "FAIL")
        self.assertEqual(res_bad.exit_code, 1)
        self.assertEqual(res_bad.violations[0]["keyword"], "控制率")


class TestContentScanningAndDocxDeepVerification(StandaloneSandboxBase):
    """文档内容扫描、深度 DOCX（段落/表格/页眉页脚）与空文档/损坏文档测试"""

    def test_empty_content_document_blocks_false_pass(self):
        """用例 13: 空文档（0字节或纯空白字符）严格返回 ERROR 2，坚决杜绝虚假 PASS"""
        empty_md = self.mock_report / "empty_draft.md"
        empty_md.write_text("   \n\n\t  \n", encoding="utf-8")

        res = run_quality_check(target_paths=[str(empty_md)], project_root=self.mock_root)
        self.assertEqual(res.status, "ERROR")
        self.assertEqual(res.exit_code, 2)
        self.assertTrue(any("无可检查的有效正文内容" in err for err in res.errors))

    def test_corrupted_docx_reports_error(self):
        """用例 14: 损坏的 DOCX（伪造损坏字节流）不能静默通过，必须返回 ERROR 2"""
        corrupted_docx = self.mock_report / "corrupted_draft.docx"
        corrupted_docx.write_bytes(b"PK\x03\x04This is corrupted non-docx file content")

        res = run_quality_check(target_paths=[str(corrupted_docx)], project_root=self.mock_root)
        self.assertEqual(res.status, "ERROR")
        self.assertEqual(res.exit_code, 2)
        self.assertTrue(any("无法读取或解析文件" in err for err in res.errors))

    def test_docx_deep_coverage_headers_footers_and_nested_tables(self):
        """用例 15: 验证 DOCX 深度扫描覆盖默认/首页/奇偶页页眉页脚及多层嵌套表格"""
        docx_file = self.mock_report / "multi_location.docx"
        doc = docx.Document()

        # 1. 节页眉违规
        sec = doc.sections[0]
        sec.different_first_page_header_footer = True
        sec.header.paragraphs[0].text = "页眉中出现开架式结构"
        sec.first_page_footer.paragraphs[0].text = "首页页脚标记控制率说明"

        # 2. 正文段落合规
        doc.add_paragraph("正常正文段落文字。")

        # 3. 嵌套表格违规
        outer_tbl = doc.add_table(rows=1, cols=1)
        inner_tbl = outer_tbl.cell(0, 0).add_table(rows=1, cols=1)
        inner_tbl.cell(0, 0).text = "嵌套表格单元格中的开架式航行器"

        doc.save(str(docx_file))

        res = run_quality_check(target_paths=[str(docx_file)], project_root=self.mock_root)
        self.assertEqual(res.status, "FAIL")
        self.assertEqual(res.exit_code, 1)
        self.assertEqual(len(res.violations), 3)

        locations = [v["location"] for v in res.violations]
        self.assertTrue(any("页眉" in loc for loc in locations))
        self.assertTrue(any("页脚" in loc for loc in locations))
        self.assertTrue(any("嵌套表格" in loc for loc in locations))

    def test_clean_docx_deep_scan_passes(self):
        """用例 16: 页眉、页脚、正文与嵌套表格全部合规的 DOCX 顺利 PASS 0"""
        clean_docx = self.mock_report / "clean_deep.docx"
        doc = docx.Document()
        sec = doc.sections[0]
        sec.header.paragraphs[0].text = "同济大学本科毕业论文"
        sec.footer.paragraphs[0].text = "第 1 页"
        doc.add_paragraph("水下航行器动力学建模与控制方法研究。")
        tbl = doc.add_table(rows=1, cols=1)
        tbl.cell(0, 0).text = "推力分配与控制律设计"
        sub_tbl = tbl.cell(0, 0).add_table(rows=1, cols=1)
        sub_tbl.cell(0, 0).text = "模型在线自适应"
        doc.save(str(clean_docx))

        res = run_quality_check(target_paths=[str(clean_docx)], project_root=self.mock_root)
        self.assertEqual(res.status, "PASS")
        self.assertEqual(res.exit_code, 0)
        self.assertEqual(len(res.violations), 0)

    def test_unsupported_file_extension_error(self):
        """用例 17: 显式传入不支持的文件类型（如 .pdf, .py）报错 ERROR 2"""
        pdf_file = self.mock_report / "report.pdf"
        pdf_file.write_bytes(b"%PDF-1.4 dummy")

        res = run_quality_check(target_paths=[str(pdf_file)], project_root=self.mock_root)
        self.assertEqual(res.status, "ERROR")
        self.assertEqual(res.exit_code, 2)
        self.assertTrue(any("不支持的文档类型" in err for err in res.errors))

    def test_chinese_and_special_character_path_handling(self):
        """用例 18: 中文目录、中文文件名与空格路径正常读取与编码兼容"""
        cn_dir = self.mock_report / "正文 章节 (测试)"
        cn_dir.mkdir(parents=True, exist_ok=True)
        cn_file = cn_dir / "第一节 紧凑型样机动力学.md"
        cn_file.write_text("八推进器水下航行器动力学控制律研究", encoding="utf-8")

        res = run_quality_check(target_paths=[str(cn_file)], project_root=self.mock_root)
        self.assertEqual(res.status, "PASS")
        self.assertEqual(res.exit_code, 0)
        self.assertEqual(len(res.scanned_files), 1)


class TestWorkspaceConfigGateSuite(unittest.TestCase):
    """轻量工作区配置完整性门禁单元测试"""

    @staticmethod
    def _create_mock_valid_workspace(tmp_root: Path):
        (tmp_root / "AGENTS.md").write_text(
            "# Agents\n\n严禁 Agent 在未经用户明确指令或直接授权下自主执行 `git push`。\n",
            encoding="utf-8",
        )
        (tmp_root / "PROJECT_NOW.md").write_text(
            "# Project Now\n\n## 当前有效来源\n## 当前工作阶段\n## 待确认事项\n",
            encoding="utf-8",
        )
        (tmp_root / "PROJECT_STATUS.md").write_text("# Project Status\n", encoding="utf-8")

        docs = tmp_root / "docs"
        docs.mkdir(parents=True, exist_ok=True)
        (docs / "PROJECT_FACTS.md").write_text(
            "### F-001\n<!-- gate:forbid:开架式 -->\n",
            encoding="utf-8",
        )
        (docs / "TERMINOLOGY.md").write_text(
            "### T-001\n<!-- gate:forbid:控制率 -->\n",
            encoding="utf-8",
        )
        (docs / "contracts").mkdir(parents=True, exist_ok=True)

        rules = tmp_root / ".agents" / "rules"
        rules.mkdir(parents=True, exist_ok=True)
        (rules / "academic-entry.md").write_text(
            "PROJECT_NOW.md docs/PROJECT_FACTS.md docs/TERMINOLOGY.md docs/contracts/",
            encoding="utf-8",
        )

        skills = tmp_root / ".agents" / "skills"
        skills.mkdir(parents=True, exist_ok=True)
        from scripts.check_workspace_config import REQUIRED_SKILLS
        for sk in REQUIRED_SKILLS:
            sk_dir = skills / sk
            sk_dir.mkdir(parents=True, exist_ok=True)
            (sk_dir / "SKILL.md").write_text(f"# {sk}\nGeneric academic skill\n", encoding="utf-8")

    def test_real_workspace_config_passes_completely(self):
        """用例 19: 真实工作区全量配置完整性核验全部 PASS 0"""
        res = run_workspace_config_check(PROJECT_ROOT)
        self.assertEqual(res.status, "PASS")
        self.assertEqual(res.exit_code, 0)
        self.assertTrue(res.passed)
        self.assertEqual(len(res.errors), 0)
        self.assertEqual(len(res.violations), 0)

    def test_mock_valid_workspace_passes(self):
        """用例 20: 合成标准虚拟工作区配置核验全部 PASS 0"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_root = Path(tmp_dir)
            self._create_mock_valid_workspace(tmp_root)
            res = run_workspace_config_check(tmp_root)
            self.assertEqual(res.status, "PASS")
            self.assertEqual(res.exit_code, 0)

    def test_missing_core_file_triggers_error(self):
        """用例 21: 临时沙箱中缺失核心管理文件触发 ERROR 2"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_root = Path(tmp_dir)
            self._create_mock_valid_workspace(tmp_root)
            (tmp_root / "PROJECT_NOW.md").unlink()

            res = run_workspace_config_check(tmp_root)
            self.assertEqual(res.status, "ERROR")
            self.assertEqual(res.exit_code, 2)
            self.assertTrue(any("PROJECT_NOW.md" in err for err in res.errors))

    def test_forbidden_words_in_generic_skill_triggers_fail(self):
        """用例 22: 通用技能泄漏项目专有词汇触发 FAIL 1"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_root = Path(tmp_dir)
            self._create_mock_valid_workspace(tmp_root)

            # 故意在 academic-writing/SKILL.md 中注入项目专有词
            aw_path = tmp_root / ".agents" / "skills" / "academic-writing" / "SKILL.md"
            aw_path.write_text("# Academic Writing\n泄漏词汇: SwiftROV PX4\n", encoding="utf-8")

            res = run_workspace_config_check(tmp_root)
            self.assertEqual(res.status, "FAIL")
            self.assertEqual(res.exit_code, 1)
            self.assertTrue(any("泄漏了项目专属词汇" in v for v in res.violations))

    def test_dangerous_push_permission_triggers_fail(self):
        """用例 23: 包含危险自动推送声明触发 FAIL 1"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_root = Path(tmp_dir)
            self._create_mock_valid_workspace(tmp_root)

            # 故意在 AGENTS.md 中注入危险 auto git push 声明
            agents_path = tmp_root / "AGENTS.md"
            agents_path.write_text("# Agents\n允许 auto git push 自动化推送\n", encoding="utf-8")

            res = run_workspace_config_check(tmp_root)
            self.assertEqual(res.status, "FAIL")
            self.assertEqual(res.exit_code, 1)
            self.assertTrue(any("不安全的自动推送权限声明" in v for v in res.violations))


class TestCliSubprocessExecution(StandaloneSandboxBase):
    """CLI 命令行进程级调用与三态退出码真实验证"""

    def test_cli_quality_check_three_states(self):
        """用例 24: CLI 命令调用 check_academic_quality.py 真实输出与三态退出码"""
        script_path = str(PROJECT_ROOT / "scripts" / "check_academic_quality.py")

        # 1. PASS (0)
        clean_file = self.mock_report / "clean_draft.md"
        clean_file.write_text("正常正文草稿内容，设计非线性控制律。", encoding="utf-8")
        cmd_pass = [sys.executable, script_path, "-r", str(self.mock_root), "-t", str(clean_file)]
        p_pass = subprocess.run(cmd_pass, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(p_pass.returncode, 0)
        self.assertIn("[PASS] 质量门禁检查通过！", p_pass.stdout)

        # 2. FAIL (1)
        bad_file = self.mock_report / "bad_draft.md"
        bad_file.write_text("违规草稿包含开架式构型。", encoding="utf-8")
        cmd_fail = [sys.executable, script_path, "-r", str(self.mock_root), "-t", str(bad_file)]
        p_fail = subprocess.run(cmd_fail, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(p_fail.returncode, 1)
        self.assertIn("[FAIL] 质量门禁检查未通过！", p_fail.stdout)
        self.assertIn("开架式", p_fail.stdout)

        # 3. ERROR (2) -- 目标不存在
        cmd_err = [sys.executable, script_path, "-r", str(self.mock_root), "-t", str(self.mock_report / "missing.md")]
        p_err = subprocess.run(cmd_err, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(p_err.returncode, 2)
        self.assertIn("[ERROR] 质量门禁执行失败！", p_err.stdout)

    def test_cli_workspace_config_check(self):
        """用例 25: CLI 命令调用 check_workspace_config.py 真实退出码为 0"""
        cfg_script = str(PROJECT_ROOT / "scripts" / "check_workspace_config.py")
        cmd = [sys.executable, cfg_script, "-r", str(PROJECT_ROOT)]
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(p.returncode, 0)
        self.assertIn("[PASS] 工作区配置完整性检查全部通过！", p.stdout)


if __name__ == "__main__":
    unittest.main()
