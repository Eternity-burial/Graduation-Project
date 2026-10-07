# Johansen & Fossen《多执行器控制分配权威综述》核心精读导读

> **英文原题**：Control Allocation—A Survey  
> **论文作者**：Tor A. Johansen, Thor I. Fossen (IEEE Fellow, IFAC Fellow)  
> **所属机构**：挪威科技大学（NTNU）工程控制论系、自主海洋系统与操作中心（AMOS）  
> **出版出处**：*Automatica*, 49(5): 1087–1103, 2013 (Elsevier / IFAC Flagship Journal)  
> **学术地位**：控制科学界与海洋工程界公认最权威、被引用最多的控制分配理论长篇综述（Google Scholar 被引 2000+ 次），被誉为“过驱动多执行器控制分配领域的行业宪法与标准教科书”。

---

## 一、 为什么控制分配是过驱动系统的核心构件？

在航空航天、海洋船舶与多推进器水下航行器等现代先进运动系统中，执行机构的数量（$m$）往往大于被控自由度数目（$n$），即 $m > n$。这种构型被称为**过驱动系统（Over-actuated Systems）**。

例如，对于我们研究的实验室八推进器紧凑型水下航行器，需要控制的自由度为 6 个（或 4 个主控自由度），而可用的物理推进器为 8 个（$m=8 > n=6$）。

### 1.1 模块化解耦架构（Modular Control Architecture）
Johansen 和 Fossen 指出，将高层运动控制律与底层执行机构驱动彻底解耦为两个独立模块，是现代控制工程最伟大的范式跃迁之一：

```
                    模块化控制分配系统架构
┌────────────────┐  期望力与力矩 τ   ┌────────────────┐  物理推进器指令 u   ┌────────────────┐
│  高层运动控制律  │ ───────────────> │  底层控制分配器  │ ────────────────> │ 8推进器物理对象 │
│ (PID/NDI/SMC)  │  (n维虚拟控制量)  │ (Control Alloc) │  (m维实际执行量)  │ (Plant Actuator)
└────────────────┘                  └────────────────┘                  └────────────────┘
        ▲                                                                       │
        └──────────────────────── 传感器状态反馈 (x, v) ─────────────────────────┘
```

1. **上层控制器专注物理轨迹**：运动控制律仅需计算期望的广义虚拟控制力与力矩 $\boldsymbol{\tau}_v \in \mathbb{R}^n$（如合力与合力矩），完全无需关心各推进器的空间物理安装位置、角度倾角与饱和边界；
2. **底层分配器专注执行机构映射与约束协调**：将 $n$ 维的 $\boldsymbol{\tau}_v$ 分配给 $m$ 维的实际执行机构输入 $\boldsymbol{u} \in \mathbb{R}^m$，并在推力饱和、推力速率受限或个别推进器发生物理故障时，实现推力的自主重构与饱和解耦。

---

## 二、 控制分配的标准数学问题形式化

对于推进器固定布置的水下航行器，推力矢量合成满足**线性推力构型映射方程**：

$$
\boldsymbol{B} \boldsymbol{u} = \boldsymbol{\tau}
$$

其中：
- $\boldsymbol{B} \in \mathbb{R}^{n \times m}$ 为**控制分配矩阵（Control Allocation Matrix / Thrust Configuration Matrix）**，由各推进器的空间安装坐标位置向量 $\boldsymbol{r}_i$ 与推力矢量方向单位向量 $\boldsymbol{d}_i$ 决定（每列对应一个推进器的力与力矩矢量贡献）；
- $\boldsymbol{u} = [T_1, T_2, \dots, T_m]^T \in \mathbb{R}^m$ 为各推进器产生的推力输入；
- $\boldsymbol{\tau} = [F_x, F_y, F_z, K, M, N]^T \in \mathbb{R}^n$ 为期望广义力与力矩。

实际物理推进器存在不可逾越的物理极限约束：
1. **幅值饱和约束（Magnitude Constraints）**：
   $$
   \underline{u}_i \le u_i \le \bar{u}_i, \quad \forall i = 1, \dots, m
   $$
2. **变化率约束（Rate Constraints）**：
   $$
   |\dot{u}_i| \le \rho_i \implies \underline{u}_i(t) \le u_i(t) \le \bar{u}_i(t)
   $$

---

## 三、 四大控制分配流派深入剖析与技术比选

Johansen 和 Fossen 将数十种控制分配算法系统性地划分为四大流派：

### 3.1 显式解析分配（Unconstrained / Explicit Pseudoinverse Methods）
- **Moore-Penrose 广义逆（最小二乘伪逆）**：
  若不考虑饱和约束，寻求能耗最小（$\min \|\boldsymbol{u}\|_2^2$）的解，其唯一显式解析解为：
  $$
  \boldsymbol{u}^* = \boldsymbol{B}^{\dagger} \boldsymbol{\tau} = \boldsymbol{B}^T (\boldsymbol{B} \boldsymbol{B}^T)^{-1} \boldsymbol{\tau}
  $$
- **加权伪逆法（Weighted Pseudoinverse, WPINV）**：
  引入对角权重矩阵 $\boldsymbol{W} = \operatorname{diag}(w_1, \dots, w_m)$，目标函数为 $\min \boldsymbol{u}^T \boldsymbol{W} \boldsymbol{u}$：
  $$
  \boldsymbol{u}^* = \boldsymbol{W}^{-1} \boldsymbol{B}^T (\boldsymbol{B} \boldsymbol{W}^{-1} \boldsymbol{B}^T)^{-1} \boldsymbol{\tau}
  $$
- **评价**：计算仅涉及一次固定矩阵求逆，可在单片机或 PX4 飞控中以微秒级执行；但**在遭遇推力饱和时无法保证执行机构边界安全**。

### 3.2 启发式抗饱和分配（Heuristic Anti-Saturation Methods - 工程实战重点）
当伪逆计算出的推进器指令超过物理上限时，必须进行防饱和处理：
1. **简单硬截断法（Simple Clipping / Truncation）**：
   $$
   u_i = \operatorname{sat}(u_i^*) = \max(\underline{u}_i, \min(\bar{u}_i, u_i^*))
   $$
   - **致命缺陷（力矩方向畸变）**：截断会破坏各推进器之间的推力比例平衡，导致**实际合成力矩的方向偏离期望力矩方向**，引发剧烈的姿态失稳甚至航行器侧翻！
2. **保方向等比例缩放（Direction-Preserving Scaling / Torque-Prioritized Scaling）**：
   计算所有推进器超出限值的最大比例因子 $s$：
   $$
   s = \max_{i} \left\{ \frac{|u_i^*|}{\bar{u}_i} \right\}
   $$
   若 $s > 1$，则将所有推进器推力统一等比缩小：$\boldsymbol{u} = \frac{1}{s} \boldsymbol{u}^*$。
   - **工程价值**：严格保持了合成力与力矩的矢量方向不变（几何保形），仅牺牲推进速度，彻底避免了方向畸变引发的失控翻滚！
3. **序贯解饱和法（Sequential Desaturation - PX4 原生飞控算法）**：
   在开源飞控 PX4 中原生采用的方法。将控制轴系按优先级排序（横滚/俯仰力矩优先级 > 偏航力矩优先级 > 垂直/水平推力），当发生饱和时，优先压缩或剥离低优先级通道（如推力速度），确保姿态力矩绝不失控。

### 3.3 约束优化分配（Constrained Quadratic Programming, QP）
将控制分配问题显式建模为标准二次规划（QP）优化问题：
$$
\min_{\boldsymbol{u}} \left\{ \|\boldsymbol{B}\boldsymbol{u} - \boldsymbol{\tau}\|_{\boldsymbol{Q}}^2 + \epsilon \|\boldsymbol{u} - \boldsymbol{u}_0\|_{\boldsymbol{R}}^2 \right\}
$$
$$
\text{s.t.} \quad \underline{\boldsymbol{u}} \le \boldsymbol{u} \le \bar{\boldsymbol{u}}
$$
- **求解算法**：有效集法（Active Set Method, 如 Härkegård 2002 算法）、内点法（Interior-Point）或乘子交替方向法（ADMM）；
- **特点**：在推力饱和约束下能够找到数学上的严格全局最优解，但算法迭代次数不固定，对嵌入式飞控处理器的算力与实时性要求较高。

### 3.4 动态控制分配（Dynamic Control Allocation）
不仅考虑当前时刻的推力上限，还将前后两个采样周期的推力增量变化率 $|\boldsymbol{u}(t) - \boldsymbol{u}(t-1)| \le \Delta \boldsymbol{u}_{\max}$ 纳入优化代价函数，用于抑制电机急加减速引起的电流冲击与结构振动。

---

## 四、 对本课题八推进器推力分配的直接指导

Johansen & Fossen (2013) 为我们课题的推力分配技术方案提供了完整的理论底座：
1. **明确推力分配的本质**：八推进器 ROV 的核心任务不是凭空“设计”新数学理论，而是针对推力饱和下的非线性物理矛盾，建立**“加权伪逆基准 ➔ 保方向等比例缩放与力矩优先 ➔ PX4 序贯解饱和 ➔ 二次规划 QP 性能对比”**的系统化实现与验证；
2. **解决水下姿态倾覆的关键所在**：文献深刻揭示了“饱和截断导致力矩失真”是水下机器人翻滚事故的元凶，这正是我们开题报告中强调“推力饱和下的力矩优先与几何保形控制分配”的物理必要性！
