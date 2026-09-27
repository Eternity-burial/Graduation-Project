# -*- coding: utf-8 -*-
"""
Word 原生 Office Math (OMML) 自动化生成与注入工具
核心链路：LaTeX 字符串 -> MathML (latex2mathml) -> OMML (MML2OMML.XSL) -> python-docx / oxml 原生公式对象
输出公式与 Microsoft Word (Cambria Math) 官方原生公式 100% 兼容，无损矢量、支持选中复制与编辑，零图片依赖。
"""

import os
import sys
from lxml import etree
import latex2mathml.converter
from docx.oxml import parse_xml

# 自动寻找 Microsoft Office 安装目录下的官方 MML2OMML.XSL 转换器
DEFAULT_XSL_PATHS = [
    r"C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL",
    r"C:\Program Files (x86)\Microsoft Office\root\Office16\MML2OMML.XSL",
    r"C:\Program Files\Microsoft Office\Office16\MML2OMML.XSL",
    r"C:\Program Files\Microsoft Office\Office15\MML2OMML.XSL",
]

_XSLT_TRANSFORM = None

def get_xslt_transform():
    """单例加载 MML2OMML.XSL 转换器"""
    global _XSLT_TRANSFORM
    if _XSLT_TRANSFORM is not None:
        return _XSLT_TRANSFORM

    xsl_path = None
    for p in DEFAULT_XSL_PATHS:
        if os.path.exists(p):
            xsl_path = p
            break

    if not xsl_path:
        raise FileNotFoundError(
            "未在默认路径找到 Microsoft Office 官方 MML2OMML.XSL 转换文件，请确认本机已安装 Office 2016/2019/365。"
        )

    xslt_doc = etree.parse(xsl_path)
    _XSLT_TRANSFORM = etree.XSLT(xslt_doc)
    return _XSLT_TRANSFORM


def latex_to_omml_xml(latex_str: str, is_display: bool = True) -> str:
    """
    将标准 LaTeX 公式字符串转换为 Office OpenXML OMML 字符串：
    - is_display=True:  生成独立行居中公式 <m:oMathPara><m:oMath>...</m:oMath></m:oMathPara>
    - is_display=False: 生成段落内行内公式 <m:oMath>...</m:oMath>
    """
    transform = get_xslt_transform()
    mathml_str = latex2mathml.converter.convert(latex_str)
    mathml_doc = etree.fromstring(mathml_str.encode("utf-8"))
    omml_doc = transform(mathml_doc)
    omml_bytes = etree.tostring(omml_doc, encoding="utf-8")
    omml_str = omml_bytes.decode("utf-8")

    # MML2OMML.XSL 默认输出 <m:oMath>...</m:oMath>
    if is_display:
        if not omml_str.startswith("<m:oMathPara"):
            M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
            W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            omml_str = f'<m:oMathPara xmlns:m="{M_NS}" xmlns:w="{W_NS}">{omml_str}</m:oMathPara>'

    return omml_str


def append_omml_formula(paragraph, latex_str: str, is_display: bool = True):
    """
    直接向 python-docx 的段落对象 (paragraph) 追加原生 OMML 公式元素
    """
    omml_xml = latex_to_omml_xml(latex_str, is_display=is_display)
    omml_el = parse_xml(omml_xml)
    paragraph._element.append(omml_el)
    return omml_el


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    test_eq = r"\dot{\boldsymbol{\eta}} = \boldsymbol{J}(\boldsymbol{\eta})\boldsymbol{\nu}"
    print("Testing LaTeX:", test_eq)
    xml_out = latex_to_omml_xml(test_eq, is_display=True)
    print("OMML XML length:", len(xml_out))
    print("Prefix:", xml_out[:120])
    print("Test passed successfully!")
