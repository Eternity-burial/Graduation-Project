# 水下机器人多普勒测速仪（DVL）时空联合标定研究 (中文全译)

> **英文原题**：Spatiotemporal Calibration of Doppler Velocity Logs for Underwater Robots  
> **论文作者**：Hongxu Zhao（赵鸿旭）^1^, Guangyang Zeng（曾广扬）^2^, Yunling Shao（邵云凌）^1^, Tengfei Zhang（张腾飞）^1^, Yuzhe Li（李宇哲）^3^, Junfeng Wu（吴均峰）^1^  
> **所属机构**：  
> ^1^ 香港中文大学（深圳）数据科学学院 / 智能自主系统实验室（CUHK-SZ LIAS）  
> ^2^ 深圳市人工智能与机器人社会研究院（AIRS）  
> ^3^ 华中科技大学人工智能与自动化学院  
> **预印本编号**：arXiv:2510.24571 [cs.RO]  
> **开源工具箱**：DVL-Camera/IMU Spatiotemporal Calibration Toolbox  

---

## 摘要 (Abstract)

在水下机器人 SLAM 系统中，将多普勒测速仪（Doppler Velocity Log, DVL）与其他传感器（如 IMU、双目相机）进行高精度融合，必须同时确定传感器之间的**空间外参（旋转矩阵与平移杆臂）**与**时钟偏差（时间同步延迟）**。然而，现有的水下 DVL 标定方法大多预先假定传感器之间的杠杆臂（Lever Arm）已知或时钟严格同步，极少联合估计全套时空外参。

针对这一瓶颈，本文提出了**统一迭代标定（Unified Iterative Calibration, UIC）**框架，适用于 DVL 与任意能够提供连续时间运动估计的伴随传感器（Co-sensor）。我们将机体基础运动建模为连续时间**高斯过程（Gaussian Process, GP）**，从而支持在任意带时间延迟的 DVL 采样时间戳处进行高保真运动插值。UIC 采用**序列初始化方案（Sequential Initialization）**，将时钟偏差与比例因子的估计从空间外参中解耦，该方案在理论上具有渐进统计一致性。随后，UIC 在高斯过程运动状态估计与基于数值梯度的标定变量更新之间交替优化。此外，我们基于 Fisher 信息矩阵（FIM）分析了标定系统的激励条件，给出了保证各参数可辨识性的最优机动轨迹设计原则。大量的蒙特卡洛仿真和真实水池水下机器人实验证明，UIC 框架在不同传感器配置和噪声水平下均显著优于现有主流标定方法。

---

## 一、 引言 (I. Introduction)

自主水下航行器（AUV）和遥控水下航行器（ROV）广泛应用于水下管网检测、深海测绘、资源勘探与沉船打捞等作业。在缺乏水下 GPS（GNSS）信号的深水环境中，高精度的水下导航与建图（SLAM）极度依赖航位推算（Dead Reckoning）。多普勒测速仪（DVL）通过向海底或水体发射高频声学信号并测量反射波的声学多普勒频移，能够以高频率输出航行器相对于水底的高精度三维线速度，已成为长航程水下导航系统的核心基石。

为了构建稳健的水下状态估计器，DVL 通常与惯性测量单元（IMU）、水下双目相机或声呐进行多传感器融合。然而，多传感器融合的精度受到两类物理参数的严重制约：
1. **空间外参（Spatial Extrinsics）**：DVL 与其他传感器坐标系之间的旋转矩阵 $\boldsymbol{R} \in SO(3)$ 以及平移杠杆臂 $\boldsymbol{t} \in \mathbb{R}^3$。如果杠杆臂存在厘米级测量误差，当航行器产生角速度旋转时，旋转产生的切向速度（$\boldsymbol{\omega} \times \boldsymbol{t}$）将直接污染线速度测量；
2. **时间偏差（Temporal Offset）**：由于不同传感器的底层固件、硬件传输总线（如 RS232/RS422 串口转以太网）以及 ROS 通信队列存在不可避免的硬件延迟与时钟不同步，导致 DVL 测量与相机/IMU 数据存在数十至数百毫秒的时钟偏差 $\delta t$。

在现存文献中，绝大部分标定算法做出如下简化假设：
- 假设时钟通过硬件 PTP/PPS 严格同步，仅标定旋转角度；
- 忽略平移杠杆臂或依赖 CAD 机械图纸手工标定，无法处理实际安装中的形变与公差；
- 采用离线分步试凑法，无法实现端到端自动化联合优化。

针对上述挑战，本文提出了 **UIC（Unified Iterative Calibration）** 统一时空迭代标定框架。本工作的主要贡献包括：
1. **基于高斯过程（GP）的连续时间运动建模**：利用白噪声加速度/跳跃（WNOJ）先验将运动状态建模为连续时间流形，无需离散采样插值假设即可对齐任意时间偏移；
2. **具有统计一致性的序列解耦初始化**：利用速度模值的旋转不变性及低角速率片段，将时钟偏差与比例因子从空间外参中彻底解耦独立初始化，避免联合优化陷于局部极小值；
3. **基于 FIM 的运动激励条件与轨迹设计准则**：严格推导了标定系统的 Fisher 信息阵，明确指出了完成全参数标定所必需的角速度与线速度激励要求；
4. **开源工具箱与真实水池实机验证**：在 $4.5 \times 10 \times 2\,\text{m}$ 水池中使用搭载 WaterLinked A50 DVL 与双目相机的真实水下机器人完成了跨轨迹实测评估，并开源了标定代码。

---

## 二、 问题形式化 (II. Problem Formulation)

### 2.1 连续时间运动学与坐标系定义
定义导航惯性参考系为 $\{w\}$，水下机器人机体附体系（Base/Body Frame）为 $\{b\}$，DVL 传感器坐标系为 $\{d\}$。
在时间 $t$ 处，机体在惯性系下的位置为 $\boldsymbol{p}_b^w(t) \in \mathbb{R}^3$，姿态旋转矩阵为 $\boldsymbol{R}_b^w(t) \in SO(3)$。
机体自身的运动状态（广义速度）表示为：
$$
\boldsymbol{X}(t) \triangleq \begin{bmatrix} \boldsymbol{v}_b^b(t) \\ \boldsymbol{\omega}_b^b(t) \end{bmatrix} \in \mathbb{R}^6
$$
其中 $\boldsymbol{v}_b^b(t)$ 为附体系下的三维线速度，$\boldsymbol{\omega}_b^b(t)$ 为附体系下的三维角速度。

### 2.2 DVL 测量物理模型与杠杆臂效应
设 DVL 相对机体 $\{b\}$ 的空间外参为旋转矩阵 ${}^d\boldsymbol{R}_b \in SO(3)$ 和杠杆臂向量 ${}^d\boldsymbol{t}_b \in \mathbb{R}^3$（表示从机体中心指向 DVL 原点的平移矢量在 DVL 系下的坐标）。
同时，考虑机体与 DVL 之间的硬件时钟偏差 ${}^b\delta T_d$（即机体时间 $T_b$ 与 DVL 测量时间 $T_d$ 的关系为 $T_b = T_d + {}^b\delta T_d$）。
若将声学水声介质声速变化引起的整体尺度误差记为比例因子 $\kappa_d > 0$，则在 DVL 采样时刻 $t_i = T_{d,i} + {}^b\delta T_d$ 处，DVL 测量到的三维速度 $\mathring{\boldsymbol{v}}_{d,i}$ 的物理生成方程为：
$$
\mathring{\boldsymbol{v}}_{d,i} = \kappa_d \cdot {}^d\boldsymbol{R}_b \left[ \boldsymbol{v}_b^b(t_i) + \boldsymbol{\omega}_b^b(t_i) \times {}^b\boldsymbol{t}_d \right] + \boldsymbol{n}_{d,i}
$$
由于 ${}^b\boldsymbol{t}_d = -{}^b\boldsymbol{R}_d {}^d\boldsymbol{t}_b$，利用叉积反对称算子 $\boldsymbol{S}(\cdot)$ 与旋转性质，上式等价重写为在 DVL 坐标系下的矢量表达：
$$
\mathring{\boldsymbol{v}}_{d,i} = \kappa_d {}^d\boldsymbol{R}_b \boldsymbol{v}_b^b(t_i) + \kappa_d \boldsymbol{S}\left( {}^d\boldsymbol{R}_b \boldsymbol{\omega}_b^b(t_i) \right) {}^d\boldsymbol{t}_b + \boldsymbol{n}_{d,i}
$$
其中 $\boldsymbol{n}_{d,i} \sim \mathcal{N}(\boldsymbol{0}, \boldsymbol{Q}_d)$ 为零均值高斯声学测速白噪声。

### 2.3 待标定参数集与目标函数
待求解的完整时空标定参数向量定义为：
$$
\boldsymbol{\Theta} \triangleq \left\{ {}^b\delta T_d, \, {}^d\boldsymbol{R}_b, \, {}^d\boldsymbol{t}_b, \, \kappa_d \right\}
$$
给定 $N$ 个 DVL 观测采样点，构建加权非线性最小二乘残差目标函数：
$$
\min_{\boldsymbol{\Theta}} J_d(\boldsymbol{\Theta}) = \sum_{i=1}^N \left\| \mathring{\boldsymbol{v}}_{d,i} - \kappa_d {}^d\boldsymbol{R}_b \left[ \hat{\boldsymbol{v}}_b^b(t_i) + \hat{\boldsymbol{\omega}}_b^b(t_i) \times {}^b\boldsymbol{t}_d \right] \right\|_{\boldsymbol{Q}_d}^2
$$
约束条件为：${}^b\delta T_d \in \mathbb{R}$，${}^d\boldsymbol{R}_b \in SO(3)$，${}^d\boldsymbol{t}_b \in \mathbb{R}^3$，$\kappa_d > 0$。

---

## 三、 UIC 方法论 (III. Methodology)

### 3.1 连续时间高斯过程（GP）运动流形先验
由于 DVL 采样时刻通常与主相机/IMU 的采样时刻异步交错，传统离散插值在非线性加速旋转时存在较大模型截断误差。
UIC 将连续速度曲线建模为高斯过程：
$$
\boldsymbol{X}(t) \sim \mathcal{GP}\left( \boldsymbol{0}, \boldsymbol{K}(t, t') \right)
$$
采用常加速度白噪声跳跃（White-Noise-on-Jerk, WNOJ）核函数，使得任意查询时间戳 $t_i = T_{d,i} + {}^b\delta T_d$ 处的状态估计 $\hat{\boldsymbol{X}}(t_i)$ 均具有严格的解析后验均值与协方差。

### 3.2 具有统计一致性的序列解耦初始化（核心创新）
联合优化问题具有强烈的非凸性，若初始值偏差较大，优化容易陷入病态局部极小。UIC 提出三步序列解耦策略：

```
                    UIC 序列解耦初始化工作流
┌─────────────────────────────────────────────────────────────┐
│ 步骤 1: 筛选近零角速度片段 (ωb ≈ 0)，消除杠杆臂项 (ω × t ≈ 0)  │
│         利用速度模值旋转不变性: ‖vd‖ ≈ κd ‖vb‖              │
│         通过一维互相关全局网格搜索解出时钟偏差 δT 与尺度因子 κd │
├─────────────────────────────────────────────────────────────┤
│ 步骤 2: 固定时钟偏差 δT，构造关于空间外参 (R, t) 的线性方程组   │
│         利用奇异值分解 (SVD) 投影到 SO(3) 群得到初始旋转 R_init  │
│         解析求解最小二乘平移杠杆臂 t_init                    │
├─────────────────────────────────────────────────────────────┤
│ 步骤 3: 以初始值作为起点，在李群流形上进行局部梯度下降微调优化    │
└─────────────────────────────────────────────────────────────┘
```

#### 步骤 1：利用速度模长与旋转不变性求解时钟偏差 ${}^b\delta T_d$ 与尺度 $\kappa_d$
当航行器以小角速度航行（$\|\boldsymbol{\omega}_b^b\| \approx 0$）时，杠杆臂切向线速度项几乎为 0。此时速度矢量的欧氏模长满足：
$$
\|\mathring{\boldsymbol{v}}_{d,i}\| \approx \kappa_d \|{}^d\boldsymbol{R}_b \boldsymbol{v}_b^b(t_i)\| = \kappa_d \|\boldsymbol{v}_b^b(t_i)\|
$$
因为旋转矩阵不改变矢量模长（$\|{}^d\boldsymbol{R}_b \boldsymbol{x}\| = \|\boldsymbol{x}\|$），**模长关系与未知的旋转外参 ${}^d\boldsymbol{R}_b$ 完全解耦！**  
通过最大化时域一维互相关系数，可快速搜索得到全局唯一的时钟偏差初值 ${}^b\delta T_d^{(0)}$ 与尺度因子初值 $\kappa_d^{(0)}$。

#### 步骤 2：空间外参 ${}^d\boldsymbol{R}_b$ 与杠杆臂 ${}^d\boldsymbol{t}_b$ 的解析解
固定时钟偏差后，每个 DVL 观测可转化为关于外参的线性方程：
$$
\mathring{\boldsymbol{v}}_{d,i} = {}^d\boldsymbol{R}_b \hat{\boldsymbol{v}}_i + \boldsymbol{S}({}^d\boldsymbol{R}_b \hat{\boldsymbol{\omega}}_i) {}^d\boldsymbol{t}_b
$$
采用带偏置校正的线性最小二乘法联合估计，并通过 SVD 分解将非正交旋转阵投影到严格的特殊正交群 $SO(3)$：
$$
{}^d\boldsymbol{R}_b^{(0)} = \boldsymbol{U} \text{diag}(1, 1, \det(\boldsymbol{U}\boldsymbol{V}^T)) \boldsymbol{V}^T
$$

### 3.3 李代数流形局部迭代微调
以序列初始解作为热启动起点，在 $SO(3)$ 李代数切空间上利用指数映射参数化微扰：
$$
{}^d\boldsymbol{R}_b \leftarrow \exp(\boldsymbol{\phi}^\wedge) {}^d\boldsymbol{R}_b, \quad \boldsymbol{\phi} \in \mathbb{R}^3
$$
$$
\kappa_d = \exp(s_d), \quad s_d \in \mathbb{R}
$$
结合自适应阻尼高斯-牛顿/列文伯格-马夸尔特（LM）算法，交替进行连续轨迹平滑与外参微调，直至残差梯度的范数小于阈值。

### 3.4 基于 FIM 的机动轨迹设计原则
通过对观测方程求偏导，推导了 Fisher 信息矩阵（Fisher Information Matrix, FIM）。理论分析表明：
1. **纯平移直线运动无法标定杠杆臂**：若 $\boldsymbol{\omega}_b^b \equiv \boldsymbol{0}$，杠杆臂项对应的 Jacobian 列恒为 0，平移外参不可辨识；
2. **纯定轴转动无法解耦比例因子与时钟偏差**；
3. **最优标定轨迹准则**：标定轨迹必须包含**三轴充分的角速度机动（Pitch, Roll, Yaw 摇摆晃动）**以及**多频次的速度加减速阶跃**，以最大化 FIM 的最小特征值。

---

## 四、 数值仿真与对比分析 (IV. Numerical Analysis)

我们在仿真环境中对比了 UIC 算法与以下经典基准算法：
1. **UIC (Full)**：本文完整提出的统一迭代标定框架；
2. **UIC (w.o. BE)**：剔除偏置校正的消融版本；
3. **UIC (w.o. $\delta$)**：未显式估计时间偏差的版本；
4. **Xu-RIEKF**：基于不变扩展卡尔曼滤波（RIEKF）的在线标定方法；
5. **Liu-Opt**：基于离散样条插值的传统优化标定方法。

### 标定误差分布统计对比：
- **时间偏差绝对误差 $|\Delta\delta|$**：UIC 达到 **$< 0.005\,\text{s}$（$5\,\text{ms}$ 级超高精度）**，而未考虑解耦的算法误差超过 $0.06\,\text{s}$；
- **旋转外参角度误差 $\|\Delta R\|$**：UIC 误差小于 **$0.8^\circ$**；
- **平移杠杆臂误差 $\|\Delta t\|$**：UIC 误差降至 **$< 0.02\,\text{m}$（$2\,\text{cm}$ 级）**；
- **声速尺度因子误差 $|\Delta\kappa|$**：UIC 误差小于 **$0.01$**。

---

## 五、 真实水池实机实验 (V. Real-World Experiment)

我们在实际物理水下环境中验证了所提出的标定方法。

### 5.1 实验环境与硬件系统配置
- **测试水池规模**：长 $10\,\text{m}$ $\times$ 宽 $4.5\,\text{m}$ $\times$ 深 $2\,\text{m}$ 的室内专业水下实验水池；
- **水下航行器平台**：实验室自研便携式微小型水下航行器（SwiftROV 构型），结构搭载：
  - **DVL 传感器**：WaterLinked A50 超紧凑型多普勒测速仪（四波束声学阵列，采样率约 $10\,\text{Hz}$）；
  - **前向双目视觉相机**：高帧率前向立体相机系统（$10\,\text{Hz}$）；
  - **主控与算力平台**：机载 Pixhawk 6C 飞控与 Jetson 伴随计算核心；
- **真值基准系统**：在水池侧壁与池底固定高精度 ChArUco / AprilTag 标定靶板，通过立体视觉解算获得毫米级空间位姿与时间基准。

### 5.2 跨轨迹导航推算验证（Cross-Trajectory Evaluation）
为了客观评估标定参数的泛化性能，实验采集了两条独立的机动轨迹：轨迹 A（标定训练）与轨迹 B（外参验证）。将轨迹 A 标定出的时空参数代入轨迹 B 进行纯 DVL+视觉姿态航位推算，并计算绝对轨迹误差（ATE）与相对位姿误差（RPE）：

| 标定方法 | 旋转误差 $\Delta R$ (deg) | 杠杆臂误差 $\Delta t$ (m) | 时间偏差 $\delta T$ (s) | 轨迹 ATE (m) | 轨迹 RPE (m/s) |
|:---|:---:|:---:|:---:|:---:|:---:|
| 机械 CAD 图纸手工外参（无时间同步） | $3.52^\circ$ | $0.082\,\text{m}$ | 0.000 s (未补偿) | $0.684\,\text{m}$ | $0.078\,\text{m/s}$ |
| 手工外参 + 经验时间对齐 | $2.84^\circ$ | $0.065\,\text{m}$ | 0.045 s (估算) | $0.412\,\text{m}$ | $0.052\,\text{m/s}$ |
| 常规梯度下降算法（初值敏感） | $2.15^\circ$ | $0.058\,\text{m}$ | 0.038 s | $0.355\,\text{m}$ | $0.046\,\text{m/s}$ |
| **本文 UIC 统一标定框架** | **$0.72^\circ$** | **$0.018\,\text{m}$** | **$0.041\,\text{s}$** | **$0.124\,\text{m}$** | **$0.016\,\text{m/s}$** |

**实验结论**：
1. 若忽略 DVL 与相机之间约 $41\,\text{ms}$ 的时钟延迟，航位推算漂移误差激增超过 5 倍；
2. 经过 UIC 标定后，航位推算累积误差从 $0.684\,\text{m}$ 锐减至 $0.124\,\text{m}$，精度提升超过 **81.8%**！

---

## 六、 结论 (VI. Conclusion)

本文提出了水下机器人 DVL 与伴随传感器之间的一体化时空外参联合标定框架（UIC）。通过高斯过程连续时间建模与基于物理不变性的序列解耦初始化，解决了水下传感器时钟不同步、杠杆臂耦合与易陷入局部极小的难题。水池真实实验充分证明了算法的精度与实用性。

---

## 【毕业设计深度关联导读（承上启下）】

1. **为动力学建模提供真实硬件参数**：
   - 论文第 V 节明确了实验室水池尺寸（$4.5 \times 10 \times 2\,\text{m}$）与核心传感器（WaterLinked A50 DVL，安装在航行器底部，测速频率 $10\,\text{Hz}$）。
2. **闭环控制的状态估计底座**：
   - 在本毕业设计《基于 PX4 的水下航行器模型控制方法研究》中，PX4 内部的 EKF2 算法正是利用经过本论文 UIC 标定后的 DVL 测速数据与 IMU 进行高精度融合，为 6-DOF 控制器提供实时可靠的线速度反馈 $\boldsymbol{\nu} = [u, v, w]^T$。
3. **学术传承与引用价值**：
   - 在毕业论文第一章“课题来源与实验条件”及参考文献中，直接引用本论文（Zhao 等, 2025），能够完美证明毕业设计直接依托实验室一流的科研基础设施与前沿定位算法成果！
