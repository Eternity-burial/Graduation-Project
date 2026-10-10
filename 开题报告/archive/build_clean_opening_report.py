# -*- coding: utf-8 -*-
"""
完整执行开题报告重构、更新参考文献、进度安排置空及历史文件归档
"""

import os
import sys
import re
import shutil
import subprocess
import docx

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"D:\tj\Graduation Project\开题报告"
ROOT_DIR = r"D:\tj\Graduation Project"
ARCHIVE_DIR = os.path.join(BASE_DIR, "archive")

# 37 篇规范化参考文献列表
REFS_37 = [
    "[1] 工业和信息化部, 国家发展和改革委员会, 科学技术部, 等. “十四五”机器人产业发展规划[J]. 中华人民共和国工业和信息化部公报, 2021(12): 20-27.",
    "[2] 工业和信息化部, 教育部, 科学技术部, 等. “机器人+”应用行动实施方案[J]. 中华人民共和国工业和信息化部公报, 2023(1): 18-24.",
    "[3] FOSSEN T I. Handbook of Marine Craft Hydrodynamics and Motion Control[M]. 2nd ed. Chichester, UK: John Wiley & Sons, 2021.",
    "[4] PX4 Development Team. Submarines (Unmanned Underwater Vehicles—UUV)[EB/OL]. (2024)[2026-10-10]. https://docs.px4.io/main/en/frames_sub/index.",
    "[5] FOSSEN T I. Nonlinear modelling of marine vehicles in 6 degrees of freedom[J]. Mathematical Modelling of Systems, 1995, 1(1): 17-27.",
    "[6] 严卫生, 高剑, 崔荣鑫, 等. 水下航行器控制技术[M]. 北京: 国防工业出版社, 2020.",
    "[7] PRESTERO T. Verification of a six-degree of freedom simulation model for the REMUS autonomous underwater vehicle[D]. Cambridge, MA: Massachusetts Institute of Technology, 2001.",
    "[8] CACCIA M, INDIVERI G, VERUGGIO G. Modeling and identification of open-frame variable configuration unmanned underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 2000, 25(2): 227-240.",
    "[9] SMALLWOOD D A, WHITCOMB L L. Model-based dynamic positioning of underwater robotic vehicles: Theory and experiment[J]. IEEE Journal of Oceanic Engineering, 2004, 29(1): 169-186.",
    "[10] VON BENZON M, SØRENSEN F F, UTH E, et al. An open-source benchmark simulator: Control of a BlueROV2 underwater robot[J]. Journal of Marine Science and Engineering, 2022, 10(12): 1898.",
    "[11] 高婷, 庞永杰, 王亚兴, 等. 水下航行器水动力系数计算方法[J]. 哈尔滨工程大学学报, 2019, 40(1): 174-180.",
    "[12] CHIN C S, LAU M W S. Modeling and testing of hydrodynamic damping for a complex-shaped underwater robot operating at low speed[C]//2012 Oceans - Yeosu. Yeosu, Korea: IEEE, 2012: 1-7.",
    "[13] ROSS A, FOSSEN T I, JOHANSEN T A. Identification of underwater vehicle hydrodynamic coefficients using free decay tests[C]//IFAC Conference on Control Applications in Marine Systems. Ancona, Italy: IFAC, 2004: 363-368.",
    "[14] AVILA J P J, ADAMOWSKI J C. Experimental model identification of open-frame unmanned underwater vehicles[C]//2013 Oceans - San Diego. San Diego, CA: IEEE, 2013: 1-7.",
    "[15] HARRIS Z J, MAO A M, PAINE T M, et al. Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models for underactuated vehicles: Theory and experimental evaluation[J]. The International Journal of Robotics Research, 2023, 42(12): 1070-1093.",
    "[16] BRUNTON S L, PROCTOR J L, KUTZ J N. Discovering governing equations from data by sparse identification of nonlinear dynamical systems[J]. Proceedings of the National Academy of Sciences, 2016, 113(15): 3932-3937.",
    "[17] RAISSI M, PERDIKARIS P, KARNIADAKIS G E. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations[J]. Journal of Computational Physics, 2019, 378: 686-707.",
    "[18] CHEN R T Q, RUBANOVA Y, BETTENCOURT J, et al. Neural ordinary differential equations[C]//Advances in Neural Information Processing Systems (NeurIPS 2018). Montréal, QC, Canada, 2018: 6571-6583.",
    "[19] LIU A, ZHANG X, XIAO F, et al. Koopman-based online identification with Sim2Real transfer for hydrodynamic modeling of turtle-inspired robot[J]. IEEE Robotics and Automation Letters, 2026, 11(6): 6632-6639.",
    "[20] YUH J. Design and control of autonomous underwater robots: A survey[J]. Autonomous Robots, 2000, 8(1): 7-24.",
    "[21] 朱大奇, 孙兵. 水下机器人运动控制研究进展[J]. 控制与决策, 2012, 27(3): 321-333.",
    "[22] YOERGER D R, SLOTINE J J E. Robust trajectory control of underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 1985, 10(4): 462-470.",
    "[23] HEALEY A J, LIENARD D. Multivariable sliding mode control for autonomous diving and steering of unmanned underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 1993, 18(3): 327-339.",
    "[24] CHU Z, XIANG X, ZHU D, et al. Adaptive trajectory tracking control for remotely operated vehicles considering thruster dynamics and saturation constraints[J]. ISA Transactions, 2020, 100: 28-37.",
    "[25] 张磊, 严卫生, 付明玉. 自主水下航行器模型预测控制研究现状与展望[J]. 控制理论与应用, 2018, 35(9): 1181-1192.",
    "[26] HESHMATI-ALAMDARI S, KARRAS G C, MARANTOS P, et al. A robust model predictive control approach for autonomous underwater vehicles operating in a constrained workspace[C]//2018 IEEE International Conference on Robotics and Automation (ICRA). Brisbane, QLD, Australia: IEEE, 2018: 6183-6188.",
    "[27] HESHMATI-ALAMDARI S, NIKOU A, DIMAROGONAS D V. Robust trajectory tracking control for underactuated autonomous underwater vehicles in uncertain environments[J]. IEEE Transactions on Automation Science and Engineering, 2020, 18(3): 1288-1301.",
    "[28] JOHANSEN T A, FOSSEN T I. Control allocation: A survey[J]. Automatica, 2013, 49(5): 1087-1103.",
    "[29] BODSON M. Evaluation of optimization methods for control allocation[J]. Journal of Guidance, Control, and Dynamics, 2002, 25(4): 703-711.",
    "[30] HÄRKEGÅRD O. Efficient active set algorithms for solving constrained linear quadratic control allocation problems[J]. Journal of Guidance, Control, and Dynamics, 2002, 25(5): 827-835.",
    "[31] 程卫平, 王猛, 曾现敏, 等. 基于可行方向法的水下机器人推力分配[J]. 舰船科学技术, 2022, 44(13): 102-106.",
    "[32] 孙功武, 苏义鑫, 毛英, 等. 基于模糊逻辑的混合推进ROV多级推力分配策略[J]. 机器人, 2023, 45(4): 472-482.",
    "[33] LI J H, LEE M J, KIM M G, et al. MCE-based direct FTC method for dynamic positioning of underwater vehicles with thruster redundancy[C]//2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). Hangzhou, China: IEEE, 2025: 1542-1549. DOI: 10.1109/IROS60139.2025.11246250.",
    "[34] MEIER L, HONEGGER D, POLLEFEYS M. PX4: A node-based multithreaded open source robotics framework for deeply embedded platforms[C]//2015 IEEE International Conference on Robotics and Automation (ICRA). Seattle, WA, USA: IEEE, 2015: 6235-6240.",
    "[35] PX4 Development Team. Control Allocation (Mixing)[EB/OL]. [2026-10-10]. https://docs.px4.io/main/en/concept/control_allocation.",
    "[36] PX4 Development Team. BlueROV2 (UUV)[EB/OL]. [2026-10-10]. https://docs.px4.io/main/en/frames_sub/bluerov2.",
    "[37] PX4 Development Team. Offboard Mode (Generic/All Frames)[EB/OL]. [2026-10-10]. https://docs.px4.io/main/en/flight_modes/offboard."
]

OLD_TO_NEW = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 45: 10,
    10: 11, 11: 12, 12: 13, 13: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19,
    20: 20, 21: 21, 23: 22, 24: 23, 25: 24, 29: 25, 30: 26, 31: 27,
    37: 28, 38: 29, 39: 30, 40: 31, 41: 32, 42: 33, 43: 34, 46: 35, 47: 36, 48: 37
}

def convert_citations_to_sup(text):
    def repl(m):
        content = m.group(1)
        if '-' in content or '–' in content:
            parts = re.split(r'[-–]', content)
            s = OLD_TO_NEW[int(parts[0])]
            e = OLD_TO_NEW[int(parts[1])]
            return f"$^{{[{s}-{e}]}}$"
        else:
            old_num = int(content)
            new_num = OLD_TO_NEW[old_num]
            return f"$^{{[{new_num}]}}$"
    return re.sub(r'\[(\d+(?:[–\-]\d+)?)\]', repl, text)

def rebuild_markdown():
    clean_docx_path = os.path.join(BASE_DIR, "PX4_研究现状_修订净稿_保留模板.docx")
    clean_docx = docx.Document(clean_docx_path)

    # 提取第2部分所有段落（P22为大标题，P23~P47为正文与子标题）
    sec2_md_paras = []
    for i in range(22, 48):
        t = clean_docx.paragraphs[i].text.strip()
        if not t:
            continue
        if t.startswith("2．") or t == "2. 国内外在该方向的研究现状和发展趋势":
            continue
        elif t.startswith("2.1 ") or t.startswith("2.2 ") or t.startswith("2.3 ") or t.startswith("2.4 "):
            sec2_md_paras.append(f"#### {t}")
        else:
            sup_t = convert_citations_to_sup(t)
            sec2_md_paras.append(sup_t)

    # 第1部分原始标准正文
    sec1_text = (
        "# 基于PX4的水下航行器模型控制方法研究 开题报告起草稿\n\n"
        "## 一、课题来源及研究的目的和意义\n\n"
        "### 1．课题来源及研究的目的和意义\n\n"
        "随着“海洋强国”战略的推进，水下基础设施的安全运维对小型水下航行器提出了更高要求。《“十四五”机器人产业发展规划》$^{[1]}$将水下探测、监测和作业机器人纳入特种机器人重点发展方向；《“机器人+”应用行动实施方案》$^{[2]}$提出在风电场、水电站、油气管网等能源基础设施场景推广巡检、维护等机器人应用。海上风电桩基、水下大坝立面及海底能源管线等设施在长期服役过程中，需要在近壁面、狭小空间及水流扰动等工况下开展定期巡检。相较于依赖潜水员或大型水下装备的作业方式，小型遥控水下航行器（ROV）部署更为灵活，适用于近距离精细巡检等任务。但在狭小空间和近壁水流扰动条件下，航行器还需兼顾稳定悬停、精确对位观测和低速灵活机动，对运动控制精度与稳定性提出了较高要求。\n\n"
        "为满足上述近距离巡检中多方向运动、位姿调整与稳定悬停的需求，本课题考虑采用空间矢量布局的八推进器构型。该构型可通过推进器协同产生不同方向的合力与力矩，为航行器的六自由度运动控制提供执行机构基础。与此同时，多推进器配置也增加了动力学建模与控制分配的难度：在动力学层面，附加质量、水动力阻尼以及重心与浮心的相对位置等因素，会使航行器的平动与转动存在耦合关系$^{[3]}$；在执行机构层面，推进器受尺寸与电机功率等条件限制，存在推力幅值上限，并可能受到响应滞后、正反转死区等非理想特性的影响。在近壁水流扰动条件下，若未能协调推进器输出并合理处理推力约束，可能出现推力饱和或控制误差增大，从而影响悬停稳定性与轨迹跟踪精度。\n\n"
        "对于多变量耦合及执行器受限的控制问题，常规比例—积分—微分（PID）控制结构简单、易于实现，但分通道PID控制若缺少耦合补偿及约束协调机制，可能难以同时兼顾多自由度控制精度与推进器推力限制。模型预测控制（MPC）基于系统动力学模型进行滚动优化，可在优化问题中显式纳入状态与推力约束，为多推进器受约束控制提供可行思路，但仍需兼顾模型精度与嵌入式计算的实时性。此外，控制算法的工程实现还需要相应的飞控软件与仿真验证环境。PX4作为开源飞控平台，已为部分水下航行器构型提供基本控制模式，但官方文档仍将其水下航行器支持列为实验性功能$^{[4]}$。因此，面向具体航行器的动力学特性及推进器约束，在PX4相关环境中开展MPC算法的适配与验证具有研究价值。\n\n"
    )

    sec2_body = "\n\n".join(sec2_md_paras)
    sec2_full = "### 2．国内外在该方向的研究现状和发展趋势\n\n" + sec2_body + "\n\n"

    sec3_full = (
        "## 二、毕业设计（论文）方案介绍\n\n"
        "### 1．主要研究内容\n\n"
        "（待后续阶段撰写）\n\n"
        "### 2．研究方案\n\n"
        "（待后续阶段撰写）\n\n"
        "### 3．工作进度安排\n\n"
        "（待后续阶段撰写）\n\n"
    )

    sec4_full = "## 三、毕业设计（论文）的主要参考文献\n\n" + "\n\n".join(REFS_37) + "\n\n"

    sec5_full = (
        "## 四、审核意见\n\n"
        "### 1．指导教师审核意见\n\n"
        "（待指导教师填写）\n\n"
        "### 2．专业委员会审核意见\n\n"
        "（待专业委员会填写）\n"
    )

    full_md = sec1_text + sec2_full + sec3_full + sec4_full + sec5_full
    md_path = os.path.join(BASE_DIR, "开题报告_正文起草稿.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(full_md)
    print(">>> [1/5] 已重构并更新《开题报告_正文起草稿.md》：Section 2接入修订净稿、37篇参考文献连续上标化编号、进度安排置空。")

def update_builder_script():
    builder_path = os.path.join(BASE_DIR, "build_opening_report_docx.py")
    with open(builder_path, "r", encoding="utf-8") as f:
        code = f.read()

    # 确保不插入进度安排表
    code = code.replace("insert_progress_table(p29, doc)", "# insert_progress_table(p29, doc)  # 进度安排置空")

    # 更新 audit 中的参考文献检查为 37 篇
    code = re.sub(r"assert len\(ref_lines\) == \d+,.*", "assert len(ref_lines) == 37, f'参考文献数量应为37篇，实际解析为: {len(ref_lines)}'", code)
    code = code.replace("t.startswith('[45]')", "t.startswith('[37]')")
    code = code.replace("45 篇", "37 篇")
    code = code.replace("45篇", "37篇")

    # 移除 audit 中对进度表表名的强制断言
    code = code.replace("if '主要研究内容' in tbl_text:", "if False and '主要研究内容' in tbl_text:")

    with open(builder_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(">>> [2/5] 已同步调整《build_opening_report_docx.py》的构建流程与验收断言（支持37篇参考文献，跳过进度表）。")

def run_build_pipeline():
    builder_path = os.path.join(BASE_DIR, "build_opening_report_docx.py")
    res = subprocess.run([sys.executable, builder_path], capture_output=True, text=True, cwd=ROOT_DIR, encoding="utf-8", errors="replace")
    print(res.stdout)
    if res.returncode != 0:
        print("STDERR:", res.stderr)
        raise RuntimeError("Word文档构建失败！")
    print(">>> [3/5] 主文档《开题报告-基于PX4的水下航行器模型控制方法研究.docx》生成并通过全部门禁审计！")

def update_bib_and_ris():
    bib_path = os.path.join(BASE_DIR, "references.bib")
    ris_path = os.path.join(BASE_DIR, "references.ris")

    # 写入规范的 references.bib
    bib_entries = """% 37 篇参考文献 BibTeX 数据库 (严格按照 GB/T 7714 顺序 [1]~[37] 连续编号)

@article{miit2021,
  author = {工业和信息化部 and 国家发展和改革委员会 and 科学技术部 and others},
  title = {“十四五”机器人产业发展规划},
  journal = {中华人民共和国工业和信息化部公报},
  year = {2021},
  number = {12},
  pages = {20--27}
}

@article{miit2023,
  author = {工业和信息化部 and 教育部 and 科学技术部 and others},
  title = {“机器人+”应用行动实施方案},
  journal = {中华人民共和国工业和信息化部公报},
  year = {2023},
  number = {1},
  pages = {18--24}
}

@book{fossen2021handbook,
  author = {Fossen, Thor I.},
  title = {Handbook of Marine Craft Hydrodynamics and Motion Control},
  edition = {2nd},
  publisher = {John Wiley & Sons},
  address = {Chichester, UK},
  year = {2021}
}

@online{px4_uuv2024,
  author = {{PX4 Development Team}},
  title = {Submarines (Unmanned Underwater Vehicles—UUV)},
  year = {2024},
  urldate = {2026-10-10},
  url = {https://docs.px4.io/main/en/frames_sub/index}
}

@article{fossen1995nonlinear,
  author = {Fossen, Thor I.},
  title = {Nonlinear modelling of marine vehicles in 6 degrees of freedom},
  journal = {Mathematical Modelling of Systems},
  volume = {1},
  number = {1},
  pages = {17--27},
  year = {1995}
}

@book{yan2020underwater,
  author = {严卫生 and 高剑 and 崔荣鑫 and others},
  title = {水下航行器控制技术},
  publisher = {国防工业出版社},
  address = {北京},
  year = {2020}
}

@phdthesis{prestero2001verification,
  author = {Prestero, Timothy},
  title = {Verification of a six-degree of freedom simulation model for the REMUS autonomous underwater vehicle},
  school = {Massachusetts Institute of Technology},
  address = {Cambridge, MA},
  year = {2001}
}

@article{caccia2000modeling,
  author = {Caccia, Massimo and Indiveri, Giovanni and Veruggio, Gianmarco},
  title = {Modeling and identification of open-frame variable configuration unmanned underwater vehicles},
  journal = {IEEE Journal of Oceanic Engineering},
  volume = {25},
  number = {2},
  pages = {227--240},
  year = {2000}
}

@article{smallwood2004model,
  author = {Smallwood, David A. and Whitcomb, Louis L.},
  title = {Model-based dynamic positioning of underwater robotic vehicles: Theory and experiment},
  journal = {IEEE Journal of Oceanic Engineering},
  volume = {29},
  number = {1},
  pages = {169--186},
  year = {2004}
}

@article{vonbenzon2022open,
  author = {von Benzon, M. and S{\o}rensen, F. F. and Uth, E. and others},
  title = {An open-source benchmark simulator: Control of a {BlueROV2} underwater robot},
  journal = {Journal of Marine Science and Engineering},
  volume = {10},
  number = {12},
  pages = {1898},
  year = {2022}
}

@article{gao2019hydrodynamic,
  author = {高婷 and 庞永杰 and 王亚兴 and others},
  title = {水下航行器水动力系数计算方法},
  journal = {哈尔滨工程大学学报},
  volume = {40},
  number = {1},
  pages = {174--180},
  year = {2019}
}

@inproceedings{chin2012modeling,
  author = {Chin, Cheng Siong and Lau, Michael Wai Shing},
  title = {Modeling and testing of hydrodynamic damping for a complex-shaped underwater robot operating at low speed},
  booktitle = {2012 Oceans - Yeosu},
  address = {Yeosu, Korea},
  publisher = {IEEE},
  pages = {1--7},
  year = {2012}
}

@inproceedings{ross2004identification,
  author = {Ross, A. and Fossen, T. I. and Johansen, T. A.},
  title = {Identification of underwater vehicle hydrodynamic coefficients using free decay tests},
  booktitle = {IFAC Conference on Control Applications in Marine Systems},
  address = {Ancona, Italy},
  publisher = {IFAC},
  pages = {363--368},
  year = {2004}
}

@inproceedings{avila2013experimental,
  author = {Avila, J. P. J. and Adamowski, J. C.},
  title = {Experimental model identification of open-frame unmanned underwater vehicles},
  booktitle = {2013 Oceans - San Diego},
  address = {San Diego, CA},
  publisher = {IEEE},
  pages = {1--7},
  year = {2013}
}

@article{harris2023stable,
  author = {Harris, Z. J. and Mao, A. M. and Paine, T. M. and others},
  title = {Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models for underactuated vehicles: Theory and experimental evaluation},
  journal = {The International Journal of Robotics Research},
  volume = {42},
  number = {12},
  pages = {1070--1093},
  year = {2023}
}

@article{brunton2016discovering,
  author = {Brunton, Steven L. and Proctor, Joshua L. and Kutz, J. Nathan},
  title = {Discovering governing equations from data by sparse identification of nonlinear dynamical systems},
  journal = {Proceedings of the National Academy of Sciences},
  volume = {113},
  number = {15},
  pages = {3932--3937},
  year = {2016}
}

@article{raissi2019physics,
  author = {Raissi, Maziar and Perdikaris, Paris and Karniadakis, George E.},
  title = {Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations},
  journal = {Journal of Computational Physics},
  volume = {378},
  pages = {686--707},
  year = {2019}
}

@inproceedings{chen2018neural,
  author = {Chen, Ricky T. Q. and Rubanova, Yulia and Bettencourt, Jesse and others},
  title = {Neural ordinary differential equations},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS 2018)},
  address = {Montr{\'e}al, QC, Canada},
  pages = {6571--6583},
  year = {2018}
}

@article{liu2026koopman,
  author = {Liu, A. and Zhang, X. and Xiao, F. and others},
  title = {Koopman-based online identification with {Sim2Real} transfer for hydrodynamic modeling of turtle-inspired robot},
  journal = {IEEE Robotics and Automation Letters},
  volume = {11},
  number = {6},
  pages = {6632--6639},
  year = {2026}
}

@article{yuh2000design,
  author = {Yuh, J.},
  title = {Design and control of autonomous underwater robots: A survey},
  journal = {Autonomous Robots},
  volume = {8},
  number = {1},
  pages = {7--24},
  year = {2000}
}

@article{zhu2012survey,
  author = {朱大奇 and 孙兵},
  title = {水下机器人运动控制研究进展},
  journal = {控制与决策},
  volume = {27},
  number = {3},
  pages = {321--333},
  year = {2012}
}

@article{yoerger1985robust,
  author = {Yoerger, Dana R. and Slotine, Jean-Jacques E.},
  title = {Robust trajectory control of underwater vehicles},
  journal = {IEEE Journal of Oceanic Engineering},
  volume = {10},
  number = {4},
  pages = {462--470},
  year = {1985}
}

@article{healey1993multivariable,
  author = {Healey, Anthony J. and Lienard, David},
  title = {Multivariable sliding mode control for autonomous diving and steering of unmanned underwater vehicles},
  journal = {IEEE Journal of Oceanic Engineering},
  volume = {18},
  number = {3},
  pages = {327--339},
  year = {1993}
}

@article{chu2020adaptive,
  author = {Chu, Zhenzhong and Xiang, Xianbo and Zhu, Daxin and others},
  title = {Adaptive trajectory tracking control for remotely operated vehicles considering thruster dynamics and saturation constraints},
  journal = {ISA Transactions},
  volume = {100},
  pages = {28--37},
  year = {2020}
}

@article{zhang2018survey,
  author = {张磊 and 严卫生 and 付明玉},
  title = {自主水下航行器模型预测控制研究现状与展望},
  journal = {控制理论与应用},
  volume = {35},
  number = {9},
  pages = {1181--1192},
  year = {2018}
}

@inproceedings{heshmati2018robust,
  author = {Heshmati-Alamdari, S. and Karras, G. C. and Marantos, P. and others},
  title = {A robust model predictive control approach for autonomous underwater vehicles operating in a constrained workspace},
  booktitle = {2018 IEEE International Conference on Robotics and Automation (ICRA)},
  address = {Brisbane, QLD, Australia},
  publisher = {IEEE},
  pages = {6183--6188},
  year = {2018}
}

@article{heshmati2020robust,
  author = {Heshmati-Alamdari, S. and Nikou, A. and Dimarogonas, D. V.},
  title = {Robust trajectory tracking control for underactuated autonomous underwater vehicles in uncertain environments},
  journal = {IEEE Transactions on Automation Science and Engineering},
  volume = {18},
  number = {3},
  pages = {1288--1301},
  year = {2020}
}

@article{johansen2013control,
  author = {Johansen, Tor Arne and Fossen, Thor I.},
  title = {Control allocation: A survey},
  journal = {Automatica},
  volume = {49},
  number = {5},
  pages = {1087--1103},
  year = {2013}
}

@article{bodson2002evaluation,
  author = {Bodson, Marc},
  title = {Evaluation of optimization methods for control allocation},
  journal = {Journal of Guidance, Control, and Dynamics},
  volume = {25},
  number = {4},
  pages = {703--711},
  year = {2002}
}

@article{harkegard2002efficient,
  author = {H{\"a}rkeg{\aa}rd, Ola},
  title = {Efficient active set algorithms for solving constrained linear quadratic control allocation problems},
  journal = {Journal of Guidance, Control, and Dynamics},
  volume = {25},
  number = {5},
  pages = {827--835},
  year = {2002}
}

@article{cheng2022thrust,
  author = {程卫平 and 王猛 and 曾现敏 and others},
  title = {基于可行方向法的水下机器人推力分配},
  journal = {舰船科学技术},
  volume = {44},
  number = {13},
  pages = {102--106},
  year = {2022}
}

@article{sun2023thrust,
  author = {孙功武 and 苏义鑫 and 毛英 and others},
  title = {基于模糊逻辑的混合推进ROV多级推力分配策略},
  journal = {机器人},
  volume = {45},
  number = {4},
  pages = {472--482},
  year = {2023}
}

@inproceedings{li2025mce,
  author = {Li, J. H. and Lee, M. J. and Kim, M. G. and others},
  title = {{MCE}-based direct {FTC} method for dynamic positioning of underwater vehicles with thruster redundancy},
  booktitle = {2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  address = {Hangzhou, China},
  publisher = {IEEE},
  pages = {1542--1549},
  doi = {10.1109/IROS60139.2025.11246250},
  year = {2025}
}

@inproceedings{meier2015px4,
  author = {Meier, Lorenz and Honegger, Dominik and Pollefeys, Marc},
  title = {{PX4}: A node-based multithreaded open source robotics framework for deeply embedded platforms},
  booktitle = {2015 IEEE International Conference on Robotics and Automation (ICRA)},
  address = {Seattle, WA, USA},
  publisher = {IEEE},
  pages = {6235--6240},
  year = {2015}
}

@online{px4_control_allocation,
  author = {{PX4 Development Team}},
  title = {Control Allocation (Mixing)},
  year = {2026},
  urldate = {2026-10-10},
  url = {https://docs.px4.io/main/en/concept/control_allocation}
}

@online{px4_bluerov2,
  author = {{PX4 Development Team}},
  title = {BlueROV2 (UUV)},
  year = {2026},
  urldate = {2026-10-10},
  url = {https://docs.px4.io/main/en/frames_sub/bluerov2}
}

@online{px4_offboard,
  author = {{PX4 Development Team}},
  title = {Offboard Mode (Generic/All Frames)},
  year = {2026},
  urldate = {2026-10-10},
  url = {https://docs.px4.io/main/en/flight_modes/offboard}
}
"""
    with open(bib_path, "w", encoding="utf-8") as f:
        f.write(bib_entries.strip() + "\n")

    # 写入规范的 references.ris
    ris_lines = []
    for ref_str in REFS_37:
        m = re.match(r"^\[(\d+)\]\s+(.*)", ref_str)
        if not m:
            continue
        num = m.group(1)
        body = m.group(2)
        ris_lines.append("TY  - GEN")
        ris_lines.append(f"ID  - ref{num}")
        ris_lines.append(f"M1  - [{num}]")
        ris_lines.append(f"TI  - {body}")
        ris_lines.append("ER  -\n")

    with open(ris_path, "w", encoding="utf-8") as f:
        f.write("\n".join(ris_lines))
    print(">>> [4/5] 已同步更新《references.bib》与《references.ris》为37篇权威文献库。")

def archive_files():
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    files_to_archive = [
        "02_PX4第一节_修改后净稿.docx",
        "PX4_第一节_修改后净稿_交付版.docx",
        "PX4_研究现状_修改后净稿.docx",
        "PX4_研究现状_黄色修订及删除线对照版.docx",
        "PX4_第二部分_评估对比与逐项修改说明.docx",
        "update_opening_report_refs.py",
        "build_bib_and_ris_45.py",
        "execute_all_updates.py",
        "V5_1.1.txt",
        "郑祺耀_1.1.txt"
    ]

    for fname in os.listdir(BASE_DIR):
        if fname.startswith("scratch_") and fname.endswith(".txt"):
            files_to_archive.append(fname)

    moved = 0
    for fname in files_to_archive:
        src = os.path.join(BASE_DIR, fname)
        if os.path.exists(src):
            dst = os.path.join(ARCHIVE_DIR, fname)
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(src, dst)
            moved += 1
            print(f"  归档移出: {fname}")

    print(f">>> [5/5] 历史过程文件已全部移入 archive 目录，主目录清理完毕。")

if __name__ == "__main__":
    print("=" * 70)
    print("启动最终开题报告规范重构与归档工作流...")
    print("=" * 70)
    rebuild_markdown()
    update_builder_script()
    run_build_pipeline()
    update_bib_and_ris()
    archive_files()
    print("=" * 70)
    print("全部操作圆满完成！")
    print("=" * 70)
