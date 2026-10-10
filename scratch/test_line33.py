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

# Test on line 33 of the file
lines = text.splitlines()
line33 = lines[32] # 0-indexed
print('LINE 33:', line33[:60])
tokens = parse_line_to_tokens(line33)
for kind, val in tokens:
    if kind != 'TEXT':
        print(f'   {kind:12s}: {val}')
