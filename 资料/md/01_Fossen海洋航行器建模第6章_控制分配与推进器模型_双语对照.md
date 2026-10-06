# 01_Fossen海洋航行器建模第6章_控制分配与推进器模型 (中英双语对照精读版)

> **自动转换源文件**: `01_Fossen海洋航行器建模第6章_控制分配与推进器模型.pdf`  
> **双语对照总页数**: 104 页  

---

## Page 1

1 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Chapter 6 – Maneuvering Models for Ships and USVs An alternative to the seakeeping formalism (Chapter 5) is to use maneuvering theory to describe the motions of ships and USVs. In classical maneuvering theory, the frequency-dependent added-mass and radiation-damping matrices are replaced by constant hydrodynamic coefficients, typically chosen as their zero-frequency values for horizontal-plane motions in surge, sway, and yaw. Hence, the fluid-memory effects are neglected, and the equations can be formulated directly in the body-fixed reference frame. For fully coupled 6-DOF maneuvering models, constant equivalent added-mass and damping matrices can alternatively be obtained by power-based spectral averaging of the frequency-dependent seakeeping coefficients. This yields a physically consistent first-principles nonlinear mass–damper–spring system suitable for simulation, guidance, navigation, and control applications.

---

## Page 2

1 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 第6章 – 船舶与无人水面艇的操纵模型 对稳航形式主义（第5章）的一种替代方法是使用机动理论来描述船舶和无人水面艇的运动。在经典机动理论中，频率 依赖的附加质量和辐射阻尼矩阵被常数水动力系数取代，这些系数通常选择为水平面运动（纵摇、横摇和偏航方向）下 的零频值。因此，流体记忆效应被忽略，方程可以直接在船体固定参考系中进行形式化。 对于完全耦合的六自由度机动模型，可以通过对频率相关的海况系数进行基于功率的谱平均，来获得恒定的等效 附加质量和阻尼矩阵。这样可以得到一个物理一致的一阶原理非线性质量–阻尼–弹簧系统，适用于仿真、制导、 导航和控制应用。

---

## Page 3

2 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Chapter Goals • Formulate the first-principles 6-DOF maneuvering model by combining rigid-body kinetics with hydrodynamic added mass, damping, hydrostatic restoring, and external forces. • Explain how the rigid-body and added-mass Coriolis–centripetal matrices arise in BODY-fixed coordinates and state their skew-symmetry property. • Explain when zero-frequency potential coefficients are appropriate for surge, sway, and yaw, why viscous damping must be added, and why the approximation fails for coupled 6-DOF motion. • Apply the power-based spectral averaging method to compute sea-state-dependent constant equivalent added-mass and damping matrices for 6-DOF maneuvering models. • Model linear and nonlinear hydrodynamic damping using ITTC surge resistance, cross-flow drag, and additional roll, pitch, and yaw damping. • Include constant irrotational ocean currents using relative velocity and formulate the dynamics with either relative or absolute velocity as the state. • Derive and compare simplified and classical maneuvering models, including longitudinal–lateral, horizontal-plane 3-DOF, dynamic positioning,  Abkowitz, second-order modulus, and MMG models.

---

## Page 4

2 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 章节目标 • 通过将刚体动力学与流体动力附加质量、阻尼、静水恢复力和外力相结合，制定基于第一性原理的六自由度 机动模型。 • 解释刚体和附加质量科里奥利-向心矩阵在机体固定坐标系中是如何产生的，并说明它们的斜对称性特性。 • 解释在纵荡、横荡和偏航中何时适合使用零频潜势系数，为什么必须添加粘性阻尼，以及为什么该近似在耦合6 自由度运动中失效。 • 应用基于功率的谱平均方法来计算6自由度机动模型的海况相关恒定等效附加质量和阻尼矩阵。 • 使用 ITTC 冲程阻力、横向流拖力以及额外的横摇、纵倾和偏航阻尼来建模线性和非线性流体阻尼。 • 使用相对速度包含恒定无旋转的海洋洋流，并用相对速度或绝对速度作为状态来制定动力学。 • 推导并比较简化和经典的机动模型，包括纵横向、水平面三自由度、动态定位、Abkowitz、二阶模量和MMG模 型。

---

## Page 5

3 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) First-Principles 6-DOF Maneuvering Model

---

## Page 6

3 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 基于第一性原理的六 自由度机动模型

---

## Page 7

4 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Maneuvering Model including Ocean Currents Chapter 6 Summary: First-Principles 6-DOF Maneuvering Model νc = Property 10.1 (Irrotational constant ocean currents) The maneuvering model can be expressed entirely in terms of the relative velocity vector 𝝂! = 𝝂−𝝂" If the rigid-body Coriolis and centripetal matrix 𝑪#$(𝝂) is parametrized independent of linear velocity 𝝂% = 𝑢, 𝑣, 𝑤& (Section 3.3.2) and the ocean current is irrotational and constant. Hence, This implies that

---

## Page 8

4 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 包括洋流的机动模型 第6章总结：基于第一性原理的六自由度机动模型 !c ! 属性 10.1（无旋转的恒定海流）操纵模型可以完 全用相对速度向量 𝝂! = 𝝂−𝝂" 表示。如果刚体 科里奥利力和向心力矩阵 𝑪#$(𝝂) 独立于线速度 𝝂% = 𝑢, 𝑣, 𝑤& 参数化（第 3.3.2 节），并且海流 是无旋的并且恒定。因此， 这意味着

---

## Page 9

5 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Chapter 6 Summary: First-Principles 6-DOF Maneuvering Model Two state-space formulations are commonly used. The first uses the relative velocity 𝝂! as state and is convenient when ocean currents are modeled explicitly and relative velocity is measured (e.g., by a DVL). The second uses the absolute velocity 𝝂as state and is often preferred for surface vessels, where INS/GNSS systems provide measurements of absolute velocity.

---

## Page 10

5 乐cture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 第6章总结：基于第一性原理的六自由度机动模型 通常使用两种状态空间公式。第一种使用相对速度 𝝂! 作为状态，在明确建模洋流且测量相对速度（例如，通过 DVL ）时很方便。第二种使用绝对速度 𝝂 作为状态，在表面船舶中通常更受欢迎，因为 INS/GNSS 系统提供绝对速度的测 量。

---

## Page 11

6 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Rigid-Body Kinetics ν = !!"! #!$! %!& Newton-Euler Equations (Chapter 3) Screw transformation between two points

---

## Page 12

6 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 刚体动力学 ν = !!"! #!$! %!& 牛顿-欧拉方程（第3章） Screw transformation between two points

---

## Page 13

7 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Hydrodynamic Derivatives for Added Mass and Linear Damping Notation of SNAME (1950) for Hydrodynamic Derivatives Added Mass Matrix Linear Damping Matrix

---

## Page 14

7 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 附加质量和线性阻尼的水动力导数 SNAME（1950年）水动力 导数的符号 添加的质量矩阵 线性阻尼矩阵

---

## Page 15

8 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 x 10 6 A22 (w) frequency (rad/s) 0 1 2 3 4 5 6 7 0 1 2 3 4 5 x 10 6 B22 (w) frequency (rad/s) Aij(ω) – added mass Bij(ω) – potential damping Zero-Frequency added mass and damping matrices can be used for surge, sway, and yaw motions (DOF 1–2–6), since radiation vanishes at high frequency. Note that when a vessel oscillates in waves, it radiates outgoing waves. Should not be extended to heave, roll, and pitch (DOF 3–4–5): o These motions generate strong radiation damping since vertical oscillations radiate waves and dissipate energy. o Their natural frequencies lie in the wave-frequency range. Hence, the coefficients are strongly frequency dependent. o Using only zero-frequency values leads to incorrect energy dissipation and unrealistic motions. Problem that coupling terms (A13, A15, A24, A26, A35, A46) peak at different frequencies: o The zero frequency cannot represent these mixed-frequency effects. o Solution: spectral averaging, such as the power-based averaging method (see next page). Estimation from Zero-Frequency Seakeeping Coefficients Potential Coefficients for a Surface Craft Added mass matrix: Linear damping matrix: 3-DOF Zero-Frequency Approximation (Classical Maneuvering Theory) Viscous damping Bv must be added since potential damping B(0) is zero. Alternatively, D can be estimated from time constants/relative damping ratios.

---

## Page 16

8 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 x 10 6 A 2 2 (w ) frequency (rad/s) 0 1 2 3 4 5 6 7 0 1 2 3 4 5 x 10 6 B 2 2 (w ) frequency (rad/s) Aij(ω) – added mass Bij(ω) – potential damping 零频附加质量和阻尼矩阵可用于纵荡、横荡和偏航运动（自由度 1–2 –6），因为在高频下辐射消失 频率。注意，当船舶在波浪中振荡时，它会辐射出外向波。 不应延伸至升降、横滚和纵摇（自由度 3–4–5）: 这些运动产生强烈的辐射阻尼，因为垂直方向 l 振荡会辐射波并耗散能量。它们的固有频率处于波频 率范围。因此，系数强烈依赖于频率。仅使用零频率值会 导致能量耗散不正确和运动不真实。 耦合项（A13、A15、A24、A26、A35、A46）达到峰值的问题 不同的频率： o 零频率无法表示这些混合频率效应。 o 解决方法：谱平均，例如 基于功率的平均方法（见下一页）。 从零频振荡系数的估计 Potential Coefficients for a Surface Craft Added mass matrix: Linear damping matrix: 三自由度零频近似（经典机动理论） 必须添加黏性阻尼 Bv，因为势能阻 尼 B(0) 为零。或者，D 可以通过时 间常数/相对阻尼比来估算。

---

## Page 17

9 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS Toolbox Zero-frequency added mass matrix

---

## Page 18

9 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） MSS 工具箱 Zero-frequency added mass matrix

---

## Page 19

10 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Estimation from Power-Averaged Seakeeping Coefficients For a fully coupled 6-DOF maneuvering model, the zero-frequency approximation is not appropriate. The zero frequency cannot represent the coupling terms (A13, A15, A24, A26, A35, A46) which peak at different frequencies. However, spectral averaging solves this problem. 6-DOF Equivalent Matrices by Power-Based Averaging (Section 5.4) Frequency-dependent added mass AU(ω) and potential damping BU(ω) for constant speed U are integrated over the full frequency band relevant to a given sea state, weighted by the spectral energy distribution using a normalized wave spectrum to ensure that only the spectral shape influences the equivalent values 𝑨! "# and 𝑩! "# (Fossen, 2025): PM-spectrum used for weighting In practical applications, the zeroth spectral moment m0 is evaluated for U = 0, thereby avoiding explicit dependence of the weighting spectrum on the forward speed U and relative wave heading 𝛽$"% such that 𝜔& = 𝜔. The peak frequency 𝜔' is then treated as a constant parameter describing the average sea state for the operating condition under consideration. Fossen, T. I. (2025). Maneuvering Coefficient Estimation from Frequency-Dependent Added Mass and Damping: A Power-Based Approach. Oceanic Engineering 341, 122494. https://doi.org/10.1016/j.oceaneng.2025.122494 S(ω) 𝜔'

---

## Page 20

10 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 基于功率平均的船舶运动系数的估算 对于一个完全耦合的六自由度机动模型，零频率近似是不合适的。零频率无法表示在不同频率下达到峰值的耦合项（A13、A15、 A24、A26、A35、A46）。然而，频谱平均法可以解决这个问题。 基于功率平均的六自由度等效矩阵（第5.4节） 频率相关附加质量 AU(ω) 和势阻尼 BU(ω) 对于恒定速度 U，在与特定海况相关的整个频率范围内进行积分，并按归一化波谱的谱能量分 布加权，以确保只有谱的形状影响等效值 𝑨! "# 和 𝑩! "#（Fossen, 2025）： 用于加权的PM光谱 在实际应用中，零阶谱矩 m0 被评估用于 U = 0，从而避免了加权谱明确依赖于前进速度 U 和相对波向 𝛽$"%，使得 𝜔& = 𝜔。然后，将峰值频率 𝜔' 作为描述所考虑操作条件下平均海况的常数参数处理。 Fossen, T. I. (2025). 基于功率方法的频率相关附加质量与阻尼的操纵系数估算 . 海洋工程 341, 122494. https://doi.org/10.1016/j.oceaneng.2025.122494 S(ω) 𝜔'

---

## Page 21

11 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS Toolbox

---

## Page 22

11 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS 工具箱

---

## Page 23

12 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Estimation from Time Constants and Relative Damping Ratios D →   D11 0 0 0 0 0 0 D22 0 0 0 0 0 0 D33 0 0 0 0 0 0 D44 0 0 0 0 0 0 D55 0 0 0 0 0 0 D66   The response of a marine craft can be approximated by (Section 6.1.1): • Time constants Ti  (1st-order systems). • Relative damping ratios zi (2nd-order systems). Assume that the added mass is approximated by a constant diagonal matrix about the CG using semi-empirical formulas: § Small craft, USVs, and AUVs: lower values § Ships and offshore vessels: higher values § Streamlined AUVs and torpedo-shaped vehicles: lower values § Ships and offshore vessels: higher values

---

## Page 24

12 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 从时间常数和相对阻尼比进行估算 < l a t e x i t s h a 1 _ b a s e 6 4 = " 7 4 W O N J z / e W j Z U i 5 t K R X z H q x P L g A = " > A A A C y X i c d V F N T x s x E P U u H 6 X b A o E e e 7 G I W v U U 7 Y Y Q O C J A C I k L l R p A y k a R 1 z s J F l 5 7 a 3 t R w m p P / E N u v f F T 8 A Y L t U k z 0 s h P 7 7 2 x x z N J z p k 2 Y f j H 8 1 d W 1 9 Y / b H w M P n 3 e 3 N p u 7 O x e a 1 k o C j 0 q u V S 3 C d H A m Y C e Y Y b D b a 6 A Z A m H m + T + t N Z v H k B p J s U v M 8 1 h k J G x Y C N G i b H U s P E S J 5 K n e p r Z o z y r c E z y X M l J E C c w Z q J M M m I U m 1 T B 2 b C M o g p / x + F 8 x n F Q n 9 b Q b i 8 Y n O g M + / v V E t E Z O p 1 q i e g M B w f V E t E Z u t 0 q i E G k 7 5 0 P G 8 2 w F c 4 C L 4 L I g S Z y c T V s P M e p p E U G w l B O t O 5 H Y W 4 G J V G G U Q 7 2 9 k J D T u g 9 G U P f Q k E y 0 I N y t o k K f 7 N M i k d S 2 R Q G z 9 i / K 0 q S 6 X r Y 1 m n 7 u 9 P z W k 3 + T + s X Z n Q 0 K J n I C w O C v j 0 0 K j g 2 E t d r x S l T Q A 2 f W k C o Y r Z X T O + I I t T Y 5 Q d 2 C N H 8 l x f B d b s V d V v d n 5 3 m 8 Y k b x w b 6 i v b Q D x S h Q 3 S M L t A V 6 i H q n X v c K 7 w H / 9 L / 7 U / 8 x z e r 7 7 m a L + i f 8 J 9 e A e L u w r 4 = < / l a t e x i t > D →   D11 0 0 0 0 0 0 D22 0 0 0 0 0 0 D33 0 0 0 0 0 0 D44 0 0 0 0 0 0 D55 0 0 0 0 0 0 D66   可以用（第6.1.1节）来近似描述海上船舶的响应： • 时间常数 Ti（一阶系统）。 • 相对阻尼比 zi（二阶系统）。 假设附加质量通过半经验公式，以质心为中心用一个常数对角矩阵来近似： § Small craft, USVs, and AUVs: lower values § Ships and offshore vessels: higher values § Streamlined AUVs and torpedo-shaped vehicles: lower values § Ships and offshore vessels: higher values

---

## Page 25

13 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS Toolbox Copyright ©  Bjarne Stenberg

---

## Page 26

13 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS 工具箱 Copyright ©  Bjarne Stenberg

---

## Page 27

14 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Coriolis–Centripetal Forces in a Rotating Coordinate System The goal is to derive a formula for the matrix 𝑪𝑨(𝝂#) such that it can be computed as a function of the matrix 𝑴𝑨= 𝑨$ %& CAνr The added mass matrix MA should should not be interpreted as a fixed amount of water being carried or dragged along with the vessel. Such an interpretation would correspond to a constant increase in mass. Instead, added mass is a dynamic effect arising from the pressure field generated by the accelerating motion, and its value therefore depends on the geometry of the body and the oscillation frequency. The body behaves as if its effective mass is the sum of its rigid-body mass and the added mass M = MRB + MA

---

## Page 28

14 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 旋转坐标系中的科里奥利—向心力 目标是推导出矩阵 𝑪𝑨(𝝂#) 的公式，以便可以将其作为矩阵 𝑴𝑨= 𝑨$ %& 的函数来计 算 CA !!r 附加质量矩阵 MA不应被解释为随 船只携带或拖拽的固定数量的水 。这种解释将对应于质量的恒定 增加。 相反，附加质量是一种由加速运动 产生的压力场引起的动态效应，因 此其值取决于物体的几何形状和振 动频率。 这个物体的行为就好像它的有效 质量是刚体质量和附加质量的总 和 M = MRB + MA

---

## Page 29

15 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Fluid Kinetic Energy • The concept of fluid kinetic energy can be used to derive the added mass Coriolis–centripetal matrix • Any motion of the vessel will induce a motion in the otherwise stationary fluid. To allow the vessel to pass through the fluid, it must move aside and then close behind the vessel. • Consequently, the fluid motion possesses kinetic energy that it would lack otherwise (Lamb 1932). Coriolis–Centripetal Forces in a Rotating Coordinate System CAνr Kinetic energy of the surrounding water When the hull moves with BODY velocity n, it induces an irrotational flow in an unbounded domain. Consider a control volume that encloses the ship and extends to a far field surface S∞ (water at rest as r à ∞). The kinetic energy of this induced flow is so the total kinetic energy is (ship-water system) T = 1 2 ω→(M RB + M A)ω. TA = 1 2 ω→M Aω

---

## Page 30

15 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 流体动能 • 流体动能的概念可以用来推导附加质量科氏–向心矩 阵 • 容器的任何运动都会引起原本静止的流体发生运 动。为了让容器通过流体，它必须向一侧移动， 然后在容器之后重新闭合。 • 因此，流体运动具有它本来不会具有的动能（Lamb 1932）。 旋转坐标系中的科里奥利—向心力 CA !!r 周围水体的动能 当船体以速度 n 移动时，它会在无限域中引发无旋流。考虑一个控 制体积，该体积包围船舶并延伸至远场表面 S∞（当 r → ∞ 时水静 止）。 该感应流的动能是 所以总动能是（船-水系统） < l a t e x i t s h a 1 _ b a s e 6 4 = " p r b b c 6 8 X g W s r M X x F R m N f m w 7 y 2 + M = " > A A A C Q 3 i c b V D L S g M x F M 3 4 r P V V d e k m W A R F K T M i 1 Y 1 Q d e N G U G l V 7 N S S S T M 1 N J M M y R 2 h D P N v b v w B d / 6 A G x e K u B V M H w u t H g g 5 n H M P u T l B L L g B 1 3 1 2 x s Y n J q e m c z P 5 2 b n 5 h c X C 0 v K l U Y m m r E a V U P o 6 I I Y J L l k N O A h 2 H W t G o k C w q 6 B z 3 P O v 7 p k 2 X M k q d G P W i E h b 8 p B T A l Z q F m 6 q + A D 7 E G p C v R 1 / 2 w + U a J l u Z K / U l 0 l 2 6 4 O K N 3 6 q p 1 k z v T j K t k a 0 w 8 3 R a K l Z K L o l t w / 8 l 3 h D U k R D n D U L T 3 5 L 0 S R i E q g g x t Q 9 N 4 Z G S j R w K l i W 9 x P D Y k I 7 p M 3 q l k o S M d N I + x 1 k e N 0 q L R w q b Y 8 E 3 F d / J l I S m d 5 2 d j I i c G d G v Z 7 4 n 1 d P I N x v p F z G C T B J B w + F i c C g c K 9 Q 3 O K a U R B d S w j V 3 O 6 K 6 R 2 x f Y K t P W 9 L 8 E a / / J d c 7 p S 8 c q l 8 v l u s H A 3 r y K F V t I Y 2 k I f 2 U A W d o D N U Q x Q 9 o B f 0 h t 6 d R + f V + X A + B 6 N j z j C z g n 7 B + f o G F A C y 6 A = = < / l a t e x i t > T = 1 2 ω→(M RB + M A)ω. < l a t e x i t s h a 1 _ b a s e 6 4 = " 4 B X z 0 w 9 8 a a c J 9 j L b E l 0 l K 6 k G Y K A = " > A A A C L 3 i c b V B N S w M x E M 3 6 W e v X q k c v w S J 4 k L J b R L 0 I V k G 8 C A r W F r p 1 y a b Z N j S b L M m s U J b + I y / + F S 8 i i n j 1 X 5 j W H r R 1 I O T x 3 h t m 5 k W p 4 A Y 8 7 9 W Z m Z 2 b X 1 g s L B W X V 1 b X 1 t 2 N z T u j M k 1 Z j S q h d C M i h g k u W Q 0 4 C N Z I N S N J J F g 9 6 p 0 P 9 f o D 0 4 Y r e Q v 9 l L U S 0 p E 8 5 p S A p U L 3 4 j a s 4 h M c Q K w J 9 S v B f h A p 0 T b 9 x H 5 5 I L P B f Q A q x b / Z q 0 F Y n X S F b s k r e 6 P C 0 8 A f g x I a 1 3 X o P g d t R b O E S a C C G N P 0 v R R a O d H A q W C D Y p A Z l h L a I x 3 W t F C S h J l W P r p 3 g H c t 0 8 a x 0 v Z J w C P 2 d 0 d O E j N c z j o T A l 0 z q Q 3 J / 7 R m B v F x K + c y z Y B J + j M o z g Q G h Y f h 4 T b X j I L o W 0 C o 5 n Z X T L v E J g c 2 4 q I N w Z 8 8 e R r c V c r + Y f n w 5 q B 0 e j a O o 4 C 2 0 Q 7 a Q z 4 6 Q q f o E l 2 j G q L o E T 2 j N / T u P D k v z o f z + W O d c c Y 9 W + h P O V / f F p a q c w = = < / l a t e x i t > TA = 1 2 ω→M Aω

---

## Page 31

16 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Euler-Lagrange’s Equation (Only for Generalized Coordinates) Kirchhoff's Equations ν! = !""" # ν! = !""" # τ! = !""" # τ! = !""" # Fluid kinetic energy Difference between kinetic and potential energy 6-DOF Generalized Coordinates: Coriolis–Centripetal Forces in a Rotating Coordinate System Quaternions are not generalized coordinates: A formula for the matrix 𝑪𝑨(𝝂#) as a function of the matrix 𝑴𝑨= 𝑨$ %& can be derived using Kirchoff’s equations.

---

## Page 32

16 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 欧拉-拉格朗日方程（仅适用于广义坐标)） 基尔霍夫方程 !! ! !! " # !! ! !! " # !! ! !! " # !! ! !! " # 流体动能 动能和势能的区别 6自由度广义坐标： 旋转坐标系中的科里奥利—向心力 四元数不是广义坐标： 可以使用基尔霍夫方程推导矩阵 𝑪𝑨(𝝂#) 作为矩阵 𝑴𝑨= 𝑨$ %& 的函数的公式。

---

## Page 33

17 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Coriolis–Centripetal Forces in a Rotating Coordinate System Kirchhoff's Equations Component form

---

## Page 34

17 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 旋转坐标系中的科里奥利—向心力 基尔霍夫方程 分量式

---

## Page 35

18 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) The added mass Coriolis and centripetal matrix is found by collecting all terms in Kirchhoff’s equations that are not functions of body accelerations. Property 6.2 (Added-mass Coriolis-centripetal matrix) For a rigid-body moving through an ideal fluid the hydrodynamic Coriolis and centripetal matrix can always be parameterized such that it is skew-symmetric Coriolis–Centripetal Forces in a Rotating Coordinate System Sagatun, S. I. and T. I. Fossen (1991). Lagrangian Formulation of Underwater Vehicles' Dynamics. IEEE International Conference on Systems, Man, and Cybernetics, Charlottesville, VA, USA, IEEE Xplore, pp. 1029-1034.

---

## Page 36

18 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 附加质量科里奥利和向心矩阵是通过收集基尔霍夫方程中所有不依赖于刚体加速度的项来得到的。 性质 6.2（附加质量科里奥利-向心矩阵）对于在理想流体中运动的刚体，流体动力学的科里奥利和向心矩阵总 可以参数化，使其为斜对称矩阵 旋转坐标系中的科里奥利—向心力 Sagatun, S. I. 和 T. I. Fossen (1991)。水下车辆动力学的拉格朗日公式。IEEE International Conference on Systems, Man, and  Cybernetics, 弗吉尼亚 州夏洛茨维尔, 美国, IEEE Xplore, 页 1029-1034。

---

## Page 37

19 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS Toolbox function C = m2c(M,nu) % C = m2c(M,nu) computes the Coriolis-centripetal matrix C(nu) from the % the system inertia matrix M > 0 for varying velocity nu. % If M is a 6x6 matrix and nu = [u, v, w, p, q, r]', the output is a 6x6 C matrix % If M is a 3x3 matrix and nu = [u, v, r]', the output is a 3x3 C matrix. % % Examples:  CRB = m2c(MRB,nu) %                     CA = m2c(MA, nu) % Output: %     C: Coriolis-centripetal matrix C = C(nu) % % Inputs: %    M: 6x6 or 3x3 rigid-body MRB or added mass MA system matrix %    nu: nu = [u, v, w, p, q, r]' or nu = [u, v, r]' % % The Coriolis and centripetal matrix depends on nu1 = [u,v,w]' and nu2 = % [p,q,r]' as shown in Fossen (2021, Theorem 3.2). Alternatively, the matrix % CRB = CRB(nu2) can be computed using % % [MRB,CRB] = rbody(m,R44,R55,R66,nu2,r_bp) M = 0.5 * (M + M'); % Symmetrization of the inertia matrix if (length(nu) == 6) % 6-DOF model M11 = M(1:3,1:3); M12 = M(1:3,4:6); M21 = M12’; M22 = M(4:6,4:6); nu1 = nu(1:3); nu2 = nu(4:6); nu1_dot = M11 * nu1 + M12 * nu2; nu2_dot = M21 * nu1 + M22 * nu2; C = [ zeros(3,3)     -Smtrx(nu1_dot) -Smtrx(nu1_dot) -Smtrx(nu2_dot) ]; else % 3-DOF model (surge, sway and yaw) C = [ 0 0 -M(2,2)*nu(2)-M(2,3)*nu(3) 0 0 M(1,1)*nu(1) M(2,2)*nu(2)+M(2,3)*nu(3) -M(1,1)*nu(1) 0 ]; end Note that CRB and CA can be computed automatically from MRB and MA both for 3-DOF and 6-DOF models.

---

## Page 38

十九 讲座ture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS 工具箱 function C = m2c(M,nu) % C = m2c(M,nu) computes the Coriolis-centripetal matrix C(nu) from the % the system inertia matrix M > 0 for varying velocity nu. % If M is a 6x6 matrix and nu = [u, v, w, p, q, r]', the output is a 6x6 C matrix % If M is a 3x3 matrix and nu = [u, v, r]', the output is a 3x3 C matrix. % % Examples:  CRB = m2c(MRB,nu) %                     CA = m2c(MA, nu) % Output: %     C: Coriolis-centripetal matrix C = C(nu) % % Inputs: %    M: 6x6 or 3x3 rigid-body MRB or added mass MA system matrix %    nu: nu = [u, v, w, p, q, r]' or nu = [u, v, r]' % % The Coriolis and centripetal matrix depends on nu1 = [u,v,w]' and nu2 = % [p,q,r]' as shown in Fossen (2021, Theorem 3.2). Alternatively, the matrix % CRB = CRB(nu2) can be computed using % % [MRB,CRB] = rbody(m,R44,R55,R66,nu2,r_bp) M = 0.5 * (M + M'); % Symmetrization of the inertia matrix if (length(nu) == 6) % 6-DOF model M11 = M(1:3,1:3); M12 = M(1:3,4:6); M21 = M12’; M22 = M(4:6,4:6); nu1 = nu(1:3); nu2 = nu(4:6); nu1_dot = M11 * nu1 + M12 * nu2; nu2_dot = M21 * nu1 + M22 * nu2; C = [ zeros(3,3)     -Smtrx(nu1_dot) -Smtrx(nu1_dot) -Smtrx(nu2_dot) ]; else % 3-DOF model (surge, sway and yaw) C = [ 0 0 -M(2,2)*nu(2)-M(2,3)*nu(3) 0 0 M(1,1)*nu(1) M(2,2)*nu(2)+M(2,3)*nu(3) -M(1,1)*nu(1) 0 ]; end Note that CRB and CA can be computed automatically from MRB and MA both for 3-DOF and 6-DOF models.

---

## Page 39

20 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS Toolbox Zero-frequency added mass matrix

---

## Page 40

20 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） MSS 工具箱 零频附加质量矩阵

---

## Page 41

21 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Coriolis–Centripetal Forces in a Rotating Coordinate System

---

## Page 42

21 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 旋转坐标系中的科里奥利—向心力

---

## Page 43

22 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Coriolis–Centripetal Forces in a Rotating Coordinate System

---

## Page 44

22 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 旋转坐标系中的科里奥利—向心力

---

## Page 45

23 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Nonlinear Damping Forces Potential theory codes assume that the fluid is inviscid. Water is assumed to be an inviscid fluid, in which the viscosity of the fluid is equal to zero. When viscous forces are neglected, such as the case of inviscid flow, the Navier-Stokes equation can be simplified to a form known as the Euler equation. Consequently, potential codes only compute: ü Potential Damping: Dissipative force in an inviscid fluid. The contribution from the potential damping terms compared to other dissipative terms like viscous damping is usually negligible. The Hydrodynamic Paradox D’Alembert’s paradox (or the hydrodynamic paradox) , first formulated in 1752 by Jean le Rond d’Alembert, states that in incompressible, inviscid, and irrotational potential flow, the drag force on a body moving at constant velocity relative to the fluid is zero. This theoretical result contradicts experimental observations, where bodies moving in fluids such as air or water experience significant drag, particularly at high Reynolds numbers. Therefore, viscous damping forces, such as quadratic drag and lift, must be included in seakeeping and maneuvering models in addition to potential damping. Jean le Rond d'Alembert (1717-1783)

---

## Page 46

23 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 非线性阻尼力 势理论代码假设流体是无黏性的。水被假定为无黏性流体，其中流体的黏度等于零。当忽略黏性力时，例如 在无黏性流动的情况下，Navier-Stokes 方程可以简化为一种称为欧拉方程的形式。 因此，潜在代码只计算： ü 势阻尼：无粘流体中的耗散力。与其他耗散项如粘性阻尼相比，势阻尼项的贡献通常可以忽略不计。 流体动力学悖论 达朗贝尔悖论（或称流体力学悖论）由让·勒·朗·达朗贝尔于1752年首次提出，指出在不可压 缩、无粘性且无旋的势流中，物体相对于流体以恒定速度运动时所受的阻力为零。这个理论 结果与实验观察相矛盾，实验中移动于空气或水等流体中的物体会经历显著的阻力，尤其是 在高雷诺数时。 因此，除了势阻尼外，还必须在船舶耐波性和操纵性模型中考虑黏性阻尼力，例如二次阻 力和升力。 让·勒·朗·达朗贝尔（17 17-1783）

---

## Page 47

24 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Nonlinear Damping Forces ü Skin friction • Boundary layer shear stresses on the hull. • Small effect on oscillatory motions but always present. ü Eddy and vortex shedding • Flow separation at bilge keels, chines, appendages. • Dominant contribution to roll damping. ü Lift-induced damping • Fins, rudders, and appendages generating side forces. • Important for control and stabilization. ü Wave drift damping • Interaction of mean drift forces with oscillations. • Often treated in second-order wave load analysis. ü Other nonlinear viscous effects • Flow separation, turbulence, appendage–hull interaction. • Typically lumped into empirical coefficients. Unfortunately, it is very hard to model all these effects and collect the terms into a common nonlinear damping matrix D(n). Linear damping must be blended with the nonlinear damping terms to avoid “double counting) at higher speed , e.g., using D exp(-a Ug)n + D(n)n. Sources of Viscous Damping

---

## Page 48

24 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 非线性阻尼力 皮肤摩擦 • 船体上的边界层剪应力。 • 对振荡运动影响很小，但总是存在。 涡旋和涡脱落 • 船舷龙骨、船底翼缘、附加装置处的流动分离。 • 对横摇阻尼的主要贡献。 升力引起的阻尼 • 产生侧向力的鳍、舵和附属物。 • 对于控制和稳定很重要。 波漂移阻尼 • 平均漂移力与振动的相互作用。 • 通常在二阶波浪载荷分析中处理。 其他非线性粘性效应 • 流动分离、湍流、附属物与船体的相互作用。 • 通常归入经验系数。 Unfortunately, it is very hard to model all these effects and collect the terms into a common nonlinear damping matrix D(n). Linear damping must be blended with the nonlinear damping terms to avoid “double counting) at higher speed , e.g., using D exp(-a Ug)n + D(n)n. 粘性阻尼的来源

---

## Page 49

25 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Nonlinear Damping Forces Linear Damping For slender bodies like ships and USVs, it is common to decouple the surge velocity from the other DOFs. Hence, we can express the damping matrix D as a function of the hydrodynamic derivatives: We can estimate a constant 6x6 damping matrix D = Beq + Bv from power- averaged seakeeping coefficients or time constants/relative damping ratios. D = →   Xu 0 0 0 0 0 0 Yv 0 Yp 0 Yr 0 0 Zw 0 Zq 0 0 Kv 0 Kp 0 Kr 0 0 Mw 0 Mq 0 0 Nv 0 Np 0 Nr   The vector 𝒅𝝂𝒓 is nonlinear dissipative forces and moments not expressible in the form 𝑫𝝂𝒓𝝂𝒓 Property 6.3 applies for linear and nonlinear damping.

---

## Page 50

25 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 非线性阻尼力 线性阻尼 对于像船舶和无人水面艇这样细长的船体 ，通常会将纵向速度与其他自由度解耦。 因此，我们可以将阻尼矩阵 D 表示为水动 力导数的函数： 我们可以从功率平均船舶运动系数或 时间常数/相对阻尼比估算一个恒定的6 x6阻尼矩阵 D = Beq + Bv。 < latexit sha1_base64 = "MkEw301C3YdnrS7FYe IQatgYaT0 = " > AAADNnicfZLNbtQwEMedlI8S vrZw5GKxAnFhlVSoVKqQqsIBaemqSGy7s FlFjjO7teo4qe20XVl5Ki48B7deOIAQVx4B Z7tFW7cwUjT/mfH87IydlpwpHYannr907fq Nm8u3gtt37t6731p5sKuKSlLo04IXcpASBZ wJ6GumOQxKCSRPOeylB6 + b + t4RSMUK8UF PSxjlZCLYmFGibSpZ8d7FacEzNc2tM29qH G + 8ijfwcxzEKUyYMGlOtGQndTBITFXjpzjE jf3Px3FwHnxMzNFik41LJ5b1YsO5/5SY4/pi fFi79K5D7zr07r/o2w59 + yp6z6H3HHqvoQcxi OzvkJJWO + yEM8OXRTQXbTS3naT1Nc4K WuUgNOVEqWEUlnpkiNSMcrD0SkFJ6AG ZwNBKQXJQIzO79ho/sZkMjwtpP6HxLLv YYUiumou1K + 359pVba5JX1YaVHq + PDBNlp UHQs43GFce6wM0bwhmTQDWfWkGoZPa  向量 𝒅𝝂𝒓 是非线性耗散力和力矩，不能以 𝑫𝝂𝒓𝝂𝒓 的形式表 示 性质 6.3 适用于线性和非线性阻 尼。

---

## Page 51

26 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Nonlinear Surge Damping ITTC Resistance where ρ    density of water S    wetted surface of the hull k    form factor giving a viscous correction (typically 0.1 for ships in transit) CF    flat plate friction from the ITTC (1957) line CR   residual friction due to hull roughness, pressure resistance, wave making resistance Reynolds number: Notation of SNAME (1950) For DP applications, the ITTC formulas often give too little damping compared to what is observed in model tests. Hence, an additional linear damping term is usually included at low speed. At higher speeds, the quadratic drag term becomes dominant and the linear damping contribution should gradually fade out. Hence,

---

## Page 52

26 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 非线性浪涌阻尼 ITTC 阻力 哪里 ρ水的密度 S    船体的湿表面积 k    给出粘性修正的形状因子（对于航行中的船舶 通常为 0.1） CF    来自 ITTC（1957）曲线的平板摩擦 CR   由船体粗糙度、压力阻力 、波浪阻力引起的剩余摩擦 雷诺数： SNAME（1950）的符号 对于DP应用，ITTC公式通常给出的阻尼比模型试验中观察到的要少。因此，通常在低速时会加入一个 额外的线性阻尼项。在高速时，二次阻力项变得占主导地位，而线性阻尼的贡献应逐渐消失。因此，

---

## Page 53

27 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Cross-Flow Drag Principle For relative current angles |βVc - ψ| ≫ 0, where βVc is the ocean current direction, the cross-flow drag principle may be applied to calculate the nonlinear damping force in sway and the yaw moment (Faltinsen, 1990) where Cd2D is the 2-D drag coefficient and T(x) is the draft. Strip theory means that the ship is cut in section along the x-axis. The integral is evaluated by summing up the contribution from each section. Extension to 6-DOF Cross-Flow Drag Dr. Sighard F. Hoerner (1906- 1971) is the author of two famous compendiums in aerodynamics entitled, Fluid-Dynamic Drag and Fluid-Dynamic Lift. Cd2D

---

## Page 54

27 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 横流阻力原理 对于相对流速角 |βVc - ψ| ≫ 0，其中 βVc  是洋流方向，可应用横流阻力原理来计算横摇的非线性阻尼力和偏航力矩（Falti nsen, 1990） 其中 Cd2D  是二维阻力系数，T(x)  是吃水。 条带理论意味着船沿 x 轴被切成若干截面。积分通 过将每个截面的贡献相加来计算。 扩展到六自由度横向阻力 西加德·F·霍尔纳博士 (1906-1971 ) 是两本著名空气动力学汇编的 作者，分别名为《流体动力学阻 力》和《流体动力学升力》. Cd2D

---

## Page 55

28 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS Toolbox The “cylinder” option is intended for cylindrical AUVs, using cylinder data from DNV-RP-C205. Conventional ship hulls are instead more accurately represented by Hoerner’s curve.

---

## Page 56

二十八 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS 工具箱 “圆柱体”选项适用于圆柱形AUV，使用 DNV-RP-C 205 的圆柱体数据。而常规船舶船体则更准确地用 Ho erner 曲线表示。

---

## Page 57

29 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Nonlinear Roll, Pitch and Yaw Damping The surge resistance and cross-flow drag model may be supplemented by additional nonlinear damping terms in roll, pitch, and yaw. This is often necessary to capture viscous and vortex-induced damping effects that are not well represented by linear hydrodynamic damping alone, in particular for roll motion of ships and offshore vessels. In yaw, the nonlinear damping term is often required to counteract the destabilizing Munk moment arising from the added- mass Coriolis and centripetal matrix 𝑪𝑨(𝝂#). At moderate and high forward speed, the Munk moment may generate an unstable yawing moment, especially for slender ships and underwater vehicles.

---

## Page 58

29 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 非线性横滚、俯仰和偏航阻尼 冲击阻力和横流阻力模型可以通过在横摇、纵摇和偏航中增加额外的非线性阻尼项来补充。这通常是必要的，以捕 捉仅靠线性水动力阻尼无法很好表示的粘性和涡旋引起的阻尼效应，尤其是对于船舶和海上船只的横摇运动。 在偏航中，非线性阻尼项通常是必要的，以抵消由附加质量科里奥利力和向心力矩阵 𝑪𝑨(𝝂#) 引起的不稳定 Munk 力矩。在中等和高速前进时，Munk 力矩可能产生不稳定的偏航力矩，尤其对于细长船舶和水下航行器。

---

## Page 59

30 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Linear and Nonlinear Hydrodynamic Damping The exponential factor 𝑒!"!|$"| fades the linear surge damping coefficient 𝑋( with increasing speed to avoid double counting of surge drag when quadratic damping 𝑋( ( 𝑢) is included. Strip theory cross-flow drag integrals using a 2-D drag coefficient. The nominal linear roll, pitch, and yaw damping derivatives are augmented by amplitude-dependent damping through the coefficients 𝜅*, 𝜅+, and 𝜅,.

---

## Page 60

30 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 线性和非线性水动力阻尼 指数因子 𝑒!"!|$"| 随速度增加而衰减线性突 升阻尼系数 𝑋(，以避免在包含二次阻尼 𝑋( ( 𝑢) 时重复计算突升阻力。 使用二维阻力系数的条 带理论横流阻力积分。 名义上的滚转、俯仰和偏航线性阻尼导数 通过系数𝜅*, 𝜅+,和𝜅,的幅值相关阻尼得到 增强。

---

## Page 61

31 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Summary: First-Principles 6-DOF Maneuvering Model Two state-space formulations are commonly used. The first uses the relative velocity 𝝂! as state and is convenient when ocean currents are modeled explicitly and relative velocity is measured (e.g., by a DVL). The second uses the absolute velocity 𝝂as state and is often preferred for surface vessels, where INS/GNSS systems provide measurements of absolute velocity. Irrotational ocean current Relative velocity vector Independent of 𝝂- = 𝑢, 𝑣, 𝑤.

---

## Page 62

31 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 摘要：基于第一性原理的六自由度机动模型 通常使用两种状态空间公式。第一种使用相对速度 𝝂! 作为状态，在明确建模洋流且测量相对速度（例如，通过 DVL ）时很方便。第二种使用绝对速度 𝝂 作为状态，在表面船舶中通常更受欢迎，因为 INS/GNSS 系统提供绝对速度的测 量。 Irrotational ocean current Relative velocity vector Independent of 𝝂- = 𝑢, 𝑣, 𝑤.

---

## Page 63

32 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen)

---

## Page 64

32 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen)

---

## Page 65

33 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen)

---

## Page 66

33 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen)

---

## Page 67

34 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Special Cases and Simplified Maneuvering Models

---

## Page 68

34 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 特殊情况和简化机动模型

---

## Page 69

35 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Longitudinal and Lateral Maneuvering Model for Marine Craft with Weak Cross-Coupling

---

## Page 70

35 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 具有弱横向耦合的海上船舶纵向与横向操纵模型

---

## Page 71

36 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Longitudinal and Lateral Maneuvering Model for Marine Craft with Weak Cross-Coupling Assumption 6.1 (Weak Longitudinal-Lateral Coupling) The equations of motion are expressed in a body-fixed frame {b} with origin at the CG. The craft is symmetric with respect to the xz-plane, and hydrodynamic coupling between longitudinal and lateral motions is neglected. The state vectors are This approximation is often appropriate for slender marine vehicles operating near straight-line motion, including submarines, torpedo-shaped AUVs, and conventional monohull ships, where longitudinal and lateral dynamics are only weakly coupled. The resulting 3-DOF longitudinal and lateral models on the next slides are based on the following assumptions and simplifications: Body-fixed coordinate origin: The equations are expressed in a body-fixed frame with origin at the CG. This eliminates the rigid- body coupling terms associated with xG, yG, and zG. Diagonal approximation: In high-fidelity maneuvering models, the off-diagonal added-mass and damping terms are usually retained. However, for slender vehicles with weak cross-coupling, and especially when only limited hydrodynamic data are available, it is common to approximate the added-mass and linear damping matrices by their diagonal elements. Expressing the equations at the CG reduces the neglected off-diagonal terms.

---

## Page 72

36 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 具有弱横向耦合的海上船舶纵向与横向操纵模型 假设 6.1（弱纵向-横向耦合） The equations of motion are expressed in a body-fixed frame {b} with origin at the CG. The craft is symmetric with respect to the xz-plane, and hydrodynamic coupling between longitudinal and lateral motions is neglected. The state vectors are This approximation is often appropriate for slender marine vehicles operating near straight-line motion, including submarines, torpedo-shaped AUVs, and conventional monohull ships, where longitudinal and lateral dynamics are only weakly coupled. 接下来的幻灯片中的三自由度纵向和横向模型是基于以下假设和简化条件： 机体固定坐标原点：方程在以质心(CG)为原点的机体固定参考系中表示。这消除了与 xG、yG 和 zG 相关的刚体耦合项 。 对角线近似：在高保真机动模型中，通常保留非对角附加质量和阻尼项。然而，对于具有较弱交叉耦合的细长车辆， 尤其是在只有有限水动力数据可用的情况下，通常将附加质量和线性阻尼矩阵近似为其对角线元素。在质心处表示方 程可以减少被忽略的非对角项。

---

## Page 73

37 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Longitudinal Equations of Motion based on Relative Velocity

---

## Page 74

37 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 基于相对速度的纵向运动方程

---

## Page 75

38 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Lateral Equations of Motion based on Relative Velocity

---

## Page 76

38 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 基于相对速度的横向运动方程

---

## Page 77

39 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Horizontal-Plane Maneuvering Model for Ships and USVs with Port–Starboard Symmetry Nonlinear Equations of Motion based on Relative Velocity The nonlinear hydrodynamic derivatives in sway and yaw can also be approximated by cross-flow drag integrals

---

## Page 78

39 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 具有左右对称性的船舶和无人水面船水平面机动模型 基于相对速度的非线性运动方程 The nonlinear hydrodynamic derivatives in sway and yaw can also be approximated by cross-flow drag integrals

---

## Page 79

40 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Horizontal-Plane Maneuvering Model for Ships and USVs with Port–Starboard Symmetry State-Space Models for Horizontal-Plane Motions Since 𝑪𝑹𝑩𝝂 is parametrized independent of linear velocity it follows from Property 10.1 that

---

## Page 80

40 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 具有左右对称性的船舶和无人水面船水平面机动模型 水平面运动的状态空间模型 由于 𝑪𝑹𝑩𝝂 是参数 独立于线速度的etrized，由性质得出 而 10.1 那个

---

## Page 81

41 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Longitudinal and Lateral Maneuvering Model for Marine Craft with Weak Cross-Coupling Several linear and nonlinear maneuvering models are included the MSS toolbox. Copyright ©  Bjarne Stenberg

---

## Page 82

41 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 具有弱横向耦合的海上船舶纵向与横向操纵模型 MSS 工具箱中包含了若干线性和非线性机动模型。 Copyright ©  Bjarne Stenberg

---

## Page 83

42 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS Toolbox Computation of Ocean Current Velocities in BODY and NED We assume that the current is irrotational and constant in NED. Consequently,

---

## Page 84

42 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MSS 工具箱 C在BODY和NED中计算海流速度 我们假设电流在NED中是无旋的且恒定。因此，

---

## Page 85

43 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3-DOF Linear Maneuvering Model for Ships and USVs Linear Maneuvering Equations (Surge–Sway–Yaw) U0 is the cruise speed used for linearization

---

## Page 86

43 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 适用于船舶和无人水面艇的三自由度线性机动模型 线性操纵方程（纵摇-横摇-偏航） U0 is the cruise speed 用于线性化

---

## Page 87

44 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3-DOF Linear Maneuvering Model for Ships and USVs Sway–Yaw Subsystem Surge Subsystem Notice: CA(n) includes the famous destabilizing Munk moment (from aerodynamics) and some other CA-terms Decoupling the surge–sway–yaw model into a surge subsystem and a sway–yaw subsystem:

---

## Page 88

44 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 适用于船舶和无人水面艇的三自由度线性机动模型 Sway–Yaw Subsystem 浪涌子系统 Notice: CA(n) includes the famous destabilizing Munk moment (from aerodynamics) and some other CA-terms 将纵荡–横荡–偏航模型解耦为纵荡子系统和横荡–偏航子系统:

---

## Page 89

45 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3-DOF Linear Models for Dynamic Positioning (DP) Kinematic Nonlinearity (The nonlinearity associated with the rotation matrix may be removed by treating the yaw angle as measured) Linear Time-Varying (LTV) Model for DP Controller-Observer Design (The bias b is constant in NED) (Control forces and moments) Linear Time-Varying (LTV) State-Space Model DP models are derived under the assumption of low-speed operation (typically up to 2m/s) , such that the quadratic Coriolis and centripetal terms and the nonlinear damping forces are negligible compared to the linear damping terms.

---

## Page 90

45 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 用于动态定位（DP）的三自由度线性模型 运动学非线性 (与旋转矩阵相关的非线性可以通过将偏航角视为已测量来消除) 用于DP控制器-观测器设计的线性时变（LTV）模型 (The bias b is constant in NED) (Control forces and moments) 线性时变 (LTV) 状态空间模型 DP 模型是在低速运行假设下推导的（通常最高可达 2 米/秒），因此二次科里奥利力和向心力项以及非线性 阻尼力相对于线性阻尼项可以忽略不计。

---

## Page 91

46 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Classical Maneuvering Models

---

## Page 92

46 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 经典机动模型

---

## Page 93

47 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) The Abkowitz (1964) Maneuvering Model Data-Driven Maneuvering Modeling Previous maneuvering models were derived from first principles: • Surge resistance • Cross-flow drag • Hydrodynamic force models An alternative approach is to fit experimental maneuvering data directly. Abkowitz’s Idea (1964) Represent the surge force, sway force, and yaw moment by a truncated Taylor-series expansion about straight-line motion: Key Assumptions 1. Third-order Taylor expansion about (u =U0). 2. Acceleration terms appear only linearly. 3. Port–starboard symmetry is enforced. 4. Acceleration–velocity coupling terms are neglected.

---

## Page 94

47 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 阿布科维茨（1964）机动模型 数据驱动的机动建模 以前的操作模型是从第一性原理推导出来的： • 浪涌抗性 • 横向流阻 • 水动力力模型 一种替代方法是直接拟合实验机动数据。 阿布考维茨的想法（1964） 用一个截断的表示浪涌力、摇摆力和偏航力矩 关于直线运动的泰勒级数展开： 关键假设 1. 关于 (u =U0) 的三阶泰勒展开。 2. 加速度项仅以线性方式出现。 3. 强制实施左舷–右舷对称。 4. 忽略加速度–速度耦合项。

---

## Page 95

48 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) The Abkowitz (1964) Maneuvering Model Taylor-Series Expansion

---

## Page 96

48 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 阿布科维茨（1964）机动模型 泰勒级数展开

---

## Page 97

49 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Second-Order Modulus Model (Fedyaevsky-Sobolev Model) The idea of using second-order modulus functions to represent the nonlinear dissipative forces and moment originates from the work of Fedyaevsky and Sobolev (1963). The model is particularly suitable for maneuvering at moderate and high speeds, where the hydrodynamic loads are dominated by quadratic cross-flow drag and propulsion losses.  This modeling philosophy was adopted by Norrbin (1970), who formulated a nonlinear maneuvering model based on modulus-function representations of the hydrodynamic forces and moments.

---

## Page 98

49 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 二阶模量模型（费佳耶夫斯基-索博列夫模型） 使用二阶模函数来表示非线性耗散力和力矩的想法源自 Fedyaevsky 和 Sobolev（1963 年）的工作。该模型特别适用于中高 速的机动，在此情况下，水动力载荷以二次横流阻力和推进损失为主。Norrbin（1970 年）采用了这种建模理念，提出了 一种基于水动力力和力矩模函数表示的非线性机动模型。

---

## Page 99

50 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Second-Order Modulus Model (Blanke, 1981) A simplified version of Norrbin’s model, retaining only the most important terms for steering and propulsion-loss prediction, was proposed by Blanke (1981). This model may be interpreted as a 2nd-order approximation of the cross-flow drag integrals.

---

## Page 100

50 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 二阶模量模型（Blanke, 1981） Blanke（1981）提出了诺尔宾模型的 简化版本，仅保留用于舵效和推进损 失预测的最重要项。该模型可以被解 释为横流阻力积分的二阶近似。

---

## Page 101

51 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) MMG Standard Maneuvering Model The Maneuvering Modeling Group (MMG) standard model, developed by the Japanese MMG committee and later standardized by Yasukawa and Yoshimura (2015) is an empirical 3-DOF maneuvering model for ships in surge, sway, and yaw. Unlike the second-order modulus and Abkowitz models, where the hydrodynamic forces and yaw moment are represented directly by polynomial or modulus functions of the body-fixed velocities, the MMG model decomposes the total force and moment into separate contributions from the hull, propeller, and rudder. This decomposition gives the model a clear physical interpretation and makes it possible to combine captive model tests with empirical formulas for the propeller and rudder. The hull force and moment contributions are represented by nonlinear hydrodynamic derivatives. A common MMG representation is Propulsion force (Section 9.1) Rudder force (Section 9.5)

---

## Page 102

51 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） MMG标准操纵模型 船舶机动建模组（MMG）标准模型，由日本MMG委员会开发，后来由Yasukawa和Yoshimura（2015）标准化，是一 个用于船舶纵摇、横摇和偏航的经验三自由度机动模型。与二阶模量模型和Abkowitz模型不同，后者的水动力作用 力和偏航力矩直接由船体固定速度的多项式或模量函数表示，MMG模型将总力和力矩分解为船体、螺旋桨和舵的单 独贡献。这种分解赋予模型明确的物理解释，并使得将固定模型试验与螺旋桨和舵的经验公式结合成为可能。 船体力和力矩的贡献由非线性水动力导数表示。一个常见的MMG表示方法是 推进力（第9.1节） 舵力（第9.5节）

---

## Page 103

52 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Chapter Goals - Revisited • Formulate the first-principles 6-DOF maneuvering model by combining rigid-body kinetics with hydrodynamic added mass, damping, hydrostatic restoring, and external forces. • Explain how the rigid-body and added-mass Coriolis–centripetal matrices arise in BODY-fixed coordinates and state their skew-symmetry property. • Explain when zero-frequency potential coefficients are appropriate for surge, sway, and yaw, why viscous damping must be added, and why the approximation fails for coupled 6-DOF motion. • Apply the power-based spectral averaging method to compute sea-state-dependent constant equivalent added-mass and damping matrices for 6-DOF maneuvering models. • Model linear and nonlinear hydrodynamic damping using ITTC surge resistance, cross-flow drag, and additional roll, pitch, and yaw damping. • Include constant irrotational ocean currents using relative velocity and formulate the dynamics with either relative or absolute velocity as the state. • Derive and compare simplified and classical maneuvering models, including longitudinal–lateral, horizontal-plane 3-DOF, dynamic positioning,  Abkowitz, second-order modulus, and MMG models.

---

## Page 104

52 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 章节目标 - 再访 • 通过将刚体动力学与流体动力附加质量、阻尼、静水恢复力和外力相结合，制定基于第一性原理的六自由度 机动模型。 • 解释刚体和附加质量科里奥利-向心矩阵在机体固定坐标系中是如何产生的，并说明它们的斜对称性特性。 • 解释在纵荡、横荡和偏航中何时适合使用零频潜势系数，为什么必须添加粘性阻尼，以及为什么该近似在耦合6 自由度运动中失效。 • 应用基于功率的谱平均方法来计算6自由度机动模型的海况相关恒定等效附加质量和阻尼矩阵。 • 使用 ITTC 冲程阻力、横向流拖力以及额外的横摇、纵倾和偏航阻尼来建模线性和非线性流体阻尼。 • 使用相对速度包含恒定无旋转的海洋洋流，并用相对速度或绝对速度作为状态来制定动力学。 • 推导并比较简化和经典的机动模型，包括纵横向、水平面三自由度、动态定位、Abkowitz、二阶模量和MMG模 型。

---
