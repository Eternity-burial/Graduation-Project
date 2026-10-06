# 01_Fossen海洋航行器建模第2章_运动学与坐标系 (中英双语对照精读版)

> **自动转换源文件**: `01_Fossen海洋航行器建模第2章_运动学与坐标系.pdf`  
> **双语对照总页数**: 102 页  

---

## Page 1

1 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Chapter 2 - Kinematics 2.1 Kinematic Preliminaries 2.2 Transformations between BODY and NED 2.3 Transformations between ECEF and NED 2.4 Transformations between ECEF and Flat-Earth Coordinates 2.5 Transformations between BODY and FLOW “The study of dynamics can be divided into two parts: kinematics, which treats only geometrical aspects of motion, and kinetics, which is the analysis of the forces causing the motion” Overall Goal of Chapters 2 to 10 Represent the 6-DOF equations of motion in a compact matrix-vector form according to: BODY

---

## Page 2

1 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 第二章 - 运动学 2.1 运动学初步 2.2 BODY与NED之间的变换 2.3 ECEF与N ED之间的变换 2.4 ECEF与平地坐标之间的变换 2.5 BODY 与FLOW之间的变换 “动力学的研究可以分为两部分：运动学，它只 处理运动的几何方面；动力学，它是对引起运动 的力的分析” 第2到第10章的总体目标 根据以下内容，以紧凑的矩阵-向量形式表示六自由 度运动方程： BODY

---

## Page 3

2 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Chapter Goals • Understand the geographic reference frame NED, the Earth-centered reference frame ECEF and the body-fixed reference frame BODY. • Understand what FLOW axes are and why we use these axes for marine craft and aircraft • Be able to write down the differential equations relating BODY velocities to NED positions, both for Euler angles and unit quaternions. • Be able to: • Transform ECEF (xe, ye, ze) positions to (longitude, latitude, height) and vice versa • Transform (longitude, latitude, height) to flat-Earth positions (xn, yn, zn) and vice versa • Define, visualize, and explain the use of: • Angle of attack a • Sideslip angle b • Vertical crab angle ac • Horizontal crab angle bc • Heading angle y • Course angle c

---

## Page 4

2 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 章节目标 • 理解地理坐标系NED、地心坐标系ECEF以及机体固定坐标系BODY。 • 了解什么是FLOW轴以及为什么我们在海上船舶和飞机上使用这些轴 • 能够写出将机体速度与NED位置相关联的微分方程，包括欧拉角和单位四元数的情 况。 • 能够： • 将 ECEF (xe, ye, ze) 位置转换为（经度，纬度，高度），反之亦然 • 将（经度, 纬度, 高度）转换为平面地球坐标（xn, yn, zn），反之亦然 • 定义、可视化并解释以下的用途： • 攻角 a • 侧滑角 b • 垂直螃蟹角 ac • 水平螃蟹角 bc • 航向角 y • 航向角 c

---

## Page 5

3 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) {i}: The Earth-centered inertial reference frame (ECI) {i} = (xi, yi, zi) is an inertial frame for terrestrial navigation, that is a nonaccelerating reference frame in which Newton’s laws of motion apply. {e}: The Earth-centered Earth-fixed reference frame (ECEF) {e} = (xe, ye, ze) has its origin oe fixed to the center of the Earth but the axes rotate relative to the inertial frame ECI, which is fixed in space. ωe t ωe x y y x z i i e e i ze ! ECEF/ECI Earth-Centered Reference Frames xe - axis in the equatorial plane pointing towards the zero/prime meridian; same longitude as the Greenwich observatory ye - axis in the equatorial plane completing the right-hand frame ze - axis pointing along the Earth’s rotational axis The Earth rotation is ωie = 7.2921 × 10−5 rad/s and the Earth’s rotational vector expressed in {e} is 2.1 Reference Frames

---

## Page 6

三 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) {i}：地心惯性参考系 (ECI) {i} = (xi, yi, zi) 是地面导航的惯性参考系，即一个非加速参考系 ，在其中牛顿运动定律适用。 {e}：地心地固参考系 (ECEF) {e} = (xe, ye, ze) 的原点 oe 固定在地球中心 但是这些轴相对于惯性坐标系ECI旋转，而ECI在空间中 是固定的。 ωe t ωe x y y x z i i e e i ze ! ECEF/ECI 地心参考系 xe - 位于赤道平面上，指向零度/本初子午线的轴；与格林威治天文台 同经度 ye  - 位于赤道平面上，完成右手坐标系的轴 ze  - 指向地球自转 轴的轴 地球的自转角速度是 ωie = 7.2921 × 10−5 弧度/秒，地球的旋转向量用 {e} 表示为 2.1 参考系

---

## Page 7

4 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.1 Reference Frames (cont.) {n}: The North-East-Down reference frame (NED) {n} = (xn, yn, zn) has its origin on defined relative to the Earth’s reference ellipsoid (WGS 84), usually as the tangent plane to the ellipsoid with xn - axis points towards true North yn - axis points towards East zn - axis points downwards normal to the Earth’s surface N E D µ e x y l z e e BODY ECEF/ECI NED Geographic Reference Frames (Tangent Planes) Geographical reference frames are usually chosen as tangent planes on the surface of the Earth. • Terrestrial navigation: The tangent plane on the surface of the Earth moves with the craft and its location is specified by time- varying longitude-latitude values (l, μ). The tangent frame is usually rotated such that its axes points in the NED directions. • Local navigation: The tangent plane is fixed at constant values (l0 , μ0 ) and the position is computed with respect to a local coordinate origin. The axes of the tangent plane are usually chosen to coincide with the NED axes. “Flat-Earth navigation”: position is accurate to a smaller geographical area (10 km × 10 km).

---

## Page 8

四 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.1 参考系（续） {n}：东北下参考系（NED） {n} = (xn, yn, zn) 的原点 on  定义为相对 于地球参考椭球体（WGS 84），通常 作为椭球体的切平面 xn - 轴指向真北 yn  - 轴指向东方 zn - 轴指向垂直于地表向下 N E D µ e x y l z e e BODY ECEF/ECI NED 地理参考框架（切平面） 地理参考框架通常选择为地球表面上的切平面。 • 陆地导航：地球表面的切平面随飞行器移动，其位置由随 时间变化的经纬度值（l, μ）表示。切平面坐标系通常被旋 转，使其轴指向北-东-下（NED）方向。 • 局部导航：切平面固定在常数值 (l0, μ0)，位置相对于局部 坐标原点计算。切平面的轴通常选择与NED轴重合。 “平地球导航”：位置精确到较小的地理区域（10 公里 × 10 公里）。

---

## Page 9

5 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) {b}: The body-fixed reference frame (BODY) For marine craft, the body axes are chosen as: xb - longitudinal axis (directed from aft to fore) yb - transversal axis (directed to starboard) zb -normal axis (directed from top to bottom) {f}: The body-fixed flow axes reference frame (FLOW) Flow axes are used to align the x-axis with the craft’s velocity vector such that lift is perpendicular to the relative flow and drag is parallel. The transformation from FLOW to BODY axes is defined by two principal rotations where the rotation angles are the angle of attack α and the sideslip angle β. The main purpose of the flow axes is to simply the computations of lift and drag forces. N E D µ e x y l z e e BODY ECEF/ECI NED Body-Fixed Reference Frames The body-fixed reference frame {b} = (xb, yb, zb) with origin ob is a moving coordinate frame that is fixed to the craft. 2.1 Reference Frames (cont.)

---

## Page 10

5 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) {b}: 机体固定参考系 (BODY) 对于海洋船舶，机体坐标轴的选择如下：xb - 纵轴（从船尾指向船首） yb - 横轴（指向右 舷） zb - 法向轴（从顶部指向底部） {f}：机体固定的流动轴参考系 (FLOW) 流向轴用于将x轴与飞行器的速度矢量对齐，使升力垂直于相对气 流而阻力与之平行。从流向轴到机体轴的变换由两个主旋转定义 ，旋转角分别是迎角α和侧滑角β。流向轴的主要目的是简化升力 和阻力的计算。 N E D µ e x y l z e e BODY ECEF/ECI NED 身体固定参考系 以机体为固定参考系{b} = (xb, yb, zb) ，其原 点为ob，是一个固定在飞行器上的移动坐标 系。 2.1 参考系（续）

---

## Page 11

6 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) The most important reference point The following time-varying points are expressed  with respect to the CO The CF is located a distance LCF from the CO in the x-direction The center of flotation is the centroid of the water plane area Awp in calm water. For small angles (linear theory), the vessel will roll and pitch about this point. 2.1 Body-Fixed Reference Points

---

## Page 12

6 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 最重要的参考点 以下随时间变化的点是相对于 CO 表示的 CF位于距离CO在x方向LCF的地方 浮心是平静水面上水面面积 Awp 的质心。对于小角度（线性理论），船舶将围绕该点横摇和纵摇。 2.1 车体固定参考点

---

## Page 13

7 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.1 Generalized Coordinates For a marine craft not subject to any motion constraints Number of independent (generalized) coordinates =  DOFs The term generalized coordinates refers to the parameters that describe the configuration of the craft relative to some reference configuration. For marine craft, the generalized position and velocity vectors are These quantities are all formulated in NED. It is advantageous to express the velocities of the craft in the BODY frame. In other words The relationship between the velocity vector in NED and BODY will be derived on the subsequent pages.

---

## Page 14

7 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.1 广义坐标 对于不受任何运动约束的海上船只 Number of independent (generalized) coordinates =  DOFs 广义坐标一词指的是描述飞行器相对于某些参考构型的配置的参数。 对于海洋船舶，广义位置和速度向量为 T这些量都是用NED表示的。把速度表示出来是有利的 o在BODY框架中的工艺。换句话说 接下来的页面将推导NED和BODY中速度向量之间的关系。

---

## Page 15

8 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) !⃗= !! ""⃗! + !" ""⃗" + !# ""⃗# !! = "! !""# !""$ ! Coordinate-free vector (arrow notation) !⃗" " = !"#"$%&' ()' *+,( -'.(/&0 ()%( 1'2,+' ! Coordinate form of                   (bold notation) !⃗!" " ‘‘ Vector expressed in {n}’’ 2.1 Vector Notation (Fossen 2021)

---

## Page 16

8 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.1 向量表示法（Fossen 2021）

---

## Page 17

9 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) The notation is adopted from: SNAME (1950). Nomenclature for Treating the Motion of a Submerged Body Through a Fluid. The Society of Naval Architects and Marine Engineers, Technical and Research Bulletin No. 1-5, April 1950, pp. 1-15. 2.1 Six Degrees-of-Freedom (6-DOF) Motions 6-DOF refers to the freedom of movement of a rigid body in 3-D space. It describes how the object can translate and rotate relative to its own body-fixed axes. It is not used for NED coordinates.

---

## Page 18

9 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 该符号采用自： SNAME（1950）。处理潜入流体中的物体运动的命名法。The Society of Naval Architects and Marine Engineers, Technical and Research Bulletin No. 1-5, April 1950, pp. 1-15. 2.1 六自由度（6-DOF）运动 6自由度（6-DOF）指的是刚体在三维空间中的运动自由度。它描述了物体相对于自身固定坐 标轴的平移和旋转方式。它不用于NED坐标系。

---

## Page 19

10 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.1 Summary: 6-DOF Vectors 6-DOF generalized position, velocity and force vectors expressed in {b} Coordinate frames {b}, {n}, and {e} Superscripts mean: - b: vector expressed in {b}. - n: vector expressed in {n}. - e: vector expressed in {e}. Subscript nb means: - Angular velocity: rotational velocity of frame {b} with respect to frame {n}. - Linear velocity: translational velocity of the origin of {b} with respect to the origin of {n}. - Euler angles: orientation of frame {b} with respect to frame {n}. - Position: position vector from origin {n} to origin {b} No superscripts or subscripts are used on generalized vectors.

---

## Page 20

10 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.1 摘要：6自由度向量 以 {b} 表示的6自由度广义位置、速度和力向量 坐标系 {b}、{n} 和 {e} 上标表示： - b：在 {b} 中表示的向量 。 - n：在 {n} 中表示的向 量。 - e：在 {e} 中表示的 向量。 下标 nb 意思是： - 角速度：参考框架 {n} 下框架 {b} 的旋转速度。 - 线速度：参考框架 {n} 原点下框架 {b} 原点的平移速 度。 - 欧拉角：参考框架 {n} 下框 架 {b} 的方向。 - 位置：从原点 {n } 到原点 {b} 的位置向量。 广义向量上不使用上标或下标 。

---

## Page 21

11 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.2 Transformations between BODY and NED

---

## Page 22

11 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.2 BODY与NED之间的转换

---

## Page 23

12 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) λ × ! != "λ! Cross-product operator as matrix-vector multiplication: where S is a skew-symmetric matrix The inverse operator is denoted: 2.2 Transformations between BODY and NED (cont.)

---

## Page 24

12 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） ! × ! !! "!!"！ 叉积运算符作为矩阵-向量乘法： 其中 S 是一个斜对称矩阵 逆运算符表示为： 2.2 BODY 与 NED 之间的变换（续）

---

## Page 25

13 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Euler’s theorem on rotation where λ = λ!"λ#"λ$" %λ% = ! β !!!" " = "! "!!!" ! " "! " #= "λ"β $ 2.2 Transformations between BODY and NED (cont.) 4 ="p0l1X8yX/zS4T4QlNcEvrR3Wok=">ACZ3 icbVFbSyMxGM2Mumq9tF4QwZesRaisW2ZaUV8E 0Rd9012rQlNLJs1oMJMZkm+EMow/0jfFfmI6 z4mU/CBzOhXw5CRIpDHjek+OjU/8mJyarszMz s1XawuLFyZONeMdFstYXwXUcCkU74Aya8SzWk USH4Z3B2N9Mt7ro2I1TkME96L6I0SoWAULNWvPZ CIwm0QZn/yfkakDQ7oFgk40Bzv43/iRXbBETE TvHvzAxQhUmsvXu+Zs3yvymdTR8/BsTFpvCtv nJd916d/Zrda/pFYO/A78EdVTOab/2SAYxSyOug ElqTNf3EuhlVINgkucVkhqeUHZHb3jXQkXtyr2 s6CnHG5YZ4DW9ijABfsxkdHImGEUWOdoWfNVG 5H/07ophHu9TKgkBa7Y20VhKjHEeFQ6HgjNGcih BZRpYXfF7JZqysB+TcW4H98ndw0Wr6O82ds+ 36wWFZxRaQ+uogXy0iw7QMTpFHcTQs1Nxlpxl 58Wtuivu6pvVdcrMEvo07s9XTy26g=</latex it> Rω,ε = I3→3 + sin ω S(ε) + (1 →cos ω) S2(ε) R11 = (1 →cos ω) ε2 1 + cos ω, R22 = (1 →cos ω) ε2 2 + cos ω, R33 = (1 →cos ω) ε2 3 + cos ω, R12 = (1 →cos ω) ε1ε2 →ε3 sin ω, R21 = (1 →cos ω) ε2ε1 + ε3 sin ω, R23 = (1 →cos ω) ε2ε3 →ε1 sin ω, R32 = (1 →cos ω) ε3ε2 + ε1 sin ω, R31 = (1 →cos ω) ε3ε1 →ε2 sin ω, R13 = (1 →cos ω) ε1ε3 + ε2 sin ω

---

## Page 26

十三 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 欧拉旋转定理 哪里 !!!λ! λ# λ$ %!% !!! β !!!" "  ! "! "!!!" !  " "! " #! "λ"β $$%$$$ 2.2 BODY 与 NED 之间的变换（续） < latexit sha1_base64 = "p0l11X8yX/zS4T4QlNcEvrR3Wok = " > AAACZ3icbVFbSyMxGM2Mumq9tF4QwZesRaisW2ZaUV8E0Rd90 < 乳胶sha1_base64 = “5x + O757M6pbmEiMWl1ERB/F/q + s = ” > AAAEJ3icfVNdT9swFDXJPlj3QRmPe7GoNjEVqjiZYC9IaHvhEaYVk

---

## Page 27

14 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Three principal rotations !"#$%&'(')&*$&+,-$.)'/0 $$$$$$(*N2, (3&4'$ R $$$$$$6&',$'0('$ R !θ ! " #" $ $ % &$ &' !' !$ (' ($ "$ "' ψ ψ !7#$%&'(')&*$&+,-$8(9 $$$$$$(*N2, (3&4'$ R $$$$$$6&',$'0('$ R !ψ ) * #* ' ' $ &% &$ )% )$ (% ($ *% *$ θ + + !:#$%&'(')&*$&+,-$-&22 $$$$$$(*N2, (3&4'$ R $$$$$$6&',$'0('$ R !φ & ( #( % % $, ) #) - . )% !% ! #! - . "#"$ φ "% *#*- *% φ + λ = !"#" # β = φ λ = !"#" ! β = θ λ = !"!" # β = ψ !!!φ = " # # # $φ %φ # %φ $φ !!!θ = "θ # $θ # % # $θ # "θ !!!ψ = "ψ #ψ $ #ψ "ψ $ $ $ % 2.2 Euler Angle Transformation The ZXZ sequence is the proper Euler angle rotation sequence used in robotics, but for aircraft and spacecraft, we use the Tait–Bryan ZYX sequence (yaw-pitch-roll), so that the singularity occurs at ±90 degrees in pitch.

---

## Page 28

14 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Three principal rotations !"#$%&'(')&*$&+,-$.)'/0 $$$$$$(*N2, (3&4'$ R $$$$$$6&',$'0('$ R !θ ! " #" $ $ % &$ &' !' !$ (' ($ "$ "' ψ ψ !7#$%&'(')&*$&+,-$8(9 $$$$$$(*N2, (3&4'$ R $$$$$$6&',$'0('$ R !ψ ) * #* ' ' $ &% &$ )% )$ (% ($ *% *$ θ + + !:#$%&'(')&*$&+,-$-&22 $$$$$$(*N2, (3&4'$ R $$$$$$6&',$'0('$ R !φ & ( #( % % $, ) #) - . )% !% ! #! - . "#"$ φ "% *#*- *% φ + λ = !"#" # β = φ λ = !"#" ! β = θ λ = !"!" # β = ψ !!!φ = " # # # $φ %φ # %φ $φ !!!θ = "θ # $θ # % # $θ # "θ !!!ψ = "ψ #ψ $ #ψ "ψ $ $ $ % 2.2 Euler Angle Transformation The ZXZ sequence is the proper Euler angle rotation sequence used in robotics, but for aircraft and spacecraft, we use the Tait–Bryan ZYX sequence (yaw-pitch-roll), so that the singularity occurs at ±90 degrees in pitch.

---

## Page 29

15 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Linear velocity transformation (zyx convention) Small-angle approximation Euler angle rotation matrix 2.2 Euler Angle Transformation (cont.)

---

## Page 30

15 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 线速度变换（zyx 约定） 小角 le approximation 欧拉角旋转矩阵 2.2 欧拉角变换（续）

---

## Page 31

16 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) NED positions (continuous time and discrete time) Component form Euler’s method with sampling time h 2.2 Euler Angle Transformation (cont.) However, because of numerical accuracy and stability is it recommended to use a higher- order method such as RK4

---

## Page 32

16 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) NED 位置（连续时间和离散时间） 分量式 欧拉法，采样时间 h 2.2 欧拉角变换（续） 然而，由于数值精度和稳定性 ，建议使用更高阶的方法，例 如 RK4

---

## Page 33

17 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Angular velocity transformation (zyx convention) where Small angle approximation 2.2 Euler Angle Transformation (cont.) Singular point at θ = ± !"! ! !!" ! !" →= -

---

## Page 34

17 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 角速度变换（zyx 约定） 哪里 小角度近似 2.2 欧拉角变换（续） 奇异点在 θ ! !! ! !! !" !  ! !" < l a t e x i t s h a 1 _ b a s e 6 4 = " b / w W 6 I z i i J F u J M b Y k M 9 Y 4 W I l J U k = " > A A A B 7 H i c b V B N S 8 N A E J 3 U r 1 q / q h 6 9 B I v g q S Q i 1 W P R i 8 c K p i 2 0 o W y 2 k 3 b p Z h N 3 N 0 I J / Q 1 e P C j i 1 R / k z X / j p s 1 B W x 8 M P N 6 b Y W Z e k H C m t O N 8 W 6 W 1 9 Y 3 N r f J 2 Z W d 3 b / + g e n j U V n E q K X o 0 5 r H s B k Q h Z w I 9 z T T H b i K R R A H H T j C 5 z f 3 O E 0 r F Y v G g p w n 6 E R k J F j J K t J G 8 v s D H y q B a c + r O H P Y q c Q t S g w K t Q f W r P 4 x p G q H Q l B O l e q 6 T a D 8 j U j P K c V b p p w o T Q i d k h D 1 D B Y l Q + d n 8 2 J l 9 Z p S h H c b S l N D 2 X P 0 9 k Z F I q W k U m M 6 I 6 L F a 9 n L x P 6 + X 6 v D a z 5 h I U o 2 C L h a F K b d 1 b O e f 2 0 M m k W o + N Y R Q y c y t N h 0 T S a g 2 + e Q h u M s v r 5 L 2 R d 1 t 1 B v 3 l 7 X m T R F H G U 7 g F M 7 B h S t o w h 2 0 w A M K D J 7 h F d 4 s Y b 1 Y 7 9 b H o r V k F T P H 8 A f W 5 w 9 R U Y 5 h < / l a t e x i t > →= -

---

## Page 35

18 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) ODE for Euler angles ODE for rotation matrix Component form Must be combined with an algorithm for computation of the Euler angles from the rotation matrix where Euler angle attitude representations 2.2 Euler Angle Transformation (cont.)

---

## Page 36

18 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 欧拉角的常微分方程 旋转矩阵的常微分方程 分量式 必须与算法结合使用 从旋转矩阵计算欧拉角 哪里 欧拉角姿态表示 2.2 欧拉角变换（续）

---

## Page 37

19 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Summary: 6-DOF kinematic equations Component form 3-parameter representation with singularity at θ = ± !"! !"= φ!θ!ψ 2.2 Euler Angle Transformation (cont.)

---

## Page 38

19 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 摘要：六自由度运动学方程 分量式 在 θ 处具有奇异性的 三参数表示！! !  !"!! φ! θ! ψ" 2.2 欧拉角变换（续）

---

## Page 39

20 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) - Avoids the representation singularity of the 3-parameter Euler angle representation known as gimbal lock - Involves fewer trigonometric calculations , enhancing stability - Quaternion interpolation results in smoother transitions compared to Euler angles - Quaternion multiplication is more efficient and stable than combining Euler angles = !"#"$ Unit quaternion (Euler parameter) rotation matrix (Chou 1992) η = !"# β $ = !"#"$= λ%&' β # 2.2 Unit Quaternions Chou, J. C. K. (1992). Quaternion Kinematic and Dynamic Differential Equations. IEEE Transactions on Robotics and Automation 8(1), 53–64. 4-parameter representation

---

## Page 40

20 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) - 避免了被称为万向节锁的三参数欧拉角表示的表示奇异性 - 涉及较少的三角计算，提高了稳定性 - 四元数插值相比欧拉角能够产生更平滑的过渡 - 四元数乘法比组合欧拉角更高效、更稳定 ! " !!" #" $!  单位四元数（欧拉参数）旋转矩阵（Chou 1992） η = !"# β $ = !"#"$= λ%&' β # 2.2 单元四元数 Chou, J. C. K.（1992）。四元数运动学与动力学微分方程。《IEEE机器人与自动化汇刊》8(1), 53–64。 四参数表示

---

## Page 41

21 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Linear velocity transformation Component form (NED positions) Must be integrated under the constraint η! + " ! + ! ! + # ! = " 2.2 Unit Quaternions (cont.)

---

## Page 42

21 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 线速度变换 分量形式（北东天坐标位置） 必须在约束 η ! ! " ! ! ! ! ! # ! 下进行积分 2.2 单元四元数（续）

---

## Page 43

22 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Angular velocity transformation Alternative representation using the quaternion product Nonsingular to the price of one more parameter but unit quaternions are numerical efficient 2.2 Unit Quaternions (cont.)

---

## Page 44

22 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 角速度变换 使用四元数乘积的替代表示 对于多一个参数的价格来说是非奇 异的，但单位四元数在数值上是高 效的 2.2 单元四元数（续）

---

## Page 45

23 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 4-parameter representation Nonsingular but one more ODE is needed. Summary: 6-DOF kinematic equations (7 ODEs) Component form ! = η!"! #! $ 2.2 Unit Quaternions (cont.)

---

## Page 46

23 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 4 参数表示 非奇异，但需要再一个常微分方程。 摘要：6自由度运动学方程（7个常微分方程） 分量式 ! ! !η! "! #! $! 2.2 单元四元数（续）

---

## Page 47

24 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.2 Unit Quaternions (cont.) Discretization of the unit quaternion differential equation It is possible to rewrite the expression such that ˙q = T(q)w ˙q = ¯T(w)q q[k+1] is computed using the matrix exponential,  which serves as the exponential map for matrix Lie groups, ensuring an  exact discretization of the quaternion differential equation: q_dot = Tquat(w) * q             q[k+1] = expm(Tquat(w[k] * h) * q[k] You can replace the build-in Matlab function expm.m with the custom-made  MSS function expm_taylor.m for this computation.

---

## Page 48

二十四 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.2 Unit Quaternions (cont.) Discretization of the unit quaternion differential equation It is possible to rewrite the expression such that <latex it sha1_base 64="Q9+eNmF6R CzNneWIs7xLCvW lCc=">AC BnicbZDLSgMxFI Yz9VbrbdSlC MEi1E2ZkaJuhI blxV6g3YomUza hmaSaZJRyjAr N76KGxeKuPUZ3 Pk2pu0stPWHwM d/zklyfj9iVG nH+bZyK6tr6xv 5zcLW9s7unr1/0 FQilpg0sGBC tn2kCKOcNDTVjL QjSVDoM9LyR zfTeueSEUFr+t JRLwQDTjtU4y0 sXr2cTcQOun6 gXJOE3hNZxzv TQ+e0h7dtEpOz PBZXAzKIJMtZ 79Ze7DcUi4xgw p1XGdSHsJkp iRtJCN1YkQniE BqRjkKOQKC+ZrZ HCU+MEsC+kO VzDmft7IkGhUpP QN50h0kO1WJua /9U6se5feQnl UawJx/OH+jGDW sBpJjCgkmDNJ gYQltT8FeIhkg hrk1zBhOAurw MzfOye1Gu3FW KVSeLIw+OwAko ARdcgiq4BTXQAB g8gmfwCt6sJ +vFerc+5q05K5s 5BH9kf4A/3iY xA=</latexi t>˙q = T(q)w <latexit sha1_base64="V 40imntPmE+2m907BfE1puhatnY= ">ACDHicbVDNSgMxGMz6W+t f1aOXYBHqpexKUS9CwYvHCv2D 7lKy2Wwbmk2SVYpyz6AF1/Fi wdFvPoA3nwb03YP2joQGbmS/K NHzOqtG1/Wyura+sbm4Wt4vbO 7t5+6eCwrUQiMWlhwYTs+kgR jlpaoZ6caSoMhnpOPbqZ+5 5IRQVv6klMvAgNOA0pRtpI/VLZD YROXV+wIB1nGbyGc+76SKbNrP JwNs5Myq7aM8Bl4uSkDHI0+qU vcytOIsI1ZkipnmPH2kuR1BQz khXdRJEY4REakJ6hHEVEelsmQy eGiWAoZDmcA1n6u+JFEVKTSLf JCOkh2rRm4r/eb1Eh1deSnmca MLx/KEwYVALOG0GBlQSrNnEI QlNX+FeIgkwtr0VzQlOIsrL5P2 edW5qNbuauW6ndRAMfgBFSA y5BHdyCBmgBDB7BM3gFb9aT9W K9Wx/z6IqVzxyBP7A+fwABqZu J</latexit> ˙q = ¯T(w)q q[k+1] is computed using the matrix exponential,  which serves as the exponential map for matrix Lie groups, ensuring an  exact discretization of the quaternion differential equation: q_dot = Tquat(w) * q             q[k+1] = expm(Tquat(w[k] * h) * q[k] You can replace the build-in Matlab function expm.m with the custom-made  MSS function expm_taylor.m for this computation.

---

## Page 49

25 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.2 Unit Quaternion from Euler Angles NASA (2013). Mission Planning and Analysis Division. Euler Angles, Quaternions, and Transformation Matrices. https://ntrs.nasa.gov/api/citations/19770024290/downloads/19770024290.pdf

---

## Page 50

25 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 2.2 从欧拉角得到单位四元数 NASA（2013）。任务规划与分析部。欧拉角、四元数与变换矩阵。 https://ntrs.nasa.gov/api/citations/19770024290/downloads/19770024290.pdf

---

## Page 51

26 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Since the rotation matrices of the two kinematic representations are equal: ! = η!"! #! $ !ψ!θ "ψ!φ + !ψ"θ"φ "ψ"φ + !ψ!φ"θ "ψ!θ !ψ!φ + "φ"θ"ψ !ψ"φ + "θ"ψ!φ "θ !θ"φ !θ!φ = !## !#$ !#% !$# !$$ !$% !%# !%$ !%% Euler angle solutions: where atan2(y,x) is the 4-quadrant inverse tangent confining the result to !"= φ!θ!ψ 2.2 Euler Angles from a Unit Quaternion

---

## Page 52

26 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 由于这两种运动学表示的旋转矩阵相等： ! ! !η! "! #! $! !ψ!θ "ψ!φ ! !ψ"θ"φ "ψ"φ ! !ψ!φ"θ "ψ!θ !ψ!φ ! "φ"θ"ψ !ψ"φ ! "θ"ψ!φ "θ !θ"φ !θ! φ " !## !#$ !#% !$# !$$ !$% !%# !%$ !%% 欧拉角解法： 其中 atan2(y,x) 是将结果限制在四象限内的反正切函数  !"！!φ！θ！ψ" 2.2 从单位四元数求欧拉角

---

## Page 53

27 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Case Study: Numerical Integration of the Kinematic Differential Equations

---

## Page 54

二十七 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 案例研究：运动学微分方程的数值积分

---

## Page 55

28 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Case Study: Numerical Integration of the Kinematic Differential Equations (cont.)

---

## Page 56

二十八 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 案例研究：运动学微分方程的数值积分（续）

---

## Page 57

29 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) N E D µ e x y l z e e ECEF {e}-frame NED {n}-frame Longitude: l (deg) Latitude:                  µ (deg) Ellipsoidal height:  h (m) A point on or above the Earth’s surface is uniquely determined by: h NED axes definitions: N – North axis is pointing North E – East axis is pointing East D – Down axis is pointing down in the normal direction to the Earth’s surface 2.3 Transformation between ECEF and NED

---

## Page 58

29 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) N E D µ e x y l z e e ECEF {e}-frame NED {n}-frame 经度：l (度) 纬度：µ ( 度) 椭球高：h (米) 地球表面上或以上的一个点可以被唯 一确定如下： h NED 轴定义： N – 北轴指向北 E – 东轴指向东 D – 下轴指向地面法线方向向下 2.3 ECEF 与 NED 之间的变换

---

## Page 59

30 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) The transformation  between the ECEF and NED velocity vectors is: Two principal rotations: 1. A rotation l about the z-axis 2. A rotation –µ – p/2 about the y-axis. !"= #!μ 2.3 Longitude and Latitude Transformations

---

## Page 60

30 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） ECEF 和 NED 速度向量之间的变换是： 两个主要旋转： 1. 绕 z 轴旋转 l 2. 绕 y 轴旋转 –µ – p/ 2。  !"! !#! μ"" S 2.3 经度和纬度转换

---

## Page 61

31 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Satellite navigation system measurements are given in the ECEF frame: Not to useful for the operator. Presentation of terrestrial position data                                    is therefore made in terms of the ellipsoidal parameter's longitude l, latitude µ and height h. l, µ and h 2.3 Longitude/Latitude from ECEF Coordinates N E D µ e x y l z e e Transformation

---

## Page 62

31 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 卫星导航系统的测量值是在ECEF坐标系中给出的：对操作员没 有用。 因此，地面位置数据的呈现是以椭球参数的经度 l、纬度 µ 和高度 h 来表示的。 l, µ and h 2.3 从 ECEF 坐标获取经纬度 N E D µ e x y l z e e Transformation

---

## Page 63

32 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) while latitude µ and height h are implicitly  computed by !"#"$%C%#' ()$$%*C' !" = ! "#A %"# & 'E)*+,-.*/ -*0.)1 ,2 P//.41,.0 51P&.&*6,- *7.18 !# = ! "9! #9: & ;,/*- *7.1 -*0.)1 ,2 P//.41,.0 51P&.&.<,- *7.18 ω" = #=:>:%%9 ⋅%? 9 -*0@1 A<B)/*- CP/,a.+E ,2 +cP '*-+c " = ?=?A%A 'aaP<+-.a.+E ,2 P//.41,.0 2.3 Longitude/Latitude from ECEF Coordinates (cont.) WGS-84 World Geodetic System (1984). Its Definition and Relationships with Local Geodetic Systems. DMA TR 8350.2, 2nd ed., Defence Mapping Agency, Fairfax, VA.

---

## Page 64

32 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 当纬度 µ 和高度 h 被隐式计算时 !"#"$%C%#' ()$$%*C' !" = ! "#A %"# & 'E)*+,-.*/ -*0.)1 ,2 P//.41,.0 51P&.&*6,- *7.18 !# = ! "9! #9: & ;,/*- *7.1 -*0.)1 ,2 P//.41,.0 51P&.&.<,- *7.18 ω" = #=:>:%%9 ⋅%? 9 -*0@1 A<B)/*- CP/,a.+E ,2 +cP '*-+c " = ?=?A%A 'aaP<+-.a.+E ,2 P//.41,.0 2.3 从ECEF坐标求经度/纬度（续） WGS-84 世界大地测量系统（1984）。其定义及与地方大地测量系统的关系。DMA TR 8350.2，第2版，美国弗吉尼亚州费尔法克斯，国防测绘局.

---

## Page 65

33 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.3 Longitude/Latitude from ECEF Coordinates (cont.) Hofmann-Wellenhof, B., H. Lichtenegger and J. Collins (1994). Global Positioning System: Theory and Practice. 3rd ed. Springer Verlag. New York, NY.

---

## Page 66

33 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 2.3 从ECEF坐标求经度/纬度（续） 霍夫曼-韦伦霍夫，B.，H. 利希滕格格和 J. 柯林斯（1994）。全球定位系统：理论与实践。第3版。施普林格出版社。纽约，纽约州。

---

## Page 67

34 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) The transformation from                     for given heights h to is given by (Heiskanen and Moritz 1967) !"= #!μ 2.3 ECEF Coordinates from Longitude/Latitude Heiskanen, W. A. and H. Moritz (1967). Physical Geodesy. Freeman. London.

---

## Page 68

34 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 从给定高度 h 的转换到 由 (Heiskanen 和 Moritz 1967) 给出  !"! !#! μ"" 2.3 从经纬度到地心地固坐标 Heiskanen, W. A. and H. Moritz (1967). Physical Geodesy. Freeman. London.

---

## Page 69

35 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.3 ECEF Coordinates from Longitude/Latitude (cont.)

---

## Page 70

35 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.3 从经纬度到地心地固坐标（续）

---

## Page 71

36 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.4 Transformations between ECEF and Flat-Earth Coordinates For local flat-Earth navigation it can be assumed that the NED tangent plane is fixed on the surface of the Earth Assume that the NED tangent plane is located at l0 and μ0 such that The ECEF coordinates satisfy the differential equation Flat Earth is a good approximation for  ships and floating structures  operating in a limited region. Flat Earth is a bad approximation for global waypoint tracking control systems for marine craft since (l, μ) will vary largely for vessels in transit between the different continents.

---

## Page 72

36 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.4 ECEF 与平地坐标之间的变换 对于本地平面地球导航，可以假设NED切平面固定在地球表面 假设 NED 切平面位于 l0 和 μ0，使得 ECEF 坐标满足微分方程 平面地球是对在有限区域内运行的船舶和漂浮结构的一个良好近似。 平面地球是海洋船舶全球航点跟踪控制系统的一个不良近似，因为 (l, μ) 在船舶穿越不同大陆之间时会有 很大变化。

---

## Page 73

37 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Given a local NED position                      with coordinate origin (l0, μ0) and reference height href in meters above the surface of the Earth, the change in longitude and latitude is (Equation 2.39, Farrell 2008) 2.4 Longitude, Latitude and Height from Flat-Earth Coordinates ssa is the smallest signed angle confining the argument to the interval [−π, π)

---

## Page 74

37 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 给定一个局部NED位置，其坐标原点为(l0, μ0)，参考高度为h ref米（地球表面以上），经度和纬度的变化为（方程2.39，F arrell 2008） 2.4 平面地球上的经度、纬度和高度 坐标 ssa 是将幅角限制在区间 [−π, π) 内的最 小带符号角

---

## Page 75

38 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Smallest Signed Angle: Smallest Difference Between Two Angles

---

## Page 76

三十八 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 最小有符号角：两个角之间的最小差

---

## Page 77

39 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.4 Flat-Earth Coordinates from Longitude, Latitude and Height The NED positions (xn,yn,zn) with respect to a flat-Earth coordinate system with origin (l0 , μ0 ) and reference height href are computed as (Equation 2.39, Farrell 2008)

---

## Page 78

三十九 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.4 从经度、纬度和高度计算平面地球坐标 相对于以原点 (l0, μ0) 和参考高度 href 的平地坐标系，NED 位置 (xn, yn, zn) 的计算公式为（方程 2.39，Farrell 20 08）

---

## Page 79

40 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) • 4 0 2.5 Recap: North-East-Down (NED) Differential Equations Euler Angle Rotation Matrix Representation The ZXZ sequence is the proper Euler angle rotation sequence used in robotics, but for aircraft and spacecraft, we use the Tait– Bryan ZYX sequence (yaw-pitch-roll), so that the singularity occurs at ±90 degrees in pitch.

---

## Page 80

40 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） • 4 0 2.5 回顾：东北-下 (NED) 微分方程 欧拉角旋转矩阵表示 The ZXZ sequence is the proper Euler angle rotation sequence used in robotics, but for aircraft and spacecraft, we use the Tait– Bryan ZYX sequence (yaw-pitch-roll), so that the singularity occurs at ±90 degrees in pitch.

---

## Page 81

41 Lecture Notes TK 8109 Advanced Guidance, Navigation and Control (T. I. Fossen) These equations can be expressed in amplitude-phase form Amplitude (speed): Phase (horizontal crab angle): Proof: 2.5 Two-Dimensional Amplitude-Phase Form Course angle = Heading (yaw) angle + Horizontal Crab angle We want to prove the famous relationship (from the figure) Horizontal crab angle

---

## Page 82

41 Lecture Notes TK 8109 Advanced Guidance, Navigation and Control (T. I. Fossen) These equations can be expressed in amplitude-phase form Amplitude (speed): Phase (horizontal crab angle): Proof: 2.5 Two-Dimensional Amplitude-Phase Form Course angle = Heading (yaw) angle + Horizontal Crab angle We want to prove the famous relationship (from the figure) Horizontal crab angle

---

## Page 83

42 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) The relationship between the course angle, heading angle and crab angle is important for maneuvering of a vehicle in the horizontal plane. The terms course and heading are used interchangeably in much of the literature on guidance, navigation and control and this leads to confusion. • Course angle χ The course angle c of a vehicle is the cardinal direction in which the vehicle is moving. Measured using GNSS (or HPR under water) • Heading (yaw) angle ψ The heading angle y, is the direction the craft’s bow (xb axis) is pointed. Measured using a compass • Horizontal crab angle βc Inspection of the figure confirms that the crab angle is the difference between the course angle and the heading angle: 2.5 Definitions of Course, Heading and Crab Angles North East

---

## Page 84

四十二 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 航向角、航迹角和偏航角之间的关系对于在水平面上操纵车辆非常重要。 在大量关于制导、导航和控制的文献中，术语“航向”和“方位”常被互换使用，这造成了混淆。 • 航向角 χ 航向角 c  指车辆移动的基 本方向。使用全球导航卫星系统（G NSS）（或水下的HPR）测量 • 航向（偏航）角 ψ 航向角 y  是飞行器 船首（xb 轴）指向的方向。使用指南 针测量 • 水平侧滑角 βc 对图形的检查确认，侧 滑角是航向角与船首方向角之间的差值 ： 2.5 航向、航迹和偏航角的定义 North 东

---

## Page 85

43 Lecture Notes TK 8109 Advanced Guidance, Navigation and Control (T. I. Fossen) 2.5 Horizontal Crab Angle due to Crosswind Component https://aviation.stackexchange.com/questions/58861/what-is-the-maximum-angle-between-an-airplane-and-runway-centerline-when-touchin A B777 (as in the photo) would generally have a maximum crab angle of about 16 degrees when approaching and landing at the maximum demonstrated crosswind component of 38 knots. A marine craft exposed to wind, waves and ocean currents will also have a non- zero horizontal crab angle. The physical observed angle is the horizontal crab angle bc and not the sideslip angle b

---

## Page 86

43 讲义 TK 8109 高级制导、导航与控制（T. I. Fossen） 2.5 由侧风分量引起的水平横摇角 https://aviation.stackexchange.com/questions/58861/飞机着陆时与跑道中心线之间的最大角度是多少 一架 B777（如照片所示）在接近并降落于最大示范横风分量为 38 节的情况下，通常的最大横滑角约为 1 6 度。 受到风、浪和洋流影响的海上船只也 会有非零的水平偏转角。 物理观测角是水平偏航角 bc，而不是侧滑角 b

---

## Page 87

44 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) For a marine craft exposed to ocean currents, the concept of relative velocities is introduced. The relative velocities are where uc, vc and wc are the  current velocities and is the ocean current speed. !" = #"! + $"! + %"! " 2.5 Extensions to Ocean Currents: Angle of Attack (AOA) and Sideslip Angle (SSA) Relative speed AOA and SSA AOA and SSA are primarily used to access lift and drag coefficients from wind tunnel data but can also be utilized in control system design.

---

## Page 88

44 讲义：海洋船舶水动力学与运动控制（T. I. Fossen） 对于暴露在洋流中的海上船舶，引入了相对速度的概念。 相对速度是 其中 uc、vc 和 wc 是当前速度，并且 是海流速度。 !" ! #"! " $"! " %"! ""#"""" 2.5 海洋洋流的扩展：攻角（AOA）和侧滑角（ SSA） 相对速度 AOA 和 SSA AOA 和 SSA 主要用于从风洞数据中获取升力和阻 力系数，但也可用于控制系统设计。

---

## Page 89

45 2.5 Horizontal Crab Angle versus Sideslip Angle In the literature, the term “sideslip angle” is often used for the “horizontal crab angle” while we explicitly distinguish between the angles. The sideslip angle is used to compute the aero-/hydrodynamic coefficients (wind tunnel look-up tables), while the horizontal crab angle enters the LOS guidance law Aircraft operate in the wind, while marine craft can be exposed to ocean currents, waves, and wind. The aerodynamic and hydrodynamic forces are functions of the relative velocity velocities: The subscript f denotes the flow due to wind, waves, and/or ocean currents Lift will be perpendicular and drag will be parallel to the relative flow. The 2-D linear relative velocities can be expressed as: Note that horizontal crab angle is equal to the sideslip angle when Sideslip angle • Horizontal Crab angle is the angle between the direction c the vehicle it is moving due to external forces such as ocean currents, waves or winds and the heading y of the vehicle satisfying • Sideslip angle is the the angle between the xb-axis of the vehicle and the direction of the flow velocity.

---

## Page 90

45 2.5 水平侧滑角与横向偏航角 在文献中，术语“侧滑角”通常用于表示“水平偏航角”，而我们明确区分这两个角度。侧滑角用于计算空气动力/水动力系数 （风洞查表），而水平偏航角则用于视线指导律。 飞机在风中运行，而船舶可能会受到洋流、波浪和风的影响。空气动力和水动力的作用力是相对速度的函数： The subscript f denotes the flow due to wind, waves, and/or ocean currents 升力将垂直于相对流，而阻力将平行于相对流。二维线性相对速度可以表示为： 注意，当侧滑角存在时，水平螃蟹角等 于侧滑角 • 水平螃蟹角是指车辆由于外部力（如洋流、海浪或风）影响而移动的方向 c 与车辆航向 y 之间的角度，满 足 • 侧滑角是车辆 xb 轴与流速方向之间的角度。

---

## Page 91

46 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.5 Three-Dimensional Amplitude-Phase Representation The course angle χ and the flight-path angle 𝜸can describe the NED velocity vector in 3-D space NED kinematic differential equations Rotating the speed vector [U, 0, 0] about the y and z axes and using the horizontal speed                                yields Coates, E. M. and T. I. Fossen (2025). A Spherical Amplitude-Phase Formulation for 3-D Adaptive Line-of-Sight (ALOS) Guidance with USGES Stability Guarantees. Submitted to Automatica. Open Access: arxiv.org/abs/2505.08344

---

## Page 92

46 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.5 三维幅度-相位表示 航向角 χ 和飞行路径角 𝜸 可以描述 NED 速度向量在三维空间中的情况 端 NED运动学微分方程 旋转 关于 y 和 z 轴的速度向量 [U, 0, 0]  并使用水平速度 产量 Coates, E. M. 和 T. I. Fossen (2025)。用于三维自适应视线（ALOS）制导的球面振幅-相位公式及其 USGES 稳定性保证。已提交至《Automatica》。开放获取：arxiv .org/abs/2505.08344

---

## Page 93

47 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.5 Three-Dimensional Amplitude-Phase Representation Euler Angle Rotation Matrix Representation Spherical Amplitude-Phase Representation Control inputs: • Pitch angle, q • Yaw angle, y • Speed, U Course angle Flight-path angle Horizontal speed Vertical and horizontal crab angles Coates, E. M. and T. I. Fossen (2025). A Spherical Amplitude-Phase Formulation for 3-D Adaptive Line-of-Sight (ALOS) Guidance with USGES Stability Guarantees. Submitted to Automatica. Open Access: arxiv.org/abs/2505.08344

---

## Page 94

47 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 2.5 三维幅度-相位表示 欧拉角旋转矩阵表示 Spherical Amplitude-Phase Representation Control inputs: • Pitch angle, q • Yaw angle, y • Speed, U Course angle Flight-path angle Horizontal speed Vertical and horizontal crab angles Coates, E. M. and T. I. Fossen (2025). A Spherical Amplitude-Phase Formulation for 3-D Adaptive Line-of-Sight (ALOS) Guidance with USGES Stability Guarantees. Submitted to Automatica. Open Access: arxiv.org/abs/2505.08344

---

## Page 95

48 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) FLOW axes are often used to express hydrodynamic data. The FLOW axes are found by rotating the BODY axis system such that resulting x-axis is parallel to the freestream flow. In FLOW axes, the x-axis directly points into the relative flow while the z-axis remains in the reference plane but rotates so that it remains perpendicular to the x-axis. The y-axis completes the right-handed system. !" α -β !#$%" &" '" ( !)*+, 2.5 Transformation between BODY and FLOW

---

## Page 96

48 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) FLOW 轴通常用于表示流体动力学数据。通过旋转 BODY 轴系统找到 FLOW 轴，使得得 到的 x 轴与自由流方向平行。 在FLOW坐标轴中，x轴直接指向相对流动方向，而z轴保持在参考平面内，但会旋转以保持 与x轴垂直。y轴则完成右手坐标系。 !" α -β !#$%" &" '" ( !)*+, 2.5 BODY 与 FLOW 之间的转换

---

## Page 97

49 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) !" α -β !#$%" &" '" ( !)*+, ! = "! + #! " Principal rotations: Velocity transformation: 2.5 Rotation Matrix between BODY and FLOW

---

## Page 98

49 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) !" α -β !#$%" &" '" ( !)*+, ! = "! + #! ""#""" 主旋转： 速度变换： 2.5 BODY与FLOW之间的旋转矩阵

---

## Page 99

50 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) !" α -β !#$%" &" '" ( !)*+, 2.5 Relative Velocities as a Function of AOA, SSA and Speed Relative velocities in component form AOA and SSA

---

## Page 100

50 讲义：海洋船舶流体力学与运动控制（T. I. Fossen） !" α -β !#$%" &" '" ( !)*+, 2.5 相对速度作为攻角、SSA 和速度的函数 分量形式的相对速度 AOA 和 SSA

---

## Page 101

51 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) Chapter Goals - Revisited • Understand the geographic reference frame NED, the Earth-centered reference frame ECEF and the body-fixed reference frame BODY. • Understand what FLOW axes are and why we use these axes for marine craft and aircraft • Be able to write down the differential equations relating BODY velocities to NED positions, both for Euler angles and unit quaternions. • Be able to: • Transform ECEF (xe, ye, ze) positions to (longitude, latitude, height) and vice versa • Transform (longitude, latitude, height) to flat-Earth positions (xn, yn, zn) and vice versa • Define, visualize, and explain the use of: • Angle of attack a • Sideslip angle b • Vertical crab angle ac • Horizontal crab angle bc • Heading angle y • Course angle c

---

## Page 102

51 Lecture Notes: Marine Craft Hydrodynamics and Motion Control  (T. I. Fossen) 章节目标 - 再访 • 理解地理坐标系NED、地心坐标系ECEF以及机体固定坐标系BODY。 • 了解什么是FLOW轴以及为什么我们在海上船舶和飞机上使用这些轴 • 能够写出将机体速度与NED位置相关联的微分方程，包括欧拉角和单位四元数的情 况。 • 能够： • 将 ECEF (xe, ye, ze) 位置转换为（经度，纬度，高度），反之亦然 • 将（经度, 纬度, 高度）转换为平面地球坐标（xn, yn, zn），反之亦然 • 定义、可视化并解释以下的用途： • 攻角 a • 侧滑角 b • 垂直螃蟹角 ac • 水平螃蟹角 bc • 航向角 y • 航向角 c

---
