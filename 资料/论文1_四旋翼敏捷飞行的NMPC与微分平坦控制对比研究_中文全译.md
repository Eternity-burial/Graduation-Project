# 四旋翼敏捷飞行的非线性模型预测控制（NMPC）与微分平坦控制（DFBC）对比研究

**英文原题**：A Comparative Study of Nonlinear MPC and Differential-Flatness-Based Control for Quadrotor Agile Flight  
**作者**：Sihao Sun (孙思豪), Angel Romero, Philipp Foehn, Elia Kaufmann, Davide Scaramuzza  
**机构**：苏黎世大学机器人与感知实验室（Robotics and Perception Group, University of Zurich, Switzerland）  
**发表期刊**：**IEEE Transactions on Robotics (T-RO), Vol. 38, No. 6, 2022**  
**视频演示**：https://youtu.be/XpuRpKHp_Bk  

---

## 摘要 (Abstract)

在复杂受限环境中实现安全导航，四旋翼无人机的高精度轨迹跟踪控制至关重要。然而，在极限敏捷飞行中，由于**高度非线性动力学、复杂的空气动力学效应以及执行机构物理约束**的共同耦合作用，高精度轨迹跟踪面临极大挑战。

在本文中，我们通过在高达 **20 m/s（即 72 km/h）** 的飞行速度和高达 **5g** 的加速度下跟踪各种极限敏捷轨迹，经验性地系统对比了当今两大主流前沿控制框架：
1. **非线性模型预测控制器（Nonlinear Model Predictive Control, NMPC）**；
2. **基于微分平坦的控制器（Differential-Flatness-Based Control, DFBC）**。

对比涵盖了高保真物理仿真与真实世界大型动作捕捉系统飞行实验，从**跟踪精度、鲁棒性、计算开销与执行器约束处理**等多个维度展开了全方位定量评估。

研究表明：
* 在跟踪**动态不可行轨迹**（Dynamically Infeasible Trajectories，即超出单电机最大推力限制的激进轨迹）时，**NMPC 展现出显著优势，其位置跟踪误差降低 48%，航向误差降低 62%**，但代价是更高的计算耗时以及潜在的数值求解收敛风险；
* 对于两种控制方法，**引入基于增量非线性动态逆（INDI）的角速度内环控制器**以及**显式建模空气动力学阻力（Aerodynamic Drag Model）**均至关重要。实飞实验表明，加入 INDI 内环可使 NMPC 与 DFBC 的轨迹跟踪误差降低 **78% 以上**。

---

## 一、引言 (I. INTRODUCTION)

四旋翼飞行器具有极高的机动敏捷性。充分发挥其敏捷性能对于时间敏感型任务至关重要，例如水下/空中搜救、管道勘测、自主探索、无人机竞速（Drone Racing）以及空中物流运输。

在敏捷极限机动中，控制系统面临三大核心瓶颈：
1. **强非线性与强耦合动力学**：大角度机动时姿态与平移完全耦合，小角度线性化假设彻底失效；
2. **空气动力学复杂性**：高速飞行时，转子叶片挥舞阻力（Rotor Drag）和机身形状阻力（Body Drag）显著增大，若忽略阻力会导致飞行器在弯道产生严重离心外洗滑动；
3. **执行机构饱和约束**：电调与电机的最大转速、推力上限以及姿态角速率限制极其严格。

为了解决上述问题，学术界形成了两大代表性控制流派：
* **NMPC**：利用受控对象动力学模型在有限预测时域内进行在线滚动时域最优控制求解，天然支持多输入多输出（MIMO）显式硬约束；
* **DFBC**：利用四旋翼系统的“微分平坦特性”（Differential Flatness），将高维非线性微分方程代数映射为平坦输出及其高阶导数，实现超低延迟的解析前馈控制。

**本文的主要学术贡献**：
1. 首次在高达 20 m/s 的极限实飞速度下，对 NMPC 与改进型 DFBC 进行全方位同台基准测试；
2. 提出将增量非线性动态逆（INDI）与空气动力学阻力模型统一融入 NMPC 和 DFBC 控制架构；
3. 系统揭示了动态可行与动态不可行轨迹、单拍计算延迟、模型不确定性及执行器饱和下的性能演化规律。

---

## 二、系统动力学与气动阻力建模 (III. PRELIMINARIES)

### A. 四旋翼非线性动力学模型
定义惯性坐标系为 $\mathcal{W} = \{x_W, y_W, z_W\}$，机体坐标系为 $\mathcal{B} = \{x_B, y_B, z_B\}$。四旋翼刚体动力学模型由下式描述：

$$\dot{\boldsymbol{\xi}} = \boldsymbol{v}$$
$$m \dot{\boldsymbol{v}} = m \boldsymbol{g}_W + \boldsymbol{R} \boldsymbol{f}_B + \boldsymbol{f}_a$$
$$\dot{\boldsymbol{q}} = \frac{1}{2} \boldsymbol{q} \otimes \begin{bmatrix} 0 \\ \boldsymbol{\Omega}_B \end{bmatrix}$$
$$\boldsymbol{J} \dot{\boldsymbol{\Omega}}_B = \boldsymbol{\tau}_B - \boldsymbol{\Omega}_B \times (\boldsymbol{J} \boldsymbol{\Omega}_B)$$

其中：
* $\boldsymbol{\xi} = [x, y, z]^T$ 为世界系位置，$\boldsymbol{v} = [\dot{x}, \dot{y}, \dot{z}]^T$ 为线速度；
* $m$ 为总质量，$\boldsymbol{g}_W = [0, 0, -g]^T$ 为重力加速度矢量；
* $\boldsymbol{R} \in SO(3)$ 为从机体系到世界系的旋转矩阵，$\boldsymbol{q} = [q_w, q_x, q_y, q_z]^T$ 为姿态四元数；
* $\boldsymbol{J}$ 为机体转动惯量矩阵，$\boldsymbol{\Omega}_B = [p, q, r]^T$ 为机体角速度；
* $\boldsymbol{f}_B = [0, 0, T]^T$ 为 4 个转子产生的机体总推力，$T = \sum_{i=1}^4 f_i$；
* $\boldsymbol{\tau}_B = [\tau_x, \tau_y, \tau_z]^T$ 为转子合成的三轴控制力矩。

### B. 空气动力学阻力模型 (Aerodynamic Drag Model)
在高速飞行时，空气阻力 $\boldsymbol{f}_a$ 不可忽略。本文采用经过风洞实验验证的复合阻力模型：
$$\boldsymbol{f}_a = - \boldsymbol{R} \boldsymbol{D}_v \boldsymbol{R}^T \boldsymbol{v}$$
其中 $\boldsymbol{D}_v = \text{diag}(d_x, d_y, d_z)$ 为对角空气阻力系数矩阵，显式包含了转子诱导阻力与机身迎风阻力。

---

## 三、控制方法设计 (IV. METHODOLOGIES)

### A. 非线性模型预测控制器 (NMPC)
NMPC 在有限时域 $\tau \in [t, t + h]$ 内将系统离散化为 $N$ 个等长步长区间 $dt = h/N$，构建如下受约束的非线性优化命题：

$$\min_{\boldsymbol{u}} \sum_{k=0}^{N-1} \left( \|\boldsymbol{x}_k - \boldsymbol{x}_{k,r}\|_{\boldsymbol{Q}}^2 + \|\boldsymbol{u}_k - \boldsymbol{u}_{k,r}\|_{\boldsymbol{Q}_u}^2 \right) + \|\boldsymbol{x}_N - \boldsymbol{x}_{N,r}\|_{\boldsymbol{Q}_N}^2$$

**约束条件**：
$$\boldsymbol{x}_{k+1} = f(\boldsymbol{x}_k, \boldsymbol{u}_k)$$
$$\boldsymbol{x}_0 = \boldsymbol{x}_{\text{init}}$$
$$\boldsymbol{\Omega}_B \in [\boldsymbol{\Omega}_{\min}, \boldsymbol{\Omega}_{\max}]$$
$$u_i \in [u_{\min}, u_{\max}], \quad i = 1, 2, 3, 4$$

其中：
* 状态向量 $\boldsymbol{x} = [\boldsymbol{\xi}^T, \dot{\boldsymbol{\xi}}^T, \boldsymbol{q}^T, \boldsymbol{\Omega}_B^T]^T \in \mathbb{R}^{13}$；
* 控制输入 $\boldsymbol{u} = [f_1, f_2, f_3, f_4]^T \in \mathbb{R}^4$ 为 4 个独立电机的推力指令；
* 求解器采用高效率 C++ 代码生成框架 **acados**，结合序列二次规划（SQP-RTI）算法在几毫秒内实时求解。

---

### B. 改进型微分平坦控制器 (DFBC)
四旋翼的平坦输出选取为位置与偏航角 $\boldsymbol{\sigma} = [x, y, z, \psi]^T$。

1. **几何前馈姿态计算**：
   考虑气动阻力后的期望合力加速度矢量为：
   $$\boldsymbol{a}_{\text{des}} = \ddot{\boldsymbol{\xi}}_{ref} + \boldsymbol{K}_p (\boldsymbol{\xi}_{ref} - \boldsymbol{\xi}) + \boldsymbol{K}_d (\dot{\boldsymbol{\xi}}_{ref} - \dot{\boldsymbol{\xi}}) - \boldsymbol{g}_W - \frac{1}{m}\boldsymbol{f}_a$$
   由此解得期望机体 $z_B$ 轴方向：
   $$\boldsymbol{z}_{B,\text{des}} = \frac{\boldsymbol{a}_{\text{des}}}{\|\boldsymbol{a}_{\text{des}}\|}$$

2. **高阶导数前馈**：
   通过对 $\boldsymbol{a}_{\text{des}}$ 进行二阶求导（涉及轨迹加加速度 Jerk 与加加加速度 Snap），可解析求出期望角速度 $\boldsymbol{\Omega}_{B,\text{des}}$ 与期望角加速度 $\dot{\boldsymbol{\Omega}}_{B,\text{des}}$。

3. **受约束二次规划控制分配 (QP Allocator)**：
   当合力需求超出单电机推力极限时，采用小型 QP 求解器在优先保证姿态控制力矩的前提下等比例缩减总推力。

---

### C. 级联增量非线性动态逆（INDI）内环设计
为隔绝转动惯量不确定性、未建模力矩与外部阵风扰动，NMPC 与 DFBC 的底层均级联了高频（500 Hz）INDI 姿态内环。

虚拟角加速度指令：
$$\boldsymbol{\nu} = \dot{\boldsymbol{\Omega}}_{B,\text{des}} + \boldsymbol{K}_p (\boldsymbol{q}_{ref} \ominus \boldsymbol{q}) + \boldsymbol{K}_d (\boldsymbol{\Omega}_{B,\text{des}} - \boldsymbol{\Omega}_B)$$

根据角加速度反馈 $\dot{\boldsymbol{\Omega}}_{B,f}$ 计算机体控制力矩增量：
$$\Delta \boldsymbol{\tau}_B = \boldsymbol{J} (\boldsymbol{\nu} - \dot{\boldsymbol{\Omega}}_{B,f})$$
$$\boldsymbol{\tau}_B = \boldsymbol{\tau}_{B,f} + \Delta \boldsymbol{\tau}_B$$

最终映射为各电机转速并直接驱动电调。

---

## 四、仿真实验与消融对比 (VI. SIMULATION EXPERIMENTS)

### A. 实验轨迹设计
测试包含了 4 种典型极限航迹：
1. **Race Track A / B / C**：专业穿越机竞速赛道，包含急转发卡弯、俯冲跃升等动作，最高速度达 20 m/s；
2. **3D Figure-8**：空间 3D 立体“8”字飞行；
3. **Looping & Barrel Roll**：包含 $360^\circ$ 滚转与俯冲回环的极限特技动作。

### B. 核心实验结果与消融数据

1. **动态可行轨迹（Dynamically Feasible）**：
   * NMPC+INDI 位置跟踪 RMSE：$0.14 \pm 0.05\text{ m}$；
   * DFBC+INDI 位置跟踪 RMSE：$0.15 \pm 0.06\text{ m}$；
   * **结论**：在轨迹物理可行时，DFBC 与 NMPC 精度几乎完全一致。

2. **动态不可行轨迹（Dynamically Infeasible，电机推力饱和）**：
   * NMPC+INDI 位置 RMSE：**$0.38\text{ m}$**，航向误差 **$3.2^\circ$**；
   * DFBC+INDI 位置 RMSE：**$0.73\text{ m}$**，航向误差 **$8.5^\circ$**；
   * **结论**：**NMPC 位置误差比 DFBC 低 48%，航向误差低 62%**。因为 NMPC 具有未来多步预测能力，能提前提前减速过弯避免剧烈饱和崩溃。

3. **消融实验：INDI 内环的决定性影响**：
   * 采用经典 PID 内环时，轨迹跟踪 RMSE 为 $0.82\text{ m}$；
   * 引入 INDI 内环后，跟踪误差直接降至 $0.18\text{ m}$（**误差降低 78%**），且完全消除了高速转弯时的姿态低频抖动。

4. **消融实验：空气动力学阻力模型**：
   * 在速度 $> 12\text{ m/s}$ 时，关闭阻力前馈会导致向心力不足，弯道最大侧向漂移超 $1.2\text{ m}$；引入阻力模型后漂移收敛至 $< 0.2\text{ m}$。

---

## 五、大型动捕实机极限飞行实验 (VII. REAL-WORLD EXPERIMENTS)

* **实验场地**：苏黎世大学 $30\text{ m} \times 30\text{ m} \times 8\text{ m}$ 大型高精度 Vicon 动作捕捉飞行大厅；
* **测试无人机**：定制竞速四旋翼，重量 $0.75\text{ kg}$，推重比高达 **4.5:1**，机载 Jetson / STM32 高性能嵌入式平台；
* **实飞最高速度**：**20 m/s (72 km/h)**，向心加速度峰值达 **5g ($49\text{ m/s}^2$)**。

实飞数据完美印证了仿真结论：
* NMPC+INDI 与 DFBC+INDI 均成功以 72 km/h 极速刷圈，轨迹重合度极高；
* DFBC 单步耗时仅 **0.05 ms**，而 NMPC 单步耗时 **2.5 ~ 4.5 ms**；
* 实飞中撤除 INDI 后，两者均在高速发卡弯出现明显发散趋势，充分证实了传感器反馈驱动的增量内环对于极限飞行的必要性。

---

## 六、综合对比与工程选型指南 (VIII. DISCUSSION & CONCLUSION)

| 评价维度 | NMPC + INDI | DFBC + INDI | 工程选型建议 |
| :--- | :--- | :--- | :--- |
| **正常可行轨迹精度** | 极高 (RMSE $\approx 0.15\text{ m}$) | 极高 (RMSE $\approx 0.15\text{ m}$) | 两者并无差异 |
| **超限不可行轨迹表现**| **极其优异 (误差低 48~62%)** | 较弱 (容易单点过冲) | 规划激进/动力受限时选 NMPC |
| **单拍计算时间** | $1.5 \sim 5.0\text{ ms}$ | **$0.02 \sim 0.06\text{ ms}$ (快 50-100 倍)** | 算力受限嵌入式端选 DFBC |
| **数学与实现复杂度** | 需配置非线性求解器与求解边界 | 纯解析代数运算，极易编写与调试 | 快速工程落地选 DFBC |
| **执行器硬约束支持** | 显式原生支持（多步时域平滑） | 依赖单拍 QP 控制分配器 | 关键安全边界选 NMPC |

**最终结论**：
1. 对于具备高质量规划器、轨迹满足动力学可行性的场景，**DFBC+INDI 是性价比最高的黄金组合**，以极低算力实现媲美 NMPC 的顶级跟踪精度；
2. 对于环境高度动态、轨迹频繁突变或执行器工作在饱和边缘的极限机动，**NMPC 是唯一能够前瞻性规避饱和的控制方案**；
3. **“INDI 姿态内环 + 空气动力学阻力补偿” 是所有高速敏捷飞行控制器的必备核心基石**。
