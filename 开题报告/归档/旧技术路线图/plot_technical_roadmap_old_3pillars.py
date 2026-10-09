# -*- coding: utf-8 -*-
"""
生成开题报告技术路线图：300 DPI 出版级极简学术线稿风格
紧凑横向版面设计（宽 6.8 英寸，高 4.8 英寸，缩印至 Word 宽度 14.5 cm 时高度约为 10.2 cm），
符合 IEEE/IFAC 顶级学术规范，白底黑灰细线、文字清晰锐利，无图内顶栏冗余大标题，无西方短横线列表符。
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
    # 画布大小：宽 6.8 英寸 (~17.2 cm)，高 4.8 英寸 (~12.2 cm)，300 DPI
    fig, ax = plt.subplots(figsize=(6.8, 4.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # 五大阶段数据定义（精炼工科短语，彻底去除短横线）
    stages = [
        {
            "id": "阶段一",
            "title": "六自由度机理动力学建模与几何惯性测算",
            "basis": "理论基座：Fossen 六自由度非线性统一动力学体系 [3]",
            "tasks": "• 建立水下 6-DOF 运动学与非线性动力学状态方程   • 3D CAD 测算质量与转动惯量   • 水池静水配平获取浮心与净浮力",
            "output": "输出：机理状态方程骨架与刚体惯性参数"
        },
        {
            "id": "阶段二",
            "title": "水池时域试验与动量滤波抗噪参数辨识",
            "basis": "方法基座：Caccia 板载传感器试验范式 [14] 与 Park 动量回归变换 [18]",
            "tasks": "• 设计推进器阶跃推力与机体自由衰减水池工况   • 广义动量积分抑制离散数值微分噪声   • 时域滤波拟合提取阻尼与校验残差",
            "output": "输出：经残差校验的水动力阻尼与有效惯性"
        },
        {
            "id": "阶段三",
            "title": "基于 PX4 的动力学模型前馈补偿与状态反馈控制",
            "basis": "控制基座：PX4 原生实时微内核架构 [8] 与 Smallwood 前馈消融范式 [9]",
            "tasks": "• 构建显式动力学模型前馈回路实时解耦流阻耗散   • 板载传感器高频姿态与位置观测状态反馈   • 形成前馈补偿+高频反馈双闭环",
            "output": "输出：六维广义期望控制力与力矩 τ_cmd"
        },
        {
            "id": "阶段四",
            "title": "八推进器空间几何分配与力矩优先抗饱和设计",
            "basis": "分配基座：Johansen 控制分配理论 [7] 与加权伪逆解析映射",
            "tasks": "• 推导空间对称与矢量倾斜推力配置矩阵   • 加权伪逆法求取最小能耗推力解析分配解   • 推力饱和时力矩优先自适应缩放平移推力",
            "output": "输出：八台推进器独立轴向推力指令 T_1 ~ T_8"
        },
        {
            "id": "阶段五",
            "title": "SITL 软件在环仿真与水池物理实验分级消融验证",
            "basis": "验证基座：PX4/SITL 水动力学闭环仿真与室内实验水池实机测试",
            "tasks": "• 搭建集成 6-DOF 水动力学的 SITL 软件在环环境   • 开展定点悬停与阶跃响应水池闭环实测   • 以无模型 PID 为对照组开展多维消融评估",
            "output": "交付成果：多维消融量化对比结论、嵌入式控制代码与论文正稿"
        }
    ]

    # 布局几何参数：紧凑纵向 5 阶段流向
    box_w = 94
    box_h = 12.8
    box_x = 3
    y_starts = [84.5, 64.0, 43.5, 23.0, 2.5]  # 5 个框的底 y 坐标

    for i, s in enumerate(stages):
        y = y_starts[i]

        # 阶段主外框（白底、深灰细线边框）
        rect = patches.FancyBboxPatch(
            (box_x, y), box_w, box_h,
            boxstyle="round,pad=0.3,rounding_size=1.0",
            facecolor="#FAFAFC", edgecolor="#333333",
            linewidth=0.9, zorder=2
        )
        ax.add_patch(rect)

        # 阶段顶部标题底色条
        header_h = 3.6
        header_rect = patches.FancyBboxPatch(
            (box_x, y + box_h - header_h), box_w, header_h,
            boxstyle="round,pad=0.3,rounding_size=1.0",
            facecolor="#EDF0F5", edgecolor="#4A5568",
            linewidth=0.7, zorder=3
        )
        ax.add_patch(header_rect)

        # 阶段序号标签块（深蓝灰底色白字，突出层级）
        tag_w = 12.5
        tag_h = 2.4
        tag_rect = patches.Rectangle(
            (box_x + 1.2, y + box_h - header_h + 0.6), tag_w, tag_h,
            facecolor="#1A365D", edgecolor="none", zorder=4
        )
        ax.add_patch(tag_rect)
        ax.text(
            box_x + 1.2 + tag_w / 2.0, y + box_h - header_h + 0.6 + tag_h / 2.0,
            s["id"], color="white", fontsize=7.8, fontweight="bold",
            ha="center", va="center", zorder=5
        )

        # 阶段标题文字
        ax.text(
            box_x + tag_w + 2.5, y + box_h - header_h + 0.6 + tag_h / 2.0,
            s["title"], color="#0F172A", fontsize=8.5, fontweight="bold",
            ha="left", va="center", zorder=5
        )

        # 右上角：理论基座说明
        ax.text(
            box_x + box_w - 1.5, y + box_h - header_h + 0.6 + tag_h / 2.0,
            s["basis"], color="#475569", fontsize=6.8, fontstyle="italic",
            ha="right", va="center", zorder=5
        )

        # 阶段核心任务内容
        ax.text(
            box_x + 2.5, y + 4.8,
            s["tasks"], color="#334155", fontsize=6.8,
            ha="left", va="center", zorder=5
        )

        # 阶段向下箭头与中间传递标签
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
                    color="#1E293B",
                    lw=1.2,
                    mutation_scale=9
                ),
                zorder=6
            )

            # 箭头右侧输出数据流小标签
            output_txt = s["output"]
            ax.text(
                52, mid_y,
                output_txt,
                color="#0369A1", fontsize=6.6, fontweight="bold",
                ha="left", va="center",
                bbox=dict(boxstyle="square,pad=0.18", facecolor="#F0F9FF", edgecolor="#7DD3FC", lw=0.6),
                zorder=7
            )

    plt.tight_layout(pad=0.15)
    output_path = "开题报告/figures/fig_technical_roadmap.png"
    plt.savefig(output_path, dpi=300, facecolor="white", edgecolor="none")
    plt.close()
    print(f"紧凑高品质技术路线图生成成功：{output_path}")

if __name__ == "__main__":
    create_technical_roadmap()
