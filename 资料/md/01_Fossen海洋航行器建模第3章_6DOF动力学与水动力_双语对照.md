# 01_Fossen海洋航行器建模第3章_6DOF动力学与水动力 (中英双语对照精读版)

> **自动转换源文件**: `01_Fossen海洋航行器建模第3章_6DOF动力学与水动力.pdf`  
> **双语对照总页数**: 58 页  

---

## Page 1

1 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Chapter 3 – Rigid-Body Kinetics To derive the marine craft equations of motion, it is necessary to study of the motion of rigid bodies, hydrodynamics, and hydrostatics. The overall goal of Chapter 3 is to show that the rigid-body equations of motion can be expressed in matrix-vector form about the CO according to the following: MRB Rigid-body mass matrix CRB Rigid-body Coriolis and centripetal matrix due to the rotation of {b} about {n} ν = [u, v, w, p, q, r]T generalized velocity expressed in {b} τRB = [X, Y, Z, K, M, N]T  generalized force expressed in {b} 3.1 Newton–Euler Equations of Motion about the CG 3.2 Newton–Euler Equations of Motion about the CO 3.3 Rigid-Body Equations of Motion CO is the body-fixed coordinate origin of the GNC system, and it is defined to meet specific control objectives. As such, the craft’s CO can be stabilized or programmed to follow a time-varying trajectory in 2-D or 3-D space.

---

## Page 2

一 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 第3章 – 刚体动力学 为了推导海上船舶的运动方程，有必要研究刚体运动、流体力学和静 水力学。 第三章的总体目标是展示刚体运动方程可以根据以下内容以矩阵-向量形式围绕质 心表示： MRB 刚体质量矩阵 CRB 由于 {b} 关于 {n} 的旋转引起的刚体科里奥利和向 心矩阵 ν = [u, v, w, p, q, r]T 在 {b} 中表示的广义速度 τRB = [X, Y, Z, K, M, N]T   在 {b} 中表示的广义力 3.1 关于质心的牛顿–欧拉运动方程 3.2 关于质心 系的牛顿–欧拉运动方程 3.3 刚体运动方程 CO是GNC系统的机体固定坐标原 点，它的定义是为了满足特定的 控制目标。因此，飞行器的CO可 以被稳定或编程以在二维或三维 空间中跟随时间变化的轨迹。

---

## Page 3

2 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Chapter Goals • Understand that Newton’s 2nd law and its generalization to the Newton-Euler equations of motion is formulated in an “approximative” inertial frame usually chosen as the tangent plane NED. • Understand why we get a CRB matrix when transforming the equations of motion to a BODY-fixed rotating reference frame instead of NED. • Be able to write down and simulate the rigid-body equation of motion about the CG for a vehicle moving in 6 DOFs. • Know how to transform the rigid-body equation of motion to other reference points such as the CO. This involves using the H-matrix (system transformation matrix) defined in Appendix C. • Understand the: - 6 x 6 rigid-body matrix MRB - 6 x 6 Coriolis and centripetal matrix  CRB and how it is computed from MRB - Parallel-axes theorem and its application to moments of inertia

---

## Page 4

2 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 章节目标 • 要理解牛顿第二定律及其推广到牛顿-欧拉运动方程，是在一个“近似的”惯性参考系中表述 的，这个参考系通常选择为切平面NED。 • 理解为什么当将运动方程转换到机体固定的旋转参考系而不是NED时，我们会得到一个CRB 矩阵。 • 能够写出并模拟车辆在六自由度运动中关于质心的刚体运动方程。 • 了解如何将刚体运动方程转换到其他参考点，例如质心。这涉及使用附录C中定义的H矩阵（ 系统转换矩阵）。 • 理解：- 6 x 6 刚体矩阵 MRB - 6 x 6 科里奥利和向心矩阵 CRB  以及它如何从 MRB 计算得出 - 平行轴定理及其在转动惯量中的应用

---

## Page 5

3 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) The equations of motion will be represented in two body-fixed reference points 1) Center of gravity (CG), subscript g 2) Origin CO of {b}, subscript b These points coincides if the vector Time differentiation of a vector in a moving reference frame {b} satisfies Time differentiation in {b} is denoted as Chapter 3 – Rigid-Body Kinetics

---

## Page 6

3 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 运动方程将以两个固定于物体的参考点表示 1) 重心 (CG)，下标 g 2) {b} 的原点 CO，下标 b 如果向量，这些点重合 在运动参考系 {b} 中，向量的时间微分 满足 {b}中的时间微分表示为 第3章 – 刚体动力学

---

## Page 7

4 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Coordinate-free vector: A vector        , velocity of {b} with respect to {n}, is defined by its magnitude and direction but without reference to a coordinate frame. Coordinate vector: A vector        decomposed in the inertial reference frame is denoted by Newton-Euler Formulation Newton's Second Law relates mass m, acceleration       and force       according to where the subscript g denotes the center of gravity (CG). Euler's First and Second Axioms Euler suggested to express Newton's Second Law in terms of conservation of both linear momentum       and angular momentum      according to: and are forces/moments about the body’s CG is the angular velocity of frame b relative frame i Ig is the inertia dyadic about the body's CG 3.1 Newton-Euler Equations of Motion about the CG !⃗" !⃗" !⃗" Isaac Newton (1642-1726) Wikimedia Commons Leonhard Euler (1707-1783) Wikimedia Commons !⃗" !⃗"

---

## Page 8

4 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 无坐标矢量：一个矢量        ，{b} 相对于 {n} 的速度，通过其大小和方向定义，但不 参考坐标系。坐标矢量：在惯性参考系中分解的矢量        表示为 牛顿-欧拉公式 牛顿第二定律根据质量 m、加速度 和力 的关系 下标 g 表示重心 (CG)。 欧拉的第一和第二公理 欧拉建议用守恒的方式表达牛顿第二定律 根据：线性动量和角动量 并且作用在物体质心上的力/力矩是相对于参 考系 i 的参考系 b 的角速度 Ig 是物体质心的惯性 二重项 3.1 关于质心的牛顿-欧拉运动方程 !!" !!" !! " 艾萨克·牛顿（1642-1726 ）维基共享资源 L莱昂哈德·欧拉（1707-178 3）维基共享资源 !!" !!"

---

## Page 9

5 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) When deriving the equations of motion, it will be assumed that: (1) The vessel is rigid (2) The NED frame is inertial—that is, {n} ≈ {i} 3.1 Translational Motion about the CG The first assumption eliminates the consideration of forces acting between individual elements of mass while the second eliminates forces due to the Earth's motion relative to a star-fixed inertial reference system such that For guidance and navigation applications in space, it is usual to use a star-fixed reference frame or a reference frame rotating with the Earth. Marine craft are, on the other hand, usually related to the NED reference frame. This is a reasonable assumption since forces on a marine craft due to the Earth's rotation ωie = 7.2921 × 10−5 rad/s are quite small compared to the hydrodynamic forces.

---

## Page 10

5 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 在推导运动方程时，将假设： (1) 该容器是刚性的 (2) NED 框架是惯性的——也就是说，{n} ≈ {i} 3.1 关于重心的平动运动 第一个假设排除了考虑作用在各个质量元素之间的力，而第二个假设排除了由于地球相对于恒星固定惯 性参考系运动而产生的力，因此 在空间中的导航和引导应用中，通常使用恒星固定参考系或随地球旋转的参考系。另一方面，海上船舶 通常与NED参考系相关。这是一个合理的假设，因为地球自转对海上船舶的作用力 ωie = 7.2921 × 10−5 rad/s 相比于流体动力，尺寸相当小。

---

## Page 11

6 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Body-fixed reference frame {b} is fixed in the point CO and rotating with respect to the inertial frame {i} Time differentiation of         in a moving reference frame {b} gives For a rigid body, the CG satisfies Translational Motion about the CG Expressed in {b} {n} is inertial 3.1 Translational Motion about the CG

---

## Page 12

6 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） Body-fixed reference frame {b} is fixed in the point CO and rotating with respect to the inertial frame {i} 在运动参考系 {b} 中的时间微分得到 对于刚体，质心满足 Translational Motion about the CG Expressed in {b} {n} is inertial 3.1 关于重心的平动运动

---

## Page 13

7 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) The derivation starts with the Euler’s 2nd axiom where is the inertia dyadic where Ix, Iy, and Iz are the moments of inertia about {b} and Ixy=Iyx, Ixz=Izx and Iyz=Izy are the products of inertia defined as Rotational Motion about the CG Expressed in  {b} 3.1 Rotational Motion about the CG

---

## Page 14

7 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 推导从欧拉的第二公理开始 inertia dyadic 在哪里 其中 Ix, Iy 和 Iz 是关于 {b} 的 moments of inertia，而 Ixy=Iyx, Ixz=Izx 和 Iyz=Izy 是定义为 products of inertia 绕质心的旋转运动用 {b} 表示 3.1 质心的旋转运动

---

## Page 15

8 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) The Newton-Euler equations can be represented in matrix form according to Expanding the matrices give Isaac Newton (1642-1726)   Leonhard Euler (1707-1783) Wikimedia Commons Wikimedia Commons 3.1 Equations of Motion about the CG

---

## Page 16

8 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 牛顿-欧拉方程可以根据矩阵形式表示 展开矩阵得到 艾萨克·牛顿（1642-1726）   莱昂哈德·欧拉（1707-17 83）  维基共享资源  维基共享资源 3.1 关于质心的运动方程

---

## Page 17

9 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) It is recommended to represent the equations of motion in the origin of an arbitrary body-fixed Coordinate Origin (CO) instead of the Centre of Gravity (CG), which can be time-varying due to varying payload and fuel consumption. Which Coordinate Origin Should I Use? The CO of the GNC system is chosen to satisfy the control objective. For instance, the CO can be either stabilized, acting as the point about which the craft rotates during stationkeeping, or directed to track a time-varying path in 2-D or 3-D space, serving as the point that follows the designated trajectory.

---

## Page 18

9 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 建议将运动方程表示在任意刚体固定坐 标原点（CO）处，而不是重心（CG）， 因为重心可能由于载荷变化和燃料消耗 而随时间变化。 我应该使用哪个坐标原点？ TheGNC 系统的 CO 选择以满足 control 目标。例如，CO 可以是 sta被稳定，作为工艺的转折点 rot在保持位置期间，或被指示在二维或三维空间 中跟踪随时间变化的路径，作为跟随指定轨迹的 点。

---

## Page 19

10 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) For marine craft, it is desirable to derive the equations of motion for an arbitrary Coordinate Origin (CO ) usually chosen as coordinate origin of the GNC system. The equations of motion can be transformed from the CG to the CO using the following coordinate transformation (see Appendix C) The transformation matrix is 3.2 Newton-Euler Equations of Motion about the CO

---

## Page 20

10 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 对于海上船舶，最好为任意坐标原点（CO）推导运动方程，这通常选择为 GNC系统的坐标原点。 可以使用以下坐标变换（见附录C）将运动方程从重心（CG） 转换到质心（CO） T变换矩阵是 3.2 关于质心的牛顿-欧拉运动方程

---

## Page 21

11 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.2 Newton-Euler Equations of Motion about the CO Expanding the matrices Newton-Euler equations in matrix-vector form about the CO Newton-Euler equations in matrix-vector form about the CG (see Section 3.1) See App. C for more details It is possible to rewrite              and using the Parallel-Axis Theorem. The motivation for this is to replace Ig with Ib (that is the inertia tensor in the CO instead of the CG).

---

## Page 22

11 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 3.2 关于质心的牛顿-欧拉运动方程 展开矩阵 关于质心的牛顿-欧拉方程的矩阵-向量形式 关于质心的牛顿-欧拉方程矩阵-向量形式（见第3.1节） 详情请参见附录C 可以使用平行轴定理重写              和。这 样做的动机是用 Ib (（即质心处的惯性张 量）替换 Ig 而不是重心处的 CG)。

---

## Page 23

12 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.2 Newton-Euler Equations of Motion about the CO Christian Huygens (1629-1695) Wikimedia Commons Jakob Steiner (1796-1863) Wikimedia Commons Ib b

---

## Page 24

12 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.2 关于质心的牛顿-欧拉运动方程 克里斯蒂安·惠更斯 (1629-169 5) 维基共享资源 雅各布·斯坦纳（1796-18 63）维基共享资源 <l atexit sha1_base64="h3cheg4jcED7 mwfgEGNj6P93jo=">AB+3icbVDNS8Mw HE3n15xfdR69BIfgabQi0+PAi94muA/Yakn TdAtLk5Kk4ij9V7x4UMSr/4g3/xvTrQfd fBDyeO/3Iy8vSBhV2nG+rcra+sbmVnW7t rO7t39gH9Z7SqQSky4WTMhBgBRhlJOupqR QSIJigNG+sH0uvD7j0QqKvi9niXEi9GY0 4hipI3k2/VRIFioZrG5stvcDx4C324TWc OuErckjRAiY5vf41CgdOYcI0ZUmroOon2 MiQ1xYzktVGqSILwFI3J0FCOYqK8bJ49h6d GCWEkpDlcw7n6eyNDsSrimckY6Yla9grx P2+Y6ujKyhPUk04XjwUpQxqAYsiYEglw ZrNDEFYUpMV4gmSCGtTV82U4C5/eZX0zp tuq9m6u2i0nbKOKjgGJ+AMuOAStMEN6IAuw OAJPINX8Gbl1ov1bn0sRitWuXME/sD6/A F3X5St</latexit> Ib b

---

## Page 25

13 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.2 Newton-Euler Equations of Motion about the CO Jacobi identity

---

## Page 26

13 L ecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.2 关于质心的牛顿-欧拉运动方程 Jacobi identity

---

## Page 27

14 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Translational Motion about the CO Expressed in {b} 3.2 Translational Motion about the CO An alternative representation  using vector cross products is Copyright ©  Bjarne Stenberg Copyright ©  Bjarne Stenberg

---

## Page 28

14 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 关于 CO 的平动表达在 {b} 中 3.2 关于质心的平动 使用向量叉乘的另一种表示是 Copyright ©  Bjarne Stenberg Copyright ©  Bjarne Stenberg

---

## Page 29

15 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Rotational Motion about the CO Expressed in {b} An alternative representation  using vector cross products is 3.2 Rotational Motion about the CO Christian Huygens (1629-1695) Wikimedia Commons Jakob Steiner (1796-1863) Wikimedia Commons

---

## Page 30

15 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 绕 CO 的旋转运动用 {b} 表示 使用向量叉乘的另一种表示是 3.2 关于质心的旋转运动 C克里斯蒂安·惠更斯 (1629-16 95) 维基共享资源 雅各布·斯坦纳（1796-18 63）维基共享资源

---

## Page 31

16 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 Rigid-Body Equations of Motion Component Form (SNAME 1950) These are the 6-DOF rigid-body equations of motion commonly found in textbooks. The upcoming formulas will provide an alternative matrix-vector representation.

---

## Page 32

16 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 刚体运动方程 组件形式（SNAME 1950） 这些是教材中常见的六 自由度刚体运动方程。 即将推出的公式将提供 一种替代的 matrix-vector 表示方式 。

---

## Page 33

17 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 Rigid-Body Equations of Motion Matrix-Vector Form Property 3.1  (Rigid-Body System Inertia Matrix) ν = !!"! #!$! %!& Generalized velocity Generalized force

---

## Page 34

17 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 3.3 刚体运动方程 矩阵-向量形式 属性 3.1（刚体系统惯性矩阵） ! ! !!！"！#！$！%！&“  广义速度 广 义力

---

## Page 35

18 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 Rigid-Body Equations of Motion

---

## Page 36

18 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 刚体运动方程

---

## Page 37

19 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Theorem 3.2  (Coriolis-Centripetal Matrix from System Inertia Matrix) Let M be a 6×6 system inertia matrix defined as: where M21= M12T. Then the Coriolis-centripetal matrix can always be parameterized such that where Proof: Sagatun and Fossen (1991). 3.3 Rigid-Body Equations of Motion ! = != !!! !!" !"! !"" > # !ν= "!×! #$""ν" + $"#ν# #$""ν" + $"#ν# #$#"ν" + $##ν# ν! = !""" #" ν#= $" %"& Sagatun, S. I. and T. I. Fossen (1991). Lagrangian Formulation of Underwater Vehicles' Dynamics. IEEE International Conference on Systems, Man, and Cybernetics, Charlottesville, VA, USA, IEEE Xplore, pp. 1029-1034.

---

## Page 38

19 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 定理 3.2 （由系统惯性矩阵得到的科里奥利-向心矩阵） 设 M 为一个 6×6 system inertia matrix，定义如下： 其中 M21= M12T。然后 Coriolis-centripetal matrix 总是可以被参数化，使得 哪里 证据：Sagatun 和 Fossen（1991）。 3.3 刚体运动方程 ! = != !!! !!" !"! !"" > # !ν= "!×! #$""ν" + $"#ν# #$""ν" + $"#ν# #$#"ν" + $##ν# !!! !!“ "” #“” ！#“ ！$” %“ &” Sagatun, S. I. 和 T. I. Fossen (1991)。水下车辆动力学的拉格朗日公式。IEEE International Conference on Systems, Man,  and Cybernetics，弗 吉尼亚州夏洛茨维尔，美国，IEEE Xplore，第1029-1034页。

---

## Page 39

20 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Property 3.2 (Rigid-Body Coriolis and Centripetal Matrix) The rigid-body Coriolis and centripetal matrix can always be represented such that                is skew-symmetric. This is mathematically equivalent to 3.3 Rigid-Body Equations of Motion !!"ν !!"ν The skew-symmetric property is very useful when designing nonlinear motion control system since the quadratic form νTCRB(ν)ν ≡ 0 This is exploited in energy-based control designs where Lyapunov functions play a key role. The same property is also used in nonlinear observer design. There exist several parameterizations that satisfy Property 3.2. Two important ones are the: • Lagrangian parametrization • Linear velocity-independent parameterization which are presented on the forthcoming pages.

---

## Page 40

20 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 属性 3.2（刚体科里奥利力和向心力矩阵） rigid-body Coriolis and centripetal matrix 总是可以被表示为 suc h 那是斜对称的。这在数学上等价于 3.3 刚体运动方程 !!"!!" ! !"!!" 斜对称性质在设计非线性运动控制系统时非常有用，因为二次型 νTCRB(ν)ν ≡ 0 这在基于能量的控制设计中得到了利用，其中李雅普诺夫函数起着关键作用。相同的特性也用于非线性观测 器设计。 存在几种满足性质 3.2 的参数化。其中两个重要的是： • 拉格朗日参数化 • 线速度无关参数化 将会在接下来的页面中呈现的。

---

## Page 41

21 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Lagrangian Parameterization Application of the Theorem 3.2 with M = MRB yields the following expression which can be rewritten according to To ensure that CRB(ν) = -CRB(ν)T, it is necessary to use  S(ν ₁)ν ₁ = 0 and add S(ν₁) in CRB{21} Joseph-Louis Lagrange (1736-1813) Wikimedia Commons 3.3 Rigid-Body Equations of Motion Sagatun, S. I. and T. I. Fossen (1991). Lagrangian Formulation of Underwater Vehicles' Dynamics. IEEE International Conference on Systems, Man, and Cybernetics, Charlottesville, VA, USA, IEEE Xplore, pp. 1029-1034.

---

## Page 42

21 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 拉格朗日参数化 将定理 3.2 应用于 M = MRB 得到以下表达式 可以根据⋯⋯重写 为了确保 CRB(ν) = -CRB(ν)T，有必要使用 S(ν  )ν   = 0 并在 CRB{21} 中加入 S(ν ) 约瑟夫-路易·拉格朗日 (1736-1813 ) 维基共享资源 3.3 刚体运动方程 Sagatun, S. I. and T. I. Fossen (1991). Lagrangian Formulation of Underwater Vehicles' Dynamics. IEEE International Conference on Systems, Man, and Cybernetics, Charlottesville, VA, USA, IEEE Xplore, pp. 1029-1034.

---

## Page 43

22 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 Rigid-Body Equations of Motion Component Form Lagrangian Parameterization

---

## Page 44

22 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 刚体运动方程 组件形式 拉格朗日参数化

---

## Page 45

23 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) This formula is the preferred representation when ocean currents enter the equations of motion. The main reason is that CRB(ν) does not depend on the linear velocity vector ν₁ = [u, v, w]T. For a marine craft exposed to irrotational ocean currents, it follows from Property 10.1 in Section 10.3 that where the relative velocity vector νr = ν - νc is defined such that only linear ocean current velocities are used Linear Velocity-Independent Parameterization By using the cross-product property S(ν₁)ν₂ = -S(ν₂)ν₁, it is possible to move S(ν₁)ν₂ from CRB{12} to CRB{11}. This gives an expression for CRB(ν) that is independent of linear velocity ν₁ (Fossen and Fjellstad 1995) 3.3 Rigid-Body Equations of Motion Fossen, T. I. and O.-E. Fjellstad (1995). Nonlinear Modelling of Marine Vehicles in 6 Degrees of Freedom. International Journal of Mathematical Modelling of Systems 1(1), 17-27.

---

## Page 46

23 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 当海流进入运动方程时，这个公式是首选表示方法。主要原因是 CRB(ν) 不依赖于线速度向量 ν  = [u, v , w]T。对于暴露在无旋海流中的海上航行器，根据第10.3节中的性质10.1可知 其中相对速度矢量 νr = ν - νc 的定义仅使用线性洋流速度 线速度无关参数化 通过使用交叉乘积性质 S(ν )ν  = -S(ν )ν ，可以将 S(ν )ν  从 CRB{12} 移动到 CRB{11}。这给出了一个与线 速度 ν  无关的 CRB(ν) 表达式 (Fossen 和 Fjellstad 1995) 3.3 刚体运动方程 Fossen, T. I. 和 O.-E. Fjellstad (1995)。海洋船舶六自由度非线性建模。《v22》 《v23》1(1), 17-27。

---

## Page 47

24 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 Rigid-Body Equations of Motion Linear Velocity-Independent Parameterization See Appendix C for more details This formula can also be expressed in terms of the CRB matrix in the CG, and the transformation matrix from the CG to the CO

---

## Page 48

二十四 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 刚体运动方程 线速度无关参数化 更多详情请参见附录C 这个公式也可以用CG中的CRB矩阵以及从CG到CO的变换矩阵来表示

---

## Page 49

25 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 Rigid-Body Equations of Motion

---

## Page 50

25 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 刚体运动方程

---

## Page 51

26 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 Linearized 6-DOF Rigid-Body Equations of Motion The nonlinear rigid-body equations of motion can be linearized about ν0 = [U, 0 , 0, 0, 0, 0]T for a marine craft moving at forward speed U. The linearized Coriolis and centripetal forces are recognized as !!" ̇ν + "!"νν = τ!" !

---

## Page 52

26 讲义：海洋船舶流体动力学与运动控制（T. I. Fossen） 3.3 线性化六自由度刚体运动方程 非线性刚体运动方程 可以关于 ν0 = [U, 0, 0, 0, 0, 0]T 对沿前进速度 U 运动的海洋船舶进行线性化。 线性化的科里奥利力和向心力被认为是 !!" !! "!"!!"! # "!"" !!"!!!

---

## Page 53

27 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 Linearized 6-DOF Rigid-Body Equations of Motion

---

## Page 54

27 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 3.3 线性化六自由度刚体运动方程

---

## Page 55

28 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Summary: 6-DOF Rigid-Body Equations of Motion Newton–Euler Equations of Motion about the CO CG to CO Matrix Transformations

---

## Page 56

28 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 摘要：6自由度刚体运动方程 关于质心的牛顿–欧拉运动方程 CG to CO Matrix Transformations

---

## Page 57

29 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) Chapter Goals - Revisited • Understand that Newton’s 2nd law and its generalization to the Newton-Euler equations of motion is formulated in an “approximative” inertial frame usually chosen as the tangent plane NED. • Understand why we get a CRB matrix when transforming the equations of motion to a BODY-fixed rotating reference frame instead of NED. • Be able to write down and simulate the rigid-body equation of motion about the CG for a vehicle moving in 6 DOFs. • Know how to transform the rigid-body equation of motion to other reference points such as the CO. This involves using the H-matrix (system transformation matrix) defined in Appendix C. • Understand the: - 6 x 6 rigid-body matrix MRB - 6 x 6 Coriolis and centripetal matrix  CRB and how it is computed from MRB - Parallel-axes theorem and its application to moments of inertia

---

## Page 58

29 Lecture Notes: Marine Craft Hydrodynamics and Motion Control (T. I. Fossen) 章节目标 - 再访 • 要理解牛顿第二定律及其推广到牛顿-欧拉运动方程，是在一个“近似的”惯性参考系中表述 的，这个参考系通常选择为切平面NED。 • 理解为什么当将运动方程转换到机体固定的旋转参考系而不是NED时，我们会得到一个CRB 矩阵。 • 能够写出并模拟车辆在六自由度运动中关于质心的刚体运动方程。 • 了解如何将刚体运动方程转换到其他参考点，例如质心。这涉及使用附录C中定义的H矩阵（ 系统转换矩阵）。 • 理解：- 6 x 6 刚体矩阵 MRB - 6 x 6 科里奥利和向心矩阵 CRB  以及它如何从 MRB 计算得出 - 平行轴定理及其在转动惯量中的应用

---
