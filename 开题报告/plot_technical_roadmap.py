# -*- coding: utf-8 -*-
"""
生成开题报告技术路线图：300 DPI 出版级极简学术线稿风格
符合 IEEE/IFAC 标准，白底、细线黑框、文字清晰自明，严禁图内顶栏大标题。
"""

import sys
sys.stdout.reconfigure(encoding="utf-8")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 设置全局字体：使用原生微软雅黑与 Times New Roman
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

def create_technical_roadmap():
    # 画布大小：宽 6.2 英寸 (~15.7 cm，契合 Word 页面版心宽度)，高 8.0 英寸，300 DPI
    fig, ax = plt.subplots(figsize=(6.2, 8.0), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # 阶段数据定义
    stages = [
        {
            "id": "阶段一",
            "title": "六自由度机理动力学建模与几何惯性测算",
            "basis": "理论基座：Fossen 六自由度非线性动力学统一建模体系 [3]",
            "tasks": [
                "- 建立水下六自由度运动学与动力学非线性状态方程",
                "- 三维 CAD 模型测算干重、质心位置与转动惯量矩阵",
                "- 室内实验水池静态悬浮配平试验获取浮心坐标与净浮力"
            ],
            "output": "输出：六自由度动力学机理方程骨架与刚体几何惯性参数"
        },
        {
            "id": "阶段二",
            "title": "水池时域试验与动量滤波抗噪参数辨识",
            "basis": "方法基座：Caccia 板载传感器试验范式 [12] 与 Park 动量回归变换 [16]",
            "tasks": [
                "- 设计推进器阶跃推力激励与自由衰减水池试验工况",
                "- 引入广义动量变换抑制离散求导的高频噪声放大",
                "- 数字滤波结合时域拟合提取阻尼参数并开展残差校验"
            ],
            "output": "输出：经独立工况残差校验的有效惯性与非线性阻尼参数"
        },
        {
            "id": "阶段三",
            "title": "基于 PX4 的动力学前馈补偿与状态反馈控制",
            "basis": "控制基座：PX4 原生实时架构 [8] 与 Smallwood 模型前馈消融范式 [9]",
            "tasks": [
                "- 构建显式动力学模型前馈回路，实时解算流阻与耦合补偿",
                "- 结合板载传感器高频姿态与位置观测构建状态反馈回路",
                "- 形成“动力学模型前馈补偿 + 状态反馈”双闭环控制架构"
            ],
            "output": "输出：高频解算的六维广义期望控制力与力矩指令 τ_cmd"
        },
        {
            "id": "阶段四",
            "title": "八推进器空间几何分配与力矩优先抗饱和设计",
            "basis": "分配基座：Johansen 控制分配理论 [7] 与加权伪逆解析映射",
            "tasks": [
                "- 推导空间对称与矢量倾斜八推进器空间几何配置矩阵",
                "- 加权伪逆法求取控制能耗最小的毫秒级基准推力解析解",
                "- 设计力矩优先解饱和机制，在推力超限时保全姿态控制力矩"
            ],
            "output": "输出：八台推进器独立物理轴向推力指令 T_1 ~ T_8"
        },
        {
            "id": "阶段五",
            "title": "SITL 软件在环仿真与水池物理实验分级消融验证",
            "basis": "验证基座：PX4/SITL 水动力学仿真闭环与室内实验水池实机测试",
            "tasks": [
                "- 搭建集成六自由度水动力模块的 PX4 SITL 软件在环仿真环境",
                "- 开展定点悬停抗扰与多轴阶跃等典型工况的实机水池闭环测试",
                "- 引入无模型 PID 为基准，从轨迹误差、姿态波动等开展消融评估"
            ],
            "output": "交付成果：多指标消融量化对比结论、控制系统软件与毕业论文正文"
        }
    ]

    # 布局几何参数
    box_w = 90
    box_h = 13.5
    box_x = 5
    y_starts = [84, 64, 44, 24, 4]  # 从上到下 5 个阶段框的底部 y 坐标

    for i, s in enumerate(stages):
        y = y_starts[i]
        
        # 外框（圆角细矩形，白底黑线，极简学术感）
        rect = patches.FancyBboxPatch(
            (box_x, y), box_w, box_h,
            boxstyle="round,pad=0.6,rounding_size=1.2",
            facecolor="#FBFBFD", edgecolor="#222222",
            linewidth=1.0, zorder=2
        )
        ax.add_patch(rect)

        # 阶段序号与标题条底色
        header_h = 3.6
        header_rect = patches.FancyBboxPatch(
            (box_x, y + box_h - header_h), box_w, header_h,
            boxstyle="round,pad=0.6,rounding_size=1.2",
            facecolor="#F0F2F5", edgecolor="#333333",
            linewidth=0.8, zorder=3
        )
        ax.add_patch(header_rect)

        # 阶段序号标签块（深灰背景白字，突出层次）
        tag_w = 14
        tag_h = 2.4
        tag_rect = patches.Rectangle(
            (box_x + 1.2, y + box_h - header_h + 0.6), tag_w, tag_h,
            facecolor="#2C3E50", edgecolor="none", zorder=4
        )
        ax.add_patch(tag_rect)
        ax.text(
            box_x + 1.2 + tag_w / 2.0, y + box_h - header_h + 0.6 + tag_h / 2.0,
            s["id"], color="white", fontsize=8.0, fontweight="bold",
            ha="center", va="center", zorder=5
        )

        # 阶段标题文字
        ax.text(
            box_x + tag_w + 2.5, y + box_h - header_h + 0.6 + tag_h / 2.0,
            s["title"], color="#1A252F", fontsize=8.8, fontweight="bold",
            ha="left", va="center", zorder=5
        )

        # 理论/方法基座说明
        ax.text(
            box_x + 2.5, y + 7.4,
            s["basis"], color="#4A5568", fontsize=7.2, fontstyle="italic",
            ha="left", va="center", zorder=5
        )

        # 任务条目
        for t_idx, task_text in enumerate(s["tasks"]):
            task_y = y + 5.2 - t_idx * 1.8
            ax.text(
                box_x + 3.0, task_y,
                task_text, color="#2D3748", fontsize=7.1,
                ha="left", va="center", zorder=5
            )

        # 阶段向下箭头与中间数据流文字（第 0~3 阶段之间）
        if i < 4:
            arrow_y_top = y
            arrow_y_bot = y_starts[i + 1] + box_h
            mid_y = (arrow_y_top + arrow_y_bot) / 2.0

            # 居中垂直向下箭头
            ax.annotate(
                "",
                xy=(50, arrow_y_bot),
                xytext=(50, arrow_y_top),
                arrowprops=dict(
                    arrowstyle="-|>",
                    color="#2C3E50",
                    lw=1.3,
                    mutation_scale=10
                ),
                zorder=6
            )

            # 箭头右侧数据流小标签
            output_txt = s["output"]
            ax.text(
                52, mid_y,
                output_txt,
                color="#1A365D", fontsize=6.8, fontweight="bold",
                ha="left", va="center",
                bbox=dict(boxstyle="square,pad=0.2", facecolor="#EDF2F7", edgecolor="#CBD5E0", lw=0.6),
                zorder=7
            )

    plt.tight_layout(pad=0.2)
    output_path = "开题报告/figures/fig_technical_roadmap.png"
    plt.savefig(output_path, dpi=300, facecolor="white", edgecolor="none")
    plt.close()
    print(f"技术路线图生成成功：{output_path}")

if __name__ == "__main__":
    create_technical_roadmap()
