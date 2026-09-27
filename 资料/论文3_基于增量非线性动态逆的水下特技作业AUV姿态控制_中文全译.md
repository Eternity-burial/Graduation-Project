# 基于增量非线性动态逆的水下特技干预 AUV Cuttlefish 姿态控制

**英文原题**：Attitude Control of the Hydrobatic Intervention AUV Cuttlefish using Incremental Nonlinear Dynamic Inversion  
**作者**：Tom Slawik, Shubham Vyas, Leif Christensen, Frank Kirchner  
**机构**：德国人工智能研究中心（DFKI GmbH）机器人创新中心（RIC），德国不来梅  
**会议/发表**：IEEE/RSJ International Conference / DFKI Underactuated Lab  
**开源代码库**：https://github.com/dfki-ric-underactuated-lab/auv_control_indi  
**实验视频**：https://youtu.be/8u8k607lpn4  

---

## 摘要 (Abstract)

在本文中，我们提出了一种基于**增量非线性动态逆（Incremental Nonlinear Dynamic Inversion, INDI）**的自主水下航行器（AUV）姿态控制方案。

传统的基于模型的控制器严重依赖于受控系统的精确数学模型，然而对于受到高度非线性水动力学效应影响的水下航行器而言，建立精确模型极其困难。INDI 通过引入高频加速度反馈与执行器输出反馈，对非线性系统进行逐拍增量局部线性化，从而实现了**“用传感器测量精度换取动力学模型精度”**。

现有的 INDI 控制研究主要集中在无人机（UAV）领域，而在海洋机器人领域的应用几乎处于空白。本文针对具有极高挑战性的 **90° 俯仰特技过渡机动（Pitch-up Maneuver）**开展研究——双臂水下干预作业型 AUV “Cuttlefish” 从水平巡航姿态快速切换到垂直干预作业姿态。

我们在德国 DFKI RIC 的大型海洋试验水池中，将 INDI 与经典的基于模型反馈线性化（Feedback Linearization, FBL）控制方案进行了严格的实机对比测试。试验结果表明，无论是在大角度动态过渡机动阶段还是在长时间定点悬停阶段，INDI 都能使 AUV 保持显著更优的平稳性，且空间漂移量远小于模型依赖型控制器。

---

## 一、引言 (I. INTRODUCTION)

随着海洋“蓝色经济”的蓬勃发展，海底基础设施（如现代化水产养殖网箱、海上风电场导管架及水下变电站）建设规模迅速扩大。这导致对水下无人化自主运维作业的需求日益迫切。

* **传统作业方式的局限**：人工潜水员作业存在巨大的人身安全风险，作业深度受限，且高度依赖气象海况窗口；遥控无人潜水器（ROV）虽能进行深海重载作业，但必须依赖大型专用支持母船与脐带缆绞车系统，运维成本高昂且机动受限。
* **干预型 AUV（I-AUV）的崛起**：配备作业机械臂的新型干预潜水器（如 AUV Cuttlefish）旨在实现全自主作业。Cuttlefish 配备 8 个推进器与双机械臂，具备**水下特技机动能力（Hydrobatics）**，能够在水体中实现任意 360° 空间姿态变换，从而深入复杂水下钢结构狭窄空间作业。此外，该潜水器还能主动调节其质心（CoM）与浮心（CoB）位置，以满足不同作业任务的静水力稳定性需求。

### 核心难点：水动力学黑盒与建模瓶颈
当 AUV 进行大角度变姿态机动（如从水平巡航翻转至垂直直立）时，船体周围流场急剧变化，产生极强的非线性耦合效应，包括：
1. 时变附加质量（Added Mass）；
2. 高度非线性的流体动压力与速度平方阻尼项（Quadratic Damping）；
3. 艇体与机械臂伸展时的复杂流体相互干扰。

传统基于模型的方法（如反馈线性化 FBL、滑模控制等）需要对上述参数进行精密辨识。若辨识出的阻尼偏大或偏小，模型补偿项就会反向施加错误推力，引发严重振荡或持续漂移。

### 增量非线性动态逆（INDI）的破局之道
增量非线性动态逆（INDI）是一种基于传感器的增量线性化控制理论。其核心理念是：**不试图去预测或计算复杂的外部气动/水动力学非线性函数，而是利用当前时刻 IMU 测量的实际加速度增量来抵消上一时刻的全部非线性效应，仅保留系统的控制效能映射关系**。

本文首次将 INDI 拓展至 6 自由度水下航行器的运动与姿态控制，并开源了全部实现方案。

---

## 二、控制系统实现与数学推导 (II. IMPLEMENTATION)

### A. 水下航行器动力学方程 (Underwater Vehicle Dynamics)
根据 Fossen 海洋航行器动力学标准建模理论，6 自由度 AUV 在机体坐标系下的运动学与动力学方程表示为：

$$\boldsymbol{M}\dot{\boldsymbol{\nu}} + \boldsymbol{C}(\boldsymbol{\nu})\boldsymbol{\nu} + \boldsymbol{D}(\boldsymbol{\nu})\boldsymbol{\nu} + \boldsymbol{g}(\boldsymbol{\eta}) = \boldsymbol{\tau}$$
$$\dot{\boldsymbol{\eta}} = \boldsymbol{J}(\boldsymbol{\eta})\boldsymbol{\nu}$$

各变量物理定义如下：
* $\boldsymbol{\eta} = [x, y, z, \phi, \theta, \psi]^T \in \mathbb{R}^6$：大地惯性系（NED）下的位置与欧拉角姿态；
* $\boldsymbol{\nu} = [u, v, w, p, q, r]^T \in \mathbb{R}^6$：机体坐标系下的线速度 $(u, v, w)$ 与角速度 $(p, q, r)$；
* $\boldsymbol{M} = \boldsymbol{M}_{RB} + \boldsymbol{M}_A \in \mathbb{R}^{6 \times 6}$：刚体质量惯性矩阵 $\boldsymbol{M}_{RB}$ 与水动力附加质量矩阵 $\boldsymbol{M}_A$ 之和；
* $\boldsymbol{C}(\boldsymbol{\nu}) = \boldsymbol{C}_{RB}(\boldsymbol{\nu}) + \boldsymbol{C}_A(\boldsymbol{\nu})$：刚体与水动力科氏/向心力矩阵；
* $\boldsymbol{D}(\boldsymbol{\nu}) = \boldsymbol{D}_{lin} + \boldsymbol{D}_{quad}(\boldsymbol{\nu})$：水动力线性阻尼与非线性二次阻尼对角矩阵；
* $\boldsymbol{g}(\boldsymbol{\eta}) \in \mathbb{R}^6$：重力与浮力产生的恢复力与恢复力矩矢量；
* $\boldsymbol{\tau} \in \mathbb{R}^6$：8 个推进器在机体六轴上合成的广义控制力与力矩；
* $\boldsymbol{J}(\boldsymbol{\eta})$：从机体坐标系速度映射到大地坐标系速度的转换雅可比矩阵。

---

### B. 对比基准：经典反馈线性化 (Feedback Linearization, FBL)
定义非线性动力学总和向量场：
$$\boldsymbol{f}(\boldsymbol{\nu}, \boldsymbol{\eta}) = \boldsymbol{C}(\boldsymbol{\nu})\boldsymbol{\nu} + \boldsymbol{D}(\boldsymbol{\nu})\boldsymbol{\nu} + \boldsymbol{g}(\boldsymbol{\eta})$$

引入虚拟控制变量 $\boldsymbol{a}_{ref} = \dot{\boldsymbol{\nu}}_{ref} = \boldsymbol{K}_\nu (\boldsymbol{\nu}_{ref} - \boldsymbol{\nu})$，经典基于模型的反馈线性化控制律为：
$$\boldsymbol{\tau}_{ref} = \boldsymbol{M} \boldsymbol{a}_{ref} + \boldsymbol{f}(\boldsymbol{\nu}, \boldsymbol{\eta})$$

* **本质缺陷**：该方法必须实时精确计算 $\boldsymbol{f}(\boldsymbol{\nu}, \boldsymbol{\eta})$ 中的每一个参数。一旦阻尼或恢复力矩存在微小辨识误差，系统就无法实现真正的解耦和精确补偿。

---

### C. 水下 6 自由度增量非线性动态逆控制 (INDI)
INDI 对受控系统在上一采样控制时刻 $(t_0)$ 附近进行一阶泰勒级数展开：

$$\boldsymbol{M}\dot{\boldsymbol{\nu}} = \boldsymbol{M}\dot{\boldsymbol{\nu}}_0 + \left. \frac{\partial (\boldsymbol{\tau} - \boldsymbol{f})}{\partial \boldsymbol{\nu}} \right|_0 (\boldsymbol{\nu} - \boldsymbol{\nu}_0) + \left. \frac{\partial (\boldsymbol{\tau} - \boldsymbol{f})}{\partial \boldsymbol{\tau}} \right|_0 (\boldsymbol{\tau} - \boldsymbol{\tau}_0)$$

由于控制回路采样频率极高（例如 $50\text{ Hz} \sim 100\text{ Hz}$），在相邻采样间隔 $\Delta t$ 内，航行器速度变化量 $\Delta \boldsymbol{\nu}$ 所引起的流体动力学力变化相比执行机构推力增量 $\Delta \boldsymbol{\tau}$ 是极小量，可以忽略：

$$\boldsymbol{M}\dot{\boldsymbol{\nu}} \approx \boldsymbol{M}\dot{\boldsymbol{\nu}}_0 + (\boldsymbol{\tau} - \boldsymbol{\tau}_0)$$

令系统期望达到的加速度为 $\boldsymbol{a}_{ref}$，用经过低通滤波的传感器实测加速度 $\dot{\boldsymbol{\nu}}_f$ 替代 $\dot{\boldsymbol{\nu}}_0$，用当前推进器估算的实际推力输出 $\boldsymbol{\tau}_f$ 替代 $\boldsymbol{\tau}_0$，推导得出 **INDI 控制律**：

$$\boldsymbol{\tau}_{ref} = \boldsymbol{\tau}_f + \boldsymbol{M} (\boldsymbol{a}_{ref} - \dot{\boldsymbol{\nu}}_f)$$

> **核心优势总结**：
> 1. **彻底免除阻尼与科氏力建模**：整个公式中完全不包含 $\boldsymbol{D}(\boldsymbol{\nu})$、$\boldsymbol{C}(\boldsymbol{\nu})$ 和 $\boldsymbol{g}(\boldsymbol{\eta})$！
> 2. **参数极简**：仅需配置惯性矩阵 $\boldsymbol{M}$，即可实现六自由度完全解耦控制。
> 3. **抗未建模扰动极强**：机械臂运动引起的水动力突变会被 IMU 加速度计在下一拍立即捕捉并自动增量抵消。

---

### D. 推进器控制分配 (Thruster Allocation)
AUV Cuttlefish 配置有 8 个大功率无刷推进器，控制分配负责将 6 自由度广义力/力矩指令 $\boldsymbol{\tau}_{ref} \in \mathbb{R}^6$ 分配为 8 个推进器的推力设定值 $\boldsymbol{u} \in \mathbb{R}^8$：

$$\boldsymbol{\tau} = \boldsymbol{B} \boldsymbol{u}$$

采用加权 Moore-Penrose 伪逆求解：
$$\boldsymbol{u} = \boldsymbol{B}^\dagger \boldsymbol{\tau}_{ref} = \boldsymbol{B}^T (\boldsymbol{B} \boldsymbol{B}^T)^{-1} \boldsymbol{\tau}_{ref}$$
其中 $\boldsymbol{B} \in \mathbb{R}^{6 \times 8}$ 为推力配置矩阵（Thruster Configuration Matrix）。

---

### E. 四元数姿态外环控制器 (Attitude Outer Loop)
由于 Cuttlefish 需要进行 90° 甚至更大角度的空间翻转，传统欧拉角描述在俯仰 $\pm 90^\circ$ 时存在万向节死锁（Gimbal Lock）奇异性。外环采用基于李群 $SO(3)$ 的姿态误差控制律：

$$\boldsymbol{\omega}_{ref}(\boldsymbol{R}, \boldsymbol{R}_d) = \boldsymbol{K}_\Omega \sum_{i=1}^3 \boldsymbol{e}_i \times (\boldsymbol{R}_d^T \boldsymbol{R} \boldsymbol{e}_i)$$

其中 $\boldsymbol{R} \in SO(3)$ 为当前姿态旋转矩阵，$\boldsymbol{R}_d \in SO(3)$ 为目标姿态旋转矩阵，$\boldsymbol{e}_i$ 为标准正交基向量，$\boldsymbol{K}_\Omega$ 为正定对角增益矩阵。

---

## 三、水池对比试验与结果分析 (III. EVALUATION)

### A. 试验平台与水动力模型辨识
* **试验平台**：AUV Cuttlefish（长 $2.8\text{ m}$，宽 $2.0\text{ m}$，高 $0.8\text{ m}$），内置军工级高精度光纤陀螺惯导系统（PHINS Compact C3）。
* **试验环境**：DFKI 室内海洋试验水池（长 $24\text{ m}$、宽 $18\text{ m}$、水深 $8\text{ m}$）。
* **水动力参数辨识**：记录 57 分钟实测航行数据，分别辨识出两套模型供 FBL 控制器使用：
  1. **线性阻尼模型（Linear Drag FBL）**
  2. **二次非线性阻尼模型（Quadratic Drag FBL）**

---

### B. 试验 1：90° 俯仰特技过渡机动 (Pitch-up Maneuver)
* **动作过程**：AUV 在 5 秒内从水平巡航姿态快速俯仰翻转 90° 进入垂直直立姿态，并在直立姿态稳定保持 300 秒。
* **稳态姿态角度误差对比**：
  * **INDI 控制器**：稳态角度误差仅为 **0.0829°**；
  * **线性阻尼 FBL**：稳态误差为 1.3459°；
  * **二次阻尼 FBL**：稳态误差为 1.6897°。

* **过渡机动过程中的速度/角速度跟踪均方根误差 (RMSE)**：

| 自由度 (DOF) | INDI 控制器 | 线性模型 FBL | 二次模型 FBL | 性能对比分析 |
| :--- | :--- | :--- | :--- | :--- |
| **Surge (前进线速度)** | **0.39 mm/s** | 0.55 mm/s | 1.04 mm/s | INDI 纵向速度跟踪最稳 |
| **Sway (侧移线速度)** | **0.12 mm/s** | 0.34 mm/s | 0.64 mm/s | INDI 横向几乎零漂移 |
| **Heave (垂荡线速度)** | **0.73 mm/s** | 0.69 mm/s | 1.11 mm/s | 垂向保持性能均优异 |
| **Roll (横滚角速度)** | **0.022°/s** | 0.043°/s | 0.063°/s | **INDI 稳定性提升近 3 倍** |
| **Pitch (俯仰角速度)** | **0.328°/s** | 0.321°/s | 0.317°/s | 三者平分秋色 |
| **Yaw (偏航角速度)** | **0.053°/s** | 0.051°/s | 0.108°/s | 航向锁定稳健 |

> **关键物理反思**：为什么二次非线性阻尼 FBL 的跟踪表现反而劣于线性 FBL？
> * 因为在低速与变姿态翻转时，水流处于层流与湍流过渡区，二次阻尼项参数在低速下极难精准辨识；辨识模型高估了阻尼后，FBL 控制回路施加了过量的反向抵消力，反而放大了误差。

---

### C. 试验 2：300 秒垂直直立悬停抗漂移测试 (Station Keeping)
在水下保持 90° 垂直直立状态 300 秒，记录水平面 $(x, y)$ 漂移轨迹：
* **INDI**：在 $x$ 轴与 $y$ 轴的空间位置漂移 **< 0.1 m**（几乎完全锁定在原地）；
* **线性阻尼 FBL**：在 $x$ 轴累计漂移达 **1.5 m**；
* **二次阻尼 FBL**：在 $x$ 轴累计漂移超过 **2.5 m**。
* **悬停功率消耗**：
  * INDI 连续功耗为 2231 W；
  * 线性 FBL 为 2246 W；
  * 二次 FBL 为 2274 W。
  * 表明 INDI 在消除漂移的同时，并未引入高频抖动或额外能耗。

---

## 四、主要结论与未来展望 (IV. CONCLUSION)

1. **水下 INDI 控制的开创性验证**：本文首次在真实 6-DOF 水下航行器上成功实现了增量非线性动态逆控制，水池试验全面证明其在大角度特技机动与定点悬停中显著超越经典基于模型的反馈线性化。
2. **极小化建模负担**：传统水下控制需要辨识数十个复杂流体动力学系数，而 INDI 仅需一个惯性矩阵 $\boldsymbol{M}$ 和推进器配置矩阵 $\boldsymbol{B}$，大幅缩短了水下机器人的控制调试周期。
3. **未来研究方向**：INDI 天然具备推力故障容错潜力（Fault-Tolerant Control）。当推进器发生局部失效或水草缠绕衰减时，结合加速度反馈的自适应 INDI 有望在无需显式故障诊断模块的情况下直接实现重构控制。
