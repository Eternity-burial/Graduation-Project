import sys
sys.stdout.reconfigure(encoding='utf-8')
import docx
from docx.oxml import parse_xml
import lxml.etree as etree
import latex2mathml.converter

xsl_path = r'C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL'
xslt = etree.parse(xsl_path)
transform = etree.XSLT(xslt)

def latex_to_omml(latex, is_display=False):
    mathml = latex2mathml.converter.convert(latex)
    dom = etree.fromstring(mathml)
    new_dom = transform(dom)
    omml_str = etree.tostring(new_dom).decode('utf-8')
    if is_display:
        return parse_xml(f'<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">{omml_str}</m:oMathPara>')
    else:
        return parse_xml(omml_str)

eqs = [
    r'M\dot{\nu} + C(\nu)\nu + D(\nu)\nu + g(\eta) = \tau',
    r'u = B^+\tau_d = B^T(BB^T)^{-1}\tau_d',
    r'\min_{u} \quad \|Bu - \tau_d\|_W^2 + \gamma\|u\|^2 \quad \text{s.t.} \quad u_{min} \leq u \leq u_{max}'
]

for i, eq in enumerate(eqs):
    omml = latex_to_omml(eq, is_display=True)
    print(f'Eq {i+1} converted successfully, tag: {omml.tag}')
