# 毕业设计文献与学术资料库索引

本目录归档毕业课题《基于PX4的水下航行器动力学建模、系统辨识、运动控制与推力分配研究》全过程所依托的核心中英文文献、经典学术讲义及精读导读指南。所有资料已按课题核心任务主干归类整合。

> [!NOTE]
> 历史开发的基于 Web 的交互式中英双语文献阅读平台、插图库与全译资产已独立归档至远程私有仓库：[Eternity-burial/rov-paper-reader](https://github.com/Eternity-burial/rov-paper-reader)。本地资料库专注于高质量原始 PDF 及精读导读手册。

---

## 目录结构与专题分类

```
资料/
├── 水下航行器从物理直觉到工程闭环极速入门指南.md   # 全局极速入门指南（物理图景->数学方程->控制分配）
├── 01_海洋航行器机理建模与理论基础/                # 课题主干 1：机理建模与动力学方程
├── 02_水动力参数辨识与数据驱动建模/                # 课题主干 2：系统辨识与水动力参数估计
├── 03_先进运动控制与动态补偿/                      # 课题主干 3：闭环运动控制（INDI、NMPC、神经自适应）
└── 04_控制分配与水下传感实验/                      # 课题主干 4：多推进器分配、传感器标定与数据集
```

---

### 01_海洋航行器机理建模与理论基础

聚焦海洋工程与水下机器人六自由度（6-DOF）运动学与动力学标准机理方程（Fossen 理论体系）。

| 文件名 | 类型 | 说明 |
| :--- | :--- | :--- |
| `01_Fossen海洋航行器建模第2章_运动学与坐标系.pdf` | 原版讲义 | NED 惯性系与 FRD 附体系坐标变换、欧拉角与旋转矩阵 $\boldsymbol{J}(\boldsymbol{\eta})$ |
| `01_Fossen海洋航行器建模第3章_6DOF动力学与水动力.pdf` | 原版讲义 | 刚体惯性 $\boldsymbol{M}_{RB}$、附加质量 $\boldsymbol{M}_A$、阻尼矩阵 $\boldsymbol{D}$ 及重浮力恢复力 $\boldsymbol{g}(\boldsymbol{\eta})$ |
| `01_Fossen海洋航行器建模与控制核心讲义_中文全译精读手册.md` | 精读手册 | Fossen 讲义核心推导、物理直觉与符号约定的中文对照精读笔记 |
| `Fossen and Fjellstad - 1995 - Nonlinear modelling of marine vehicles in 6 degrees of freedom.pdf` | 经典论文 | IEEE JOE 经典文献：海洋航行器 6-DOF 非线性动力学统一建模框架 |
| `02_Fossen1995_海洋航行器六自由度非线性统一建模_中文版.pdf` | 中文排版 | 经典论文 1995 高清现代矢量排版中文版（公式 100% 原生矢量还原） |
| `02_Fossen1995_海洋航行器六自由度非线性统一建模_双语对照.pdf` | 双语对照 | 经典论文 1995 中英卡片式并排双语对照版（查阅文献与英文术语零摩擦） |
| `02_Fossen1995_海洋航行器六自由度非线性统一建模_中文全译精读.md` | 全译精读 | 完整中文全译 Markdown（含定理证明、机理推导与理论地位导读） |

---

### 02_水动力参数辨识与数据驱动建模

聚焦水下航行器附加质量、线性/二次阻尼参数及未建模水流扰动的系统辨识与数据驱动建模前沿算法。

| 文件名 | 类型 | 说明 |
| :--- | :--- | :--- |
| `03_水下航行器动力学建模与参数辨识综述_arXiv2312.pdf` | 权威综述 | 2023 最新水下机器人动力学建模与参数辨识方法前沿综述 |
| `03_水下航行器动力学建模与参数辨识综述_arXiv2312_中文精译导读.md` | 精译导读 | 辨识综述中文精要导读，横向对比最小二乘、卡尔曼滤波与智能方法优劣 |
| `Brunton et al. - 2016 - Discovering governing equations from data by sparse identification of nonlinear dynamical systems.pdf` | 奠基论文 | SINDy 稀疏回归算法奠基作（PNAS），非线性动力学机理方程数据驱动发现 |
| `Chen et al. - 2019 - Neural Ordinary Differential Equations.pdf` | 顶级论文 | Neural ODE 神经微分方程奠基作（NeurIPS Best Paper），连续动力系统建模 |
| `Duong et al. - 2024 - Port-Hamiltonian Neural ODE Networks on Lie Groups for Robot Dynamics Learning and Control.pdf` | 前沿论文 | 李群上端口哈密顿神经微分方程（PH-NODE），保留物理守恒特性的动力学学习 |
| `Harris et al. - 2023 - Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models.pdf` | 核心论文 | IEEE TCST：6 自由度被控对象与执行器模型的零空间稳定自适应参数辨识 |
| `Liu 等 - 2026 - Koopman-Based Online Identification With Sim2Real Transfer for Hydrodynamic Modeling of Turtle Inspi.pdf` | 前沿论文 | 基于 Koopman 算子理论的在线水动力辨识与 Sim2Real 迁移 |
| `Park和Choi - 2016 - System identification method for robotic manipulator based on dynamic momentum regressor.pdf` | 经典论文 | 基于广义动量回归（Momentum Regressor）的机器人系统辨识，无需角加速度信号 |

---

### 03_先进运动控制与动态补偿

聚焦未知水流扰动与模型不确定性下的先进鲁棒与模型控制方法（增量非线性动态逆 INDI、非线性模型预测控制 NMPC、神经自适应控制）。

| 文件名 | 语言/形式 | 说明 |
| :--- | :--- | :--- |
| `01-en-*.pdf` / `01-zh-*.pdf` | 英文 / 中文版 | 自适应增量非线性动态逆（A-INDI）微型飞行器姿态控制（TU Delft） |
| `02-en-*.pdf` / `02-zh-*.pdf` | 英文 / 中文版 | 敏捷飞行下非线性模型预测控制（NMPC）与微分平坦控制（DFBC）横向对比 |
| `03-en-*.pdf` / `03-zh-*.pdf` | 英文 / 中文版 | 特技作业 AUV Cuttlefish 姿态控制：基于水下传感器滤波的增量非线性动态逆（INDI）水池实测验证 |
| `04-en-*.pdf` / `04-zh-*.pdf` | 英文 / 中文版 | 神经内模控制（NIMC）：基于预测误差反馈学习的高鲁棒性控制策略 |
| `05-en-*.pdf` / `05-zh-*.pdf` | 英文 / 中文版 | 神经增强增量非线性动态逆（NA-INDI）：负载自适应与机动性能增强 |
| `O'Connell 等 - 2024 - Neural-Fly Enables Rapid Learning for Agile Flight in Strong Winds.pdf` | Science Robotics | Caltech Neural-Fly：基于元学习与深度表征的风扰自适应飞行控制 |

---

### 04_控制分配与水下传感实验

聚焦八推进器空间布置矢量合成与推力分配（$6 \times 8$ 控制分配矩阵、推力饱和约束）、水下多源传感器（DVL/IMU）时空联合标定与真实水下数据集。

| 文件名 | 类型 | 说明 |
| :--- | :--- | :--- |
| `01_Fossen海洋航行器建模第6章_控制分配与推进器模型.pdf` | 原版讲义 | 控制分配标准数学框架、加权伪逆法、线性/二次规划与推进器静态/动态模型 |
| `02_水下航行器冗余推进控制分配_Li2025.pdf` | 核心论文 | 水下航行器冗余推进系统控制分配算法与抗饱和策略研究 |
| `02_水下航行器冗余推进控制分配_Li2025_中文版.pdf` | 中文排版 | Li2025 论文全篇 8 页 1:1 原位排版中文版（公式与双栏图表完美保留） |
| `02_水下航行器冗余推进控制分配_Li2025_双语对照.pdf` | 双语对照 | Li2025 论文全篇 16 页逐页中英双语对照版（查阅英文术语零摩擦） |
| `02_水下航行器冗余推进控制分配_Li2025_中文全译.md` | 中文全译 | Li2025 论文完整中文翻译与控制分配工程实现拆解 |
| `04_LIAS实验室_DVL时空标定_Zhao2025.pdf` | 核心论文 | 水下多普勒计程仪（DVL）与惯导时空联合标定方法 |
| `04_LIAS实验室_DVL时空标定_Zhao2025_中文全译.md` | 中文全译 | Zhao2025 论文中文翻译与水下速度计标定工程要点 |
| `05_LIAS实验室_AquaticVision水下数据集_Peng2025.pdf` | 核心论文 | AquaticVision 多模态水下感知与定位基准数据集 |
| `05_LIAS实验室_AquaticVision水下数据集_Peng2025_中文全译.md` | 中文全译 | Peng2025 论文中文翻译与水下数据集使用说明 |
