# -*- coding: utf-8 -*-
"""
生成《基于PX4的水下航行器模型控制方法研究》开题报告高清配图 (300 DPI)
使用 Pillow + 系统 TrueType 字体绘制出版级流程图：
1. fig1_technical_roadmap.png: 课题总体技术路线图
2. fig2_px4_rov_architecture.png: 基于PX4/SITL的水下航行器闭环仿真系统结构框图
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT_DIR, exist_ok=True)


def get_font(size, bold=False):
    font_candidates = (
        ["C:/Windows/Fonts/msyhbd.ttc", "C:/Windows/Fonts/simhei.ttf", "C:/Windows/Fonts/msyh.ttc"]
        if bold else
        ["C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simsun.ttc", "C:/Windows/Fonts/simhei.ttf"]
    )
    for fp in font_candidates:
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()


def draw_rounded_box(draw, xc, yc, w, h, text, fill="#F4F7FB", outline="#2B579A",
                     text_color="#1A1A1A", font_size=26, bold=False, radius=18,
                     border_width=3, line_spacing=12):
    x0 = int(xc - w / 2)
    y0 = int(yc - h / 2)
    x1 = int(xc + w / 2)
    y1 = int(yc + h / 2)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill,
                           outline=outline, width=border_width)

    font = get_font(font_size, bold=bold)
    bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=line_spacing, align="center")
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = xc - tw / 2 - bbox[0]
    ty = yc - th / 2 - bbox[1]
    draw.multiline_text((tx, ty), text, font=font, fill=text_color,
                        spacing=line_spacing, align="center")


def draw_dashed_rect(draw, x0, y0, x1, y1, fill="#F8FAFC", outline="#8FAADC",
                     width=2, dash_len=14, gap_len=8):
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


def draw_arrow(draw, x1, y1, x2, y2, color="#2B579A", width=4, head_len=18, head_width=11,
               label=None, label_offset=(0, 0), font_size=23):
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
        font = get_font(font_size, bold=False)
        mx = (x1 + x2) / 2 + label_offset[0]
        my = (y1 + y2) / 2 + label_offset[1]
        bbox = draw.multiline_textbbox((0, 0), label, font=font, spacing=6, align="center")
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        pad = 6
        draw.rounded_rectangle(
            [mx - tw / 2 - pad, my - th / 2 - pad, mx + tw / 2 + pad, my + th / 2 + pad],
            radius=6, fill="#FFFFFF", outline=None
        )
        draw.multiline_text(
            (mx - tw / 2 - bbox[0], my - th / 2 - bbox[1]),
            label, font=font, fill="#222222", spacing=6, align="center"
        )


def draw_polyline_arrow(draw, points, color="#2B579A", width=4, head_len=18, head_width=11,
                        label=None, label_pos=None, font_size=23):
    for i in range(len(points) - 2):
        draw.line([points[i], points[i + 1]], fill=color, width=width)
    x1, y1 = points[-2]
    x2, y2 = points[-1]
    draw_arrow(draw, x1, y1, x2, y2, color=color, width=width,
               head_len=head_len, head_width=head_width)
    if label and label_pos:
        font = get_font(font_size, bold=False)
        mx, my = label_pos
        bbox = draw.multiline_textbbox((0, 0), label, font=font, spacing=6, align="center")
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        pad = 6
        draw.rounded_rectangle(
            [mx - tw / 2 - pad, my - th / 2 - pad, mx + tw / 2 + pad, my + th / 2 + pad],
            radius=6, fill="#FFFFFF", outline=None
        )
        draw.multiline_text(
            (mx - tw / 2 - bbox[0], my - th / 2 - bbox[1]),
            label, font=font, fill="#222222", spacing=6, align="center"
        )


def generate_fig1_roadmap():
    """图1：课题总体技术路线图 (2400 x 1680 px @ 300 DPI)"""
    W, H = 2400, 1680
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    # 顶部表头
    draw_rounded_box(draw, 235, 75, 340, 86, "研究阶段",
                     fill="#1F4E79", outline="#1F4E79", text_color="white",
                     font_size=31, bold=True, radius=14)
    draw_rounded_box(draw, 1205, 75, 1510, 86, "主要研究内容与技术实现路径",
                     fill="#1F4E79", outline="#1F4E79", text_color="white",
                     font_size=31, bold=True, radius=14)
    draw_rounded_box(draw, 2175, 75, 350, 86, "阶段预期成果",
                     fill="#1F4E79", outline="#1F4E79", text_color="white",
                     font_size=31, bold=True, radius=14)

    stages = [
        {
            "yc": 310, "h": 300,
            "stage": "第一阶段\n平台梳理与\n动力学建模",
            "left": "依托已有八推进器\n水下航行器平台\n梳理构型与参数资料",
            "mid1": "建立六自由度运动学与动力学模型\n（考虑刚体惯性、附加质量、科氏力与向心力、\n水动力阻尼、重力与浮力恢复作用等因素）",
            "mid2": "推进器特性建模\n（建立单推进器或执行机构\n必要模型与安装几何关系）",
            "out": "水下航行器6-DOF\n理论模型与推进器模型"
        },
        {
            "yc": 685, "h": 300,
            "stage": "第二阶段\n系统辨识与\n模型验证",
            "left": "明确系统辨识\n输入、输出关系\n及所需相关数据",
            "mid1": "关键未知参数辨识与模型修正\n（结合平台参数资料和相关数据开展系统辨识，\n对影响主要动态特性的未知量进行辨识修正）",
            "mid2": "模型基本验证与误差分析\n（对比模型输出与代表性响应，\n分析模型偏差及适用范围）",
            "out": "经验证的航行器\n控制与仿真基准模型"
        },
        {
            "yc": 1060, "h": 300,
            "stage": "第三阶段\n运动控制与\n八推进器分配",
            "left": "参考运动状态输入\n（姿态、深度、\n航向等控制目标）",
            "mid1": "基于模型与状态反馈的运动控制设计\n（结合经验证的航行器模型特性与状态误差反馈，\n计算航行器所需的期望广义力和力矩）",
            "mid2": "八推进器控制分配设计\n（建立八推进器控制分配矩阵，\n考虑基本推力范围生成指令）",
            "out": "闭环运动控制方法\n与八推进器分配模型"
        },
        {
            "yc": 1435, "h": 300,
            "stage": "第四阶段\nPX4/SITL闭环\n仿真与系统验证",
            "left": "基于PX4架构与\nuORB实现模型、控制\n与分配闭环集成",
            "mid1": "代表性运动与外部扰动工况仿真\n（在PX4/SITL环境中开展姿态、深度、航向等\n代表性运动工况及适量外部扰动条件仿真验证）",
            "mid2": "系统性能分析与论文总结\n（结合跟踪误差、动态响应及\n分配误差等指标评估闭环效果）",
            "out": "PX4/SITL闭环系统\n与毕业论文成果"
        }
    ]

    # Step 1: 先绘制所有阶段的虚线底框，防止遮挡跨阶段箭头
    for st in stages:
        yc, h = st["yc"], st["h"]
        draw_dashed_rect(draw, 45, yc - h // 2, 2355, yc + h // 2,
                         fill="#F8FAFC", outline="#8FAADC", width=3)

    # Step 2: 绘制各阶段内部模块框与横向箭头
    for st in stages:
        yc, h = st["yc"], st["h"]
        bh = h - 48
        # 阶段标题 (xc=235, w=330 -> [70, 400])
        draw_rounded_box(draw, 235, yc, 330, bh, st["stage"],
                         fill="#D9E1F2", outline="#2F5597", text_color="#1F3864",
                         font_size=27, bold=True)
        # 左模块 (xc=645, w=350 -> [470, 820])
        draw_rounded_box(draw, 645, yc, 350, bh, st["left"],
                         fill="#FFFFFF", outline="#4472C4", text_color="#1A1A1A",
                         font_size=23, bold=False)
        # 中模块1 (xc=1155, w=530 -> [890, 1420])
        draw_rounded_box(draw, 1155, yc, 530, bh, st["mid1"],
                         fill="#EDF2F8", outline="#2F5597", text_color="#102542",
                         font_size=23, bold=True)
        # 中模块2 (xc=1695, w=410 -> [1490, 1900])
        draw_rounded_box(draw, 1695, yc, 410, bh, st["mid2"],
                         fill="#FFFFFF", outline="#4472C4", text_color="#1A1A1A",
                         font_size=23, bold=False)
        # 右侧产出 (xc=2160, w=360 -> [1980, 2340])
        draw_rounded_box(draw, 2160, yc, 360, bh, st["out"],
                         fill="#E2EFDA", outline="#548235", text_color="#274E13",
                         font_size=25, bold=True)

        # 横向箭头
        draw_arrow(draw, 400, yc, 470, yc, color="#2F5597", width=4)
        draw_arrow(draw, 820, yc, 890, yc, color="#2F5597", width=4)
        draw_arrow(draw, 1420, yc, 1490, yc, color="#2F5597", width=4)
        draw_arrow(draw, 1900, yc, 1980, yc, color="#548235", width=4)

    # Step 3: 绘制阶段间纵向递进箭头（位于最上层，清晰可见）
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
    """图2：基于PX4/SITL的水下航行器闭环仿真系统结构框图 (2400 x 1320 px @ 300 DPI)"""
    W, H = 2400, 1320
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    # 外围大框：PX4/SITL 闭环仿真环境
    draw.rounded_rectangle([40, 40, 2360, 1280], radius=24,
                           fill="#FAFBFD", outline="#2F5597", width=4)
    title_font = get_font(32, bold=True)
    title_text = "PX4 / SITL 水下航行器闭环仿真系统结构框图（通过 uORB 实现模块间数据交互）"
    tb = draw.textbbox((0, 0), title_text, font=title_font)
    draw.text((W // 2 - (tb[2] - tb[0]) // 2, 68), title_text, font=title_font, fill="#1F3864")

    # 顶层支撑模块1：系统辨识与模型验证 (加宽至 830px, 字号 23)
    draw_rounded_box(
        draw, 960, 265, 830, 190,
        "平台参数资料与相关数据支撑\n系统辨识与模型验证模块\n（明确辨识输入输出关系，辨识修正关键未知参数并验证模型动态响应）",
        fill="#FFF2CC", outline="#BF9000", text_color="#332600",
        font_size=23, bold=True
    )

    # 顶层支撑模块2：典型运动工况与外部扰动设置
    draw_rounded_box(
        draw, 1960, 265, 620, 190,
        "代表性工况与外部扰动条件设置\n（姿态、深度、航向等典型运动任务\n及适量外部水流扰动作用）",
        fill="#FCE4D6", outline="#C65911", text_color="#331500",
        font_size=23, bold=True
    )

    # 中层核心闭环链路（Y = 660）
    yc = 660
    bh = 250
    # 1. 参考状态
    draw_rounded_box(
        draw, 240, yc, 300, bh,
        "参考运动状态\n\n姿态 / 深度 /\n航向参考状态",
        fill="#E2EFDA", outline="#548235", text_color="#1E3F0F",
        font_size=26, bold=True
    )

    # 2. 水下航行器运动控制模块
    draw_rounded_box(
        draw, 760, yc, 450, bh,
        "水下航行器运动控制模块\n\n结合航行器动力学特性与状态反馈\n根据参考状态与当前状态误差\n计算期望广义力和力矩",
        fill="#D9E1F2", outline="#2F5597", text_color="#102542",
        font_size=24, bold=True
    )

    # 3. 八推进器控制分配模块
    draw_rounded_box(
        draw, 1410, yc, 450, bh,
        "八推进器控制分配模块\n\n依据推进器安装位置、推力方向\n及力臂建立控制分配矩阵\n考虑基本推力输出范围生成指令",
        fill="#D9E1F2", outline="#2F5597", text_color="#102542",
        font_size=24, bold=True
    )

    # 4. 航行器与推进器六自由度动力学模型
    draw_rounded_box(
        draw, 2040, yc, 450, bh,
        "水下航行器与推进器动力学模型\n\n单推进器特性模型 +\n六自由度运动学与动力学模型\n（惯性/附加质量/科氏力/阻尼/恢复力）",
        fill="#EDEDED", outline="#595959", text_color="#1A1A1A",
        font_size=23, bold=True
    )

    # 底层：uORB 状态反馈与性能评价
    draw_rounded_box(
        draw, 1250, 1090, 1280, 160,
        "uORB 状态信息反馈与闭环系统性能分析模块\n（实时反馈姿态、角速度、深度、航向等运动状态；结合跟踪误差、动态响应与控制分配误差进行性能评价）",
        fill="#E8EEF5", outline="#4472C4", text_color="#1F3864",
        font_size=23, bold=True
    )

    # 主前向箭头
    draw_arrow(draw, 390, yc, 535, yc, color="#2F5597", width=5,
               label="参考状态", label_offset=(0, -42), font_size=23)
    draw_arrow(draw, 985, yc, 1185, yc, color="#2F5597", width=5,
               label="期望广义力\n与力矩", label_offset=(0, -52), font_size=23)
    draw_arrow(draw, 1635, yc, 1815, yc, color="#2F5597", width=5,
               label="八推进器\n推力指令", label_offset=(0, -52), font_size=23)

    # 顶层系统辨识模块 → 运动控制模块 & 动力学模型
    draw_polyline_arrow(
        draw, [(760, 360), (760, 535)],
        color="#BF9000", width=4,
        label="提供经验证的模型基础", label_pos=(760, 445), font_size=23
    )
    draw_polyline_arrow(
        draw, [(1220, 360), (1220, 445), (1920, 445), (1920, 535)],
        color="#BF9000", width=4,
        label="辨识修正模型参数", label_pos=(1560, 445), font_size=23
    )

    # 顶层扰动模块 → 动力学模型
    draw_arrow(draw, 2100, 360, 2100, 535, color="#C65911", width=4,
               label="外部扰动输入", label_offset=(95, 0), font_size=23)

    # 动力学模型 → 底层状态反馈模块 → 运动控制模块
    draw_polyline_arrow(
        draw, [(2040, 785), (2040, 1090), (1890, 1090)],
        color="#4472C4", width=5,
        label="实时运动状态输出", label_pos=(2040, 935), font_size=23
    )
    draw_polyline_arrow(
        draw, [(610, 1090), (490, 1090), (490, 720), (535, 720)],
        color="#4472C4", width=5,
        label="状态反馈 (uORB)", label_pos=(490, 920), font_size=23
    )

    out_path = os.path.join(OUT_DIR, "fig2_px4_rov_architecture.png")
    img.save(out_path, dpi=(300, 300))
    print("Saved:", out_path)


if __name__ == "__main__":
    generate_fig1_roadmap()
    generate_fig2_architecture()
