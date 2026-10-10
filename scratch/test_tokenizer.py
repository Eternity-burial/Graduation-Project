import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\Zhangwh\.gemini\antigravity\brain\aa6d7f65-5069-44a3-9da3-cee528067884\开题报告_融合版.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect paragraphs in Sec 1.1 and Sec 1.2
sec1 = text.split('## 一、毕业论文课题背景')[1].split('## 二、毕业论文方案介绍')[0]
paras = [p.strip() for p in sec1.split('\n\n') if p.strip() and not p.strip().startswith('---')]

for idx, p in enumerate(paras):
    print(f'P{idx:02d}: {p[:60]}...')
