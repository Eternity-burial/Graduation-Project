# Timothy Prestero《REMUS水下航行器六自由度仿真模型验证》核心精读手册

> **原著文献**：Timothy Prestero. *Verification of a Six-Degree of Freedom Simulation Model for the REMUS Autonomous Underwater Vehicle*. Master's Thesis, Massachusetts Institute of Technology (MIT) & Woods Hole Oceanographic Institution (WHOI), September 2001.  
> **整理定位**：本手册为水下航行器（AUV/ROV）六自由度全状态动力学建模、水动力参数辨识体系（拖曳水池阻力实验与经验半经验公式）及控制系统仿真的**工程学术标杆文献**。对原著全部 9 大章节的机理建模、水动力导数解析推导、拖曳水池实验设计与海试验证进行了**系统性、逐式逐参数的中文精读导读**。

---

## 目录

- [第一篇：研究背景、平台架构与基本建模假设 (Introduction & Assumptions)](#第一篇研究背景平台架构与基本建模假设)
  - [1.1 REMUS 研发背景与研究动机](#11-remus-研发背景与研究动机)
  - [1.2 几何外形（Myring 剖面）与质量分布特性](#12-几何外形myring-剖面与质量分布特性)
  - [1.3 环境与动力学基本假设（刚体、无限深水流场、忽略波浪）](#13-环境与动力学基本假设)
- [第二篇：坐标系定义与六自由度运动学 (Kinematics & Coordinate Systems)](#第二篇坐标系定义与六自由度运动学)
  - [2.1 附体坐标系 (BODY) 与惯性坐标系 (INERTIAL) 定义](#21-附体坐标系-body-与惯性坐标系-inertial-定义)
  - [2.2 欧拉角变换与速度/角速度映射矩阵](#22-欧拉角变换与速度角速度映射矩阵)
- [第三篇：刚体动力学方程 (Rigid-Body Dynamics)](#第三篇刚体动力学方程)
  - [3.1 牛顿-欧拉方程在任意原点（浮心 CB）处的展开](#31-牛顿-欧拉方程在任意原点浮心-cb-处的展开)
  - [3.2 刚体惯性矩阵 $\boldsymbol{M}_{RB}$ 与科氏向心力矩阵 $\boldsymbol{C}_{RB}$](#32-刚体惯性矩阵-boldsymbolm_rb-与科氏向心力矩阵-boldsymbolc_rb)
- [第四篇：水动力学机理、水动力导数与外力建模 (Hydrodynamic Modeling)](#第四篇水动力学机理水动力导数与外力建模)
  - [4.1 静水力学：重力与浮力恢复力/力矩 $\boldsymbol{g}(\boldsymbol{\eta})$](#41-静水力学重力与浮力恢复力力矩-boldsymbolgboldsymeta)
  - [4.2 水动力附加质量矩阵 $\boldsymbol{M}_A$ 与附加科氏力 $\boldsymbol{C}_A$（椭球体解析积分与细长体理论）](#42-水动力附加质量矩阵-boldsymbolm_a-与附加科氏力-boldsymbolc_a)
  - [4.3 水动力阻尼 $\boldsymbol{D}(\boldsymbol{\nu})$：线性阻尼与非线性交叉阻尼项](#43-水动力阻尼-boldsymboldboldsymbolnu线性阻尼与非线性交叉阻尼项)
  - [4.4 执行机构建模：推进器推力与尾舵/升降舵水动力模型](#44-执行机构建模推进器推力与尾舵升降舵水动力模型)
  - [4.5 总体非线性运动方程集成与矩阵形式](#45-总体非线性运动方程集成与矩阵形式)
- [第五篇：拖曳水池实验与阻力参数辨识 (Tow Tank Experiments)](#第五篇拖曳水池实验与阻力参数辨识)
  - [5.1 实验装置：柔性安装架与拖曳水池拖车系统](#51-实验装置柔性安装架与拖曳水池拖车系统)
  - [5.2 纵向阻力与攻角阻力测试数据与信号去噪处理](#52-纵向阻力与攻角阻力测试数据与信号去噪处理)
  - [5.3 基于部件拆解的阻力模型 (Component-Based Drag Model)](#53-基于部件拆解的阻力模型)
- [第六篇：海试数据验证、模型对比与控制器设计 (Sea Trials & Control)](#第六篇海试数据验证模型对比与控制器设计)
  - [6.1 海试航路追踪与传感器数据融合回放](#6.1-海试航路追踪与传感器数据融合回放)
  - [6.2 仿真模型输出与实测动态响应对比分析](#62-仿真模型输出与实测动态响应对比分析)
  - [6.3 垂向深度平面线性化模型与状态反馈控制律设计](#63-垂向深度平面线性化模型与状态反馈控制律设计)
- [第七篇：对实验室八推进器 ROV（SwiftROV）的借鉴与启示](#第七篇对实验室八推进器-rovswiftrov的借鉴与启示)

---

# 第一篇：研究背景、平台架构与基本建模假设

### 1.1 REMUS 研发背景与研究动机

REMUS（Remote Environmental Monitoring UnitS）是由 Woods Hole Oceanographic Institution（WHOI）伍兹霍尔海洋研究所 Christopher von Alt 团队研制的微小型、低成本、高机动性自主水下航行器（AUV）。  
在 Prestero 2001 开展研究之前，绝大多数 AUV 导航与控制算法依赖高度简化的无耦合运动方程，无法精准预测复杂流场下的三维机动特性。Prestero 论文的**核心使命**在于：**为 REMUS AUV 构建第一座完整的六自由度非线性非定常水动力学仿真模型，并通过严格的拖曳水池实验与真实海试数据，实现模型参数闭环标定与精度验证**。

### 1.2 几何外形与结构参数

REMUS 采用经典的鱼雷形回转体构型，外形母线由 **Myring 剖面公式** 定义：
- **前段（Bow）**：半椭球形导流罩；
- **中段（Midbody）**：标准圆柱耐压壳体；
- **后段（Tail）**：平滑收缩的锥体，尾端对称布置十字舵（两副水平尾舵、两副垂直方向舵）及单螺旋桨推进器。

| 物理参数 | 符号表示 | 数值 / 单位 | 物理意义 |
| :--- | :---: | :---: | :--- |
| 全长 | $L$ | $1.33\,\text{m}$ | 航行器总长度 |
| 壳体最大直径 | $d$ | $0.191\,\text{m}$ | 耐压舱外径 |
| 空气中重量 | $W$ | $299\,\text{N}$ ($m = 30.48\,\text{kg}$) | 总质量 |
| 水中净浮力 | $B$ | $306\,\text{N}$ | 排水浮力（具有微小正浮力 $\approx 7\,\text{N}$） |
| 浮心位置（CB） | $\boldsymbol{r}_B$ | $[0, 0, 0]^T\,\text{m}$ | **坐标系原点设定在浮心（CB）** |
| 重心位置（CG） | $\boldsymbol{r}_G$ | $[0, 0, 0.0196]^T\,\text{m}$ | 重心位于浮心正下方 $1.96\,\text{cm}$（提供极强横滚/俯仰复原力） |
| 绕各轴惯性矩 | $I_{xx}, I_{yy}, I_{zz}$ | $0.177, 3.45, 3.45\,\text{kg}\cdot\text{m}^2$ | 细长体对称分布 |

### 1.3 建模基本假设

1. **刚体假设**：航行器在运动过程中形变忽略不计，质量分布恒定；
2. **无限深水无界流场**：假设远离水面、海底及池壁，忽略自由液面兴波效应与壁面近地效应；
3. **低马赫数与不可压缩流体**：海水密度 $\rho = 1025\,\text{kg/m}^3$ 为常数；
4. **准定常流体动力分解**：将流体作用力正交分解为：静水力（重力与浮力）、理想流体无粘附加质量惯性力、粘性水动力阻尼力、执行机构操纵力。

---

# 第二篇：坐标系定义与六自由度运动学

### 2.1 坐标系定义

Prestero 遵循 SNAME（1950）海洋工程规范，定义了两个右手笛卡尔正交坐标系：
1. **地固惯性坐标系** $\{n\}$：NED（北-东-地），原点固定于水面某一基准点，$x$ 轴指向正北，$y$ 轴指向正东，$z$ 轴垂直向下指向地心。
2. **附体坐标系** $\{b\}$：原点位于航行器的**浮心（Center of Buoyancy, CB）**：
   - $x_b$ 轴沿航行器纵轴指向艏部（向前）；
   - $y_b$ 轴正交指向航行器右舷（向右）；
   - $z_b$ 轴垂直指向航行器龙骨底部（向下）。

### 2.2 状态矢量与运动学变换

定义航行器的六自由度位置/姿态矢量 $\boldsymbol{\eta}$ 与附体速度/角速度矢量 $\boldsymbol{\nu}$：
$$\boldsymbol{\eta} = [x, y, z, \phi, \theta, \psi]^T \in \mathbb{R}^6$$
$$\boldsymbol{\nu} = [u, v, w, p, q, r]^T \in \mathbb{R}^6$$

运动学微分方程为：
$$\dot{\boldsymbol{\eta}} = \boldsymbol{J}(\boldsymbol{\eta}) \boldsymbol{\nu} = \begin{bmatrix} \boldsymbol{R}_b^n(\boldsymbol{\Theta}) & \boldsymbol{0}_{3\times 3} \\ \boldsymbol{0}_{3\times 3} & \boldsymbol{T}_\Theta(\boldsymbol{\Theta}) \end{bmatrix} \begin{bmatrix} \boldsymbol{\nu}_1 \\ \boldsymbol{\nu}_2 \end{bmatrix}$$

其中线速度旋转矩阵 $\boldsymbol{R}_b^n(\boldsymbol{\Theta})$ 为经典的 $Z$-$Y$-$X$ 欧拉角变换序列（Yaw-Pitch-Roll）：
$$\boldsymbol{R}_b^n = \begin{bmatrix} c\psi c\theta & -s\psi c\phi + c\psi s\theta s\phi & s\psi s\phi + c\psi s\theta c\phi \\ s\psi c\theta & c\psi c\phi + s\psi s\theta s\phi & -c\psi s\phi + s\psi s\theta c\phi \\ -s\theta & c\theta s\phi & c\theta c\phi \end{bmatrix}$$

角速度转换矩阵 $\boldsymbol{T}_\Theta(\boldsymbol{\Theta})$：
$$\begin{bmatrix} \dot{\phi} \\ \dot{\theta} \\ \dot{\psi} \end{bmatrix} = \begin{bmatrix} 1 & \sin\phi\tan\theta & \cos\phi\tan\theta \\ 0 & \cos\phi & -\sin\phi \\ 0 & \sin\phi/\cos\theta & \cos\phi/\cos\theta \end{bmatrix} \begin{bmatrix} p \\ q \\ r \end{bmatrix}$$
> **注**：当俯仰角 $\theta \to \pm 90^\circ$ 时存在欧拉角万向节死锁奇异性，REMUS 在常规水平巡航与定深工况下俯仰角限制在 $\pm 30^\circ$ 以内。

---

# 第三篇：刚体动力学方程

### 3.1 浮心坐标原点处的刚体动力学

由于坐标原点选在浮心 $\text{CB}$，重心位置为 $\boldsymbol{r}_G = [x_G, y_G, z_G]^T$（对于 REMUS，严格对齐后 $x_G \approx 0, y_G \approx 0, z_G > 0$），牛顿-欧拉方程可写为：

$$\boldsymbol{M}_{RB} \dot{\boldsymbol{\nu}} + \boldsymbol{C}_{RB}(\boldsymbol{\nu}) \boldsymbol{\nu} = \boldsymbol{\tau}_{RB}$$

### 3.2 刚体惯性矩阵 $\boldsymbol{M}_{RB}$

$$\boldsymbol{M}_{RB} = \begin{bmatrix}
m & 0 & 0 & 0 & m z_G & -m y_G \\
0 & m & 0 & -m z_G & 0 & m x_G \\
0 & 0 & m & m y_G & -m x_G & 0 \\
0 & -m z_G & m y_G & I_{xx} & -I_{xy} & -I_{xz} \\
m z_G & 0 & -m x_G & -I_{yx} & I_{yy} & -I_{yz} \\
-m y_G & m x_G & 0 & -I_{zx} & -I_{zy} & I_{zz}
\end{bmatrix}$$

当 $x_G = y_G = 0$ 且惯性积 $I_{xy} = I_{yz} = I_{xz} \approx 0$ 时，矩阵高度稀疏解耦：
$$\boldsymbol{M}_{RB} = \operatorname{diag}\big([m, m, m, I_{xx}, I_{yy}, I_{zz}]\big) + \text{偏心耦合项}$$

---

# 第四篇：水动力学机理、水动力导数与外力建模

Prestero 论文最核心的学术贡献在于将作用在航行器上的外力精确展开为 4 大物理分支：
$$\boldsymbol{\tau}_{\text{total}} = \boldsymbol{\tau}_{\text{hydrostatic}} + \boldsymbol{\tau}_{\text{added\_mass}} + \boldsymbol{\tau}_{\text{drag}} + \boldsymbol{\tau}_{\text{control}}$$

### 4.1 静水力学恢复力 $\boldsymbol{\tau}_{\text{hydrostatic}}$

在浮心原点处，浮力矢量始终通过原点（不产生力矩），而重力矢量通过重心产生恢复力矩：
$$\boldsymbol{g}(\boldsymbol{\eta}) = \begin{bmatrix}
(W - B) \sin\theta \\
-(W - B) \cos\theta \sin\phi \\
-(W - B) \cos\theta \cos\phi \\
-z_G W \cos\theta \sin\phi \\
-z_G W \sin\theta \\
0
\end{bmatrix}$$
当航行器受扰横滚 $\phi \ne 0$ 或俯仰 $\theta \ne 0$ 时，由于 $z_G > 0$（重心在浮心下方），将产生极强的负反馈自稳力矩。

### 4.2 水动力附加质量矩阵 $\boldsymbol{M}_A$

Prestero 将 REMUS 分解为主壳体（细长回转体）与附着物（尾舵片、声呐换能器），运用细长体理论与等效椭球体势流积分计算附加质量导数：

$$\boldsymbol{M}_A = -\begin{bmatrix}
X_{\dot{u}} & 0 & 0 & 0 & 0 & 0 \\
0 & Y_{\dot{v}} & 0 & 0 & 0 & Y_{\dot{r}} \\
0 & 0 & Z_{\dot{w}} & 0 & Z_{\dot{q}} & 0 \\
0 & 0 & 0 & K_{\dot{p}} & 0 & 0 \\
0 & 0 & M_{\dot{w}} & 0 & M_{\dot{q}} & 0 \\
0 & N_{\dot{v}} & 0 & 0 & 0 & N_{\dot{r}}
\end{bmatrix}$$

**REMUS 关键附加质量导数标定值**：
- 纵向附加质量 $X_{\dot{u}} = -0.93\,\text{kg}$（仅占刚体质量的 $3\%$，流线型回转体纵向阻水极小）；
- 横向/垂向附加质量 $Y_{\dot{v}} = -35.5\,\text{kg}$, $Z_{\dot{w}} = -35.5\,\text{kg}$（**超过刚体自身质量 $30.48\,\text{kg}$，水动力附加惯性占主导**）；
- 转动附加惯量 $M_{\dot{q}} = -4.88\,\text{kg}\cdot\text{m}^2$, $N_{\dot{r}} = -4.88\,\text{kg}\cdot\text{m}^2$；
- 横滚转动附加惯量 $K_{\dot{p}} = -0.070\,\text{kg}\cdot\text{m}^2$。

### 4.3 粘性水动力阻尼模型

Prestero 建立了包含轴向非线性二次阻尼与侧向交叉耦合阻尼的高保真模型：
- **轴向总阻力**：$X_{\text{drag}} = X_{u|u|} u |u|$，其中 $X_{u|u|} = -\frac{1}{2}\rho c_d A_{\text{frontal}} = -1.62\,\text{kg/m}$；
- **侧向与垂向阻尼**（包含横向速度与转动角速度耦合）：
  $$Y_{\text{damping}} = Y_{v|v|} v |v| + Y_{r|r|} r |r| + Y_{uv} u v + Y_{ur} u r$$
  $$Z_{\text{damping}} = Z_{w|w|} w |w| + Z_{q|q|} q |q| + Z_{uw} u w + Z_{uq} u q$$
- **阻尼力矩**：
  $$K_{\text{damping}} = K_{p|p|} p |p|$$
  $$M_{\text{damping}} = M_{w|w|} w |w| + M_{q|q|} q |q| + M_{uw} u w + M_{uq} u q$$
  $$N_{\text{damping}} = N_{v|v|} v |v| + N_{r|r|} r |r| + N_{uv} u v + N_{ur} u r$$

### 4.4 执行机构模型（推进器与尾舵）

1. **推进器推力与反扭力矩**：
   $$X_{\text{prop}} = C_T \rho n^2 D^4$$
   $$K_{\text{prop}} = C_Q \rho n^2 D^5$$
   其中 $n$ 为桨叶转速（$\text{rev/s}$），$D$ 为桨叶直径。反扭力矩 $K_{\text{prop}}$ 会导致航行器在加速时产生微弱的横滚扰动。
2. **尾舵操纵力（方向舵 $\delta_r$ 与升降舵 $\delta_s$）**：
   采用升力面气动理论：
   $$Y_{\text{fin}} = Y_{uu\delta_r} u^2 \delta_r, \quad N_{\text{fin}} = N_{uu\delta_r} u^2 \delta_r$$
   $$Z_{\text{fin}} = Z_{uu\delta_s} u^2 \delta_s, \quad M_{\text{fin}} = M_{uu\delta_s} u^2 \delta_s$$
   > 操纵力与航速平方 $u^2$ 及舵偏角 $\delta$ 成正比，低速或悬停状态下舵效迅速丧失（这也是开架式/多推进器矢量 ROV 相比传统 AUV 的核心优势所在）。

---

# 第五篇：拖曳水池实验与阻力参数辨识

Prestero 在 MIT 船舶拖曳水池（MIT Tow Tank，长 $30\,\text{m}$，宽 $2.6\,\text{m}$，深 $1.5\,\text{m}$）开展了系统的物理水池实验：

```
                              MIT 拖曳水池实验布局
        拖曳轨道车 (Carriage, 匀速运行 U = 0.5 ~ 2.5 m/s)
         └── 柔性测量支柱 (Flexural Mount + 测力传感器)
              └── REMUS 实体样机 (水下沉深 0.75m, 调节攻角 α)
```

### 5.1 实验步骤与数据处理

1. **传感器静态与动态标定**：利用精密砝码在纵向与横向加载，消除柔性架弹性变形耦合；
2. **多航速阶跃拖曳**：分别在 $U \in [0.5, 1.0, 1.5, 2.0, 2.5]\,\text{m/s}$ 下进行多组拖曳测试；
3. **零位漂移与波浪瞬态滤波**：剔除启动阶段瞬态水浪反弹，截取稳定段进行低通 Butterworth 滤波与均值提取。

### 5.2 部件拆解阻力分析结果 (Component-Based Drag)

实验测得 REMUS 在 $1.54\,\text{m/s}$（3 节标准航速）下的总纵向阻力为 $15.5\,\text{N}$。各部件阻力占比如下：
- **圆柱形主壳体表面摩擦阻力**：$61\%$
- **声呐换能器与外部凸起物压差阻力**：$23\%$
- **尾部 4 片稳定尾舵寄生阻力**：$16\%$
实验与理论部件叠加模型的相对误差小于 $4.2\%$，充分证明了第一性原理水动力建模的可靠性。

---

# 第六篇：海试数据验证、模型对比与控制器设计

### 6.1 海试验证（WHOI 沿岸水域试验）

在 Woods Hole 沿海真实海况下，搭载声学多普勒流速剖面仪（ADCP）、DVL、三轴光纤陀螺仪（FOG）和高精度深度传感器，执行以下典型机动动作：
1. **直线高速巡航与加减速**；
2. **阶跃舵角转向回转回车（Turning Circles）**；
3. **正弦波定深升降机动（Zig-Zag maneuvers）**。

### 6.2 仿真与实测对比

Prestero 将海试实测的执行器输入序列（推进器转速 $n(t)$、舵角 $\delta_r(t), \delta_s(t)$）输入到 MATLAB/Simulink 6-DOF 仿真器中，对比仿真轨迹与实测轨迹：
- **速度响应**：纵向速度 $u$ 预测吻合度 $> 96\%$；
- **回转角速度**：偏航角速度 $r$ 峰值预测误差 $< 8\%$；
- **回转半径**：稳态回转半径实测值 $14.2\,\text{m}$，模型预测值 $14.9\,\text{m}$（误差仅 $4.9\%$）。

### 6.3 垂向定深控制器设计

基于对小扰动状态方程的线性化：
$$\Delta \dot{\boldsymbol{x}} = \boldsymbol{A} \Delta \boldsymbol{x} + \boldsymbol{B} \Delta u$$
状态矢量 $\Delta \boldsymbol{x} = [w, q, \theta, z]^T$，输入量为升降舵角 $\delta_s$。设计了经典带前馈的 LQR / 状态反馈控制器，成功实现了无静差定深跟踪。

---

# 第七篇：对实验室八推进器 ROV（SwiftROV）的借鉴与启示

Prestero 2001 的经典工作为本毕业设计（基于 PX4 的八推进器紧凑型水下航行器控制）提供了极为关键的技术参照与方法论启示：

1. **水动力参数解耦辨识范式**：
   - 细长回转体可拆解为回转体势流积分 + 细长体切片法（Strip Theory）；
   - 实验室 SwiftROV 虽然为非流线型双耐压舱紧凑构型，但其附加质量 $\boldsymbol{M}_A$ 同样呈现“横向/垂向远大于纵向”的显著特征，且具有极强的低速非线性二次阻尼 $\boldsymbol{D}(\boldsymbol{\nu}) = \operatorname{diag}(D_i) |\boldsymbol{\nu}|$。
2. **坐标原点选择的工程智慧**：
   - Prestero 将坐标系原点设定在**浮心（CB）**，极大地简化了重浮力恢复力矩方程，并将恢复力偶的稳定性直接与重浮心垂向偏置 $z_G - z_B$ 挂钩；
   - 本课题在构建 SwiftROV 6-DOF 动力学模型时，可借鉴原点统一选在几何对称几何中心/浮心的方法，规避恢复力矩阵的非对角混乱。
3. **执行机构特性的本质差异（AUV 舵控 vs. 八推矢量冗余）**：
   - REMUS AUV 严重依赖前进航速 $u$ 产生尾舵升力，低速或零速下完全不可控；
   - 实验室 SwiftROV 配置 8 台无刷推进器（4 台水平面 $45^\circ$ 矢量倾斜布置 + 4 台垂直面空间对称布置），在零速悬停工况下拥有完全可控的全驱动与过驱动冗余度，控制分配矩阵由 $1 \times 1$ 变为 $6 \times 8$，这也是本毕设核心任务聚焦于“抗流扰闭环控制与 $6 \times 8$ 控制分配”的根本物理与工程背景！
