# -*- coding: utf-8 -*-
"""
scripts/check_workspace_config.py: Antigravity 工作区配置完整性与安全性轻量检查脚本

定位与原则：
1. 专门核查工作区规则、Skills 入口、契约依赖、受控权限与配置解耦状态；
2. 独立于学术正文起草进度（即使尚未生成任何正文，配置检查亦能正常执行并判定）；
3. 遵循轻量原则，只验证当前有效配置与真实应该存在的本地引用，不引入复杂重型框架；
4. 严格三态退出码：
   - PASS (0): 工作区有效配置、核心文档、Skills 与门禁规则完整合规；
   - FAIL (1): 发现明确的配置违规（如通用技能泄漏项目专有词、危险的自动推送授权等）；
   - ERROR (2): 必需的核心配置文件缺失、损坏或无法解析。
"""

import sys
import re
import argparse
from pathlib import Path

# 确保控制台 UTF-8 输出
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# 通用写作技能严禁泄漏的项目专有词汇清单
FORBIDDEN_PROJECT_WORDS_IN_GENERIC_SKILLS = [
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

# 核心管理与规则文档
CORE_MANAGEMENT_FILES = [
    "AGENTS.md",
    "PROJECT_NOW.md",
    "PROJECT_STATUS.md",
]

# 必需的 Skills 清单及其入口
REQUIRED_SKILLS = [
    "academic-writing",
    "academic-doc-builder",
    "drawio-reconstruction",
    "paper-translation-reader",
    "paper-framework-figure-studio-pro",
]


class ConfigCheckResult:
    """工作区配置检查结果对象"""

    def __init__(self, status: str, checks: list, errors: list, violations: list, warnings: list):
        self.status = status  # "PASS", "FAIL", "ERROR"
        self.checks = checks
        self.errors = errors
        self.violations = violations
        self.warnings = warnings

    @property
    def passed(self) -> bool:
        return self.status == "PASS"

    @property
    def exit_code(self) -> int:
        if self.status == "PASS":
            return 0
        elif self.status == "FAIL":
            return 1
        else:
            return 2


def run_workspace_config_check(project_root=None) -> ConfigCheckResult:
    """执行工作区配置完整性、有效性与安全性检查"""
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_root = Path(project_root).resolve()
    checks = []
    errors = []
    violations = []
    warnings = []

    # -------------------------------------------------------------
    # 检查 1: 核心管理文档存在性与基本内容完整性
    # -------------------------------------------------------------
    core_missing = []
    for f_name in CORE_MANAGEMENT_FILES:
        f_path = project_root / f_name
        if not f_path.exists() or not f_path.is_file():
            core_missing.append(f_name)

    if core_missing:
        errors.append(f"核心管理文件缺失: {', '.join(core_missing)}")
        checks.append(("核心管理文件存在性", False, f"缺失: {core_missing}"))
    else:
        # 校验 PROJECT_NOW.md 包含必要小节
        now_content = (project_root / "PROJECT_NOW.md").read_text(encoding="utf-8")
        req_sections = ["当前有效来源", "当前工作阶段", "待确认事项"]
        missing_sec = [s for s in req_sections if s not in now_content]
        if missing_sec:
            errors.append(f"PROJECT_NOW.md 缺少必要结构节: {missing_sec}")
            checks.append(("核心管理文件存在性", False, f"PROJECT_NOW 缺少节: {missing_sec}"))
        else:
            checks.append(("核心管理文件存在性", True, "AGENTS.md, PROJECT_NOW.md, PROJECT_STATUS.md 完整"))

    # -------------------------------------------------------------
    # 检查 2: 学术任务规则入口与本地引用有效性
    # -------------------------------------------------------------
    rule_entry_file = project_root / ".agents" / "rules" / "academic-entry.md"
    if not rule_entry_file.exists():
        errors.append("学术任务接入规则缺失: .agents/rules/academic-entry.md")
        checks.append(("学术任务规则接入点", False, "academic-entry.md 缺失"))
    else:
        entry_content = rule_entry_file.read_text(encoding="utf-8")
        # 检查其引用的本地核心文档是否有效存在
        referenced_paths = [
            "PROJECT_NOW.md",
            "docs/PROJECT_FACTS.md",
            "docs/TERMINOLOGY.md",
            "docs/contracts/",
        ]
        broken_refs = []
        for ref in referenced_paths:
            target = project_root / ref
            if not target.exists():
                broken_refs.append(ref)

        if broken_refs:
            errors.append(f"academic-entry.md 引用的本地路径不存在: {broken_refs}")
            checks.append(("学术任务规则引用完整性", False, f"失效引用: {broken_refs}"))
        else:
            checks.append(("学术任务规则引用完整性", True, "本地引用路径全部有效"))

    # -------------------------------------------------------------
    # 检查 3: 必需质量门禁规则源与标记解析
    # -------------------------------------------------------------
    facts_path = project_root / "docs" / "PROJECT_FACTS.md"
    term_path = project_root / "docs" / "TERMINOLOGY.md"

    if not facts_path.exists() or not term_path.exists():
        errors.append("docs/PROJECT_FACTS.md 或 docs/TERMINOLOGY.md 不存在")
        checks.append(("门禁规则源文件存在性", False, "缺少门禁源文件"))
    else:
        # 解析门禁标记
        facts_text = facts_path.read_text(encoding="utf-8")
        term_text = term_path.read_text(encoding="utf-8")

        facts_tags = re.findall(r"<!--\s*gate:forbid:(.*?)\s*-->", facts_text)
        term_tags = re.findall(r"<!--\s*gate:forbid:(.*?)\s*-->", term_text)

        if not facts_tags:
            errors.append("docs/PROJECT_FACTS.md 未包含任何 <!-- gate:forbid:... --> 规则")
        if not term_tags:
            errors.append("docs/TERMINOLOGY.md 未包含任何 <!-- gate:forbid:... --> 规则")

        if facts_tags and term_tags:
            checks.append(("门禁规则源有效标记", True, f"已解析 {len(facts_tags) + len(term_tags)} 个门禁规则标记"))
        else:
            checks.append(("门禁规则源有效标记", False, "规则标记解析不完整"))

    # -------------------------------------------------------------
    # 检查 4: Skills 入口文件与规范性
    # -------------------------------------------------------------
    skills_dir = project_root / ".agents" / "skills"
    missing_skills = []
    for skill_name in REQUIRED_SKILLS:
        skill_file = skills_dir / skill_name / "SKILL.md"
        if not skill_file.exists():
            missing_skills.append(skill_name)

    if missing_skills:
        errors.append(f"必需技能缺失或入口不存在: {missing_skills}")
        checks.append(("Skills 入口完整性", False, f"缺失: {missing_skills}"))
    else:
        checks.append(("Skills 入口完整性", True, f"所有 {len(REQUIRED_SKILLS)} 个必需技能入口正常"))

    # -------------------------------------------------------------
    # 检查 5: 通用学术写作技能彻底解耦（零项目专有词泄漏）
    # -------------------------------------------------------------
    academic_writing_file = skills_dir / "academic-writing" / "SKILL.md"
    if academic_writing_file.exists():
        aw_text = academic_writing_file.read_text(encoding="utf-8")
        leaked = [w for w in FORBIDDEN_PROJECT_WORDS_IN_GENERIC_SKILLS if w in aw_text]
        if leaked:
            violations.append(f"academic-writing/SKILL.md 泄漏了项目专属词汇: {leaked}")
            checks.append(("通用写作技能解耦", False, f"泄漏词汇: {leaked}"))
        else:
            checks.append(("通用写作技能解耦", True, "零项目专属词汇泄漏"))
    else:
        # 已在检查 4 中记录缺失
        pass

    # -------------------------------------------------------------
    # 检查 6: 安全推送防护（严禁未经授权的自动 push 权限声明）
    # -------------------------------------------------------------
    agents_file = project_root / "AGENTS.md"
    if agents_file.exists():
        agents_text = agents_file.read_text(encoding="utf-8")
        # 必须显式声明禁止自主 git push
        if "严禁 Agent 在未经用户明确指令或直接授权下自主执行 `git push`" not in agents_text and "严禁" not in agents_text:
            warnings.append("AGENTS.md 中对 git push 权限的限制描述不够清晰")

        # 检查是否包含危险的自动推送放权关键字
        dangerous_patterns = [
            r"auto\s+git\s+push",
            r"自动推送至远程",
            r"unattended\s+push",
            r"git\s+push\s+--force",
        ]
        has_dangerous = False
        for pat in dangerous_patterns:
            if re.search(pat, agents_text, re.IGNORECASE):
                violations.append(f"AGENTS.md 发现了不安全的自动推送权限声明: {pat}")
                has_dangerous = True

        if not has_dangerous:
            checks.append(("安全推送防护权限", True, "未发现危险自动推送放权，权限严格受控"))
        else:
            checks.append(("安全推送防护权限", False, "存在危险推送声明"))

    # -------------------------------------------------------------
    # 检查 7: 活跃配置未重新引入已作废的旧前端或旧路径
    # -------------------------------------------------------------
    now_file = project_root / "PROJECT_NOW.md"
    if now_file.exists():
        now_text = now_file.read_text(encoding="utf-8")
        # 检查是否误把旧版开题报告全量草稿声明为有效活跃文件
        if "开题报告_全文草稿.md" in now_text:
            violations.append("PROJECT_NOW.md 中误包含了已物理隔离的作废文件 开题报告_全文草稿.md")
            checks.append(("旧版作废资产隔离", False, "PROJECT_NOW.md 包含作废草稿引用"))
        else:
            checks.append(("旧版作废资产隔离", True, "活跃配置未引入已隔离废弃文件"))

    # 判定三态结果
    if errors:
        status = "ERROR"
    elif violations:
        status = "FAIL"
    else:
        status = "PASS"

    return ConfigCheckResult(status, checks, errors, violations, warnings)


def main():
    parser = argparse.ArgumentParser(description="Antigravity 工作区配置完整性与安全性轻量检查工具")
    parser.add_argument("--root", "-r", default=None, help="指定项目根目录（可选，默认当前仓库根目录）")
    args = parser.parse_args()

    project_root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent

    print("==================================================")
    print(" Antigravity 工作区配置完整性门禁 (Workspace Config Gate)")
    print(f" 根目录: {project_root}")
    print("==================================================")

    res = run_workspace_config_check(project_root)

    print(f"[INFO] 已执行 {len(res.checks)} 项配置与安全性核验:")
    for name, passed, detail in res.checks:
        mark = "[PASS]" if passed else "[FAIL]"
        print(f"  {mark} {name}: {detail}")
    print("--------------------------------------------------")

    if res.warnings:
        print(f"[WARN] 提示信息 (共 {len(res.warnings)} 条):")
        for w in res.warnings:
            print(f"  - {w}")
        print("--------------------------------------------------")

    if res.status == "PASS":
        print("\n[PASS] 工作区配置完整性检查全部通过！")
        print("核心管理文档、学术接入规则、Skills 拓扑与门禁配置状态良好。\n")
        sys.exit(0)
    elif res.status == "FAIL":
        print(f"\n[FAIL] 工作区配置检查未通过！发现 {len(res.violations)} 处配置违规:\n")
        for idx, v in enumerate(res.violations, start=1):
            print(f"  {idx}. {v}")
        print("\n【整改要求】：请立即修正上述配置违规！\n")
        sys.exit(1)
    else:  # ERROR
        print(f"\n[ERROR] 工作区配置检查失败！发现 {len(res.errors)} 处关键文件缺失或解析异常:\n")
        for idx, err in enumerate(res.errors, start=1):
            print(f"  {idx}. {err}")
        print()
        sys.exit(2)


if __name__ == "__main__":
    main()
