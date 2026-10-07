---
name: rov-modeling-control-px4
description: >-
  Use this skill whenever the user asks to derive mathematical models, run
  system identification, design motion controllers, configure control allocation,
  write simulations, or develop/modify PX4 C++ modules and uORB topics for the
  underwater vehicle (UUV/ROV).
---

# 水下航行器建模、控制分配与 PX4 仿真工程规范 (ROV Modeling, Control & PX4 Skill)

本技能规范了《基于PX4的水下航行器模型控制方法研究》课题在动力学推导、数值仿真与 PX4/SITL 开发中的工程设计原则、模块解耦架构与仿真验证规范。

> [!IMPORTANT]
> **通用工程与模块化原则**：水动力参数辨识方案与控制算法需保持充分的学术开放性与工程比选空间。在编写仿真脚本、嵌入式代码及文档时，必须采用**参数化配置（Config/YAML/Struct）与模块化插拔设计**，严禁将未验证的经验假设或排他性的狭窄实现硬编码死。

---

## 一、 通用工程架构与四大模块解耦规范

无论编写离线仿真脚本还是二次开发飞控固件，系统均遵循清晰的分层解耦架构，确保各环节具备高度独立性与可替换性：

1. **航行器与执行器动力学仿真模块 (Plant Dynamics)**：
   - 职责：根据执行器控制输入与外部环境扰动，数值积分求解航行器运动状态；
   - 接口：接收底层控制输入与扰动，输出航行器位姿、速度与加速度状态；内部动力学参数通过外部配置文件注入。
2. **系统辨识与模型验证模块 (System Identification & Validation)**：
   - 职责：基于激励测试数据与状态响应序列，进行水动力参数辨识，并评估标称模型的预测精度与残差特性；
   - 接口：接收时序输入输出数据，输出校准后的模型参数集与残差量化评估报告。
3. **闭环运动控制模块 (Motion Controller)**：
   - 职责：结合航行器模型特性补偿与实时状态反馈，计算航行器在各受控自由度上的期望广义控制力与力矩；
   - 架构：采用支持多算法横向比选的开放式架构，能够平滑接入基础反馈控制、模型前馈补偿以及增量/自适应控制策略；
   - 接口：接收参考设定值与状态反馈估计值，输出期望广义控制量。
4. **控制分配模块 (Control Allocator)**：
   - 职责：根据航行器推进器空间布局与几何配置，将期望广义控制量映射至各个独立推进器的控制指令，并合理处理执行器物理受限情况；
   - 接口：接收期望广义控制量，输出各推进器控制指令及未分配残差。

---

## 二、 仿真实验、数据可视化与验证门禁

在开展算法验证与仿真对比时，必须严格执行以下工程规范：

1. **定量指标量化输出**：
   - 每次仿真评估必须自动统计并输出量化指标：包括状态跟踪均方根误差（RMSE）、调节时间、超调量、控制分配残差范数以及推进器输出负荷分布等；
   - 严禁缺乏定量数据的空泛定性评价。
2. **出版级科学绘图规范**：
   - 曲线对比图必须采用**颜色 + 线型双重编码**（实线、虚线、点划线等），确保黑白打印或色盲场景下均可清晰分辨；
   - 图像分辨率保持在 300 DPI 以上，物理量符号与度量单位标注规范严谨，杜绝字体过小、文字遮挡或背景杂乱。
3. **参数整定与优化闭环**：
   - 在进行模型参数调优或控制器增益整定时，坚持**“明确量化目标 ➔ 运行基准记录 ➔ 单一变量改动 ➔ 评估对比验证”**的渐进迭代流程，避免同时修改多重参数导致因果关系混乱；
   - 有效优化结果与关键配置及时记录并提交版本管理。

---

## 三、 PX4/SITL 相关参考资料与代码资产索引

在推进 PX4 架构调研与算法移植时，优先查阅项目内已有技术报告与验证原型：
- PX4 与 ArduSub 控制与分配架构调研：[PX4与ArduSub对比分析.md](file:///d:/tj/Graduation%20Project/选题/PX4与ArduSub对比分析.md)
- PX4 架构与消息链路研报：[01_PX4架构与控制体系全景深度报告.md](file:///d:/tj/Graduation%20Project/PX4_INDI_Research/01_PX4架构与控制体系全景深度报告.md)
- 飞控端 C++ 原型参考：[RateControlINDI.hpp](file:///d:/tj/Graduation%20Project/PX4_INDI_Research/02_INDI算法在PX4中的嵌入式C++实现/RateControlINDI.hpp)
- Python 离线对比仿真原型：[indi_vs_pid_simulation.py](file:///d:/tj/Graduation%20Project/PX4_INDI_Research/03_Python离线原型与对比实验仿真/indi_vs_pid_simulation.py)
