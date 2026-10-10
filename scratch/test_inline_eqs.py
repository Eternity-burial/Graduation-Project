import sys, re
sys.stdout.reconfigure(encoding='utf-8')
import lxml.etree as etree
import latex2mathml.converter

xsl_path = r'C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL'
xslt = etree.parse(xsl_path)
transform = etree.XSLT(xslt)

def latex_to_omml(latex, is_display=False):
    mathml = latex2mathml.converter.convert(latex)
    dom = etree.fromstring(mathml)
    new_dom = transform(dom)
    return new_dom

with open(r'c:\Users\Zhangwh\.gemini\antigravity\brain\aa6d7f65-5069-44a3-9da3-cee528067884\开题报告_融合版.md', 'r', encoding='utf-8') as f:
    text = f.read()

no_disp = re.sub(r'\$\$[\s\S]*?\$\$', '', text)
inline_eqs = re.findall(r'\$([^$\n]+?)\$', no_disp)

print(f'Testing {len(inline_eqs)} inline formulas...')
for i, eq in enumerate(inline_eqs):
    try:
        omml = latex_to_omml(eq)
        # print(f'[{i+1}] OK: {eq}')
    except Exception as e:
        print(f'[{i+1}] FAILED: {eq} -> {e}')
print('All tests completed.')
