# -*- coding: utf-8 -*-
"""
生成并严格校验开题报告草稿 (45 篇参考文献与正文深度融合版)
"""
import re
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")

MD_PATH = r"开题报告/开题报告_正文起草稿.md"

SECTION_1_1 = """### 1．课题来源及研究的目的和意义

随着“海洋强国”战略的推进，水下基础设施的安全运维对小型水下航行器提出了更高要求。《“十四五”机器人产业发展规划》$^{[1]}$将水下探测、监测和作业机器人纳入特种机器人重点发展方向；《“机器人+”应用行动实施方案》$^{[2]}$提出在风电场、水电站、油气管网等能源基础设施场景推广巡检、维护等机器人应用。海上风电桩基、水下大坝立面及海底能源管线等设施在长期服役过程中，需要在近壁面、狭小空间及水流扰动等工况下开展定期巡检。相较于依赖潜水员或大型水下装备的作业方式，小型遥控水下航行器（ROV）部署更为灵活，适用于近距离精细巡检等任务。但在狭小空间和近壁水流扰动条件下，航行器还需兼顾稳定悬停、精确对位观测和低速灵活机动，对运动控制精度与稳定性提出了较高要求。

为满足上述近距离巡检中多方向运动、位姿调整与稳定悬停的需求，本课题考虑采用空间矢量布局的八推进器构型。该构型可通过推进器协同产生不同方向的合力与力矩，为航行器的六自由度运动控制提供执行机构基础。与此同时，多推进器配置也增加了动力学建模与控制分配的难度：在动力学层面，附加质量、水动力阻尼以及重心与浮心的相对位置等因素，会使航行器的平动与转动存在耦合关系$^{[3]}$；在执行机构层面，推进器受尺寸与电机功率等条件限制，存在推力幅值上限，并可能受到响应滞后、正反转死区等非理想特性的影响。在近壁水流扰动条件下，若未能协调推进器输出并合理处理推力约束，可能出现推力饱和或控制误差增大，从而影响悬停稳定性与轨迹跟踪精度。

对于多变量耦合及执行器受限的控制问题，常规比例—积分—微分（PID）控制结构简单、易于实现，但分通道PID控制若缺少耦合补偿及约束协调机制，可能难以同时兼顾多自由度控制精度与推进器推力限制。模型预测控制（MPC）基于系统动力学模型进行滚动优化，可在优化问题中显式纳入状态与推力约束，为多推进器受约束控制提供可行思路，但仍需兼顾模型精度与嵌入式计算的实时性。此外，控制算法的工程实现还需要相应的飞控软件与仿真验证环境。PX4作为开源飞控平台，已为部分水下航行器构型提供基本控制模式，但官方文档仍将其水下航行器支持列为实验性功能$^{[4]}$。因此，面向具体航行器的动力学特性及推进器约束，在PX4相关环境中开展MPC算法的适配与验证具有研究价值。

本课题立足于水下基础设施近距离巡检中精确运动控制的实际工程需求。针对水下近距离精细巡检对位姿控制精度、悬停稳定性及推力约束处理的实际需求，本课题以八推进器紧凑型水下航行器为研究对象，选用适用于控制设计的六自由度动力学模型与推进器推力分配模型，研究考虑推进器推力约束的模型预测控制（MPC）方法，并在PX4相关控制与仿真环境中开展闭环验证。本研究旨在分析水动力耦合与推力约束对航行器运动控制性能的影响，探索控制精度与实时计算开销之间的权衡。在研究层面，可为多推进器水下航行器的受约束运动控制提供方法参考；在工程层面，可为预测控制算法在PX4平台中的集成验证，以及水下基础设施近距离巡检中的运动控制应用提供技术借鉴。"""

SECTION_2 = """### 2．国内外在该方向的研究现状和发展趋势

水下基础设施的近距离精细巡检要求小型水下航行器具备空间全向机动、稳定对位悬停与抗近壁水流扰动的综合控制能力。围绕空间矢量布局八推进器水下航行器的受约束运动控制问题，国内外学者的研究主要集中于以下三个相互关联的核心维度：水下航行器动力学建模与参数辨识、多推进器受约束运动控制与推力分配、以及开源飞控平台适配与闭环仿真验证。以下分别阐述各维度的研究进展、技术路线对比与瓶颈痛点，并提炼本课题的切入点。

#### 2.1 水下航行器动力学建模与参数辨识研究现状

精确且适用的动力学模型是开展高性能模型预测控制与推力分配的物理与数学基石。水下航行器在流体介质中处于六自由度空间运动状态，呈现出显著的强非线性、大惯性水动力附加质量、时变高阶流体阻尼以及重力与浮力姿态恢复力矩等多物理效应耦合特征。围绕如何准确表征上述流体动力学特性，国内外学者开展了机理建模、物理与数值试验辨识、以及数据驱动混合建模等不同技术路径的研究。

在机理建模与动力学理论框架方面，Fossen$^{[5]}$ 奠定了海洋航行器六自由度非线性矢量统一建模的理论基石，系统规范了刚体运动学、质量惯性阵、科氏力与向心力矩阵、水动力附加质量矩阵、流体阻尼矩阵及恢复力矩的规范化数学形式；严卫生等$^{[6]}$ 进一步系统阐明了复杂水下航行器空间六自由度动力学机理推导与控制方程体系。在此基础上，针对不同外形构型，Prestero$^{[7]}$ 针对流线型回转体 REMUS 水下航行器建立了完整的六自由度机理模型，并通过系统拖曳水池阻力实验与经验半经验公式完成了模型参数标定与校验，形成了水下航行器参数测算的公认基准；而针对非流线型、开架式（Open-frame）小型观测级水下航行器，Caccia 等人$^{[8]}$ 指出了其强各向异性流阻与轴间不对称耦合特征，提出了集总参数阻抗建模与通道解耦建模方法；Smallwood 与 Whitcomb$^{[9]}$ 则通过系统的水池动力定位对比实验，证实了在低速复杂扰动工况下，引入非线性动力学机理前馈补偿相比传统纯独立通道解耦控制在跟踪精度与抗扰稳定性上具有显著优势。

在水动力参数获取与物理试验辨识途径方面，由于水动力阻尼与附加质量难以仅凭几何尺寸纯解析推导，参数获取主要依赖数值计算与试验辨识两大途径。高婷等$^{[10]}$ 研究了基于计算流体力学（CFD）重叠网格与定常/非定常数值模拟的水动力系数高效计算方法，但在近壁低速工况下非定常涡流与系缆扰动计算耗时巨大且对网格边界敏感；在试验辨识方面，Chin 与 Lau$^{[11]}$ 针对低速复杂构型机器人流体阻尼开展了物理测试，验证了二次非线性流体阻尼多项式的有效性；Ross 等人$^{[12]}$ 提出了基于自由衰减试验（Free Decay Tests）辨识水下航行器非线性阻尼与惯性参数的实用方法；Avila 与 Adamowski$^{[13]}$ 通过小型试验水池阶跃与正弦激励试验完成了开架式水下航行器解耦水动力参数拟合。然而，传统时域最小二乘辨识对高频加速度测量与数值微分极为敏感，在微小型航行器传感器噪声干扰下极易发散。为此，Park 等人$^{[14]}$ 提出了基于广义动量回归器的系统辨识方法，通过对刚体动力学方程进行时域动量变换消除了对瞬时加速度微分的严苛依赖；Harris 等人$^{[15]}$ 在《International Journal of Robotics Research》提出了六自由度航行器与执行器联合模型的稳定零空间自适应参数在线辨识理论，在严格数学上给出了满足持续激励条件下的参数收敛性证明。然而，上述高阶自适应辨识算法结构复杂且对轨迹激励持续性要求苛刻，难以直接部署于计算资源受限的嵌入式微处理器中。

在数据驱动与物理信息混合动力学建模新趋势方面，随着近壁面巡检中非定常回流、狭窄空间壁面效应等未建模扰动日益突出，传统纯机理模型在微流场复杂工况下的预测能力受到挑战，促使学术界探索数据驱动与机器学习辅助建模方法。Brunton 等人$^{[16]}$ 提出的非线性动力学稀疏辨识（SINDy）利用稀疏回归从时序轨迹数据中提取控制微分方程；Raissi 等人$^{[17]}$ 提出的物理信息神经网络（PINN）将物理守恒律嵌入神经网络损失函数，实现了小样本流体场与参数的反演；Chen 等人$^{[18]}$ 提出的神经常微分方程（Neural ODE）通过将动力学残差映射为连续时间状态演化，为复杂时变流体阻尼的连续辨识开辟了新途径；Liu 等人$^{[19]}$ 在 IEEE Robotics and Automation Letters 提出了基于 Koopman 算子的水下仿生航行器水动力在线辨识框架，利用高维线性提升表征强非线性动态并成功实现了 Sim2Real 仿真到实物迁移。

综上所述，当前水下动力学建模研究呈现“高精度全耦合机理模型”、“轻量化工程降阶模型”与“数据驱动学习模型”并存的发展格局。然而，面向实际运动控制任务，现有成果仍存在明显局限：高阶全耦合机理模型参数繁多，在嵌入式预测控制中单步多步递推预测开销过大；简单解耦降阶模型计算迅速，但忽略轴间水动力耦合会导致强机动下模型失配加剧；纯黑盒数据驱动模型则依赖海量实测数据且存在外推泛化风险。因此，构建涵盖机理模型、降阶解耦模型及数据驱动模型的候选模型体系，并基于水池实测数据横向对比多步预测精度与单步计算耗时，筛选出兼顾物理表征能力与在线实时性的轻量化预测模型，是当前该领域的重要研究方向。

#### 2.2 多推进器水下航行器受约束运动控制与推力分配研究现状

小型水下航行器在近距离精细巡检时，不仅面临流体阻尼非线性与水动力耦合的干扰，还受到执行机构物理性能的硬性约束。八推进器空间矢量布局虽然提供了六自由度运动的驱动冗余，但单机推进器受电机功率、螺旋桨反转死区及流体动态滞后的制约，推力幅值与变化率具有严格上下限。如何在多变量耦合与推力物理约束下实现高精度、无超调的运动控制，是水下控制理论与工程界长期的核心课题。

在传统控制与鲁棒非线性控制演进方面，Yuh$^{[20]}$ 与朱大奇、孙兵$^{[21]}$ 先后系统综述了水下机器人运动控制技术的演进脉络与典型控制架构；Fernandes 等人$^{[22]}$ 在《Control Engineering Practice》针对观测级水下航行器设计了基于高增益观测器的输出反馈控制方法。早期水下航行器主要依赖分通道 PID 控制，但由于缺乏轴间交叉耦合解耦机制，在多自由度联动时控制品质严重退化。为提高抗扰鲁棒性，Yoerger 与 Slotine$^{[23]}$ 开创性地将滑模变结构控制（SMC）应用于水下航行器轨迹跟踪，利用非线性不连续控制面克服水动力参数不确定性；Healey 与 Lienard$^{[24]}$ 进一步针对欠驱动与多变量航行器提出了俯仰、航向与深度解耦滑模控制方法，奠定了多变量滑模控制在海洋工程中的应用基础；针对多推进器推力滞后与饱和难题，Chu 与向先波等$^{[25]}$ 在《ISA Transactions》提出了考虑推进器动态特性与输入饱和约束的自适应反步轨迹跟踪控制方法，通过构造辅助抗饱和动态系统抑制了推力超限诱发的姿态失稳。为处理多回路动态响应差异，钱辰与方勇纯$^{[26]}$ 基于奇异摄动理论剖析了系统快慢回路的时间尺度分离特性，为多变量系统的分层协同控制提供了理论指导；Smeur 等人$^{[27]}$ 与 Slawik 等人$^{[28]}$ 分别在微型飞行器与敏捷水下机器人 Cuttlefish 上验证了增量非线性动态逆（INDI）控制，利用高频角加速度反馈增强系统抗扰能力。然而，滑模控制的抖振现象易加剧推进器机械磨损，且传统鲁棒非线性控制本质上属于基于当前状态误差的被动反馈补偿，无法在时域内主动前瞻系统演化趋势，难以在控制量生成源头显式协调执行器物理硬约束。

在模型预测控制（MPC）及约束优化控制方面，MPC基于系统内部动力学模型在前向滚动时域内实时求解带约束最优控制问题，因其能够在目标函数中直接集成状态偏差、能量消耗，并在优化求解器中显式施加控制量幅值与变化率约束，成为解决水下航行器受约束运动控制最具前景的技术路线$^{[29]}$。张磊、严卫生与付明玉$^{[29]}$ 在《控制理论与应用》系统综述了水下航行器模型预测控制的研究现状，系统梳理了线性 MPC、非线性 MPC（NMPC）以及鲁棒 MPC 在水下轨迹跟踪中的适用性与局限；Heshmati-Alamdari 等人$^{[30-31]}$ 先后针对工作空间受限环境下的全驱动与欠驱动水下航行器，提出了鲁棒非线性模型预测控制（Robust NMPC）架构，在存在模型不确定性与外界水流扰动的条件下实现了有界约束内的安全避障与轨迹跟踪；Torrente 等人$^{[32]}$ 在《IEEE Robotics and Automation Letters》系统对比了数据驱动 MPC 与基于机理模型的平坦前馈控制，揭示了解析前馈与预测优化在算力消耗与跟踪精度之间的折效应；Liniger 等人$^{[33]}$ 提出的模型预测轮廓控制（MPCC）通过在时域优化中动态权衡行进进度与正交轮廓误差，为空间曲率变化较大的精细轨迹跟踪提供了全新优化思路；Shi 等人$^{[34]}$（Neural-Lander）与 O'Connell 等人$^{[35]}$（Neural-Fly, Science Robotics）将深度神经网络流场残差预测融入优化控制，展示了预测补偿非定常强流扰动的巨大潜力；Brunke 等人$^{[36]}$ 在机器人安全学习综述中指出，在执行器存在严格物理幅值与速率约束时，保证系统满足控制李雅普诺夫函数与控制屏障函数（CBF）安全包络是防止多轴耦合系统失稳倾覆的先决条件。

在推进器空间配置与推力分配（Control Allocation）方面，针对过驱动（Over-actuated）水下航行器，上层运动控制器输出的六自由度广义控制力与力矩必须通过推力分配算法映射为各个推进器的实际转速控制指令。Johansen 与 Fossen$^{[37]}$ 在其控制分配权威综述中全面剖析了广义逆（Pseudo-inverse）、定点迭代法及二次规划（QP）等主流分配方法；Bodson$^{[38]}$ 在经典对比研究中系统评估了加权伪逆法与带约束二次规划分配算法，指出无约束伪逆单次解算仅耗费数微秒，但在推力超限时存在严重的方向畸变截断误差；Härkegård$^{[39]}$ 提出了用于带约束线性二次控制分配的高效有效集（Active Set）算法，在保证毫秒级计算的同时严格保证了推力幅值物理可行性；程卫平等$^{[40]}$ 针对多推进器水下机器人推力分配建立了二次规划模型，并采用可行方向法在线求解，避免了传统拉格朗日乘子法在边界奇异处的发散；孙功武等$^{[41]}$ 针对混合推进 ROV 提出了基于模糊逻辑的多级推力分配策略，在推进器推力逼近饱和限值时自适应调整控制权重，实现了推力饱和平滑过渡与综合能耗优化；Li 等人$^{[42]}$（IROS 2025）针对具有冗余推进布局的水下机器人，提出了基于运动控制误差（MCE）的直接容错推力分配方法，在推进器出现推力削减或故障时保障了动力定位稳定性。

综上所述，模型预测控制与多推进器优化分配在理论层面已日臻成熟，但在面向实际微小型八推进器航行器时仍面临突出矛盾：一方面，非线性六自由度 NMPC 在线求解依赖非凸优化迭代，单步求解开销常达数十甚至数百毫秒，难以满足板载微控制器数十赫兹的高频闭环控制节拍；另一方面，现有工程方案普遍采用“外环 MPC 解算广义控制力矩 + 底层独立 QP 推力分配”的解耦串级架构，当突发水流扰动导致多个推进器达到推力幅值极限时，底层分配层发生的不可达截断误差无法直接反馈给上层优化器，容易引发轴间控制权争夺与姿态漂移。因此，研究兼顾推进器推力硬约束、轴间协调机制与毫秒级在线计算实时性的轻量化预测控制方法，是突破当前受约束控制瓶颈的核心关键。

#### 2.3 水下机器人开源飞控架构与闭环仿真验证发展现状

先进控制算法的工程化验证与应用落地，离不开可靠的嵌入式飞控软件体系与高保真闭环仿真生态。近年来，开源飞控平台与数字孪生仿真技术的成熟，为水下机器人控制系统的快速开发与迭代验证提供了标准化基础设施。

在开源飞控平台的演进与 PX4 架构特性方面，开源飞控系统逐渐打破了传统工业闭源自研嵌入式系统的壁垒。在现存主流开源体系中，ArduPilot 社区的 ArduSub 固件在低成本观测级 ROV 领域占据了主要市场份额，但其软件架构历史遗留代码较多，多任务调度与高阶模型控制扩展相对受限；相比之下，Meier 等人$^{[43]}$ 研发的 PX4 Autopilot 平台代表了现代微内核机器人飞控架构的发展方向。PX4 基于 NuttX 实时嵌入式操作系统构建，其核心技术优势体现在：采用基于 uORB（Micro Object Request Broker）的超低时延、发布/订阅式进程间通信中间件，实现了传感器采集、状态估计、轨迹控制与执行器输出的深度解耦与线程隔离；自 PX4 v1.13 及 v1.14 版本起，系统重构并推出了参数化动态控制分配子系统（Control Allocator），支持多类执行机构的在线动态几何混控与推力映射。

在水下航行器开源飞控支持现状与局限方面，尽管 PX4 在空中多旋翼、固定翼和垂起 VTOL 领域已高度成熟，但官方对水下无人系统（UUV/Submarine）的支持仍被明确界定为实验性阶段（Experimental）$^{[4]}$。Duecker 等人$^{[44]}$ 在微小型水下机器人 HippoCampus 上率先完成了 PX4 系统的底层移植与敏捷水下机动验证，证实了 PX4 微内核架构在水下动力学控制中的可行性。然而，现有 PX4 原生水下控制链路仍直接沿用空中多旋翼的四级串级 PID 架构（位置 P -> 速度 PID -> 姿态 P -> 角速率 PID），对于八推进器紧凑型水下航行器这类具有全向空间推力、显著附加质量以及各向异性流体阻尼的特殊载体，PX4 原生固件存在两大不足：其一，缺乏通用的水动力非线性前馈补偿机制；其二，尚未提供直接面向外部高阶优化控制（如 MPC）的标准化低时延全状态接管接口与安全回退机制，外挂预测控制算法往往依赖 MAVROS 通过串口或以太网与机载电脑交互，极易引入通信时延与抖动。

在水下高保真仿真与软件在环（SITL）验证生态方面，为降低水下实机测试高昂的设备进水与碰撞风险，基于物理引擎的闭环仿真验证已成为不可或缺的开发环节。von Benzon 等人$^{[45]}$ 在《Journal of Marine Science and Engineering》开源了针对标准 BlueROV2 构型的动力学基准仿真器，完整重构了六自由度 Fossen 流体动力学方程、推进器非线性推力响应及系缆扰动模型，为国际水下控制研究提供了公认的性能评测基准。结合 PX4 的软件在环（Software-in-the-Loop, SITL）技术，飞控固件可直接编译并在宿主操作系统上以原生进程运行，通过轻量级网络协议与 Gazebo 等三维水下动力学仿真物理引擎实现闭环交互，使得研究者在无需实体硬件的情况下，能够真实模拟传感器噪声、执行器饱和、通讯丢包以及外流水流扰动，完成全链路算法的闭环逻辑验证。

综上所述，当前开源飞控与仿真生态虽然为水下机器人提供了标准化框架，但学术界先进控制算法与工程开源飞控系统之间仍存在显著的工程脱节：学术研究多停留在 MATLAB 理想连续时间仿真环境，忽略了板载 RTOS 多线程调度、时钟离散化、uORB 通信阻塞与执行器控制周期约束；而开源 PX4 社区现存的水下控制方案则普遍停留在经验 PID 调谐层面，缺乏先进模型预测控制的集成范例。因此，探究先进预测控制方法与 PX4 微内核分层控制分配架构的接口集成方式，并在 SITL 仿真环境中开展系统性闭环性能评测，是推动水下先进模型控制技术走向工程实用的关键桥梁。

#### 2.4 国内外研究现状评述与本课题切入点

综合前述对水下航行器动力学建模、受约束运动控制以及开源飞控闭环验证三个维度的文献回顾与技术梳理，国内外在相关领域已积累了丰富的理论模型与工程工具，但针对紧凑型八推进器水下航行器面向实际近距离巡检任务的应用场景，现有研究仍存在以下三个核心矛盾与技术痛点：

1. **动力学模型保真度与在线优化实时算力之间的矛盾**：水下近壁面与狭小空间巡检面临复杂的流体动力学耦合与近壁扰动，高阶机理模型与高维非线性状态方程能够提供较高的仿真保真度，但在嵌入式优化求解中会导致滚动时域预测步长内的计算负担成倍增加；现有降阶模型或纯数据驱动模型则容易走向过度简化的极端，忽视轴间水动力耦合与外推稳定性。如何在保证动力学表征能力与泛化精度的前提下，构建计算复杂度适中、适配在线优化快速求解的轻量化动力学预测模型，是控制设计的首要挑战。
2. **多推进器推力硬饱和与六自由度高精度控制之间的矛盾**：八推进器空间矢量布局虽然具备六自由度全向驱动能力，但紧凑尺寸限制了推进器的峰值推力。在近壁抗流悬停或轨迹剧烈转向时，多个推进器极易陷入幅值饱和与死区非线性区间；常规级联控制或解耦式推力分配在推力超限时难以即时协调各控制轴间的控制优先级，极易引发积分饱和、推力削减不均甚至航向发散。如何在时域优化过程中显式处理八推进器的推力幅值硬约束，实现受约束轨迹跟踪精度与推力平滑性的兼顾，是提升运动控制性能的核心瓶颈。
3. **先进预测控制算法理论与开源飞控PX4工程架构之间的脱节**：现有前沿水下控制文献大多基于理想数值仿真验证算法，缺乏对真实嵌入式飞控系统任务调度与通信机制的考虑；而PX4开源飞控在水下领域的支持仍处实验阶段，默认控制流缺乏高阶模型控制的接口规范。如何在PX4架构下设计合理的控制接口方案（例如对比上层MPC规划参考轨迹与下层PX4内环稳定姿态的“分层协同方案”，与由MPC直接求解多自由度控制力矩的“集中控制方案”），并基于PX4软件在环（SITL）仿真开展全流程闭环验证，尚未形成成熟的方法体系。

针对上述关键痛点，本课题立足于水下基础设施近距离巡检中精确位姿控制与稳定悬停的工程应用需求，以八推进器紧凑型水下航行器为研究载体，确立以下三个维度的研究切入点：

1. **构建面向控制的多动力学候选模型体系并开展试验数据驱动比选**：结合水下航行器物理机理建模与数据驱动方法，构建涵盖非线性机理模型、降阶解耦模型与数据驱动模型的候选模型库；明确八推进器空间几何安装与推力矢量映射关系；基于水池实测运行数据开展模型参数拟合，建立统一度量衡，在独立测试工况下横向评估候选模型的多步预测精度、泛化稳定性与单步计算耗时，优选出最适配预测控制在线求解的轻量化预测模型。
2. **设计考虑推进器推力硬约束的轻量化模型预测控制与推力分配方法**：以水下轨迹跟踪精度与推力平顺性为优化目标，在预测控制优化问题中显式纳入八推进器的推力幅值上下界等物理约束；研究推力饱和工况下的多轴优先级协调机制，权衡时域优化求解精度与单步计算开销，实现抗水流扰动下的高精度平稳轨迹跟踪。
3. **探索预测控制与PX4飞控系统的架构接口集成方案并开展SITL闭环仿真验证**：深入剖析PX4系统的微内核多线程机制与控制分配架构，系统对比论证“分层协同控制方案”与“集中控制方案”在控制权划分、uORB通信延迟与运行稳定性上的综合表现；搭建集动力学特性、推进器约束与水流扰动于一体的高保真仿真环境，打通PX4软件在环（SITL）闭环仿真测试链路，并在仿真及水池试验条件下对算法跟踪精度、推力饱和情况与计算实时性进行全面评估。"""

SECTION_2_PLACEHOLDER = """## 二、毕业设计（论文）方案介绍

### 1．主要研究内容

（待后续阶段撰写）

### 2．研究方案

（待后续阶段撰写）

### 3．工作进度安排

（待后续阶段撰写）"""

REFERENCES_45 = [
    "[1] 工业和信息化部, 国家发展和改革委员会, 科学技术部, 等. “十四五”机器人产业发展规划[J]. 中华人民共和国工业和信息化部公报, 2021(12): 20-27.",
    "[2] 工业和信息化部, 教育部, 科学技术部, 等. “机器人+”应用行动实施方案[J]. 中华人民共和国工业和信息化部公报, 2023(1): 18-24.",
    "[3] FOSSEN T I. Handbook of Marine Craft Hydrodynamics and Motion Control[M]. 2nd ed. Chichester, UK: John Wiley & Sons, 2021.",
    "[4] PX4 Development Team. Submarines (Unmanned Underwater Vehicles—UUV)[EB/OL]. (2024)[2026-10-10]. https://docs.px4.io/main/en/frames_sub/index.",
    "[5] FOSSEN T I. Nonlinear modelling of marine vehicles in 6 degrees of freedom[J]. Mathematical Modelling of Systems, 1995, 1(1): 17-27.",
    "[6] 严卫生, 高剑, 崔荣鑫, 等. 水下航行器控制技术[M]. 北京: 国防工业出版社, 2020.",
    "[7] PRESTERO T. Verification of a six-degree of freedom simulation model for the REMUS autonomous underwater vehicle[D]. Cambridge, MA: Massachusetts Institute of Technology, 2001.",
    "[8] CACCIA M, INDIVERI G, VERUGGIO G. Modeling and identification of open-frame variable configuration unmanned underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 2000, 25(2): 227-240.",
    "[9] SMALLWOOD D A, WHITCOMB L L. Model-based dynamic positioning of underwater robotic vehicles: Theory and experiment[J]. IEEE Journal of Oceanic Engineering, 2004, 29(1): 169-186.",
    "[10] 高婷, 庞永杰, 王亚兴, 等. 水下航行器水动力系数计算方法[J]. 哈尔滨工程大学学报, 2019, 40(1): 174-180.",
    "[11] CHIN C S, LAU M W S. Modeling and testing of hydrodynamic damping for a complex-shaped underwater robot operating at low speed[C]//2012 Oceans - Yeosu. Yeosu, Korea: IEEE, 2012: 1-7.",
    "[12] ROSS A, FOSSEN T I, JOHANSEN T A. Identification of underwater vehicle hydrodynamic coefficients using free decay tests[C]//IFAC Conference on Control Applications in Marine Systems. Ancona, Italy: IFAC, 2004: 363-368.",
    "[13] AVILA J P J, ADAMOWSKI J C. Experimental model identification of open-frame unmanned underwater vehicles[C]//2013 Oceans - San Diego. San Diego, CA: IEEE, 2013: 1-7.",
    "[14] PARK S, SUNG S, CHOI H. System identification method for robotic manipulator based on dynamic momentum regressor[J]. IEEE Transactions on Instrumentation and Measurement, 2016, 65(9): 2085-2095.",
    "[15] HARRIS Z J, MAO A M, PAINE T M, et al. Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models for underactuated vehicles: Theory and experimental evaluation[J]. The International Journal of Robotics Research, 2023, 42(12): 1070-1093.",
    "[16] BRUNTON S L, PROCTOR J L, KUTZ J N. Discovering governing equations from data by sparse identification of nonlinear dynamical systems[J]. Proceedings of the National Academy of Sciences, 2016, 113(15): 3932-3937.",
    "[17] RAISSI M, PERDIKARIS P, KARNIADAKIS G E. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations[J]. Journal of Computational Physics, 2019, 378: 686-707.",
    "[18] CHEN R T Q, RUBANOVA Y, BETTENCOURT J, et al. Neural ordinary differential equations[C]//Advances in Neural Information Processing Systems (NeurIPS 2018). Montréal, QC, Canada, 2018: 6571-6583.",
    "[19] LIU A, ZHANG X, XIAO F, et al. Koopman-based online identification with Sim2Real transfer for hydrodynamic modeling of turtle-inspired robot[J]. IEEE Robotics and Automation Letters, 2026, 11(6): 6632-6639.",
    "[20] YUH J. Design and control of autonomous underwater robots: A survey[J]. Autonomous Robots, 2000, 8(1): 7-24.",
    "[21] 朱大奇, 孙兵. 水下机器人运动控制研究进展[J]. 控制与决策, 2012, 27(3): 321-333.",
    "[22] FERNANDES D, SØRENSEN D, PETTERSEN K Y, et al. Output-feedback motion control of an underwater vehicle-manipulator system[J]. Control Engineering Practice, 2015, 39: 50-64.",
    "[23] YOERGER D R, SLOTINE J J E. Robust trajectory control of underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 1985, 10(4): 462-470.",
    "[24] HEALEY A J, LIENARD D. Multivariable sliding mode control for autonomous diving and steering of unmanned underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 1993, 18(3): 327-339.",
    "[25] CHU Z, XIANG X, ZHU D, et al. Adaptive trajectory tracking control for remotely operated vehicles considering thruster dynamics and saturation constraints[J]. ISA Transactions, 2020, 100: 28-37.",
    "[26] 钱辰, 方勇纯. 面向扑翼飞行控制的建模与奇异摄动分析[J]. 自动化学报, 2020, 46(12): 2585-2595.",
    "[27] SMEUR E J J, CHU Q P, DE CROON G C H E. Adaptive incremental nonlinear dynamic inversion for attitude control of micro air vehicles[J]. Journal of Guidance, Control, and Dynamics, 2016, 39(3): 450-461.",
    "[28] SLAWIK T, VYAS S, CHRISTENSEN L, et al. Attitude control of the hydrobatic intervention AUV Cuttlefish using incremental nonlinear dynamic inversion[C]//2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). Abu Dhabi, UAE: IEEE, 2024: 781-787.",
    "[29] 张磊, 严卫生, 付明玉. 自主水下航行器模型预测控制研究现状与展望[J]. 控制理论与应用, 2018, 35(9): 1181-1192.",
    "[30] HESHMATI-ALAMDARI S, KARRAS G C, MARANTOS P, et al. A robust model predictive control approach for autonomous underwater vehicles operating in a constrained workspace[C]//2018 IEEE International Conference on Robotics and Automation (ICRA). Brisbane, QLD, Australia: IEEE, 2018: 6183-6188.",
    "[31] HESHMATI-ALAMDARI S, NIKOU A, DIMAROGONAS D V. Robust trajectory tracking control for underactuated autonomous underwater vehicles in uncertain environments[J]. IEEE Transactions on Automation Science and Engineering, 2020, 18(3): 1288-1301.",
    "[32] TORRENTE G, KAUFMANN E, FÖHN P, et al. Data-driven MPC for quadrotors[J]. IEEE Robotics and Automation Letters, 2021, 6(2): 3769-3776.",
    "[33] LINIGER A, DOMAHIDI A, MORARI M. Optimization-based autonomous racing of 1:43 scale RC cars[J]. Optimal Control Applications and Methods, 2015, 36(5): 628-647.",
    "[34] SHI G, SHI X, O'CONNELL M, et al. Neural-Lander: Stable drone landing control using learned dynamics[C]//2019 International Conference on Robotics and Automation (ICRA). Montreal, QC, Canada: IEEE, 2019: 9784-9790.",
    "[35] O'CONNELL M, SHI G, SHI X, et al. Neural-Fly enables rapid learning for agile flight in strong winds[J]. Science Robotics, 2022, 7(66): eabg6513.",
    "[36] BRUNKE L, GREEFF M, HALL A W, et al. Safe learning in robotics: From learning-based control to safe reinforcement learning[J]. Annual Review of Control, Robotics, and Autonomous Systems, 2022, 5: 411-444.",
    "[37] JOHANSEN T A, FOSSEN T I. Control allocation: A survey[J]. Automatica, 2013, 49(5): 1087-1103.",
    "[38] BODSON M. Evaluation of optimization methods for control allocation[J]. Journal of Guidance, Control, and Dynamics, 2002, 25(4): 703-711.",
    "[39] HÄRKEGÅRD O. Efficient active set algorithms for solving constrained linear quadratic control allocation problems[J]. Journal of Guidance, Control, and Dynamics, 2002, 25(5): 827-835.",
    "[40] 程卫平, 王猛, 曾现敏, 等. 基于可行方向法的水下机器人推力分配[J]. 舰船科学技术, 2022, 44(13): 102-106.",
    "[41] 孙功武, 苏义鑫, 毛英, 等. 基于模糊逻辑的混合推进ROV多级推力分配策略[J]. 机器人, 2023, 45(4): 472-482.",
    "[42] LI J H, LEE M J, KIM M G, et al. MCE-based direct FTC method for dynamic positioning of underwater vehicles with thruster redundancy[C]//2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). Abu Dhabi, UAE: IEEE, 2025: arXiv:2503.18348.",
    "[43] MEIER L, HONEGGER D, POLLEFEYS M. PX4: A node-based multithreaded open source robotics framework for deeply embedded platforms[C]//2015 IEEE International Conference on Robotics and Automation (ICRA). Seattle, WA, USA: IEEE, 2015: 6235-6240.",
    "[44] DUECKER D A, BAUSCHMANN N, HANSEN T, et al. HippoCampus X—A hydrobatic open-source micro AUV for confined environments[C]//2020 IEEE/OES Autonomous Underwater Vehicles Symposium (AUV). St. John's, NL, Canada: IEEE, 2020: 1-6.",
    "[45] VON BENZON M, SØRENSEN F F, UTH E, et al. An open-source benchmark simulator: Control of a BlueROV2 underwater robot[J]. Journal of Marine Science and Engineering, 2022, 10(12): 1898."
]

def generate_markdown():
    lines = [
        "# 基于PX4的水下航行器模型控制方法研究 开题报告起草稿",
        "",
        "## 一、毕业论文课题背景",
        "",
        SECTION_1_1,
        "",
        SECTION_2,
        "",
        SECTION_2_PLACEHOLDER,
        "",
        "## 三、毕业设计（论文）的主要参考文献",
        ""
    ]
    for ref in REFERENCES_45:
        lines.append(ref)
    lines.extend([
        "",
        "## 四、审核意见",
        "",
        "（待审核）",
        ""
    ])
    full_content = "\n".join(lines)
    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"已成功写入完整草稿至 {MD_PATH}，总字数约 {len(full_content)} 字符。")

if __name__ == "__main__":
    generate_markdown()
