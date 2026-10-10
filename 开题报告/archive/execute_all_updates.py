# -*- coding: utf-8 -*-
"""
执行全部更新任务脚本：
1. 采用修订后研究现状（2.4先维持修订净稿的问题链收束，不展开具体算法细节）；
2. 连续重排正文引用与参考文献，由原先的不连续编号更新为纯连续的 [1]~[37]；
   纠正原 [42]（现 [33]）会议地点为 Hangzhou, China 并补充 DOI 与页码；
3. 将进度安排内容置空（移去原有进度安排表及矛盾文本，仅保留“（待后续阶段撰写）”）；
4. 同步更新 开题报告_正文起草稿.md、build_opening_report_docx.py、references.bib、references.ris；
5. 调用构建脚本重新生成最终主文档《开题报告-基于PX4的水下航行器模型控制方法研究.docx》并执行合规审查；
6. 将历史与过程文件移入 archive 目录。
"""

import os
import sys
import shutil
import re
import docx

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"D:\tj\Graduation Project\开题报告"
ARCHIVE_DIR = os.path.join(BASE_DIR, "archive")

# 37 篇最新完整参考文献 (GB/T 7714 顺序编码制，严格按正文首次出现顺序编号)
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

# 旧编号到新连续编号映射
OLD_TO_NEW = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 45: 10,
    10: 11, 11: 12, 12: 13, 13: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19,
    20: 20, 21: 21, 23: 22, 24: 23, 25: 24, 29: 25, 30: 26, 31: 27,
    37: 28, 38: 29, 39: 30, 40: 31, 41: 32, 42: 33, 43: 34, 46: 35, 47: 36, 48: 37
}

def update_citations(text):
    def repl(m):
        content = m.group(1)
        if '-' in content or '–' in content:
            parts = re.split(r'[-–]', content)
            start = OLD_TO_NEW[int(parts[0])]
            end = OLD_TO_NEW[int(parts[1])]
            return f'[{start}-{end}]'
        else:
            old_num = int(content)
            new_num = OLD_TO_NEW[old_num]
            return f'[{new_num}]'
    return re.sub(r'\[(\d+(?:[–\-]\d+)?)\]', repl, text)

# 1. 生成并更新 开题报告_正文起草稿.md
def step1_update_markdown():
    clean_docx = docx.Document(os.path.join(BASE_DIR, "PX4_研究现状_修订净稿_保留模板.docx"))
    
    # 提取修订净稿中的第2部分内容
    sec2_lines = []
    for i in range(22, 48):
        p = clean_docx.paragraphs[i]
        t = p.text.strip()
        if not t:
            continue
        if t.startswith("2．") or t.startswith("2."):
            continue
        elif t.startswith("2.1 ") or t.startswith("2.2 ") or t.startswith("2.3 ") or t.startswith("2.4 "):
            sec2_lines.append(f"#### {t}\n")
        else:
            new_t = update_citations(t)
            sec2_lines.append(f"{new_t}\n")

    md_path = os.path.join(BASE_DIR, "开题报告_正文起草稿.md")
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # 读取第1部分
    header_part = md_text.split("### 2． 国内外在该方向的研究现状和发展趋势")[0]
    
    # 构造新的 Section 2
    new_sec2_text = "### 2． 国内外在该方向的研究现状和发展趋势\n\n" + "\n".join(sec2_lines) + "\n"

    # 构造新的 Section 3（进度安排置空）
    new_sec3_text = (
        "## 二、毕业设计（论文）方案介绍\n\n"
        "### 1． 主要研究内容\n\n"
        "（待后续阶段撰写）\n\n"
        "### 2． 研究方案\n\n"
        "（待后续阶段撰写）\n\n"
        "### 3． 进度安排\n\n"
        "（待后续阶段撰写）\n\n"
    )

    # 构造新的 Section 4（37篇参考文献）
    new_sec4_text = "## 三、毕业设计（论文）的主要参考文献\n\n" + "\n\n".join(REFS_37) + "\n\n"

    # 保留审核意见部分
    tail_part = "## 四、审核意见\n\n" + md_text.split("## 四、审核意见")[1]

    full_new_md = header_part + new_sec2_text + new_sec3_text + new_sec4_text + tail_part
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(full_new_md)
    print(">>> [1/5] 已成功更新《开题报告_正文起草稿.md》：第2部分净稿接入、参考文献37篇连续重排、进度安排置空。")

# 2. 更新 build_opening_report_docx.py
def step2_update_builder_script():
    builder_path = os.path.join(BASE_DIR, "build_opening_report_docx.py")
    with open(builder_path, "r", encoding="utf-8") as f:
        code = f.read()

    # 注释掉 insert_progress_table(p29, doc)
    code = code.replace("insert_progress_table(p29, doc)", "# insert_progress_table(p29, doc)  # 进度安排置空")

    # 更新 audit 中的文献数量断言由 45 篇改为 37 篇
    code = re.sub(r"t\.startswith\('\[45\]'\)", "t.startswith('[37]')", code)
    code = code.replace("45 篇参考文献", "37 篇参考文献")
    code = code.replace("45篇参考文献", "37篇参考文献")
    code = code.replace("45篇", "37篇")
    code = code.replace("45 篇", "37 篇")

    # 在 audit 中移除 Table 2 进度安排的必要性断言
    code = code.replace("assert not sec2_leaks, f\"Section 2 漏/泄露到可编辑区外: {sec2_leaks}\"",
                        "# sec2_leaks checked\n    assert not sec2_leaks, f\"Section 2 漏/泄露到可编辑区外: {sec2_leaks}\"")

    with open(builder_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(">>> [2/5] 已成功更新《build_opening_report_docx.py》构建逻辑与审计断言。")

# 3. 运行 build_opening_report_docx.py 重新生成主报告 docx
def step3_run_build():
    import subprocess
    cmd = [sys.executable, os.path.join(BASE_DIR, "build_opening_report_docx.py")]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=r"D:\tj\Graduation Project", encoding="utf-8", errors="replace")
    print(res.stdout)
    if res.returncode != 0:
        print("STDERR:", res.stderr)
        raise RuntimeError("构建脚本执行失败！")
    print(">>> [3/5] 主文档《开题报告-基于PX4的水下航行器模型控制方法研究.docx》重新构建成功，通过全部格式与权限审计！")

# 4. 更新 references.bib 与 references.ris
def step4_update_bib_and_ris():
    # 生成 references.bib
    bib_path = os.path.join(BASE_DIR, "references.bib")
    ris_path = os.path.join(BASE_DIR, "references.ris")

    # 37 篇 BibTeX 数据库
    bib_entries = """% 37 篇参考文献 BibTeX 数据库 (严格按照 GB/T 7714 顺序 [1]~[37] 编号)

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

    # 简单生成 RIS 格式
    ris_content = []
    for ref_str in REFS_37:
        m = re.match(r"^\[(\d+)\]\s+(.*)", ref_str)
        if not m:
            continue
        num = m.group(1)
        body = m.group(2)
        ris_content.append("TY  - GEN")
        ris_content.append(f"ID  - ref{num}")
        ris_content.append(f"M1  - [{num}]")
        ris_content.append(f"TI  - {body}")
        ris_content.append("ER  -\n")

    with open(ris_path, "w", encoding="utf-8") as f:
        f.write("\n".join(ris_content))

    print(">>> [4/5] 已成功同步更新《references.bib》与《references.ris》（37篇文献数据库）。")

# 5. 将历史过程文件移出至 archive 目录
def step5_archive_historical_files():
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    files_to_archive = [
        "02_PX4第一节_修改后净稿.docx",
        "PX4_第一节_修改后净稿_交付版.docx",
        "PX4_研究现状_修改后净稿.docx",
        "PX4_研究现状_黄色修订及删除线对照版.docx",
        "PX4_第二部分_评估对比与逐项修改说明.docx",
        "开题报告-基于PX4的水下航行器模型控制方法研究.docx.bak",
        "update_opening_report_refs.py",
        "build_bib_and_ris_45.py",
        "V5_1.1.txt",
        "郑祺耀_1.1.txt"
    ]

    # 也包括所有 scratch_*.txt 临时文件
    for fname in os.listdir(BASE_DIR):
        if fname.startswith("scratch_") and fname.endswith(".txt"):
            files_to_archive.append(fname)

    moved_count = 0
    for fname in files_to_archive:
        src = os.path.join(BASE_DIR, fname)
        if os.path.exists(src):
            dst = os.path.join(ARCHIVE_DIR, fname)
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(src, dst)
            moved_count += 1
            print(f"  已移入归档: {fname} -> archive/")

    print(f">>> [5/5] 历史过程文件归档完毕，共移出 {moved_count} 个历史文件。")

if __name__ == "__main__":
    print("=" * 70)
    print("开始执行全套更新任务...")
    print("=" * 70)
    step1_update_markdown()
    step2_update_builder_script()
    step3_run_build()
    step4_update_bib_and_ris()
    step5_archive_historical_files()
    print("=" * 70)
    print("全部更新任务顺利完成！")
    print("=" * 70)
