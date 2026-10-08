# -*- coding: utf-8 -*-
"""
scripts/check_academic_quality.py: 毕业论文写作质量门禁确定性检查脚本

功能：
1. 动态解析 docs/PROJECT_FACTS.md 与 docs/TERMINOLOGY.md 中的 <!-- gate:forbid:关键词 --> 门禁标记；
2. 针对指定或默认的学术正文草稿（支持 Markdown 与 Word OOXML DOCX）执行确定性违规扫描；
3. 严格执行白名单/黑名单过滤，绝不扫描规则文件、参考文献、历史档案或字典；
4. 实现 PASS(0) / FAIL(1) / ERROR(2) 确定性三态退出码：
   - 0 (PASS): 实际扫描 >= 1 个正文文件，未发现违规；
   - 1 (FAIL): 扫描完成，正文中发现阻断级违规词汇；
   - 2 (ERROR): 规则加载失败、指定目标不存在、零文件扫描、文件损坏或解码失败、路径越界等致命异常；
5. 显式输出生效规则清单与实际扫描的文件清单及数量。
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


class QualityCheckResult:
    """质量门禁执行结果对象，封装三态结果并支持元组解包 (passed, violations, rules)"""

    def __init__(self, status: str, violations: list, rules: list, scanned_files: list, errors: list):
        self.status = status  # "PASS", "FAIL", "ERROR"
        self.violations = violations
        self.rules = rules
        self.scanned_files = scanned_files
        self.errors = errors

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

    def __iter__(self):
        """兼容原有 (passed, violations, rules) 解包语法"""
        return iter((self.passed, self.violations, self.rules))


def load_gate_rules(project_root: Path):
    """
    从 docs/PROJECT_FACTS.md 与 docs/TERMINOLOGY.md 提取所有 <!-- gate:forbid:KEYWORD --> 规则
    返回: list of dict [{"keyword": ..., "rule_id": ..., "source_file": ..., "rule_line": ...}]
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
    try:
        rel = file_path.resolve().relative_to(project_root.resolve())
    except ValueError:
        # 不在 project_root 内部，视为黑名单/越界
        return True

    parts = rel.parts
    if not parts:
        return True
    # 顶层目录或文件在黑名单中
    if parts[0] in IGNORED_DIRS_AND_FILES:
        return True
    if file_path.name in IGNORED_DIRS_AND_FILES:
        return True
    # 临时或备份文件
    if file_path.suffix.lower() in [".bak", ".tmp", ".log"]:
        return True
    if file_path.name.startswith("~$"):
        return True
    return False


def extract_file_lines(file_path: Path):
    """
    从目标文件中提取文本行列表。
    - Markdown / Text: 按 UTF-8 解码提取行
    - DOCX: 按 Word OOXML 规范提取段落与表格文本
    返回: list of tuple (line_num or None, text, location_str)
    """
    ext = file_path.suffix.lower()
    if ext in [".md", ".txt"]:
        content = file_path.read_text(encoding="utf-8")
        lines = []
        for idx, line in enumerate(content.splitlines(), start=1):
            stripped = line.strip()
            if stripped:
                lines.append((idx, stripped, f"第 {idx} 行"))
        return lines

    elif ext == ".docx":
        import docx
        doc = docx.Document(str(file_path))
        lines = []
        for p_idx, p in enumerate(doc.paragraphs, start=1):
            t = p.text.strip()
            if t:
                lines.append((p_idx, t, f"段落 {p_idx}"))
        for t_idx, tbl in enumerate(doc.tables, start=1):
            for r_idx, row in enumerate(tbl.rows, start=1):
                for c_idx, cell in enumerate(row.cells, start=1):
                    t = cell.text.strip()
                    if t:
                        lines.append((None, t, f"表格 {t_idx} (行{r_idx}, 列{c_idx})"))
        return lines

    else:
        raise ValueError(f"不支持的文档类型: {ext} (仅支持 .md, .txt, .docx)")


def find_default_targets(project_root: Path):
    """
    查找默认需要受检的学术正文草稿及正式交付文件
    授权范围：开题报告目录下的正文起草稿、正文草稿 Markdown 以及正式/草稿 DOCX 文件
    排除：备份文件（.bak）、大纲规划、脚本、参考文献、历史任务书底稿
    """
    targets = []
    report_dir = project_root / "开题报告"
    if not report_dir.exists():
        return targets

    for p in report_dir.iterdir():
        if not p.is_file():
            continue
        if p.name.endswith(".bak") or p.name.startswith("~$"):
            continue
        # Markdown 正文草稿
        if p.suffix.lower() == ".md" and ("起草" in p.name or "草稿" in p.name):
            targets.append(p)
        # DOCX 正文与正式交付文件
        elif p.suffix.lower() == ".docx":
            # 扫描正式开题报告与草稿 DOCX，排除历史任务书底稿
            if ("开题报告" in p.name or "草稿" in p.name or "起草" in p.name) and not p.name.startswith("基于PX4"):
                targets.append(p)
    return sorted(targets)


def run_quality_check(target_paths=None, project_root=None) -> QualityCheckResult:
    """
    程序化执行质量门禁检查，返回确定性 QualityCheckResult 对象
    """
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    errors = []
    rules = load_gate_rules(project_root)
    if not rules:
        errors.append("未在 docs/ 中发现任何有效的 gate:forbid 门禁规则（或规则文件不存在）！")

    targets = []
    if target_paths:
        for p in target_paths:
            path_obj = Path(p).resolve()
            if not path_obj.exists():
                errors.append(f"指定的目标路径不存在: {p}")
                continue
            try:
                path_obj.relative_to(project_root.resolve())
            except ValueError:
                errors.append(f"目标路径超出项目授权范围: {p}")
                continue
            if is_blacklisted(path_obj, project_root):
                errors.append(f"目标路径属于受保护黑名单或非学术正文范围: {p}")
                continue
            if path_obj.is_file():
                targets.append(path_obj)
            elif path_obj.is_dir():
                found = []
                for f in path_obj.glob("**/*"):
                    if f.is_file() and not is_blacklisted(f, project_root):
                        if f.suffix.lower() in [".md", ".docx", ".txt"] and not f.name.endswith(".bak") and not f.name.startswith("~$"):
                            found.append(f)
                if not found:
                    errors.append(f"指定目录下未找到任何有效的正文文件: {p}")
                else:
                    targets.extend(found)
    else:
        targets = find_default_targets(project_root)
        if not targets:
            errors.append("在授权目录 [开题报告] 中未找到任何默认的正文草稿或交付文件！")

    # 去重并排序
    targets = sorted(list(set(targets)))

    if not targets and not errors:
        errors.append("受检正文文件集合为空（未实际扫描任何正文文件）！")

    all_violations = []
    scanned_files = []

    for target in targets:
        try:
            lines = extract_file_lines(target)
            scanned_files.append(target)
        except Exception as e:
            errors.append(f"无法读取或解析文件 {target}: {e}")
            continue

        for line_num, line_text, loc_desc in lines:
            for rule in rules:
                kw = rule["keyword"]
                if kw in line_text:
                    all_violations.append({
                        "file": target,
                        "location": loc_desc,
                        "line_num": line_num,
                        "content": line_text,
                        "keyword": kw,
                        "rule_id": rule["rule_id"],
                        "source": rule["source_file"],
                    })

    # 判定三态结果
    if errors:
        status = "ERROR"
    elif all_violations:
        status = "FAIL"
    elif scanned_files:
        status = "PASS"
    else:
        status = "ERROR"
        errors.append("实际扫描文件数量为 0！")

    return QualityCheckResult(status, all_violations, rules, scanned_files, errors)


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

    result = run_quality_check(args.target, project_root)

    print(f"[INFO] 已加载 {len(result.rules)} 条生效门禁规则:")
    for r in result.rules:
        print(f"  - [{r['rule_id']}] 严禁词: \"{r['keyword']}\" (来自 {r['source_file']})")
    print("--------------------------------------------------")

    if result.scanned_files:
        print(f"[INFO] 本次实际扫描正文文件 (共 {len(result.scanned_files)} 个):")
        for idx, f in enumerate(result.scanned_files, start=1):
            try:
                rel = f.relative_to(project_root)
            except ValueError:
                rel = f
            print(f"  {idx}. {rel}")
        print("--------------------------------------------------")

    if result.status == "PASS":
        print("\n[PASS] 质量门禁检查通过！")
        print(f"本次实际扫描 {len(result.scanned_files)} 个正文文件，未发现任何阻断级违规。\n")
        sys.exit(0)
    elif result.status == "FAIL":
        print(f"\n[FAIL] 质量门禁检查未通过！发现 {len(result.violations)} 处阻断级违规:\n")
        for idx, v in enumerate(result.violations, start=1):
            try:
                rel = v["file"].relative_to(project_root)
            except ValueError:
                rel = v["file"]
            print(f"  {idx}. [{v['rule_id']}] 命中禁词: \"{v['keyword']}\"")
            print(f"     文件: {rel}")
            print(f"     位置: {v['location']}")
            print(f"     正文摘录: \"{v['content']}\"")
            print(f"     规则来源: docs/{v['source']}")
            print()
        print("【整改要求】：请立即根据 docs/PROJECT_FACTS.md 与 docs/TERMINOLOGY.md 修正上述用词后再行提交验收！\n")
        sys.exit(1)
    else:  # ERROR
        print(f"\n[ERROR] 质量门禁执行失败！发现 {len(result.errors)} 处配置或系统致命异常:\n")
        for idx, err in enumerate(result.errors, start=1):
            print(f"  {idx}. {err}")
        print()
        sys.exit(2)


if __name__ == "__main__":
    main()
