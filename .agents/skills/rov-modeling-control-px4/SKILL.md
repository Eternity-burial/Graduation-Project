---
name: rov-modeling-control-px4
description: >-
  Use this skill whenever the user asks to derive mathematical models, run
  system identification, design motion controllers (model-based + state feedback,
  PID, FBL, INDI), configure 8-thruster 6x8 control allocation, write Python
  6-DOF simulations, or develop/modify PX4 C++ modules and uORB topics for the
  underwater vehicle (UUV/ROV).
---

# 八推进器水下航行器建模、控制分配与 PX4 仿真规范 (ROV Modeling, Control & PX4 Skill)

本技能规范了《基于PX4的水下航行器模型控制方法研究》课题在数学推导、Python 原型仿真与 PX4/SITL (C++) 模块开发中的符号体系、坐标系约定、模块接口规范与验证指标。

> [!IMPORTANT]
> **阶段性推进原则**：由于具体水动力参数辨识结果与最终选定的细分控制律形式将随研究推进逐步确定，在编写仿真代码与文档时，必须采用**参数化配置（Config/YAML/Struct）与模块化插拔设计**，严禁将未验证的物理参数或单一算法假设硬编码死。

---

## 一、 坐标系与正方向严格约定（NED + FRD）

所有动力学推导、Python 仿真与 PX4 C++ 模块必须统一采用海洋工程（Fossen）与航空飞控（PX4）天然兼容的右手坐标系：

1. **北东地惯性坐标系 $\{n\} = (x_n, y_n, z_n)$ (NED)**：
   - $x_n$ 指北（North），$y_n$ 指东（East），$z_n$ **垂直向下指向地心（Down，即潜深正方向向下）**。
2. **附体坐标系 $\{b\} = (x_b, y_b, z_b)$ (Body-fixed / FRD)**：
   - 原点取在航行器重心（CG）或几何中心；
   - $x_b$ 沿艇体纵轴向前（Forward，纵荡 Surge $u$ 正方向）；
   - $y_b$ 沿艇体横轴向右舷（Right/Starboard，横荡 Sway $v$ 正方向）；
   - $z_b$ 沿艇体立轴向下（Down，垂荡 Heave $w$ 正方向）；
   - 姿态欧拉角 $\boldsymbol{\Theta} = [\phi, \theta, \psi]^T$ 采用 Z-Y-X 旋转顺序（横滚 Roll $\phi$、俯仰 Pitch $\theta$、偏航 Yaw $\psi$），满足右手螺旋定则。

---

## 二、 论文公式、Python 与 PX4 C++ 变量命名对齐表

为防止论文公式、Python 脚本与 C++ 代码之间出现符号混乱，强制执行以下命名映射：

| 物理意义 | 论文 LaTeX 符号 | 维度 | Python 变量名 | PX4 C++ / uORB 对应变量或主题 |
| :--- | :--- | :---: | :--- | :--- |
| 广义位置与姿态矢量 | $\boldsymbol{\eta} = [x, y, z, \phi, \theta, \psi]^T$ | $6 \times 1$ | `eta` | `vehicle_local_position` + `vehicle_attitude` |
| 附体系线速度与角速度 | $\boldsymbol{\nu} = [u, v, w, p, q, r]^T$ | $6 \times 1$ | `nu` | `vehicle_local_position` ($v_b$) + `vehicle_angular_velocity` (`xyz`) |
| 附体系加速度矢量 | $\dot{\boldsymbol{\nu}} = [\dot{u}, \dot{v}, \dot{w}, \dot{p}, \dot{q}, \dot{r}]^T$ | $6 \times 1$ | `nu_dot` | `sensor_combined` / `vehicle_angular_velocity` (差分/滤波) |
| 运动学转换矩阵 | $\boldsymbol{J}(\boldsymbol{\eta})$ | $6 \times 6$ | `J_eta` | `matrix::Dcmf(q)` (旋转矩阵) + 欧拉角速率变换 |
| 总惯性矩阵（刚体+附加质量） | $\boldsymbol{M} = \boldsymbol{M}_{RB} + \boldsymbol{M}_A$ | $6 \times 6$ | `M_total` (`M_RB`, `M_A`) | 模型参数结构体 `ModelParams` |
| 科氏力与向心力矩阵 | $\boldsymbol{C}(\boldsymbol{\nu}) = \boldsymbol{C}_{RB}(\boldsymbol{\nu}) + \boldsymbol{C}_A(\boldsymbol{\nu})$ | $6 \times 6$ | `C_nu` (`C_RB`, `C_A`) | `computeCoriolisMatrix(nu)` |
| 水动力阻尼矩阵（线性+二次） | $\boldsymbol{D}(\boldsymbol{\nu}) = \boldsymbol{D}_{\text{lin}} + \boldsymbol{D}_{\text{quad}}(\boldsymbol{\nu})$ | $6 \times 6$ | `D_nu` (`D_lin`, `D_quad`) | `computeDampingMatrix(nu)` |
| 重浮力恢复力与力矩矢量 | $\boldsymbol{g}(\boldsymbol{\eta})$ | $6 \times 1$ | `g_eta` | `computeRestoringWrench(q, W, B, r_g, r_b)` |
| 待辨识未知水动力参数集 | $\boldsymbol{\theta}$ | $p \times 1$ | `theta_id` | 辨识参数配置文件 / PX4 `ParamFloat` |
| 参考状态与跟踪误差 | $\boldsymbol{\eta}_r, \boldsymbol{\nu}_r, \boldsymbol{e}_{\eta}, \boldsymbol{e}_{\nu}$ | $6 \times 1$ | `eta_ref`, `nu_ref`, `e_eta`, `e_nu` | `vehicle_attitude_setpoint`, `vehicle_rates_setpoint` |
| 期望广义控制力与力矩 | $\boldsymbol{\tau}_c = [F_x, F_y, F_z, M_x, M_y, M_z]^T$ | $6 \times 1$ | `tau_c` | `vehicle_thrust_setpoint` ($F_{x,y,z}$) + `vehicle_torque_setpoint` ($M_{x,y,z}$) |
| 八推进器控制分配矩阵 | $\boldsymbol{B}$ | $6 \times 8$ | `B_alloc` | `control_allocator` (`ActuatorEffectivenessUUV`) |
| 各推进器推力指令矢量 | $\boldsymbol{T} = [T_1, \dots, T_8]^T$ | $8 \times 1$ | `T_cmd` | `actuator_motors` (归一化控制量 $u_i \in [-1, 1]$) |
| 推进器推力范围约束 | $[\boldsymbol{T}_{\min}, \boldsymbol{T}_{\max}]$ | $8 \times 1$ | `T_min`, `T_max` | `CA_ACT_MIN`, `CA_ACT_MAX` |
| 控制分配残差矢量 | $\boldsymbol{e}_{\tau} = \boldsymbol{\tau}_c - \boldsymbol{B}\boldsymbol{T}$ | $6 \times 1$ | `e_tau` | `control_allocator_status` (`unallocated_thrust`, `unallocated_torque`) |

---

## 三、 四大模块解耦接口规范

无论是编写 Python 仿真程序还是改造 PX4 C++ 模块，均需严格保持以下四个子模块的接口解耦（对应开题报告图 2 系统结构框图）：

1. **航行器与推进器动力学模型模块 (`Plant6DOF` & `ThrusterModel`)**：
   - 输入：8 推进器推力指令 $\boldsymbol{T}$ 及外部扰动 $\boldsymbol{\tau}_d$；
   - 内部：包含单推进器静态/动态特性映射与 6-DOF 微分方程积分器（RK4 或欧拉法）；
   - 输出：实时运动状态 $\boldsymbol{\eta}, \boldsymbol{\nu}, \dot{\boldsymbol{\nu}}$。
2. **系统辨识与模型验证模块 (`SystemIdentification`)**：
   - 输入：激励输入序列（$\boldsymbol{T}$ 或 $\boldsymbol{\tau}$）与状态响应数据（$\boldsymbol{\eta}, \boldsymbol{\nu}$）；
   - 输出：辨识修正后的标称模型参数 $(\hat{\boldsymbol{M}}, \hat{\boldsymbol{C}}, \hat{\boldsymbol{D}}, \hat{\boldsymbol{g}})$ 及模型验证拟合残差分析。
3. **基于模型与状态反馈的运动控制模块 (`MotionController`)**：
   - 输入：参考状态 $(\boldsymbol{\eta}_r, \boldsymbol{\nu}_r)$、实时状态反馈 $(\boldsymbol{\eta}, \boldsymbol{\nu})$ 及经验证的标称模型参数；
   - 结构：遵循通用弹性架构 $\boldsymbol{\tau}_c = \mathcal{F}_{\text{model}}(\hat{\boldsymbol{M}}, \hat{\boldsymbol{C}}, \hat{\boldsymbol{D}}, \hat{\boldsymbol{g}}, \boldsymbol{\eta}, \boldsymbol{\nu}, \boldsymbol{\eta}_r, \boldsymbol{\nu}_r) + \mathcal{F}_{\text{fb}}(\boldsymbol{e}_{\eta}, \boldsymbol{e}_{\nu})$，支持通过配置切换不同控制律实现（如纯反馈 PID、标称模型前馈补偿 + 状态反馈、增量动态逆 INDI 等）以开展对比实验；
   - 输出：六维期望广义控制力与力矩 $\boldsymbol{\tau}_c \in \mathbb{R}^6$。
4. **八推进器控制分配模块 (`ControlAllocator8T`)**：
   - 输入：期望广义力与力矩 $\boldsymbol{\tau}_c \in \mathbb{R}^6$、$6 \times 8$ 控制分配矩阵 $\boldsymbol{B}$、推力上下限 $[\boldsymbol{T}_{\min}, \boldsymbol{T}_{\max}]$；
   - 输出：各推进器推力指令 $\boldsymbol{T} \in \mathbb{R}^8$ 及控制分配误差 $\boldsymbol{e}_{\tau} = \boldsymbol{\tau}_c - \boldsymbol{B}\boldsymbol{T}$。

---

## 四、 PX4/SITL 相关参考资料与代码资产索引

在推进 PX4 相关工作时，优先查阅项目内已有研报与代码资产：
- PX4 与 ArduSub 水下 6-DOF 控制与分配深度对比：[PX4与ArduSub对比分析.md](file:///d:/tj/Graduation%20Project/选题/PX4与ArduSub对比分析.md)
- PX4 架构与 uORB 控制链路研报：[01_PX4架构与控制体系全景深度报告.md](file:///d:/tj/Graduation%20Project/PX4_INDI_Research/01_PX4架构与控制体系全景深度报告.md)
- INDI 嵌入式 C++ 原型实现：[RateControlINDI.hpp](file:///d:/tj/Graduation%20Project/PX4_INDI_Research/02_INDI算法在PX4中的嵌入式C++实现/RateControlINDI.hpp)、[RateControlINDI.cpp](file:///d:/tj/Graduation%20Project/PX4_INDI_Research/02_INDI算法在PX4中的嵌入式C++实现/RateControlINDI.cpp)
- Python 离线仿真原型：[indi_vs_pid_simulation.py](file:///d:/tj/Graduation%20Project/PX4_INDI_Research/03_Python离线原型与对比实验仿真/indi_vs_pid_simulation.py)

---

## 五、 仿真实验与图表输出验证规范

每次运行仿真或对比实验脚本时：
1. **定量指标自动输出**：必须在终端或日志中量化输出**状态跟踪误差（如 RMSE、最大超调量、调节时间）**以及**控制分配误差（$\|\boldsymbol{e}_{\tau}\|_2$ 均值与峰值、各推进器推力饱和占比）**。
2. **学术级绘图标准**：所有 Matplotlib 生成的仿真曲线图必须配置中英文字体兼容（中文宋体/黑体、英文 Times New Roman / Arial，修复负号显示 `axes.unicode_minus = False`），分辨率不少于 300 DPI，图例、坐标轴物理量及单位（如 $\text{m}, \text{deg}, \text{rad/s}, \text{N}, \text{N}\cdot\text{m}$）标注齐全。
