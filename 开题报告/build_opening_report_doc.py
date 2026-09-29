# -*- coding: utf-8 -*-
"""
自动化构建《基于PX4的水下航行器模型控制方法研究》本科毕业论文开题报告 (.docx 与 .doc)
同时生成：
1. 正式提交纯净版：开题报告-基于PX4的水下航行器模型控制方法研究 (.docx / .doc) —— 100% 无高亮
2. 新旧修改对比版：开题报告-新旧版本修改对比版_逐段差异高亮 (.docx / .doc) —— 黄色高亮标注所有新增/优化内容

严格遵循官方模板《2毕业设计(论文)开题报告.docx》的底层 XML 样式表与学术规范：
1. 毕设类型统一为：毕业论文
2. 模板原生样式绑定与段间距规范：
   - 一级标题 (h1)：Normal 样式，四号(14pt)黑体，首行缩进2字符(w:firstLine="560")，1.5倍行距，段前0.5行、段后0.5行
   - 二级标题 (h2)：挂载模板内置“条”(a6)样式，小四号(12pt)黑体，顶格无缩进，序号与题名空一格，1.5倍行距，段前0.5行、段后0.5行
   - 三级标题 (h3)：挂载模板内置“正文格式”(a7)样式，小四号(12pt)黑体，首行缩进2字符，1.5倍行距，无段前段后间距
   - 正文段落 (body)：挂载模板内置“正文格式”(a7)样式，中文宋体、西文 Times New Roman，小四号(12pt)，首行缩进2字符，1.5倍行距，无段前段后间距
   - 参考文献 (ref)：挂载模板内置“参考文献”(a9)样式，小四号(12pt)，1.5倍行距，悬挂缩进0.74cm(420 dxa)，无段前段后间距
3. 数学公式：全部采用 Word 原生 OMML (m:oMath / m:oMathPara, Cambria Math) 渲染，区分矩阵粗斜体(bi)、标量斜体(i)与算子正体(p)
4. 参考文献引用：支持 GB/T 7714-2015 顺序编码自动校验 ([1]~[20])、Word 原生书签 (_Ref_Paper_i) 与可点击跳转的上标角标 [i]
"""

import os
import re
import sys
import shutil
import docx
from lxml import etree
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"D:\tj\Graduation Project"
TEMPLATE_PATH = os.path.join(BASE_DIR, "模板", "2毕业设计(论文)开题报告.docx")
OUT_DIR = os.path.join(BASE_DIR, "开题报告")
ARCHIVE_DIR = os.path.join(OUT_DIR, "归档")
DIFF_HISTORY_DIR = os.path.join(ARCHIVE_DIR, "历次修改对比版")
DOC_ARCHIVE_DIR = os.path.join(ARCHIVE_DIR, "历史DOC版本")
os.makedirs(DIFF_HISTORY_DIR, exist_ok=True)
os.makedirs(DOC_ARCHIVE_DIR, exist_ok=True)

OUT_DOCX = os.path.join(OUT_DIR, "开题报告-基于PX4的水下航行器模型控制方法研究.docx")
OUT_DOC = os.path.join(DOC_ARCHIVE_DIR, "开题报告-基于PX4的水下航行器模型控制方法研究.doc")

DIFF_DOCX = os.path.join(OUT_DIR, "开题报告-新旧版本修改对比版_逐段差异高亮.docx")
DIFF_DOC = os.path.join(DOC_ARCHIVE_DIR, "开题报告-新旧版本修改对比版_逐段差异高亮.doc")

SENIOR_DOCX = os.path.join(OUT_DIR, "开题报告-实验室学长审阅确认版.docx")

FIG1_LIT_PATH = os.path.join(OUT_DIR, "figures", "fig1_lit_control_architecture.png")
FIG2_ROV_PATH = os.path.join(OUT_DIR, "figures", "fig0_rov_coord_thrusters.png")
FIG3_ROADMAP_PATH = os.path.join(OUT_DIR, "figures", "fig1_technical_roadmap.png")
FIG4_PX4_PATH = os.path.join(OUT_DIR, "figures", "fig2_px4_rov_architecture.png")

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"


# ==============================================================================
# 一、 Word 原生 OMML 数学公式构造器 (Cambria Math)
# ==============================================================================

def _m_run(text, sty="i", highlight=False):
    """
    生成 OMML <m:r> 节点片段:
    sty: 'bi' (粗斜体, 用于矩阵/矢量), 'i' (斜体, 用于标量), 'p' (正体, 用于括号/运算符/常量下标)
    """
    esc = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    sty_xml = f'<m:rPr><m:sty m:val="{sty}"/></m:rPr>' if sty else ""
    hl_xml = '<w:highlight w:val="yellow"/>' if highlight else ""
    return (
        f"<m:r>{sty_xml}"
        f'<w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:eastAsia="宋体"/>'
        f'<w:sz w:val="24"/><w:szCs w:val="24"/>{hl_xml}</w:rPr>'
        f"<m:t>{esc}</m:t></m:r>"
    )


def _m_sub(base_xml, sub_xml):
    """下标结构 <m:sSub>"""
    return f"<m:sSub><m:e>{base_xml}</m:e><m:sub>{sub_xml}</m:sub></m:sSub>"


def _m_sup(base_xml, sup_xml):
    """上标结构 <m:sSup>"""
    return f"<m:sSup><m:e>{base_xml}</m:e><m:sup>{sup_xml}</m:sup></m:sSup>"


def _m_acc(base_xml, chr_val="&#x0307;"):
    """顶标结构 <m:acc>: 默认 &#x0307; 为一阶导数点 (dot)，&#x0302; 为估计值帽号 (hat)"""
    return (
        f"<m:acc><m:accPr><m:chr m:val=\"{chr_val}\"/></m:accPr>"
        f"<m:e>{base_xml}</m:e></m:acc>"
    )


def _m_col_vec2(row1_xml, row2_xml):
    """2x1 括号列向量结构 <m:d><m:m>...</m:m></m:d>"""
    return (
        '<m:d><m:dPr><m:begChr m:val="["/><m:endChr m:val="]"/></m:dPr>'
        "<m:e><m:m>"
        "<m:mPr><m:mcs><m:mc><m:mcPr><m:count m:val=\"1\"/><m:mcJc m:val=\"center\"/></m:mcPr></m:mc></m:mcs></m:mPr>"
        f"<m:mr><m:e>{row1_xml}</m:e></m:mr>"
        f"<m:mr><m:e>{row2_xml}</m:e></m:mr>"
        "</m:m></m:e></m:d>"
    )


# 预定义行内与独立 OMML 公式字典
INLINE_MATH_XML = {
    "tau_c_R6": (
        _m_sub(_m_run("τ", "bi"), _m_run("c", "i"))
        + _m_run(" ∈ ", "p")
        + _m_sup(_m_run("ℝ", "p"), _m_run("6", "p"))
    ),
    "T_R8": (
        _m_run("T", "bi")
        + _m_run(" ∈ ", "p")
        + _m_sup(_m_run("ℝ", "p"), _m_run("8", "p"))
    ),
    "6x8": _m_run("6 × 8", "p"),
    "n_coord": (
        _m_run("{", "p") + _m_run("n", "i") + _m_run("}(", "p")
        + _m_sub(_m_run("O", "i"), _m_run("n", "i")) + _m_run("-", "p")
        + _m_sub(_m_run("x", "i"), _m_run("n", "i"))
        + _m_sub(_m_run("y", "i"), _m_run("n", "i"))
        + _m_sub(_m_run("z", "i"), _m_run("n", "i"))
        + _m_run(")", "p")
    ),
    "b_coord": (
        _m_run("{", "p") + _m_run("b", "i") + _m_run("}(", "p")
        + _m_sub(_m_run("O", "i"), _m_run("b", "i")) + _m_run("-", "p")
        + _m_sub(_m_run("x", "i"), _m_run("b", "i"))
        + _m_sub(_m_run("y", "i"), _m_run("b", "i"))
        + _m_sub(_m_run("z", "i"), _m_run("b", "i"))
        + _m_run(")", "p")
    ),
    "eta_def": (
        _m_run("η", "bi")
        + _m_run(" = [", "p")
        + _m_run("x", "i") + _m_run(", ", "p")
        + _m_run("y", "i") + _m_run(", ", "p")
        + _m_run("z", "i") + _m_run(", ", "p")
        + _m_run("ϕ", "i") + _m_run(", ", "p")
        + _m_run("θ", "i") + _m_run(", ", "p")
        + _m_run("ψ", "i")
        + _m_sup(_m_run("]", "p"), _m_run("T", "p"))
    ),
    "nu_def": (
        _m_run("ν", "bi")
        + _m_run(" = [", "p")
        + _m_run("u", "i") + _m_run(", ", "p")
        + _m_run("v", "i") + _m_run(", ", "p")
        + _m_run("w", "i") + _m_run(", ", "p")
        + _m_run("p", "i") + _m_run(", ", "p")
        + _m_run("q", "i") + _m_run(", ", "p")
        + _m_run("r", "i")
        + _m_sup(_m_run("]", "p"), _m_run("T", "p"))
    ),
    "J_eta": _m_run("J", "bi") + _m_run("(", "p") + _m_run("η", "bi") + _m_run(")", "p"),
    "M_sum": (
        _m_run("M", "bi")
        + _m_run(" = ", "p")
        + _m_sub(_m_run("M", "bi"), _m_run("RB", "p"))
        + _m_run(" + ", "p")
        + _m_sub(_m_run("M", "bi"), _m_run("A", "p"))
    ),
    "M_RB": _m_sub(_m_run("M", "bi"), _m_run("RB", "p")),
    "M_A": _m_sub(_m_run("M", "bi"), _m_run("A", "p")),
    "C_nu": _m_run("C", "bi") + _m_run("(", "p") + _m_run("ν", "bi") + _m_run(")", "p"),
    "D_nu": _m_run("D", "bi") + _m_run("(", "p") + _m_run("ν", "bi") + _m_run(")", "p"),
    "g_eta": _m_run("g", "bi") + _m_run("(", "p") + _m_run("η", "bi") + _m_run(")", "p"),
    "tau": _m_run("τ", "bi"),
    "tau_d": _m_sub(_m_run("τ", "bi"), _m_run("d", "i")),
    "theta_vec": _m_run("θ", "bi"),
    "eta_r": _m_sub(_m_run("η", "bi"), _m_run("r", "i")),
    "nu_r": _m_sub(_m_run("ν", "bi"), _m_run("r", "i")),
    "e_eta": _m_sub(_m_run("e", "bi"), _m_run("η", "i")),
    "e_eta_def": (
        _m_sub(_m_run("e", "bi"), _m_run("η", "i"))
        + _m_run(" = ", "p")
        + _m_sub(_m_run("η", "bi"), _m_run("r", "i"))
        + _m_run(" − ", "p")
        + _m_run("η", "bi")
    ),
    "e_nu_def": (
        _m_sub(_m_run("e", "bi"), _m_run("ν", "i"))
        + _m_run(" = ", "p")
        + _m_sub(_m_run("ν", "bi"), _m_run("r", "i"))
        + _m_run(" − ", "p")
        + _m_run("ν", "bi")
    ),
    "model_hats": (
        _m_acc(_m_run("M", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_acc(_m_run("C", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_acc(_m_run("D", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_acc(_m_run("g", "bi"), "&#x0302;")
    ),
    "model_hats_paren": (
        _m_run("(", "p")
        + _m_acc(_m_run("M", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_acc(_m_run("C", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_acc(_m_run("D", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_acc(_m_run("g", "bi"), "&#x0302;")
        + _m_run(")", "p")
    ),
    "tau_c": _m_sub(_m_run("τ", "bi"), _m_run("c", "i")),
    "F_model": _m_sub(_m_run("F", "bi"), _m_run("model", "p")) + _m_run("(·)", "p"),
    "F_model_zero": _m_sub(_m_run("F", "bi"), _m_run("model", "p")) + _m_run("(·) = ", "p") + _m_run("0", "bi"),
    "F_fb": _m_sub(_m_run("F", "bi"), _m_run("fb", "p")) + _m_run("(·)", "p"),
    "T1_T4": _m_sub(_m_run("T", "i"), _m_run("1", "p")) + _m_run(" ~ ", "p") + _m_sub(_m_run("T", "i"), _m_run("4", "p")),
    "T5_T8": _m_sub(_m_run("T", "i"), _m_run("5", "p")) + _m_run(" ~ ", "p") + _m_sub(_m_run("T", "i"), _m_run("8", "p")),
    "i_idx": _m_run("i", "i"),
    "i_1_8": _m_run("i", "i") + _m_run(" = 1, …, 8", "p"),
    "r_i": _m_sub(_m_run("r", "bi"), _m_run("i", "i")),
    "d_i": _m_sub(_m_run("d", "bi"), _m_run("i", "i")),
    "r_i_R3": (
        _m_sub(_m_run("r", "bi"), _m_run("i", "i"))
        + _m_run(" ∈ ", "p")
        + _m_sup(_m_run("ℝ", "p"), _m_run("3", "p"))
    ),
    "d_i_R3": (
        _m_sub(_m_run("d", "bi"), _m_run("i", "i"))
        + _m_run(" ∈ ", "p")
        + _m_sup(_m_run("ℝ", "p"), _m_run("3", "p"))
    ),
    "B_mat": _m_run("B", "bi"),
    "B_def": (
        _m_run("B", "bi")
        + _m_run(" = [", "p")
        + _m_sub(_m_run("b", "bi"), _m_run("1", "p"))
        + _m_run(", ", "p")
        + _m_sub(_m_run("b", "bi"), _m_run("2", "p"))
        + _m_run(", …, ", "p")
        + _m_sub(_m_run("b", "bi"), _m_run("8", "p"))
        + _m_run("] ∈ ", "p")
        + _m_sup(_m_run("ℝ", "p"), _m_run("6×8", "p"))
    ),
    "T_bounds": (
        _m_sub(_m_run("T", "bi"), _m_run("min", "p"))
        + _m_run(" ≤ ", "p")
        + _m_run("T", "bi")
        + _m_run(" ≤ ", "p")
        + _m_sub(_m_run("T", "bi"), _m_run("max", "p"))
    ),
    "T_interval": (
        _m_run("[", "p")
        + _m_sub(_m_run("T", "bi"), _m_run("min", "p"))
        + _m_run(", ", "p")
        + _m_sub(_m_run("T", "bi"), _m_run("max", "p"))
        + _m_run("]", "p")
    ),
    "T_vec_def": (
        _m_run("T", "bi")
        + _m_run(" = [", "p")
        + _m_sub(_m_run("T", "i"), _m_run("1", "p"))
        + _m_run(", …, ", "p")
        + _m_sub(_m_run("T", "i"), _m_run("8", "p"))
        + _m_sup(_m_run("]", "p"), _m_run("T", "p"))
    ),
    "T_vec_R8": (
        _m_run("T", "bi")
        + _m_run(" = [", "p")
        + _m_sub(_m_run("T", "i"), _m_run("1", "p"))
        + _m_run(", …, ", "p")
        + _m_sub(_m_run("T", "i"), _m_run("8", "p"))
        + _m_sup(_m_run("]", "p"), _m_run("T", "p"))
        + _m_run(" ∈ ", "p")
        + _m_sup(_m_run("ℝ", "p"), _m_run("8", "p"))
    ),
    "e_tau": _m_sub(_m_run("e", "bi"), _m_run("τ", "i")),
    "e_tau_def": (
        _m_sub(_m_run("e", "bi"), _m_run("τ", "i"))
        + _m_run(" = ", "p")
        + _m_sub(_m_run("τ", "bi"), _m_run("c", "i"))
        + _m_run(" − ", "p")
        + _m_run("B", "bi")
        + _m_run("T", "bi")
    ),
}

DISPLAY_MATH_XML = {
    "eq1_6dof": (
        _m_acc(_m_run("η", "bi"), "&#x0307;")
        + _m_run(" = ", "p")
        + _m_run("J", "bi") + _m_run("(", "p") + _m_run("η", "bi") + _m_run(")", "p")
        + _m_run("ν", "bi")
        + _m_run(" ,    ", "p")
        + _m_run("M", "bi") + _m_acc(_m_run("ν", "bi"), "&#x0307;")
        + _m_run(" + ", "p")
        + _m_run("C", "bi") + _m_run("(", "p") + _m_run("ν", "bi") + _m_run(")", "p") + _m_run("ν", "bi")
        + _m_run(" + ", "p")
        + _m_run("D", "bi") + _m_run("(", "p") + _m_run("ν", "bi") + _m_run(")", "p") + _m_run("ν", "bi")
        + _m_run(" + ", "p")
        + _m_run("g", "bi") + _m_run("(", "p") + _m_run("η", "bi") + _m_run(")", "p")
        + _m_run(" = ", "p")
        + _m_run("τ", "bi")
        + _m_run(" + ", "p")
        + _m_sub(_m_run("τ", "bi"), _m_run("d", "i"))
        + _m_run("      (1)", "p")
    ),
    "eq2_ctrl": (
        _m_sub(_m_run("τ", "bi"), _m_run("c", "i"))
        + _m_run(" = ", "p")
        + _m_sub(_m_run("F", "bi"), _m_run("model", "p"))
        + _m_run("(", "p")
        + _m_acc(_m_run("M", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_acc(_m_run("C", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_acc(_m_run("D", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_acc(_m_run("g", "bi"), "&#x0302;") + _m_run(", ", "p")
        + _m_run("η", "bi") + _m_run(", ", "p")
        + _m_run("ν", "bi") + _m_run(", ", "p")
        + _m_sub(_m_run("η", "bi"), _m_run("r", "i")) + _m_run(", ", "p")
        + _m_sub(_m_run("ν", "bi"), _m_run("r", "i"))
        + _m_run(") + ", "p")
        + _m_sub(_m_run("F", "bi"), _m_run("fb", "p"))
        + _m_run("(", "p")
        + _m_sub(_m_run("e", "bi"), _m_run("η", "i")) + _m_run(", ", "p")
        + _m_sub(_m_run("e", "bi"), _m_run("ν", "i"))
        + _m_run(")      (2)", "p")
    ),
    "eq3_alloc": (
        _m_sub(_m_run("b", "bi"), _m_run("i", "i"))
        + _m_run(" = ", "p")
        + _m_col_vec2(
            _m_sub(_m_run("d", "bi"), _m_run("i", "i")),
            _m_sub(_m_run("r", "bi"), _m_run("i", "i"))
            + _m_run(" × ", "p")
            + _m_sub(_m_run("d", "bi"), _m_run("i", "i")),
        )
        + _m_run(" ∈ ", "p")
        + _m_sup(_m_run("ℝ", "p"), _m_run("6", "p"))
        + _m_run(" ,    ", "p")
        + _m_sub(_m_run("T", "bi"), _m_run("min", "p"))
        + _m_run(" ≤ ", "p")
        + _m_run("T", "bi")
        + _m_run(" ≤ ", "p")
        + _m_sub(_m_run("T", "bi"), _m_run("max", "p"))
        + _m_run(" ,    ", "p")
        + _m_sub(_m_run("e", "bi"), _m_run("τ", "i"))
        + _m_run(" = ", "p")
        + _m_sub(_m_run("τ", "bi"), _m_run("c", "i"))
        + _m_run(" − ", "p")
        + _m_run("B", "bi")
        + _m_run("T", "bi")
        + _m_run("      (3)", "p")
    ),
}


def _apply_omml_highlight(xml_str, highlight=False):
    """若需在对比版中高亮公式，为每个 <w:szCs .../> 后追加 <w:highlight w:val="yellow"/>"""
    if not highlight:
        return xml_str
    return xml_str.replace('<w:szCs w:val="24"/>', '<w:szCs w:val="24"/><w:highlight w:val="yellow"/>')


def append_inline_omath(p, math_key, highlight=False):
    """在段落 p 中追加行内原生 <m:oMath> 公式节点"""
    inner_xml = _apply_omml_highlight(INLINE_MATH_XML[math_key], highlight=highlight)
    omath_str = f'<m:oMath xmlns:m="{M_NS}" xmlns:w="{W_NS}">{inner_xml}</m:oMath>'
    p._element.append(etree.fromstring(omath_str))


def append_display_omath(p, eq_key, highlight=False):
    """在居中段落 p 中追加独立行原生 <m:oMathPara><m:oMath> 公式节点"""
    inner_xml = _apply_omml_highlight(DISPLAY_MATH_XML[eq_key], highlight=highlight)
    omath_para_str = (
        f'<m:oMathPara xmlns:m="{M_NS}" xmlns:w="{W_NS}">'
        f"<m:oMath>{inner_xml}</m:oMath>"
        f"</m:oMathPara>"
    )
    p._element.append(etree.fromstring(omath_para_str))


# ==============================================================================
# 二、 字体、段落样式与上标交叉引用构造器
# ==============================================================================

CITATION_TRACKER = []  # 记录正文中首次出现的文献编号顺序


def set_run_font(run, cn_font="宋体", en_font="Times New Roman", size_pt=12.0,
                 bold=False, italic=False, superscript=False, highlight=False):
    """设置 Run 的中西文字体、字号、粗斜体、上标、黑色字色及可选高亮"""
    run.font.name = en_font
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    run.font.superscript = superscript
    run.font.color.rgb = RGBColor(0, 0, 0)
    if highlight:
        run.font.highlight_color = WD_COLOR_INDEX.YELLOW
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    rFonts.set(qn("w:ascii"), en_font)
    rFonts.set(qn("w:hAnsi"), en_font)
    rFonts.set(qn("w:cs"), en_font)
    rFonts.set(qn("w:eastAsia"), cn_font)


def add_superscript_citation(p, cite_str, highlight=False, track=True):
    """
    将形如 '[1]' 或 '[1, 8]' 的正文引用添加为带内部书签跳转 (_Ref_Paper_i) 的上标节点，
    并记录引用出现顺序以校验 GB/T 7714-2015 顺序编码制。
    """
    nums = [int(x.strip()) for x in re.findall(r"\d+", cite_str)]
    if track:
        for n in nums:
            if n not in CITATION_TRACKER:
                CITATION_TRACKER.append(n)
    first_num = nums[0] if nums else 1

    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("w:anchor"), f"_Ref_Paper_{first_num}")
    hyperlink.set(qn("w:history"), "1")

    r_el = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Times New Roman")
    rFonts.set(qn("w:hAnsi"), "Times New Roman")
    rFonts.set(qn("w:cs"), "Times New Roman")
    rFonts.set(qn("w:eastAsia"), "宋体")
    rPr.append(rFonts)

    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "24")
    rPr.append(sz)
    szCs = OxmlElement("w:szCs")
    szCs.set(qn("w:val"), "24")
    rPr.append(szCs)

    color = OxmlElement("w:color")
    color.set(qn("w:val"), "000000")
    rPr.append(color)

    if highlight:
        hl_el = OxmlElement("w:highlight")
        hl_el.set(qn("w:val"), "yellow")
        rPr.append(hl_el)

    va = OxmlElement("w:vertAlign")
    va.set(qn("w:val"), "superscript")
    rPr.append(va)

    r_el.append(rPr)
    t_el = OxmlElement("w:t")
    t_el.text = cite_str
    r_el.append(t_el)

    hyperlink.append(r_el)
    p._element.append(hyperlink)


def add_rich_text_to_paragraph(p, text, cn_font="宋体", en_font="Times New Roman",
                               size_pt=12.0, bold=False, highlight_diff=False,
                               highlight_platform=False,
                               force_hl=False, parse_citations=True):
    """
    解析段落文本中的：
    - 高亮起止标记 {{hl}} ... {{/hl}} (用于对比版)
    - 平台重点标记 {{platform_hl}} ... {{/platform_hl}} (用于学长审阅版)
    - 行内公式标记 {{math:key}}
    - 文献角标 [1]、[1, 8]
    分别渲染为原生 OMML 公式、可点击跳转的上标引用及可选高亮。
    """
    token_pattern = re.compile(
        r"(\{\{hl\}\}|\{\{/hl\}\}|\{\{platform_hl\}\}|\{\{/platform_hl\}\}|\{\{math:[a-zA-Z0-9_]+\}\}|\[\d+(?:,\s*\d+)*\])"
    )
    tokens = token_pattern.split(text)
    hl_active = force_hl
    platform_hl_active = False
    for tok in tokens:
        if not tok:
            continue
        if tok == "{{hl}}":
            hl_active = True
        elif tok == "{{/hl}}":
            hl_active = force_hl
        elif tok == "{{platform_hl}}":
            platform_hl_active = True
        elif tok == "{{/platform_hl}}":
            platform_hl_active = False
        elif tok.startswith("{{math:") and tok.endswith("}}"):
            math_key = tok[7:-2]
            is_hl = (highlight_diff and hl_active) or (highlight_platform and platform_hl_active)
            append_inline_omath(p, math_key, highlight=is_hl)
        elif parse_citations and re.fullmatch(r"\[\d+(?:,\s*\d+)*\]", tok):
            # 文献引用仅在修改对比模式下按需高亮
            add_superscript_citation(p, tok, highlight=(highlight_diff and hl_active))
        else:
            r = p.add_run(tok)
            is_hl = (highlight_diff and hl_active) or (highlight_platform and platform_hl_active)
            set_run_font(r, cn_font=cn_font, en_font=en_font, size_pt=size_pt,
                         bold=bold, highlight=is_hl)


def configure_pPr_xml(p, before_lines=None, after_lines=None, line_twips=360,
                      first_line_twips=None, first_line_chars=None,
                      hanging_twips=None, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    """
    精确配置段落的底层 <w:spacing> 与 <w:ind> XML 属性：
    - 当 before_lines / after_lines 为 None 时，严格清除段前段后间距属性（确保正文与参考文献紧致无多余空隙）
    - 当 before_lines / after_lines 指定时（如 0.5 行），写入 beforeLines="50" afterLines="50"
    """
    p.alignment = align
    pPr = p._element.get_or_add_pPr()

    spacing = pPr.find(qn("w:spacing"))
    if spacing is None:
        spacing = OxmlElement("w:spacing")
        pPr.append(spacing)
    for attr in ["w:before", "w:beforeLines", "w:after", "w:afterLines", "w:line", "w:lineRule"]:
        if qn(attr) in spacing.attrib:
            del spacing.attrib[qn(attr)]

    spacing.set(qn("w:line"), str(line_twips))
    spacing.set(qn("w:lineRule"), "auto")
    if before_lines is not None and before_lines > 0:
        spacing.set(qn("w:beforeLines"), str(int(round(before_lines * 100))))
        spacing.set(qn("w:before"), str(int(round(before_lines * 240))))
    if after_lines is not None and after_lines > 0:
        spacing.set(qn("w:afterLines"), str(int(round(after_lines * 100))))
        spacing.set(qn("w:after"), str(int(round(after_lines * 240))))

    ind = pPr.find(qn("w:ind"))
    if ind is None:
        ind = OxmlElement("w:ind")
        pPr.append(ind)
    for attr in ["w:firstLine", "w:firstLineChars", "w:hanging", "w:hangingChars", "w:left", "w:leftChars"]:
        if qn(attr) in ind.attrib:
            del ind.attrib[qn(attr)]

    if hanging_twips is not None:
        ind.set(qn("w:left"), str(hanging_twips))
        ind.set(qn("w:hanging"), str(hanging_twips))
    elif first_line_twips is not None or first_line_chars is not None:
        if first_line_chars is not None and first_line_chars > 0:
            ind.set(qn("w:firstLineChars"), str(int(round(first_line_chars * 100))))
        if first_line_twips is not None:
            ind.set(qn("w:firstLine"), str(first_line_twips))
    else:
        ind.set(qn("w:firstLine"), "0")
        ind.set(qn("w:firstLineChars"), "0")
        ind.set(qn("w:left"), "0")


def insert_paragraph_before(doc, ref_p, text="", style_type="body", bold_prefix=None,
                            ref_index=None, highlight_diff=False, highlight_platform=False,
                            force_hl=False, page_break_before=False):
    """
    在锚点段落 ref_p 前插入严格挂载官方模板样式的段落：
    - h1: 一级标题（Normal 样式，黑体四号 14pt，首行缩进 2 字符 560 dxa，段前 0.5 行、段后 0.5 行）
    - h2: 二级标题（条 样式 a6，黑体小四号 12pt，顶格无缩进，序号与题名空一格，段前 0.5 行、段后 0.5 行）
    - h3: 三级标题（正文格式 样式 a7，黑体小四号 12pt，首行缩进 2 字符 480 dxa，无段前段后间距）
    - body: 正文段落（正文格式 样式 a7，宋体/TNR 小四号 12pt，首行缩进 2 字符 480 dxa，无段前段后间距）
    - formula: 独立公式段落（正文格式 样式 a7，居中无缩进，OMML 公式对象）
    - caption: 图题（Normal 样式，五号加粗，居中，段后 0.5 行）
    - table_caption: 表题（Normal 样式，五号加粗，居中，段前 0.5 行、无段后间距）
    - ref: 参考文献条目（参考文献 样式 a9，宋体/TNR 小四号 12pt，悬挂缩进 0.74cm = 420 dxa，无段前段后间距，带原生书签）
    """
    if style_type == "body" and "\n\n" in text:
        parts = [pt.strip() for pt in text.split("\n\n") if pt.strip()]
        last_p = None
        for idx, part in enumerate(parts):
            pfx = bold_prefix if idx == 0 else None
            pbb = page_break_before if idx == 0 else False
            last_p = insert_paragraph_before(
                doc, ref_p, part, style_type=style_type, bold_prefix=pfx,
                highlight_diff=highlight_diff, highlight_platform=highlight_platform,
                force_hl=force_hl, page_break_before=pbb
            )
        return last_p

    new_p = ref_p.insert_paragraph_before("")
    do_hl = highlight_diff and force_hl

    # 严格对齐原模板格式：正文第一节“一、毕业论文课题背景”前插入分页符，确保正文从第2页顶格起排，封面独立成页
    if page_break_before or (style_type == "h1" and text.startswith("一、")):
        r_br = new_p.add_run()
        r_br.add_break(WD_BREAK.PAGE)

    if style_type == "h1":
        new_p.style = doc.styles["Normal"]
        configure_pPr_xml(new_p, before_lines=0.5, after_lines=0.5, line_twips=360,
                          first_line_twips=560, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        add_rich_text_to_paragraph(
            new_p, text, cn_font="黑体", en_font="Times New Roman",
            size_pt=14.0, bold=False, highlight_diff=highlight_diff,
            highlight_platform=highlight_platform,
            force_hl=force_hl, parse_citations=False
        )

    elif style_type == "h2":
        new_p.style = doc.styles["条"]
        configure_pPr_xml(new_p, before_lines=0.5, after_lines=0.5, line_twips=360,
                          first_line_twips=None, first_line_chars=None, align=WD_ALIGN_PARAGRAPH.LEFT)
        add_rich_text_to_paragraph(
            new_p, text, cn_font="黑体", en_font="Times New Roman",
            size_pt=12.0, bold=False, highlight_diff=highlight_diff,
            highlight_platform=highlight_platform,
            force_hl=force_hl, parse_citations=False
        )

    elif style_type == "h3":
        new_p.style = doc.styles["正文格式"]
        configure_pPr_xml(new_p, before_lines=None, after_lines=None, line_twips=360,
                          first_line_twips=480, first_line_chars=2.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        add_rich_text_to_paragraph(
            new_p, text, cn_font="黑体", en_font="Times New Roman",
            size_pt=12.0, bold=False, highlight_diff=highlight_diff,
            highlight_platform=highlight_platform,
            force_hl=force_hl, parse_citations=False
        )

    elif style_type == "formula":
        new_p.style = doc.styles["正文格式"]
        configure_pPr_xml(new_p, before_lines=None, after_lines=None, line_twips=360,
                          first_line_twips=None, first_line_chars=None, align=WD_ALIGN_PARAGRAPH.CENTER)
        append_display_omath(new_p, text, highlight=do_hl)

    elif style_type == "caption":
        new_p.style = doc.styles["Normal"]
        configure_pPr_xml(new_p, before_lines=None, after_lines=0.5, line_twips=360,
                          first_line_twips=None, first_line_chars=None, align=WD_ALIGN_PARAGRAPH.CENTER)
        add_rich_text_to_paragraph(
            new_p, text, cn_font="宋体", en_font="Times New Roman",
            size_pt=10.5, bold=True, highlight_diff=highlight_diff,
            highlight_platform=highlight_platform,
            force_hl=force_hl, parse_citations=False
        )

    elif style_type == "table_caption":
        new_p.style = doc.styles["Normal"]
        configure_pPr_xml(new_p, before_lines=0.5, after_lines=None, line_twips=240,
                          first_line_twips=None, first_line_chars=None, align=WD_ALIGN_PARAGRAPH.CENTER)
        add_rich_text_to_paragraph(
            new_p, text, cn_font="宋体", en_font="Times New Roman",
            size_pt=10.5, bold=True, highlight_diff=highlight_diff,
            highlight_platform=highlight_platform,
            force_hl=force_hl, parse_citations=False
        )

    elif style_type == "ref":
        new_p.style = doc.styles["参考文献"]
        configure_pPr_xml(new_p, before_lines=None, after_lines=None, line_twips=360,
                          hanging_twips=420, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        if ref_index is not None:
            bm_start = OxmlElement("w:bookmarkStart")
            bm_start.set(qn("w:id"), str(100 + ref_index))
            bm_start.set(qn("w:name"), f"_Ref_Paper_{ref_index}")
            new_p._element.append(bm_start)

        add_rich_text_to_paragraph(
            new_p, text, cn_font="宋体", en_font="Times New Roman",
            size_pt=12.0, bold=False, highlight_diff=highlight_diff,
            highlight_platform=highlight_platform,
            force_hl=force_hl, parse_citations=False
        )

        if ref_index is not None:
            bm_end = OxmlElement("w:bookmarkEnd")
            bm_end.set(qn("w:id"), str(100 + ref_index))
            new_p._element.append(bm_end)

    else:  # body
        new_p.style = doc.styles["正文格式"]
        configure_pPr_xml(new_p, before_lines=None, after_lines=None, line_twips=360,
                          first_line_twips=480, first_line_chars=2.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        if bold_prefix:
            add_rich_text_to_paragraph(
                new_p, bold_prefix, cn_font="宋体", en_font="Times New Roman",
                size_pt=12.0, bold=True, highlight_diff=highlight_diff,
                highlight_platform=highlight_platform,
                force_hl=force_hl, parse_citations=False
            )
        add_rich_text_to_paragraph(
            new_p, text, cn_font="宋体", en_font="Times New Roman",
            size_pt=12.0, bold=False, highlight_diff=highlight_diff,
            highlight_platform=highlight_platform, force_hl=force_hl
        )

    return new_p


def insert_image_before(doc, ref_p, img_path, caption_text, width_cm=15.2,
                        highlight_diff=False, highlight_platform=False, force_hl=False):
    """在 ref_p 前插入居中高清图及五号加粗图题"""
    p_img = ref_p.insert_paragraph_before("")
    p_img.style = doc.styles["Normal"]
    configure_pPr_xml(p_img, before_lines=0.5, after_lines=None, line_twips=240,
                      first_line_twips=None, first_line_chars=None, align=WD_ALIGN_PARAGRAPH.CENTER)
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Cm(width_cm))
    insert_paragraph_before(doc, ref_p, caption_text, style_type="caption",
                            highlight_diff=highlight_diff, highlight_platform=highlight_platform, force_hl=force_hl)


def set_table_borders(table):
    """为表格添加标准细实线边框"""
    tblPr = table._tbl.tblPr
    borders = tblPr.find(qn("w:tblBorders"))
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tblPr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = borders.find(qn(f"w:{edge}"))
        if el is None:
            el = OxmlElement(f"w:{edge}")
            borders.append(el)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")


def remove_protection(doc):
    """移除模板中的 permStart/permEnd 及 documentProtection，使生成的文档可自由编辑与插入插件"""
    body = doc.element.body
    for tag in ("w:permStart", "w:permEnd"):
        for el in body.findall(".//" + qn(tag)):
            el.getparent().remove(el)
    settings = doc.settings.element
    for dp in settings.findall(".//" + qn("w:documentProtection")):
        dp.getparent().remove(dp)


def set_repeat_table_header(row):
    """设置表格首行在跨页时自动重复表头 (<w:tblHeader/>)"""
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn("w:tblHeader")) is None:
        trPr.append(OxmlElement("w:tblHeader"))


def set_row_cant_split(row):
    """设置表格行禁止跨页断行 (<w:cantSplit/>)"""
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn("w:cantSplit")) is None:
        trPr.append(OxmlElement("w:cantSplit"))


def set_cover_cell_text(cell, text, cn_font="宋体", en_font="Times New Roman", size_pt=14.0):
    """填充封面信息表单元格：严格保持原模板 vAlign='bottom'（靠底贴线对齐）、无段间距、单倍行距与四号字"""
    cell.text = ""
    cell.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pPr = p._p.get_or_add_pPr()
    for tag in ("w:spacing", "w:ind"):
        old = pPr.find(qn(tag))
        if old is not None:
            pPr.remove(old)
    r = p.add_run(text)
    set_run_font(r, cn_font=cn_font, en_font=en_font, size_pt=size_pt, bold=False)


def set_cell_text(cell, text, cn_font="宋体", en_font="Times New Roman", size_pt=14.0,
                  bold=False, align=WD_ALIGN_PARAGRAPH.CENTER,
                  highlight_diff=False, highlight_platform=False, force_hl=False):
    """清空正文表格单元格并写入指定格式文本（支持 {{math:key}} 公式与 {{hl}}/{{platform_hl}} 高亮）"""
    cell.text = ""
    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    p = cell.paragraphs[0]
    p.alignment = align
    pf = p.paragraph_format
    pf.space_before = Pt(2)
    pf.space_after = Pt(2)
    pf.line_spacing = 1.2
    pf.first_line_indent = Pt(0)
    add_rich_text_to_paragraph(
        p, text, cn_font=cn_font, en_font=en_font, size_pt=size_pt,
        bold=bold, highlight_diff=highlight_diff, highlight_platform=highlight_platform,
        force_hl=force_hl, parse_citations=False
    )


def build_single_docx(out_docx_path, highlight_mode="none"):
    """
    构建单个开题报告 .docx 文件
    highlight_mode:
      - 'none': 纯净正式版 (100% 无任何高亮)
      - 'diff': 新旧版本修改对比高亮版 (高亮 {{hl}}...{{/hl}})
      - 'platform': 实验室学长审阅确认版 (仅高亮 {{platform_hl}}...{{/platform_hl}} 涉及实验室已有平台/数据的内容)
    """
    highlight_diff = (highlight_mode == "diff")
    highlight_platform = (highlight_mode == "platform")
    CITATION_TRACKER.clear()
    if highlight_mode == "none" and os.path.exists(out_docx_path):
        shutil.copy2(out_docx_path, out_docx_path + ".bak")

    doc = docx.Document(TEMPLATE_PATH)
    remove_protection(doc)

    # 1. 更新封面大标题：统一为“毕业论文开题报告”
    for p in doc.paragraphs:
        if "毕业设计(论文)开题报告" in p.text:
            p.text = ""
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run("毕业论文开题报告")
            set_run_font(r, cn_font="黑体", en_font="Times New Roman", size_pt=36.0, bold=False)
            break

    # 2. 填充封面信息表 (Table 0)：使用 set_cover_cell_text 保持底部对齐与原模板一致
    t_info = doc.tables[0]
    set_cover_cell_text(t_info.cell(0, 1), "基于PX4的水下航行器模型控制方法研究", size_pt=14.0)
    set_cover_cell_text(t_info.cell(1, 1), "", size_pt=14.0)
    set_cover_cell_text(t_info.cell(2, 1), "机械工程与机器人学院", size_pt=14.0)
    set_cover_cell_text(t_info.cell(3, 1), "机械设计制造及其自动化", size_pt=14.0)
    set_cover_cell_text(t_info.cell(4, 1), "张卫恒", size_pt=14.0)
    set_cover_cell_text(t_info.cell(4, 3), "2352407", size_pt=14.0)

    # 3. 清理模板中原有的章节占位段落（从“一、毕业设计（论文）课题背景”到“四、审核意见”之前）
    p_audit = None
    to_delete = []
    collecting = False
    for p in doc.paragraphs:
        txt = p.text.strip()
        if txt.startswith("一、毕业设计（论文）课题背景"):
            collecting = True
        if txt.startswith("四、审核意见"):
            p_audit = p
            break
        if collecting:
            to_delete.append(p)

    for p in to_delete:
        p._element.getparent().remove(p._element)

    # 确保“四、审核意见”保持原模板一级标题样式（黑体四号、首行缩进2字符 560 dxa、段前段后0.5行）
    p_audit.text = ""
    p_audit.style = doc.styles["Normal"]
    configure_pPr_xml(p_audit, before_lines=0.5, after_lines=0.5, line_twips=360,
                      first_line_twips=560, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    r_audit = p_audit.add_run("四、审核意见")
    set_run_font(r_audit, cn_font="黑体", en_font="Times New Roman", size_pt=14.0, bold=False)

    def _add(text="", style_type="body", bold_prefix=None, ref_index=None, force_hl=False, page_break_before=False):
        return insert_paragraph_before(
            doc, p_audit, text=text, style_type=style_type, bold_prefix=bold_prefix,
            ref_index=ref_index, highlight_diff=highlight_diff,
            highlight_platform=highlight_platform, force_hl=force_hl,
            page_break_before=page_break_before
        )

    # =========================================================================
    # 一、毕业论文课题背景
    # =========================================================================
    _add("一、毕业论文课题背景", style_type="h1", page_break_before=True)

    # 1. 课题来源及研究的目的和意义
    _add("{{hl}}1. {{/hl}}课题来源及研究的目的和意义", style_type="h2", force_hl=False)

    _add("{{hl}}1.1 {{/hl}}课题来源", style_type="h3", force_hl=False)
    _add(
        "{{hl}}随着国家海洋强国战略的深入推进与现代海洋工程装备体系的持续完善，水下机器人在海洋资源勘探、水下基础设施运维及水域环境监测中的战略地位日益凸显。国家相关产业发展规划明确将水下探测、监测、作业及深海资源开发等水下机器人列为特种机器人重点研制方向；工业和信息化部、教育部、公安部等十七部门联合印发的《“机器人+”应用行动实施方案》（工信部联通装〔2022〕187号）进一步将安全应急和极限环境列为十大重点应用领域之一，明确提出要“推动空间、水下、深地等极限环境场景应用” [1]。{{/hl}}\n\n"
        "{{hl}}在上述国家产业政策牵引与行业应用需求驱动下，水下航行器被广泛应用于海底油气管网巡检、海上风电大直径基桩与跨海桥隧水下结构物无损检测、大型水利水电大坝安全排查，以及现代海洋牧场立体监测等作业场景。在贴近被测复杂水下结构物或狭窄受限水域开展近距离观测与精细作业时，非定常水流扰动与水下视线受阻对航行器的低速机动与位姿保持能力提出了严格要求，亟需航行器能够在水流干扰环境下稳定可靠地完成空间定点悬停、姿态稳定、定深控制与定航控制等基本运动控制任务。{{/hl}}\n\n"
        "{{hl}}在此背景下，{{/hl}}本课题来源于实验室在水下无人系统与智能海洋装备方向的科研实践与工程开发需求，{{platform_hl}}直接依托实验室{{hl}}已有的八推进器便携式水下航行器（Remotely Operated Vehicle，ROV）{{/hl}}实验平台方案及相关结构数据开展研究。{{/platform_hl}}{{platform_hl}}该平台具备八推进器空间对称与矢量倾斜布置的硬件驱动能力{{/platform_hl}}，但在流体环境中实现{{hl}}稳定可靠的闭环运动控制{{/hl}}仍面临诸多瓶颈：缺乏系统化的水动力建模与参数辨识，使得控制器难以获取物理平台的真实动力学特性；运动控制与推力分配多采用人工试凑的经验PID参数，未能在六自由度耦合层面上充分释放八推进器过驱动配置的协调潜力；控制系统软件缺乏工业级模块化规范，难以直接面向工程部署开展高可信度的闭环验证。为此，本课题{{platform_hl}}立足于实验室已有平台的方案与数据基础{{/platform_hl}}，围绕“动力学建模、系统辨识、模型运动控制、八推进器控制分配及 PX4/SITL 闭环仿真验证”开展系统性研究，具有坚实的{{hl}}工程实践{{/hl}}背景与明确的技术升级需求。",
        style_type="body", force_hl=False
    )

    _add("{{hl}}1.2 {{/hl}}研究目的", style_type="h3", force_hl=False)
    _add(
        "{{hl}}水下航行器在黏性流场中运动时具有显著的附加质量、水动力阻尼与重浮力恢复力矩等六自由度非线性耦合特性，且由常规欠驱动构型向八推进器过驱动构型拓展后，亟需同步解决多自由度耦合状态下的稳定闭环运动控制与受推力物理边界约束的多推进器协调控制分配两大核心问题。为此，本课题的研究目的在于：{{/hl}}{{platform_hl}}依托{{hl}}实验室{{/hl}}已有八推进器{{hl}}便携式{{/hl}}水下航行器平台，建立六自由度动力学与推进器模型；结合已有平台参数资料和相关{{hl}}动态响应{{/hl}}数据开展系统辨识与模型验证{{/platform_hl}}，明确系统辨识的输入输出关系，对关键未知{{hl}}水动力参数{{/hl}}进行{{hl}}估计{{/hl}}修正并分析模型适用范围；在此基础上，结合经验证的航行器模型特性{{hl}}补偿{{/hl}}与{{hl}}实时{{/hl}}状态反馈构建闭环运动控制系统，实现姿态、深度和航向等基本运动状态的{{hl}}稳定{{/hl}}闭环控制；{{platform_hl}}依据八推进器空间布局建立控制分配矩阵{{/platform_hl}}，考虑基本推力输出范围生成{{hl}}各推进器{{/hl}}推力指令；最终在PX4/SITL软件在环仿真环境中构建闭环系统，通过{{hl}}典型{{/hl}}运动工况与{{hl}}适量{{/hl}}流扰条件开展闭环仿真验证与量化性能评价，形成“已有平台—建模与系统辨识—模型验证—运动控制—控制分配—PX4/SITL闭环验证”的完整研究闭环。",
        style_type="body", force_hl=False
    )

    _add("{{hl}}1.3 {{/hl}}研究意义", style_type="h3", force_hl=False)
    _add(
        "{{hl}}开展本课题研究对提升水下航行器的运动控制性能与工程开发效率具有直接价值。一方面，针对便携式水下航行器水动力参数不确定、多自由度交叉耦合以及八推进器推力受限等问题，将经辨识验证的动力学模型引入闭环控制器与受约束控制分配设计，能够有效克服传统经验控制在多轴机动与流扰环境下易超调、推力分配易饱和失真的局限，为过驱动水下航行器的稳定可靠控制提供方法支撑。另一方面，依托开源 PX4 飞控软件架构构建水下软件在环（SITL）闭环仿真环境，使动力学模型、运动控制律与推力分配算法在与实机一致的模块化软件框架下完成闭环检验，不仅能够在安全、可重复的条件下系统评估算法性能并降低水池实机联调的试错成本，还有助于为后续控制算法向实验室水下航行器机载硬件迁移部署奠定可靠的软件基础。{{/hl}}",
        style_type="body", force_hl=False
    )

    # 2. 国内外在该方向的研究现状和发展趋势
    _add("{{hl}}2. {{/hl}}国内外在该方向的研究现状和发展趋势", style_type="h2", force_hl=False)

    _add(
        "{{hl}}水下航行器在复杂黏性流场中的稳定运动控制，本质上涉及非流线型机体的多自由度流固耦合机理表征、非线性运动控制律设计、冗余推进器推力协调映射以及嵌入式控制软件闭环实现等关键科学和工程问题。围绕{{/hl}}水下航行器六自由度动力学机理建模与参数辨识、基于模型与状态反馈的运动控制方法、多推进器受约束控制分配以及基于开源飞控软件（PX4）的闭环仿真等四个核心{{hl}}方向{{/hl}}，国内外学术界与工业界进行了深入研究并取得了丰富成果。",
        style_type="body", force_hl=False
    )

    _add("{{hl}}2.1 {{/hl}}水下航行器动力学建模与系统辨识研究现状", style_type="h3", force_hl=False)
    _add(
        "在动力学机理建模方面，水下航行器的运动学与动力学理论体系历经长期发展，已形成规范的标准框架。国际水池会议（ITTC）与国际海事组织（IMO）为海洋船舶与运载器的运动表述奠定了基础，挪威科技大学学者 Fossen 系统提出了海洋航行器六自由度非线性矢量建模理论体系{{hl}}[2]{{/hl}}。该体系将{{hl}}惯性坐标系与固连于航行器的附体坐标系{{/hl}}相结合，通过坐标变换矩阵统一描述位置、姿态{{hl}}角{{/hl}}与六自由度线速度、角速度，并将作用于机体上的广义力矩解构为刚体惯性矩阵、水动力附加质量矩阵、刚体与附加质量科氏向心力矩阵、线性与非线性水动力阻尼矩阵以及重力与浮力恢复力矩矢量，成为当前水下航行器建模与控制研究所公认的方程基础。{{hl}}对于搭载耐压水密舱、外部传感器探头及多推进器组件的非流线型多附体水下航行器（ROV）而言，其水动力特性与流线型回转体 AUV 存在明显差异。{{/hl}}Caccia 等较早对{{hl}}可变构型无人水下航行器{{/hl}}的动力学建模与水动力参数辨识展开了系统研究，{{hl}}指出了在标准六自由度方程结构下根据低速对称特性简化水动力矩阵并结合试验数据辨识主导水动力参数的可行性[3]。{{/hl}}\n\n"
        "{{hl}}由于非流线型多附体航行器的水动力系数难以仅凭理论经验公式精确估算，而传统平面运动机构（PMM）大型水池拖曳试验设备成本高、周期长，因此在套用标准六自由度机理方程结构的基础上，利用平台几何质量先验参数确定刚体项、结合低成本原位动态响应数据拟合未知水动力系数，成为获取可用工程动力学模型的主流途径。{{/hl}}Ross、Fossen 与 Johansen 提出了基于自由衰减试验（Free Decay Tests）辨识水下航行器水动力系数的方法，通过释放初始位移并记录单自由度衰减振荡曲线即可解算出主要惯性与阻尼参数{{hl}}[4]{{/hl}}；Avila 等针对{{hl}}复杂构型{{/hl}}水下航行器开展了实验水动力模型辨识研究，结合阶跃推力激励与频域响应分析对附加质量与流体阻尼特性进行了定量标定{{hl}}[5]{{/hl}}；Chin 与 Lau 针对{{hl}}复杂外形 ROV{{/hl}} 开展了水动力阻尼建模与试验对比，分析了不同速度区间线性阻尼与二次非线性阻尼的主导权重{{hl}}[6]{{/hl}}。国内哈尔滨工程大学高婷、庞永杰等针对复杂构型水下航行器水动力系数计算方法开展了系统研究，结合几何特征分析与试验修正建立了面向控制设计的实用化模型{{hl}}[7]{{/hl}}。{{hl}}近年来，von Benzon 等面向主流八推进器 BlueROV2 平台建立了开源物理仿真与动力学基准，提供了标准化的模型参数与对比基础[8]。这表明，直接采用经典六自由度动力学方程结构、对水动力矩阵做合理工程简化，并结合特征激励响应数据通过参数拟合辨识未知水动力系数，是构建水下航行器实用化动力学模型的成熟路径。{{/hl}}",
        style_type="body", force_hl=False
    )

    _add("{{hl}}2.2 {{/hl}}水下航行器运动控制方法研究现状", style_type="h3", force_hl=False)
    _add(
        "水下航行器运动控制的核心任务在于驱动推进器系统产生协调推力与力矩，使航行器的空间位置、潜深以及横滚、俯仰、偏航姿态稳定准确地跟踪给定的参考运动指令，并在存在未建模动态与外部水流干扰时维持良好的瞬态与稳态性能。{{hl}}典型水下航行器六自由度模型控制与推力分配通用闭环结构如图 1 所示（基于 Fossen 经典海洋航行器控制理论架构 [2]）：{{/hl}}",
        style_type="body", force_hl=False
    )

    if os.path.exists(FIG1_LIT_PATH):
        insert_image_before(
            doc, p_audit, FIG1_LIT_PATH,
            "图 1  典型水下航行器六自由度模型控制与推力分配通用闭环结构框图",
            width_cm=15.2, highlight_diff=highlight_diff, force_hl=True
        )

    _add(
        "{{hl}}在常规工程实践与开源水下飞控中，不依赖动力学模型的独立单回路 PID 或串级 PID 控制应用最为广泛，其在平稳水流环境下的定点悬停或低速巡航中具备结构简单、易于初调的优势 [2, 8]。然而，八推进器便携式水下航行器本质上是一个多自由度耦合的非线性系统：航行器在水平面做纵向或侧向机动时易诱发俯仰、垂荡或横滚耦合运动，且重力与浮力的恢复力矩随姿态倾角呈三角函数非线性变化。完全忽略航行器动力学特性的纯无模型 PID 控制，在较大幅度机动与外部水流扰动下容易出现响应滞后、超调偏大或多通道相互拉扯干扰，难以兼顾动态跟踪精度与抗扰稳定性。{{/hl}}\n\n"
        "{{hl}}针对传统无模型 PID 控制的上述局限，将辨识得到的航行器动力学模型引入控制器设计、与实时状态误差反馈相结合，成为提升水下航行器闭环控制性能的重要途径。如图 1 所示，通用模型闭环控制器由“基于动力学模型的动态特性补偿”与“基于状态误差的闭环反馈”两部分协同构成。围绕如何有效利用动力学模型信息，国内外学者发展了多种代表性方法：{{/hl}}Fernandes 等针对观察级 ROV 提出了一种{{hl}}结合航行器动力学模型与高增益状态观测器的输出反馈运动控制系统，有效提升了深度、航向和水平面位置的闭环控制品质{{/hl}} [9]；Chu 等针对{{hl}}水下航行器水动力阻尼不确定性与推力受限问题{{/hl}}，提出了一种融合动力学模型前馈补偿与参数更新的轨迹跟踪控制方法，{{hl}}改善了耦合机动下的跟踪精度{{/hl}} [10]；{{hl}}围绕非线性解耦与抗扰，基于反馈线性化、动态逆以及增量非线性动态逆（INDI）的控制方法也受到广泛关注，例如 Slawik 等将增量动态逆方法引入水下航行器姿态控制中，利用机体惯性与控制效能模型配合高频状态反馈在局部时间微元内抵消未建模水动力阻尼与外部流扰，展现出良好的抗扰能力 [11]。{{/hl}}\n\n"
        "{{hl}}综合国内外研究进展可知，相较于完全忽略物理特性的传统无模型 PID 控制，利用辨识验证后的航行器动力学模型对重浮力恢复力矩、主导水动力阻尼或惯性动态进行补偿，并结合实时状态误差反馈构建闭环控制器，能够有效改善多自由度耦合与流扰环境下的控制性能，也为本课题根据实机辨识模型特性比选合适的模型控制律（如模型前馈补偿、反馈线性化或增量动态逆等）提供了扎实的理论方法支撑。{{/hl}}",
        style_type="body", force_hl=False
    )

    _add("{{hl}}2.3 {{/hl}}多推进器控制分配研究现状", style_type="h3", force_hl=False)
    _add(
        "对于配备八个推进器的{{hl}}便携式{{/hl}}水下航行器而言，其独立的物理执行器数量（8 个推进器）大于空间六自由度广义力与力矩的数量（6 个控制维度），属于典型的过驱动（Over-actuated）冗余控制系统。上层运动控制器计算出的是机体所需的六维期望广义力与力矩 {{math:tau_c_R6}}，而实际作用于水体的是各推进器产生的推力矢量 {{math:T_R8}}。如何根据推进器空间安装布局将期望广义力矩准确、低失真地映射为各推进器推力指令，即为控制分配（Control Allocation）的核心任务。\n\n"
        "{{hl}}Johansen 与 Fossen 在控制分配综述中系统总结了无约束广义逆、加权伪逆、有界优化及再分配方法的理论体系 [12, 13]。在基础工程应用中，常采用固定比例混控表或无约束伪逆法直接求解推力指令；当某一推进器计算推力超出物理输出上下限时，常规做法通常直接进行硬截断（Clipping）。然而，由于八推进器空间布置存在多自由度力臂耦合，简单的超限硬截断会破坏原本各推进器之间的推力配比，导致合成的六维广义力和力矩方向发生偏转（即产生较大的控制分配残差与姿态耦合失真）。为此，考虑推进器基本推力输出范围约束的控制分配策略受到广泛重视：{{/hl}}程卫平、王猛等针对水下机器人推力器物理输出上限，研究了基于可行方向法等处理推力边界约束的分配算法，{{hl}}有效减小了推力饱和引起的力矩畸变 [14]{{/hl}}；孙广威等针对矢量推进 ROV 提出了兼顾推力约束与分配效率的多级推力分配策略，{{hl}}提升了多推进器协调能力 [15]。由此可见，{{/hl}}{{platform_hl}}依据平台八推进器真实几何构型建立准确的 {{math:6x8}} 控制分配矩阵{{/platform_hl}}{{hl}}，并在分配求解中引入推力输出范围约束处理策略以克服直接硬截断失真，是保障闭环控制系统稳定运行的关键环节。{{/hl}}",
        style_type="body", force_hl=False
    )

    _add("{{hl}}2.4 {{/hl}}基于开源软件架构（PX4）的水下航行器闭环仿真研究现状", style_type="h3", force_hl=False)
    _add(
        "在现代机器人与无人系统的研发流程中，控制算法的模块化软件实现与闭环仿真验证平台至关重要。传统的控制算法验证多基于纯离线数学脚本（如纯 MATLAB 或 Python 数值积分），虽然便于验证控制律的数学收敛性，但脱离了嵌入式实时操作系统（RTOS）的多任务并发调度、模块间异步通信以及离散采样周期等工程约束，导致算法向实验平台机载硬件迁移时面临较大的代码重构工作量。\n\n"
        "苏黎世联邦理工学院（ETH Zurich）Meier 等主导研发的 PX4 Autopilot 是当前无人系统领域广泛应用的开源嵌入式控制软件框架之一{{hl}}[16]{{/hl}}。PX4 采用“算法模块层与系统中间件层”解耦的架构设计，通过基于共享内存的微对象请求代理（uORB）异步发布/订阅总线实现状态估计、运动控制与控制分配模块之间的标准化数据交互；同时原生支持软件在环（SITL）闭环编译运行与 ULog 全状态日志记录。近年来，国内外研究团队开始将 PX4 架构拓展至水下无人航行器领域，{{hl}}如 Duecker 等依托基于 PX4 的软件在环仿真与水池实验完成了 HippoCampus X 水下平台的三维机动控制验证，证实了基于 PX4/SITL 构建水下航行器闭环仿真与验证体系的工程合理性[17]。{{/hl}}",
        style_type="body", force_hl=False
    )

    _add("{{hl}}2.5 {{/hl}}发展趋势与对本课题的启示", style_type="h3", force_hl=False)
    _add(
        "{{hl}}结合任务书确定的四个核心研究模块，将各模块常规工程做法的局限性、国内外代表性改进方法与本课题拟采取的研究方案归纳对比如下（见表 1）：{{/hl}}",
        style_type="body", force_hl=False
    )

    # 插入表 1：本课题四大研究模块的现状局限、代表性方法与拟采取方案对比
    _add("{{hl}}表 1  本课题四大研究模块的现状局限、代表性方法与拟采取方案对比{{/hl}}", style_type="table_caption", force_hl=False)
    cmp_data = [
        ("{{hl}}研究模块{{/hl}}", "{{hl}}常规做法与主要局限{{/hl}}", "{{hl}}国内外代表性改进方法{{/hl}}", "{{hl}}本课题拟采取的研究方案{{/hl}}"),
        (
            "{{hl}}1. 动力学建模与系统辨识{{/hl}}",
            "{{hl}}纯理论经验公式估算复杂构型水动力参数误差较大；大型平面运动机构（PMM）拖曳水池试验成本高、周期长{{/hl}}",
            "{{hl}}采用 Fossen 六自由度动力学方程结构，对水动力矩阵做合理简化，结合自由衰减、阶跃激励等原位试验数据辨识主导水动力系数 [2]–[8]{{/hl}}",
            "{{platform_hl}}{{hl}}套用六自由度标准方程，由三维模型与硬件资料确定刚体先验参数及推进器静态映射，对附加质量与阻尼矩阵做对角化简化，利用特征响应数据通过最小二乘/曲线拟合辨识未知参数并验证{{/hl}}{{/platform_hl}}"
        ),
        (
            "{{hl}}2. 水下航行器运动控制{{/hl}}",
            "{{hl}}传统无模型独立通道 PID 控制，忽略非线性重浮力恢复力矩与多轴水动力耦合，较大机动与水流扰动下易超调、响应滞后 [2], [8]{{/hl}}",
            "{{hl}}引入动力学模型信息与状态反馈相结合（如模型前馈补偿、状态观测输出反馈、反馈线性化、增量动态逆 INDI 等）[9]–[11]{{/hl}}",
            "{{hl}}采用“辨识模型动态特性补偿 + 实时状态误差反馈”闭环控制思路（保留具体模型控制律比选空间），以传统无模型 PID 为基准开展多工况跟踪与抗流扰对比{{/hl}}"
        ),
        (
            "{{hl}}3. 八推进器控制分配{{/hl}}",
            "{{hl}}固定比例混控表或无约束伪逆分配加直接硬截断（Clipping），推进器饱和时易导致合成广义力与力矩方向失真{{/hl}}",
            "{{hl}}基于空间几何映射矩阵的有界控制分配方法（加权伪逆、保方向缩放再分配、可行方向优化、多级分配等）[12]–[15]{{/hl}}",
            "{{platform_hl}}{{hl}}推导八推进器 {{math:6x8}} 控制分配矩阵 {{math:B_mat}}，引入基本推力范围 {{math:T_interval}} 约束处理策略，并与无约束直接硬截断对比分析分配误差 {{math:e_tau}}{{/hl}}{{/platform_hl}}"
        ),
        (
            "{{hl}}4. 闭环仿真与系统验证{{/hl}}",
            "{{hl}}纯离线数学脚本（如纯 MATLAB/Python）仿真，脱离嵌入式实时多任务调度与异步通信约束，向实机移植重构工作量大{{/hl}}",
            "{{hl}}基于开源嵌入式飞控软件架构（PX4）与 uORB 异步微消息总线的软件在环（SITL）闭环验证体系 [16], [17]{{/hl}}",
            "{{hl}}在 PX4/SITL 环境中集成辨识后的六自由度模型、运动控制模块与八推进器控制分配模块，完成典型运动工况与适量流扰下的闭环性能验证{{/hl}}"
        ),
    ]
    tbl_cmp = doc.add_table(rows=len(cmp_data), cols=4)
    tbl_cmp.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_cmp)
    set_repeat_table_header(tbl_cmp.rows[0])
    for row in tbl_cmp.rows:
        set_row_cant_split(row)
    cmp_col_widths = [Cm(2.6), Cm(3.8), Cm(4.3), Cm(4.7)]
    for r_idx, row_tuple in enumerate(cmp_data):
        is_header = (r_idx == 0)
        for c_idx, val in enumerate(row_tuple):
            cell = tbl_cmp.cell(r_idx, c_idx)
            cell.width = cmp_col_widths[c_idx]
            align = WD_ALIGN_PARAGRAPH.CENTER if (is_header or c_idx == 0) else WD_ALIGN_PARAGRAPH.LEFT
            cn_f = "黑体" if is_header else "宋体"
            set_cell_text(
                cell, val, cn_font=cn_f, en_font="Times New Roman",
                size_pt=9.5, bold=(is_header or c_idx == 0),
                align=align, highlight_diff=highlight_diff,
                highlight_platform=highlight_platform, force_hl=False
            )
    p_audit._element.addprevious(tbl_cmp._tbl)

    _add(
        "{{hl}}综合上述四个模块的研究现状与表 1 对比分析，可以提炼出对本课题的关键启示：一是直接套用成熟的六自由度动力学方程框架并做对角化工程简化，利用三维结构数据确定刚体参数，再通过特征动态响应数据拟合未知水动力系数，能够以较低成本获取满足控制器设计与仿真需求的实用化模型；二是针对传统无模型 PID 控制易超调及无约束伪逆硬截断易失真的工程痛点，在控制层引入辨识模型的动态补偿、在分配层引入推进器推力范围约束处理，并保留具体模型控制算法的横向比选余地，兼具性能提升潜力与工程稳健性；三是将动力学模型、运动控制与八推进器控制分配统一集成至 PX4/SITL 软件架构下开展闭环验证，能够有效弥合离线算法设计与嵌入式工程实现之间的鸿沟。{{/hl}}",
        style_type="body", force_hl=False
    )

    # =========================================================================
    # 二、毕业论文方案介绍
    # =========================================================================
    _add("二、毕业论文方案介绍", style_type="h1")

    # 1. 主要研究内容
    _add("{{hl}}1. {{/hl}}主要研究内容", style_type="h2", force_hl=False)

    _add("{{hl}}1.1 {{/hl}}预期研究目标", style_type="h3", force_hl=False)
    _add(
        "本课题{{platform_hl}}依托已有八推进器{{hl}}便携式{{/hl}}水下航行器平台，建立能够反映航行器主要动态特性的六自由度动力学模型与推进器模型，结合平台参数资料和相关数据完成系统辨识与模型验证{{/platform_hl}}；在此基础上研究基于航行器模型和状态反馈的闭环运动控制方法及八推进器控制分配方案，并在PX4/SITL环境下构建完整闭环仿真系统，完成典型运动工况与适量外部扰动工况下的仿真验证与性能分析，形成“已有平台—建模与系统辨识—模型验证—运动控制—控制分配—PX4/SITL闭环验证”的完整研究闭环。",
        style_type="body", force_hl=False
    )

    _add("{{hl}}1.2 {{/hl}}研究内容要点", style_type="h3", force_hl=False)
    _add(
        "{{hl}}围绕上述预期目标与任务书要求，本课题的主要研究内容划分为以下四个核心模块：{{/hl}}",
        style_type="body", force_hl=False
    )

    _add(
        "{{platform_hl}}依托已有八推进器{{hl}}便携式{{/hl}}水下航行器平台，{{hl}}套用六自由度运动学与动力学标准方程{{/hl}}{{/platform_hl}}，考虑刚体惯性、附加质量、科氏力与向心力、水动力阻尼以及重力与浮力恢复作用等主要动力学因素；{{platform_hl}}{{hl}}结合平台三维结构资料确定刚体质量、转动惯量与重浮心位置等先验参数，建立单推进器控制输入到推力输出的静态映射关系并明确基本推力范围。在此基础上，对附加质量与水动力阻尼矩阵做工程对角化简化，明确系统辨识的激励输入、状态输出及所需数据关系，结合平台特征工况（如阶跃推力或自由衰减）动态响应数据，采用最小二乘或曲线拟合方法对关键未知水动力参数进行辨识与修正，并通过代表性动态响应验证模型与数据之间的偏差，得到用于运动控制设计和 PX4/SITL 闭环仿真的航行器动力学模型。{{/hl}}{{/platform_hl}}",
        style_type="body", bold_prefix="1） 水下航行器动力学建模与系统辨识：", force_hl=False
    )

    _add(
        "{{hl}}以辨识验证后的航行器动力学模型为基础，针对传统无模型 PID 控制在多自由度耦合与流扰下易超调的局限，结合航行器动力学特性补偿与实时状态误差反馈构建闭环运动控制系统（可根据辨识模型特性灵活采用模型前馈补偿、反馈线性化或增量动态逆等模型控制律），根据参考状态与当前状态之间的误差计算航行器所需的期望广义力和力矩，实现姿态、深度和航向等基本运动状态的稳定闭环控制；以传统无模型 PID 控制为对比基准，选取代表性运动工况分析跟踪性能和动态特性，并考察外部水流扰动对闭环控制性能的影响。{{/hl}}",
        style_type="body", bold_prefix="2） 水下航行器运动控制方法研究：", force_hl=False
    )

    _add(
        "{{platform_hl}}{{hl}}根据已有八推进器平台（水平面 4 台矢量倾斜布置、垂直面 4 台垂向对称布置）的推进器安装位置、推力方向及力臂关系，建立各推进器推力与航行器广义力、力矩之间的映射关系及 {{math:6x8}} 控制分配矩阵；{{/hl}}{{/platform_hl}}{{hl}}针对常规无约束伪逆分配在推进器超限时直接硬截断易造成合成力矩方向失真的问题，结合推进器实际输出范围引入推力边界约束处理策略，将运动控制器输出的期望广义力和力矩转换为各推进器推力指令，并与无约束直接硬截断方案对比，结合控制分配误差和各推进器输出饱和情况分析分配效果。{{/hl}}",
        style_type="body", bold_prefix="3） 八推进器控制分配：", force_hl=False
    )

    _add(
        "在 PX4/SITL 仿真环境中构建由航行器动力学模型、运动控制模块和八推进器控制分配模块组成的闭环仿真系统，通过 uORB 异步消息总线完成必要的状态信息、控制量和推进器指令交互；{{hl}}设置空间定点悬停、姿态稳定、定深控制与定航控制等代表性运动工况及适量外部水流扰动条件，考察闭环系统的动态特性和控制效果，结合位置/姿态跟踪误差、动态响应指标及控制分配误差进行量化性能分析，验证闭环系统的控制效果。{{/hl}}",
        style_type="body", bold_prefix="4） PX4/SITL 闭环仿真与系统验证：", force_hl=False
    )

    # 2. 研究方案
    _add("{{hl}}2. {{/hl}}研究方案", style_type="h2", force_hl=False)

    _add("{{hl}}2.1 {{/hl}}拟采取的研究方法", style_type="h3", force_hl=False)
    _add(
        "{{hl}}对应上述四个研究模块，本课题拟采取的具体研究方法如下：{{/hl}}",
        style_type="body", force_hl=False
    )

    _add(
        "{{hl}}如图 2 所示，建立惯性坐标系{{/hl}} {{math:n_coord}} 与附体坐标系 {{math:b_coord}}，设航行器广义位置与姿态矢量为 {{math:eta_def}}，附体系下线速度与角速度矢量为 {{math:nu_def}}。{{hl}}套用标准六自由度运动学与动力学方程：{{/hl}}",
        style_type="body", bold_prefix="1） 水下航行器动力学建模与系统辨识方法：", force_hl=False
    )
    _add("eq1_6dof", style_type="formula")
    _add(
        "式中，{{math:J_eta}} 为坐标转换矩阵；{{math:M_sum}} 为刚体惯性与附加质量矩阵；{{math:C_nu}} 为科氏力与向心力矩阵；{{math:D_nu}} 为包含线性与二次非线性项的水动力阻尼矩阵；{{math:g_eta}} 为重力与浮力恢复力矩矢量；{{math:tau}} 为推进器产生的广义控制力与力矩矢量；{{math:tau_d}} 为外部扰动项。{{platform_hl}}{{hl}}其中，刚体惯性矩阵 {{math:M_RB}} 与恢复力矩项 {{math:g_eta}} 由平台三维模型与质量属性直接确定；单推进器采用控制输入到推力输出的静态拟合映射关系，并明确推力上下界 {{math:T_interval}}。{{/hl}}{{/platform_hl}}",
        style_type="body", force_hl=False
    )

    if os.path.exists(FIG2_ROV_PATH):
        insert_image_before(
            doc, p_audit, FIG2_ROV_PATH,
            "{{hl}}图 2{{/hl}}  八推进器水下航行器坐标系定义与推力矢量空间布置示意图",
            width_cm=15.2, highlight_diff=highlight_diff, force_hl=False
        )

    _add(
        "{{platform_hl}}{{hl}}考虑便携式水下航行器低速运动特性与机体对称性，忽略次要的非对角交叉水动力耦合项，将附加质量矩阵 {{math:M_A}} 及线性、二次水动力阻尼矩阵简化为对角矩阵，提炼出各自由度待辨识的关键未知水动力参数集 {{math:theta_vec}}。在单自由度特征激励（如阶跃推力或自由衰减）下，将式 (1) 整理为关于未知参数 {{math:theta_vec}} 的参数化辨识方程，利用推力输入与状态响应数据通过最小二乘法或非线性最小二乘曲线拟合求解参数集 {{math:theta_vec}}；随后将辨识参数代回六自由度模型，对比模型仿真输出与验证数据的响应曲线偏差，获得经验证的航行器动力学模型 {{math:model_hats_paren}}。{{/hl}}{{/platform_hl}}",
        style_type="body", force_hl=False
    )

    _add(
        "{{hl}}以辨识验证后的航行器动力学模型为基础{{/hl}}，设参考运动状态为 {{math:eta_r}} 与 {{math:nu_r}}，定义姿态、深度与航向等状态跟踪误差 {{math:e_eta_def}} 及速度误差 {{math:e_nu_def}}。{{hl}}采用“动力学模型特性补偿 + 实时状态误差反馈”的复合闭环控制思路计算期望广义力和力矩 {{math:tau_c_R6}}：{{/hl}}",
        style_type="body", bold_prefix="2） 基于模型与状态反馈的闭环运动控制方法：", force_hl=False
    )
    _add("eq2_ctrl", style_type="formula")
    _add(
        "{{hl}}式中，{{math:F_model}} 为基于辨识动力学模型计算的已知动态特性补偿项（用于前馈抵消重浮力恢复力矩、主导水动力阻尼或惯性耦合效应），{{math:F_fb}} 为基于状态误差的闭环反馈控制项。该设计思路不将控制器锁死于单一固定算法，可根据辨识模型的准确度与控制需求灵活设计具体的模型前馈补偿、反馈线性化或增量动态逆等模型控制形式，并以传统无模型 PID 控制（即 {{math:F_model_zero}}）作为对比基准，开展多工况跟踪与抗流扰性能对比分析。{{/hl}}",
        style_type="body", force_hl=False
    )

    _add(
        "{{platform_hl}}如图 2(b) 所示，已有平台包含水平面 4 台矢量倾斜推进器（{{math:T1_T4}}）与垂直面 4 台垂向对称推进器（{{math:T5_T8}}）。根据第 {{math:i_idx}} 个推进器（{{math:i_1_8}}）在附体系下的安装位置矢量 {{math:r_i_R3}} 与推力方向单位矢量 {{math:d_i_R3}}，构造 {{math:6x8}} 控制分配矩阵 {{math:B_def}}{{/platform_hl}}，并在推进器基本推力输出范围约束下求解各推进器推力指令 {{math:T_vec_R8}}：",
        style_type="body", bold_prefix="3） 八推进器控制分配方法：", force_hl=False
    )
    _add("eq3_alloc", style_type="formula")
    _add(
        "{{hl}}在基础广义逆/加权伪逆求解框架上，引入推进器推力范围 {{math:T_interval}} 约束处理策略（如保方向比例缩放、饱和自由度再分配或有界优化求解），抑制推进器超限引起的合成力矩方向畸变；通过与无约束伪逆直接硬截断基准进行对比，量化分析控制分配残差 {{math:e_tau}} 与各推进器推力饱和情况，再结合单推进器静态推力映射转换为执行机构控制输入。{{/hl}}",
        style_type="body", force_hl=False
    )

    _add(
        "利用PX4模块化软件架构与uORB发布/订阅消息机制，在SITL环境中将辨识验证后的水下航行器动力学模型、运动控制模块与八推进器控制分配模块集成为闭环系统，{{hl}}设置空间定点悬停、姿态稳定、定深控制与定航控制等典型运动工况及适量外部水流扰动条件开展闭环仿真{{/hl}}，综合跟踪误差 {{math:e_eta}}、动态响应指标及控制分配残差 {{math:e_tau}} 验证闭环系统性能。",
        style_type="body", bold_prefix="4） PX4/SITL闭环仿真验证方法：", force_hl=False
    )

    # 2.2 技术路线图与系统仿真结构
    _add("{{hl}}2.2 {{/hl}}技术路线图与系统仿真结构", style_type="h3", force_hl=False)
    _add(
        "本课题的总体研究技术路线{{hl}}如图 3 所示{{/hl}}，基于PX4/SITL的水下航行器闭环仿真系统结构框图{{hl}}如图 4 所示{{/hl}}。",
        style_type="body", force_hl=False
    )

    if os.path.exists(FIG3_ROADMAP_PATH):
        insert_image_before(
            doc, p_audit, FIG3_ROADMAP_PATH, "{{hl}}图 3{{/hl}}  课题总体研究技术路线图",
            width_cm=15.2, highlight_diff=highlight_diff, force_hl=False
        )
    if os.path.exists(FIG4_PX4_PATH):
        insert_image_before(
            doc, p_audit, FIG4_PX4_PATH, "{{hl}}图 4{{/hl}}  基于PX4/SITL的水下航行器闭环仿真系统结构框图",
            width_cm=15.2, highlight_diff=highlight_diff, force_hl=False
        )

    # 2.3 可行性分析
    _add("{{hl}}2.3 {{/hl}}可行性分析", style_type="h3", force_hl=False)
    _add("本课题研究方案的可行性主要体现在以下三个方面：", style_type="body", force_hl=False)
    _add(
        "水下航行器六自由度动力学建模（Fossen模型框架）、系统参数辨识、基于模型与状态反馈的运动控制以及多推进器控制分配矩阵求解均具有成熟完备的理论体系。各研究模块之间物理接口清晰（以运动状态、期望广义力/力矩、各推进器推力指令依次传递），理论方案合理可行。",
        style_type="body", bold_prefix="1） 理论与方法可行性：", force_hl=False
    )
    _add(
        "{{platform_hl}}本课题直接依托实验室已有八推进器{{hl}}便携式{{/hl}}水下航行器平台开展研究，平台几何构型、质量惯性属性、推进器安装布置及相关参数数据具备良好基础，能够为动力学建模、系统辨识、模型验证及八推进器控制分配矩阵建立提供可靠的数据支撑。{{/platform_hl}}",
        style_type="body", bold_prefix="2） 平台与数据基础可行性：", force_hl=False
    )
    _add(
        "PX4开源软件框架提供了完善的SITL软件在环仿真环境、标准化的uORB模块间通信机制以及ULog数据记录工具。前期已完成PX4架构与控制链路调研及基础仿真环境测试，具备在规定时间内完成模块集成与多工况仿真验证的软硬件条件。",
        style_type="body", bold_prefix="3） 软件与仿真环境可行性：", force_hl=False
    )

    # 3. 工作进度安排
    _add("{{hl}}3. {{/hl}}工作进度安排", style_type="h2", force_hl=False)
    _add(
        "根据学校毕业论文总体进程与任务书要求，本课题各阶段工作进度安排如表 2 所示：",
        style_type="body", force_hl=False
    )

    _add("表 2  毕业论文工作进度安排", style_type="table_caption", force_hl=False)
    sched_data = [
        ("序 号", "论文各阶段名称", "时间安排（教学周）"),
        ("1", "课题申报、审核", "2026.7.13~2026.7.24\n（第20~21周）"),
        ("2", "学生选课、选题", "2026.8.4~2026.8.7\n（第23周）"),
        ("3", "下达任务书及任务书审核", "2026.8.17~2026.8.21\n（第25周）"),
        ("4", "编写开题报告、开题答辩、提交开题报告、审核", "2026.9.16~2026.10.9\n（第1~4周）"),
        ("5", "水下航行器动力学与推进器建模、PX4/SITL基础环境搭建", "2026.10.12~2026.11.20\n（第5~10周）"),
        ("6", "系统辨识与模型验证、运动控制方法研究", "2026.11.23~2026.12.25\n（第11~15周）"),
        ("7", "中期检查及中期答辩", "2026.12.28~2027.1.15\n（第16~18周）"),
        ("8", "运动控制、八推进器控制分配及PX4/SITL闭环集成", "2027.2.22~2027.3.12\n（第1~3周）"),
        ("9", "SITL闭环仿真、典型工况验证与结果分析", "2027.3.15~2027.4.2\n（第4~6周）"),
        ("10", "论文撰写与仿真补充", "2027.4.5~2027.4.16\n（第7~8周）"),
        ("11", "论文查重、导师评阅、专家评阅、学生修改完善论文并定稿、毕业答辩", "2027.4.19~2027.4.28\n（第9~10周）"),
        ("12", "论文评优、论文各类资料（书面版和电子版）整理、归档", "2027.5.3~2027.5.14\n（第11~12周）"),
    ]

    tbl_sched = doc.add_table(rows=len(sched_data), cols=3)
    tbl_sched.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_sched)
    set_repeat_table_header(tbl_sched.rows[0])
    for row in tbl_sched.rows:
        set_row_cant_split(row)
    col_widths = [Cm(1.8), Cm(8.8), Cm(4.8)]
    for r_idx, row_tuple in enumerate(sched_data):
        is_header = (r_idx == 0)
        for c_idx, val in enumerate(row_tuple):
            cell = tbl_sched.cell(r_idx, c_idx)
            cell.width = col_widths[c_idx]
            align = WD_ALIGN_PARAGRAPH.CENTER if (is_header or c_idx != 1) else WD_ALIGN_PARAGRAPH.LEFT
            cn_f = "黑体" if is_header else "宋体"
            set_cell_text(
                cell, val, cn_font=cn_f, en_font="Times New Roman",
                size_pt=10.5, bold=is_header, align=align,
                highlight_diff=highlight_diff, force_hl=False
            )
    p_audit._element.addprevious(tbl_sched._tbl)

    # =========================================================================
    # 三、毕业论文的主要参考文献 (严格遵循正文首次出现顺序 [1]~[17], 悬挂缩进 0.74cm = 420 dxa, 无段前段后间距)
    # =========================================================================
    _add("三、毕业论文的主要参考文献", style_type="h1")

    refs = [
        ("[1] 工业和信息化部, 教育部, 公安部, 等. 关于印发《“机器人+”应用行动实施方案》的通知: 工信部联通装〔2022〕187号[EB/OL]. (2023-01-18) [2026-09-28]. http://www.gov.cn/zhengce/zhengceku/2023-01/19/content_5737976.htm.", True),
        ("{{hl}}[2]{{/hl}} Fossen T I. Handbook of Marine Craft Hydrodynamics and Motion Control[M]. 2nd ed. Chichester, UK: John Wiley & Sons, 2021. DOI: 10.1002/9781119575016.", False),
        ("{{hl}}[3]{{/hl}} Caccia M, Indiveri G, Veruggio G. Modeling and identification of open-frame variable configuration unmanned underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 2000, 25(2): 227-240. DOI: 10.1109/48.838986.", False),
        ("{{hl}}[4]{{/hl}} Ross A, Fossen T I, Johansen T A. Identification of underwater vehicle hydrodynamic coefficients using free decay tests[J]. IFAC Proceedings Volumes, 2004, 37(10): 363-368. DOI: 10.1016/S1474-6670(17)31759-7.", False),
        ("{{hl}}[5]{{/hl}} Avila J P J, Donha D C, Adamowski J C. Experimental model identification of open-frame underwater vehicles[J]. Ocean Engineering, 2013, 60: 81-94. DOI: 10.1016/j.oceaneng.2012.10.007.", False),
        ("{{hl}}[6]{{/hl}} Chin C, Lau M. Modeling and testing of hydrodynamic damping model for a complex-shaped remotely-operated vehicle for control[J]. Journal of Marine Science and Application, 2012, 11(2): 150-163. DOI: 10.1007/s11804-012-1117-2.", False),
        ("{{hl}}[7]{{/hl}} 高婷, 庞永杰, 王亚星, 等. 水下航行器水动力系数计算方法[J]. 哈尔滨工程大学学报, 2019, 40(1): 174-180.", False),
        ("[8] von Benzon M, Sørensen F F, Uth E, et al. An Open-Source Benchmark Simulator: Control of a BlueROV2 Underwater Robot[J]. Journal of Marine Science and Engineering, 2022, 10(12): 1898. DOI: 10.3390/jmse10121898.", True),
        ("[9] Fernandes D A, Sørensen A J, Pettersen K Y, Donha D C. Output feedback motion control system for observation class ROVs based on a high-gain state observer: Theoretical and experimental results[J]. Control Engineering Practice, 2015, 39: 90-102. DOI: 10.1016/j.conengprac.2014.12.005.", False),
        ("[10] Chu Z, Xiang X, Zhu D, et al. Adaptive trajectory tracking control for remotely operated vehicles considering thruster dynamics and saturation constraints[J]. ISA Transactions, 2020, 100: 28-37. DOI: 10.1016/j.isatra.2019.11.032.", False),
        ("{{hl}}[11]{{/hl}} Slawik T, Vyas S, Christensen L, et al. Attitude Control of the Hydrobatic Intervention AUV Cuttlefish using Incremental Nonlinear Dynamic Inversion[C]//2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). Abu Dhabi, UAE: IEEE, 2024: 781-787. DOI: 10.1109/IROS58592.2024.10801686.", False),
        ("[12] Johansen T A, Fossen T I. Control allocation—A survey[J]. Automatica, 2013, 49(5): 1087-1103. DOI: 10.1016/j.automatica.2013.01.035.", True),
        ("[13] Fossen T I, Johansen T A. A survey of control allocation methods for ships and underwater vehicles[C]//2006 14th Mediterranean Conference on Control and Automation. Ancona, Italy: IEEE, 2006: 1-6. DOI: 10.1109/MED.2006.328749.", True),
        ("{{hl}}[14]{{/hl}} 程卫平, 王猛, 曾现敏, 等. 基于可行方向法的水下机器人推力分配[J]. 舰船科学技术, 2022, 44(13): 102-106.", False),
        ("{{hl}}[15]{{/hl}} 孙广威, 苏玉玺, 毛义, 等. 基于模糊逻辑的混合推进ROV多级推力分配策略[J]. 机器人, 2023, 45(4): 472-482.", False),
        ("{{hl}}[16]{{/hl}} Meier L, Honegger D, Pollefeys M. PX4: A node-based multithreaded open source robotics framework for deeply embedded platforms[C]//2015 IEEE International Conference on Robotics and Automation (ICRA). Seattle, WA: IEEE, 2015: 6235-6240. DOI: 10.1109/ICRA.2015.7140074.", False),
        ("{{hl}}[17]{{/hl}} Duecker D A, Bauschmann N, Hansen T, et al. HippoCampus X – A hydrobatic open-source micro AUV for confined environments[C]//2020 IEEE/OES Autonomous Underwater Vehicles Symposium (AUV). St. John's, NL, Canada: IEEE, 2020: 1-6. DOI: 10.1109/AUV50043.2020.9267895.", False),
    ]

    for idx, (r_txt, is_hl) in enumerate(refs, start=1):
        _add(r_txt, style_type="ref", ref_index=idx, force_hl=is_hl)

    # 校验正文首次出现文献顺序是否严格为 [1, 2, ..., 17]
    expected_order = list(range(1, len(refs) + 1))
    assert CITATION_TRACKER == expected_order, (
        f"GB/T 7714-2015 顺序编码校验失败！正文首次出现顺序为 {CITATION_TRACKER}，应为 {expected_order}"
    )
    print(f"[OK] GB/T 7714-2015 顺序编码校验通过：正文首次引用顺序 {CITATION_TRACKER}")

    try:
        doc.save(out_docx_path)
        print(f"[OK] 已生成 .docx: {out_docx_path}")
    except PermissionError:
        fallback_path = out_docx_path.replace(".docx", "_新版.docx")
        doc.save(fallback_path)
        print(f"[WARN] 目标文件正在 WPS/Word 中打开被锁定，已自动保存为: {fallback_path}")
        print(f"[TIP] 请在 WPS/Word 中关闭原文件后，新版文件将可自动覆盖或直接替换原文件。")


def convert_docx_to_doc_batch(pairs):
    """使用 Word COM 批量将 .docx 转换为兼容版 .doc (FileFormat=0)"""
    if os.path.exists(OUT_DOC):
        shutil.copy2(OUT_DOC, OUT_DOC + ".bak")
    try:
        import win32com.client as win32
        word = win32.gencache.EnsureDispatch("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        try:
            for docx_path, doc_path in pairs:
                wdoc = word.Documents.Open(docx_path)
                wdoc.Fields.Update()
                target_doc = doc_path
                try:
                    with open(doc_path, "ab"):
                        pass
                except PermissionError:
                    target_doc = doc_path.replace(".doc", "_新版.doc")
                    print(f"[INFO] 原 .doc 文件正在编辑器中打开，自动另存为: {target_doc}")
                wdoc.SaveAs(target_doc, FileFormat=0)
                wdoc.Close(False)
                print(f"[OK] 已同步转换生成兼容版 .doc: {target_doc}")
        finally:
            word.Quit()
    except Exception as e:
        print(f"[WARN] win32com 转换 .doc 异常: {e}")


def archive_previous_diff(description=""):
    """
    若开题报告根目录下已存在旧的修改对比版，在生成新对比版前将其归档至
    '开题报告/归档/历次修改对比版/'，并打上时间戳快照。
    """
    if not os.path.exists(DIFF_DOCX):
        return None
    import datetime
    mtime = os.path.getmtime(DIFF_DOCX)
    date_str = datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d_%H%M%S")
    desc_part = f"_{description}" if description else ""
    archived_name = f"开题报告-新旧版本修改对比版_逐段差异高亮_{date_str}{desc_part}.docx"
    archived_path = os.path.join(DIFF_HISTORY_DIR, archived_name)
    shutil.copy2(DIFF_DOCX, archived_path)
    print(f"[INFO] 已将上一版修改对比版归档至: {archived_path}")
    return archived_path


def build_document(generate_doc=False, generate_diff=False, generate_senior=True, archive_old_diff=False, diff_desc=""):
    # 0. 若明确指定生成新修改对比版且需归档
    if generate_diff and archive_old_diff:
        archive_previous_diff(diff_desc)

    # 1. 构建正式提交纯净版 (.docx) —— 100% 无任何高亮
    build_single_docx(OUT_DOCX, highlight_mode="none")

    # 2. 构建实验室学长审阅确认版 (.docx) —— 仅将涉及实验室已有平台/数据的内容标黄
    if generate_senior:
        build_single_docx(SENIOR_DOCX, highlight_mode="platform")

    # 3. 仅在明确指定时才构建修改对比高亮版 (避免意外覆盖用户手动标注版)
    if generate_diff:
        build_single_docx(DIFF_DOCX, highlight_mode="diff")

    # 4. 仅在明确指定时才使用 Word COM 批量转换为 .doc 并输出至归档/历史DOC版本/
    if generate_doc:
        pairs = [(OUT_DOCX, OUT_DOC)]
        if generate_diff:
            pairs.append((DIFF_DOCX, DIFF_DOC))
        convert_docx_to_doc_batch(pairs)
    else:
        print("[INFO] 默认模式：仅生成 .docx 文档。如需同步导出 .doc 请添加参数 --doc (将保存至 归档/历史DOC版本/)")


if __name__ == "__main__":
    gen_doc = ("--doc" in sys.argv or "--all" in sys.argv)
    gen_diff = ("--diff" in sys.argv or "--all" in sys.argv)
    gen_senior = ("--no-senior" not in sys.argv)
    archive_old = ("--archive-old-diff" in sys.argv)
    build_document(generate_doc=gen_doc, generate_diff=gen_diff, generate_senior=gen_senior, archive_old_diff=archive_old)
