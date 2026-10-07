# Yoerger & Slotine《水下航行器鲁棒轨迹滑模控制》核心精读导读

> **英文原题**：Robust Trajectory Control of Underwater Vehicles  
> **论文作者**：Dana R. Yoerger (WHOI 资深科学家), Jean-Jacques E. Slotine (MIT 终身教授, 《应用非线性控制》作者)  
> **所属机构**：伍兹霍尔海洋研究所深潜实验室（WHOI Deep Submergence Laboratory）与麻省理工学院机械工程系（MIT Department of Mechanical Engineering）  
> **出版出处**：*IEEE Journal of Oceanic Engineering*, OE-10(4): 462–470, October 1985  
> **学术地位**：**水下航行器非线性滑模鲁棒控制（Sliding Mode Control, SMC）的开山鼻祖奠基作**（被引 1300+ 次），首次将李雅普诺夫滑动模态理论与边界层平滑技术引入水下机器人轨迹跟踪控制。

---

## 一、 论文核心动机：如何面对未知复杂水动力不确定性？

1980 年代初期，随着深潜机器人（如著名阿尔文号 Alvin 及 Jason ROV）在深海科考与打捞任务中的应用，工程师面临极大的控制难题：
1. **水动力参数难以精确测量**：附加质量随运动状态剧烈波动，流体阻尼具有强非线性与时变性；
2. **水下扰动难以直接传感器测量**：深海突发水流冲击与缆绳拉力无法实时加装高精度流速计测量；
3. **传统线性控制器（如定增益 PID）失稳频繁**：在线性化工作点设计的 PID 控制器在航行器大范围快速转向或变速跟踪时，超调巨大、响应迟钝甚至闭环发散。

为此，Slotine（滑模控制国际泰斗）与 Yoerger（海洋机器人先驱）合作，首次系统性提出了**无需已知精确水动力学参数、具备极强参数不确定性容忍度的滑模轨迹跟踪控制框架**。

---

## 二、 滑模控制系统设计与边界层抖振消除

### 2.1 标称动力学方程与不确定性界限
以水下航行器单个解耦运动自由度（如纵荡位置 $x$ 或偏航角 $\psi$）为例，其二阶非线性运动方程写为：
$$
m \ddot{x} + f(x, \dot{x}) = u(t)
$$
由于物理参数难以完全测准，系统由**标称估计值**与**有界不确定性偏差**构成：
$$
\hat{m} \approx m, \quad \hat{f} \approx f(x, \dot{x})
$$
定义质量摄动边界与动力学不确定性上界：
$$
\beta^{-1} \le \frac{\hat{m}}{m} \le \beta, \quad |f(x, \dot{x}) - \hat{f}(x, \dot{x})| \le F(x, \dot{x})
$$

### 2.2 滑模切换面定义
定义位置跟踪误差 $\tilde{x}(t) = x(t) - x_d(t)$，构建一阶滑动模态曲面：
$$
s(t) = \dot{\tilde{x}}(t) + \lambda \tilde{x}(t)
$$
其中 $\lambda > 0$ 为正实数设计参数，决定了滑模面上的指数衰减收敛带宽（时间常数 $\tau = 1/\lambda$）。当系统状态轨迹被驱动至滑模面 $s(t) = 0$ 时，跟踪误差 $\tilde{x}(t)$ 将以 $e^{-\lambda t}$ 的速率自主渐近收敛至零。

### 2.3 鲁棒控制律合成与边界层连续化（Boundary Layer Technique）
为保证即使在最大参数不确定性下李雅普诺夫函数导数 $\frac{1}{2} \frac{d}{dt} s^2 \le -\eta |s|$ 恒成立，理想切换控制律包含**标称动态逆项**与**鲁棒切换项**：
$$
u(t) = \hat{m} \left( \ddot{x}_d - \lambda \dot{\tilde{x}} \right) + \hat{f} - k(x, \dot{x}) \operatorname{sgn}(s)
$$
其中增益 $k \ge \beta (F + \eta) + (\beta - 1) |\hat{u}|$。

#### 物理推进器防抖振工程突破：
理想符号函数 $\operatorname{sgn}(s)$ 在滑模面两侧会产生无限高频的开关切换（Chattering），这会瞬间烧毁水下航行器的无刷直流推进器或打齿。  
Yoerger 和 Slotine **首创性地引入厚度为 $\Phi$ 的滑动边界层（Boundary Layer）**，用平滑饱和函数 $\operatorname{sat}(s / \Phi)$ 替代不连续的 $\operatorname{sgn}(s)$：
$$
\operatorname{sat}\left(\frac{s}{\Phi}\right) = 
\begin{cases}
\frac{s}{\Phi}, & |s| \le \Phi \\
\operatorname{sgn}(s), & |s| > \Phi
\end{cases}
$$
在边界层内部，控制律退化为高增益线性低通滤波控制器，既彻底消除了执行机构的高频抖振，又保证了跟踪误差严格收敛至由 $\Phi$ 决定的紧致邻域内。

---

## 三、 对本课题运动控制方案的直接启示

Yoerger & Slotine (1985) 为我们提供了运动控制演进的“鲁棒性基准标杆”：
1. **揭示了“模型前馈”在抗扰中的核心地位**：即便模型不完全精确，基于标称模型的逆补偿也能显著降低闭环对高增益反馈的依赖；
2. **指明了推进器物理特性的制约**：任何先进非线性控制律（包括滑模与增量动态逆）必须充分考虑推进器执行机构的带宽极限与抖振问题，必须在底层加入连续化平滑或低通滤波处理，这与 PX4 底层滤波架构不谋而合。
