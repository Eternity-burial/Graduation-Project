# -*- coding: utf-8 -*-
"""
生成《基于PX4的水下航行器模型控制方法研究》开题报告出版级高清学术配图 (300 DPI PNG + 可编辑 .drawio)
彻底贯彻国际顶刊（IEEE/IFAC/Elsevier 及 Fossen 经典教材）学术制图规范：
- 纯黑白 / 极浅灰阶（Grayscale Line Art）工程制图风格，坚决剔除任何花哨 AI 配色
- 严格遵循 Fossen 6-DOF 海洋航行器符号规范与标准右手坐标系
- 原生富文本数学排版（上下标、粗斜体、顶标点号/帽号，零乱码方框，零标注重叠）

包含全套 4 幅学术配图：
1. fig1_lit_control_architecture.png (.drawio): 图 1  典型水下航行器六自由度模型控制与推力分配通用闭环结构框图
2. fig0_rov_coord_thrusters.png      (.drawio): 图 2  八推进器水下航行器坐标系定义与推力矢量空间布置示意图
3. fig1_technical_roadmap.png        (.drawio): 图 3  课题总体研究技术路线图
4. fig2_px4_rov_architecture.png     (.drawio): 图 4  基于PX4/SITL的水下航行器闭环仿真系统结构框图
"""

import os
import re
import sys
import math
from xml.sax.saxutils import escape as xml_escape
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT_DIR, exist_ok=True)


def get_font(size, bold=False):
    size = max(10, int(round(size)))
    font_candidates = (
        ["C:/Windows/Fonts/msyhbd.ttc", "C:/Windows/Fonts/simhei.ttf", "C:/Windows/Fonts/msyh.ttc"]
        if bold else
        ["C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simsun.ttc", "C:/Windows/Fonts/simhei.ttf"]
    )
    for fp in font_candidates:
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()


TOKEN_RE = re.compile(r"(\{(?:sub|sup|hat|dot):[^{}]+\})")


def parse_rich_line(line):
    parts = TOKEN_RE.split(line)
    tokens = []
    for p in parts:
        if not p:
            continue
        if p.startswith("{sub:") and p.endswith("}"):
            tokens.append(("sub", p[5:-1]))
        elif p.startswith("{sup:") and p.endswith("}"):
            tokens.append(("sup", p[5:-1]))
        elif p.startswith("{hat:") and p.endswith("}"):
            tokens.append(("hat", p[5:-1]))
        elif p.startswith("{dot:") and p.endswith("}"):
            tokens.append(("dot", p[5:-1]))
        else:
            tokens.append(("norm", p))
    return tokens


def measure_rich_line(draw, tokens, font_size, bold=False):
    f_main = get_font(font_size, bold=bold)
    f_script = get_font(font_size * 0.72, bold=bold)
    total_w = 0
    for kind, txt in tokens:
        f = f_script if kind in ("sub", "sup") else f_main
        bb = draw.textbbox((0, 0), txt, font=f)
        w = bb[2] - bb[0]
        total_w += w + (1 if kind in ("sub", "sup") else 0)
    return total_w, int(font_size * 1.32)


def draw_rich_line(draw, x, y, tokens, font_size, fill="#000000", bold=False):
    f_main = get_font(font_size, bold=bold)
    f_script = get_font(font_size * 0.72, bold=bold)
    cur_x = x
    for kind, txt in tokens:
        if kind == "norm":
            bb = draw.textbbox((0, 0), txt, font=f_main)
            draw.text((cur_x, y), txt, font=f_main, fill=fill)
            cur_x += (bb[2] - bb[0])
        elif kind == "sub":
            bb = draw.textbbox((0, 0), txt, font=f_script)
            draw.text((cur_x + 1, y + int(font_size * 0.34)), txt, font=f_script, fill=fill)
            cur_x += (bb[2] - bb[0]) + 1
        elif kind == "sup":
            bb = draw.textbbox((0, 0), txt, font=f_script)
            draw.text((cur_x + 1, y - int(font_size * 0.14)), txt, font=f_script, fill=fill)
            cur_x += (bb[2] - bb[0]) + 1
        elif kind == "hat":
            bb = draw.textbbox((0, 0), txt, font=f_main)
            w = bb[2] - bb[0]
            draw.text((cur_x, y), txt, font=f_main, fill=fill)
            cx = cur_x + w / 2
            hy = y + bb[1] - 7
            hw = max(5, int(font_size * 0.22))
            hh = max(4, int(font_size * 0.18))
            draw.line([(cx - hw, hy + hh), (cx, hy), (cx + hw, hy + hh)], fill=fill, width=2)
            cur_x += w
        elif kind == "dot":
            bb = draw.textbbox((0, 0), txt, font=f_main)
            w = bb[2] - bb[0]
            draw.text((cur_x, y), txt, font=f_main, fill=fill)
            cx = cur_x + w / 2
            dy = y + bb[1] - 5
            r = max(2, int(font_size * 0.08))
            draw.ellipse([cx - r, dy - r, cx + r, dy + r], fill=fill)
            cur_x += w
    return cur_x


def draw_rich_text(draw, box, text, font_size, fill="#000000", bold=False, align="center"):
    bx, by, bw, bh = box
    lines = text.split("\n")
    parsed_lines = [parse_rich_line(ln) for ln in lines]
    line_metrics = [measure_rich_line(draw, toks, font_size, bold=bold) for toks in parsed_lines]
    line_h = max(m[1] for m in line_metrics) if line_metrics else int(font_size * 1.32)
    total_h = len(parsed_lines) * line_h
    start_y = by + (bh - total_h) / 2
    for idx, tokens in enumerate(parsed_lines):
        lw, _ = line_metrics[idx]
        if align == "center":
            lx = bx + (bw - lw) / 2
        elif align == "right":
            lx = bx + bw - lw - 10
        else:
            lx = bx + 12
        ly = start_y + idx * line_h
        draw_rich_line(draw, lx, ly, tokens, font_size, fill=fill, bold=bold)


def draw_arrow(draw, p1, p2, fill="#000000", width=2, arrow_len=11, arrow_w=6):
    draw.line([p1, p2], fill=fill, width=width)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    length = math.hypot(dx, dy)
    if length < 1e-4:
        return
    ux = dx / length
    uy = dy / length
    perp_x = -uy
    perp_y = ux
    bx = p2[0] - arrow_len * ux
    by = p2[1] - arrow_len * uy
    p_left = (bx + arrow_w * perp_x, by + arrow_w * perp_y)
    p_right = (bx - arrow_w * perp_x, by - arrow_w * perp_y)
    draw.polygon([p2, p_left, p_right], fill=fill)


def draw_academic_box(draw, box, text, font_size=20, fill="#FFFFFF", border="#000000",
                      text_fill="#000000", bold=False, width=2, radius=4, align="center"):
    bx, by, bw, bh = box
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=radius, fill=fill, outline=border, width=width)
    draw_rich_text(draw, box, text, font_size=font_size, fill=text_fill, bold=bold, align=align)


def export_drawio_xml(filename, cells_xml, width=1800, height=1000):
    xml = f"""<mxfile host="Electron" modified="2026-09-28T00:00:00.000Z" agent="Antigravity Academic" version="21.0.0" type="device">
  <diagram id="diagram_1" name="Page-1">
    <mxGraphModel dx="{width}" dy="{height}" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{width}" pageHeight="{height}" math="1" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
{cells_xml}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    fp = os.path.join(OUT_DIR, filename)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"[OK] 已导出可编辑矢量图: {fp}")


# ==============================================================================
# 1. 图 1：典型水下航行器六自由度模型控制与推力分配通用闭环结构框图
# ==============================================================================

def generate_fig1_lit_control_architecture():
    w, h = 2400, 1100
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw_rich_line(draw, 50, 40, parse_rich_line("图 1  典型水下航行器六自由度模型控制与推力分配通用闭环结构框图"),
                   30, fill="#000000", bold=True)
    draw_rich_line(draw, 50, 85, parse_rich_line("基于海洋航行器经典控制理论架构（Fossen Handbook [1] & Johansen & Fossen [14]）"),
                   20, fill="#444444", bold=False)

    # 1. 参考指令生成
    draw.rounded_rectangle([60, 150, 360, 490], radius=6, fill="#FAFAFA", outline="#000000", width=2)
    draw_rich_line(draw, 80, 170, parse_rich_line("参考运动规划与指令"), 22, fill="#000000", bold=True)
    draw_academic_box(draw, (90, 230, 240, 90), "参考位姿轨迹\n{dot:η}{sub:r}(t), η{sub:r}(t)", font_size=21, fill="#FFFFFF", border="#000000", bold=True)
    draw_academic_box(draw, (90, 360, 240, 90), "参考速度与加速度\n{dot:ν}{sub:r}(t), ν{sub:r}(t)", font_size=21, fill="#FFFFFF", border="#000000", bold=True)

    # 误差比较点 (Summing junction 1)
    cx1, cy1 = 440, 375
    draw.ellipse([cx1 - 20, cy1 - 20, cx1 + 20, cy1 + 20], fill="#FFFFFF", outline="#000000", width=2)
    draw.line([cx1 - 13, cy1, cx1 + 13, cy1], fill="#000000", width=2)
    draw.line([cx1, cy1 - 13, cx1, cy1 + 13], fill="#000000", width=2)
    draw.text((cx1 - 28, cy1 - 32), "+", font=get_font(20, bold=True), fill="#000000")
    draw.text((cx1 - 8, cy1 + 20), "−", font=get_font(22, bold=True), fill="#000000")

    # 2. 运动控制模块
    draw.rounded_rectangle([520, 150, 1020, 600], radius=8, fill="#F9F9F9", outline="#000000", width=2)
    draw_rich_line(draw, 545, 170, parse_rich_line("运动控制器 (Motion Controller)"), 24, fill="#000000", bold=True)

    draw_academic_box(draw, (550, 220, 440, 140),
                      "基于标称模型的动力学前馈补偿项\nF{sub:model}(·) = {hat:M}{dot:ν}{sub:r} + {hat:C}(ν)ν + {hat:D}(ν)ν + {hat:g}(η)\n(包含刚体/附加质量惯性耦合、水动力阻尼与静水力恢复)",
                      font_size=18, fill="#FFFFFF", border="#000000", bold=False)

    draw_academic_box(draw, (550, 390, 440, 120),
                      "闭环状态误差反馈调节项\nF{sub:fb}(·) = K{sub:p} e{sub:η} + K{sub:d} e{sub:ν} + K{sub:i} ∫ e{sub:η} dt\n(误差跟踪收敛与抗未知低频外扰)",
                      font_size=19, fill="#FFFFFF", border="#000000", bold=False)

    # 控制器内部求和点 (放置在两项右侧中心，信号直接向右输出)
    cx_ctrl, cy_ctrl = 1045, 370
    draw.ellipse([cx_ctrl - 16, cy_ctrl - 16, cx_ctrl + 16, cy_ctrl + 16], fill="#FFFFFF", outline="#000000", width=2)
    draw.line([cx_ctrl - 11, cy_ctrl, cx_ctrl + 11, cy_ctrl], fill="#000000", width=2)
    draw.line([cx_ctrl, cy_ctrl - 11, cx_ctrl, cy_ctrl + 11], fill="#000000", width=2)
    draw.text((cx_ctrl + 6, cy_ctrl - 34), "+", font=get_font(18, bold=True), fill="#000000")
    draw.text((cx_ctrl + 6, cy_ctrl + 16), "+", font=get_font(18, bold=True), fill="#000000")

    # 3. 控制分配模块
    draw.rounded_rectangle([1120, 150, 1500, 600], radius=8, fill="#F9F9F9", outline="#000000", width=2)
    draw_rich_line(draw, 1145, 170, parse_rich_line("八推进器控制分配 (Control Allocation)"), 23, fill="#000000", bold=True)
    draw_academic_box(draw, (1140, 220, 340, 130),
                      "6×8 推力几何配置矩阵\nB = [b{sub:1}, b{sub:2}, …, b{sub:8}] ∈ R{sup:6×8}\nb{sub:i} = [d{sub:i}{sup:T}, (r{sub:i} × d{sub:i}){sup:T}]{sup:T}\n(水平4矢量 + 垂直4对称布局)",
                      font_size=18, fill="#FFFFFF", border="#000000")
    draw_academic_box(draw, (1140, 380, 340, 130),
                      "推力幅值物理边界约束求解\nT{sub:min} ≤ T ≤ T{sub:max}\n加权伪逆 / 有界优化分配\ne{sub:τ} = τ{sub:c} − BT",
                      font_size=18, fill="#FFFFFF", border="#000000")

    # 4. 推进器执行机构
    draw.rounded_rectangle([1550, 220, 1840, 520], radius=8, fill="#F9F9F9", outline="#000000", width=2)
    draw_rich_line(draw, 1575, 240, parse_rich_line("推进器执行机构"), 23, fill="#000000", bold=True)
    draw_academic_box(draw, (1570, 290, 250, 90), "电机电调与螺旋桨动态\nT{sub:i}(s) = 1/(1 + τ{sub:m}s) T{sub:c,i}\n推力正反转非对称", font_size=18, fill="#FFFFFF", border="#000000")
    draw_academic_box(draw, (1570, 400, 250, 90), "实际推力输出矢量\nT = [T{sub:1}, …, T{sub:8}]{sup:T} ∈ R{sup:8}", font_size=19, fill="#FFFFFF", border="#000000", bold=True)

    # 5. 水下航行器六自由度被控对象 (ROV Plant)
    draw.rounded_rectangle([1900, 150, 2340, 600], radius=8, fill="#F5F5F5", outline="#000000", width=3)
    draw_rich_line(draw, 1925, 175, parse_rich_line("水下航行器动力学与运动学模型"), 23, fill="#000000", bold=True)
    draw_academic_box(draw, (1920, 220, 400, 170),
                      "六自由度非线性动力学方程\nM{dot:ν} + C(ν)ν + D(ν)ν + g(η) = τ + τ{sub:d}\nM = M{sub:RB} + M{sub:A}\nC(ν) = C{sub:RB}(ν) + C{sub:A}(ν)\nD(ν) = D{sub:lin} + D{sub:quad}(ν)",
                      font_size=18, fill="#FFFFFF", border="#000000")
    draw_academic_box(draw, (1920, 410, 400, 100),
                      "六自由度运动学坐标变换方程\n{dot:η} = J(η)ν\nη = [x, y, z, ϕ, θ, ψ]{sup:T}",
                      font_size=18, fill="#FFFFFF", border="#000000")
    draw_academic_box(draw, (1920, 525, 400, 55),
                      "合力与力矩产生: τ = B T", font_size=19, fill="#FFFFFF", border="#000000", bold=True)

    # 外部流扰输入 (修正坐标: box width 300, height 70)
    draw.rounded_rectangle([1980, 40, 2260, 110], radius=4, fill="#FFFFFF", outline="#000000", width=2)
    draw_rich_text(draw, (1980, 40, 280, 70), "环境扰动力与力矩\nτ{sub:d} (复杂水流、波浪扰动)", font_size=18, fill="#000000", bold=True)
    draw_arrow(draw, (2120, 110), (2120, 150), fill="#000000", width=2)

    # 6. 反馈测量与状态估计
    draw.rounded_rectangle([700, 750, 1700, 980], radius=8, fill="#F9F9F9", outline="#000000", width=2)
    draw_rich_line(draw, 730, 770, parse_rich_line("导航传感与全状态估计模块 (Navigation & State Estimation / EKF)"), 23, fill="#000000", bold=True)
    draw_academic_box(draw, (730, 820, 430, 130), "机载传感单元采集\nIMU (加速度计、角速度陀螺仪)\n电子罗盘 (偏航航向角)、深度计 (水压)\nDVL / 声学定位 (流速与相对底速)", font_size=18, fill="#FFFFFF", border="#000000")
    draw_academic_box(draw, (1200, 820, 460, 130), "扩展卡尔曼滤波与状态重构 (EKF2)\n位姿估计: {hat:η} = [{hat:x}, {hat:y}, {hat:z}, {hat:ϕ}, {hat:θ}, {hat:ψ}]{sup:T}\n速度估计: {hat:ν} = [{hat:u}, {hat:v}, {hat:w}, {hat:p}, {hat:q}, {hat:r}]{sup:T}", font_size=18, fill="#FFFFFF", border="#000000", bold=True)

    # 信号连接线
    draw_arrow(draw, (330, 275), (440, 275), fill="#000000", width=2)
    draw_arrow(draw, (440, 275), (440, 355), fill="#000000", width=2)
    draw_rich_text(draw, (350, 240, 80, 30), "η{sub:r}", font_size=20, fill="#000000", bold=True)

    draw_arrow(draw, (460, 375), (550, 440), fill="#000000", width=2)
    draw_rich_text(draw, (460, 335, 90, 30), "e{sub:η}, e{sub:ν}", font_size=19, fill="#000000", bold=True)

    draw.line([(330, 405), (490, 405)], fill="#000000", width=2)
    draw.line([(490, 405), (490, 270)], fill="#000000", width=2)
    draw_arrow(draw, (490, 270), (550, 270), fill="#000000", width=2)
    draw_rich_text(draw, (485, 235, 100, 30), "{dot:ν}{sub:r}, ν{sub:r}", font_size=19, fill="#000000", bold=True)

    # 模型补偿项与反馈项汇聚到求和点
    draw.line([(990, 290), (cx_ctrl, 290)], fill="#000000", width=2)
    draw_arrow(draw, (cx_ctrl, 290), (cx_ctrl, cy_ctrl - 16), fill="#000000", width=2)

    draw.line([(990, 450), (cx_ctrl, 450)], fill="#000000", width=2)
    draw_arrow(draw, (cx_ctrl, 450), (cx_ctrl, cy_ctrl + 16), fill="#000000", width=2)

    # 期望力矩直接平直输出到控制分配模块
    draw_arrow(draw, (cx_ctrl + 16, cy_ctrl), (1120, cy_ctrl), fill="#000000", width=3)
    draw_rich_text(draw, (cx_ctrl + 20, cy_ctrl - 36, 120, 32), "τ{sub:c} ∈ R{sup:6}", font_size=20, fill="#000000", bold=True)

    draw_arrow(draw, (1500, 370), (1550, 370), fill="#000000", width=2)
    draw_rich_text(draw, (1485, 335, 80, 32), "T{sub:cmd}", font_size=20, fill="#000000", bold=True)

    draw_arrow(draw, (1840, 370), (1900, 370), fill="#000000", width=2)
    draw_rich_text(draw, (1835, 335, 75, 32), "T ∈ R{sup:8}", font_size=20, fill="#000000", bold=True)

    draw.line([(2120, 600), (2120, 890)], fill="#000000", width=2)
    draw_arrow(draw, (2120, 890), (1700, 890), fill="#000000", width=2)
    draw_rich_text(draw, (2130, 720, 160, 40), "真实运动状态\nη(t), ν(t)", font_size=20, fill="#000000", bold=True)

    draw.line([(700, 890), (440, 890)], fill="#000000", width=2)
    draw_arrow(draw, (440, 890), (440, 395), fill="#000000", width=2)
    draw_rich_text(draw, (350, 650, 120, 50), "状态反馈\n{hat:η}, {hat:ν}", font_size=20, fill="#000000", bold=True)

    draw.line([(510, 890), (510, 320)], fill="#000000", width=2)
    draw_arrow(draw, (510, 320), (550, 320), fill="#000000", width=2)

    fp_png = os.path.join(OUT_DIR, "fig1_lit_control_architecture.png")
    img.save(fp_png, dpi=(300, 300))
    print(f"[OK] 已生成文献控制框架黑白图 (300 DPI): {fp_png}")


# ==============================================================================
# 2. 图 2：八推进器水下航行器坐标系定义与推力矢量空间布置示意图
# ==============================================================================

def generate_fig0_rov_coord_thrusters():
    w, h = 2400, 1150
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw_rich_line(draw, 50, 35, parse_rich_line("图 2  八推进器水下航行器坐标系定义与推力矢量空间布置示意图"),
                   30, fill="#000000", bold=True)

    # (a) 左图
    ox_a, oy_a = 50, 95
    w_a, h_a = 1120, 1010
    draw.rectangle([ox_a, oy_a, ox_a + w_a, oy_a + h_a], fill="#FFFFFF", outline="#000000", width=2)
    draw_rich_line(draw, ox_a + 25, oy_a + 25, parse_rich_line("(a) 北东地惯性系 {n} 与附体系 {b} 及六自由度定义"),
                   24, fill="#000000", bold=True)

    # 惯性系 {n}
    on_x, on_y = ox_a + 130, oy_a + 130
    draw.ellipse([on_x - 5, on_y - 5, on_x + 5, on_y + 5], fill="#000000")
    draw_rich_text(draw, (on_x - 110, on_y - 35, 100, 30), "{n}: O{sub:n}", font_size=22, fill="#000000", bold=True)
    draw_arrow(draw, (on_x, on_y), (on_x + 130, on_y - 40), fill="#000000", width=2)
    draw_rich_text(draw, (on_x + 135, on_y - 65, 140, 30), "x{sub:n} (北 North)", font_size=19, fill="#000000", bold=True)
    draw_arrow(draw, (on_x, on_y), (on_x + 130, on_y + 40), fill="#000000", width=2)
    draw_rich_text(draw, (on_x + 135, on_y + 35, 140, 30), "y{sub:n} (东 East)", font_size=19, fill="#000000", bold=True)
    draw_arrow(draw, (on_x, on_y), (on_x, on_y + 130), fill="#000000", width=2)
    draw_rich_text(draw, (on_x - 30, on_y + 135, 140, 30), "z{sub:n} (地 Down)", font_size=19, fill="#000000", bold=True)

    # 附体系与机身 (略微上移至 cy_b = oy_a + 360，避免碰撞下表)
    cx_b, cy_b = ox_a + 570, oy_a + 360
    L, W, H = 210, 150, 100

    p_fff = (cx_b + L, cy_b - 25)
    p_frf = (cx_b + 45, cy_b + W)
    p_flf = (cx_b - 45, cy_b - W)
    p_bbf = (cx_b - L, cy_b + 25)

    p_fft = (p_fff[0], p_fff[1] - H)
    p_frt = (p_frf[0], p_frf[1] - H)
    p_flt = (p_flf[0], p_flf[1] - H)
    p_bbt = (p_bbf[0], p_bbf[1] - H)

    draw.line([p_bbf, p_flf], fill="#888888", width=1)
    draw.line([p_bbf, p_bbt], fill="#888888", width=1)
    draw.line([p_flf, p_flt], fill="#888888", width=1)

    draw.polygon([p_fft, p_frt, p_bbt, p_flt], fill="#FAFAFA", outline="#000000")
    draw.line([p_fft, p_frt], fill="#000000", width=2)
    draw.line([p_frt, p_bbt], fill="#000000", width=2)
    draw.line([p_bbt, p_flt], fill="#000000", width=2)
    draw.line([p_flt, p_fft], fill="#000000", width=2)

    draw.line([p_fft, p_fff], fill="#000000", width=2)
    draw.line([p_frt, p_frf], fill="#000000", width=2)
    draw.line([p_fff, p_frf], fill="#000000", width=2)
    draw.line([p_frf, p_bbf], fill="#000000", width=2)

    draw.rounded_rectangle([cx_b - 110, cy_b - 95, cx_b + 110, cy_b - 35], radius=15, fill="#EFEFEF", outline="#000000", width=2)
    draw_rich_text(draw, (cx_b - 110, cy_b - 90, 220, 45), "主耐压电子水密舱", font_size=18, fill="#000000", bold=True)

    draw.ellipse([cx_b - 6, cy_b - 6, cx_b + 6, cy_b + 6], fill="#000000")
    draw_rich_text(draw, (cx_b - 110, cy_b - 15, 100, 30), "{b}: O{sub:b}", font_size=23, fill="#000000", bold=True)

    # 附体系三轴
    draw_arrow(draw, (cx_b, cy_b), (cx_b + 280, cy_b - 45), fill="#000000", width=3, arrow_len=14, arrow_w=8)
    draw_rich_text(draw, (cx_b + 285, cy_b - 80, 260, 40), "x{sub:b} (前向 Surge, 速度 u, 力 X)\n横滚角 ϕ, 角速度 p", font_size=18, fill="#000000", bold=True)

    draw_arrow(draw, (cx_b, cy_b), (cx_b + 70, cy_b + 210), fill="#000000", width=3, arrow_len=14, arrow_w=8)
    draw_rich_text(draw, (cx_b + 75, cy_b + 215, 260, 40), "y{sub:b} (右舷 Sway, 速度 v, 力 Y)\n俯仰角 θ, 角速度 q", font_size=18, fill="#000000", bold=True)

    draw_arrow(draw, (cx_b, cy_b), (cx_b, cy_b + 240), fill="#000000", width=3, arrow_len=14, arrow_w=8)
    draw_rich_text(draw, (cx_b - 280, cy_b + 225, 270, 40), "z{sub:b} (下向 Heave, 速度 w, 力 Z)\n偏航角 ψ, 角速度 r", font_size=18, fill="#000000", bold=True)

    draw.arc([cx_b + 120, cy_b - 50, cx_b + 160, cy_b - 10], start=30, end=270, fill="#000000", width=2)
    draw.arc([cx_b + 30, cy_b + 80, cx_b + 70, cy_b + 120], start=30, end=270, fill="#000000", width=2)
    draw.arc([cx_b - 30, cy_b + 120, cx_b + 10, cy_b + 160], start=30, end=270, fill="#000000", width=2)

    # 底部严格对应表
    table_y = oy_a + 695
    draw.line([ox_a + 20, table_y, ox_a + w_a - 20, table_y], fill="#000000", width=2)
    headers = ["自由度 (DOF)", "线/角位置 (η)", "线/角速度 (ν)", "力和力矩 (τ)"]
    xs = [ox_a + 35, ox_a + 295, ox_a + 565, ox_a + 835]
    for idx, h_txt in enumerate(headers):
        draw_rich_text(draw, (xs[idx], table_y + 8, 220, 30), h_txt, font_size=19, fill="#000000", bold=True, align="left")
    draw.line([ox_a + 20, table_y + 42, ox_a + w_a - 20, table_y + 42], fill="#000000", width=1)

    rows = [
        ("1. 纵荡 (Surge, 沿 x{sub:b})", "x (前向位移)", "u (前向线速度)", "X (纵向推进力 F{sub:x})"),
        ("2. 横荡 (Sway, 沿 y{sub:b})", "y (侧向位移)", "v (横向线速度)", "Y (横向推进力 F{sub:y})"),
        ("3. 垂荡 (Heave, 沿 z{sub:b})", "z (下向位移/深度)", "w (垂向线速度)", "Z (垂向推进力 F{sub:z})"),
        ("4. 横滚 (Roll, 绕 x{sub:b})", "ϕ (横滚角)", "p (横滚角速度)", "K (横滚力矩 M{sub:x})"),
        ("5. 俯仰 (Pitch, 绕 y{sub:b})", "θ (俯仰角)", "q (俯仰角速度)", "M (俯仰力矩 M{sub:y})"),
        ("6. 偏航 (Yaw, 绕 z{sub:b})", "ψ (航向角)", "r (偏航角速度)", "N (偏航力矩 M{sub:z})"),
    ]
    for r_idx, row in enumerate(rows):
        ry = table_y + 48 + r_idx * 35
        for c_idx, val in enumerate(row):
            draw_rich_text(draw, (xs[c_idx], ry, 250, 30), val, font_size=17, fill="#000000", align="left")
    draw.line([ox_a + 20, table_y + 48 + len(rows) * 35 + 5, ox_a + w_a - 20, table_y + 48 + len(rows) * 35 + 5], fill="#000000", width=2)

    # (b) 右图
    ox_b, oy_b = 1220, 95
    w_b, h_b = 1130, 1010
    draw.rectangle([ox_b, oy_b, ox_b + w_b, oy_b + h_b], fill="#FFFFFF", outline="#000000", width=2)
    draw_rich_line(draw, ox_b + 25, oy_b + 25, parse_rich_line("(b) 水平4矢量倾斜 + 垂直4对称推进器空间布置 (Top View / 3D)"),
                   24, fill="#000000", bold=True)

    tc_x, tc_y = ox_b + 550, oy_b + 340
    f_w, f_h = 420, 320
    draw.rectangle([tc_x - f_w / 2, tc_y - f_h / 2, tc_x + f_w / 2, tc_y + f_h / 2],
                   fill="#FAFAFA", outline="#000000", width=3)

    draw.ellipse([tc_x - 6, tc_y - 6, tc_x + 6, tc_y + 6], fill="#000000")
    draw_rich_text(draw, (tc_x + 12, tc_y - 28, 80, 25), "O{sub:b}", font_size=21, fill="#000000", bold=True)
    draw_arrow(draw, (tc_x, tc_y), (tc_x + 150, tc_y), fill="#000000", width=2)
    draw_rich_text(draw, (tc_x + 155, tc_y - 15, 95, 25), "x{sub:b} (前)", font_size=19, fill="#000000", bold=True)
    draw_arrow(draw, (tc_x, tc_y), (tc_x, tc_y + 130), fill="#000000", width=2)
    draw_rich_text(draw, (tc_x - 10, tc_y + 135, 80, 25), "y{sub:b} (右)", font_size=19, fill="#000000", bold=True)

    t_coords = [
        ("T{sub:1}", tc_x + 220, tc_y - 170, 45),
        ("T{sub:2}", tc_x - 220, tc_y - 170, 135),
        ("T{sub:3}", tc_x - 220, tc_y + 170, 225),
        ("T{sub:4}", tc_x + 220, tc_y + 170, 315),
    ]

    for name, px, py, deg in t_coords:
        rad = math.radians(deg)
        draw.ellipse([px - 22, py - 22, px + 22, py + 22], fill="#EAEAEA", outline="#000000", width=2)
        draw_rich_text(draw, (px - 25, py - 13, 50, 25), name, font_size=19, fill="#000000", bold=True)
        arr_dx = int(65 * math.cos(rad))
        arr_dy = int(65 * math.sin(rad))
        draw_arrow(draw, (px, py), (px + arr_dx, py + arr_dy), fill="#000000", width=3, arrow_len=13, arrow_w=7)
        draw.line([(tc_x, tc_y), (px, py)], fill="#888888", width=1)

    draw_rich_text(draw, (tc_x + 230, tc_y - 120, 120, 25), "α = 45°", font_size=18, fill="#000000", bold=True)
    draw.arc([tc_x + 190, tc_y - 180, tc_x + 250, tc_y - 120], start=0, end=45, fill="#000000", width=1)

    # 4台垂直推进器 (避免使用渲染为□的特殊箭头字符，用 (垂向 ±zb) 代替)
    vt_coords = [
        ("T{sub:5}", tc_x + 130, tc_y - 75),
        ("T{sub:6}", tc_x - 130, tc_y - 75),
        ("T{sub:7}", tc_x - 130, tc_y + 75),
        ("T{sub:8}", tc_x + 130, tc_y + 75),
    ]
    for name, px, py in vt_coords:
        draw.ellipse([px - 20, py - 20, px + 20, py + 20], fill="#FFFFFF", outline="#000000", width=2)
        draw.ellipse([px - 13, py - 13, px + 13, py + 13], fill="#E0E0E0", outline="#000000", width=1)
        draw_rich_text(draw, (px - 20, py - 12, 40, 25), name, font_size=17, fill="#000000", bold=True)
        draw_rich_text(draw, (px + 24, py - 12, 110, 25), "(垂向 ±z{sub:b})", font_size=15, fill="#000000")

    # 说明小框
    box_math_y = oy_b + 580
    draw.rounded_rectangle([ox_b + 35, box_math_y, ox_b + w_b - 35, oy_b + h_b - 25], radius=6, fill="#F9F9F9", outline="#000000", width=2)
    draw_rich_line(draw, ox_b + 55, box_math_y + 18, parse_rich_line("八推进器 6×8 控制分配与空间力臂映射原理 (Control Allocation Mapping)"), 21, fill="#000000", bold=True)

    math_lines = [
        "1. 单推进器推力与力矩矢量: b{sub:i} = [d{sub:i}{sup:T}, (r{sub:i} × d{sub:i}){sup:T}]{sup:T} ∈ R{sup:6} (i = 1, …, 8)",
        "   - r{sub:i} ∈ R{sup:3} 为第 i 个推进器在附体系 {b} 中的空间安装位置矢量 (力臂)",
        "   - d{sub:i} ∈ R{sup:3} 为第 i 个推进器产生的推力方向单位矢量",
        "2. 八推进器推力分配矩阵方程: τ{sub:c} = B T = [b{sub:1}, b{sub:2}, …, b{sub:8}] [T{sub:1}, T{sub:2}, …, T{sub:8}]{sup:T}",
        "   - 水平 4 推进器 (T{sub:1} ~ T{sub:4}): 呈 45° 矢量布置，协同产生纵荡力 X、横荡力 Y 及偏航力矩 N",
        "   - 垂直 4 推进器 (T{sub:5} ~ T{sub:8}): 呈矩形对称垂直布置，协同产生垂荡力 Z、横滚力矩 K 及俯仰力矩 M",
        "3. 实际执行器幅值物理约束: T{sub:min} ≤ T{sub:i} ≤ T{sub:max} (正转最大推力 / 反转最大推力边界)",
    ]
    for m_idx, ml in enumerate(math_lines):
        draw_rich_line(draw, ox_b + 55, box_math_y + 55 + m_idx * 46, parse_rich_line(ml), 18, fill="#000000")

    fp_png = os.path.join(OUT_DIR, "fig0_rov_coord_thrusters.png")
    img.save(fp_png, dpi=(300, 300))
    print(f"[OK] 已生成图2坐标与推进器布置黑白图 (300 DPI): {fp_png}")


# ==============================================================================
# 3. 图 3：课题总体研究技术路线图
# ==============================================================================

def generate_fig1_technical_roadmap():
    w, h = 2400, 1350
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw_rich_line(draw, 50, 35, parse_rich_line("图 3  课题总体研究技术路线图"), 30, fill="#000000", bold=True)
    draw_rich_line(draw, 50, 80, parse_rich_line("“已有实验平台 → 机理建模与系统辨识 → 模型运动控制与控制分配 → PX4/SITL闭环验证”四阶段全链路闭环"), 20, fill="#444444")

    col_w = 540
    spacing = 40
    start_x = 60
    start_y = 130
    box_h = 1170

    phases = [
        ("阶段一：实验平台梳理与六自由度动力学建模", [
            ("已有八推进器开架式物理平台", "实验室已有开架式ROV机械构型方案\n空间几何尺寸、质量与重心/浮心属性\n8推进器空间三维布置与矢量倾斜角度"),
            ("北东地惯性系与附体系定义", "定义惯性坐标系 {n} 与附体坐标系 {b}\n6-DOF 广义位置矢量 η 与线/角速度矢量 ν\n建立运动学欧拉角坐标变换矩阵 J(η)"),
            ("非线性流体动力学机理建模", "刚体惯性矩阵 M{sub:RB} 与水动力附加质量 M{sub:A}\n刚体/附加质量科氏向心力矩阵 C(ν)\n线性与非线性水动力阻尼矩阵 D(ν)\n重浮力恢复力与力矩矢量 g(η)"),
            ("推进器特性与静态映射建模", "单推进器推力-转速静态映射特性\n推力正反向非对称与死区特性分析\n为控制分配矩阵建立提供物理基础"),
        ]),
        ("阶段二：系统辨识与模型验证分析", [
            ("先验物理参数提取与辨识量梳理", "基于物理平台设计资料确定几何/惯性先验\n梳理出主导动态响应的关键未知水动力参数集 θ\n分析各自由度方程的参数解耦与可辨识性"),
            ("辨识激励输入设计与动态响应采样", "设计推进器阶跃推力与多频正弦扫频激励\n记录纵荡、横荡、垂荡与姿态角速度响应输出\n明确系统辨识的明确输入输出数据映射链路"),
            ("水动力阻尼与附加质量参数估计", "构建最小二乘或优化回归目标函数\n辨识得到标称模型参数: {hat:M}, {hat:C}, {hat:D}, {hat:g}\n修正非线性阻尼项与附加质量主导项"),
            ("代表性动态响应对比与模型验证", "代表性阶跃响应与典型运动轨迹拟合对比\n量化分析模型输出与真实数据之间的残差指标\n评估标称动力学模型的保真度与适用范围边界"),
        ]),
        ("阶段三：模型运动控制与八推进器控制分配", [
            ("闭环运动控制系统总体架构设计", "基于经验证的航行器标称动力学模型\n引入期望位置/姿态 η{sub:r} 与参考速度 ν{sub:r}\n定义状态跟踪误差 e{sub:η} 与速度误差 e{sub:ν}"),
            ("融合模型补偿与状态反馈的控制律", "前馈补偿项 F{sub:model}(·): 抵消静水力与阻尼耦合\n反馈调节项 F{sub:fb}(·): 状态误差自适应消除残差\n输出期望空间六维广义力和力矩 τ{sub:c} ∈ R{sup:6}\n(预留模型前馈、反馈线性化与增量动态逆比选)"),
            ("八推进器 6×8 控制分配矩阵构建", "根据8推进器位置 r{sub:i} 与矢量方向 d{sub:i}\n建立各推进器推力与机体合力矩映射矩阵 B ∈ R{sup:6×8}\n(水平4矢量倾斜 + 垂直4对称布局)"),
            ("推力范围物理约束与分配误差分析", "系统考虑推进器推力上下限 [T{sub:min}, T{sub:max}]\n研究基于有界二次规划/截断伪逆的分配算法\n量化分析分配残差 e{sub:τ} = τ{sub:c} − BT 及推力饱和"),
        ]),
        ("阶段四：PX4/SITL闭环仿真与系统性能验证", [
            ("PX4 软件在环 (SITL) 架构搭建", "基于 PX4 Autopilot 模块化开源飞控架构\n配置水下航行器参数混控与执行器映射\n依托 NuttX / POSIX 环境运行原生控制算法"),
            ("uORB 微消息异步发布/订阅总线集成", "发布 vehicle_attitude / trajectory_setpoint 消息\n订阅 sensor_combined / vehicle_odometry 状态\n传输 vehicle_thrust / torque 及 actuator_motors 消息"),
            ("典型运动工况闭环仿真验证", "定深控制 (垂向克服重浮力失配与流扰)\n定向航向保持 (偏航高精度锁定)\n空间定点悬停与三维复杂轨迹跟踪仿真"),
            ("外部扰动测试与控制品质综合评价", "注入定常洋流、湍流等水下环境扰动 τ{sub:d}\n考察动态响应超调量、调节时间与稳态跟踪误差\n对比不同控制律与推力分配策略的鲁棒抗扰性能"),
        ]),
    ]

    for c_idx, (p_title, sub_boxes) in enumerate(phases):
        col_x = start_x + c_idx * (col_w + spacing)
        draw.rounded_rectangle([col_x, start_y, col_x + col_w, start_y + box_h], radius=6, fill="#FFFFFF", outline="#000000", width=2)
        draw.rounded_rectangle([col_x, start_y, col_x + col_w, start_y + 65], radius=6, fill="#EFEFEF", outline="#000000", width=2)
        draw_rich_text(draw, (col_x + 10, start_y + 12, col_w - 20, 45), p_title, font_size=20, fill="#000000", bold=True)

        sub_y = start_y + 85
        sub_h = 245
        for s_idx, (s_title, s_desc) in enumerate(sub_boxes):
            cur_y = sub_y + s_idx * (sub_h + 20)
            draw_academic_box(draw, (col_x + 20, cur_y, col_w - 40, sub_h), "", fill="#FFFFFF", border="#000000", width=1, radius=4)
            draw.rectangle([col_x + 21, cur_y + 1, col_x + col_w - 21, cur_y + 45], fill="#F8F8F8")
            draw.line([col_x + 20, cur_y + 45, col_x + col_w - 20, cur_y + 45], fill="#000000", width=1)
            draw_rich_text(draw, (col_x + 30, cur_y + 10, col_w - 60, 30), f"{c_idx+1}.{s_idx+1} {s_title}", font_size=19, fill="#000000", bold=True, align="left")
            draw_rich_text(draw, (col_x + 30, cur_y + 55, col_w - 60, sub_h - 65), s_desc, font_size=16, fill="#000000", align="left")

            if s_idx < len(sub_boxes) - 1:
                ay = cur_y + sub_h
                draw_arrow(draw, (col_x + col_w / 2, ay), (col_x + col_w / 2, ay + 20), fill="#000000", width=2, arrow_len=8, arrow_w=5)

        if c_idx < len(phases) - 1:
            next_col_x = col_x + col_w + spacing
            mid_arrow_y = start_y + box_h / 2
            draw_arrow(draw, (col_x + col_w, mid_arrow_y), (next_col_x, mid_arrow_y), fill="#000000", width=4, arrow_len=16, arrow_w=9)

    fp_png = os.path.join(OUT_DIR, "fig1_technical_roadmap.png")
    img.save(fp_png, dpi=(300, 300))
    print(f"[OK] 已生成技术路线图黑白版 (300 DPI): {fp_png}")


# ==============================================================================
# 4. 图 4：基于PX4/SITL的水下航行器闭环仿真系统结构框图
# ==============================================================================

def generate_fig2_px4_rov_architecture():
    w, h = 2400, 1200
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw_rich_line(draw, 50, 35, parse_rich_line("图 4  基于PX4/SITL的水下航行器闭环仿真系统结构框图"), 30, fill="#000000", bold=True)
    draw_rich_line(draw, 50, 80, parse_rich_line("PX4 Autopilot 开源固件架构与 uORB 异步微消息总线闭环仿真链路"), 20, fill="#444444")

    # 上半部分：PX4 自动驾驶仪飞控固件
    draw.rounded_rectangle([60, 130, 2340, 520], radius=8, fill="#FAFAFA", outline="#000000", width=3)
    draw_rich_line(draw, 90, 155, parse_rich_line("PX4 Autopilot 控制系统固件架构 (原生 C++ 模块 / NuttX & POSIX 运行时)"), 24, fill="#000000", bold=True)

    m_w = 510
    m_h = 280
    m_xs = [90, 660, 1230, 1800]
    m_y = 205

    draw_academic_box(draw, (m_xs[0], m_y, m_w, m_h),
                      "自主任务与期望轨迹规划模块\n(Navigator / Mission Planner)\n\n"
                      "- 接收地面站 QGroundControl 航点指令\n"
                      "- 生成三维平滑参考位姿轨迹: η{sub:r}(t)\n"
                      "- 输出期望参考线速度与角速度: ν{sub:r}(t)\n"
                      "- 定深、定向悬停及自动返航模式切换",
                      font_size=18, fill="#FFFFFF", border="#000000", align="left")

    draw_academic_box(draw, (m_xs[1], m_y, m_w, m_h),
                      "水下航行器闭环运动控制模块\n(UUV Motion Controller)\n\n"
                      "- 基于标称模型动力学前馈补偿 F{sub:model}(·)\n"
                      "- 姿态、深度与航向状态误差鲁棒反馈 F{sub:fb}(·)\n"
                      "- 输出期望三维控制力与力矩矢量:\n"
                      "  τ{sub:c} = [F{sub:x}, F{sub:y}, F{sub:z}, M{sub:x}, M{sub:y}, M{sub:z}]{sup:T} ∈ R{sup:6}",
                      font_size=18, fill="#FFFFFF", border="#000000", align="left")

    draw_academic_box(draw, (m_xs[2], m_y, m_w, m_h),
                      "八推进器受约束控制分配模块\n(8-Thruster Control Allocator)\n\n"
                      "- 载入物理平台 6×8 推力几何配置矩阵 B\n"
                      "- 推进器物理幅值边界约束求解: T{sub:min} ≤ T ≤ T{sub:max}\n"
                      "- 输出8通道标准化推力指令: T = [T{sub:1}, …, T{sub:8}]{sup:T}\n"
                      "- 实时计算并记录分配残差: e{sub:τ} = τ{sub:c} − BT",
                      font_size=18, fill="#FFFFFF", border="#000000", align="left")

    draw_academic_box(draw, (m_xs[3], m_y, m_w, m_h),
                      "扩展卡尔曼滤波全状态估计模块\n(EKF2 State Estimator)\n\n"
                      "- 多源传感器高频异步数据融合\n"
                      "- 滤波重构航行器全状态估计值:\n"
                      "  位姿: {hat:η} = [{hat:x}, {hat:y}, {hat:z}, {hat:ϕ}, {hat:θ}, {hat:ψ}]{sup:T}\n"
                      "  速度: {hat:ν} = [{hat:u}, {hat:v}, {hat:w}, {hat:p}, {hat:q}, {hat:r}]{sup:T}\n"
                      "- 实时传感器故障检测与方差评估",
                      font_size=18, fill="#FFFFFF", border="#000000", align="left")

    # 中间部分：uORB 实时异步总线
    uorb_y = 570
    uorb_h = 95
    draw.rectangle([60, uorb_y, 2340, uorb_y + uorb_h], fill="#F0F0F0", outline="#000000", width=2)
    draw_rich_line(draw, 90, uorb_y + 15, parse_rich_line("uORB (Micro Object Request Broker) 实时微消息通信总线 (微秒级发布/订阅机制)"), 22, fill="#000000", bold=True)

    topics = [
        "trajectory_setpoint\n(参考位姿/速度)",
        "vehicle_attitude / status\n(机体当前位姿与状态)",
        "vehicle_torque / thrust_setpoint\n(期望广义力和力矩 τ{sub:c})",
        "actuator_motors\n(8通道推进器输出指令 T)",
        "sensor_combined / odometry\n(传感器数据与状态反馈)"
    ]
    t_xs = [90, 540, 990, 1440, 1890]
    for idx, t_txt in enumerate(topics):
        draw_academic_box(draw, (t_xs[idx], uorb_y + 45, 410, 42), t_txt, font_size=15, fill="#FFFFFF", border="#000000", bold=True)

    # 下半部分：SITL 软件在环物理仿真环境
    draw.rounded_rectangle([60, 710, 2340, 1140], radius=8, fill="#FAFAFA", outline="#000000", width=3)
    draw_rich_line(draw, 90, 735, parse_rich_line("SITL 软件在环物理仿真环境 (Simulation-In-The-Loop / 外部物理引擎与日志黑匣子)"), 24, fill="#000000", bold=True)

    s_xs = [90, 660, 1230, 1800]
    s_y = 785
    s_h = 320

    draw_academic_box(draw, (s_xs[0], s_y, m_w, s_h),
                      "SITL 通信桥接与锁步调度中间件\n(Lockstep Simulator Bridge)\n\n"
                      "- TCP / UDP / MAVLink 双向实时通信接口\n"
                      "- 物理时间与飞控时钟高保真严格锁步同步\n"
                      "- 支持毫秒级断点调试与多倍速非实时仿真\n"
                      "- 接收各推进器指令并下发物理仿真机",
                      font_size=18, fill="#FFFFFF", border="#000000", align="left")

    draw_academic_box(draw, (s_xs[1], s_y, m_w, s_h),
                      "水下八推进器水动力执行机构模型\n(Thruster & Propeller Model)\n\n"
                      "- 8通道推进器直流无刷电机一阶动态响应\n"
                      "- 螺旋桨转速-推力二次非线性映射特性\n"
                      "- 正反转推力非对称系数与死区模拟\n"
                      "- 输出机体所受真实合推力与力矩矢量 τ = BT",
                      font_size=18, fill="#FFFFFF", border="#000000", align="left")

    draw_academic_box(draw, (s_xs[2], s_y, m_w, s_h),
                      "水下航行器六自由度流体动力学环境\n(6-DOF Underwater Vehicle Plant)\n\n"
                      "- 刚体惯性 M{sub:RB} 与水动力附加质量 M{sub:A}\n"
                      "- 科氏力与向心力耦合作用 C(ν)\n"
                      "- 线性与二次非线性水动力黏性阻尼 D(ν)\n"
                      "- 重心/浮心恢复力矩 g(η) 及外部流扰 τ{sub:d}",
                      font_size=18, fill="#FFFFFF", border="#000000", align="left")

    draw_academic_box(draw, (s_xs[3], s_y, m_w, s_h),
                      "虚拟传感仪表与全工况日志记录\n(Virtual Sensors & ULog Logger)\n\n"
                      "- IMU 加速度计/陀螺仪高频白噪声与零偏模拟\n"
                      "- 虚拟深度水压传感器与 DVL 测速噪声\n"
                      "- 高频 ULog 黑匣子记录全闭环试验数据\n"
                      "- MATLAB / Python 离线指标评估与消融分析",
                      font_size=18, fill="#FFFFFF", border="#000000", align="left")

    # 飞控与仿真间的垂直双向交互箭头 (彻底修复坐标)
    draw_arrow(draw, (m_xs[0] + m_w / 2, m_y + m_h), (m_xs[0] + m_w / 2, uorb_y), fill="#000000", width=2)
    draw_arrow(draw, (m_xs[1] + m_w / 2, m_y + m_h), (m_xs[1] + m_w / 2, uorb_y), fill="#000000", width=2)
    draw_arrow(draw, (m_xs[2] + m_w / 2, m_y + m_h), (m_xs[2] + m_w / 2, uorb_y), fill="#000000", width=2)
    # EKF2 从 uORB 订阅传感器数据 (向上箭头)
    draw_arrow(draw, (m_xs[3] + m_w / 2, uorb_y), (m_xs[3] + m_w / 2, m_y + m_h), fill="#000000", width=2)

    # uORB 向下传递给 SITL Bridge
    draw_arrow(draw, (s_xs[0] + m_w / 2, uorb_y + uorb_h), (s_xs[0] + m_w / 2, s_y), fill="#000000", width=2)
    draw_arrow(draw, (s_xs[0] + m_w, s_y + s_h / 2), (s_xs[1], s_y + s_h / 2), fill="#000000", width=2)
    draw_arrow(draw, (s_xs[1] + m_w, s_y + s_h / 2), (s_xs[2], s_y + s_h / 2), fill="#000000", width=2)
    draw_arrow(draw, (s_xs[2] + m_w, s_y + s_h / 2), (s_xs[3], s_y + s_h / 2), fill="#000000", width=2)
    # Virtual Sensors 向上发布给 uORB (向上箭头)
    draw_arrow(draw, (s_xs[3] + m_w / 2, s_y), (s_xs[3] + m_w / 2, uorb_y + uorb_h), fill="#000000", width=2)

    fp_png = os.path.join(OUT_DIR, "fig2_px4_rov_architecture.png")
    img.save(fp_png, dpi=(300, 300))
    print(f"[OK] 已生成PX4架构图黑白版 (300 DPI): {fp_png}")


def build_all_figures():
    print("=== 开始生成开题报告全套出版级纯黑白学术配图 (300 DPI) ===")
    generate_fig1_lit_control_architecture()
    generate_fig0_rov_coord_thrusters()
    generate_fig1_technical_roadmap()
    generate_fig2_px4_rov_architecture()
    print("=== 全套 4 幅纯黑白高清配图及 .drawio 导出完毕 ===")


if __name__ == "__main__":
    build_all_figures()
