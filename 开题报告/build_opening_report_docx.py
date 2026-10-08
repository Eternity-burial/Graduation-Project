# -*- coding: utf-8 -*-
"""
开题报告 Word (.docx) 官方模板复制与就地内容填充构建脚本
遵循用户铁律：严格以模板为基础，进行内容填充，绝非照着模板格式新建，而是复制后对模板进行填充。

构建流程：
1. 复制学校官方空白模板 模板/2毕业设计(论文)开题报告.docx 到目标文件；
2. 打开复制出的文档对象；
3. 就地填充封面表格 Table 0 与日期表格 Table 1（严格遵守 vAlign="bottom"、单倍行距、无段间距、四号宋体）；
4. 就地更新原模板骨架标题（保留原有 XML 属性、原生硬分页符与原生样式）；
5. 在对应章节骨架节点处精准插入正文、三/四级标题、技术路线图高清图表、三线进度安排表与 45 篇参考文献；
6. 干净清理原模板中的空占位段落与填写说明提示段落；
7. 原生保留四、审核意见及其审核意见表 Table 2；
8. 执行完整的格式合规与学术规范验证。
"""

import os
import sys
import re
import shutil

sys.stdout.reconfigure(encoding="utf-8")

import docx
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

# 路径常量
TEMPLATE_DOCX = r"模板/2毕业设计(论文)开题报告.docx"
MARKDOWN_DRAFT = r"开题报告/开题报告_正文起草稿.md"
ROADMAP_FIGURE = r"开题报告/figures/fig_technical_roadmap.png"
OUTPUT_DOCX = r"开题报告/开题报告-基于PX4的水下航行器模型控制方法研究.docx"


# ==================== XML 样式辅助函数 ====================

def set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=10.5, bold=False, italic=False, color=None):
    """同时精确设置中西文字体、字号与样式属性（默认五号 10.5 pt，对齐杨佳轩学长终稿）"""
    run.font.name = western_font
    run.font.size = Pt(font_size_pt)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color

    # 通过 oxml 设置中文字体 (eastAsia)
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    rFonts.set(qn("w:ascii"), western_font)
    rFonts.set(qn("w:hAnsi"), western_font)
    rFonts.set(qn("w:cs"), western_font)
    rFonts.set(qn("w:eastAsia"), chinese_font)


def set_paragraph_spacing(paragraph, line_pt=18.0, line_rule="exact", before_pt=0.0, after_pt=0.0, before_lines=None, after_lines=None):
    """设置段落行距与段前段后间距（默认固定值 18 磅 line=360 exact，支持磅值与行数，严格对齐杨佳轩学长规范）"""
    pPr = paragraph._p.get_or_add_pPr()
    sp = pPr.find(qn("w:spacing"))
    if sp is None:
        sp = OxmlElement("w:spacing")
        pPr.append(sp)

    # 固定值 18 磅对应 line="360" lineRule="exact"
    sp.set(qn("w:line"), str(int(line_pt * 20)))
    sp.set(qn("w:lineRule"), line_rule)

    if before_lines is not None:
        sp.set(qn("w:beforeLines"), str(int(before_lines * 100)))
        sp.set(qn("w:before"), str(int(before_lines * 240)))
    else:
        if qn("w:beforeLines") in sp.attrib:
            del sp.attrib[qn("w:beforeLines")]
        sp.set(qn("w:before"), str(int(before_pt * 20)))

    if after_lines is not None:
        sp.set(qn("w:afterLines"), str(int(after_lines * 100)))
        sp.set(qn("w:after"), str(int(after_lines * 240)))
    else:
        if qn("w:afterLines") in sp.attrib:
            del sp.attrib[qn("w:afterLines")]
        sp.set(qn("w:after"), str(int(after_pt * 20)))




def set_image_paragraph_format(paragraph, before_pt=6.0, after_pt=2.0):
    """
    专门设置图片所在段落的格式：
    1. 居中对齐；
    2. 单倍行距，XML 严格设为 lineRule="auto" line="240"，绝不使用 exact 固定值（防止图片被裁剪或覆盖）；
    3. 段前段后间距；
    4. 显式开启 keepNext（keep_with_next = True），保证图片与下方的图题绝不跨页分裂！
    """
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.keep_with_next = True

    pPr = paragraph._p.get_or_add_pPr()
    if pPr.find(qn("w:keepNext")) is None:
        pPr.append(OxmlElement("w:keepNext"))

    sp = pPr.find(qn("w:spacing"))
    if sp is None:
        sp = OxmlElement("w:spacing")
        pPr.append(sp)
    sp.set(qn("w:line"), "240")
    sp.set(qn("w:lineRule"), "auto")
    if qn("w:beforeLines") in sp.attrib:
        del sp.attrib[qn("w:beforeLines")]
    if qn("w:afterLines") in sp.attrib:
        del sp.attrib[qn("w:afterLines")]
    sp.set(qn("w:before"), str(int(before_pt * 20)))
    sp.set(qn("w:after"), str(int(after_pt * 20)))

    ind = pPr.find(qn("w:ind"))
    if ind is not None:
        pPr.remove(ind)


def set_paragraph_indent(paragraph, first_line_dxa=420, first_line_chars=200):
    """设置首行缩进 2 字符 (五号字对应 420 dxa = 21 pt)"""
    pPr = paragraph._p.get_or_add_pPr()
    ind = pPr.find(qn("w:ind"))
    if ind is None:
        ind = OxmlElement("w:ind")
        pPr.append(ind)
    ind.set(qn("w:firstLine"), str(first_line_dxa))
    ind.set(qn("w:firstLineChars"), str(first_line_chars))
    if qn("w:left") in ind.attrib:
        del ind.attrib[qn("w:left")]
    if qn("w:hanging") in ind.attrib:
        del ind.attrib[qn("w:hanging")]


def set_paragraph_no_indent(paragraph):
    """顶格无缩进"""
    pPr = paragraph._p.get_or_add_pPr()
    ind = pPr.find(qn("w:ind"))
    if ind is None:
        ind = OxmlElement("w:ind")
        pPr.append(ind)
    ind.set(qn("w:firstLine"), "0")
    ind.set(qn("w:firstLineChars"), "0")
    if qn("w:left") in ind.attrib:
        del ind.attrib[qn("w:left")]
    if qn("w:hanging") in ind.attrib:
        del ind.attrib[qn("w:hanging")]


def set_paragraph_hanging_indent(paragraph, left_dxa=420, hanging_dxa=420):
    """设置参考文献悬挂缩进 2 汉字符 (420 dxa = 21 pt)"""
    pPr = paragraph._p.get_or_add_pPr()
    ind = pPr.find(qn("w:ind"))
    if ind is None:
        ind = OxmlElement("w:ind")
        pPr.append(ind)
    ind.set(qn("w:left"), str(left_dxa))
    ind.set(qn("w:hanging"), str(hanging_dxa))
    if qn("w:firstLine") in ind.attrib:
        del ind.attrib[qn("w:firstLine")]
    if qn("w:firstLineChars") in ind.attrib:
        del ind.attrib[qn("w:firstLineChars")]


def add_text_with_superscripts(paragraph, text, chinese_font="宋体", western_font="Times New Roman", font_size_pt=10.5, default_bold=False):
    """
    智能解析 Markdown 正文中的上标（如 $^{[1]}$、$^{[1][2]}$）与普通文字，
    并自动拆分为正文 Run 和上标 Run。
    正文段落统一以统一字体与常规字重排版，绝不在段落内部产生孤立的加粗或黑体。
    """
    # 替换 LaTeX 箭头为标准中文符号
    clean_text = text.replace(r"$\rightarrow$", "→").replace(r"\rightarrow", "→")

    # 去除任何残留的 Markdown 粗体标记 **...**，还原为纯净文字
    clean_text = clean_text.replace("**", "")

    # 正则切分：识别 $^{[数字等]}$ 或 $^\{...\}$
    pattern = re.compile(r'(\$\^\{[^}]+\}\$)')
    tokens = pattern.split(clean_text)

    for token in tokens:
        if not token:
            continue
        if token.startswith("$^{") and token.endswith("}$"):
            # 上标内容，如 $^{[1]}$ -> [1]
            sup_content = token[3:-2].strip()
            run = paragraph.add_run(sup_content)
            set_run_font(run, chinese_font=chinese_font, western_font=western_font, font_size_pt=font_size_pt, bold=default_bold)
            run.font.superscript = True
        else:
            run = paragraph.add_run(token)
            set_run_font(run, chinese_font=chinese_font, western_font=western_font, font_size_pt=font_size_pt, bold=default_bold)


# ==================== 表格边框与对齐辅助函数 ====================

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """设置单元格内部边距 (dxa)"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_cell_valign(cell, valign="center"):
    """设置单元格垂直对齐：'bottom' 或 'center'"""
    tcPr = cell._tc.get_or_add_tcPr()
    for old_v in tcPr.findall(qn("w:vAlign")):
        tcPr.remove(old_v)
    vAlign_el = OxmlElement("w:vAlign")
    vAlign_el.set(qn("w:val"), valign)
    tcPr.append(vAlign_el)


def set_three_line_borders(table):
    """设置标准三线表边框：顶线 1.5 pt (12 dxa)，表头底线 0.75 pt (6 dxa)，底线 1.5 pt (12 dxa)"""
    tblPr = table._tbl.tblPr
    tblBorders = tblPr.find(qn('w:tblBorders'))
    if tblBorders is not None:
        tblPr.remove(tblBorders)
    tblBorders = OxmlElement('w:tblBorders')

    # 顶线
    top = OxmlElement('w:top')
    top.set(qn('w:val'), 'single')
    top.set(qn('w:sz'), '12')  # 1.5 pt
    top.set(qn('w:space'), '0')
    top.set(qn('w:color'), '000000')
    tblBorders.append(top)

    # 底线
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '12')  # 1.5 pt
    bottom.set(qn('w:space'), '0')
    bottom.set(qn('w:color'), '000000')
    tblBorders.append(bottom)

    # 清除左、右、垂直内边框
    for b_name in ['left', 'right', 'insideV']:
        b = OxmlElement(f'w:{b_name}')
        b.set(qn('w:val'), 'none')
        tblBorders.append(b)

    # 内部水平线清除
    insideH = OxmlElement('w:insideH')
    insideH.set(qn('w:val'), 'none')
    tblBorders.append(insideH)

    tblPr.append(tblBorders)

    # 为首行（表头）的每个单元格添加 0.75 pt (6 dxa) 的底线
    for cell in table.rows[0].cells:
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = tcPr.find(qn('w:tcBorders'))
        if tcBorders is None:
            tcBorders = OxmlElement('w:tcBorders')
            tcPr.append(tcBorders)
        bottom = OxmlElement('w:bottom')
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '6')  # 0.75 pt
        bottom.set(qn('w:space'), '0')
        bottom.set(qn('w:color'), '000000')
        tcBorders.append(bottom)


def set_table_header(row):
    """设置表格首行跨页自动重复表头"""
    trPr = row._tr.get_or_add_trPr()
    tblHeader = trPr.find(qn('w:tblHeader'))
    if tblHeader is None:
        tblHeader = OxmlElement('w:tblHeader')
        trPr.append(tblHeader)


# ==================== 核心构建主流程 ====================

def populate_section_paragraphs(anchor_p, markdown_section_text, is_ref_section=False):
    """
    将特定小节的 Markdown 文本解析并依次插入到 anchor_p 之前。
    anchor_p 为该小节之后的下一个骨架标题段落。
    """
    lines = markdown_section_text.splitlines()
    in_code_block = False

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped == "---":
            continue

        # 跳过 Markdown 标题注释与引用提示
        if stripped.startswith("# 《基于PX4") or stripped.startswith(">"):
            continue

        # 跳过 ASCII 流程图代码块
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # 彻底清洗行首的 Markdown 列表符号（如 '- ', '* ', '+ '）
        if stripped.startswith("- ") or stripped.startswith("* ") or stripped.startswith("+ "):
            stripped = stripped[2:].strip()

        # 参考文献条目：[1] ... / [45] ...
        if is_ref_section and stripped.startswith("["):
            p_ref = anchor_p.insert_paragraph_before()
            p_ref.style = "Normal"
            # 严格依据杨佳轩学长终稿规范：参考文献五号字 (10.5 pt)，固定值 18 磅行距，零段间距，悬挂缩进 2 字符 (420 dxa)
            set_paragraph_spacing(p_ref, line_pt=18.0, line_rule="exact", before_pt=0.0, after_pt=0.0)
            set_paragraph_hanging_indent(p_ref, left_dxa=420, hanging_dxa=420)
            add_text_with_superscripts(p_ref, stripped, chinese_font="宋体", western_font="Times New Roman", font_size_pt=10.5)
            continue

        # 三级标题：#### 2.1 ... / #### 1.1 ... / #### （1）...
        if stripped.startswith("#### "):
            h3_text = stripped[5:].strip()
            if "课题进度安排与阶段成果表" in h3_text:
                continue
            p_h3 = anchor_p.insert_paragraph_before()
            p_h3.style = "Normal"
            set_paragraph_spacing(p_h3, line_pt=18.0, line_rule="exact", before_pt=7.8, after_pt=3.9)
            set_paragraph_indent(p_h3, first_line_dxa=420, first_line_chars=200)
            run = p_h3.add_run(h3_text)
            set_run_font(run, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)
            continue

        # 四级/占行标题：##### （1）... / ##### （2）...
        if stripped.startswith("##### "):
            h4_text = stripped[6:].strip()
            p_h4 = anchor_p.insert_paragraph_before()
            p_h4.style = "Normal"
            set_paragraph_spacing(p_h4, line_pt=18.0, line_rule="exact", before_pt=0.0, after_pt=0.0)
            set_paragraph_indent(p_h4, first_line_dxa=420, first_line_chars=200)
            run = p_h4.add_run(h4_text)
            set_run_font(run, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)
            continue

        # 进度表格：由独立逻辑插入，跳过 markdown 表格文本
        if stripped.startswith("|") and ("阶段" in stripped or "---" in stripped or "阶段一" in stripped or "阶段二" in stripped or "阶段三" in stripped or "阶段四" in stripped or "阶段五" in stripped):
            continue

        # 技术路线图引导文字与插图处理
        if "课题总体技术路线流程如下所示" in stripped or "课题总体技术路线流程如下" in stripped:
            p_lead = anchor_p.insert_paragraph_before()
            p_lead.style = "Normal"
            set_paragraph_spacing(p_lead, line_pt=18.0, line_rule="exact", before_pt=0.0, after_pt=0.0)
            set_paragraph_indent(p_lead, first_line_dxa=420, first_line_chars=200)
            run = p_lead.add_run("课题总体技术路线如图 1 所示：")
            set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=10.5)

            # 插入高清技术路线图（严格设置居中、单倍行距auto、keepNext防跨页拆散、宽14.5cm）
            if os.path.exists(ROADMAP_FIGURE):
                p_img = anchor_p.insert_paragraph_before()
                p_img.style = "Normal"
                set_image_paragraph_format(p_img, before_pt=6.0, after_pt=2.0)
                r_img = p_img.add_run()
                r_img.add_picture(ROADMAP_FIGURE, width=Cm(14.5))

                # 图题段落：五号黑体加粗，单倍行距或固定值18磅，段前2pt段后6pt，居中
                p_fig_caption = anchor_p.insert_paragraph_before()
                p_fig_caption.style = "Normal"
                p_fig_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_paragraph_spacing(p_fig_caption, line_pt=18.0, line_rule="exact", before_pt=2.0, after_pt=6.0)
                run = p_fig_caption.add_run("图 1 课题总体研究技术路线流程图")
                set_run_font(run, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)
            continue

        # 普通正文段落
        p_body = anchor_p.insert_paragraph_before()
        p_body.style = "Normal"
        set_paragraph_spacing(p_body, line_pt=18.0, line_rule="exact", before_pt=0.0, after_pt=0.0)
        set_paragraph_indent(p_body, first_line_dxa=420, first_line_chars=200)
        add_text_with_superscripts(p_body, stripped, chinese_font="宋体", western_font="Times New Roman", font_size_pt=10.5)


def insert_progress_table(anchor_p, doc):
    """在 anchor_p 之前插入规范的三线进度安排表"""
    # 1. 插入表题段落
    p_tbl_caption = anchor_p.insert_paragraph_before()
    p_tbl_caption.style = "Normal"
    p_tbl_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_spacing(p_tbl_caption, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.2)
    run = p_tbl_caption.add_run("表 1 课题进度安排与阶段成果表")
    set_run_font(run, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)

    # 2. 插入表格数据
    tbl_data = [
        ["阶段序号", "起止时间（教学周）", "主要研究工作内容", "拟达成的阶段性成果与交付物"],
        ["阶段一", "2026.09.16 ~ 2026.10.09\n（第 1 ~ 4 周）",
         "查阅国内外经典文献与行业标准，比选技术路线与方案，完成开题报告撰写与论证",
         "提交开题报告正式文本，完成开题答辩 PPT 汇报并通过开题答辩"],
        ["阶段二", "2026.10.12 ~ 2026.11.20\n（第 5 ~ 10 周）",
         "建立六自由度机理动力学方程，计算刚体质量惯性参数，配置 PX4/SITL 水动力仿真环境",
         "完成动力学模型方程推导，建立参数化的 SITL 仿真工程基座"],
        ["阶段三", "2026.11.23 ~ 2027.01.15\n（第 11 ~ 18 周）",
         "设计水池阶跃与衰减试验工况，采集板载响应数据，利用动量滤波回归提取参数并校验残差；总结阶段性进展",
         "提取水动力阻尼与有效惯性参数，完成模型残差校验；提交中期报告并通过中期答辩"],
        ["阶段四", "2027.02.22 ~ 2027.04.02\n（第 1 ~ 6 周）",
         "在 PX4 底层嵌入动力学模型前馈补偿算法，构建力矩优先分配机制，开展 SITL 与水池实机消融对比测试",
         "完成控制与分配算法工程代码开发，获取消融对比测试曲线与评估数据指标"],
        ["阶段五", "2027.04.05 ~ 2027.05.14\n（第 7 ~ 12 周）",
         "提炼全周期研究成果，绘制学术图表，撰写并修改毕业论文，参加盲审与毕业答辩，完成资料归档",
         "提交符合学术规范的毕业论文正稿，通过论文查重与盲审，完成毕业答辩与材料归档"],
    ]

    tbl = doc.add_table(rows=len(tbl_data), cols=4)
    # 将表格移动到 anchor_p 之前
    anchor_p._p.addprevious(tbl._tbl)

    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_three_line_borders(tbl)
    set_table_header(tbl.rows[0])

    col_widths = [Cm(1.8), Cm(3.6), Cm(5.0), Cm(4.8)]

    for r_idx, row in enumerate(tbl.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx]
            set_cell_valign(cell, valign="center")
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)

            cell_text = tbl_data[r_idx][c_idx]
            cell.text = ""
            p_c = cell.paragraphs[0]
            p_c.paragraph_format.line_spacing = 1.2
            p_c.paragraph_format.space_before = Pt(2)
            p_c.paragraph_format.space_after = Pt(2)

            if r_idx == 0:
                p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p_c.add_run(cell_text)
                set_run_font(run, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)
            else:
                if c_idx in [0, 1]:
                    p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run = p_c.add_run(cell_text)
                    set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=9.5, bold=(c_idx == 0))
                else:
                    p_c.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    run = p_c.add_run(cell_text)
                    set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=9.5, bold=False)

    # 紧随空行间隔
    p_space = anchor_p.insert_paragraph_before()
    p_space.style = "Normal"
    set_paragraph_spacing(p_space, line_pt=12.0, line_rule="exact", before_pt=0, after_pt=0)


def build_opening_report():
    print("=" * 60)
    print("【开题报告构建】基于官方模板复制并就地填充内容")
    print("=" * 60)

    # 1. 严格以模板为基础：物理复制模板文件
    if not os.path.exists(TEMPLATE_DOCX):
        raise FileNotFoundError(f"未找到学校官方空白模板：{TEMPLATE_DOCX}")

    if os.path.exists(OUTPUT_DOCX):
        bak_path = OUTPUT_DOCX + ".bak"
        shutil.copy2(OUTPUT_DOCX, bak_path)
        print(f"已创建旧版本备份：{bak_path}")

    print(f"正在复制官方空白模板：{TEMPLATE_DOCX} -> {OUTPUT_DOCX}")
    shutil.copy2(TEMPLATE_DOCX, OUTPUT_DOCX)

    # 2. 打开刚刚复制出的文档对象进行就地填充
    print(f"正在打开复制后的文档：{OUTPUT_DOCX}")
    doc = docx.Document(OUTPUT_DOCX)

    # 显式保护封面大标题段落 P 5（"毕业设计(论文)开题报告"，字号 36 pt），设定为单倍行距自适应，绝不使用固定值（防止36磅大字被截断裁剪）
    p_cover_title = doc.paragraphs[5]
    pPr_cover = p_cover_title._p.get_or_add_pPr()
    sp_cover = pPr_cover.find(qn("w:spacing"))
    if sp_cover is None:
        sp_cover = OxmlElement("w:spacing")
        pPr_cover.append(sp_cover)
    sp_cover.set(qn("w:line"), "240")
    sp_cover.set(qn("w:lineRule"), "auto")

    # 3. 就地填充封面表格 Table 0
    print("正在就地填充封面表格 Table 0...")
    t0 = doc.tables[0]

    # R0: 课题名称
    cell_title = t0.rows[0].cells[1]
    cell_title.text = ""
    p = cell_title.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("基于PX4的水下航行器模型控制方法研究")
    set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=14.0, bold=False)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    set_cell_valign(cell_title, valign="bottom")

    # R2: 学院
    cell_dept = t0.rows[2].cells[1]
    cell_dept.text = ""
    p = cell_dept.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("机械工程与机器人学院")
    set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=14.0, bold=False)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    set_cell_valign(cell_dept, valign="bottom")

    # R3: 专业
    cell_major = t0.rows[3].cells[1]
    cell_major.text = ""
    p = cell_major.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("机械设计制造及其自动化")
    set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=14.0, bold=False)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    set_cell_valign(cell_major, valign="bottom")

    # R4: 姓名与学号
    cell_name = t0.rows[4].cells[1]
    cell_name.text = ""
    p = cell_name.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("张卫恒")
    set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=14.0, bold=False)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    set_cell_valign(cell_name, valign="bottom")

    cell_sid = t0.rows[4].cells[3]
    cell_sid.text = ""
    p = cell_sid.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("2352407")
    set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=14.0, bold=False)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    set_cell_valign(cell_sid, valign="bottom")

    # 确保 Table 0 所有单元格均为 bottom 对齐
    for row in t0.rows:
        for cell in row.cells:
            set_cell_valign(cell, valign="bottom")

    # 4. 就地填充日期表格 Table 1
    print("正在就地填充日期表格 Table 1...")
    t1 = doc.tables[1]
    t1.rows[0].cells[0].text = "2026"
    t1.rows[0].cells[2].text = "10"
    t1.rows[0].cells[4].text = "9"
    for cell in t1.rows[0].cells:
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            for r in p.runs:
                set_run_font(r, chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0)
        set_cell_valign(cell, valign="bottom")

    # 5. 读取 Markdown 草稿并切分各小节
    print(f"正在读取 Markdown 草稿：{MARKDOWN_DRAFT}")
    with open(MARKDOWN_DRAFT, "r", encoding="utf-8") as f:
        md_text = f.read()

    sec_1_1 = md_text.split("### 1．课题来源及研究的目的和意义")[1].split("### 2．国内外在该方向的研究现状和发展趋势")[0]
    sec_1_2 = md_text.split("### 2．国内外在该方向的研究现状和发展趋势")[1].split("## 二、毕业设计（论文）方案介绍")[0]
    sec_2_1 = md_text.split("### 1．主要研究内容")[1].split("### 2．研究方案")[0]
    sec_2_2 = md_text.split("### 2．研究方案")[1].split("### 3．工作进度安排")[0]
    sec_2_3 = md_text.split("### 3．工作进度安排")[1].split("## 三、毕业设计（论文）的主要参考文献")[0]
    sec_3_ref = md_text.split("## 三、毕业设计（论文）的主要参考文献")[1].split("## 四、审核意见")[0]

    # 6. 定位原模板骨架标题段落并微调标题文字（保留原有 XML 属性、原生硬分页符）
    p16_h1_1 = doc.paragraphs[16]  # 一、毕业设计（论文）课题背景
    p17_note1 = doc.paragraphs[17] # 提示说明
    p18_note2 = doc.paragraphs[18] # 提示说明
    p19_h2_1 = doc.paragraphs[19]  # 1．课题来源及研究的目的和意义
    p20_empty1 = doc.paragraphs[20]
    p21_h2_2 = doc.paragraphs[21]  # 2．国内外在该方向的研究现状和发展趋势\t
    p22_empty2 = doc.paragraphs[22]
    p23_h1_2 = doc.paragraphs[23]  # 二、毕业设计（论文）方案介绍
    p24_h2_3 = doc.paragraphs[24]  # 1．主要研究内容...
    p25_empty3 = doc.paragraphs[25]
    p26_h2_4 = doc.paragraphs[26]  # 2．研究方案...
    p27_empty4 = doc.paragraphs[27]
    p28_h2_5 = doc.paragraphs[28]  # 3．工作进度安排
    p29_empty5 = doc.paragraphs[29]
    p30_h1_3 = doc.paragraphs[30]  # 三、毕业设计（论文）的主要参考文献
    p31_empty6 = doc.paragraphs[31]
    p32_empty7 = doc.paragraphs[32]
    p33_empty8 = doc.paragraphs[33]
    p34_h1_4 = doc.paragraphs[34]  # 四、审核意见

    # 原模板占位段落清理列表
    placeholders_to_remove = [
        p17_note1, p18_note2, p20_empty1, p22_empty2, p25_empty3,
        p27_empty4, p29_empty5, p31_empty6, p32_empty7, p33_empty8
    ]

    print("正在就地校准模板骨架标题文字与样式（严格对齐杨佳轩学长终稿规范）...")
    # 一级标题 1：P 16（保留原生硬分页符 run 0，四号黑体 14 pt，固定值 18 磅，首行缩进 2 字符 560 dxa）
    p16_h1_1.runs[2].text = "毕业论文"
    set_paragraph_spacing(p16_h1_1, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.5)
    set_paragraph_indent(p16_h1_1, first_line_dxa=560, first_line_chars=200)

    # 二级标题 1：P 19（五号黑体 10.5 pt，固定值 18 磅，顶格无缩进，段前段后 0.5 行）
    p19_h2_1.runs[1].text = "． "
    set_paragraph_spacing(p19_h2_1, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.5)
    set_paragraph_no_indent(p19_h2_1)
    for r in p19_h2_1.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)

    # 二级标题 2：P 21（五号黑体 10.5 pt，固定值 18 磅，顶格无缩进，段前段后 0.5 行）
    p21_h2_2.runs[1].text = "． 国内外在该方向的研究现状"
    p21_h2_2.runs[3].text = ""  # 清除末尾制表符
    set_paragraph_spacing(p21_h2_2, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.5)
    set_paragraph_no_indent(p21_h2_2)
    for r in p21_h2_2.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)

    # 一级标题 2：P 23（四号黑体 14 pt，固定值 18 磅，首行缩进 2 字符 560 dxa）
    p23_h1_2.runs[1].text = "毕业论文"
    set_paragraph_spacing(p23_h1_2, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.5)
    set_paragraph_indent(p23_h1_2, first_line_dxa=560, first_line_chars=200)

    # 二级标题 3：P 24（五号黑体 10.5 pt，固定值 18 磅，顶格无缩进，段前段后 0.5 行）
    p24_h2_3.runs[1].text = "． "
    p24_h2_3.runs[3].text = ""  # 清除括号说明
    set_paragraph_spacing(p24_h2_3, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.5)
    set_paragraph_no_indent(p24_h2_3)
    for r in p24_h2_3.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)

    # 二级标题 4：P 26（五号黑体 10.5 pt，固定值 18 磅，顶格无缩进，段前段后 0.5 行）
    p26_h2_4.runs[1].text = "． "
    p26_h2_4.runs[3].text = ""  # 清除括号说明
    set_paragraph_spacing(p26_h2_4, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.5)
    set_paragraph_no_indent(p26_h2_4)
    for r in p26_h2_4.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)

    # 二级标题 5：P 28（五号黑体 10.5 pt，固定值 18 磅，顶格无缩进，段前段后 0.5 行）
    p28_h2_5.runs[1].text = "． "
    set_paragraph_spacing(p28_h2_5, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.5)
    set_paragraph_no_indent(p28_h2_5)
    for r in p28_h2_5.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)

    # 一级标题 3：P 30（四号黑体 14 pt，固定值 18 磅，首行缩进 2 字符 560 dxa）
    p30_h1_3.runs[1].text = "毕业论文"
    set_paragraph_spacing(p30_h1_3, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.5)
    set_paragraph_indent(p30_h1_3, first_line_dxa=560, first_line_chars=200)

    # 一级标题 4：P 34（四号黑体 14 pt，固定值 18 磅，首行缩进 2 字符 560 dxa）
    set_paragraph_spacing(p34_h1_4, line_pt=18.0, line_rule="exact", before_lines=0.5, after_lines=0.5)
    set_paragraph_indent(p34_h1_4, first_line_dxa=560, first_line_chars=200)

    # 7. 分别在对应骨架锚点前注入各小节正文内容
    print("正在注入 §1.1 课题来源及研究的目的和意义...")
    populate_section_paragraphs(p21_h2_2, sec_1_1)

    print("正在注入 §1.2 国内外在该方向的研究现状和发展趋势...")
    populate_section_paragraphs(p23_h1_2, sec_1_2)

    print("正在注入 §2.1 主要研究内容...")
    populate_section_paragraphs(p26_h2_4, sec_2_1)

    print("正在注入 §2.2 研究方案（含技术路线图与可行性分析）...")
    populate_section_paragraphs(p28_h2_5, sec_2_2)

    print("正在注入 §2.3 工作进度安排（含进度三线表）...")
    populate_section_paragraphs(p30_h1_3, sec_2_3)
    insert_progress_table(p30_h1_3, doc)

    print("正在注入 §3 毕业论文的主要参考文献（45 篇顺序编码）...")
    populate_section_paragraphs(p34_h1_4, sec_3_ref, is_ref_section=True)

    # 8. 清理原模板中的空占位段落与填写说明提示段落
    print(f"正在移除原模板中 {len(placeholders_to_remove)} 个空占位与提示段落...")
    for p_ph in placeholders_to_remove:
        p_ph._element.getparent().remove(p_ph._element)

    # 9. 保存填充完毕的 Word 文档
    print(f"正在保存已填充的开题报告文档：{OUTPUT_DOCX}")
    doc.save(OUTPUT_DOCX)
    print(">>> 开题报告构建完成！<<<")


if __name__ == "__main__":
    build_opening_report()
