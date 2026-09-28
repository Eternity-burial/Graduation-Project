# -*- coding: utf-8 -*-
"""
生成《基于PX4的水下航行器模型控制方法研究》开题报告出版级高清学术配图 (300 DPI PNG + 可编辑 .drawio)

严格执行极简学术制图规范（Minimalist Academic Diagram Standard）：
1. 严禁在图片内部绘制顶部总图题/副标题（图题统一由 Word 正文下方五号宋体段落承载）；
2. 严禁在图片内部塞入表格、大段文字说明或 Bullet Points 列表；
3. 单节点字数严格控制在 5~15 字词组，连线仅标注核心数学符号或 uORB 话题名；
4. 画布尺寸设为 1600~1850 px，正文字号 20~24 px（缩放到 Word 15cm 宽后对应 9~10.5pt，清晰易读）；
5. 黑白灰主调 + 极低饱和度学术蓝点缀（#F4F7FA / #1F4E79），正交折线连线，留白充足，零文字压线。
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
    size = max(12, int(round(size)))
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
    return total_w, int(font_size * 1.38)


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
            hy = y + bb[1] - 6
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


def draw_rich_text(draw, box, text, font_size, fill="#000000", bold=False, align="center", first_line_bold=False):
    bx, by, bw, bh = box
    lines = text.split("\n")
    parsed_lines = [parse_rich_line(ln) for ln in lines]
    line_metrics = [
        measure_rich_line(draw, toks, font_size, bold=(bold or (first_line_bold and i == 0)))
        for i, toks in enumerate(parsed_lines)
    ]
    line_h = max(m[1] for m in line_metrics) if line_metrics else int(font_size * 1.38)
    total_h = len(parsed_lines) * line_h
    start_y = by + (bh - total_h) / 2
    for idx, tokens in enumerate(parsed_lines):
        is_b = bold or (first_line_bold and idx == 0)
        lw, _ = line_metrics[idx]
        if align == "center":
            lx = bx + (bw - lw) / 2
        elif align == "right":
            lx = bx + bw - lw - 10
        else:
            lx = bx + 12
        ly = start_y + idx * line_h
        draw_rich_line(draw, lx, ly, tokens, font_size, fill=fill, bold=is_b)


def draw_arrow(draw, p1, p2, fill="#000000", width=3, arrow_len=14, arrow_w=7):
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


def draw_dashed_line(draw, p1, p2, dash_len=10, gap_len=6, fill="#666666", width=2):
    sx, sy = p1
    ex, ey = p2
    dist = math.hypot(ex - sx, ey - sy)
    if dist < 1e-4:
        return
    ux, uy = (ex - sx) / dist, (ey - sy) / dist
    pos = 0
    while pos < dist:
        end_pos = min(pos + dash_len, dist)
        draw.line([(sx + ux * pos, sy + uy * pos), (sx + ux * end_pos, sy + uy * end_pos)],
                  fill=fill, width=width)
        pos += dash_len + gap_len


def draw_dashed_rect(draw, box, dash_len=12, gap_len=8, outline="#555555", width=2, fill=None):
    x1, y1, x2, y2 = box
    if fill:
        draw.rectangle([x1, y1, x2, y2], fill=fill, outline=None)
    edges = [((x1, y1), (x2, y1)), ((x2, y1), (x2, y2)), ((x2, y2), (x1, y2)), ((x1, y2), (x1, y1))]
    for p1, p2 in edges:
        draw_dashed_line(draw, p1, p2, dash_len=dash_len, gap_len=gap_len, fill=outline, width=width)


def draw_sum_node(draw, cx, cy, r=22, signs=None):
    """绘制控制框图标准求和节点 ⊕"""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#FFFFFF", outline="#000000", width=2)
    draw.line([cx - r + 6, cy, cx + r - 6, cy], fill="#000000", width=2)
    draw.line([cx, cy - r + 6, cx, cy + r - 6], fill="#000000", width=2)
    if signs:
        for pos, s in signs.items():
            f = get_font(20, bold=True)
            if pos == "left":
                draw.text((cx - r - 20, cy - 28), s, font=f, fill="#000000")
            elif pos == "bottom":
                draw.text((cx + 8, cy + r + 1), s, font=f, fill="#000000")
            elif pos == "top":
                draw.text((cx + 8, cy - r - 26), s, font=f, fill="#000000")


def draw_node_box(draw, box, text, font_size=22, fill="#FFFFFF", border="#000000",
                  text_fill="#000000", bold=False, first_line_bold=True, width=2, radius=6):
    bx, by, bw, bh = box
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=radius, fill=fill, outline=border, width=width)
    draw_rich_text(draw, box, text, font_size=font_size, fill=text_fill, bold=bold,
                   align="center", first_line_bold=first_line_bold)


# ==============================================================================
# 1. 图 1：水下航行器六自由度模型控制与推力分配通用闭环框图
# ==============================================================================

def generate_fig1_lit_control_architecture():
    w, h = 1860, 560
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # 闭环运动控制器虚线背景框 (向右留出充足走廊避免文字贴边)
    draw_dashed_rect(draw, (315, 40, 760, 380), outline="#1F4E79", width=2, fill="#F4F7FA")
    draw_rich_text(draw, (315, 48, 445, 34), "闭环运动控制器 (模型补偿 + 状态反馈)", font_size=21, fill="#1F4E79", bold=True)

    # 核心节点坐标 (主前向通道中心线 y_mid = 230)
    y_mid = 230
    cx_sum1 = 190
    draw_sum_node(draw, cx_sum1, y_mid, r=22, signs={"left": "+", "bottom": "−"})

    # 参考输入箭头 (左侧直接进入求和节点1)
    draw_arrow(draw, (30, y_mid), (cx_sum1 - 22, y_mid), width=3)
    draw_rich_text(draw, (25, y_mid - 64, 140, 54), "参考运动指令\nη{sub:r}, ν{sub:r}", font_size=21, bold=True)

    # 控制器内上下并联支路
    box_ff = (350, 96, 305, 92)    # 上支路: 模型补偿
    box_fb = (350, 256, 305, 92)   # 下支路: 状态误差反馈
    draw_node_box(draw, box_ff, "动力学模型补偿项\nF{sub:model}({hat:M}, {hat:C}, {hat:D}, {hat:g})",
                  font_size=21, fill="#FFFFFF", border="#1F4E79", width=2)
    draw_node_box(draw, box_fb, "状态误差反馈项\nF{sub:fb}(e{sub:η}, e{sub:ν})",
                  font_size=21, fill="#FFFFFF", border="#000000", width=2)

    # 求和节点1 -> 状态误差反馈项 (折线设在 x=285，使 e_η, e_ν 居中于 212..295 之间，绝不碰虚线框)
    draw.line([(cx_sum1 + 22, y_mid), (285, y_mid)], fill="#000000", width=3)
    draw.line([(285, y_mid), (285, 302)], fill="#000000", width=3)
    draw_arrow(draw, (285, 302), (350, 302), width=3)
    draw_rich_text(draw, (212, y_mid - 42, 72, 34), "e{sub:η}, e{sub:ν}", font_size=20, bold=True)

    # 参考信号分支 -> 模型补偿项
    draw.line([(125, y_mid), (125, 142)], fill="#000000", width=2)
    draw_arrow(draw, (125, 142), (350, 142), width=2)

    # 控制器内部合成节点 ⊕2
    cx_sum2 = 710
    draw_sum_node(draw, cx_sum2, y_mid, r=20, signs={"top": "+", "bottom": "+"})
    draw.line([(655, 142), (cx_sum2, 142)], fill="#000000", width=3)
    draw_arrow(draw, (cx_sum2, 142), (cx_sum2, y_mid - 20), width=3)
    draw.line([(655, 302), (cx_sum2, 302)], fill="#000000", width=3)
    draw_arrow(draw, (cx_sum2, 302), (cx_sum2, y_mid + 20), width=3)

    # 控制分配模块 (加宽至 315 px，两侧留白充裕)
    box_alloc = (880, 174, 315, 112)
    draw_arrow(draw, (cx_sum2 + 20, y_mid), (880, y_mid), width=3)
    draw_rich_text(draw, (765, y_mid - 64, 110, 56), "期望广义力\nτ{sub:c} ∈ R{sup:6}", font_size=20, bold=True)
    draw_node_box(draw, box_alloc, "过驱动控制分配\nB ∈ R{sup:6×8},  T{sub:min} ≤ T ≤ T{sub:max}",
                  font_size=20, fill="#F4F7FA", border="#1F4E79", width=2)

    # 推进器与6-DOF动力学受控对象
    cx_sum3 = 1315
    draw_arrow(draw, (1195, y_mid), (cx_sum3 - 20, y_mid), width=3)
    draw_rich_text(draw, (1198, y_mid - 64, 98, 56), "推力指令\nT ∈ R{sup:8}", font_size=20, bold=True)
    draw_sum_node(draw, cx_sum3, y_mid, r=20, signs={"left": "+", "top": "+"})

    # 外部水流扰动输入
    draw_arrow(draw, (cx_sum3, 100), (cx_sum3, y_mid - 20), width=3)
    draw_rich_text(draw, (cx_sum3 - 100, 42, 200, 50), "外部水流扰动 τ{sub:d}", font_size=21, bold=True)

    # 航行器动力学框 (加宽至 355 px，方程两侧留白 > 22 px)
    box_plant = (1370, 172, 355, 116)
    draw_arrow(draw, (cx_sum3 + 20, y_mid), (1370, y_mid), width=3)
    draw_node_box(draw, box_plant, "推进器与 6-DOF 动力学\nM{dot:ν} + C(ν)ν + D(ν)ν + g(η) = τ + τ{sub:d}",
                  font_size=19, fill="#FFFFFF", border="#000000", width=2)

    # 系统输出箭头
    draw_arrow(draw, (1725, y_mid), (1835, y_mid), width=3)
    draw_rich_text(draw, (1735, y_mid - 64, 95, 56), "运动状态\nη, ν", font_size=21, bold=True)

    # 下方反馈通道：导航传感与状态估计 (加宽至 510 px，文字居中留白充裕)
    y_fb = 465
    box_est = (760, y_fb - 45, 510, 90)
    draw_node_box(draw, box_est, "机载导航传感与状态估计 (IMU / 深度计 / EKF)",
                  font_size=21, fill="#FAFAFA", border="#000000", width=2, first_line_bold=True)

    # 右侧向下反馈支路
    fb_tap_x = 1765
    draw.ellipse([fb_tap_x - 5, y_mid - 5, fb_tap_x + 5, y_mid + 5], fill="#000000")
    draw.line([(fb_tap_x, y_mid), (fb_tap_x, y_fb)], fill="#000000", width=3)
    draw_arrow(draw, (fb_tap_x, y_fb), (1270, y_fb), width=3)

    # 状态估计向左回传至求和节点1
    draw.line([(760, y_fb), (cx_sum1, y_fb)], fill="#000000", width=3)
    draw_arrow(draw, (cx_sum1, y_fb), (cx_sum1, y_mid + 22), width=3)
    draw_rich_text(draw, (420, y_fb - 44, 260, 38), "状态反馈估计 {hat:η}, {hat:ν}", font_size=21, bold=True)

    fp_png = os.path.join(OUT_DIR, "fig1_lit_control_architecture.png")
    img.save(fp_png, dpi=(300, 300))
    print(f"[OK] 已生成图1 (通用闭环框图, 300 DPI): {fp_png}")


# ==============================================================================
# 2. 图 2：八推进器水下航行器坐标系定义与推力矢量空间布置示意图 (纯净双子图)
# ==============================================================================

def generate_fig0_rov_coord_thrusters():
    w, h = 1840, 740
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # ---------------- 左子图 (a): 惯性系 {n} 与附体系 {b} ----------------
    ox_a, oy_a, w_a, h_a = 25, 20, 870, 700
    draw.rounded_rectangle([ox_a, oy_a, ox_a + w_a, oy_a + h_a], radius=6, fill="#FFFFFF", outline="#000000", width=2)
    draw_rich_text(draw, (ox_a + 20, oy_a + 18, w_a - 40, 38),
                   "(a) 北东地惯性系 {n} 与附体系 {b} 六自由度定义", font_size=23, bold=True)

    # 惯性系 {n} (左上角独立清爽区域)
    on_x, on_y = ox_a + 135, oy_a + 150
    draw.ellipse([on_x - 5, on_y - 5, on_x + 5, on_y + 5], fill="#000000")
    draw_rich_text(draw, (on_x - 105, on_y - 38, 100, 34), "{n}: O{sub:n}", font_size=22, bold=True)
    draw_arrow(draw, (on_x, on_y), (on_x + 135, on_y - 38), width=3)
    draw_rich_text(draw, (on_x + 142, on_y - 56, 145, 34), "x{sub:n} (北 N)", font_size=20, bold=True, align="left")
    draw_arrow(draw, (on_x, on_y), (on_x + 130, on_y + 42), width=3)
    draw_rich_text(draw, (on_x + 138, on_y + 26, 145, 34), "y{sub:n} (东 E)", font_size=20, bold=True, align="left")
    draw_arrow(draw, (on_x, on_y), (on_x, on_y + 130), width=3)
    draw_rich_text(draw, (on_x - 55, on_y + 136, 150, 34), "z{sub:n} (地 D)", font_size=20, bold=True)

    # 附体系 {b} 与 ROV 立体几何线框
    cx_b, cy_b = ox_a + 455, oy_a + 395
    L, W, H = 175, 115, 80

    p_fff = (cx_b + L, cy_b - 22)
    p_frf = (cx_b + 38, cy_b + W)
    p_flf = (cx_b - 38, cy_b - W)
    p_bbf = (cx_b - L, cy_b + 22)

    p_fft = (p_fff[0], p_fff[1] - H)
    p_frt = (p_frf[0], p_frf[1] - H)
    p_flt = (p_flf[0], p_flf[1] - H)
    p_bbt = (p_bbf[0], p_bbf[1] - H)

    # 背面虚化棱线
    draw.line([p_bbf, p_flf], fill="#BBBBBB", width=2)
    draw.line([p_bbf, p_bbt], fill="#BBBBBB", width=2)
    draw.line([p_flf, p_flt], fill="#BBBBBB", width=2)

    # 顶面浅蓝灰填充与前景实线
    draw.polygon([p_fft, p_frt, p_bbt, p_flt], fill="#F4F7FA", outline="#1F4E79")
    for p1, p2 in [(p_fft, p_frt), (p_frt, p_bbt), (p_bbt, p_flt), (p_flt, p_fft),
                   (p_fft, p_fff), (p_frt, p_frf), (p_fff, p_frf), (p_frf, p_bbf)]:
        draw.line([p1, p2], fill="#1F4E79", width=2)

    # 惯性系到附体系的广义位置矢量 η 虚线箭头 (标签置于虚线上方空白区，不压任何棱线)
    draw_dashed_line(draw, (on_x + 12, on_y + 12), (cx_b - 14, cy_b - 10), dash_len=10, gap_len=6, fill="#555555", width=2)
    draw_arrow(draw, (cx_b - 42, cy_b - 31), (cx_b - 10, cy_b - 7), fill="#555555", width=2)
    draw_rich_text(draw, (ox_a + 185, oy_a + 265, 135, 34), "位姿矢量 η", font_size=20, fill="#333333", bold=True)

    # 质心原点 Ob (标注在原点正上方顶面空白处，完全不碰边框线)
    draw.ellipse([cx_b - 6, cy_b - 6, cx_b + 6, cy_b + 6], fill="#000000")
    draw_rich_text(draw, (cx_b - 45, cy_b - 56, 110, 34), "{b}: O{sub:b}", font_size=22, bold=True)

    # 附体系三轴与速度/角速度标注 (全部位于线框外侧空白区，零重叠)
    # xb 轴 (前向)
    xb_end = (cx_b + 255, cy_b - 38)
    draw_arrow(draw, (cx_b, cy_b), xb_end, fill="#000000", width=3, arrow_len=15, arrow_w=8)
    draw_rich_text(draw, (cx_b + 185, cy_b - 115, 215, 62),
                   "x{sub:b} (前向)\n纵荡 u, 横滚 p", font_size=20, bold=True)

    # yb 轴 (右舷)
    yb_end = (cx_b + 65, cy_b + 205)
    draw_arrow(draw, (cx_b, cy_b), yb_end, fill="#000000", width=3, arrow_len=15, arrow_w=8)
    draw_rich_text(draw, (cx_b + 82, cy_b + 170, 215, 62),
                   "y{sub:b} (右舷)\n横荡 v, 俯仰 q", font_size=20, bold=True, align="left")

    # zb 轴 (下向)
    zb_end = (cx_b, cy_b + 225)
    draw_arrow(draw, (cx_b, cy_b), zb_end, fill="#000000", width=3, arrow_len=15, arrow_w=8)
    draw_rich_text(draw, (cx_b - 235, cy_b + 175, 220, 62),
                   "z{sub:b} (下向)\n垂荡 w, 偏航 r", font_size=20, bold=True, align="right")

    # ---------------- 右子图 (b): 八推进器空间布置俯视图 ----------------
    ox_b, oy_b, w_b, h_b = 930, 20, 885, 700
    draw.rounded_rectangle([ox_b, oy_b, ox_b + w_b, oy_b + h_b], radius=6, fill="#FFFFFF", outline="#000000", width=2)
    draw_rich_text(draw, (ox_b + 20, oy_b + 18, w_b - 40, 38),
                   "(b) 八推进器空间对称与矢量布置俯视图 (6×8 构型)", font_size=23, bold=True)

    # 标准俯视图：机头朝上 (+xb 前向)，右舷朝右 (+yb 右舷)
    tc_x, tc_y = ox_b + 435, oy_b + 355
    f_w, f_h = 360, 360
    draw.rounded_rectangle([tc_x - f_w / 2, tc_y - f_h / 2, tc_x + f_w / 2, tc_y + f_h / 2],
                           radius=12, fill="#FAFAFA", outline="#000000", width=3)

    # 质心 Ob 与附体系坐标轴
    draw.ellipse([tc_x - 6, tc_y - 6, tc_x + 6, tc_y + 6], fill="#000000")
    draw_rich_text(draw, (tc_x - 62, tc_y + 8, 55, 30), "O{sub:b}", font_size=21, bold=True)
    # +xb 向上走出机架上沿
    draw_arrow(draw, (tc_x, tc_y), (tc_x, tc_y - 250), fill="#1F4E79", width=3)
    draw_rich_text(draw, (tc_x + 12, tc_y - 265, 130, 34), "+x{sub:b} (机头前)", font_size=20, fill="#1F4E79", bold=True, align="left")
    # +yb 向右走出机架右沿
    draw_arrow(draw, (tc_x, tc_y), (tc_x + 250, tc_y), fill="#1F4E79", width=3)
    draw_rich_text(draw, (tc_x + 256, tc_y - 18, 125, 34), "+y{sub:b} (右舷)", font_size=20, fill="#1F4E79", bold=True, align="left")

    # 四个角：水平面矢量倾斜推进器 T1(右前), T2(左前), T3(左后), T4(右后)
    horiz_thrusters = [
        ("T{sub:1}", tc_x + 180, tc_y - 180, -45),
        ("T{sub:2}", tc_x - 180, tc_y - 180, -135),
        ("T{sub:3}", tc_x - 180, tc_y + 180, 135),
        ("T{sub:4}", tc_x + 180, tc_y + 180, 45),
    ]
    for name, px, py, deg in horiz_thrusters:
        # 力臂虚线 r_i
        draw_dashed_line(draw, (tc_x, tc_y), (px, py), dash_len=8, gap_len=6, fill="#888888", width=2)
        # 推进器导流罩圆圈
        r_t = 28
        draw.ellipse([px - r_t, py - r_t, px + r_t, py + r_t], fill="#DCE6F2", outline="#1F4E79", width=3)
        draw_rich_text(draw, (px - 28, py - 18, 56, 36), name, font_size=20, fill="#000000", bold=True)
        # 推力方向单位矢量箭头 d_i
        rad = math.radians(deg)
        ax = px + int(72 * math.cos(rad))
        ay = py + int(72 * math.sin(rad))
        draw_arrow(draw, (px + int(r_t * math.cos(rad)), py + int(r_t * math.sin(rad))),
                   (ax, ay), fill="#000000", width=3, arrow_len=14, arrow_w=7)

    # 内部对称：垂直面垂向推进器 T5~T8 (放置在 x = ±120, y = ±62，完全避开 45° 对角力臂线!)
    vert_thrusters = [
        ("T{sub:5}", tc_x + 120, tc_y - 62),
        ("T{sub:6}", tc_x - 120, tc_y - 62),
        ("T{sub:7}", tc_x - 120, tc_y + 62),
        ("T{sub:8}", tc_x + 120, tc_y + 62),
    ]
    for name, px, py in vert_thrusters:
        draw.ellipse([px - 27, py - 27, px + 27, py + 27], fill="#FFFFFF", outline="#000000", width=2)
        draw.ellipse([px - 20, py - 20, px + 20, py + 20], fill="#F2F2F2", outline="#000000", width=1)
        draw_rich_text(draw, (px - 27, py - 18, 54, 36), name, font_size=19, fill="#000000", bold=True)

    # 在 T1 对角线上方清晰标注力臂矢量 r_1、方向 d_1 与倾角 α = 45°
    draw_rich_text(draw, (tc_x + 52, tc_y - 122, 65, 32), "r{sub:1}", font_size=21, fill="#1F4E79", bold=True)
    draw_rich_text(draw, (tc_x + 235, tc_y - 260, 60, 32), "d{sub:1}", font_size=21, fill="#000000", bold=True)
    draw_rich_text(draw, (tc_x + 245, tc_y - 195, 110, 32), "α = 45°", font_size=20, fill="#1F4E79", bold=True, align="left")

    # 底部简洁图例栏 (左右留白充裕)
    leg_y = oy_b + 622
    draw.rounded_rectangle([ox_b + 30, leg_y, ox_b + w_b - 30, leg_y + 56],
                           radius=6, fill="#F4F7FA", outline="#1F4E79", width=1)
    draw.ellipse([ox_b + 55, leg_y + 14, ox_b + 83, leg_y + 42], fill="#DCE6F2", outline="#1F4E79", width=2)
    draw_rich_text(draw, (ox_b + 92, leg_y + 10, 320, 36),
                   "T{sub:1}~T{sub:4}: 水平45°矢量推进器", font_size=19, bold=True, align="left")
    draw.ellipse([ox_b + 435, leg_y + 14, ox_b + 463, leg_y + 42], fill="#FFFFFF", outline="#000000", width=2)
    draw.ellipse([ox_b + 441, leg_y + 20, ox_b + 457, leg_y + 36], fill="#F2F2F2", outline="#000000", width=1)
    draw_rich_text(draw, (ox_b + 472, leg_y + 10, 360, 36),
                   "T{sub:5}~T{sub:8}: 垂直对称推进器 (沿 ±z{sub:b})", font_size=19, bold=True, align="left")

    fp_png = os.path.join(OUT_DIR, "fig0_rov_coord_thrusters.png")
    img.save(fp_png, dpi=(300, 300))
    print(f"[OK] 已生成图2 (坐标系与推进器布置纯净图, 300 DPI): {fp_png}")


# ==============================================================================
# 3. 图 3：课题总体研究技术路线图 (纵向四阶段分层极简框图，对标学长V5升级版)
# ==============================================================================

def generate_fig1_technical_roadmap():
    w, h = 1600, 980
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    stages = [
        (
            "第一阶段：平台梳理与六自由度机理建模",
            "第一、二章",
            [
                "八推进器平台构型梳理\n(几何尺寸与质量特性)",
                "NED与FRD坐标系建立\n(运动学变换矩阵 J(η))",
                "6-DOF非线性动力学建模\n(M, C(ν), D(ν), g(η) 与推进器)",
            ],
        ),
        (
            "第二阶段：水动力系统辨识与模型验证",
            "第三章",
            [
                "辨识激励与数据采集\n(阶跃与多频动态响应)",
                "关键水动力参数估计\n(附加质量 M{sub:A} 与阻尼 D)",
                "标称模型验证与残差分析\n({hat:M}, {hat:C}, {hat:D}, {hat:g} 适用边界)",
            ],
        ),
        (
            "第三阶段：闭环运动控制与八推进器推力分配",
            "第四章",
            [
                "模型补偿+状态反馈控制\n(PID / FBL / INDI 比选)",
                "八推进器 6×8 分配矩阵\n(B = [b{sub:1}, …, b{sub:8}] ∈ R{sup:6×8})",
                "推力物理边界约束分配\n(T{sub:min} ≤ T ≤ T{sub:max} 与残差 e{sub:τ})",
            ],
        ),
        (
            "第四阶段：PX4/SITL 闭环仿真与性能评价",
            "第五、六章",
            [
                "PX4/SITL 软件在环集成\n(uORB 异步微消息闭环)",
                "典型运动工况闭环测试\n(定深、定向与三维轨迹)",
                "外部流扰测试与综合评价\n(跟踪误差 e{sub:η} 与分配误差 e{sub:τ})",
            ],
        ),
    ]

    margin_x = 45
    stage_w = w - 2 * margin_x
    stage_h = 190
    gap_y = 48
    start_y = 25

    for s_idx, (s_title, ch_tag, nodes) in enumerate(stages):
        sy = start_y + s_idx * (stage_h + gap_y)

        # 阶段外框
        draw.rounded_rectangle([margin_x, sy, margin_x + stage_w, sy + stage_h],
                               radius=8, fill="#F8FAFC", outline="#1F4E79", width=2)
        # 顶部阶段标题条
        draw.rounded_rectangle([margin_x, sy, margin_x + stage_w, sy + 46],
                               radius=8, fill="#E8EEF5", outline="#1F4E79", width=2)
        draw_rich_text(draw, (margin_x + 20, sy + 5, 800, 36), s_title,
                       font_size=23, fill="#1F4E79", bold=True, align="left")
        draw_rich_text(draw, (margin_x + stage_w - 260, sy + 5, 240, 36), f"对应论文：{ch_tag}",
                       font_size=21, fill="#333333", bold=True, align="right")

        # 内部 3 个横向短语节点
        node_w = 415
        node_h = 105
        node_gap = 65
        total_nodes_w = 3 * node_w + 2 * node_gap
        nx_start = margin_x + (stage_w - total_nodes_w) // 2
        ny = sy + 64

        for n_idx, n_text in enumerate(nodes):
            nx = nx_start + n_idx * (node_w + node_gap)
            draw_node_box(draw, (nx, ny, node_w, node_h), n_text,
                          font_size=22, fill="#FFFFFF", border="#000000", width=2, radius=6)
            if n_idx < 2:
                ax1 = nx + node_w
                ax2 = nx + node_w + node_gap
                ay = ny + node_h // 2
                draw_arrow(draw, (ax1, ay), (ax2, ay), fill="#1F4E79", width=3, arrow_len=14, arrow_w=7)

        # 阶段间向下大箭头
        if s_idx < len(stages) - 1:
            mid_x = w // 2
            ay1 = sy + stage_h
            ay2 = ay1 + gap_y
            draw_arrow(draw, (mid_x, ay1), (mid_x, ay2), fill="#000000", width=4, arrow_len=16, arrow_w=9)

    fp_png = os.path.join(OUT_DIR, "fig1_technical_roadmap.png")
    img.save(fp_png, dpi=(300, 300))
    print(f"[OK] 已生成图3 (纵向四阶段技术路线图, 300 DPI): {fp_png}")


# ==============================================================================
# 4. 图 4：基于PX4/SITL的水下航行器闭环仿真系统结构框图 (标准闭环框图+双层分区)
# ==============================================================================

def generate_fig2_px4_rov_architecture():
    w, h = 1860, 760
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # 上半区：PX4 Autopilot 飞控软件层 (uORB 异步消息总线)
    draw_dashed_rect(draw, (35, 25, 1825, 335), outline="#1F4E79", width=2, fill="#F4F7FA")
    draw_rich_text(draw, (55, 35, 900, 36),
                   "PX4 Autopilot 飞控软件层 (C++ 原生模块 / uORB 异步发布-订阅总线)",
                   font_size=22, fill="#1F4E79", bold=True, align="left")

    # 下半区：SITL 水下六自由度物理仿真环境 (标题置于底部左侧或中间，彻底避开左侧垂直反馈线!)
    draw_dashed_rect(draw, (35, 415, 1825, 735), outline="#333333", width=2, fill="#FAFAFA")
    draw_rich_text(draw, (55, 685, 950, 36),
                   "SITL 软件在环水下物理仿真层 (6-DOF 水动力模型与虚拟传感闭环)",
                   font_size=22, fill="#222222", bold=True, align="left")

    # ---------------- 上半区前向控制链路 (y_top = 195) ----------------
    y_top = 195
    # 1. 期望轨迹给定模块
    box_nav = (60, y_top - 55, 260, 110)
    draw_node_box(draw, box_nav, "参考运动指令生成\n(Navigator / 航点与轨迹)",
                  font_size=21, fill="#FFFFFF", border="#000000", width=2)

    # 求和节点 ⊕1 (x = 530，与左侧模块留出 210 px 宽裕走廊)
    cx_err = 530
    draw_sum_node(draw, cx_err, y_top, r=22, signs={"left": "+", "bottom": "−"})
    draw_arrow(draw, (320, y_top), (cx_err - 22, y_top), width=3)
    draw_rich_text(draw, (325, y_top - 66, 175, 58), "η{sub:r}, ν{sub:r}\n(trajectory_setpoint)", font_size=18, bold=True)

    # 2. UUV 闭环运动控制模块
    box_ctrl = (690, y_top - 58, 380, 116)
    draw_arrow(draw, (cx_err + 22, y_top), (690, y_top), width=3)
    draw_rich_text(draw, (560, y_top - 48, 120, 40), "误差 e{sub:η}, e{sub:ν}", font_size=20, bold=True)
    draw_node_box(draw, box_ctrl, "UUV 闭环运动控制模块\nF{sub:model}({hat:η},{hat:ν}) + F{sub:fb}(e{sub:η},e{sub:ν})",
                  font_size=21, fill="#FFFFFF", border="#1F4E79", width=3)

    # 3. 八推进器控制分配模块
    box_alloc = (1320, y_top - 58, 420, 116)
    draw_arrow(draw, (1070, y_top), (1320, y_top), width=3)
    draw_rich_text(draw, (1080, y_top - 66, 230, 58), "期望广义力 τ{sub:c} ∈ R{sup:6}\n(vehicle_thrust/torque)", font_size=18, bold=True)
    draw_node_box(draw, box_alloc, "八推进器 6×8 控制分配模块\nB ∈ R{sup:6×8},  T{sub:min} ≤ T ≤ T{sub:max}",
                  font_size=21, fill="#FFFFFF", border="#1F4E79", width=3)

    # ---------------- 下半区物理仿真与状态反馈链路 (y_bot = 565) ----------------
    y_bot = 565

    # 4. 右下：八推进器执行机构水动力模型
    box_thr = (1320, y_bot - 58, 420, 116)
    draw_node_box(draw, box_thr, "八推进器执行机构模型\n电机动态与推力映射 τ = BT",
                  font_size=21, fill="#FFFFFF", border="#000000", width=2)

    # 跨层下发通道：控制分配 -> 推进器模型 (沿右侧 x = 1530 垂直向下)
    x_down = 1530
    draw_arrow(draw, (x_down, y_top + 58), (x_down, y_bot - 58), fill="#1F4E79", width=3)
    draw_rich_text(draw, (x_down + 14, 344, 270, 62),
                   "8通道推力指令 T ∈ R{sup:8}\n(uORB: actuator_motors)", font_size=18, fill="#1F4E79", bold=True, align="left")

    # 扰动叠加节点 ⊕2 (位于推进器模型左侧 cx_dist = 1195)
    cx_dist = 1195
    draw_sum_node(draw, cx_dist, y_bot, r=20, signs={"top": "+"})
    draw_arrow(draw, (1320, y_bot), (cx_dist + 20, y_bot), width=3)
    draw_rich_text(draw, (1225, y_bot - 45, 85, 36), "τ ∈ R{sup:6}", font_size=20, bold=True)

    # 外部流扰注入箭头
    draw_arrow(draw, (cx_dist, 468), (cx_dist, y_bot - 20), width=3)
    draw_rich_text(draw, (cx_dist - 105, 428, 210, 34), "外部水流扰动 τ{sub:d}", font_size=20, bold=True)

    # 5. 中下：水下航行器 6-DOF 非线性动力学模型
    box_plant = (690, y_bot - 58, 380, 116)
    draw_arrow(draw, (cx_dist - 20, y_bot), (1070, y_bot), width=3)
    draw_node_box(draw, box_plant, "水下航行器 6-DOF 动力学模型\nM{dot:ν}+C(ν)ν+D(ν)ν+g(η) = τ+τ{sub:d}",
                  font_size=20, fill="#FFFFFF", border="#000000", width=2)

    # 6. 左下：虚拟传感器与 EKF2 状态估计 (以 x = cx_err = 530 为中心右侧或顶部中心对齐!)
    # 设 box_ekf = (165, y_bot - 58, 365, 116)，其顶部向上输出点设在 x = 347，正交折向 cx_err = 530，或者直接让 box_ekf 居中于 cx_err!
    # 更清爽的对称布局：让 box_ekf 位于 (160, y_bot - 58, 360, 116)，真实状态箭头在 690 -> 520 (长 170 px)，
    # 反馈线从 box_ekf 顶边中心 (x = 340) 向上到 y = 375，再向右到 x = 530 向上进入 ⊕1！
    box_ekf = (150, y_bot - 58, 360, 116)
    draw_arrow(draw, (690, y_bot), (510, y_bot), width=3)
    draw_rich_text(draw, (530, y_bot - 58, 140, 52), "真实状态\nη(t), ν(t)", font_size=20, bold=True)
    draw_node_box(draw, box_ekf, "虚拟传感器与 EKF2 状态估计\nIMU / 深度计 / DVL 数据融合",
                  font_size=20, fill="#FFFFFF", border="#000000", width=2)

    # 跨层反馈回传通道：从 box_ekf 顶部 (330, 507) 垂直向上至 y = 295，再向右至 cx_err = 530 向上进 ⊕1，同时向右至 880 向上进控制器！
    x_fb_up = 330
    y_fb_turn = 295
    draw.line([(x_fb_up, y_bot - 58), (x_fb_up, y_fb_turn)], fill="#1F4E79", width=3)
    draw.line([(x_fb_up, y_fb_turn), (880, y_fb_turn)], fill="#1F4E79", width=3)
    draw.ellipse([cx_err - 5, y_fb_turn - 5, cx_err + 5, y_fb_turn + 5], fill="#1F4E79")
    draw_arrow(draw, (cx_err, y_fb_turn), (cx_err, y_top + 22), fill="#1F4E79", width=3)
    draw_arrow(draw, (880, y_fb_turn), (880, y_top + 58), fill="#1F4E79", width=3)

    draw_rich_text(draw, (x_fb_up + 14, 344, 290, 62),
                   "全状态反馈 {hat:η}, {hat:ν}\n(vehicle_odometry / attitude)",
                   font_size=18, fill="#1F4E79", bold=True, align="left")

    fp_png = os.path.join(OUT_DIR, "fig2_px4_rov_architecture.png")
    img.save(fp_png, dpi=(300, 300))
    print(f"[OK] 已生成图4 (PX4/SITL闭环结构框图, 300 DPI): {fp_png}")


def build_all_figures():
    print("=== 开始生成开题报告全套极简出版级学术配图 (300 DPI) ===")
    generate_fig1_lit_control_architecture()
    generate_fig0_rov_coord_thrusters()
    generate_fig1_technical_roadmap()
    generate_fig2_px4_rov_architecture()
    print("=== 全套 4 幅高清配图生成完毕 ===")


if __name__ == "__main__":
    build_all_figures()
