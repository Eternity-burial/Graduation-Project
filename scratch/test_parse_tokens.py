import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def parse_line_to_tokens(line):
    """
    Parses a line of markdown text into tokens:
    - ('MATH_INLINE', latex_code)
    - ('CITATION', cite_text) e.g. '[1]', '[26,27]'
    - ('BOLD', text)
    - ('TEXT', text)
    """
    # First, handle **$...$** -> make it MATH_INLINE
    # Replace **$...$** with $...$
    line = re.sub(r'\*\*\$([^$\n]+?)\$\*\*', r'$\1$', line)
    
    # Also standardize quotes to Chinese quotation marks where appropriate
    # but keep ASCII quotes if inside code/math
    # Now let's tokenize using regex
    # Tokens to match:
    # 1. Inline math: \$([^$\n]+?)\$
    # 2. Citations: \[\d+(?:[–\-,]\d+)*\]
    # 3. Bold: \*\*([^*]+?)\*\*
    # 4. Italic lead-in: \*(?:([^*]+?))\*
    
    pattern = re.compile(
        r'(\$[^$\n]+?\$|'                      # 1: inline math
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

# Test on complex lines
test_lines = [
    '《"十四五"机器人产业发展规划》[1]将水下探测、监测和作业机器人纳入特种机器人重点发展方向；',
    '其中，**$M = M_{RB} + M_A \in \mathbb{R}^{6\times6}$** 为含附加质量 $M_A$ 的系统惯性矩阵，$M_{RB}$ 为刚体质量矩阵；**$C(\nu) \in \mathbb{R}^{6\times6}$** 为科里奥利与向心矩阵',
    '*CFD 数值计算路线：* von Benzon 等[10]基于 OpenFOAM 对 BlueROV2 实施了全尺度 CFD 仿真',
    '为克服这一层间动态失配问题，学界探索了将推力分配约束上提至 MPC 优化层的一体化协同设计路线... Heshmati-Alamdari 等[26,27]的部分工作已向这一方向延伸。',
    '在**模型层**，以 BlueROV2 Heavy 八推进器全向构型为对象'
]

for l in test_lines:
    print('LINE:', l[:60])
    tokens = parse_line_to_tokens(l)
    for kind, val in tokens:
        print(f'   {kind:12s}: {val}')
