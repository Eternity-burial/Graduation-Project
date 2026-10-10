# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

# 45 篇参考文献题录
REFERENCES_TEXT = [
    "[1] 中华人民共和国工业和信息化部, 国家发展和改革委员会, 科学技术部, 等. “十四五”机器人产业发展规划[J]. 中华人民共和国工业和信息化部公报, 2021(12): 20-27.",
    "[2] 工业和信息化部, 教育部, 科学技术部, 等. “机器人+”应用行动实施方案[J]. 中华人民共和国工业和信息化部公报, 2023(1): 18-24.",
    "[3] FOSSEN T I. Handbook of Marine Craft Hydrodynamics and Motion Control[M]. 2nd ed. Chichester, UK: John Wiley & Sons, 2021.",
    "[4] FERNANDES D, SØRENSEN D, PETTERSEN K Y, et al. Output-feedback motion control of an underwater vehicle-manipulator system[J]. Control Engineering Practice, 2015, 39: 50-64.",
    "[5] VON BENZON M, SØRENSEN F F, UTH E, et al. An open-source benchmark simulator: Control of a BlueROV2 underwater robot[J]. Journal of Marine Science and Engineering, 2022, 10(12): 1898.",
    "[6] DUECKER D A, BAUSCHMANN N, HANSEN T, et al. HippoCampus X: A hydrobatic open-source micro AUV for confined environments[C]//2020 IEEE/OES Autonomous Underwater Vehicles Symposium (AUV). St. John's, NL, Canada: IEEE, 2020: 1-6.",
    "[7] JOHANSEN T A, FOSSEN T I. Control allocation: A survey[J]. Automatica, 2013, 49(5): 1087-1103.",
    "[8] MEIER L, HONEGGER D, POLLEFEYS M. PX4: A node-based multithreaded open source robotics framework for deeply embedded platforms[C]//2015 IEEE International Conference on Robotics and Automation (ICRA). Seattle, WA, USA: IEEE, 2015: 6235-6240.",
    "[9] SMALLWOOD D A, WHITCOMB L L. Model-based dynamic positioning of underwater robotic vehicles: Theory and experiment[J]. IEEE Journal of Oceanic Engineering, 2004, 29(1): 169-186.",
    "[10] FOSSEN T I. Nonlinear modelling of marine vehicles in 6 degrees of freedom[J]. Mathematical Modelling of Systems, 1995, 1(1): 17-27.",
    "[11] 严卫生, 高剑, 崔荣鑫, 等. 水下航行器控制技术[M]. 北京: 国防工业出版社, 2020.",
    "[12] PRESTERO T. Verification of a six-degree of freedom simulation model for the REMUS autonomous underwater vehicle[D]. Cambridge, MA: Massachusetts Institute of Technology, 2001.",
    "[13] 高婷, 庞永杰, 王亚兴, 等. 水下航行器水动力系数计算方法[J]. 哈尔滨工程大学学报, 2019, 40(1): 174-180.",
    "[14] CACCIA M, INDIVERI G, VERUGGIO G. Modeling and identification of open-frame variable configuration unmanned underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 2000, 25(2): 227-240.",
    "[15] CHIN C, LAU M. Modeling and testing of hydrodynamic damping model for a complex-shaped remotely-operated vehicle for control[J]. Journal of Marine Science and Application, 2012, 11(2): 150-163.",
    "[16] ROSS A, FOSSEN T I, JOHANSEN T A. Identification of underwater vehicle hydrodynamic coefficients using free decay tests[J]. IFAC Proceedings Volumes, 2004, 37(10): 363-368.",
    "[17] AVILA J P J, DONHA D C, ADAMOWSKI J C. Experimental model identification of open-frame underwater vehicles[J]. Ocean Engineering, 2013, 60: 81-94.",
    "[18] PARK S, SUNG S, CHOI H. System identification method for robotic manipulator based on dynamic momentum regressor[J]. IEEE Transactions on Instrumentation and Measurement, 2016, 65(9): 2085-2095.",
    "[19] HARRIS M, MAURYA P. Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models[J]. IEEE Transactions on Control Systems Technology, 2023, 31(6): 2816-2823.",
    "[20] RAISSI M, PERDIKARIS P, KARNIADAKIS G E. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations[J]. Journal of Computational Physics, 2019, 378: 686-707.",
    "[21] BRUNTON S L, PROCTOR J L, KUTZ J N. Discovering governing equations from data by sparse identification of nonlinear dynamical systems[J]. Proceedings of the National Academy of Sciences, 2016, 113(15): 3932-3937.",
    "[22] CHEN R T Q, RUBANOVA Y, BETTENCOURT J, et al. Neural ordinary differential equations[C]//Advances in Neural Information Processing Systems (NeurIPS 2018). Montréal, QC, Canada, 2018: 6571-6583.",
    "[23] DUONG T, ATANASOV N. Port-Hamiltonian neural ODE networks on Lie groups for robot dynamics learning and control[J]. IEEE Transactions on Robotics, 2024, 40: 1215-1233.",
    "[24] YUH J. Design and control of autonomous underwater robots: A survey[J]. Autonomous Robots, 2000, 8(1): 7-24.",
    "[25] 朱大奇, 孙兵. 水下机器人运动控制研究进展[J]. 控制与决策, 2012, 27(3): 321-333.",
    "[26] CAPOCCI R, DRONIOU N, BOYER F, et al. Inspection-class remotely operated vehicles: A review[J]. Journal of Marine Science and Engineering, 2017, 5(1): 13.",
    "[27] YOERGER D R, SLOTINE J J E. Robust trajectory control of underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 1985, 10(4): 462-470.",
    "[28] HEALEY A J, LIENARD D. Multivariable sliding mode control for autonomous diving and steering of unmanned underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 1993, 18(3): 327-339.",
    "[29] CHU Z, XIANG X, ZHU D, et al. Adaptive trajectory tracking control for remotely operated vehicles considering thruster dynamics and saturation constraints[J]. ISA Transactions, 2020, 100: 28-37.",
    "[30] 钱辰, 方勇纯. 面向扑翼飞行控制的建模与奇异摄动分析[J]. 自动化学报, 2020, 46(12): 2585-2595.",
    "[31] SMEUR E J J, CHU Q P, DE CROON G C H E. Adaptive incremental nonlinear dynamic inversion for attitude control of micro air vehicles[J]. Journal of Guidance, Control, and Dynamics, 2016, 39(3): 450-461.",
    "[32] SLAWIK T, VYAS S, CHRISTENSEN L, et al. Attitude control of the hydrobatic intervention AUV Cuttlefish using incremental nonlinear dynamic inversion[C]//2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). Abu Dhabi, UAE: IEEE, 2024: 781-787.",
    "[33] HESHMATI-ALAMDARI S, NIKOU A, DIMAROGONAS D V. Robust trajectory tracking control for underactuated autonomous underwater vehicles in presence of current disturbances[J]. IEEE Transactions on Automation Science and Engineering, 2020, 18(3): 1292-1306.",
    "[34] LINIGER A, DOMAHOIDI A, MORARI M. Optimization-based autonomous racing of 1:43 scale RC cars[J]. Optimal Control Applications and Methods, 2015, 36(5): 628-647.",
    "[35] TORRENTE G, KAUFMANN E, FÖHN P, et al. Data-driven MPC for quadrotors[J]. IEEE Robotics and Automation Letters, 2021, 6(2): 3769-3776.",
    "[36] SHI G, HÖNIG W, YUE Y, et al. Neural-Lander: Stable drone landing in ground effect with learning-based dynamics[C]//2019 International Conference on Robotics and Automation (ICRA). Montreal, QC, Canada: IEEE, 2019: 9811-9818.",
    "[37] O'CONNELL M, SHI G, SHI X, et al. Neural-Fly enables rapid learning for agile flight in strong winds[J]. Science Robotics, 2022, 7(66): eabg6513.",
    "[38] BODSON M. Evaluation of optimization methods for control allocation[J]. Journal of Guidance, Control, and Dynamics, 2002, 25(4): 703-711.",
    "[39] HÄRKEGÅRD O. Efficient active set algorithms for solving constrained linear quadratic control allocation problems[J]. Journal of Guidance, Control, and Dynamics, 2002, 25(5): 827-835.",
    "[40] 程卫平, 王猛, 曾现敏, 等. 基于可行方向法的水下机器人推力分配[J]. 舰船科学技术, 2022, 44(13): 102-106.",
    "[41] 孙功武, 苏义鑫, 毛英, 等. 基于模糊逻辑的混合推进ROV多级推力分配策略[J]. 机器人, 2023, 45(4): 472-482.",
    "[42] LI Y, ZHANG M, CHEN Y, et al. MCE-based direct FTC method for underwater vehicles with thruster redundancy[J]. Ocean Engineering, 2025, 317: 119985.",
    "[43] BRUNKE L, GREEFF M, HALL A W, et al. Safe learning in robotics: From learning-based control to safe reinforcement learning[J]. Annual Review of Control, Robotics, and Autonomous Systems, 2022, 5: 411-444.",
    "[44] ZHAO Y, PENG X, WU J, et al. Spatiotemporal calibration of Doppler velocity logs for underwater robots[J]. arXiv preprint arXiv:2510.24571, 2025.",
    "[45] PENG X, ZHAO Y, WU J, et al. AquaticVision: Benchmarking visual SLAM in underwater environment with events and frames[C]//2025 IEEE International Conference on Robotics and Automation (ICRA). Atlanta, GA, USA: IEEE, 2025: 1-7."
]

def main():
    draft_path = "开题报告/开题报告_正文起草稿.md"
    with open(draft_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 替换 §2.1 段落
    # 替换第 19 行（Fossen 建模体系 -> 补充严卫生 [11] 与 Prestero [12]）
    target_p19 = "在海洋工程与水下机器人领域，挪威学者 Fossen$^{[3]}$ 基于牛顿-欧拉方程与流体势流理论构建的非线性动力学统一建模体系，已成为学术界与工业界广泛遵循的经典范式$^{[10]}$。该体系将航行器六自由度空间运动解耦为附体坐标系下的速度矢量与惯性坐标系下的位姿矢量，完整刻画了刚体质量惯性、水动力附加质量、科氏力与向心力、流体阻尼以及重浮力恢复力矩等动力学分量。"
    replace_p19 = "在海洋工程与水下机器人领域，挪威学者 Fossen$^{[3]}$ 基于牛顿-欧拉方程与流体势流理论构建的非线性动力学统一建模体系，已成为学术界与工业界广泛遵循的经典范式$^{[10]}$；严卫生等人$^{[11]}$ 进一步针对复杂水下航行器系统给出了六自由度空间运动学与刚体-流体动力学的系统化分析方法。该体系将航行器空间运动解耦为附体坐标系下的速度矢量与惯性坐标系下的位姿矢量，完整刻画了刚体质量惯性、水动力附加质量、科氏力与向心力、流体阻尼以及重浮力恢复力矩等动力学分量；Prestero$^{[12]}$ 则基于该机理体系完成了 REMUS 航行器六自由度动力学模型的全维度试验标定与仿真验证，建立了水下小型航行器机理参数测算与模型校验的公认基准。"
    assert target_p19 in content, "target_p19 not found"
    content = content.replace(target_p19, replace_p19)

    # 替换原 [11] -> [13]
    assert "$^{[11]}$" in content
    content = content.replace("在缺乏实体物理样机的前期设计阶段具有重要参考价值$^{[11]}$", "在缺乏实体物理样机的前期设计阶段具有重要参考价值$^{[13]}$")

    # 替换原 [12]~[15] -> [14]~[17]
    assert "Caccia 等人$^{[12]}$" in content
    content = content.replace("Caccia 等人$^{[12]}$", "Caccia 等人$^{[14]}$")
    content = content.replace("Chin 与 Lau$^{[13]}$", "Chin 与 Lau$^{[15]}$")
    content = content.replace("Ross 等人$^{[14]}$", "Ross 等人$^{[16]}$")
    content = content.replace("Avila 等人$^{[15]}$", "Avila 等人$^{[17]}$")

    # 替换原 [16]~[19] -> [18]~[21]，并补充 [22] Neural ODE 与 [23] PH-NODE
    content = content.replace("Park 等人$^{[16]}$", "Park 等人$^{[18]}$")
    content = content.replace("Harris 等人$^{[17]}$", "Harris 等人$^{[19]}$")
    
    target_p25_tail = "此外，物理信息神经网络（PINN）$^{[18]}$ 与动态系统稀疏辨识（SINDy）$^{[19]}$ 等将先验物理定律与数据驱动相结合的非线性辨识方法也展现了良好潜力，但在小型嵌入式系统上的模型泛化性与训练开销仍待进一步验证。"
    replace_p25_tail = "此外，物理信息神经网络（PINN）$^{[20]}$ 与动态系统稀疏辨识（SINDy）$^{[21]}$ 等将先验物理定律与数据驱动相结合的非线性辨识方法展现了良好潜力；Chen 等人$^{[22]}$ 提出的神经常微分方程（Neural ODE）通过将残差动力学映射为连续时间状态演化，为复杂时变动态的连续辨识开辟了新途径；Duong 与 Atanasov$^{[23]}$ 则进一步将李群几何与能量守恒定律引入连续神经网络，提出了面向海洋航行器的端口哈密顿神经微分方程（PH-NODE），在保持物理系统能量守恒的前提下实现了流体阻尼与强耦合动力学的高保真学习。然而，纯数据驱动与深度学习辨识方法高度依赖大规模高质量训练样本，且复杂的网络结构在小型嵌入式系统上的模型泛化性与在线推断开销仍面临显著挑战。"
    assert target_p25_tail in content, "target_p25_tail not found"
    content = content.replace(target_p25_tail, replace_p25_tail)

    # 2. 替换 §2.2 段落
    # 替换原 [20] -> [24] 并补充朱大奇 [25]
    target_p31 = "是水下机器人控制领域长盛不衰的研究热点$^{[20]}$。经过数十年的演进，国内外学者围绕海洋航行器运动控制与动态补偿形成了清晰的理论与技术脉络"
    replace_p31 = "是水下机器人控制领域长盛不衰的研究热点$^{[24]}$；朱大奇与孙兵$^{[25]}$ 对水下机器人运动控制技术的演进脉络与典型控制架构进行了系统综述。经过数十年的演进，国内外学者围绕海洋航行器运动控制与动态补偿形成了清晰的理论与技术脉络"
    assert target_p31 in content, "target_p31 not found"
    content = content.replace(target_p31, replace_p31)

    # 替换原 [21] -> [26]
    content = content.replace("巡检级遥控航行器（ROV）广泛采用的底层基准方案$^{[21]}$", "巡检级遥控航行器（ROV）广泛采用的底层基准方案$^{[26]}$")

    # 替换原 [22]~[23] -> [27]~[28]，并补充 [29] Chu 2020
    content = content.replace("Yoerger 与 Slotine$^{[22]}$", "Yoerger 与 Slotine$^{[27]}$")
    content = content.replace("Healey 与 Lienard$^{[23]}$", "Healey 与 Lienard$^{[28]}$")
    target_p35_tail = "加剧机械磨损与电池能量损耗。"
    replace_p35_tail = "加剧机械磨损与电池能量损耗；为此，Chu 等人$^{[29]}$ 针对未知海流扰动与推进器推力饱和双重受限工况，提出了带高增益状态观测器的自适应积分端点滑模控制方案，有效改善了多轴饱和受限下的抗扰跟踪性能，但其观测器增益自适应调节规律依然较为复杂。"
    assert target_p35_tail in content, "target_p35_tail not found"
    content = content.replace(target_p35_tail, replace_p35_tail)

    # 替换原 [24] -> [30] 反步法
    content = content.replace("反步控制（Backstepping）方法在 20 世纪 90 年代后得到系统研究$^{[24]}$", "反步控制（Backstepping）方法在 20 世纪 90 年代后得到系统研究$^{[30]}$")

    # 替换原 [25]~[26] -> [31]~[32] INDI
    content = content.replace("Smeur 等人$^{[25]}$ 奠定了增量动态逆", "Smeur 等人$^{[31]}$ 奠定了增量动态逆")
    content = content.replace("Slawik 等人$^{[26]}$ 则将其进一步拓展", "Slawik 等人$^{[32]}$ 则将其进一步拓展")

    # 替换原 [27]~[29] -> [33]~[37]，并补充 [35] Torrente 与 [36] Shi Neural-Lander
    target_p43 = "主要包括非线性模型预测控制（NMPC）、模型预测轮廓控制（MPCC）以及数据驱动自适应控制。Heshmati 等人$^{[27]}$ 针对欠驱动水下航行器在波流扰动下的轨迹跟踪，构建了基于非线性状态观测的鲁棒 NMPC 框架；Liniger 等人$^{[28]}$ 建立了考虑轮廓误差的预测优化模型；加州理工学院团队提出的 Neural-Fly 架构$^{[29]}$ 则展示了深度神经网络在线自适应抵御非定常强流扰动的潜力。该类算法能够在有限预测时域内显式处理推进器推力饱和与变化速率等物理约束，控制性能上限极高；然而，在线滚动优化通常需要在每个控制周期内执行密集的多重矩阵迭代求解，其巨大的计算与内存开销超出了常规低功耗微控制器的硬件承受范围。"
    replace_p43 = "主要包括非线性模型预测控制（NMPC）、模型预测轮廓控制（MPCC）以及数据驱动自适应控制。Heshmati 等人$^{[33]}$ 针对欠驱动水下航行器在波流扰动下的轨迹跟踪，构建了基于非线性状态观测的鲁棒 NMPC 框架；Liniger 等人$^{[34]}$ 建立了考虑轮廓误差的预测优化模型；Torrente 等人$^{[35]}$ 则通过实机对比系统评估了数据驱动 NMPC 与基于机理模型平坦前馈补偿的性能边界，指出在计算资源受限场景下，解析模型前馈能够在耗费极低算力的前提下达成接近预测优化的动态补偿效果；Shi 等人$^{[36]}$ 提出的 Neural-Lander 框架展示了离线学习气动流扰残差以实现复杂扰动前馈补偿的有效性；加州理工学院团队在此基础上提出的 Neural-Fly 架构$^{[37]}$ 则进一步实现了深度神经网络对非定常强风扰动的毫秒级在线自适应抵御。该类算法能够在有限预测时域内显式处理推进器推力饱和与变化速率等物理约束，控制性能上限极高；然而，在线滚动优化或深度神经网络在线推理通常需要在控制周期内执行密集的多重矩阵迭代求解，其巨大的计算与内存开销超出了常规低功耗微控制器的硬件承受范围。"
    assert target_p43 in content, "target_p43 not found"
    content = content.replace(target_p43, replace_p43)

    # 3. 替换 §2.3 段落
    # 补充 Bodson [38]
    target_p51 = "由于其求解过程仅涉及离线常数矩阵求逆与在线代数矩阵乘加，单次解算仅耗费数微秒，对计算资源受限的微控制器具有天然的适配性。然而，广义逆法本质上属于无约束线性映射"
    replace_p51 = "Bodson$^{[38]}$ 在其经典对比研究中系统评估了加权伪逆法、直接分配法与二次规划优化分配的性能特性，指出加权伪逆在无约束区域具备极高的计算效率与能耗最优性。由于其求解过程仅涉及离线常数矩阵求逆与在线代数矩阵乘加，单次解算仅耗费数微秒，对计算资源受限的微控制器具有天然的适配性。然而，广义逆法本质上属于无约束线性映射"
    assert target_p51 in content, "target_p51 not found"
    content = content.replace(target_p51, replace_p51)

    # 替换原 [30]~[31] -> [39]~[40]
    content = content.replace("Härkegård$^{[30]}$", "Härkegård$^{[39]}$")
    content = content.replace("程卫平等$^{[31]}$", "程卫平等$^{[40]}$")

    # 替换原 [32] -> [41]
    content = content.replace("关键诱因$^{[32]}$", "关键诱因$^{[41]}$")

    # 替换原 [33] -> [42]，并补充 [43] Brunke 与 [44] Zhao
    target_p57 = "从而以主动牺牲部分平移航速为代价，严格保证合成姿态力矩的方向与相对比例不发生畸变$^{[33]}$。类似地，开源飞控 PX4 在其底层控制分配模块中采用了序贯解饱和（Sequential Desaturation）逻辑，按照角速度姿态力矩、偏航力矩、垂荡推力与水平平移推力的固定优先级，在执行器饱和时自底向上逐级削减低优先级通道的控制量。这类启发式分配方法在保持解析计算极低开销的同时，有效消除了力矩方向畸变对姿态稳定性的威胁。"
    replace_p57 = "从而以主动牺牲部分平移航速为代价，严格保证合成姿态力矩的方向与相对比例不发生畸变$^{[42]}$。Brunke 等人$^{[43]}$ 在机器人安全学习与控制综述中强调，在执行器存在严格物理幅值与速率约束时，保证系统满足控制李雅普诺夫安全性屏障是防止系统倾覆失稳的先决条件；类似地，开源飞控 PX4 在其底层控制分配模块中采用了序贯解饱和（Sequential Desaturation）逻辑，按照角速度姿态力矩、偏航力矩、垂荡推力与水平平移推力的固定优先级，在执行器饱和时自底向上逐级削减低优先级通道的控制量。此外，在水下多模态感知与高频闭环反馈方面，Zhao 等人$^{[44]}$ 针对微小型紧凑水下机器人提出了无标定 IMU-DVL 时空联合标定与高频测速估计框架（UIC），为控制系统在高频内环中获取可靠的机体线速度与姿态反馈提供了高保真感知支撑。这类启发式分配方法在保持解析计算极低开销的同时，有效消除了力矩方向畸变对姿态稳定性的威胁。"
    assert target_p57 in content, "target_p57 not found"
    content = content.replace(target_p57, replace_p57)

    # 4. 替换第二大节中的复引
    content = content.replace("借鉴板载传感器试验辨识范式$^{[12]}$", "借鉴板载传感器试验辨识范式$^{[14]}$")
    content = content.replace("采用广义动量变换方法$^{[16]}$", "采用广义动量变换方法$^{[18]}$")
    content = content.replace("时域试验与动量滤波抗噪参数辨识 (Caccia 范式 [12])", "时域试验与动量滤波抗噪参数辨识 (Caccia 范式 [14])")
    content = content.replace("借鉴了 Caccia 等人建立的经典板载试验范式$^{[12]}$，结合广义动量变换$^{[16]}$", "借鉴了 Caccia 等人建立的经典板载试验范式$^{[14]}$，结合广义动量变换$^{[18]}$")

    # 在硬件与实验条件可行性处补充 [44] 与 [45]
    target_hardware = "板载供电、通信与底层驱动链路均已打通并稳定运行，为试验辨识与算法验证提供了可靠的物理载体；"
    replace_hardware = "板载供电、通信与底层驱动链路均已打通并稳定运行；课题团队前期在微小型紧凑水下机器人上开展了系统的 IMU-DVL 时空联合标定$^{[44]}$与水下多模态感知基准测试（AquaticVision）$^{[45]}$，积累了丰富的水池实机调试与传感器在环运行经验，为本课题的参数辨识与闭环控制算法验证提供了可靠的物理载体与数据支撑；"
    assert target_hardware in content, "target_hardware not found"
    content = content.replace(target_hardware, replace_hardware)

    # 5. 替换第三大节参考文献列表
    ref_block_pattern = re.compile(r"(## 三、毕业设计（论文）的主要参考文献\s*\n\s*\n)(.*?)(\n\s*---\s*\n\s*## 四、审核意见)", re.S)
    new_refs_str = "  \n".join(REFERENCES_TEXT) + "  \n"
    new_content = ref_block_pattern.sub(r"\g<1>" + new_refs_str + r"\g<3>", content)
    assert new_content != content, "ref block replacement failed"

    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Successfully updated {draft_path} with 45 references!")

if __name__ == "__main__":
    main()
