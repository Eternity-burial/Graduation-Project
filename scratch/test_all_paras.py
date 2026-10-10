import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def parse_line_to_tokens(line):
    # Normalize **$...$** to $...$
    line = re.sub(r'\*\*\$([^\$]+?)\$\*\*', r'$\1$', line)
    
    pattern = re.compile(
        r'(\$[^\$]+?\$|'                       # 1: inline math
        r'\[\d+(?:[–\-,]\s*\d+)*\]|'          # 2: citation
        r'\*\*[^*]+?\*\*|'                     # 3: bold
        r'(?<!\*)\*[^*]+?\*(?!\*))'           # 4: italic
    )
    
    raw_tokens = pattern.split(line)
    result = []
    for t in raw_tokens:
        if not t:
            continue
        if t.startswith('$') and t.endswith('$') and len(t) >= 2:
            result.append(('MATH_INLINE', t[1:-1].strip()))
        elif re.match(r'^\[\d+(?:[–\-,]\s*\d+)*\]$', t):
            result.append(('CITATION', t))
        elif t.startswith('**') and t.endswith('**') and len(t) >= 4:
            result.append(('BOLD', t[2:-2]))
        elif t.startswith('*') and t.endswith('*') and len(t) >= 2:
            result.append(('BOLD', t[1:-1]))
        else:
            result.append(('TEXT', t))
    return result

with open(r'c:\Users\Zhangwh\.gemini\antigravity\brain\aa6d7f65-5069-44a3-9da3-cee528067884\开题报告_融合版.md', 'r', encoding='utf-8') as f:
    text = f.read()

sec1 = text.split('## 一、毕业论文课题背景')[1].split('## 二、毕业论文方案介绍')[0]
paras = [p.strip() for p in sec1.split('\n\n') if p.strip() and not p.strip().startswith('---')]

total_math = 0
total_cite = 0
total_bold = 0
leaked_stars = []

for idx, p in enumerate(paras):
    if p.startswith('###') or p.startswith('####') or p.startswith('$$'):
        continue
    tokens = parse_line_to_tokens(p)
    reconstructed_text = ""
    for kind, val in tokens:
        if kind == 'MATH_INLINE':
            total_math += 1
            reconstructed_text += f"MATH({val})"
        elif kind == 'CITATION':
            total_cite += 1
            reconstructed_text += val
        elif kind == 'BOLD':
            total_bold += 1
            reconstructed_text += val
        elif kind == 'TEXT':
            reconstructed_text += val
            if '*' in val:
                leaked_stars.append((idx, val))

print(f'Total inline math: {total_math}')
print(f'Total citations: {total_cite}')
print(f'Total bold tokens: {total_bold}')
print(f'Leaked asterisks: {len(leaked_stars)}')
if leaked_stars:
    for item in leaked_stars:
        print('  LEAK:', item)
