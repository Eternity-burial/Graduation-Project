# -*- coding: utf-8 -*-
"""
scripts/check_academic_quality.py: 毕业论文写作质量门禁确定性检查脚本

功能：
1. 动态解析 docs/PROJECT_FACTS.md 与 docs/TERMINOLOGY.md 中的 <!-- gate:forbid:关键词 --> 门禁标记；
2. 针对指定或默认的学术正文交付草稿执行严格阻断级违规扫描；
3. 严格执行白名单/黑名单过滤，绝不扫描规则文件、参考文献、历史档案或字典；
4. 输出违规行号与修复指引，返回确定性退出码（0: 通过，1: 存在违规）。
"""

import sys
import re
import argparse
from pathlib import Path

# 确保控制台 UTF-8 输出
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# 绝对排除扫描的路径或目录（黑名单，防止误扫规则与历史资产）
IGNORED_DIRS_AND_FILES = {
    ".git",
    ".agents",
    "docs",
    "参考",
    "资料",
    "模板",
    "PX4_INDI_Research",
    "选题",
    "AGENTS.md",
    "PROJECT_NOW.md",
    "PROJECT_STATUS.md",
    "references.bib",
    "references.ris",
}


def load_gate_rules(project_root: Path):
    """
    从 docs/PROJECT_FACTS.md 与 docs/TERMINOLOGY.md 提取所有 <!-- gate:forbid:KEYWORD --> 规则
    返回: list of dict [{"keyword": ..., "rule_id": ..., "source_file": ...}]
    """
    rules = []
    docs_dir = project_root / "docs"
    if not docs_dir.exists():
        return rules

    for doc_name in ["PROJECT_FACTS.md", "TERMINOLOGY.md"]:
        doc_path = docs_dir / doc_name
        if not doc_path.exists():
            continue

        content = doc_path.read_text(encoding="utf-8")
        lines = content.splitlines()
        current_id = "UNKNOWN"

        for idx, line in enumerate(lines, start=1):
            # 匹配形如 ### F-001： 或 ### T-001： 的编号
            id_match = re.match(r"^###\s+([F|T]-\d+)", line.strip())
            if id_match:
                current_id = id_match.group(1)

            # 匹配 <!-- gate:forbid:关键词 -->
            gate_match = re.search(r"<!--\s*gate:forbid:(.*?)\s*-->", line)
            if gate_match:
                keyword = gate_match.group(1).strip()
                if keyword:
                    rules.append({
                        "keyword": keyword,
                        "rule_id": current_id,
                        "source_file": doc_name,
                        "rule_line": idx,
                    })

    return rules


def is_blacklisted(file_path: Path, project_root: Path) -> bool:
    """检查文件是否位于严格忽略的黑名单路径中"""
    rel = file_path.resolve().relative_to(project_root.resolve())
    parts = rel.parts
    if not parts:
        return True
    # 顶层目录或文件在黑名单中
    if parts[0] in IGNORED_DIRS_AND_FILES:
        return True
    # 备份文件
    if file_path.suffix in [".bak", ".tmp", ".log"]:
        return True
    return False


def find_default_targets(project_root: Path):
    """查找默认需要受检的学术正文草稿文件"""
    targets = []
    report_dir = project_root / "开题报告"
    if report_dir.exists():
        for p in report_dir.glob("*.md"):
            if "起草" in p.name or "草稿" in p.name:
                if not p.name.endswith(".bak"):
                    targets.append(p)
    return targets


def scan_file(target_file: Path, rules: list):
    """
    扫描单一文件，返回违规记录列表
    """
    violations = []
    if not target_file.exists():
        return violations

    try:
        content = target_file.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[ERROR] 无法读取文件 {target_file}: {e}", file=sys.stderr)
        return violations

    lines = content.splitlines()
    for line_num, line in enumerate(lines, start=1):
        # 跳过空行或代码注释
        stripped = line.strip()
        if not stripped:
            continue

        for rule in rules:
            kw = rule["keyword"]
            if kw in line:
                violations.append({
                    "file": target_file,
                    "line_num": line_num,
                    "content": stripped,
                    "keyword": kw,
                    "rule_id": rule["rule_id"],
                    "source": rule["source_file"],
                })

    return violations


def run_quality_check(target_paths=None, project_root=None):
    """
    程序化执行质量门禁检查
    返回: (pass_status: bool, violations: list, rules: list)
    """
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    rules = load_gate_rules(project_root)
    if not rules:
        print("[WARN] 未在 docs/ 中发现任何 gate:forbid 门禁规则！")
        return True, [], []

    targets = []
    if target_paths:
        for p in target_paths:
            path_obj = Path(p).resolve()
            if not path_obj.exists():
                print(f"[WARN] 目标路径不存在，已跳过: {p}")
                continue
            if is_blacklisted(path_obj, project_root):
                print(f"[INFO] 路径在受保护黑名单中，依法跳过扫描: {p}")
                continue
            if path_obj.is_file():
                targets.append(path_obj)
            elif path_obj.is_dir():
                for f in path_obj.glob("**/*.md"):
                    if not is_blacklisted(f, project_root):
                        targets.append(f)
    else:
        targets = find_default_targets(project_root)

    all_violations = []
    for target in targets:
        v = scan_file(target, rules)
        all_violations.extend(v)

    passed = (len(all_violations) == 0)
    return passed, all_violations, rules


def main():
    parser = argparse.ArgumentParser(description="学术写作质量门禁确定性检查工具")
    parser.add_argument("--target", "-t", nargs="*", help="指定受检目标文件或目录（默认扫描开题报告正文草稿）")
    parser.add_argument("--root", "-r", default=None, help="指定项目根目录（可选）")
    args = parser.parse_args()

    project_root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent

    print(f"==================================================")
    print(f" 学术写作流程确定性质量门禁 (Quality Gate Check)")
    print(f" 根目录: {project_root}")
    print(f"==================================================")

    passed, violations, rules = run_quality_check(args.target, project_root)

    print(f"[INFO] 已加载 {len(rules)} 条生效门禁规则:")
    for r in rules:
        print(f"  - [{r['rule_id']}] 严禁词: \"{r['keyword']}\" (来自 {r['source_file']})")
    print("--------------------------------------------------")

    if not violations:
        print("\n[PASS] 质量门禁检查通过！")
        print("所有扫描草稿均符合项目有效事实与专业术语规范，未发现任何阻断级违规。\n")
        sys.exit(0)
    else:
        print(f"\n[FAIL] 质量门禁检查未通过！发现 {len(violations)} 处阻断级违规:\n")
        for idx, v in enumerate(violations, start=1):
            print(f"  {idx}. [{v['rule_id']}] 命中禁词: \"{v['keyword']}\"")
            print(f"     文件: {v['file']}")
            print(f"     行号: 第 {v['line_num']} 行")
            print(f"     正文摘录: \"{v['content']}\"")
            print(f"     规则来源: docs/{v['source']}")
            print()
        print("【整改要求】：请立即根据 docs/PROJECT_FACTS.md 与 docs/TERMINOLOGY.md 修正上述用词后再行提交验收！\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
