# 毕业设计文献与学术资料库索引

本目录归档毕业课题《基于PX4的水下航行器动力学建模、系统辨识、运动控制与推力分配研究》全过程所依托的核心中英文文献、经典学术讲义、学位论文及精读导读指南。所有资料已按课题核心任务主干归类整合。

> [!NOTE]
> 1. **纯净 PDF 铁律与源码归档规范**：各主题分类目录下仅保留纯净权威的 PDF 文档（英文原版、中文版、双语对照版），所有 Markdown 源码一律且仅存放在 `资料/md/` 统一收纳管理；
> 2. **历史资产与平台**：历史开发的基于 Web 的交互式中英双语文献阅读平台、插图库与全译资产已独立归档至远程私有仓库：[Eternity-burial/rov-paper-reader](https://github.com/Eternity-burial/rov-paper-reader)。
> 3. **全覆盖双语化标准**：全库所有外文文献均配备 100% 完整原位双栏中文版与中英双语对照版高保真 PDF，公式无损保留，双语卡片结构清晰。

---

## 目录结构与专题分类总览

```
资料/
├── 水下航行器从物理直觉到工程闭环极速入门指南.md   # 全局极速入门指南（物理图景->数学方程->控制分配）
├── 00_研究背景与装备现状/                          # 专题 0：海洋强国战略、巡检级 ROV 装备现状与流扰瓶颈
├── 01_海洋航行器机理建模与理论基础/                # 课题主干 1：机理建模、刚体与水动力方程 (01~04)
├── 02_水动力参数辨识与数据驱动建模/                # 课题主干 2：系统辨识、水动力参数估计与 PINN (01~08)
├── 03_先进运动控制与动态补偿/                      # 课题主干 3：闭环运动控制（NMPC、MPCC、INDI、安全学习）(01~10)
├── 04_控制分配与水下传感实验/                      # 课题主干 4：多推进器分配、传感器标定与数据集 (01~04)
├── 02_水动力机理建模与参数辨识文献库/              # 历史专题文献库：已全面配备对应中文版与双语对照版 PDF
├── 03_先进运动控制与动态补偿文献库/                # 历史专题文献库：已全面配备对应中文版与双语对照版 PDF
├── 04_多推进器控制分配文献库/                      # 历史专题文献库：已全面配备对应中文版与双语对照版 PDF
└── md/                                             # 全量文献 Markdown 源码归档库 (30+ 篇)
```

---

### 00_研究背景与装备现状

聚焦国家海洋战略规划背景、巡检级水下航行器（ROV/AUV）国际发展现状、恶劣多维流扰工况下的物理矛盾与控制瓶颈。

| 序号 | 英文原版 / 源 PDF | 中文版 / 精读导读 | 双语对照版 PDF | 说明 |
| :---: | :--- | :--- | :--- | :--- |
| **00-1** | `00_政策_十四五机器人产业发展规划_工信部联规2021_206号.pdf` | `资料/md/00_十四五机器人产业发展规划_政策精读与课题战略支撑导读.md` | - | 【国家产业规划】工信部等十五部门：强调突破特种机器人、机器人自主控制软件与核心算法 (12p) |
| **00-2** | `00_政策_机器人+应用行动实施方案_工信部联通装2022_187号.pdf` | `资料/md/00_机器人+应用行动实施方案_政策精读与课题战略支撑导读.md` | - | 【国家战略行动】工信部等十七部门：部署安全应急/极限环境特种机器人与重大基础设施巡检应用 (11p) |
| **01** | `01_Capocci2017_Inspection-Class Remotely Operated Vehicles A Review.pdf` | `01_巡检级水下航行器ROV综述_Capocci2017_中文版.pdf` | `01_巡检级水下航行器ROV综述_Capocci2017_双语对照.pdf` | 【装备现状综述】巡检级（Inspection-class）遥控水下机器人发展现状、典型构型与抗扰瓶颈分析 (10p) |
| **02** | `02_钱辰2020_面向扑翼飞行控制的建模与奇异摄动分析.pdf` | （源文件即为中文） | - | 【多时间尺度解耦】自动化学报：多刚体时变动力学建模与高频脉动流扰的双时间尺度奇异摄动分析 (10p) |
| **05** | `05_Yuh2000_Design_and_control_of_autonomous_underwater_robots.pdf` | `资料/md/05_水下机器人设计与控制综述_Yuh2000_中文精译导读.md` | - | 【运动控制大综述】Autonomous Robots：水下机器人设计与六大运动控制流派权威奠基综述 (18p, 被引2500+) |


---

### 01_海洋航行器机理建模与理论基础

聚焦海洋工程与水下机器人六自由度（6-DOF）运动学与动力学标准机理方程（Fossen 理论体系与 MIT REMUS 标杆）。

| 序号 | 英文原版 PDF | 中文版 PDF | 双语对照版 PDF | 说明 |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `01_Fossen_Chapter2_Kinematics.pdf` | `01_Fossen海洋航行器建模第2章_运动学与坐标系_中文版.pdf` | `01_Fossen海洋航行器建模第2章_运动学与坐标系_双语对照.pdf` | NED 惯性系与 FRD 附体系坐标变换、欧拉角与旋转矩阵 $\boldsymbol{J}(\boldsymbol{\eta})$ (51p) |
| **02** | `02_Fossen_Chapter3_Rigid_Body_Kinetics.pdf` | `02_Fossen海洋航行器建模第3章_6DOF动力学与水动力_中文版.pdf` | `02_Fossen海洋航行器建模第3章_6DOF动力学与水动力_双语对照.pdf` | 刚体惯性 $\boldsymbol{M}_{RB}$、附加质量 $\boldsymbol{M}_A$、阻尼矩阵 $\boldsymbol{D}$ 及重浮力恢复力 $\boldsymbol{g}(\boldsymbol{\eta})$ (29p) |
| **03** | `03_Fossen1995_Nonlinear modelling of marine vehicles in 6 degrees of freedom.pdf` | `03_Fossen1995_海洋航行器六自由度非线性统一建模_中文版.pdf` | `03_Fossen1995_海洋航行器六自由度非线性统一建模_双语对照.pdf` | IEEE JOE 经典文献：海洋航行器 6-DOF 非线性动力学统一建模框架 (11p, 50个公式无删减) |
| **04** | `04_Prestero2001_Verification of a Six-Degree of Freedom Simulation Model for the REMUS Autonomous Underwater Vehicle.pdf` | `04_REMUS水下航行器六自由度仿真模型验证_Prestero2001_中文版.pdf` | `04_REMUS水下航行器六自由度仿真模型验证_Prestero2001_双语对照.pdf` | 【学术工程标杆】MIT 硕士学位论文：REMUS 水下航行器 6-DOF 非线性仿真模型、水动力导数与水池实验验证 (127p) |

---

### 02_水动力参数辨识与数据驱动建模

聚焦水下航行器附加质量、线性/二次阻尼参数及未建模水流扰动的系统辨识与数据驱动建模前沿算法（由宏观综述、工程防噪、显式方程发现到物理信息深度学习 PINN 与过驱动联合辨识）。

| 序号 | 英文原版 PDF | 中文版 / 精读导读 | 双语对照版 PDF | 说明 |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `01_Makam2023_A Comprehensive Study on Modelling and Control of Autonomous Underwater Vehicle.pdf` | `01_水下航行器动力学建模与参数辨识综述_arXiv2312_中文版.pdf` | `01_水下航行器动力学建模与参数辨识综述_arXiv2312_双语对照.pdf` | 【全局地图】2023 最新水下机器人动力学建模与参数辨识方法前沿综述 (33p 长篇综述) |
| **02** | `02_Park2016_System identification method for robotic manipulator based on dynamic momentum regressor.pdf` | `02_机械臂动态动量回归器系统辨识_Park2016_中文版.pdf` | `02_机械臂动态动量回归器系统辨识_Park2016_双语对照.pdf` | 【工程防噪基石】基于广义动量回归（Momentum Regressor）的系统辨识，彻底规避加速度求导噪声 |
| **03** | `03_Brunton2016_Discovering governing equations from data by sparse identification of nonlinear dynamical systems.pdf` | `03_SINDy非线性动力学稀疏辨识_Brunton2016_中文版.pdf` | `03_SINDy非线性动力学稀疏辨识_Brunton2016_双语对照.pdf` | 【显式方程发现】SINDy 稀疏回归算法奠基作（PNAS），物理字典+稀疏化提炼紧凑方程，可直上PX4飞控 |
| **04** | `04_Chen2019_Neural Ordinary Differential Equations.pdf` | `04_神经常微分方程Neural_ODE_Chen2019_中文版.pdf` | `04_神经常微分方程Neural_ODE_Chen2019_双语对照.pdf` | 【连续神经底座】Neural ODE 神经微分方程奠基作（NeurIPS Best Paper），连续动力系统深度学习建模 |
| **05** | `06_Duong2024_Port-Hamiltonian Neural ODE Networks on Lie Groups for Robot Dynamics Learning and Control.pdf` | `05_李群端口哈密顿Neural_ODE机器人动力学学习与控制_Duong2024_中文版.pdf` | `05_李群端口哈密顿Neural_ODE机器人动力学学习与控制_Duong2024_双语对照.pdf` | 【物理守恒约束】李群 SE(3) 上端口哈密顿神经微分方程（PH-NODE），保留能量守恒与无源性约束 |
| **06** | `06_Liu2026_Koopman-Based Online Identification With Sim2Real Transfer for Hydrodynamic Modeling of Turtle Inspired ROV.pdf` | `06_仿生海龟ROV水动力Koopman在线辨识与Sim2Real迁移_Liu2026_中文版.pdf` | `06_仿生海龟ROV水动力Koopman在线辨识与Sim2Real迁移_Liu2026_双语对照.pdf` | 【算子升维与实车迁移】基于 Koopman 算子理论的在线水动力辨识与 Sim2Real 迁移 (Liu 2026) |
| **07** | `07_Harris2023_Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models.pdf` | `07_水下航行器六自由度零空间自适应参数辨识_Harris2023_中文版.pdf` | `07_水下航行器六自由度零空间自适应参数辨识_Harris2023_双语对照.pdf` | 【过驱动联合辨识】IEEE TCST：6 自由度水下航行器被控对象与多执行器模型的零空间稳定自适应辨识 |
| **08** | `08_Raissi2019_Physics-Informed Neural Networks.pdf` | `08_物理信息神经网络PINN_Raissi2019_中文版.pdf` | `08_物理信息神经网络PINN_Raissi2019_双语对照.pdf` | 【物理约束深度学习】JCP 开山之作：物理信息神经网络（PINN）求解偏微分与常微分非线性正逆动力学问题 (22p) |
| **09** | `09_Caccia2000_Modeling_and_identification_open_frame_UUV.pdf` | `资料/md/09_水下航行器建模与板载辨识_Caccia2000_中文精译导读.md` | - | 【板载辨识工程标杆】IEEE JOE：无需拖曳水池、仅利用板载传感器阶跃与衰减试验的最小二乘水动力辨识 (14p, 被引500+) |
| **10** | `10_Chin2012_Modeling_and_testing_hydrodynamic_damping_ROV.pdf` | `资料/md/10_水下航行器阻尼建模与试验测试_Chin2012_中文精译导读.md` | - | 【阻尼建模与试验测试】JMSA：复杂构型 ROV 线性黏性与非线性二次压差阻尼的 CFD 虚拟拖曳与水池试验互证 (14p) |

---

### 03_先进运动控制与动态补偿

聚焦未知水流扰动与模型不确定性下的先进鲁棒与模型控制方法（从先进优化基准、增量动态逆理论、水下工程落地，到 MPCC 轮廓控制、NMPC、神经内模、增广复合控制与安全学习界限）。

| 序号 | 英文原版 PDF | 中文版 / 精读导读 | 双语对照版 PDF | 说明 |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `01_Torrente2021_A Comparative Study of Nonlinear MPC and Differential-Flatness-Based Control for Quadrotor Agile Flight.pdf` | `01_四旋翼NMPC与微分平坦控制对比研究_中文版.pdf` | `01_四旋翼NMPC与微分平坦控制对比研究_双语对照.pdf` | 【先进优化基准】敏捷运动下非线性模型预测控制（NMPC）与微分平坦控制（DFBC）横向对比 |
| **02** | `02_Smeur2016_Adaptive Incremental Nonlinear Dynamic Inversion for Attitude Control of Micro Air Vehicles.pdf` | `02_微型飞行器自适应INDI姿态控制_中文版.pdf` | `02_微型飞行器自适应INDI姿态控制_双语对照.pdf` | 【抗扰逆控理论源头】自适应增量非线性动态逆（A-INDI）姿态控制（TU Delft 奠基标杆） |
| **03** | `03_Corno2020_Attitude Control of the Hydrobatic Intervention AUV Cuttlefish using Incremental Nonlinear Dynamic Inversion.pdf` | `03_AUV_INDI姿态控制_Cuttlefish_中文版.pdf` | `03_AUV_INDI姿态控制_Cuttlefish_双语对照.pdf` | 【水下INDI实战验证】特技干预 AUV Cuttlefish 姿态控制：基于水下低通滤波的 INDI 水池实测验证 |
| **04** | `04_Neural Internal Model Control - Learning a Robust Control Policy Via Predictive Error Feedback.pdf` | `04_神经内模控制_基于预测误差反馈学习鲁棒策略_中文版.pdf` | `04_神经内模控制_基于预测误差反馈学习鲁棒策略_双语对照.pdf` | 【预测误差反馈】神经内模控制（NIMC）：基于数据驱动预测误差反馈学习的高鲁棒性控制策略 |
| **05** | `05_Neural-Augmented Incremental Nonlinear Dynamic Inversion for Quadrotors with Payload Adaptation.pdf` | `05_神经增广INDI四旋翼负载自适应控制_中文版.pdf` | `05_神经增广INDI四旋翼负载自适应控制_双语对照.pdf` | 【复合增广控制】神经增强增量非线性动态逆（NA-INDI）：机理增量逆 + 神经负载在线自适应 |
| **06** | `06_OConnell2024_Neural-Fly Enables Rapid Learning for Agile Flight in Strong Winds.pdf` | `06_Neural-Fly强风敏捷飞行深度学习自适应控制_ScienceRobotics2024_中文版.pdf` | `06_Neural-Fly强风敏捷飞行深度学习自适应控制_ScienceRobotics2024_双语对照.pdf` | 【深度自适应前沿】Caltech Neural-Fly：基于元学习与深度表征的风扰自适应飞行控制 (Science Robotics) |
| **07** | `07_Heshmati2020_Robust Trajectory Tracking Control for Underactuated Autonomous Underwater Vehicles.pdf` | `07_欠驱动水下航行器鲁棒NMPC轨迹跟踪_Heshmati2020_中文版.pdf` | `07_欠驱动水下航行器鲁棒NMPC轨迹跟踪_Heshmati2020_双语对照.pdf` | 【水下鲁棒预测控制】IEEE T-ASE 顶刊：欠驱动自主水下航行器在外界流扰与不确定性下的鲁棒非线性模型预测控制 (9p) |
| **08** | `08_Liniger2015_Optimization-Based Autonomous Racing of 1 to 43 Scale RC Cars.pdf` | `08_基于MPCC模型预测轮廓控制的自主竞速_Liniger2015_中文版.pdf` | `08_基于MPCC模型预测轮廓控制的自主竞速_Liniger2015_双语对照.pdf` | 【轮廓误差优化鼻祖】模型预测轮廓控制（MPCC）开山之作：联合优化轨迹轮廓误差与前进进度的经典范式 (20p) |
| **09** | `09_Shi2019_Neural Lander Stable Drone Landing Control Using Learned Dynamics.pdf` | `09_Neural-Lander动力学学习无人机着陆控制_Shi2019_中文版.pdf` | `09_Neural-Lander动力学学习无人机着陆控制_Shi2019_双语对照.pdf` | 【近界复杂气流学习】IEEE ICRA：Neural-Lander 基于深度残差动力学学习补偿近壁效应流扰，实现高稳定着陆 (7p) |
| **10** | `10_Brunke2022_Safe Learning in Robotics From Learning-Based Control to Safe Reinforcement Learning.pdf` | `10_机器人安全学习综述_从控制到强化学习_Brunke2022_中文版.pdf` | `10_机器人安全学习综述_从控制到强化学习_Brunke2022_双语对照.pdf` | 【控制安全理论大成】机器人安全学习权威综述：控制屏障函数（CBF）、Lyapunov 稳定性与安全强化学习理论体系 (36p) |
| **11** | `11_Yoerger1985_Robust_trajectory_control_underwater_vehicles.pdf` | `资料/md/11_水下航行器鲁棒轨迹滑模控制_Yoerger1985_中文精译导读.md` | - | 【滑模鲁棒控制开山鼻祖】IEEE JOE：Yoerger & Slotine 首次将滑模变结构控制引入 UUV，提出边界层消除抖振 (9p, 被引1300+) |
| **12** | `12_Healey1993_Multivariable_sliding_mode_control_diving_steering_AUV.pdf` | `资料/md/12_水下航行器多变量滑模解耦控制_Healey1993_中文精译导读.md` | - | 【多变量解耦控制标杆】IEEE JOE：NPS AUV II 航速、潜浮、航向三大子系统解耦与交叉耦合滑模抵消经典架构 (13p, 被引900+) |
| **13** | `13_Smallwood2004_Model_based_dynamic_positioning_underwater_vehicles.pdf` | `资料/md/13_水下机器人基于模型的动力定位控制_Smallwood2004_中文精译导读.md` | - | 【模型控制实机消融验证】IEEE JOE：JHU ROV 水池真实对比纯PD、非线性解耦与模型前馈补偿（MB-PD），跟踪精度提升2~3倍 (18p, 被引500+) |

---

### 04_控制分配与水下传感实验

聚焦八推进器空间布置矢量合成与推力分配（$6 \times 8$ 控制分配矩阵、推力饱和约束）、水下多源传感器（DVL/IMU）时空联合标定与真实水下数据集。

| 序号 | 英文原版 PDF | 中文版 / 精读导读 | 双语对照版 PDF | 说明 |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `01_Fossen_Chapter6_Maneuvering_Models_and_Control_Allocation.pdf` | `01_Fossen海洋航行器建模第6章_控制分配与推进器模型_中文版.pdf` | `01_Fossen海洋航行器建模第6章_控制分配与推进器模型_双语对照.pdf` | 控制分配标准数学框架、加权伪逆法、线性/二次规划与推进器静态/动态模型 (52p) |
| **02** | `02_Li2025_MCE-based Direct FTC Method for Underwater Vehicles with Thruster Redundancy.pdf` | `02_水下航行器冗余推进控制分配_Li2025_中文版.pdf` | `02_水下航行器冗余推进控制分配_Li2025_双语对照.pdf` | 水下航行器冗余推进系统控制分配算法与抗饱和策略研究 (8p, 矢量8推核心对标) |
| **03** | `03_Zhao2025_Spatiotemporal Calibration of Doppler Velocity Logs for Underwater Robots.pdf` | `03_LIAS实验室_DVL时空标定_Zhao2025_中文版.pdf` | `03_LIAS实验室_DVL时空标定_Zhao2025_双语对照.pdf` | CUHK-SZ LIAS 成果：水下多普勒计程仪（DVL）与惯导时空联合标定方法 |
| **04** | `04_Peng2025_AquaticVision Benchmarking Visual SLAM in Underwater Environment with Events and Frames.pdf` | `04_LIAS实验室_AquaticVision水下数据集_Peng2025_中文版.pdf` | `04_LIAS实验室_AquaticVision水下数据集_Peng2025_双语对照.pdf` | CUHK-SZ LIAS 成果（ICRA）：AquaticVision 多模态水下感知与定位基准数据集 |
| **05** | `05_Johansen2013_Control_Allocation_Survey_Automatica.pdf` | `资料/md/05_多执行器控制分配综述_Johansen2013_中文精译导读.md` | - | 【控制分配行业宪法】Automatica：过驱动多执行器控制分配权威长篇综述（加权伪逆、保方向等比例抗饱和缩放、QP二次规划、动态分配） (17p, 被引2000+) |


---

### 资料/md/ Markdown 源码统一收纳库

所有文献的中文全译精读手册、精读导读与中英双语对照 Markdown 源码已 100% 统一归集收纳于 [资料/md/](file:///d:/tj/Graduation%20Project/资料/md/)，确保 5 大主题子目录保持纯净 PDF，便于全文检索与跨章节理论推导。
