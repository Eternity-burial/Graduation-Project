# Thor I. Fossen《海洋航行器流体动力学与运动控制》核心讲义中文精读手册

> **原著来源**：Thor I. Fossen 教授（挪威科技大学 NTNU）研究生核心课程 *TTK4190 Guidance, Navigation and Control of Marine Craft and Drones* 官方讲义教材配套课件。  
> **整理定位**：本手册为实验室水下航行器（SwiftROV）六自由度运动学、刚体与流体动力学建模及控制分配的**底层理论母本**。对原著第 2 章（运动学与参考坐标系）、第 3 章（刚体动力学机理）以及第 6 章（第一性原理水动力模型与水动力导数）进行了**系统性、逐式逐概念的 100% 完整中文全译与工程精读批注**。

---

## 目录

- [第一篇：第 2 章 运动学与参考坐标系 (Kinematics & Reference Frames)](#第一篇第-2-章-运动学与参考坐标系)
  - [1.1 核心坐标系定义（ECI, ECEF, NED, BODY, FLOW）](#11-核心坐标系定义)
  - [1.2 欧拉角变换与旋转矩阵](#12-欧拉角变换与旋转矩阵)
  - [1.3 运动学微分方程与奇异性](#13-运动学微分方程与奇异性)
  - [1.4 单位四元数姿态表达](#14-单位四元数姿态表达)
  - [1.5 附体坐标系 (BODY) 与水流坐标系 (FLOW) 的转换](#15-附体坐标系-body-与水流坐标系-flow-的转换)
- [第二篇：第 3 章 刚体动力学机理 (Rigid-Body Kinetics)](#第二篇第-3-章-刚体动力学机理)
  - [2.1 质心（CG）处的牛顿-欧拉运动学方程](#21-质心cg处的牛顿-欧拉运动学方程)
  - [2.2 任意坐标原点（CO）处的运动方程平移变换](#22-任意坐标原点co处的运动方程平移变换)
  - [2.3 刚体惯性矩阵 $\boldsymbol{M}_{RB}$ 的标准矩阵-矢量表达与性质](#23-刚体惯性矩阵-boldsymbolm_rb-的标准矩阵-矢量表达与性质)
  - [2.4 刚体科氏力与向心力矩阵 $\boldsymbol{C}_{RB}(\boldsymbol{\nu})$ 的参数化构造（拉格朗日反对称形式）](#24-刚体科氏力与向心力矩阵-boldsymbolc_rbboldsymbolnu-的参数化构造)
  - [2.5 线性化 6-DOF 刚体动力学小扰动方程](#25-线性化-6-dof-刚体动力学小扰动方程)
- [第三篇：第 6 章 水动力学与第一性原理操纵模型 (Hydrodynamics & Maneuvering Models)](#第三篇第-6-章-水动力学与第一性原理操纵模型)
  - [3.1 第一性原理 6-DOF 操纵动力学总方程](#31-第一性原理-6-dof-操纵动力学总方程)
  - [3.2 水动力导数：附加质量矩阵 $\boldsymbol{M}_A$ 的物理机理与频域极限](#32-水动力导数附加质量矩阵-boldsymbolm_a-的物理机理与频域极限)
  - [3.3 水动力附加质量引起的科氏力与向心力 $\boldsymbol{C}_A(\boldsymbol{\nu})$](#33-水动力附加质量引起的科氏力与向心力-boldsymbolc_aboldsymbolnu)
  - [3.4 水动力阻尼矩阵 $\boldsymbol{D}(\boldsymbol{\nu})$：线性摩擦与二次非线性压差涡流阻力](#34-水动力阻尼矩阵-boldsymboldboldsymbolnu线性摩擦与二次非线性压差涡流阻力)
  - [3.5 静水力重浮力恢复力与力矩矢量 $\boldsymbol{g}(\boldsymbol{\eta})$（稳度与不倒翁机制）](#35-静水力重浮力恢复力与力矩矢量-boldsymbolgboldsymenta)
- [第四篇：八推进器控制分配数学机理 (8-Thruster Control Allocation)](#第四篇八推进器控制分配数学机理)
  - [4.1 广义推力-PWM 静态映射曲线](#41-广义推力-pwm-静态映射曲线)
  - [4.2 $6 \times 8$ 推力配置矩阵 $\boldsymbol{B}$ 的空间几何构造](#42-6-times-8-推力配置矩阵-boldsymbolb-的空间几何构造)
  - [4.3 Moore-Penrose 广义伪逆分配法与推力饱和等比缩放](#43-moore-penrose-广义伪逆分配法与推力饱和等比缩放)

---

# 第一篇：第 2 章 运动学与参考坐标系

### 本章学习目标
- 深刻理解地理参考坐标系（NED）、地心地固参考坐标系（ECEF）与附体参考坐标系（BODY）的标准定义；
- 掌握水流参考坐标系（FLOW）的定义及其在流体动力学阻力计算中的决定性作用；
- 熟练写出欧拉角与单位四元数的旋转矩阵与微分运动学变换方程。

---

### 1.1 核心坐标系定义

在海洋工程中，为了严密描述航行器在三维空间中的运动，SNAME (1950) 与 Fossen 规范确立了以下相互嵌套的右手直角参考坐标系：

```
                           空间参考坐标系层次关系
       {i}: 地心惯性系 (ECI)
            │ (地球自转 ωe)
            ▼
       {e}: 地心地固系 (ECEF)
            │ (当地切平面投影 WGS 84)
            ▼
       {n}: 北东地坐标系 (NED) ──[水平/深度导航基准]
            │
            │ 欧拉角旋转 J1(η)
            ▼
       {b}: 附体坐标系 (BODY) ──[固定在机器人本体, FRD]
            │
            │ 攻角 α 与侧滑角 β
            ▼
       {f}: 水流坐标系 (FLOW) ──[决定相对水流阻力与升力]
```

#### 1. 地心惯性参考坐标系 $\{i\}$ (ECI: Earth-Centered Inertial Frame)
- **原点**：地球质心；
- **轴向**：$z_i$ 轴指向地球自转北极，$x_i$ 轴指向春分点，$y_i$ 轴在赤道平面内正交构成右手系。
- **物理意义**：牛顿运动定律仅在严格的非加速惯性系中严格成立。在常规近水面/水池水下机器人作业中，地球自转角速度极其微弱，通常忽略柯氏加速度，将局部切平面近似为惯性系。

#### 2. 地心地固参考坐标系 $\{e\}$ (ECEF: Earth-Centered Earth-Fixed Frame)
- **原点**：地球质心；
- **轴向**：固定在地球表面，随着地球以角速度 $\omega_e \approx 7.2921 \times 10^{-5}\,\text{rad/s}$ 绕 $z_i$ 轴自转。$x_e$ 轴通过本初子午线与赤道的交点。

#### 3. 北-东-地地理参考坐标系 $\{n\}$ (NED: North-East-Down Frame)
- **定义**：定义在地球参考椭球体（WGS 84）局部切平面上的切坐标系；
- **轴向**：
  - $x_n$ 轴指向**地理真北（True North）**；
  - $y_n$ 轴指向**地理正东（True East）**；
  - $z_n$ 轴垂直于参考椭球面并**正向朝下（Down）**。
- **工程价值**：海洋航行器（潜艇、ROV、水面艇）通用此坐标系作为导航与定深基准。**$z_n$ 朝下使得下潜深度（Depth）天然为正数**。

#### 4. 附体参考坐标系 $\{b\}$ (BODY: Body-Fixed Frame)
- **定义**：固连在水下航行器壳体结构上的运动坐标系；
- **轴向（FRD 规范）**：
  - $x_b$ 轴为航行器**纵轴（Longitudinal Axis）**，从尾部指向艏部（Forward）；
  - $y_b$ 轴为航行器**横轴（Transversal Axis）**，指向右舷（Starboard / Right）；
  - $z_b$ 轴为航行器**立轴（Normal Axis）**，从甲板垂直指向底部龙骨（Down）。

> **与机器人学 ROS REP-103 坐标系的无缝接轨**：  
> 机器人学上层（ROS/ROS2）通用 FLU（前-左-上）与 ENU（东-北-天）。两者转换仅为确定镜像映射：
> $$x_{\text{FLU}} = x_{\text{FRD}}, \quad y_{\text{FLU}} = -y_{\text{FRD}}, \quad z_{\text{FLU}} = -z_{\text{FRD}}$$

#### 5. 水流参考坐标系 $\{f\}$ (FLOW: Body-Fixed Flow Axes Frame)
- **定义**：原点与附体系一致，但通过绕 $y_b$ 轴旋转攻角 $\alpha$（Angle of Attack）与绕 $z_b$ 轴旋转侧滑角 $\beta$（Sideslip Angle）对齐于航行器相对水流的速度矢量 $\boldsymbol{\nu}_r$。
- **物理意义**：水动力升力和迎风阻力必须在水流坐标系下才能精确计算，阻力方向天然反向于相对流速方向。

---

### 1.2 欧拉角变换与旋转矩阵

航行器附体系 $\{b\}$ 相对地理系 $\{n\}$ 的姿态由三个欧拉角表达：
$$\boldsymbol{\Theta} = [\phi, \theta, \psi]^T$$
- $\phi$：横滚角（Roll，绕 $x$ 轴）；
- $\theta$：俯仰角（Pitch，绕 $y$ 轴）；
- $\psi$：偏航角（Yaw，绕 $z$ 轴）。

按航空航海标准 **$z-y-x$ 旋转顺序（Tait-Bryan 序列）**，附体系到地理系的旋转变换矩阵 $\boldsymbol{R}_b^n(\boldsymbol{\Theta}) \in SO(3)$ 为：
$$
\boldsymbol{R}_b^n(\boldsymbol{\Theta}) = \boldsymbol{R}_{z,\psi} \boldsymbol{R}_{y,\theta} \boldsymbol{R}_{x,\phi}
$$
展开得完整表达式（简写 $c\cdot = \cos(\cdot), s\cdot = \sin(\cdot)$）：
$$
\boldsymbol{R}_b^n(\boldsymbol{\Theta}) = \begin{bmatrix}
c\psi c\theta & -s\psi c\phi + c\psi s\theta s\phi & s\psi s\phi + c\psi s\theta c\phi \\
s\psi c\theta & c\psi c\phi + s\psi s\theta s\phi & -c\psi s\phi + s\psi s\theta c\phi \\
-s\theta & c\theta s\phi & c\theta c\phi
\end{bmatrix}
$$
**重要正交性质**：
$$
(\boldsymbol{R}_b^n)^{-1} = (\boldsymbol{R}_b^n)^T = \boldsymbol{R}_n^b, \quad \det(\boldsymbol{R}_b^n) = +1
$$

---

### 1.3 运动学微分方程与奇异性

六自由度位置与速度向量定义为：
$$
\boldsymbol{\eta} = [\boldsymbol{p}^n, \boldsymbol{\Theta}]^T = [x, y, z, \phi, \theta, \psi]^T \in \mathbb{R}^6
$$
$$
\boldsymbol{\nu} = [\boldsymbol{\nu}_1, \boldsymbol{\nu}_2]^T = [u, v, w, p, q, r]^T \in \mathbb{R}^6
$$
其中 $u,v,w$ 分别为附体系纵荡、横荡、垂荡线速度；$p,q,r$ 分别为横滚、俯仰、偏航角速率。

**六自由度运动学微分方程统一写为**：
$$
\dot{\boldsymbol{\eta}} = \boldsymbol{J}(\boldsymbol{\eta}) \boldsymbol{\nu} \iff \begin{bmatrix} \dot{\boldsymbol{p}}^n \\ \dot{\boldsymbol{\Theta}} \end{bmatrix} = \begin{bmatrix} \boldsymbol{R}_b^n(\boldsymbol{\Theta}) & \boldsymbol{0}_{3 \times 3} \\ \boldsymbol{0}_{3 \times 3} & \boldsymbol{T}_\Theta(\boldsymbol{\Theta}) \end{bmatrix} \begin{bmatrix} \boldsymbol{\nu}_1 \\ \boldsymbol{\nu}_2 \end{bmatrix}
$$
其中欧拉角速率变换矩阵 $\boldsymbol{T}_\Theta(\boldsymbol{\Theta})$ 为：
$$
\boldsymbol{T}_\Theta(\boldsymbol{\Theta}) = \begin{bmatrix}
1 & \sin\phi \tan\theta & \cos\phi \tan\theta \\
0 & \cos\phi & -\sin\phi \\
0 & \sin\phi / \cos\theta & \cos\phi / \cos\theta
\end{bmatrix}
$$

> **奇异性警示（万向节死锁 Gimbal Lock）**：  
> 当俯仰角 $\theta \to \pm 90^\circ$ 时，$\cos\theta \to 0$，$\tan\theta \to \infty$，矩阵 $\boldsymbol{T}_\Theta$ 出现除以零奇异点。水下航行器若执行特技全周翻滚，必须使用四元数表示；但在常规 ROV 巡检悬停工况下，由于静水力不倒翁扶正效应，$\theta$ 维持在 $\pm 15^\circ$ 以内，欧拉角极其稳定直观。

---

### 1.4 单位四元数姿态表达

为消除奇异性，定义单位四元数 $\boldsymbol{q} = [\eta, \boldsymbol{\epsilon}^T]^T = [\eta, \epsilon_1, \epsilon_2, \epsilon_3]^T \in \mathbb{S}^3$，满足 $\eta^2 + \boldsymbol{\epsilon}^T \boldsymbol{\epsilon} = 1$。
四元数对应的旋转矩阵为：
$$
\boldsymbol{R}_b^n(\boldsymbol{q}) = \boldsymbol{I}_{3 \times 3} + 2\eta \boldsymbol{S}(\boldsymbol{\epsilon}) + 2\boldsymbol{S}^2(\boldsymbol{\epsilon})
$$
其中 $\boldsymbol{S}(\cdot)$ 为叉积对应的**反对称矩阵算子（Skew-Symmetric Operator）**：
$$
\boldsymbol{S}(\boldsymbol{a}) = \begin{bmatrix} 0 & -a_3 & a_2 \\ a_3 & 0 & -a_1 \\ -a_2 & a_1 & 0 \end{bmatrix} \implies \boldsymbol{S}(\boldsymbol{a})\boldsymbol{b} = \boldsymbol{a} \times \boldsymbol{b}
$$
四元数运动学微分方程为无奇异的线性双线性微分方程：
$$
\dot{\boldsymbol{q}} = \frac{1}{2} \begin{bmatrix} -\boldsymbol{\epsilon}^T \\ \eta \boldsymbol{I} + \boldsymbol{S}(\boldsymbol{\epsilon}) \end{bmatrix} \boldsymbol{\nu}_2
$$

---

# 第二篇：第 3 章 刚体动力学机理

### 本章学习目标
- 掌握欧拉第一和第二定律在附体运动系下的牛顿-欧拉方程表述；
- 搞清楚为什么动力学方程必须从质心（CG）平移变换到任意几何坐标原点（CO）；
- 掌握刚体惯性矩阵 $\boldsymbol{M}_{RB}$ 的标准形式与其对偶的反对称科氏力向心力矩阵 $\boldsymbol{C}_{RB}(\boldsymbol{\nu})$ 的构造方法。

---

### 2.1 质心（CG）处的牛顿-欧拉运动学方程

设质心（Center of Gravity, CG）的线速度为 $\boldsymbol{\nu}_g = [u_g, v_g, w_g]^T$，角速度为 $\boldsymbol{\omega}_{i/b}^b = [p, q, r]^T$。
由欧拉动量定理与动量矩定理，在质心 CG 处的刚体动力学方程为：
$$
m \left( \dot{\boldsymbol{\nu}}_g + \boldsymbol{\omega}_{i/b}^b \times \boldsymbol{\nu}_g \right) = \boldsymbol{f}_g^b
$$
$$
\boldsymbol{I}_g \dot{\boldsymbol{\omega}}_{i/b}^b + \boldsymbol{\omega}_{i/b}^b \times (\boldsymbol{I}_g \boldsymbol{\omega}_{i/b}^b) = \boldsymbol{m}_g^b
$$
其中 $m$ 为刚体质量，$\boldsymbol{I}_g$ 为以质心为原点的 $3 \times 3$ 转动惯量张量：
$$
\boldsymbol{I}_g = \begin{bmatrix}
I_{xx} & -I_{xy} & -I_{xz} \\
-I_{yx} & I_{yy} & -I_{yz} \\
-I_{zx} & -I_{zy} & I_{zz}
\end{bmatrix}
$$

---

### 2.2 任意坐标原点（CO）处的运动方程平移变换

在实际工程中，**严禁将坐标原点选在质心 CG**！
- **为什么？** 因为水下机器人的载荷变化（加装机械臂、水下声呐采样器）或电池仓更换会导致质心位置 $\boldsymbol{r}_g = [x_g, y_g, z_g]^T$ 发生漂移。如果坐标系跟着质心跑，所有的传感器安装外参和推进器几何位置都要重新标定！
- **正确的工程做法**：将坐标原点固定在结构中轴线的几何中心（CO: Coordinate Origin），将质心偏移量 $\boldsymbol{r}_g = [x_g, y_g, z_g]^T$ 作为变量参数。

质心速度与 CO 点速度的运动学转换关系为：
$$
\boldsymbol{\nu}_g = \boldsymbol{\nu}_o + \boldsymbol{\omega} \times \boldsymbol{r}_g = \boldsymbol{\nu}_o - \boldsymbol{S}(\boldsymbol{r}_g)\boldsymbol{\omega}
$$
代入质心动力学方程，并利用螺线变换（Screw Transformation），得到以原点 CO 表达的 6-DOF 刚体动力学方程：
$$
\boldsymbol{M}_{RB} \dot{\boldsymbol{\nu}} + \boldsymbol{C}_{RB}(\boldsymbol{\nu})\boldsymbol{\nu} = \boldsymbol{\tau}_{RB}
$$

---

### 2.3 刚体惯性矩阵 $\boldsymbol{M}_{RB}$ 的标准形式

**性质 3.1（刚体系统惯性矩阵）**：
$$
\boldsymbol{M}_{RB} = \begin{bmatrix}
m \boldsymbol{I}_{3 \times 3} & -m \boldsymbol{S}(\boldsymbol{r}_g) \\
m \boldsymbol{S}(\boldsymbol{r}_g) & \boldsymbol{I}_o
\end{bmatrix} \in \mathbb{R}^{6 \times 6}
$$
展开得完整矩阵：
$$
\boldsymbol{M}_{RB} = \begin{bmatrix}
m & 0 & 0 & 0 & m z_g & -m y_g \\
0 & m & 0 & -m z_g & 0 & m x_g \\
0 & 0 & m & m y_g & -m x_g & 0 \\
0 & -m z_g & m y_g & I_{xx} & -I_{xy} & -I_{xz} \\
m z_g & 0 & -m x_g & -I_{yx} & I_{yy} & -I_{yz} \\
-m y_g & m x_g & 0 & -I_{zx} & -I_{zy} & I_{zz}
\end{bmatrix}
$$
**数学性质**：
1. **对称正定性**：$\boldsymbol{M}_{RB} = \boldsymbol{M}_{RB}^T > 0$；
2. **解耦特性**：如果原点 CO 恰好重合于质心 CG（即 $\boldsymbol{r}_g = \boldsymbol{0}$），则右上与左下 $3 \times 3$ 块退化为零，线运动与角运动在惯性层面完全解耦。

---

### 2.4 刚体科氏力与向心力矩阵 $\boldsymbol{C}_{RB}(\boldsymbol{\nu})$ 的构造

在附体旋转坐标系下表达刚体加速度必然引出科氏力和向心力。为了满足无源性（Passivity）并便于李雅普诺夫非线性稳定性证明，$\boldsymbol{C}_{RB}(\boldsymbol{\nu})$ 必须满足**反对称性质（Skew-Symmetric Property）**：
$$
\boldsymbol{C}_{RB}(\boldsymbol{\nu}) = -\boldsymbol{C}_{RB}^T(\boldsymbol{\nu}) \implies \boldsymbol{\nu}^T \boldsymbol{C}_{RB}(\boldsymbol{\nu}) \boldsymbol{\nu} \equiv 0
$$
这在物理上意味着：**科氏力与向心力是做功为零的虚力，不改变航行器的动能**。

**拉格朗日标准反对称参数化形式**：
$$
\boldsymbol{C}_{RB}(\boldsymbol{\nu}) = \begin{bmatrix}
\boldsymbol{0}_{3 \times 3} & -m \boldsymbol{S}(\boldsymbol{\nu}_1) - m \boldsymbol{S}(\boldsymbol{\nu}_2)\boldsymbol{S}(\boldsymbol{r}_g) \\
-m \boldsymbol{S}(\boldsymbol{\nu}_1) + m \boldsymbol{S}(\boldsymbol{r}_g)\boldsymbol{S}(\boldsymbol{\nu}_2) & -\boldsymbol{S}(\boldsymbol{I}_o \boldsymbol{\nu}_2)
\end{bmatrix}
$$
其中：
- $\boldsymbol{\nu}_1 = [u, v, w]^T$ 为线速度；
- $\boldsymbol{\nu}_2 = [p, q, r]^T$ 为角速度。

---

# 第三篇：第 6 章 水动力学与第一性原理操纵模型

### 本章学习目标
- 掌握水动力第一性原理下完整的 6-DOF 操纵方程；
- 搞懂附加质量矩阵 $\boldsymbol{M}_A$ 的物理实质与低频/高频极限；
- 掌握水动力阻尼为何拆分为“线性层流阻尼 + 二次非线性湍流压差阻力”；
- 搞清重力与浮力的偏心如何形成“水下不倒翁”静态恢复力矩 $\boldsymbol{g}(\boldsymbol{\eta})$。

---

### 3.1 第一性原理 6-DOF 操纵动力学总方程

水下航行器在流体中运动时，周围流体反作用于本体的广义水动力包括：**流体惯性力（附加质量）、流体粘性阻尼、静水力恢复力与推进器控制力**。标准 Fossen 动力学总方程写为：

$$\boxed{\boldsymbol{M}\dot{\boldsymbol{\nu}} + \boldsymbol{C}(\boldsymbol{\nu})\boldsymbol{\nu} + \boldsymbol{D}(\boldsymbol{\nu})\boldsymbol{\nu} + \boldsymbol{g}(\boldsymbol{\eta}) = \boldsymbol{\tau} + \boldsymbol{\tau}_d}$$

各矩阵项的严格分解如下：
- **总系统惯性矩阵**：$\boldsymbol{M} = \boldsymbol{M}_{RB} + \boldsymbol{M}_A \in \mathbb{R}^{6 \times 6}$
- **总科氏向心力矩阵**：$\boldsymbol{C}(\boldsymbol{\nu}) = \boldsymbol{C}_{RB}(\boldsymbol{\nu}) + \boldsymbol{C}_A(\boldsymbol{\nu}) \in \mathbb{R}^{6 \times 6}$
- **总水动力阻尼矩阵**：$\boldsymbol{D}(\boldsymbol{\nu}) = \boldsymbol{D}_{\text{lin}} + \boldsymbol{D}_{\text{quad}}(\boldsymbol{\nu}) \in \mathbb{R}^{6 \times 6}$
- **静水力恢复力矢量**：$\boldsymbol{g}(\boldsymbol{\eta}) \in \mathbb{R}^6$
- **控制输入矢量**：$\boldsymbol{\tau} = \boldsymbol{B} \boldsymbol{T} \in \mathbb{R}^6$
- **外部水流/浪涌扰动**：$\boldsymbol{\tau}_d \in \mathbb{R}^6$

---

### 3.2 附加质量矩阵 $\boldsymbol{M}_A$ 的物理机理与水动力导数

#### 1. 物理本质：被加速流体的“虚加惯性”
当刚体在无界流体中以加速度 $\dot{\boldsymbol{\nu}}$ 运动时，周围被强制推开的流体流动具有流体动能 $T_A$。流体动能随时间的变化率等效于在刚体上施加了一个反向反作用力：
$$
T_A = \frac{1}{2} \boldsymbol{\nu}^T \boldsymbol{M}_A \boldsymbol{\nu} \implies \boldsymbol{\tau}_A = -\boldsymbol{M}_A \dot{\boldsymbol{\nu}}
$$

#### 2. SNAME 水动力导数符号体系
在流体力学中，水动力对加速度的偏导数统称为水动力导数。例如，纵荡方向外力 $X$ 对纵荡加速度 $\dot{u}$ 的偏导记为 $X_{\dot{u}}$：
$$
X_A = X_{\dot{u}} \dot{u} + X_{\dot{v}} \dot{v} + \dots + X_{\dot{r}} \dot{r}
$$
因此，附加质量矩阵各元素定义为：
$$
\boldsymbol{M}_A = -\begin{bmatrix}
X_{\dot{u}} & X_{\dot{v}} & X_{\dot{w}} & X_{\dot{p}} & X_{\dot{q}} & X_{\dot{r}} \\
Y_{\dot{u}} & Y_{\dot{v}} & Y_{\dot{w}} & Y_{\dot{p}} & Y_{\dot{q}} & Y_{\dot{r}} \\
Z_{\dot{u}} & Z_{\dot{v}} & Z_{\dot{w}} & Z_{\dot{p}} & Z_{\dot{q}} & Z_{\dot{r}} \\
K_{\dot{u}} & K_{\dot{v}} & K_{\dot{w}} & K_{\dot{p}} & K_{\dot{q}} & K_{\dot{r}} \\
M_{\dot{u}} & M_{\dot{v}} & M_{\dot{w}} & M_{\dot{p}} & M_{\dot{q}} & M_{\dot{r}} \\
N_{\dot{u}} & N_{\dot{v}} & N_{\dot{w}} & N_{\dot{p}} & N_{\dot{q}} & N_{\dot{r}}
\end{bmatrix} \in \mathbb{R}^{6 \times 6}
$$

#### 3. SwiftROV 对称性对矩阵的简化
根据流体动力学理论，在理想不可压缩无旋流体中：
1. $\boldsymbol{M}_A$ 严格对称且正定：$\boldsymbol{M}_A = \boldsymbol{M}_A^T > 0$；
2. **双耐压舱紧凑构型对称性**：SwiftROV 具有左右（port-starboard）对称面与前后近似对称性。非对角耦合项极微弱，在低速机动中可近似为**纯对角矩阵**：
$$
\boldsymbol{M}_A \approx \text{diag}(-X_{\dot{u}}, -Y_{\dot{v}}, -Z_{\dot{w}}, -K_{\dot{p}}, -M_{\dot{q}}, -N_{\dot{r}})
$$

---

### 3.3 水动力科氏力与向心力 $\boldsymbol{C}_A(\boldsymbol{\nu})$

与刚体惯性类似，附加质量矩阵伴随着旋转运动也会激发出流体科氏力。利用 Kirchhoff 动量方程，$\boldsymbol{C}_A(\boldsymbol{\nu})$ 同样可构造为标准反对称矩阵：
设流体虚加动量为 $\boldsymbol{\mu} = \boldsymbol{M}_A \boldsymbol{\nu} = [\boldsymbol{a}_1^T, \boldsymbol{a}_2^T]^T$，其中 $\boldsymbol{a}_1, \boldsymbol{a}_2 \in \mathbb{R}^3$，则：
$$
\boldsymbol{C}_A(\boldsymbol{\nu}) = \begin{bmatrix}
\boldsymbol{0}_{3 \times 3} & -\boldsymbol{S}(\boldsymbol{a}_1) \\
-\boldsymbol{S}(\boldsymbol{a}_1) & -\boldsymbol{S}(\boldsymbol{a}_2)
\end{bmatrix}
$$
满足 $\boldsymbol{C}_A(\boldsymbol{\nu}) = -\boldsymbol{C}_A^T(\boldsymbol{\nu})$，对系统的无源性能量守恒起到了理论支撑。

---

### 3.4 水动力阻尼矩阵 $\boldsymbol{D}(\boldsymbol{\nu})$

水动力阻尼来源于四种物理现象：
1. **辐射阻尼（Radiation Damping）**：物体在自由液面振荡产生表面重力波向外辐射能量（水池深潜作业时此项为 0）；
2. **表面附面层摩擦阻力（Skin Friction）**：粘性流体在航行器表面的剪切切应力（线性主导）；
3. **压差涡流脱落阻力（Form Drag / Vortex Shedding）**：钝头耐压舱、圆柱电池筒迎流分离导致尾部形成低压涡流区（二次方非线性主导）；
4. **横倾与升沉横流阻尼（Cross-Flow Drag）**：大侧偏角或急转弯时的横向撞水阻力。

**工程分解模型**：
$$
\boldsymbol{D}(\boldsymbol{\nu}) = \boldsymbol{D}_{\text{lin}} + \boldsymbol{D}_{\text{quad}}(\boldsymbol{\nu})
$$
对角化展开式：
$$
\boldsymbol{D}_{\text{lin}} = -\text{diag}(X_u, Y_v, Z_w, K_p, M_q, N_r)
$$
$$
\boldsymbol{D}_{\text{quad}}(\boldsymbol{\nu}) = -\text{diag}(X_{u|u}|u|, Y_{v|v}|v|, Z_{w|w}|w|, K_{p|p}|p|, M_{q|q}|q|, N_{r|r}|r|)
$$
阻尼力对各通道的贡献为：
$$
F_{\text{drag}, i} = -(D_{\text{lin}, i} + D_{\text{quad}, i}|\nu_i|)\nu_i
$$
- 低速漂移时（$\nu_i \approx 0.1\,\text{m/s}$），线性项占主导；
- 高速巡航时（$\nu_i \approx 0.8 \sim 1.5\,\text{m/s}$），二次方非线性阻力剧增，成为推进器主要克服的阻力。

---

### 3.5 静水力恢复力与力矩矢量 $\boldsymbol{g}(\boldsymbol{\eta})$

静水力由刚体重力 $W = mg$ 与阿基米德浮力 $B = \rho g \nabla$ 产生。
- 重心坐标：$\boldsymbol{r}_G = [x_g, y_g, z_g]^T$；
- 浮心坐标：$\boldsymbol{r}_B = [x_b, y_b, z_b]^T$。

水下航行器通常调配为**微正浮力（$B \gtrsim W$）**或中性浮力（$B = W$），以确保突发断电时能够自动上浮脱险。

#### 1. 恢复力与力矩推导
重力和浮力在附体系下的投影为：
$$
\boldsymbol{f}_G^b = \boldsymbol{R}_n^b \begin{bmatrix} 0 \\ 0 \\ W \end{bmatrix}, \quad \boldsymbol{f}_B^b = -\boldsymbol{R}_n^b \begin{bmatrix} 0 \\ 0 \\ B \end{bmatrix}
$$
合力与合力矩矢量为：
$$
\boldsymbol{g}(\boldsymbol{\eta}) = -\begin{bmatrix}
\boldsymbol{f}_G^b + \boldsymbol{f}_B^b \\
\boldsymbol{r}_G \times \boldsymbol{f}_G^b + \boldsymbol{r}_B \times \boldsymbol{f}_B^b
\end{bmatrix}
$$
展开得完整 6-DOF 恢复力矢量：
$$
\boldsymbol{g}(\boldsymbol{\eta}) = \begin{bmatrix}
(W - B)\sin\theta \\
-(W - B)\cos\theta\sin\phi \\
-(W - B)\cos\theta\cos\phi \\
-(y_g W - y_b B)\cos\theta\cos\phi + (z_g W - z_b B)\cos\theta\sin\phi \\
(z_g W - z_b B)\sin\theta + (x_g W - x_b B)\cos\theta\cos\phi \\
-(x_g W - x_b B)\cos\theta\sin\phi - (y_g W - y_b B)\sin\theta
\end{bmatrix}
$$

#### 2. “不倒翁”固有稳度条件
对于中性对称设计的 SwiftROV（$W = B$，$x_g = x_b = 0$，$y_g = y_b = 0$）：
$$
\boldsymbol{g}(\boldsymbol{\eta}) = \begin{bmatrix}
0 \\
0 \\
0 \\
(z_g - z_b) W \cos\theta \sin\phi \\
(z_g - z_b) W \sin\theta \\
0
\end{bmatrix}
$$
- **初稳性高（Metacentric Height）**：$\overline{GM} = z_g - z_b$。
- **物理判定**：在 NED 坐标系下，$z$ 向下为正。因为耐压舱（空气）在顶部，电池在底部，所以**浮心在重心上方（$z_b < z_g \implies z_g - z_b > 0$）**。
- **结论**：当横滚角 $\phi > 0$（向右倾斜）时，恢复力矩产生一个**负向的扶正力矩**；俯仰角 $\theta > 0$（抬头）时产生**负向抬头力矩**。航行器具有极强的被动静态自稳定不倒翁特性！

---

# 第四篇：八推进器控制分配数学机理

### 4.1 推进器推力映射模型

单台无刷推进器（如配备 3 叶螺旋桨的 W60 水下推进器）的稳态轴向推力与电机转速 $n$（或 PWM 控制信号）成二次方关系：
$$
T_i = C_T \cdot \text{sign}(n_i) \cdot n_i^2 \approx K_T \cdot \text{sign}(\text{PWM}_i - 1500) \cdot (\text{PWM}_i - 1500)^2
$$
推力具有物理饱和边界：
$$
T_{\min} \le T_i \le T_{\max} \quad (i = 1, 2, \dots, 8)
$$
在控制器设计中，运动控制层直接计算**期望广义力/力矩 $\boldsymbol{\tau}_c \in \mathbb{R}^6$**，而由**控制分配器（Control Allocator）**解算各推进器的具体推力指令。

---

### 4.2 $6 \times 8$ 推力配置矩阵 $\boldsymbol{B}$ 的构造

设第 $i$ 台推进器的安装位置坐标矢量为 $\boldsymbol{r}_i = [x_i, y_i, z_i]^T$，推力方向单位矢量为 $\boldsymbol{d}_i = [d_{ix}, d_{iy}, d_{iz}]^T$。
单台推进器推力 $T_i$ 在机体质心产生的合力和合力矩为：
$$
\boldsymbol{\tau}_i = \begin{bmatrix} \boldsymbol{f}_i \\ \boldsymbol{m}_i \end{bmatrix} = \begin{bmatrix} \boldsymbol{d}_i \\ \boldsymbol{r}_i \times \boldsymbol{d}_i \end{bmatrix} T_i = \boldsymbol{b}_i T_i
$$
综合 8 台推进器，建立推力配置方程：
$$
\boldsymbol{\tau}_c = \sum_{i=1}^8 \boldsymbol{b}_i T_i = \boldsymbol{B} \boldsymbol{T}
$$
其中控制分配矩阵 $\boldsymbol{B} \in \mathbb{R}^{6 \times 8}$：
$$
\boldsymbol{B} = [\boldsymbol{b}_1, \boldsymbol{b}_2, \boldsymbol{b}_3, \boldsymbol{b}_4, \boldsymbol{b}_5, \boldsymbol{b}_6, \boldsymbol{b}_7, \boldsymbol{b}_8]
$$

#### SwiftROV 推进器几何布局特性：
- **$T_1 \sim T_4$（水平矢量推进器）**：$d_{iz} = 0$，推力方向沿 $\pm 45^\circ$ 安装于四个角，其生成的列向量仅在第 1、2、6 行非零，纯粹负责纵荡（Surge $X$）、横荡（Sway $Y$）与偏航（Yaw $N$）；
- **$T_5 \sim T_8$（垂直垂向推进器）**：$d_{ix} = 0, d_{iy} = 0, d_{iz} = 1$，竖直安装于四个象限，其生成的列向量仅在第 3、4、5 行非零，纯粹负责垂荡（Heave $Z$）、横滚（Roll $K$）与俯仰（Pitch $M$）；
- **结构稀疏解耦特性**：矩阵 $\boldsymbol{B}$ 呈现出高度优雅的块状稀疏结构：
$$
\boldsymbol{B} = \begin{bmatrix}
\boldsymbol{B}_{\text{horiz}} & \boldsymbol{0}_{3 \times 4} \\
\boldsymbol{0}_{3 \times 4} & \boldsymbol{B}_{\text{vert}}
\end{bmatrix}_{6 \times 8}
$$
这证明了水平机动控制与垂直升沉俯仰控制在推进器硬件层面是**完全正交解耦的**！

---

### 4.3 Moore-Penrose 广义伪逆分配法与推力饱和等比缩放

由于未知量推力指令有 8 个，而约束控制自由度为 6 个，系统处于**过驱动冗余状态（Over-Actuated System）**。

#### 1. 最小能耗欧式范数解（Moore-Penrose Pseudoinverse）
寻找使得推进器能量损耗 $\sum T_i^2 = \boldsymbol{T}^T \boldsymbol{T}$ 最小的无约束极值解：
$$
\min_{\boldsymbol{T}} \frac{1}{2} \boldsymbol{T}^T \boldsymbol{T} \quad \text{s.t.} \quad \boldsymbol{B} \boldsymbol{T} = \boldsymbol{\tau}_c
$$
构造拉格朗日乘子函数并求导，得全局解析唯一解：
$$
\boldsymbol{T} = \boldsymbol{B}^\dagger \boldsymbol{\tau}_c = \boldsymbol{B}^T (\boldsymbol{B} \boldsymbol{B}^T)^{-1} \boldsymbol{\tau}_c
$$
其中 $\boldsymbol{B}^\dagger \in \mathbb{R}^{8 \times 6}$ 为 Moore-Penrose 广义伪逆。因为矩阵 $\boldsymbol{B}$ 行满秩，$(\boldsymbol{B}\boldsymbol{B}^T)^{-1}$ 恒存在。在飞控启动初始化时离线计算一次 $\boldsymbol{B}^\dagger$，运行时仅需执行一次 $8 \times 6$ 矩阵与 6 维矢量的乘法，运算耗时小于 $10\,\mu\text{s}$！

#### 2. 推力饱和等比缩放（Saturation Desaturation / Scaling）
当某一推进器计算值超出物理限幅（$|T_i| > T_{\max}$）时，若直接截断（Clipping）会破坏分配矩阵的力矩平衡比例，导致航行器姿态失稳打滚。
工程中采用**等比比例缩放策略**：
$$
s = \max \left( 1.0, \frac{\max_{i} |T_i|}{T_{\max}} \right)
$$
$$
\boldsymbol{T}_{\text{safe}} = \frac{1}{s} \boldsymbol{T}
$$
- 若所有推力均在限幅内，则 $s = 1.0$，输出原指令；
- 若出现超限，所有推力等比衰减，**严格保住 6 个自由度的力和力矩方向不变**，优先确保闭环姿态与航向稳定！

---

## 总结：理论到毕设仿真的映射清单

| 理论矩阵 / 矢量 | 物理含义 | 在毕设仿真/PX4中的实现方式 |
|:---|:---|:---|
| $\boldsymbol{J}(\boldsymbol{\eta})$ | 6-DOF 运动学坐标系转换 | `J_eta = kinematics(eta)`，将附体系速度转换为大地系位姿积分 |
| $\boldsymbol{M}_{RB}$ | 刚体质量与惯量矩阵 | 直接从 SolidWorks 模型点击“质量属性”导出数值赋给仿真常数矩阵 |
| $\boldsymbol{M}_A$ | 水动力附加质量 | 对角矩阵，通过水池自由衰减周期试验或水动力估算公式获取 |
| $\boldsymbol{D}(\boldsymbol{\nu})$ | 线性与二次非线性阻尼 | 对角矩阵，通过水池阶跃恒推力测定最大巡航航速拟合获取 |
| $\boldsymbol{g}(\boldsymbol{\eta})$ | 重力浮力恢复力矩 | 根据浮心与重心垂向偏心距 $z_g - z_b$ 计算，提供被动自稳不倒翁力矩 |
| $\boldsymbol{B}$ | $6 \times 8$ 推力配置矩阵 | 从 SolidWorks 测得 8 个推进器的安装位置 $\boldsymbol{r}_i$ 与方向 $\boldsymbol{d}_i$ 构造常数矩阵 |
| $\boldsymbol{B}^\dagger$ | 伪逆控制分配器 | 离线计算 `B_pinv = B.T @ np.linalg.inv(B @ B.T)`，实时解算各电机推力 |
