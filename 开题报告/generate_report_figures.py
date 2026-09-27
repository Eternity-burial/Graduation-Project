# -*- coding: utf-8 -*-
"""
生成《基于PX4的水下航行器模型控制方法研究》开题报告出版级高清配图 (300 DPI PNG + 可编辑 .drawio)
使用 Pillow + 富文本数学排版引擎（原生支持上下标、粗斜体变量、顶标点号/帽号，零乱码框）：
1. fig0_rov_coord_thrusters.png (.drawio): 图1 八推进器水下航行器坐标系定义与推力矢量空间布置示意图
2. fig1_technical_roadmap.png   (.drawio): 图2 课题总体研究技术路线图
3. fig2_px4_rov_architecture.png (.drawio): 图3 基于PX4/SITL的水下航行器闭环仿真系统结构框图
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


def draw_rich_line(draw, x, y, tokens, font_size, fill="#1A1A1A", bold=False):
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
            hy = y + bb[1] - 7  # 上移帽号，避免与字母顶部粘连
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
            r = max(2, int(font_size * 0.09))
            draw.ellipse([cx - r, dy - r, cx + r, dy + r], fill=fill)
            cur_x += w


def draw_rich_multiline(draw, xc, yc, text, font_size=23, fill="#1A1A1A", bold=False,
                        line_spacing=10, align="center"):
    lines = text.split("\n")
    parsed_lines = [parse_rich_line(line) for line in lines]
    metrics = [measure_rich_line(draw, toks, font_size, bold=bold) for toks in parsed_lines]
    max_w = max((m[0] for m in metrics), default=0)
    total_h = sum(m[1] for m in metrics) + max(0, len(lines) - 1) * line_spacing

    cur_y = yc - total_h / 2
    for toks, (lw, lh) in zip(parsed_lines, metrics):
        if align == "center":
            lx = xc - lw / 2
        elif align == "left":
            lx = xc - max_w / 2
        else:
            lx = xc + max_w / 2 - lw
        draw_rich_line(draw, lx, cur_y, toks, font_size, fill=fill, bold=bold)
        cur_y += lh + line_spacing


def draw_rounded_box(draw, xc, yc, w, h, text, fill="#F4F7FB", outline="#2B579A",
                     text_color="#1A1A1A", font_size=24, bold=False, radius=16,
                     border_width=3, line_spacing=10, align="center"):
    x0 = int(xc - w / 2)
    y0 = int(yc - h / 2)
    x1 = int(xc + w / 2)
    y1 = int(yc + h / 2)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill,
                           outline=outline, width=border_width)
    draw_rich_multiline(draw, xc, yc, text, font_size=font_size, fill=text_color,
                        bold=bold, line_spacing=line_spacing, align=align)


def draw_dashed_rect(draw, x0, y0, x1, y1, fill="#F8FAFC", outline="#8FAADC",
                     width=3, dash_len=14, gap_len=8):
    if fill:
        draw.rectangle([x0, y0, x1, y1], fill=fill, outline=None)
    edges = [
        ((x0, y0), (x1, y0)),
        ((x1, y0), (x1, y1)),
        ((x1, y1), (x0, y1)),
        ((x0, y1), (x0, y0)),
    ]
    for (sx, sy), (ex, ey) in edges:
        dist = math.hypot(ex - sx, ey - sy)
        if dist == 0:
            continue
        ux, uy = (ex - sx) / dist, (ey - sy) / dist
        pos = 0
        while pos < dist:
            seg_end = min(pos + dash_len, dist)
            p1 = (sx + ux * pos, sy + uy * pos)
            p2 = (sx + ux * seg_end, sy + uy * seg_end)
            draw.line([p1, p2], fill=outline, width=width)
            pos += dash_len + gap_len


def draw_dashed_line(draw, p1, p2, fill="#666666", width=3, dash_len=12, gap_len=8):
    sx, sy = p1
    ex, ey = p2
    dist = math.hypot(ex - sx, ey - sy)
    if dist == 0:
        return
    ux, uy = (ex - sx) / dist, (ey - sy) / dist
    pos = 0
    while pos < dist:
        seg_end = min(pos + dash_len, dist)
        q1 = (sx + ux * pos, sy + uy * pos)
        q2 = (sx + ux * seg_end, sy + uy * seg_end)
        draw.line([q1, q2], fill=fill, width=width)
        pos += dash_len + gap_len


def draw_label_pill(draw, mx, my, label, font_size=21, text_color="#222222", bold=False):
    lines = label.split("\n")
    parsed = [parse_rich_line(l) for l in lines]
    metrics = [measure_rich_line(draw, t, font_size, bold=bold) for t in parsed]
    tw = max((m[0] for m in metrics), default=0)
    th = sum(m[1] for m in metrics) + max(0, len(lines) - 1) * 6
    pad_x, pad_y = 8, 5
    draw.rounded_rectangle(
        [mx - tw / 2 - pad_x, my - th / 2 - pad_y, mx + tw / 2 + pad_x, my + th / 2 + pad_y],
        radius=6, fill="#FFFFFF", outline=None
    )
    draw_rich_multiline(draw, mx, my, label, font_size=font_size, fill=text_color, bold=bold, line_spacing=6)


def draw_arrow(draw, x1, y1, x2, y2, color="#2B579A", width=4, head_len=18, head_width=11,
               label=None, label_offset=(0, 0), font_size=21, bold_label=False):
    angle = math.atan2(y2 - y1, x2 - x1)
    lx2 = x2 - head_len * 0.7 * math.cos(angle)
    ly2 = y2 - head_len * 0.7 * math.sin(angle)
    draw.line([(x1, y1), (lx2, ly2)], fill=color, width=width)

    p_tip = (x2, y2)
    p_left = (
        x2 - head_len * math.cos(angle) + head_width * math.sin(angle),
        y2 - head_len * math.sin(angle) - head_width * math.cos(angle)
    )
    p_right = (
        x2 - head_len * math.cos(angle) - head_width * math.sin(angle),
        y2 - head_len * math.sin(angle) + head_width * math.cos(angle)
    )
    draw.polygon([p_tip, p_left, p_right], fill=color)

    if label:
        mx = (x1 + x2) / 2 + label_offset[0]
        my = (y1 + y2) / 2 + label_offset[1]
        draw_label_pill(draw, mx, my, label, font_size=font_size,
                        text_color=color if bold_label else "#222222", bold=bold_label)


def draw_polyline_arrow(draw, points, color="#2B579A", width=4, head_len=18, head_width=11,
                        label=None, label_pos=None, font_size=21):
    for i in range(len(points) - 2):
        draw.line([points[i], points[i + 1]], fill=color, width=width)
    x1, y1 = points[-2]
    x2, y2 = points[-1]
    draw_arrow(draw, x1, y1, x2, y2, color=color, width=width,
               head_len=head_len, head_width=head_width)
    if label and label_pos:
        draw_label_pill(draw, label_pos[0], label_pos[1], label, font_size=font_size, text_color="#222222")


def draw_rotation_arc(draw, cx, cy, rx, ry, start_deg, end_deg, color="#C55A11", width=3,
                      label=None, label_pos=None):
    bbox = [cx - rx, cy - ry, cx + rx, cy + ry]
    draw.arc(bbox, start=start_deg, end=end_deg, fill=color, width=width)
    rad = math.radians(end_deg)
    tx = cx + rx * math.cos(rad)
    ty = cy + ry * math.sin(rad)
    tan_angle = math.atan2(ry * math.cos(rad), -rx * math.sin(rad))
    head_len, head_w = 12, 7
    p_left = (
        tx - head_len * math.cos(tan_angle) + head_w * math.sin(tan_angle),
        ty - head_len * math.sin(tan_angle) - head_w * math.cos(tan_angle)
    )
    p_right = (
        tx - head_len * math.cos(tan_angle) - head_w * math.sin(tan_angle),
        ty - head_len * math.sin(tan_angle) + head_w * math.cos(tan_angle)
    )
    draw.polygon([(tx, ty), p_left, p_right], fill=color)
    if label and label_pos:
        draw_rich_multiline(draw, label_pos[0], label_pos[1], label, font_size=20, fill=color, bold=True)


def generate_fig0_rov_coord_thrusters():
    """
    图1：八推进器水下航行器坐标系定义与推力矢量空间布置示意图 (2400 x 1240 px @ 300 DPI)
    """
    W, H = 2400, 1240
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    # =========================================================================
    # 左子图 (a)：惯性坐标系 {n} 与附体坐标系 {b} 六自由度定义
    # =========================================================================
    draw.rounded_rectangle([35, 35, 1145, 1205], radius=20, fill="#FAFBFD", outline="#2F5597", width=3)
    draw_rich_multiline(
        draw, 590, 72,
        "(a) 惯性坐标系 {n} 与附体坐标系 {b} 六自由度运动定义",
        font_size=27, fill="#1F3864", bold=True
    )

    # 1. 北东地惯性系 {n} (O_n - x_n y_n z_n)
    on_x, on_y = 215, 735
    draw_arrow(draw, on_x, on_y, on_x + 170, on_y - 95, color="#1F4E79", width=5)
    draw_rich_multiline(draw, on_x + 280, on_y - 102, "x{sub:n} (北 North, x)", font_size=21, fill="#1F4E79", bold=True)

    draw_arrow(draw, on_x, on_y, on_x + 195, on_y + 35, color="#1F4E79", width=5)
    draw_rich_multiline(draw, on_x + 300, on_y + 36, "y{sub:n} (东 East, y)", font_size=21, fill="#1F4E79", bold=True)

    draw_arrow(draw, on_x, on_y, on_x, on_y + 185, color="#1F4E79", width=5)
    draw_rich_multiline(draw, on_x + 35, on_y + 212, "z{sub:n} (地 Down, 潜深 z)", font_size=21, fill="#1F4E79", bold=True)

    draw.ellipse([on_x - 7, on_y - 7, on_x + 7, on_y + 7], fill="#1F4E79")
    draw_rich_multiline(draw, on_x - 75, on_y - 15, "惯性系 {n}\n原点 O{sub:n}", font_size=21, fill="#1F4E79", bold=True)

    # 2. 附体系 {b} (O_b - x_b y_b z_b) 与 ROV 立体轮廓
    ob_x, ob_y = 685, 455
    draw_dashed_line(draw, (on_x, on_y), (ob_x - 15, ob_y + 15), fill="#548235", width=4)
    draw_arrow(draw, ob_x - 45, ob_y + 35, ob_x - 8, ob_y + 8, color="#548235", width=4)
    draw_rounded_box(
        draw, 420, 565, 290, 74,
        "广义位置与姿态矢量 η\nη = [x, y, z, φ, θ, ψ]{sup:T}",
        fill="#E2EFDA", outline="#548235", text_color="#274E13", font_size=19, bold=True, radius=10
    )

    hull_pts = [(ob_x - 130, ob_y - 55), (ob_x + 70, ob_y - 145), (ob_x + 210, ob_y - 95), (ob_x + 10, ob_y - 5)]
    hull_btm = [(x, y + 95) for (x, y) in hull_pts]
    draw.polygon(hull_btm, fill="#EDF2F8", outline="#8FAADC")
    for i in range(4):
        draw.line([hull_pts[i], hull_btm[i]], fill="#8FAADC", width=3)
    draw.polygon(hull_pts, fill="#D9E1F2", outline="#4472C4")

    cb_x, cb_y = ob_x, ob_y - 48
    draw.ellipse([cb_x - 7, cb_y - 7, cb_x + 7, cb_y + 7], fill="#0072B2", outline="white")
    draw_arrow(draw, cb_x, cb_y, cb_x, cb_y - 45, color="#0072B2", width=3, head_len=13, head_width=8)
    draw_rich_multiline(draw, cb_x - 95, cb_y - 25, "浮心 CB (浮力 B)", font_size=19, fill="#0072B2", bold=True)

    draw.ellipse([ob_x - 8, ob_y - 8, ob_x + 8, ob_y + 8], fill="#D55E00", outline="white")
    draw_rich_multiline(draw, ob_x - 115, ob_y + 32, "附体系 {b} 原点 O{sub:b}\n(重心 CG, 重力 W)", font_size=19, fill="#D55E00", bold=True)

    xb_end = (ob_x + 250, ob_y - 115)
    draw_arrow(draw, ob_x, ob_y, xb_end[0], xb_end[1], color="#C00000", width=5)
    draw_rich_multiline(draw, xb_end[0] + 5, xb_end[1] - 42, "x{sub:b} 轴 (前 Forward)\n纵荡速度 u, 横滚 (φ, p)",
                        font_size=20, fill="#C00000", bold=True)
    draw_rotation_arc(draw, ob_x + 165, ob_y - 76, 22, 34, -60, 150, color="#C00000", width=3,
                      label="p, φ", label_pos=(ob_x + 205, ob_y - 108))

    yb_end = (ob_x + 235, ob_y + 82)
    draw_arrow(draw, ob_x, ob_y, yb_end[0], yb_end[1], color="#274E13", width=5)
    draw_rich_multiline(draw, yb_end[0] + 25, yb_end[1] + 38, "y{sub:b} 轴 (右 Right)\n横荡速度 v, 俯仰 (θ, q)",
                        font_size=20, fill="#274E13", bold=True)
    draw_rotation_arc(draw, ob_x + 150, ob_y + 52, 22, 32, -40, 160, color="#274E13", width=3,
                      label="q, θ", label_pos=(ob_x + 195, ob_y + 32))

    zb_end = (ob_x, ob_y + 235)
    draw_arrow(draw, ob_x, ob_y, zb_end[0], zb_end[1], color="#1F4E79", width=5)
    draw_rich_multiline(draw, zb_end[0] + 135, zb_end[1] - 12, "z{sub:b} 轴 (下 Down)\n垂荡速度 w, 偏航 (ψ, r)",
                        font_size=20, fill="#1F4E79", bold=True)
    draw_rotation_arc(draw, ob_x, ob_y + 155, 36, 18, 0, 210, color="#1F4E79", width=3,
                      label="r, ψ", label_pos=(ob_x - 52, ob_y + 155))

    draw_rounded_box(
        draw, 590, 1090, 1050, 145,
        "六自由度运动学与动力学状态矢量约定（Fossen 标准框架 + PX4 机体 FRD 规范）：\n"
        "• 惯性系广义位置与姿态：η = [x, y, z, φ, θ, ψ]{sup:T} ∈ R{sup:6} ，运动学转换：{dot:η} = J(η)ν\n"
        "• 附体系速度矢量：ν = [u, v, w, p, q, r]{sup:T} ∈ R{sup:6} ；期望广义力与力矩：τ{sub:c} = [F{sub:x}, F{sub:y}, F{sub:z}, M{sub:x}, M{sub:y}, M{sub:z}]{sup:T} ∈ R{sup:6}",
        fill="#F2F5F9", outline="#4472C4", text_color="#1A1A1A", font_size=19, bold=False, radius=12, line_spacing=9
    )

    # =========================================================================
    # 右子图 (b)：八推进器空间对称与矢量倾斜布置示意图 (俯视投影)
    # =========================================================================
    draw.rounded_rectangle([1185, 35, 2365, 1205], radius=20, fill="#FAFBFD", outline="#2F5597", width=3)
    draw_rich_multiline(
        draw, 1775, 72,
        "(b) 八推进器空间对称与矢量倾斜布置示意图 (俯视投影)",
        font_size=27, fill="#1F3864", bold=True
    )

    cx, cy = 1775, 540
    frame_w, frame_h = 490, 580
    fx0, fy0 = cx - frame_w // 2, cy - frame_h // 2
    fx1, fy1 = cx + frame_w // 2, cy + frame_h // 2

    # ROV 开架外框与左右浮力梁、中央水密电子舱
    draw.rounded_rectangle([fx0, fy0, fx1, fy1], radius=28, fill="#F0F4FA", outline="#2F5597", width=4)
    draw.rounded_rectangle([fx0 + 18, fy0 + 35, fx0 + 68, fy1 - 35], radius=10, fill="#D9E1F2", outline="#4472C4", width=2)
    draw.rounded_rectangle([fx1 - 68, fy0 + 35, fx1 - 18, fy1 - 35], radius=10, fill="#D9E1F2", outline="#4472C4", width=2)
    draw.rounded_rectangle([cx - 84, cy - 160, cx + 84, cy + 160], radius=34, fill="#FFFFFF", outline="#2F5597", width=3)
    draw_rich_multiline(draw, cx, cy - 108, "水密电子舱\n(飞控与传感器)", font_size=19, fill="#1F3864", bold=True)

    # 坐标轴 x_b (向上为前), y_b (向右为右舷), O_b (z_b 垂直向下)
    draw_arrow(draw, cx, fy1 + 35, cx, fy0 - 65, color="#C00000", width=4)
    draw_rich_multiline(draw, cx + 112, fy0 - 62, "x{sub:b} (前 Forward, F{sub:x})", font_size=21, fill="#C00000", bold=True)

    draw_arrow(draw, fx0 - 65, cy, fx1 + 95, cy, color="#274E13", width=4)
    draw_rich_multiline(draw, fx1 + 100, cy + 30, "y{sub:b} (右 Right, F{sub:y})", font_size=21, fill="#274E13", bold=True)

    draw.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill="white", outline="#1F4E79", width=3)
    draw.line([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill="#1F4E79", width=3)
    draw.line([(cx - 8, cy + 8), (cx + 8, cy - 8)], fill="#1F4E79", width=3)
    draw_rich_multiline(draw, cx + 82, cy + 24, "O{sub:b} (z{sub:b} 垂直向下)", font_size=19, fill="#1F4E79", bold=True)

    # 1. 水平面 4 台矢量倾斜推进器 T_1 ~ T_4 (文字放置在框架外侧白底区域，绝不压线)
    horiz_thrusters = [
        ("T{sub:1}", cx + 158, cy - 205, -45, "右前水平 T{sub:1}", (168, 0)),
        ("T{sub:2}", cx - 158, cy - 205,  45, "左前水平 T{sub:2}", (-168, 0)),
        ("T{sub:3}", cx + 158, cy + 205,  45, "右后水平 T{sub:3}", (168, 0)),
        ("T{sub:4}", cx - 158, cy + 205, -45, "左后水平 T{sub:4}", (-168, 0)),
    ]

    for name, tx, ty, deg, desc, (lx_off, ly_off) in horiz_thrusters:
        if name == "T{sub:1}":
            draw_dashed_line(draw, (cx, cy), (tx, ty), fill="#BF9000", width=3)
            draw_label_pill(draw, cx + 98, cy - 110, "位置力臂 r{sub:i}", font_size=19, text_color="#996600", bold=True)
            # 标注倾角 α
            draw_dashed_line(draw, (tx, ty), (tx, ty - 82), fill="#666666", width=2)
            draw.arc([tx - 46, ty - 46, tx + 46, ty + 46], start=-135, end=-90, fill="#C00000", width=3)
            draw_rich_multiline(draw, tx - 17, ty - 62, "α", font_size=22, fill="#C00000", bold=True)

        draw.ellipse([tx - 26, ty - 26, tx + 26, ty + 26], fill="#FFE699", outline="#BF9000", width=3)
        draw_rich_multiline(draw, tx, ty, name, font_size=20, fill="#332600", bold=True)

        rad = math.radians(deg - 90)
        dx = int(76 * math.cos(rad))
        dy = int(76 * math.sin(rad))
        draw_arrow(draw, tx, ty, tx + dx, ty + dy, color="#D55E00", width=5, head_len=16, head_width=10)
        if name == "T{sub:1}":
            draw_label_pill(draw, tx + dx - 52, ty + dy - 18, "推力方向 d{sub:i}", font_size=18, text_color="#D55E00", bold=True)

        draw_label_pill(draw, tx + lx_off, ty + ly_off, desc, font_size=19, text_color="#222222", bold=True)

    # 2. 垂直面 4 台垂向对称推进器 T_5 ~ T_8 (文字放置在框架外侧白底区域，绝不压线)
    vert_thrusters = [
        ("T{sub:5}", cx + 142, cy - 82, "右前垂向 T{sub:5}", (182, 0)),
        ("T{sub:6}", cx - 142, cy - 82, "左前垂向 T{sub:6}", (-182, 0)),
        ("T{sub:7}", cx + 142, cy + 82, "右后垂向 T{sub:7}", (182, 0)),
        ("T{sub:8}", cx - 142, cy + 82, "左后垂向 T{sub:8}", (-182, 0)),
    ]
    for name, vx, vy, vdesc, (vx_off, vy_off) in vert_thrusters:
        draw.ellipse([vx - 24, vy - 24, vx + 24, vy + 24], fill="#D9E1F2", outline="#1F4E79", width=3)
        draw.ellipse([vx - 5, vy - 5, vx + 5, vy + 5], fill="#1F4E79")
        draw_rich_multiline(draw, vx, vy + 38, name, font_size=18, fill="#1F4E79", bold=True)
        draw_label_pill(draw, vx + vx_off, vy + vy_off, vdesc, font_size=19, text_color="#1F4E79", bold=True)

    # 右子图底部说明框
    draw_rounded_box(
        draw, 1775, 1090, 1110, 145,
        "八推进器过驱动冗余构型与 6 × 8 控制分配矩阵 B 映射机理：\n"
        "• 水平面矢量推进器 (T{sub:1} ~ T{sub:4}，倾角 α)：协同产生纵荡推力 F{sub:x}、横荡推力 F{sub:y} 与偏航力矩 M{sub:z}\n"
        "• 垂直面垂向推进器 (T{sub:5} ~ T{sub:8}，沿 z{sub:b} 轴)：协同产生垂荡推力 F{sub:z}、横滚力矩 M{sub:x} 与俯仰力矩 M{sub:y}；列矢量 b{sub:i} = [d{sub:i}{sup:T}, (r{sub:i} × d{sub:i}){sup:T}]{sup:T}",
        fill="#F2F5F9", outline="#4472C4", text_color="#1A1A1A", font_size=19, bold=False, radius=12, line_spacing=9
    )

    out_path = os.path.join(OUT_DIR, "fig0_rov_coord_thrusters.png")
    img.save(out_path, dpi=(300, 300))
    print("Saved:", out_path)


def generate_fig1_roadmap():
    """图2：课题总体研究技术路线图 (2400 x 1680 px @ 300 DPI)"""
    W, H = 2400, 1680
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    draw_rounded_box(draw, 235, 75, 340, 86, "研究阶段",
                     fill="#1F4E79", outline="#1F4E79", text_color="white",
                     font_size=30, bold=True, radius=14)
    draw_rounded_box(draw, 1205, 75, 1510, 86, "主要研究内容与技术实现路径",
                     fill="#1F4E79", outline="#1F4E79", text_color="white",
                     font_size=30, bold=True, radius=14)
    draw_rounded_box(draw, 2165, 75, 350, 86, "阶段预期成果",
                     fill="#1F4E79", outline="#1F4E79", text_color="white",
                     font_size=30, bold=True, radius=14)

    stages = [
        {
            "yc": 310, "h": 300,
            "stage": "第一阶段\n平台梳理与\n动力学建模",
            "left": "依托已有八推进器\n水下航行器平台\n梳理构型与参数资料",
            "mid1": "建立六自由度运动学与动力学模型\n（考虑刚体惯性 M{sub:RB}、附加质量 M{sub:A}、科氏力 C(ν)、\n水动力阻尼 D(ν) 与重浮力恢复项 g(η)）",
            "mid2": "推进器特性建模\n（建立单推进器特性模型\n与空间安装几何关系 r{sub:i}, d{sub:i}）",
            "out": "水下航行器 6-DOF\n理论模型与推进器模型"
        },
        {
            "yc": 685, "h": 300,
            "stage": "第二阶段\n系统辨识与\n模型验证",
            "left": "明确系统辨识\n激励输入、响应输出\n及所需相关数据",
            "mid1": "关键未知参数辨识与模型修正\n（结合平台参数资料和相关数据开展系统辨识，\n对未知水动力参数集 θ 进行估计与修正）",
            "mid2": "模型基本验证与误差分析\n（对比模型输出与代表性动态响应，\n分析模型偏差及适用范围）",
            "out": "经验证的标称动力学模型\n({hat:M}, {hat:C}, {hat:D}, {hat:g})"
        },
        {
            "yc": 1060, "h": 300,
            "stage": "第三阶段\n运动控制与\n八推进器分配",
            "left": "参考运动状态输入 η{sub:r}\n（姿态、深度、\n航向等控制目标）",
            "mid1": "基于模型与状态反馈的运动控制设计\n（结合标称模型补偿 F{sub:model} 与状态反馈 F{sub:fb}，\n计算期望广义控制力与力矩 τ{sub:c} ∈ R{sup:6}）",
            "mid2": "八推进器控制分配设计\n（建立 6 × 8 控制分配矩阵 B，\n考虑推力范围 T{sub:min} ≤ T ≤ T{sub:max}）",
            "out": "闭环运动控制方法与\n八推进器控制分配模型"
        },
        {
            "yc": 1435, "h": 300,
            "stage": "第四阶段\nPX4/SITL闭环\n仿真与系统验证",
            "left": "基于PX4架构与\nuORB实现模型、控制\n与分配闭环集成",
            "mid1": "代表性运动与外部扰动工况仿真\n（在PX4/SITL环境中开展姿态、深度、航向等\n典型运动工况及适量外部扰动 τ{sub:d} 仿真验证）",
            "mid2": "系统性能分析与论文总结\n（结合跟踪误差 e{sub:η}、动态响应及\n分配残差 e{sub:τ} = τ{sub:c} − BT 评价效果）",
            "out": "PX4/SITL闭环仿真系统\n与毕业论文成果"
        }
    ]

    for st in stages:
        yc, h = st["yc"], st["h"]
        draw_dashed_rect(draw, 45, yc - h // 2, 2355, yc + h // 2,
                         fill="#F8FAFC", outline="#8FAADC", width=3)

    for st in stages:
        yc, h = st["yc"], st["h"]
        bh = h - 48
        draw_rounded_box(draw, 235, yc, 330, bh, st["stage"],
                         fill="#D9E1F2", outline="#2F5597", text_color="#1F3864",
                         font_size=26, bold=True)
        draw_rounded_box(draw, 645, yc, 350, bh, st["left"],
                         fill="#FFFFFF", outline="#4472C4", text_color="#1A1A1A",
                         font_size=22, bold=False)
        draw_rounded_box(draw, 1155, yc, 535, bh, st["mid1"],
                         fill="#EDF2F8", outline="#2F5597", text_color="#102542",
                         font_size=21, bold=True)
        draw_rounded_box(draw, 1695, yc, 415, bh, st["mid2"],
                         fill="#FFFFFF", outline="#4472C4", text_color="#1A1A1A",
                         font_size=21, bold=False)
        draw_rounded_box(draw, 2160, yc, 360, bh, st["out"],
                         fill="#E2EFDA", outline="#548235", text_color="#274E13",
                         font_size=23, bold=True)

        draw_arrow(draw, 400, yc, 470, yc, color="#2F5597", width=4)
        draw_arrow(draw, 820, yc, 887, yc, color="#2F5597", width=4)
        draw_arrow(draw, 1423, yc, 1487, yc, color="#2F5597", width=4)
        draw_arrow(draw, 1903, yc, 1980, yc, color="#548235", width=4)

    for idx in range(len(stages) - 1):
        yc = stages[idx]["yc"]
        bh = stages[idx]["h"] - 48
        next_yc = stages[idx + 1]["yc"]
        next_bh = stages[idx + 1]["h"] - 48
        y_start = yc + bh // 2
        y_end = next_yc - next_bh // 2
        draw_arrow(draw, 235, y_start, 235, y_end, color="#1F4E79", width=5, head_len=20, head_width=12)
        draw_arrow(draw, 1155, y_start, 1155, y_end, color="#2F5597", width=5, head_len=20, head_width=12)
        draw_arrow(draw, 2160, y_start, 2160, y_end, color="#548235", width=5, head_len=20, head_width=12)

    out_path = os.path.join(OUT_DIR, "fig1_technical_roadmap.png")
    img.save(out_path, dpi=(300, 300))
    print("Saved:", out_path)


def generate_fig2_architecture():
    """图3：基于PX4/SITL的水下航行器闭环仿真系统结构框图 (2400 x 1320 px @ 300 DPI)"""
    W, H = 2400, 1320
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([40, 40, 2360, 1280], radius=24,
                           fill="#FAFBFD", outline="#2F5597", width=4)
    draw_rich_multiline(
        draw, W // 2, 86,
        "PX4 / SITL 水下航行器闭环仿真系统结构框图（通过 uORB 总线实现模块间数据交互）",
        font_size=31, fill="#1F3864", bold=True
    )

    draw_rounded_box(
        draw, 955, 265, 860, 190,
        "平台参数资料与相关数据支撑：系统辨识与模型验证模块\n"
        "（明确激励输入与响应输出关系，辨识未知参数集 θ 并输出标称模型 {hat:M}, {hat:C}, {hat:D}, {hat:g}）",
        fill="#FFF2CC", outline="#BF9000", text_color="#332600",
        font_size=21, bold=True
    )

    draw_rounded_box(
        draw, 1960, 265, 620, 190,
        "代表性工况与外部扰动条件设置\n（姿态、深度、航向等典型运动任务\n及外部水流扰动输入 τ{sub:d}）",
        fill="#FCE4D6", outline="#C65911", text_color="#331500",
        font_size=21, bold=True
    )

    yc = 660
    bh = 255
    draw_rounded_box(
        draw, 230, yc, 285, bh,
        "参考运动状态\n(η{sub:r}, ν{sub:r})\n\n姿态 / 深度 /\n航向参考指令",
        fill="#E2EFDA", outline="#548235", text_color="#1E3F0F",
        font_size=23, bold=True
    )

    draw_rounded_box(
        draw, 755, yc, 465, bh,
        "水下航行器闭环运动控制模块\n\n标称模型特性补偿 F{sub:model}({hat:M}, {hat:C}, {hat:D}, {hat:g})\n+ 实时状态误差反馈 F{sub:fb}(e{sub:η}, e{sub:ν})\n计算期望广义力与力矩 τ{sub:c} ∈ R{sup:6}",
        fill="#D9E1F2", outline="#2F5597", text_color="#102542",
        font_size=21, bold=True
    )

    draw_rounded_box(
        draw, 1415, yc, 450, bh,
        "八推进器控制分配模块\n\n基于推进器位置 r{sub:i} 与方向 d{sub:i}\n构建 6 × 8 控制分配矩阵 B\n考虑推力范围 [T{sub:min}, T{sub:max}] 求解",
        fill="#D9E1F2", outline="#2F5597", text_color="#102542",
        font_size=21, bold=True
    )

    draw_rounded_box(
        draw, 2048, yc, 455, bh,
        "水下航行器与推进器动力学模型\n\n单推进器特性模型 + 6-DOF 方程：\nM{dot:ν} + C(ν)ν + D(ν)ν + g(η) = τ + τ{sub:d}\n运动学转换：{dot:η} = J(η)ν",
        fill="#EDEDED", outline="#595959", text_color="#1A1A1A",
        font_size=21, bold=True
    )

    draw_rounded_box(
        draw, 1250, 1090, 1340, 160,
        "uORB 状态信息反馈与闭环系统性能分析模块\n"
        "（实时发布/订阅位置与姿态 η、速度 ν；综合跟踪误差 e{sub:η}、动态响应与分配残差 e{sub:τ} = τ{sub:c} − BT 评价闭环性能）",
        fill="#E8EEF5", outline="#4472C4", text_color="#1F3864",
        font_size=21, bold=True
    )

    draw_arrow(draw, 373, yc, 522, yc, color="#2F5597", width=5,
               label="参考状态\n(η{sub:r}, ν{sub:r})", label_offset=(0, -48), font_size=20)
    draw_arrow(draw, 988, yc, 1190, yc, color="#2F5597", width=5,
               label="期望广义力矩\nτ{sub:c} ∈ R{sup:6}", label_offset=(0, -50), font_size=20)
    draw_arrow(draw, 1640, yc, 1820, yc, color="#2F5597", width=5,
               label="八推进器指令\nT ∈ R{sup:8}", label_offset=(0, -50), font_size=20)

    draw_polyline_arrow(
        draw, [(755, 360), (755, 532)],
        color="#BF9000", width=4,
        label="提供经验证的标称模型 ({hat:M}, {hat:C}, {hat:D}, {hat:g})", label_pos=(755, 445), font_size=20
    )
    draw_polyline_arrow(
        draw, [(1245, 360), (1245, 445), (1920, 445), (1920, 532)],
        color="#BF9000", width=4,
        label="辨识修正水动力参数 θ", label_pos=(1580, 445), font_size=20
    )

    draw_arrow(draw, 2100, 360, 2100, 532, color="#C65911", width=4,
               label="外部扰动 τ{sub:d}", label_offset=(88, 0), font_size=20)

    draw_polyline_arrow(
        draw, [(2048, 788), (2048, 1090), (1920, 1090)],
        color="#4472C4", width=5,
        label="实时运动状态 (η, ν)", label_pos=(2048, 935), font_size=20
    )
    draw_polyline_arrow(
        draw, [(580, 1090), (465, 1090), (465, 720), (522, 720)],
        color="#4472C4", width=5,
        label="uORB 状态反馈 (η, ν)", label_pos=(465, 920), font_size=20
    )

    out_path = os.path.join(OUT_DIR, "fig2_px4_rov_architecture.png")
    img.save(out_path, dpi=(300, 300))
    print("Saved:", out_path)


def generate_drawio_files():
    """同步生成三张图的原生可编辑 .drawio (mxGraphModel XML) 矢量文件"""
    # 1. fig1_technical_roadmap.drawio
    roadmap_xml = """<mxfile host="Electron" modified="2026-09-27T22:45:00.000Z" agent="Antigravity" version="24.0.0">
  <diagram id="roadmap" name="课题总体研究技术路线图">
    <mxGraphModel dx="1422" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="1120" math="1" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="h1" value="研究阶段" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1F4E79;strokeColor=#1F4E79;fontColor=#FFFFFF;fontSize=16;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="45" y="25" width="220" height="50" as="geometry" /></mxCell>
        <mxCell id="h2" value="主要研究内容与技术实现路径" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1F4E79;strokeColor=#1F4E79;fontColor=#FFFFFF;fontSize=16;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="290" y="25" width="980" height="50" as="geometry" /></mxCell>
        <mxCell id="h3" value="阶段预期成果" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1F4E79;strokeColor=#1F4E79;fontColor=#FFFFFF;fontSize=16;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="1295" y="25" width="240" height="50" as="geometry" /></mxCell>
        <mxCell id="s1" value="第一阶段&lt;br&gt;平台梳理与动力学建模" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D9E1F2;strokeColor=#2F5597;fontColor=#1F3864;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="45" y="105" width="220" height="160" as="geometry" /></mxCell>
        <mxCell id="s1_1" value="依托已有八推进器&lt;br&gt;水下航行器平台&lt;br&gt;梳理构型与参数资料" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4472C4;fontSize=13;" vertex="1" parent="1"><mxGeometry x="295" y="105" width="230" height="160" as="geometry" /></mxCell>
        <mxCell id="s1_2" value="建立六自由度运动学与动力学模型&lt;br&gt;（考虑刚体惯性 M_RB、附加质量 M_A、科氏力 C(ν)、&lt;br&gt;水动力阻尼 D(ν) 与重浮力恢复项 g(η)）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EDF2F8;strokeColor=#2F5597;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="565" y="105" width="360" height="160" as="geometry" /></mxCell>
        <mxCell id="s1_3" value="推进器特性建模&lt;br&gt;（建立单推进器特性模型与&lt;br&gt;空间安装几何关系 r_i, d_i）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4472C4;fontSize=13;" vertex="1" parent="1"><mxGeometry x="965" y="105" width="290" height="160" as="geometry" /></mxCell>
        <mxCell id="s1_out" value="水下航行器 6-DOF&lt;br&gt;理论模型与推进器模型" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2EFDA;strokeColor=#548235;fontColor=#274E13;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="1295" y="105" width="240" height="160" as="geometry" /></mxCell>
        <mxCell id="s2" value="第二阶段&lt;br&gt;系统辨识与模型验证" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D9E1F2;strokeColor=#2F5597;fontColor=#1F3864;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="45" y="315" width="220" height="160" as="geometry" /></mxCell>
        <mxCell id="s2_1" value="明确系统辨识&lt;br&gt;激励输入、响应输出&lt;br&gt;及所需相关数据" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4472C4;fontSize=13;" vertex="1" parent="1"><mxGeometry x="295" y="315" width="230" height="160" as="geometry" /></mxCell>
        <mxCell id="s2_2" value="关键未知参数辨识与模型修正&lt;br&gt;（结合平台参数资料和相关数据开展系统辨识，&lt;br&gt;对未知水动力参数集 θ 进行估计与修正）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EDF2F8;strokeColor=#2F5597;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="565" y="315" width="360" height="160" as="geometry" /></mxCell>
        <mxCell id="s2_3" value="模型基本验证与误差分析&lt;br&gt;（对比模型输出与代表性动态响应，&lt;br&gt;分析模型偏差及适用范围）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4472C4;fontSize=13;" vertex="1" parent="1"><mxGeometry x="965" y="315" width="290" height="160" as="geometry" /></mxCell>
        <mxCell id="s2_out" value="经验证的标称动力学模型&lt;br&gt;(M̂, Ĉ, D̂, ĝ)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2EFDA;strokeColor=#548235;fontColor=#274E13;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="1295" y="315" width="240" height="160" as="geometry" /></mxCell>
        <mxCell id="s3" value="第三阶段&lt;br&gt;运动控制与八推进器分配" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D9E1F2;strokeColor=#2F5597;fontColor=#1F3864;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="45" y="525" width="220" height="160" as="geometry" /></mxCell>
        <mxCell id="s3_1" value="参考运动状态输入 η_r&lt;br&gt;（姿态、深度、航向等控制目标）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4472C4;fontSize=13;" vertex="1" parent="1"><mxGeometry x="295" y="525" width="230" height="160" as="geometry" /></mxCell>
        <mxCell id="s3_2" value="基于模型与状态反馈的运动控制设计&lt;br&gt;（结合标称模型补偿 F_model 与状态反馈 F_fb，&lt;br&gt;计算期望广义控制力与力矩 τ_c ∈ R^6）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EDF2F8;strokeColor=#2F5597;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="565" y="525" width="360" height="160" as="geometry" /></mxCell>
        <mxCell id="s3_3" value="八推进器控制分配设计&lt;br&gt;（建立 6×8 控制分配矩阵 B，&lt;br&gt;考虑推力范围 T_min ≤ T ≤ T_max）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4472C4;fontSize=13;" vertex="1" parent="1"><mxGeometry x="965" y="525" width="290" height="160" as="geometry" /></mxCell>
        <mxCell id="s3_out" value="闭环运动控制方法与&lt;br&gt;八推进器控制分配模型" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2EFDA;strokeColor=#548235;fontColor=#274E13;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="1295" y="525" width="240" height="160" as="geometry" /></mxCell>
        <mxCell id="s4" value="第四阶段&lt;br&gt;PX4/SITL闭环仿真与验证" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D9E1F2;strokeColor=#2F5597;fontColor=#1F3864;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="45" y="735" width="220" height="160" as="geometry" /></mxCell>
        <mxCell id="s4_1" value="基于PX4架构与uORB实现&lt;br&gt;模型、控制与分配闭环集成" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4472C4;fontSize=13;" vertex="1" parent="1"><mxGeometry x="295" y="735" width="230" height="160" as="geometry" /></mxCell>
        <mxCell id="s4_2" value="代表性运动与外部扰动工况仿真&lt;br&gt;（在PX4/SITL环境中开展姿态、深度、航向等&lt;br&gt;典型运动工况及适量外部扰动 τ_d 仿真验证）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EDF2F8;strokeColor=#2F5597;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="565" y="735" width="360" height="160" as="geometry" /></mxCell>
        <mxCell id="s4_3" value="系统性能分析与论文总结&lt;br&gt;（结合跟踪误差 e_η、动态响应及&lt;br&gt;分配残差 e_τ = τ_c - BT 评价效果）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4472C4;fontSize=13;" vertex="1" parent="1"><mxGeometry x="965" y="735" width="290" height="160" as="geometry" /></mxCell>
        <mxCell id="s4_out" value="PX4/SITL闭环仿真系统&lt;br&gt;与毕业论文成果" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2EFDA;strokeColor=#548235;fontColor=#274E13;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="1295" y="735" width="240" height="160" as="geometry" /></mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    with open(os.path.join(OUT_DIR, "fig1_technical_roadmap.drawio"), "w", encoding="utf-8") as f:
        f.write(roadmap_xml)

    # 2. fig2_px4_rov_architecture.drawio
    arch_xml = """<mxfile host="Electron" modified="2026-09-27T22:45:00.000Z" agent="Antigravity" version="24.0.0">
  <diagram id="px4_arch" name="PX4_SITL闭环仿真系统结构框图">
    <mxGraphModel dx="1422" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="900" math="1" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="id_box" value="平台参数资料与相关数据支撑：系统辨识与模型验证模块&lt;br&gt;（明确激励输入与响应输出关系，辨识未知参数集 θ 并输出标称模型 M̂, Ĉ, D̂, ĝ）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#BF9000;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="340" y="90" width="580" height="120" as="geometry" /></mxCell>
        <mxCell id="dist_box" value="代表性工况与外部扰动条件设置&lt;br&gt;（姿态、深度、航向等典型运动任务及外部水流扰动输入 τ_d）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4D6;strokeColor=#C65911;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="1080" y="90" width="420" height="120" as="geometry" /></mxCell>
        <mxCell id="ref_box" value="参考运动状态 (η_r, ν_r)&lt;br&gt;姿态 / 深度 / 航向参考指令" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2EFDA;strokeColor=#548235;fontSize=14;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="60" y="340" width="200" height="160" as="geometry" /></mxCell>
        <mxCell id="ctrl_box" value="水下航行器闭环运动控制模块&lt;br&gt;&lt;br&gt;标称模型特性补偿 F_model(M̂, Ĉ, D̂, ĝ)&lt;br&gt;+ 实时状态误差反馈 F_fb(e_η, e_ν)&lt;br&gt;计算期望广义力与力矩 τ_c ∈ R^6" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D9E1F2;strokeColor=#2F5597;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="360" y="340" width="320" height="160" as="geometry" /></mxCell>
        <mxCell id="alloc_box" value="八推进器控制分配模块&lt;br&gt;&lt;br&gt;基于推进器位置 r_i 与方向 d_i&lt;br&gt;构建 6 × 8 控制分配矩阵 B&lt;br&gt;考虑推力范围 [T_min, T_max] 求解" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D9E1F2;strokeColor=#2F5597;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="780" y="340" width="310" height="160" as="geometry" /></mxCell>
        <mxCell id="plant_box" value="水下航行器与推进器动力学模型&lt;br&gt;&lt;br&gt;单推进器特性模型 + 6-DOF 方程：&lt;br&gt;Mν̇ + C(ν)ν + D(ν)ν + g(η) = τ + τ_d&lt;br&gt;运动学转换：η̇ = J(η)ν" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EDEDED;strokeColor=#595959;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="1190" y="340" width="320" height="160" as="geometry" /></mxCell>
        <mxCell id="uorb_box" value="uORB 状态信息反馈与闭环系统性能分析模块&lt;br&gt;（实时发布/订阅位置与姿态 η、速度 ν；综合跟踪误差 e_η、动态响应与分配残差 e_τ = τ_c - BT 评价闭环性能）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8EEF5;strokeColor=#4472C4;fontSize=13;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="400" y="640" width="880" height="105" as="geometry" /></mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    with open(os.path.join(OUT_DIR, "fig2_px4_rov_architecture.drawio"), "w", encoding="utf-8") as f:
        f.write(arch_xml)

    # 3. fig0_rov_coord_thrusters.drawio
    coord_xml = """<mxfile host="Electron" modified="2026-09-27T22:45:00.000Z" agent="Antigravity" version="24.0.0">
  <diagram id="rov_coord" name="八推进器水下航行器坐标系与推力矢量布置示意图">
    <mxGraphModel dx="1422" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="840" math="1" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="pa" value="(a) 惯性坐标系 {n} 与附体坐标系 {b} 六自由度运动定义" style="rounded=1;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#FAFBFD;strokeColor=#2F5597;fontSize=15;fontStyle=1;spacingTop=10;" vertex="1" parent="1"><mxGeometry x="30" y="25" width="740" height="780" as="geometry" /></mxCell>
        <mxCell id="pb" value="(b) 八推进器空间对称与矢量倾斜布置示意图 (俯视投影)" style="rounded=1;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#FAFBFD;strokeColor=#2F5597;fontSize=15;fontStyle=1;spacingTop=10;" vertex="1" parent="1"><mxGeometry x="800" y="25" width="770" height="780" as="geometry" /></mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    with open(os.path.join(OUT_DIR, "fig0_rov_coord_thrusters.drawio"), "w", encoding="utf-8") as f:
        f.write(coord_xml)
    print("Saved editable .drawio files in:", OUT_DIR)


if __name__ == "__main__":
    generate_fig0_rov_coord_thrusters()
    generate_fig1_roadmap()
    generate_fig2_architecture()
    generate_drawio_files()
