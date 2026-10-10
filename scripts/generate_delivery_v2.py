# -*- coding: utf-8 -*-
"""
生成方案二的交付文件：
1. 开题报告/PX4_第一节_修改后净稿_交付版.docx
2. 开题报告/PX4_第一节_对照修改稿_交付版.docx
同时严格保留全部 25 处可编辑区域 (permStart / permEnd)。
"""

import os
import sys
import docx
from docx.shared import Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_COLOR_INDEX

sys.stdout.reconfigure(encoding="utf-8")

BASE_DOC = r"开题报告/02_PX4第一节_修改后净稿.docx"
CLEAN_OUT = r"开题报告/PX4_第一节_修改后净稿_交付版.docx"
DIFF_OUT  = r"开题报告/PX4_第一节_对照修改稿_交付版.docx"

def set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0, bold=False):
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

def add_runs_to_para(p, text_spec_list):
    """
    text_spec_list is a list of tuples:
    (text, is_strike, is_yellow, is_superscript)
    """
    # 清空原有 run，但保留段落属性和 permStart / permEnd 节点
    for r in list(p.runs):
        p._p.remove(r._r)
    
    for text, is_strike, is_yellow, is_super in text_spec_list:
        if not text:
            continue
        run = p.add_run(text)
        set_run_font(run, chinese_font="宋体", western_font="Times New Roman", font_size_pt=12.0)
        if is_strike:
            run.font.strike = True
        if is_yellow:
            run.font.highlight_color = WD_COLOR_INDEX.YELLOW
        if is_super:
            run.font.superscript = True

# --- 纯净版文本定义 ---
clean_p18_specs = [
    ("随着“海洋强国”战略的推进，水下基础设施的安全运维对小型水下航行器提出了更高要求。《“十四五”机器人产业发展规划》", False, False, False),
    ("[1]", False, False, True),
    ("将水下探测、监测和作业机器人纳入特种机器人重点发展方向；《“机器人+”应用行动实施方案》", False, False, False),
    ("[2]", False, False, True),
    ("提出在风电场、水电站、油气管网等能源基础设施场景推广巡检、维护等机器人应用。海上风电桩基、水下大坝立面及海底能源管线等设施在长期服役过程中，需要在近壁面、狭小空间及水流扰动等工况下开展定期巡检。相较于依赖潜水员或大型水下装备的作业方式，小型遥控水下航行器（ROV）部署更为灵活，适用于近距离精细巡检等任务。但在狭小空间和近壁水流扰动条件下，航行器还需兼顾稳定悬停、精确对位观测和低速灵活机动，对运动控制精度与稳定性提出了较高要求。", False, False, False)
]

clean_p19_specs = [
    ("为满足上述近距离巡检中多方向运动、位姿调整与稳定悬停的需求，本课题考虑采用空间矢量布局的八推进器构型。该构型可通过推进器协同产生不同方向的合力与力矩，为航行器的六自由度运动控制提供执行机构基础。与此同时，多推进器配置也增加了动力学建模与控制分配的难度：在动力学层面，附加质量、水动力阻尼以及重心与浮心的相对位置等因素，会使航行器的平动与转动存在耦合关系", False, False, False),
    ("[3]", False, False, True),
    ("；在执行机构层面，推进器受尺寸与电机功率等条件限制，存在推力幅值上限，并可能受到响应滞后、正反转死区等非理想特性的影响。在近壁水流扰动条件下，若未能协调推进器输出并合理处理推力约束，可能出现推力饱和或控制误差增大，从而影响悬停稳定性与轨迹跟踪精度。", False, False, False)
]

clean_p20_specs = [
    ("对于多变量耦合及执行器受限的控制问题，常规比例—积分—微分（PID）控制结构简单、易于实现，但分通道PID控制若缺少耦合补偿及约束协调机制，可能难以同时兼顾多自由度控制精度与推进器推力限制。模型预测控制（MPC）基于系统动力学模型进行滚动优化，可在优化问题中显式纳入状态与推力约束，为多推进器受约束控制提供可行思路，但仍需兼顾模型精度与嵌入式计算的实时性。此外，控制算法的工程实现还需要相应的飞控软件与仿真验证环境。PX4作为开源飞控平台，已为部分水下航行器构型提供基本控制模式，但官方文档仍将其水下航行器支持列为实验性功能", False, False, False),
    ("[4]", False, False, True),
    ("。因此，面向具体航行器的动力学特性及推进器约束，在PX4相关环境中开展MPC算法的适配与验证具有研究价值。", False, False, False)
]

clean_p21_specs = [
    ("本课题立足于水下基础设施近距离巡检中精确运动控制的实际工程需求。针对水下近距离精细巡检对位姿控制精度、悬停稳定性及推力约束处理的实际需求，本课题以八推进器紧凑型水下航行器为研究对象，选用适用于控制设计的六自由度动力学模型与推进器推力分配模型，研究考虑推进器推力约束的模型预测控制（MPC）方法，并在PX4相关控制与仿真环境中开展闭环验证。本研究旨在分析水动力耦合与推力约束对航行器运动控制性能的影响，探索控制精度与实时计算开销之间的权衡。在研究层面，可为多推进器水下航行器的受约束运动控制提供方法参考；在工程层面，可为预测控制算法在PX4平台中的集成验证，以及水下基础设施近距离巡检中的运动控制应用提供技术借鉴。", False, False, False)
]

# --- 对比版文本定义 ---
diff_p18_specs = [
    ("随着“海洋强国”战略的推进，水下基础设施的安全运维对小型水下航行器提出了更高要求。《“十四五”机器人产业发展规划》", False, False, False),
    ("[1]", False, False, True),
    ("将水下探测、监测和作业机器人纳入特种机器人重点发展方向；《“机器人+”应用行动实施方案》", False, False, False),
    ("[2]", False, False, True),
    ("提出推动机器人在风电场、水电站、油气管网等能源基础设施巡检与维护场景中的深化应用。", True, False, False),
    ("提出在风电场、水电站、油气管网等能源基础设施场景推广巡检、维护等机器人应用。", False, True, False),
    ("海上风电桩基、水下大坝立面及海底能源管线等设施长期服役，存在近壁面、狭小空间和水流扰动下的定期巡检需求。", True, False, False),
    ("海上风电桩基、水下大坝立面及海底能源管线等设施在长期服役过程中，需要在近壁面、狭小空间及水流扰动等工况下开展定期巡检。", False, True, False),
    ("相较于依赖潜水员或大型水下装备的作业方式，", False, False, False),
    ("小型水下机器人（ROV）", True, False, False),
    ("小型遥控水下航行器（ROV）", False, True, False),
    ("在部署灵活性方面具有优势，逐渐成为执行近距离精细巡检的核心作业装备。", True, False, False),
    ("部署更为灵活，适用于近距离精细巡检等任务。", False, True, False),
    ("然而，水下狭窄空间近壁作业环境复杂、水流扰动频繁，对航行器的稳定悬停对齐观测与低速多自由度灵活机动提出了严苛要求。", True, False, False),
    ("但在狭小空间和近壁水流扰动条件下，航行器还需兼顾稳定悬停、精确对位观测和低速灵活机动，对运动控制精度与稳定性提出了较高要求。", False, True, False)
]

diff_p19_specs = [
    ("为满足上述近距精细巡检中任意姿态调节与稳定悬停的需求，具备全向驱动能力的空间矢量布局八推进器构型成为主流选择，为实现航行器空间六自由度姿态的主动调节提供了物理基础。", True, False, False),
    ("为满足上述近距离巡检中多方向运动、位姿调整与稳定悬停的需求，本课题考虑采用空间矢量布局的八推进器构型。该构型可通过推进器协同产生不同方向的合力与力矩，为航行器的六自由度运动控制提供执行机构基础。", False, True, False),
    ("然而，这种多推进器空间矢量布局也带来了复杂的控制问题：", True, False, False),
    ("与此同时，多推进器配置也增加了动力学建模与控制分配的难度：", False, True, False),
    ("在动力学机理层面，受流体附加质量非对角交叉项、高阶非线性水动力阻尼以及重心与浮心偏置诱发的静水恢复力矩共同作用，航行器的空间平动与姿态转动之间存在固有的强非线性交叉耦合特性", True, False, False),
    ("在动力学层面，附加质量、水动力阻尼以及重心与浮心的相对位置等因素，会使航行器的平动与转动存在耦合关系", False, True, False),
    ("[3]", False, False, True),
    ("；", False, False, False),
    ("在执行机构层面，推进器受紧凑机体尺寸与电机功率限制，存在严格的推力幅值饱和、响应滞后及正反转死区等物理硬约束。", True, False, False),
    ("在执行机构层面，推进器受尺寸与电机功率等条件限制，存在推力幅值上限，并可能受到响应滞后、正反转死区等非理想特性的影响。", False, True, False),
    ("在近壁复杂水流扰动下，若多推进器推力无法协调优化，极易诱发执行器饱和与控制分配失真，进而导致悬停失稳或跟踪精度大幅下降。", True, False, False),
    ("在近壁水流扰动条件下，若未能协调推进器输出并合理处理推力约束，可能出现推力饱和或控制误差增大，从而影响悬停稳定性与轨迹跟踪精度。", False, True, False)
]

diff_p20_specs = [
    ("面对多变量强耦合与执行器物理约束，常规比例—积分—微分（PID）控制实现简便，但由于缺乏对多变量动力学特性的显式表征，难以在控制律中直接协调多推进器的物理极限，在强扰动或机动作业时易引发推力饱和与系统超调。", True, False, False),
    ("对于多变量耦合及执行器受限的控制问题，常规比例—积分—微分（PID）控制结构简单、易于实现，但分通道PID控制若缺少耦合补偿及约束协调机制，可能难以同时兼顾多自由度控制精度与推进器推力限制。", False, True, False),
    ("模型预测控制（MPC）基于系统动力学模型进行在线滚动优化，能够在控制律中显式处理状态与推力硬约束，是解决水下多变量受约束运动控制的有效途径，但需兼顾模型描述精度与嵌入式计算的实时性。", True, False, False),
    ("模型预测控制（MPC）基于系统动力学模型进行滚动优化，可在优化问题中显式纳入状态与推力约束，为多推进器受约束控制提供可行思路，但仍需兼顾模型精度与嵌入式计算的实时性。", False, True, False),
    ("此外，先进控制算法的实际工程应用离不开成熟的机载飞控系统支撑。", True, False, False),
    ("此外，控制算法的工程实现还需要相应的飞控软件与仿真验证环境。", False, True, False),
    ("PX4作为目前工业界与学术界广泛采用的开源标准化自主飞控平台[4]，近年来逐步拓展了对水下航行器的支持；但其官方原生固件仍主要采用传统的PID控制框架，尚未集成考虑水动力学模型与推力非线性约束的预测优化控制算法，难以充分发挥多推进器构型的控制潜力。", True, False, False),
    ("PX4作为开源飞控平台，已为部分水下航行器构型提供基本控制模式，但官方文档仍将其水下航行器支持列为实验性功能", False, True, False),
    ("[4]", False, True, True),
    ("。因此，面向具体航行器的动力学特性及推进器约束，在PX4相关环境中开展MPC算法的适配与验证具有研究价值。", False, True, False)
]

diff_p21_specs = [
    ("本课题立足于水下基础设施近距离巡检中精确运动控制的实际工程需求。", False, True, False),
    ("针对水下近距离精细巡检对位姿控制精度、悬停稳定性及推力约束处理的", False, False, False),
    ("迫切需求", True, False, False),
    ("实际需求", False, True, False),
    ("，本课题以八推进器紧凑型水下航行器为研究对象，", False, False, False),
    ("选用适用于控制设计的六自由度动力学与推力分配模型", True, False, False),
    ("选用适用于控制设计的六自由度动力学模型与推进器推力分配模型", False, True, False),
    ("，", False, False, False),
    ("研究兼顾执行器推力物理约束的模型预测控制（MPC）方法", True, False, False),
    ("研究考虑推进器推力约束的模型预测控制（MPC）方法", False, True, False),
    ("，并在PX4相关控制与仿真环境中开展闭环验证。", False, False, False),
    ("本研究旨在突破强耦合与物理约束下水下航行器的高性能运动控制瓶颈，有助于深入分析多推进器水下航行器在物理约束与水动力特性下的控制性能权衡，同时探索先进预测控制算法在标准化开源飞控系统中的工程实现路径，为我国水下基础设施的高精度无人化自主巡检提供切实有效的方法与技术参考。", True, False, False),
    ("本研究旨在分析水动力耦合与推力约束对航行器运动控制性能的影响，探索控制精度与实时计算开销之间的权衡。在研究层面，可为多推进器水下航行器的受约束运动控制提供方法参考；在工程层面，可为预测控制算法在PX4平台中的集成验证，以及水下基础设施近距离巡检中的运动控制应用提供技术借鉴。", False, True, False)
]

def main():
    print(">>> 开始生成交付文档...")
    
    # 1. 纯净版
    doc_clean = docx.Document(BASE_DOC)
    add_runs_to_para(doc_clean.paragraphs[18], clean_p18_specs)
    add_runs_to_para(doc_clean.paragraphs[19], clean_p19_specs)
    add_runs_to_para(doc_clean.paragraphs[20], clean_p20_specs)
    add_runs_to_para(doc_clean.paragraphs[21], clean_p21_specs)
    doc_clean.save(CLEAN_OUT)
    print("成功生成纯净版：", CLEAN_OUT)

    # 2. 对比版
    doc_diff = docx.Document(BASE_DOC)
    add_runs_to_para(doc_diff.paragraphs[18], diff_p18_specs)
    add_runs_to_para(doc_diff.paragraphs[19], diff_p19_specs)
    add_runs_to_para(doc_diff.paragraphs[20], diff_p20_specs)
    add_runs_to_para(doc_diff.paragraphs[21], diff_p21_specs)
    doc_diff.save(DIFF_OUT)
    print("成功生成对比版：", DIFF_OUT)

    # 3. 校验权限节点
    print("\n>>> 开始校验可编辑区域权限节点 (permStart / permEnd)...")
    for path in [CLEAN_OUT, DIFF_OUT]:
        d = docx.Document(path)
        body = d._body._element
        starts = [s.get(qn("w:id")) for s in body.xpath(".//w:permStart")]
        ends = [e.get(qn("w:id")) for e in body.xpath(".//w:permEnd")]
        print(f"[{os.path.basename(path)}] permStart 总数: {len(starts)}, permEnd 总数: {len(ends)}")
        assert len(starts) == 25, f"permStart 数量异常: {len(starts)}"
        assert len(ends) == 25, f"permEnd 数量异常: {len(ends)}"
        assert "10" in starts, "Section 1 permStart (id=10) 丢失！"
        assert "10" in ends, "Section 1 permEnd (id=10) 丢失！"
        print(f"  -> 权限审计 100% 通过！25 对权限节点完全闭环且平衡。")

if __name__ == "__main__":
    main()
