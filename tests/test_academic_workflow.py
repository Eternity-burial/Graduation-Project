# -*- coding: utf-8 -*-
"""
tests/test_academic_workflow.py: 学术写作流程架构重构与质量门禁自动化验证套件
"""

import sys
import unittest
import subprocess
from pathlib import Path

# 确保控制台 UTF-8 输出
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.check_academic_quality import (
    load_gate_rules,
    scan_file,
    run_quality_check,
    is_blacklisted,
)


class TestAcademicWorkflowArchitecture(unittest.TestCase):
    """学术写作流程架构解耦与规范性验证"""

    def test_academic_writing_skill_is_strictly_generic(self):
        """用例 1: 验证 academic-writing/SKILL.md 彻底解耦，不含任何本项目特定词汇"""
        skill_path = PROJECT_ROOT / ".agents" / "skills" / "academic-writing" / "SKILL.md"
        self.assertTrue(skill_path.exists(), f"文件不存在: {skill_path}")
        content = skill_path.read_text(encoding="utf-8")

        # 课题专属硬件、算法、人员与机构黑名单
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

    def test_chapter_contract_single_source(self):
        """用例 2: 验证开题契约单一可信源位于 docs/contracts/，旧路径已安全重定向"""
        target_contract = PROJECT_ROOT / "docs" / "contracts" / "opening_report_contracts_and_evidence.md"
        self.assertTrue(target_contract.exists(), f"单一可信源契约不存在: {target_contract}")
        contract_text = target_contract.read_text(encoding="utf-8")
        self.assertIn("UC-01", contract_text, "契约未包含最新的未决主张 UC-01")
        self.assertIn("UC-02", contract_text, "契约未包含最新的未决主张 UC-02")
        self.assertIn("1.2.4", contract_text, "契约未包含最新的 1.2.4 章节划分")

        # 检查旧路径已置换为重定向声明，未丢失文件且未保留项目旧契约
        legacy_writing = PROJECT_ROOT / ".agents" / "skills" / "academic-writing" / "references" / "opening_report_contracts_and_evidence.md"
        self.assertTrue(legacy_writing.exists())
        legacy_writing_text = legacy_writing.read_text(encoding="utf-8")
        self.assertIn("已迁移", legacy_writing_text)
        self.assertNotIn("UC-01", legacy_writing_text)

        legacy_builder = PROJECT_ROOT / ".agents" / "skills" / "academic-doc-builder" / "references" / "opening_report_contracts_and_evidence.md"
        self.assertTrue(legacy_builder.exists())
        legacy_builder_text = legacy_builder.read_text(encoding="utf-8")
        self.assertIn("已迁移", legacy_builder_text)

    def test_facts_and_terminology_independence(self):
        """用例 3: 验证 PROJECT_FACTS.md 与 TERMINOLOGY.md 独立维护且包含 gate 标记"""
        facts_path = PROJECT_ROOT / "docs" / "PROJECT_FACTS.md"
        terms_path = PROJECT_ROOT / "docs" / "TERMINOLOGY.md"
        self.assertTrue(facts_path.exists())
        self.assertTrue(terms_path.exists())

        facts_text = facts_path.read_text(encoding="utf-8")
        terms_text = terms_path.read_text(encoding="utf-8")

        self.assertIn("<!-- gate:forbid:开架式 -->", facts_text)
        self.assertIn("<!-- gate:forbid:控制率 -->", terms_text)
        self.assertIn("F-001", facts_text)
        self.assertIn("T-001", terms_text)
        self.assertIn("PREFERENCE", terms_text)
        self.assertIn("CONTEXT", terms_text)

    def test_agents_rule_and_project_now_linkage(self):
        """用例 4: 验证 AGENTS.md 与 PROJECT_NOW.md 链接有效，无死链或冲突"""
        agents_path = PROJECT_ROOT / "AGENTS.md"
        now_path = PROJECT_ROOT / "PROJECT_NOW.md"
        entry_path = PROJECT_ROOT / ".agents" / "rules" / "academic-entry.md"

        agents_text = agents_path.read_text(encoding="utf-8")
        now_text = now_path.read_text(encoding="utf-8")
        entry_text = entry_path.read_text(encoding="utf-8")

        # AGENTS.md 必须引用 docs/contracts/ 与 PROJECT_NOW.md
        self.assertIn("docs/contracts/opening_report_contracts_and_evidence.md", agents_text)
        self.assertIn("PROJECT_NOW.md", agents_text)
        self.assertNotIn(".agents/skills/academic-writing/references/opening_report_contracts_and_evidence.md", agents_text)

        # academic-entry.md 必须引用 docs/contracts/ 与 PROJECT_NOW.md
        self.assertIn("PROJECT_NOW.md", entry_text)
        self.assertIn("docs/contracts/", entry_text)

        # PROJECT_NOW.md 必须引导至 docs/contracts/
        self.assertIn("docs/contracts/opening_report_contracts_and_evidence.md", now_text)


class TestQualityGateEnforcement(unittest.TestCase):
    """质量门禁脚本的功能与鲁棒性验证"""

    def test_quality_gate_detects_violations_and_exits_nonzero(self):
        """用例 5: 验证质量门禁脚本对包含违规用词的临时草稿能准确阻断并报出所有违规项"""
        mock_draft = PROJECT_ROOT / "开题报告" / "temp_mock_test_draft.md"
        bad_text = (
            "# 测试草稿\n"
            "第一行正常文字。\n"
            "本实验平台采用开架式结构构建。\n"
            "第三行正常文字。\n"
            "本章研究水下航行器的控制率算法。\n"
        )
        mock_draft.write_text(bad_text, encoding="utf-8")

        try:
            passed, violations, _ = run_quality_check(target_paths=[str(mock_draft)], project_root=PROJECT_ROOT)
            self.assertFalse(passed, "质量门禁未能拦截违规用词！")
            self.assertEqual(len(violations), 2, f"违规数量不符: {violations}")

            keywords_hit = [v["keyword"] for v in violations]
            self.assertIn("开架式", keywords_hit)
            self.assertIn("控制率", keywords_hit)

            line_nums = [v["line_num"] for v in violations]
            self.assertEqual(line_nums, [3, 5])
        finally:
            if mock_draft.exists():
                mock_draft.unlink()

    def test_quality_gate_ignores_blacklisted_rules_and_dictionaries(self):
        """用例 6: 验证黑名单机制有效，绝不误扫 docs/TERMINOLOGY.md 等规则自身"""
        # 测试黑名单判定函数
        term_file = PROJECT_ROOT / "docs" / "TERMINOLOGY.md"
        self.assertTrue(is_blacklisted(term_file, PROJECT_ROOT))

        agents_file = PROJECT_ROOT / "AGENTS.md"
        self.assertTrue(is_blacklisted(agents_file, PROJECT_ROOT))

        # 尝试显式传入黑名单文件，门禁应自动过滤，不报出违规
        passed, violations, _ = run_quality_check(target_paths=[str(term_file), str(agents_file)], project_root=PROJECT_ROOT)
        self.assertTrue(passed)
        self.assertEqual(len(violations), 0)

    def test_quality_gate_passes_on_current_active_drafts(self):
        """用例 7: 验证工作区现有的实际起草稿能顺利通过门禁检查"""
        passed, violations, rules = run_quality_check(project_root=PROJECT_ROOT)
        self.assertTrue(
            passed,
            f"现行正式草稿未通过门禁: {[v['content'] for v in violations]}",
        )
        self.assertGreaterEqual(len(rules), 2)


if __name__ == "__main__":
    unittest.main()
