# -*- coding: utf-8 -*-
"""
开题报告参考文献双向互锁与完整性校验脚本
校验规则：
1. 提取开题报告正文（Section 1.1 及后续章节）全部上标/行内引用序号 [x]
2. 校验正文首次引用序号严格单调递增，无跳号、断号
3. 校验第三部分“参考文献”所列条目数与正文引用完全一致
4. 校验 references.bib 与 references.ris 词条数及 ID 100% 互锁对齐
"""
import re
import sys
import os
import docx

sys.stdout.reconfigure(encoding="utf-8")

DOCX_PATH = r"开题报告/基于PX4的水下航行器模型控制方法研究_开题报告.docx"
BIB_PATH  = r"开题报告/references.bib"
RIS_PATH  = r"开题报告/references.ris"

def verify():
    print("=" * 60)
    print(">>> 启动开题报告参考文献双向校验")
    print("=" * 60)

    # 1. 校验 Word 文档引用
    doc = docx.Document(DOCX_PATH)
    
    # 提取正文（在三、毕业设计（论文）的主要参考文献之前）
    body_paras = []
    sec3_paras = []
    in_sec3 = False
    in_sec4 = False

    for p in doc.paragraphs:
        t = p.text.strip()
        if "三、毕业设计（论文）的主要参考文献" in t:
            in_sec3 = True
            continue
        elif "四、审核意见" in t:
            in_sec4 = True
            in_sec3 = False
            continue
        
        if in_sec3:
            if t.startswith("["):
                sec3_paras.append(t)
        elif not in_sec4:
            if t:
                body_paras.append(t)

    body_text = "\n".join(body_paras)
    citations = re.findall(r"\[([0-9,\s\-–]+)\]", body_text)
    
    first_seen = {}
    order_list = []
    for c in citations:
        parts = re.split(r"[,，]", c)
        for part in parts:
            part = part.strip()
            if "-" in part or "–" in part:
                nums = [int(x) for x in re.split(r"[-–]", part) if x.strip()]
                for n in range(nums[0], nums[-1] + 1):
                    if n not in first_seen:
                        first_seen[n] = len(order_list)
                        order_list.append(n)
            elif part.isdigit():
                n = int(part)
                if n not in first_seen:
                    first_seen[n] = len(order_list)
                    order_list.append(n)

    print(f"正文实际引用文献数量: {len(order_list)}")
    print(f"正文首次引用顺序: {order_list}")
    expected_order = list(range(1, len(order_list) + 1))
    assert order_list == expected_order, f"引用顺序非严格递增！实际: {order_list}, 期望: {expected_order}"
    print("【校验 1 通过】正文引用顺序完全严格递增，无断号跳号！")

    print(f"第三部分参考文献列表条目数: {len(sec3_paras)}")
    assert len(sec3_paras) == len(order_list), f"参考文献列表数量 ({len(sec3_paras)}) 与正文引用 ({len(order_list)}) 不一致！"
    print("【校验 2 通过】第三部分参考文献列表与正文引用 100% 对应！")

    # 2. 校验 BibTeX 数据库
    with open(BIB_PATH, "r", encoding="utf-8") as f:
        bib_text = f.read()
    bib_entries = re.findall(r"@\w+\{([^,]+),", bib_text)
    print(f"references.bib 词条数: {len(bib_entries)}，词条ID: {bib_entries}")
    assert len(bib_entries) == len(order_list), f"BibTeX 词条数 ({len(bib_entries)}) 与正文引用数 ({len(order_list)}) 不一致！"
    print("【校验 3 通过】references.bib 词条与开题报告 100% 互锁！")

    # 3. 校验 RIS 数据库
    with open(RIS_PATH, "r", encoding="utf-8") as f:
        ris_text = f.read()
    ris_ids = re.findall(r"ID  - ([^\r\n]+)", ris_text)
    print(f"references.ris 词条数: {len(ris_ids)}，词条ID: {ris_ids}")
    assert len(ris_ids) == len(order_list), f"RIS 词条数 ({len(ris_ids)}) 与正文引用数 ({len(order_list)}) 不一致！"
    assert ris_ids == bib_entries, f"RIS 词条 ID 与 BibTeX 不一致！RIS: {ris_ids}, BIB: {bib_entries}"
    print("【校验 4 通过】references.ris 词条与 references.bib 100% 互锁对齐！")

    print("\n>>> 恭喜！参考文献体系（Word正文、Word列表、BibTeX、RIS）全部通过核验，100% 闭环一致！\n")

if __name__ == "__main__":
    verify()
