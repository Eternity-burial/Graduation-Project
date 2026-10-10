# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open(r"开题报告/开题报告_正文起草稿.md", encoding="utf-8") as f:
    text = f.read()

body = text.split("## 三、毕业设计（论文）的主要参考文献")[0]

matches = re.findall(r"\[([0-9,\s\-–]+)\]", body)
first_appearance = {}
order_list = []
for m in matches:
    parts = re.split(r"[,，]", m)
    for p in parts:
        p = p.strip()
        if "-" in p or "–" in p:
            nums = [int(x) for x in re.split(r"[-–]", p) if x.strip()]
            for n in range(nums[0], nums[-1] + 1):
                if n not in first_appearance:
                    first_appearance[n] = len(order_list)
                    order_list.append(n)
        else:
            if p.isdigit():
                n = int(p)
                if n not in first_appearance:
                    first_appearance[n] = len(order_list)
                    order_list.append(n)

print(f"Total unique cited references in body: {len(first_appearance)}")
print("Order of first appearance:", order_list)

expected = list(range(1, 46))
assert order_list == expected, f"Order mismatch! Expected {expected}, got {order_list}"
print("Citation order is 100% strictly monotonically increasing from [1] to [45]!")

sec3 = text.split("## 三、毕业设计（论文）的主要参考文献")[1].split("## 四、审核意见")[0]
ref_lines = [l.strip() for l in sec3.splitlines() if l.strip().startswith("[")]
print(f"Total references in Section 3: {len(ref_lines)}")
assert len(ref_lines) == 45
print("Section 3 has exactly 45 references!")
