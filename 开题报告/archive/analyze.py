import re
import docx

def analyze():
    with open("build_comparison_docx.py", "r", encoding="utf-8") as f:
        code = f.read()

    # Find all OLD_
    old_vars = re.findall(r'(OLD_[A-Z0-9_]+)\s*=\s*"([^"]+)"', code)
    print("Old variables count:", len(old_vars))
    total_old = sum(len(v[1]) for v in old_vars if not v[0].endswith("HEAD"))
    print("Total old chars (excluding headings):", total_old)
    
    # Analyze sections
    old_sec = {"Lead": 0, "2.1": 0, "2.2": 0, "2.3": 0, "2.4": 0}
    for name, val in old_vars:
        if "LEAD" in name:
            old_sec["Lead"] += len(val)
        elif "2_1" in name and not name.endswith("HEAD"):
            old_sec["2.1"] += len(val)
        elif "2_2" in name and not name.endswith("HEAD"):
            old_sec["2.2"] += len(val)
        elif "2_3" in name and not name.endswith("HEAD"):
            old_sec["2.3"] += len(val)
        elif "2_4" in name and not name.endswith("HEAD"):
            old_sec["2.4"] += len(val)
            
    for k, v in old_sec.items():
        print(f"Old {k}: {v} chars")

    doc_clean = docx.Document(r"D:\tj\Graduation Project\开题报告\PX4研究现状_最新重构清洁版.docx")
    clean_paras = []
    started = False
    for p in doc_clean.paragraphs:
        t = p.text.strip()
        if "2．" in t or "2." in t or "国内外在该方向的研究现状" in t:
            started = True
        elif started and ("3．" in t or "3." in t or "主要研究内容" in t or "二、" in t):
            started = False
            break
        if started and t:
            clean_paras.append(t)

    new_sec = {"Lead": 0, "2.1": 0, "2.2": 0, "2.3": 0}
    current_sub = "Lead"
    for p in clean_paras:
        if p.startswith("2.1"):
            current_sub = "2.1"
            continue
        elif p.startswith("2.2"):
            current_sub = "2.2"
            continue
        elif p.startswith("2.3"):
            current_sub = "2.3"
            continue
        elif p.startswith("2．"):
            continue
        new_sec[current_sub] += len(p)

    print("\nNew sections char count:")
    for k, v in new_sec.items():
        print(f"New {k}: {v} chars")

    print("\nTotal clean sec2 chars (excluding headings):", sum(new_sec.values()))

if __name__ == "__main__":
    analyze()
