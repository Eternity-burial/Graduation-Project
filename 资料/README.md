# 毕业设计文献与学术资料库索引

本目录归档毕业课题《基于PX4的水下航行器动力学建模、系统辨识、运动控制与推力分配研究》全过程所依托的核心中英文文献、经典学术讲义及精读导读指南。所有资料已按课题核心任务主干归类整合。

> [!NOTE]
> 历史开发的基于 Web 的交互式中英双语文献阅读平台、插图库与全译资产已独立归档至远程私有仓库：[Eternity-burial/rov-paper-reader](https://github.com/Eternity-burial/rov-paper-reader)。本地资料库专注于高质量英文原版、中文版与中英双语对照版 PDF，所有 Markdown 源码统一归集收纳于 `资料/md/` 目录下。

---

## 目录结构与专题分类

```
资料/
├── 水下航行器从物理直觉到工程闭环极速入门指南.md   # 全局极速入门指南（物理图景->数学方程->控制分配）
├── 01_海洋航行器机理建模与理论基础/                # 课题主干 1：机理建模与动力学方程 (01~03)
├── 02_水动力参数辨识与数据驱动建模/                # 课题主干 2：系统辨识与水动力参数估计 (01~07)
├── 03_先进运动控制与动态补偿/                      # 课题主干 3：闭环运动控制（INDI、NMPC、神经自适应）(01~06)
├── 04_控制分配与水下传感实验/                      # 课题主干 4：多推进器分配、传感器标定与数据集 (01~04)
└── md/                                             # 全量文献 Markdown 源码归档库 (26 篇)
```

---

### 01_海洋航行器机理建模与理论基础

聚焦海洋工程与水下机器人六自由度（6-DOF）运动学与动力学标准机理方程（Fossen 理论体系）。

| 序号 | 英文原版 PDF | 中文版 PDF | 双语对照版 PDF | 说明 |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `01_Fossen_Chapter2_Kinematics.pdf` | `01_Fossen海洋航行器建模第2章_运动学与坐标系_中文版.pdf` | `01_Fossen海洋航行器建模第2章_运动学与坐标系_双语对照.pdf` | NED 惯性系与 FRD 附体系坐标变换、欧拉角与旋转矩阵 $\boldsymbol{J}(\boldsymbol{\eta})$ (51p) |
| **02** | `02_Fossen_Chapter3_Rigid_Body_Kinetics.pdf` | `02_Fossen海洋航行器建模第3章_6DOF动力学与水动力_中文版.pdf` | `02_Fossen海洋航行器建模第3章_6DOF动力学与水动力_双语对照.pdf` | 刚体惯性 $\boldsymbol{M}_{RB}$、附加质量 $\boldsymbol{M}_A$、阻尼矩阵 $\boldsymbol{D}$ 及重浮力恢复力 $\boldsymbol{g}(\boldsymbol{\eta})$ (29p) |
| **03** | `03_Fossen1995_Nonlinear modelling of marine vehicles in 6 degrees of freedom.pdf` | `03_Fossen1995_海洋航行器六自由度非线性统一建模_中文版.pdf` | `03_Fossen1995_海洋航行器六自由度非线性统一建模_双语对照.pdf` | IEEE JOE 经典文献：海洋航行器 6-DOF 非线性动力学统一建模框架 (11p, 50个公式无删减) |

---

### 02_水动力参数辨识与数据驱动建模

聚焦水下航行器附加质量、线性/二次阻尼参数及未建模水流扰动的系统辨识与数据驱动建模前沿算法（由宏观综述、工程防噪、显式方程发现到物理信息深度学习与过驱动联合辨识）。

| 序号 | 英文原版 PDF | 中文版 PDF | 双语对照版 PDF | 说明 |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `01_Makam2023_A Comprehensive Study on Modelling and Control of Autonomous Underwater Vehicle.pdf` | `01_水下航行器动力学建模与参数辨识综述_arXiv2312_中文版.pdf` | `01_水下航行器动力学建模与参数辨识综述_arXiv2312_双语对照.pdf` | 【全局地图】2023 最新水下机器人动力学建模与参数辨识方法前沿综述 (33p 长篇综述) |
| **02** | `02_Park2016_System identification method for robotic manipulator based on dynamic momentum regressor.pdf` | `02_机械臂动态动量回归器系统辨识_Park2016_中文版.pdf` | `02_机械臂动态动量回归器系统辨识_Park2016_双语对照.pdf` | 【工程防噪基石】基于广义动量回归（Momentum Regressor）的系统辨识，彻底规避加速度求导噪声 |
| **03** | `03_Brunton2016_Discovering governing equations from data by sparse identification of nonlinear dynamical systems.pdf` | `03_SINDy非线性动力学稀疏辨识_Brunton2016_中文版.pdf` | `03_SINDy非线性动力学稀疏辨识_Brunton2016_双语对照.pdf` | 【显式方程发现】SINDy 稀疏回归算法奠基作（PNAS），物理字典+稀疏化提炼紧凑方程，可直上PX4飞控 |
| **04** | `04_Chen2019_Neural Ordinary Differential Equations.pdf` | `04_神经常微分方程Neural_ODE_Chen2019_中文版.pdf` | `04_神经常微分方程Neural_ODE_Chen2019_双语对照.pdf` | 【连续神经底座】Neural ODE 神经微分方程奠基作（NeurIPS Best Paper），连续动力系统深度学习建模 |
| **05** | `06_Duong2024_Port-Hamiltonian Neural ODE Networks on Lie Groups for Robot Dynamics Learning and Control.pdf` | `05_李群端口哈密顿Neural_ODE机器人动力学学习与控制_Duong2024_中文版.pdf` | `05_李群端口哈密顿Neural_ODE机器人动力学学习与控制_Duong2024_双语对照.pdf` | 【物理守恒约束】李群 SE(3) 上端口哈密顿神经微分方程（PH-NODE），保留能量守恒与无源性约束 |
| **06** | `06_Liu2026_Koopman-Based Online Identification With Sim2Real Transfer for Hydrodynamic Modeling of Turtle Inspired ROV.pdf` | `06_仿生海龟ROV水动力Koopman在线辨识与Sim2Real迁移_Liu2026_中文版.pdf` | `06_仿生海龟ROV水动力Koopman在线辨识与Sim2Real迁移_Liu2026_双语对照.pdf` | 【算子升维与实车迁移】基于 Koopman 算子理论的在线水动力辨识与 Sim2Real 迁移 (Liu 2026) |
| **07** | `07_Harris2023_Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models.pdf` | `07_水下航行器六自由度零空间自适应参数辨识_Harris2023_中文版.pdf` | `07_水下航行器六自由度零空间自适应参数辨识_Harris2023_双语对照.pdf` | 【过驱动联合辨识】IEEE TCST：6 自由度水下航行器被控对象与多执行器模型的零空间稳定自适应辨识 |

---

### 03_先进运动控制与动态补偿

聚焦未知水流扰动与模型不确定性下的先进鲁棒与模型控制方法（从先进优化基准、增量动态逆理论、水下工程落地，到神经内模、增广复合控制与深度自适应极限）。

| 序号 | 英文原版 PDF | 中文版 PDF | 双语对照版 PDF | 说明 |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `01_Torrente2021_A Comparative Study of Nonlinear MPC and Differential-Flatness-Based Control for Quadrotor Agile Flight.pdf` | `01_四旋翼NMPC与微分平坦控制对比研究_中文版.pdf` | `01_四旋翼NMPC与微分平坦控制对比研究_双语对照.pdf` | 【先进优化基准】敏捷运动下非线性模型预测控制（NMPC）与微分平坦控制（DFBC）横向对比 |
| **02** | `02_Smeur2016_Adaptive Incremental Nonlinear Dynamic Inversion for Attitude Control of Micro Air Vehicles.pdf` | `02_微型飞行器自适应INDI姿态控制_中文版.pdf` | `02_微型飞行器自适应INDI姿态控制_双语对照.pdf` | 【抗扰逆控理论源头】自适应增量非线性动态逆（A-INDI）姿态控制（TU Delft 奠基标杆） |
| **03** | `03_Corno2020_Attitude Control of the Hydrobatic Intervention AUV Cuttlefish using Incremental Nonlinear Dynamic Inversion.pdf` | `03_AUV_INDI姿态控制_Cuttlefish_中文版.pdf` | `03_AUV_INDI姿态控制_Cuttlefish_双语对照.pdf` | 【水下INDI实战验证】特技干预 AUV Cuttlefish 姿态控制：基于水下低通滤波的 INDI 水池实测验证 |
| **04** | `04_Neural Internal Model Control - Learning a Robust Control Policy Via Predictive Error Feedback.pdf` | `04_神经内模控制_基于预测误差反馈学习鲁棒策略_中文版.pdf` | `04_神经内模控制_基于预测误差反馈学习鲁棒策略_双语对照.pdf` | 【预测误差反馈】神经内模控制（NIMC）：基于数据驱动预测误差反馈学习的高鲁棒性控制策略 |
| **05** | `05_Neural-Augmented Incremental Nonlinear Dynamic Inversion for Quadrotors with Payload Adaptation.pdf` | `05_神经增广INDI四旋翼负载自适应控制_中文版.pdf` | `05_神经增广INDI四旋翼负载自适应控制_双语对照.pdf` | 【复合增广控制】神经增强增量非线性动态逆（NA-INDI）：机理增量逆 + 神经负载在线自适应 |
| **06** | `06_OConnell2024_Neural-Fly Enables Rapid Learning for Agile Flight in Strong Winds.pdf` | `06_Neural-Fly强风敏捷飞行深度学习自适应控制_ScienceRobotics2024_中文版.pdf` | `06_Neural-Fly强风敏捷飞行深度学习自适应控制_ScienceRobotics2024_双语对照.pdf` | 【深度自适应前沿】Caltech Neural-Fly：基于元学习与深度表征的风扰自适应飞行控制 (Science Robotics) |

---

### 04_控制分配与水下传感实验

聚焦八推进器空间布置矢量合成与推力分配（$6 \times 8$ 控制分配矩阵、推力饱和约束）、水下多源传感器（DVL/IMU）时空联合标定与真实水下数据集。

| 序号 | 英文原版 PDF | 中文版 PDF | 双语对照版 PDF | 说明 |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `01_Fossen_Chapter6_Maneuvering_Models_and_Control_Allocation.pdf` | `01_Fossen海洋航行器建模第6章_控制分配与推进器模型_中文版.pdf` | `01_Fossen海洋航行器建模第6章_控制分配与推进器模型_双语对照.pdf` | 控制分配标准数学框架、加权伪逆法、线性/二次规划与推进器静态/动态模型 (52p) |
| **02** | `02_Li2025_MCE-based Direct FTC Method for Underwater Vehicles with Thruster Redundancy.pdf` | `02_水下航行器冗余推进控制分配_Li2025_中文版.pdf` | `02_水下航行器冗余推进控制分配_Li2025_双语对照.pdf` | 水下航行器冗余推进系统控制分配算法与抗饱和策略研究 (8p, 矢量8推核心对标) |
| **03** | `03_Zhao2025_Spatiotemporal Calibration of Doppler Velocity Logs for Underwater Robots.pdf` | `03_LIAS实验室_DVL时空标定_Zhao2025_中文版.pdf` | `03_LIAS实验室_DVL时空标定_Zhao2025_双语对照.pdf` | CUHK-SZ LIAS 成果：水下多普勒计程仪（DVL）与惯导时空联合标定方法 |
| **04** | `04_Peng2025_AquaticVision Benchmarking Visual SLAM in Underwater Environment with Events and Frames.pdf` | `04_LIAS实验室_AquaticVision水下数据集_Peng2025_中文版.pdf` | `04_LIAS实验室_AquaticVision水下数据集_Peng2025_双语对照.pdf` | CUHK-SZ LIAS 成果（ICRA）：AquaticVision 多模态水下感知与定位基准数据集 |

---

### 资料/md/ Markdown 源码统一收纳库

所有 26 个文献的全译、精读与双语对照 Markdown 源码统一归集收纳于 [资料/md/](file:///d:/tj/Graduation%20Project/资料/md/)，确保 4 大主题子目录保持纯净 PDF，便于文本检索与知识沉淀。
