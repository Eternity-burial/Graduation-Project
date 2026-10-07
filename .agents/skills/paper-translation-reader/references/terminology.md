# 水下航行器与飞控领域标准中英术语对照表 (Standard Terminology Reference)

在进行外文文献翻译、撰写开题报告或毕业论文时，必须严格统一使用以下标准中文译名：

## 1. 航行器构型与运动学/动力学 (Vehicle & Hydrodynamics)

| 英文术语 (English) | 标准中文译名 (Chinese) | 禁用/不规范译法 |
| :--- | :--- | :--- |
| Unmanned Underwater Vehicle (UUV) | 水下无人航行器 | 水下无人机、无人潜艇 |
| Remotely Operated Vehicle (ROV) | 遥控水下航行器 / 遥控无人潜水器 | 远程操作车 |
| Autonomous Underwater Vehicle (AUV) | 自主水下航行器 | 自动水下车 |
| Intervention AUV (I-AUV) | 干预作业型自主水下航行器 | 介入式AUV |
| Open-frame configuration | 开架式构型 | 开放框架结构 |
| Over-actuated system | 过驱动系统（冗余驱动系统） | 超驱动系统 |
| Underactuated system | 欠驱动系统 | 欠致动系统 |
| Six Degrees of Freedom (6-DOF) | 六自由度 | 六个自由度 |
| North-East-Down (NED) frame | 北东地惯性坐标系 | 东北天（注意区分 ENU 与 NED） |
| Body-fixed frame (FRD) | 附体坐标系（机体坐标系，前-右-下） | 身体坐标系 |
| Surge / Sway / Heave | 纵荡（纵向）/ 横荡（横向）/ 垂荡（垂向） | 前冲 / 侧滑 / 升沉 |
| Roll / Pitch / Yaw | 横滚 / 俯仰 / 偏航 | 翻滚 / 倾斜 / 航向角 |
| Rigid-body inertia matrix ($\boldsymbol{M}_{RB}$) | 刚体质量惯性矩阵 | 刚体矩阵 |
| Added mass ($\boldsymbol{M}_A$) | 附加质量（水动力附加质量） | 增加质量、额外质量 |
| Coriolis and centripetal matrix ($\boldsymbol{C}(\boldsymbol{\nu})$) | 科氏力与向心力矩阵 | 科里奥利矩阵 |
| Hydrodynamic damping ($\boldsymbol{D}(\boldsymbol{\nu})$) | 水动力阻尼（流体阻尼） | 水阻力 |
| Linear / Quadratic damping | 线性阻尼 / 二次非线性阻尼（平方阻尼） | 二阶阻尼 |
| Restoring forces and moments ($\boldsymbol{g}(\boldsymbol{\eta})$) | 重力与浮力恢复力及力矩（静水恢复力矩） | 还原力矩 |
| Center of Gravity (CG) / Center of Mass (CoM) | 重心 / 质心 | 重力中心 |
| Center of Buoyancy (CB / CoB) | 浮心 | 浮力中心 |
| Free decay test | 自由衰减试验 | 自由衰减测试 |
| System identification | 系统辨识（参数辨识） | 系统识别 |

---

## 2. 运动控制与控制分配 (Motion Control & Control Allocation)

| 英文术语 (English) | 标准中文译名 (Chinese) | 备注 |
| :--- | :--- | :--- |
| Generalized control forces and moments / Wrench ($\boldsymbol{\tau}$) | 广义控制力与力矩（广义力矩螺旋） | 6维矢量 $[F_x, F_y, F_z, M_x, M_y, M_z]^T$ |
| Feedback Linearization (FBL) | 反馈线性化 | 基于精确机理模型的非线性解耦 |
| Nonlinear Dynamic Inversion (NDI) | 非线性动态逆 | 传统动态逆 |
| Incremental Nonlinear Dynamic Inversion (INDI) | 增量非线性动态逆 | 基于传感器局部增量线性化 |
| Differential-Flatness-Based Control (DFBC) | 基于微分平坦的控制 | 常用于四旋翼/敏捷轨迹对比 |
| Nonlinear Model Predictive Control (NMPC) | 非线性模型预测控制 | 滚动时域优化控制 |
| Control allocation | 控制分配（推力分配） | 将广义力与力矩映射至各推进器控制量 |
| Control effectiveness matrix ($\boldsymbol{B}$) | 控制分配矩阵（控制效能矩阵） | 映射矩阵 |
| Moore-Penrose pseudoinverse ($\boldsymbol{B}^+$) | 广义逆（Moore-Penrose 伪逆） | 最小二乘最小范数解析解 |
| Weighted pseudoinverse | 加权伪逆 | 含推进器权重矩阵 |
| Actuator saturation | 执行器饱和（推力幅值饱和） | 执行机构推力或输出达到物理极限 |
| Sequential desaturation | 序贯解饱和法 | PX4 内置优先级抗饱和分配方法 |

---

## 3. PX4 飞控软件架构与仿真 (PX4 Architecture & SITL)

| 英文术语 (English) | 标准中文译名 (Chinese) | 备注 |
| :--- | :--- | :--- |
| Flight Stack / Middleware | 飞控算法层 / 系统中间件层 | PX4 双层解耦架构 |
| uORB (Micro Object Request Broker) | uORB 微对象请求代理（异步发布/订阅消息总线） | PX4 核心进程间通信机制 |
| Software-In-The-Loop (SITL) | 软件在环仿真 | PC 端运行原生飞控代码闭环 |
| Hardware-In-The-Loop (HIL / HITL) | 硬件在环仿真 | 嵌入式飞控板连接仿真器 |
| Extended Kalman Filter (EKF2) | 扩展卡尔曼滤波器（EKF2 状态估计模块） | 位姿与速度融合估计 |
| ULog | ULog 高频飞行/航行数据日志 | 配合 PlotJuggler 分析 |
| Butterworth low-pass filter | 巴特沃斯低通滤波器 | 用于角速度/角加速度降噪与相位对齐 |
