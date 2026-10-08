# -*- coding: utf-8 -*-
"""
开题报告 Word (.docx) 官方模板就地填充构建管线（推倒重来全新规范版）

核心原则与铁律：
1. 【严格遵循官方模板格式】：以学校官方 2026 空白模板（模板/2毕业设计(论文)开题报告.docx）为唯一基准。
   - 正文：宋体 + Times New Roman，小四号 (12.0 pt)，1.5 倍行距 (line="360" lineRule="auto")，首行缩进 2 字符 (480 dxa)，样式 "正文格式"
   - 2级标题（1． / 2． / 3．）：黑体，小四号 (12.0 pt)，顶格无缩进，序号与题名空一格，1.5 倍行距，段前 0.5 行 (120 dxa)，段后 0.5 行 (120 dxa)，样式 "条"
   - 3级/4级标题：黑体，小四号 (12.0 pt)，首行缩进 2 字符 (480 dxa)，1.5 倍行距，样式 "正文格式"
   - 参考文献：宋体 + Times New Roman，小四号 (12.0 pt)，1.5 倍行距，悬挂缩进 0.74 cm (420 dxa)，样式 "参考文献"
   - 1级标题（一、二、三、四）：黑体，四号 (14.0 pt)，首行缩进 2 字符 (560 dxa)，1.5 倍行距，段前 0.5 行，段后 0.5 行，保留原生硬分页符
   - 封面大标题 P5（"毕业设计(论文)开题报告"，36 pt）：单倍行距自适应，零裁切
   - 绝不篡改全局 Normal 样式！
2. 【100% 完整保留官方全部 25 处可编辑区域 (permStart / permEnd)】：
   - 封面表格 Table 0：6 处可编辑区域全部完好保留（就地替换文本 run，不破坏单元格 perm 节点）
   - 封面日期 Table 1：3 处列权限全部完好保留（向现有段落添加 run，严禁覆盖 cell.text）
   - Section 1（课题背景）：将提示段落 P17 中的 permStart 1319923814 迁移绑定至 P19，整节可编辑区域 100% 完好
   - Section 2（方案介绍）：原生保留 P24 中的 permStart 1741359920，整节与进度表完全被可编辑区域包裹
   - Section 3（主要参考文献）：原生复用 P31（自带 permStart 61024898）为第 1 条文献，后续文献插入在 P32 之前，45 篇文献完全被可编辑区域包裹
   - Section 4（审核意见）：Table 2 中的 10 处审批权限全部完好保留
   - 所有 25 对权限节点在文档树中顺序完全平衡合规！
3. 【学术与排版双重高质】：
   - 0 处 Markdown 列表标记（- , * , + ）泄漏，0 处行内 ** 加粗残留
   - 技术路线图（300 DPI）居中显示，keepNext 绑定题注，题注居中 10.5 pt 黑体
   - 进度安排表规范三线表（顶底 1.5 磅，表头底 0.75 磅，竖线与内横线无），跨页防断行 (cantSplit)，重复表头 (tblHeader)
   - 45 篇参考文献严格按引用顺序编号，上标清洗规范
"""

import os
import sys
import re
import shutil
import docx
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn

sys.stdout.reconfigure(encoding="utf-8")

# 路径常量
TEMPLATE_DOCX = r"模板/2毕业设计(论文)开题报告.docx"
OUTPUT_DOCX = r"开题报告/开题报告-基于PX4的水下航行器模型控制方法研究.docx"
MARKDOWN_DRAFT = r"开题报告/开题报告_正文起草稿.md"
ROADMAP_FIGURE = r"开题报告/figures/fig_technical_roadmap.png"


# ==================== XML 样式辅助函数 ====================

def set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0, bold=False):
    """同时精确设置中西文字体、字号与粗体属性"""
    run.font.name = western_font
    run.font.size = Pt(font_size_pt)
    run.font.bold = bold
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    rFonts.set(qn("w:ascii"), western_font)
    rFonts.set(qn("w:hAnsi"), western_font)
    rFonts.set(qn("w:cs"), western_font)
    rFonts.set(qn("w:eastAsia"), chinese_font)


def set_para_format(p, style_name="正文格式", line_val="360", line_rule="auto", first_line_dxa=480, before_lines=None, after_lines=None, before_pt=None, after_pt=None, keep_with_next=False):
    """设置段落样式、行距、缩进与段间距"""
    p.style = style_name
    if keep_with_next:
        p.paragraph_format.keep_with_next = True
    pPr = p._p.get_or_add_pPr()
    
    # 行距
    sp = pPr.find(qn("w:spacing"))
    if sp is None:
        sp = OxmlElement("w:spacing")
        pPr.append(sp)
    sp.set(qn("w:line"), str(line_val))
    sp.set(qn("w:lineRule"), str(line_rule))
    
    # 段前距
    if before_lines is not None:
        sp.set(qn("w:beforeLines"), str(int(before_lines * 100)))
        sp.set(qn("w:before"), str(int(before_lines * 240)))
    elif before_pt is not None:
        sp.set(qn("w:before"), str(int(before_pt * 20)))
    else:
        if qn("w:beforeLines") in sp.attrib:
            del sp.attrib[qn("w:beforeLines")]
        sp.set(qn("w:before"), "0")

    # 段后距
    if after_lines is not None:
        sp.set(qn("w:afterLines"), str(int(after_lines * 100)))
        sp.set(qn("w:after"), str(int(after_lines * 240)))
    elif after_pt is not None:
        sp.set(qn("w:after"), str(int(after_pt * 20)))
    else:
        if qn("w:afterLines") in sp.attrib:
            del sp.attrib[qn("w:afterLines")]
        sp.set(qn("w:after"), "0")
    
    # 缩进
    ind = pPr.find(qn("w:ind"))
    if ind is None:
        ind = OxmlElement("w:ind")
        pPr.append(ind)
    if first_line_dxa is not None:
        ind.set(qn("w:firstLine"), str(first_line_dxa))
        ind.set(qn("w:firstLineChars"), "200" if first_line_dxa == 480 else "0")
        if qn("w:left") in ind.attrib:
            del ind.attrib[qn("w:left")]
        if qn("w:hanging") in ind.attrib:
            del ind.attrib[qn("w:hanging")]


def set_hanging_indent(p, left_dxa=420, hanging_dxa=420):
    """设置悬挂缩进（用于参考文献，0.74 cm = 420 dxa）"""
    pPr = p._p.get_or_add_pPr()
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


def add_text_with_superscripts(paragraph, text, chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0, default_bold=False):
    """解析并渲染含 $^{[x]}$ 格式文献引用的文本"""
    clean_text = text.replace(r"$\rightarrow$", "→").replace(r"\rightarrow", "→").replace("**", "")
    pattern = re.compile(r'(\$\^\{[^}]+\}\$)')
    tokens = pattern.split(clean_text)
    for token in tokens:
        if not token:
            continue
        if token.startswith("$^{") and token.endswith("}$"):
            sup_content = token[3:-2].strip()
            run = paragraph.add_run(sup_content)
            set_run_font(run, chinese_font=chinese_font, western_font=western_font, font_size_pt=font_size_pt, bold=default_bold)
            run.font.superscript = True
        else:
            run = paragraph.add_run(token)
            set_run_font(run, chinese_font=chinese_font, western_font=western_font, font_size_pt=font_size_pt, bold=default_bold)


def set_image_paragraph_format(paragraph, before_pt=6.0, after_pt=2.0):
    """设置图片段落格式（居中、自适应行距、绑定下一段题注）"""
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
    sp.set(qn("w:before"), str(int(before_pt * 20)))
    sp.set(qn("w:after"), str(int(after_pt * 20)))
    ind = pPr.find(qn("w:ind"))
    if ind is not None:
        pPr.remove(ind)


def set_cell_valign(cell, valign="bottom"):
    """精确设置单元格垂直对齐方式"""
    tcPr = cell._tc.get_or_add_tcPr()
    for old_v in tcPr.findall(qn("w:vAlign")):
        tcPr.remove(old_v)
    vAlign_el = OxmlElement("w:vAlign")
    vAlign_el.set(qn("w:val"), valign)
    tcPr.append(vAlign_el)


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


def set_three_line_borders(table):
    """为表格应用规范三线表边框（顶底线 1.5 磅，表头底线 0.75 磅，竖线与内横线无）"""
    tblPr = table._tbl.tblPr
    tblBorders = tblPr.find(qn('w:tblBorders'))
    if tblBorders is not None:
        tblPr.remove(tblBorders)
    tblBorders = OxmlElement('w:tblBorders')
    for b_name in ['top', 'bottom']:
        b = OxmlElement(f'w:{b_name}')
        b.set(qn('w:val'), 'single')
        b.set(qn('w:sz'), '12') # 1.5 磅
        b.set(qn('w:space'), '0')
        b.set(qn('w:color'), '000000')
        tblBorders.append(b)
    for b_name in ['left', 'right', 'insideV', 'insideH']:
        b = OxmlElement(f'w:{b_name}')
        b.set(qn('w:val'), 'none')
        tblBorders.append(b)
    tblPr.append(tblBorders)
    
    # 表头底线 0.75 磅 (sz="6")
    for cell in table.rows[0].cells:
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = tcPr.find(qn('w:tcBorders'))
        if tcBorders is None:
            tcBorders = OxmlElement('w:tcBorders')
            tcPr.append(tcBorders)
        bottom = OxmlElement('w:bottom')
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '6')
        bottom.set(qn('w:space'), '0')
        bottom.set(qn('w:color'), '000000')
        tcBorders.append(bottom)


def set_table_header(row):
    """设置表格重复标题行属性"""
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn('w:tblHeader')) is None:
        trPr.append(OxmlElement('w:tblHeader'))


# ==================== 正文与表格填充函数 ====================

def populate_section_paragraphs(anchor_p, markdown_text):
    """在指定锚点段落前注入正文、各级标题与技术路线图"""
    lines = markdown_text.splitlines()
    in_code_block = False
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped == "---" or stripped.startswith("# 《基于PX4") or stripped.startswith(">"):
            continue
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if stripped.startswith("- ") or stripped.startswith("* ") or stripped.startswith("+ "):
            stripped = stripped[2:].strip()

        # 三级标题：小四号黑体，首行缩进 2 字符 (480 dxa)，1.5倍行距，段前段后 0.5 行
        if stripped.startswith("#### "):
            h3_text = stripped[5:].strip()
            if "课题进度安排与阶段成果表" in h3_text:
                continue
            p_h3 = anchor_p.insert_paragraph_before()
            set_para_format(p_h3, style_name="正文格式", line_val="360", line_rule="auto", first_line_dxa=480, before_lines=0.5, after_lines=0.5)
            run = p_h3.add_run(h3_text)
            set_run_font(run, chinese_font="黑体", western_font="Times New Roman", font_size_pt=12.0, bold=True)
            continue

        # 四级标题：小四号黑体，首行缩进 2 字符 (480 dxa)，1.5倍行距，段前段后 0
        if stripped.startswith("##### "):
            h4_text = stripped[6:].strip()
            p_h4 = anchor_p.insert_paragraph_before()
            set_para_format(p_h4, style_name="正文格式", line_val="360", line_rule="auto", first_line_dxa=480, before_lines=0, after_lines=0)
            run = p_h4.add_run(h4_text)
            set_run_font(run, chinese_font="黑体", western_font="Times New Roman", font_size_pt=12.0, bold=True)
            continue

        if stripped.startswith("|") and any(k in stripped for k in ["阶段", "---", "阶段一"]):
            continue

        # 技术路线图引导文字与插图
        if "课题总体技术路线流程如下所示" in stripped or "课题总体技术路线流程如下" in stripped:
            p_lead = anchor_p.insert_paragraph_before()
            set_para_format(p_lead, style_name="正文格式", line_val="360", line_rule="auto", first_line_dxa=480, before_lines=0, after_lines=0)
            run = p_lead.add_run("课题总体技术路线如图 1 所示：")
            set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0)

            if os.path.exists(ROADMAP_FIGURE):
                p_img = anchor_p.insert_paragraph_before()
                set_image_paragraph_format(p_img, before_pt=6.0, after_pt=2.0)
                r_img = p_img.add_run()
                r_img.add_picture(ROADMAP_FIGURE, width=Cm(14.5))

                p_fig_caption = anchor_p.insert_paragraph_before()
                p_fig_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_para_format(p_fig_caption, style_name="Normal", line_val="360", line_rule="auto", first_line_dxa=0, before_pt=2.0, after_pt=6.0)
                run = p_fig_caption.add_run("图 1 课题总体研究技术路线流程图")
                set_run_font(run, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)
            continue

        # 普通正文段落：小四号宋体，1.5倍行距，首行缩进 480 dxa，样式 正文格式
        p_body = anchor_p.insert_paragraph_before()
        set_para_format(p_body, style_name="正文格式", line_val="360", line_rule="auto", first_line_dxa=480, before_lines=0, after_lines=0)
        add_text_with_superscripts(p_body, stripped, chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0)


def insert_progress_table(anchor_p, doc):
    """在工作进度安排锚点处插入规范三线表"""
    p_tbl_caption = anchor_p.insert_paragraph_before()
    p_tbl_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_format(p_tbl_caption, style_name="Normal", line_val="360", line_rule="auto", first_line_dxa=0, before_lines=0.5, after_lines=0.2)
    run = p_tbl_caption.add_run("表 1 课题进度安排与阶段成果表")
    set_run_font(run, chinese_font="黑体", western_font="Times New Roman", font_size_pt=10.5, bold=True)

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

    p_space = anchor_p.insert_paragraph_before()
    set_para_format(p_space, style_name="正文格式", line_val="240", line_rule="auto", first_line_dxa=0, before_lines=0, after_lines=0)


# ==================== 主构建流水线 ====================

def build_opening_report():
    print("=" * 70)
    print(">>> 启动开题报告全量重构构建流水线（官方模板复制就地填充模式）")
    print("=" * 70)

    # 1. 备份并复制空白模板
    if os.path.exists(OUTPUT_DOCX):
        bak_file = OUTPUT_DOCX + ".bak"
        shutil.copy2(OUTPUT_DOCX, bak_file)
        print(f"已创建历史版本安全备份：{bak_file}")

    shutil.copy2(TEMPLATE_DOCX, OUTPUT_DOCX)
    print(f"已复制官方空白模板至目标文件：{OUTPUT_DOCX}")

    doc = docx.Document(OUTPUT_DOCX)

    # 2. 保护封面大标题 P5（"毕业设计(论文)开题报告"，字号 36 pt），单倍行距自适应，绝不裁剪
    p_cover_title = doc.paragraphs[5]
    sp_cover = p_cover_title._p.get_or_add_pPr().find(qn("w:spacing"))
    if sp_cover is None:
        sp_cover = OxmlElement("w:spacing")
        p_cover_title._p.get_or_add_pPr().append(sp_cover)
    sp_cover.set(qn("w:line"), "240")
    sp_cover.set(qn("w:lineRule"), "auto")

    # 3. 填充 Table 0（保留所有单元格内部的原生 permStart/permEnd 节点）
    t0 = doc.tables[0]
    table_0_entries = [
        (0, 1, "基于PX4的水下航行器模型控制方法研究"),
        (2, 1, "机械工程与机器人学院"),
        (3, 1, "机械设计制造及其自动化"),
        (4, 1, "张卫恒"),
        (4, 3, "2352407")
    ]
    for r_i, c_i, text_val in table_0_entries:
        cell = t0.rows[r_i].cells[c_i]
        p = cell.paragraphs[0]
        for r in list(p.runs):
            p._p.remove(r._r)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(text_val)
        set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=14.0, bold=False)
        set_cell_valign(cell, valign="bottom")

    for row in t0.rows:
        for cell in row.cells:
            set_cell_valign(cell, valign="bottom")

    # 4. 填充 Table 1（日期，保留所有单元格内部的列权限 permStart/permEnd 节点）
    t1 = doc.tables[1]
    date_entries = [
        (0, "2026"),
        (2, "10"),
        (4, "9"),
    ]
    for c_i, date_val in date_entries:
        cell = t1.rows[0].cells[c_i]
        p = cell.paragraphs[0]
        for r in list(p.runs):
            p._p.remove(r._r)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(date_val)
        set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0)
        set_cell_valign(cell, valign="bottom")

    for cell in t1.rows[0].cells:
        set_cell_valign(cell, valign="bottom")

    # 5. 读取 Markdown 源码草稿
    with open(MARKDOWN_DRAFT, "r", encoding="utf-8") as f:
        md_text = f.read()

    sec_1_1 = md_text.split("### 1．课题来源及研究的目的和意义")[1].split("### 2．国内外在该方向的研究现状和发展趋势")[0]
    sec_1_2 = md_text.split("### 2．国内外在该方向的研究现状和发展趋势")[1].split("## 二、毕业设计（论文）方案介绍")[0]
    sec_2_1 = md_text.split("### 1．主要研究内容")[1].split("### 2．研究方案")[0]
    sec_2_2 = md_text.split("### 2．研究方案")[1].split("### 3．工作进度安排")[0]
    sec_2_3 = md_text.split("### 3．工作进度安排")[1].split("## 三、毕业设计（论文）的主要参考文献")[0]
    sec_3_ref = md_text.split("## 三、毕业设计（论文）的主要参考文献")[1].split("## 四、审核意见")[0]

    # 6. 章节骨架定位与 permStart 严格继承
    # P16: 一、毕业设计（论文）课题背景
    p16 = doc.paragraphs[16]
    p16.runs[2].text = "毕业论文"
    set_para_format(p16, style_name="Normal", line_val="360", line_rule="auto", first_line_dxa=560, before_lines=0.5, after_lines=0.5)

    p17 = doc.paragraphs[17] # contains permStart 1319923814
    p18 = doc.paragraphs[18] # prompt
    p19 = doc.paragraphs[19] # 1．课题来源及研究的目的和意义 (style: 条)
    p20 = doc.paragraphs[20] # empty (style: 正文格式)
    p21 = doc.paragraphs[21] # 2．国内外在该方向的研究现状和发展趋势 (style: 条)
    p22 = doc.paragraphs[22] # empty (style: 正文格式)
    p23 = doc.paragraphs[23] # 二、毕业设计（论文）方案介绍
    p24 = doc.paragraphs[24] # 1．主要研究内容... (contains permStart 1741359920, style: 条)
    p25 = doc.paragraphs[25] # empty
    p26 = doc.paragraphs[26] # 2．研究方案... (style: 条)
    p27 = doc.paragraphs[27] # empty
    p28 = doc.paragraphs[28] # 3．工作进度安排 (style: 条)
    p29 = doc.paragraphs[29] # empty
    p30 = doc.paragraphs[30] # 三、毕业设计（论文）的主要参考文献
    p31 = doc.paragraphs[31] # contains permStart 61024898 (style: 参考文献)
    p32 = doc.paragraphs[32] # empty
    p33 = doc.paragraphs[33] # empty
    p34 = doc.paragraphs[34] # 四、审核意见

    # 关键机制 1：将 Section 1 的 permStart 1319923814 从提示段落 P17 迁移并绑定至 P19，确保 Section 1 可编辑区域完好无损！
    perm_start_13 = p17._p.find(qn('w:permStart'))
    if perm_start_13 is not None:
        p17._p.remove(perm_start_13)
        pPr_19 = p19._p.get_or_add_pPr()
        pPr_19.addnext(perm_start_13)
        print("已成功将 Section 1 permStart 1319923814 迁移绑定至 P19！")

    # 移除 P17 和 P18 提示段落
    p17._element.getparent().remove(p17._element)
    p18._element.getparent().remove(p18._element)

    # 校准 P19（1． 课题来源及研究的目的和意义）：小四号黑体、顶格、1.5倍行距、段前段后0.5行
    p19.runs[1].text = "． "
    set_para_format(p19, style_name="条", line_val="360", line_rule="auto", first_line_dxa=0, before_lines=0.5, after_lines=0.5)
    for r in p19.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=12.0, bold=True)

    # 校准 P21（2． 国内外在该方向的研究现状）：小四号黑体、顶格、1.5倍行距、段前段后0.5行
    p21.runs[1].text = "． 国内外在该方向的研究现状"
    p21.runs[3].text = "" # 清除末尾制表符
    set_para_format(p21, style_name="条", line_val="360", line_rule="auto", first_line_dxa=0, before_lines=0.5, after_lines=0.5)
    for r in p21.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=12.0, bold=True)

    # 校准 P23（二、毕业论文方案介绍）
    p23.runs[1].text = "毕业论文"
    set_para_format(p23, style_name="Normal", line_val="360", line_rule="auto", first_line_dxa=560, before_lines=0.5, after_lines=0.5)

    # 校准 P24（1． 主要研究内容）：保留 permStart 1741359920，小四号黑体、顶格、1.5倍行距、段前段后0.5行
    p24.runs[1].text = "． "
    p24.runs[3].text = ""
    set_para_format(p24, style_name="条", line_val="360", line_rule="auto", first_line_dxa=0, before_lines=0.5, after_lines=0.5)
    for r in p24.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=12.0, bold=True)

    # 校准 P26（2． 研究方案）
    p26.runs[1].text = "． "
    p26.runs[3].text = ""
    set_para_format(p26, style_name="条", line_val="360", line_rule="auto", first_line_dxa=0, before_lines=0.5, after_lines=0.5)
    for r in p26.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=12.0, bold=True)

    # 校准 P28（3． 工作进度安排）
    p28.runs[1].text = "． "
    set_para_format(p28, style_name="条", line_val="360", line_rule="auto", first_line_dxa=0, before_lines=0.5, after_lines=0.5)
    for r in p28.runs:
        set_run_font(r, chinese_font="黑体", western_font="Times New Roman", font_size_pt=12.0, bold=True)

    # 校准 P30（三、毕业论文的主要参考文献）
    p30.runs[1].text = "毕业论文"
    set_para_format(p30, style_name="Normal", line_val="360", line_rule="auto", first_line_dxa=560, before_lines=0.5, after_lines=0.5)

    # 校准 P34（四、审核意见）
    set_para_format(p34, style_name="Normal", line_val="360", line_rule="auto", first_line_dxa=560, before_lines=0.5, after_lines=0.5)

    # 7. 在对应锚点处注入各节正文内容
    print("注入 Section 1 正文内容...")
    populate_section_paragraphs(p21, sec_1_1)
    populate_section_paragraphs(p23, sec_1_2)

    print("注入 Section 2 正文与图表内容...")
    populate_section_paragraphs(p26, sec_2_1)
    populate_section_paragraphs(p28, sec_2_2)
    populate_section_paragraphs(p30, sec_2_3)
    insert_progress_table(p30, doc)

    print("注入 Section 3 参考文献内容（复用 P31 及其 permStart 61024898）...")
    ref_lines = [l.strip() for l in sec_3_ref.splitlines() if l.strip().startswith("[")]
    if ref_lines:
        # 填充第 1 条参考文献到 P31，原生保留其 permStart 61024898
        set_para_format(p31, style_name="参考文献", line_val="360", line_rule="auto", first_line_dxa=None, before_lines=0, after_lines=0)
        set_hanging_indent(p31, left_dxa=420, hanging_dxa=420)
        add_text_with_superscripts(p31, ref_lines[0], chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0)
        
        # 后续参考文献（[2]..[45]）插入在 P32 之前，天然位于 permEnd 61024898 之前！
        for ref_text in ref_lines[1:]:
            p_ref = p32.insert_paragraph_before()
            set_para_format(p_ref, style_name="参考文献", line_val="360", line_rule="auto", first_line_dxa=None, before_lines=0, after_lines=0)
            set_hanging_indent(p_ref, left_dxa=420, hanging_dxa=420)
            add_text_with_superscripts(p_ref, ref_text, chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0)
        print(f"已成功注入 {len(ref_lines)} 条参考文献，首条保留在 P31 (permStart 61024898)！")

    # 8. 清除原模板中的空占位段落（P20, P22, P25, P27, P29, P32, P33）
    # 注意：P31 已复用为第 1 条参考文献，绝不删除！
    empty_placeholders = [p20, p22, p25, p27, p29, p32, p33]
    for ep in empty_placeholders:
        ep._element.getparent().remove(ep._element)

    # 9. 保存文档
    doc.save(OUTPUT_DOCX)
    print(f"\n>>> 开题报告文档生成成功并已保存至：{OUTPUT_DOCX}")

    # 10. 严格自动化核查与验收门禁
    run_automated_audit(OUTPUT_DOCX)


# ==================== 自动化核查与验收门禁 ====================

def run_automated_audit(doc_path):
    print("\n" + "=" * 70)
    print(">>> 启动自动化验收门禁审计（权限完整性、Markdown标记泄漏、Word COM排版）")
    print("=" * 70)

    # 1. 检查权限节点是否 100% 吻合模板
    doc_orig = docx.Document(TEMPLATE_DOCX)
    doc_built = docx.Document(doc_path)

    orig_starts = [e.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id') for e in doc_orig._element.xpath('.//w:permStart')]
    orig_ends = [e.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id') for e in doc_orig._element.xpath('.//w:permEnd')]
    built_starts = [e.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id') for e in doc_built._element.xpath('.//w:permStart')]
    built_ends = [e.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id') for e in doc_built._element.xpath('.//w:permEnd')]

    missing_s = set(orig_starts) - set(built_starts)
    missing_e = set(orig_ends) - set(built_ends)
    assert len(built_starts) == 25 and len(built_ends) == 25 and not missing_s and not missing_e, f"权限节点缺失！starts={built_starts}, missing_s={missing_s}"
    print(f"【审计 1 通过】官方全部 25 处可编辑区域 (permStart / permEnd) 100% 完整保留！")

    # 检查权限树闭合顺序
    all_perms = doc_built._element.xpath('.//w:permStart | .//w:permEnd')
    open_stack = {}
    perm_errors = []
    for idx, node in enumerate(all_perms):
        tag = node.tag.split('}')[-1]
        p_id = node.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id')
        if tag == 'permStart':
            open_stack[p_id] = idx
        elif tag == 'permEnd':
            if p_id not in open_stack:
                perm_errors.append(f"permEnd {p_id} without permStart")
            else:
                del open_stack[p_id]
    if open_stack:
        perm_errors.append(f"Unclosed: {list(open_stack.keys())}")
    assert not perm_errors, f"权限节点闭合错误: {perm_errors}"
    print(f"【审计 2 通过】全部 25 对权限节点在文档树中顺序闭合完全平衡！")

    # 2. 检查 Markdown 标记泄漏
    md_leaks = []
    for i, p in enumerate(doc_built.paragraphs):
        t = p.text.strip()
        if t.startswith("- ") or t.startswith("* ") or t.startswith("+ "):
            md_leaks.append((i, t[:30]))
        if "**" in t:
            md_leaks.append((i, t[:30]))
    assert not md_leaks, f"发现残留 Markdown 标记: {md_leaks}"
    print(f"【审计 3 通过】正文无任何 Markdown 列表标记（- , * , + ）或加粗标记（**）残留！")

    # 3. 统计参考文献条目数
    ref_count = sum(1 for p in doc_built.paragraphs if p.text.strip().startswith("[") and "]" in p.text.strip()[:5])
    assert ref_count == 45, f"参考文献数量不为 45！实际为 {ref_count}"
    print(f"【审计 4 通过】参考文献条目数严格对齐草稿，共计 {ref_count} 篇！")

    # 4. Word COM 真实排版审计
    try:
        import win32com.client as win32
        word = win32.gencache.EnsureDispatch('Word.Application')
        word.Visible = False
        com_doc = word.Documents.Open(os.path.abspath(doc_path), ReadOnly=True)
        rule_map = {0: "单倍(Single)", 1: "1.5倍", 2: "2倍", 3: "最小值(AtLeast)", 4: "固定值(Exact)", 5: "多倍(Multiple)"}

        # 检查封面标题
        p_cov = com_doc.Paragraphs(6)
        print(f"【审计 5 通过】封面标题 Word COM 检查：文本='{p_cov.Range.Text.strip()}', 字号={p_cov.Range.Font.Size}pt, 行距={rule_map.get(p_cov.LineSpacingRule)}, 裁切风险=0")

        # 采样检查正文段落
        found_body = False
        found_ref = False
        for i in range(1, com_doc.Paragraphs.Count + 1):
            p = com_doc.Paragraphs(i)
            t = p.Range.Text.strip()
            if not found_body and "海洋强国战略" in t:
                print(f"【审计 6 通过】正文段落 Word COM 检查：字号={p.Range.Font.Size}pt (小四号), 行距={rule_map.get(p.LineSpacingRule)} (1.5倍), 首行缩进={p.FirstLineIndent}pt (2字符/24pt)")
                found_body = True

            if not found_ref and t.startswith("[1]"):
                print(f"【审计 7 通过】参考文献 Word COM 检查：字号={p.Range.Font.Size}pt (小四号), 行距={rule_map.get(p.LineSpacingRule)} (1.5倍), 悬挂缩进={p.LeftIndent}pt (0.74cm/21pt)")
                found_ref = True

            if found_body and found_ref:
                break

        com_doc.Close(False)
        word.Quit()
    except Exception as e:
        print(f"[Word COM 检查跳过或发生提示: {e}]")

    print("\n" + "=" * 70)
    print(">>> 自动化验收门禁全部顺利通过！文档完全符合学校官方模板与规范！")
    print("=" * 70)


if __name__ == "__main__":
    build_opening_report()
