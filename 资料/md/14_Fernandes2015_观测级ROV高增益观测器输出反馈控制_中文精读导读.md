# Daniel A. Fernandes 等《基于高增益观测器的观测级ROV输出反馈运动控制》核心精读导读

> **英文原题**：Output Feedback Motion Control System for Observation Class ROVs Based on a High-Gain State Observer: Theoretical and Experimental Results  
> **论文作者**：Daniel A. Fernandes, Asgeir J. Sørensen, Kristin Y. Pettersen, Décio C. Donha  
> **所属机构**：挪威科技大学 AMOS 自主海洋系统卓越中心（NTNU AMOS）  
> **出版出处**：*Control Engineering Practice*, 39: 90–102, 2015  
> **学术地位**：海洋工程控制顶刊经典文献，首次在真实多推进器观测级 ROV 上闭环验证高增益状态观测器（HGO）与模型动力学补偿控制。

---

## 一、 核心内容与技术贡献

在水下低成本航行器中，线速度与角速度信号往往受到高频噪声污染。Fernandes 团队提出了完整的理论与物理验证闭环：
1. **高增益状态观测器设计**：在无需高频微分滤波的前提下重构不可测或高噪声状态，具有半全局渐近稳定性；
2. **模型前馈动态补偿**：基于航行器标称动力学逆模型进行前馈抵消，降低对反馈控制增益的激进要求；
3. **真实水池物理消融实验**：在巴西圣保罗大学实验水池完成轨迹跟踪实测，量化证明了模型前馈补偿对降低跟踪误差 RMS 的关键作用。

---

## 二、 对本课题的启发与开题报告映射

为本课题“标称模型解耦前馈 + 高频状态反馈”架构提供了极佳的理论支撑，特别是其模型前馈与无模型 PID 的水池消融对比范式，是本课题实验方案的直接对标依据。
