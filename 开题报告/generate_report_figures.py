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
# 1. 图 1：实验室八推进器便携式水下航行器实验平台实物图 ((a) 整体斜视图 + (b) 俯视图)
# ==============================================================================

def crop_center_ratio(img, target_w, target_h, focus_x=0.5, focus_y=0.5, zoom=0.82):
    """按目标宽高比居中裁剪实物照片并缩放至指定像素尺寸"""
    src_w, src_h = img.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        crop_h = int(src_h * zoom)
        crop_w = int(crop_h * target_ratio)
    else:
        crop_w = int(src_w * zoom)
        crop_h = int(crop_w / target_ratio)

    cx = int(src_w * focus_x)
    cy = int(src_h * focus_y)
    x1 = max(0, min(src_w - crop_w, cx - crop_w // 2))
    y1 = max(0, min(src_h - crop_h, cy - crop_h // 2))
    cropped = img.crop((x1, y1, x1 + crop_w, y1 + crop_h))
    return cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)


def generate_fig1_rov_platform_photo():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_dir = os.path.join(project_root, "图片")
    fp_iso = os.path.join(img_dir, "5e115d95cae30e1fe648bb174d68bd60.jpg")
    fp_top = os.path.join(img_dir, "6c46c6d7ec6a1075a9e6c6d4505c33b2.jpg")

    w, h = 1800, 680
    canvas = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(canvas)

    sub_w, sub_h = 850, 580
    y_top = 16
    x_left = 25
    x_right = 925

    img_iso = Image.open(fp_iso).convert("RGB")
    img_top = Image.open(fp_top).convert("RGB")

    # 保持完整航行器主体（不裁切边角推进器）
    sub_iso = crop_center_ratio(img_iso, sub_w, sub_h, focus_x=0.50, focus_y=0.48, zoom=0.96)
    sub_top = crop_center_ratio(img_top, sub_w, sub_h, focus_x=0.50, focus_y=0.48, zoom=0.96)

    canvas.paste(sub_iso, (x_left, y_top))
    canvas.paste(sub_top, (x_right, y_top))

    # 细边框装饰
    draw.rectangle([x_left, y_top, x_left + sub_w, y_top + sub_h], outline="#CCCCCC", width=2)
    draw.rectangle([x_right, y_top, x_right + sub_w, y_top + sub_h], outline="#CCCCCC", width=2)

    # 子图题注
    draw_rich_text(
        draw,
        (x_left, y_top + sub_h + 14, sub_w, 48),
        "(a) 航行器整体结构斜视图",
        font_size=24,
        fill="#000000",
        bold=False,
    )
    draw_rich_text(
        draw,
        (x_right, y_top + sub_h + 14, sub_w, 48),
        "(b) 双耐压舱与八推进器空间布置俯视图",
        font_size=24,
        fill="#000000",
        bold=False,
    )

    fp_out = os.path.join(OUT_DIR, "fig1_rov_platform_photo.png")
    canvas.save(fp_out, dpi=(300, 300))
    print(f"[OK] 已生成图1 (实验室八推进器水下航行器实物图, 300 DPI): {fp_out}")


# ==============================================================================
# 2. 图 2：课题总体研究技术路线图 (严格对齐任务书四大模块，零旧词遗留)
# ==============================================================================

def generate_fig2_technical_roadmap():
    w, h = 1640, 960
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    stages = [
        (
            "模块一：水下航行器动力学建模与系统辨识",
            [
                "三维结构与先验参数确定\n(刚体惯性 M{sub:RB}、重浮心与推进器静态映射)",
                "六自由度方程与水动力简化\n(惯性系/附体系建立，M{sub:A} 与 D 对角化)",
                "特征工况辨识与模型验证\n(阶跃/自由衰减响应，最小二乘拟合与验证)",
            ],
        ),
        (
            "模块二：水下航行器运动控制方法研究",
            [
                "姿态/深度/航向状态反馈\n(位置姿态误差 e{sub:η} 与速度误差 e{sub:ν})",
                "辨识模型动态特性补偿\n(抵消重浮力恢复项、水动力阻尼或动态逆)",
                "闭环控制律设计与基准对比\n(输出期望广义力 τ{sub:c}，对比传统无模型 PID)",
            ],
        ),
        (
            "模块三：八推进器控制分配",
            [
                "八推进器空间几何关系梳理\n(水平4台矢量倾斜 + 垂直4台垂向对称)",
                "6×8 控制分配矩阵构造\n(由位置 r{sub:i} 与方向 d{sub:i} 构造 B ∈ R{sup:6×8})",
                "推力范围约束分配与误差分析\n(引入 [T{sub:min}, T{sub:max}] 约束，对比硬截断残差 e{sub:τ})",
            ],
        ),
        (
            "模块四：PX4/SITL 闭环仿真与系统验证",
            [
                "PX4/SITL 闭环系统构建\n(基于 uORB 总线集成模型、控制与分配模块)",
                "典型运动工况闭环仿真\n(空间定点悬停、姿态稳定、定深与定航控制)",
                "外部流扰测试与量化评价\n(抗流扰测试，量化跟踪误差 e{sub:η} 与残差 e{sub:τ})",
            ],
        ),
    ]

    margin_x = 40
    stage_w = w - 2 * margin_x
    stage_h = 188
    gap_y = 46
    start_y = 24

    for s_idx, (s_title, nodes) in enumerate(stages):
        sy = start_y + s_idx * (stage_h + gap_y)

        # 模块外框
        draw.rounded_rectangle([margin_x, sy, margin_x + stage_w, sy + stage_h],
                               radius=8, fill="#F8FAFC", outline="#1F4E79", width=2)
        # 顶部模块标题栏
        draw.rounded_rectangle([margin_x, sy, margin_x + stage_w, sy + 46],
                               radius=8, fill="#E8EEF5", outline="#1F4E79", width=2)
        draw_rich_text(draw, (margin_x + 22, sy + 5, stage_w - 44, 36), s_title,
                       font_size=23, fill="#1F4E79", bold=True, align="left")

        # 内部 3 个横向步骤节点
        node_w = 445
        node_h = 104
        node_gap = 55
        total_nodes_w = 3 * node_w + 2 * node_gap
        nx_start = margin_x + (stage_w - total_nodes_w) // 2
        ny = sy + 64

        for n_idx, n_text in enumerate(nodes):
            nx = nx_start + n_idx * (node_w + node_gap)
            draw_node_box(draw, (nx, ny, node_w, node_h), n_text,
                          font_size=21, fill="#FFFFFF", border="#000000", width=2, radius=6)
            if n_idx < 2:
                ax1 = nx + node_w
                ax2 = nx + node_w + node_gap
                ay = ny + node_h // 2
                draw_arrow(draw, (ax1, ay), (ax2, ay), fill="#1F4E79", width=3, arrow_len=14, arrow_w=7)

        # 模块间向下主流程箭头
        if s_idx < len(stages) - 1:
            mid_x = w // 2
            ay1 = sy + stage_h
            ay2 = ay1 + gap_y
            draw_arrow(draw, (mid_x, ay1), (mid_x, ay2), fill="#000000", width=4, arrow_len=16, arrow_w=9)

    fp_png = os.path.join(OUT_DIR, "fig2_technical_roadmap.png")
    img.save(fp_png, dpi=(300, 300))
    print(f"[OK] 已生成图2 (四大模块技术路线图, 300 DPI): {fp_png}")


def build_all_figures():
    print("=== 开始生成开题报告精简版学术配图 (共 2 幅, 300 DPI) ===")
    generate_fig1_rov_platform_photo()
    generate_fig2_technical_roadmap()
    print("=== 全部 2 幅高清配图生成完毕 ===")


if __name__ == "__main__":
    build_all_figures()

