# 04_REMUS水下航行器六自由度仿真模型验证_Prestero2001 (中英双语对照精读版)

> **自动转换源文件**: `04_REMUS水下航行器六自由度仿真模型验证_Prestero2001`  
> **双语对照总页数**: 254 页  

---

## Page 1

Verification of a Six-Degree of Freedom Simulation Model for the REMUS Autonomous Underwater Vehicle by Timothy Prestero B.S., Mechanical Engineering University of California at Davis (1994) Submitted to the Joint Program in Applied Ocean Science and Engineering in partial fulfillment of the requirements for the degrees of Master of Science in Ocean Engineering and Master of Science in Mechanical Engineering at the MASSACHUSETTS INSTITUTE OF TECHNOLOGY and the WOODS HOLE OCEANOGRAPHIC INSTITUTION September 2001 @ 2001 Timothy Prestero. All rights reserved. The author hereby grants MIT and WHOI permission to reproduce paper and electronic copies of this thesis in whole or in part and to distribute them publicly. Author ....... ....... ..... .................... Joint Progra in Applied Ocean Science and Engineering August 2001 Certified by. Certified by......... ...... .. . Certified by ................ Jerome Milgram Professor of Ocean Engineering, MIT Thesis Supervisor .................... .... ... Kamal Youcef-Toumi Professor of Mechanical Engineering, MIT eebn~c 2-Q rvisor Christopher von Alt -ipal Engineer, WHOI Thesis Supervisor A ccepted by ................ .................... tael S. Triantafyllou Professor of Ocean Engineering, MIT/WHOI Chairman, Joint Committee for Applied Ocean ScjM4 Engineering Accepted by...........................................- MASSACHUSETTS iNSTITUTe OF TECHNOLOGY NOV 2 7 2001 LIBRARIES Ain A. Sonin Professor of Mechanical Engineering, MIT Chairperson, Committee on Graduate Students ARCHIVES

---

## Page 2

用于REMUS自主水下航行器六自由度仿真模型的验证 提摩西·普雷斯特罗 (Timothy Pres tero) 理学学士，机械工程，加利福尼亚大学戴维斯分校 (1994) 提交给联合应用海洋科学与工程项目，以部分满足在麻省理工 学院和伍兹霍尔海洋研究所获得海洋工程硕士与机械工程硕士 学位的要求 2001年9月 © 2001 提摩西·普雷斯特罗。版权所有。 作者在此授予麻省理工学院和伍兹霍尔海洋研究所许可，可全 部或部分复制本文论文及电子版本，并公开分发。 作者 ....... ....... ..... .................... 联合应用海洋科学与工程项目 A u g u s t  2001 认 证人。认证人......... ...... ..  . 认证人 ................ Jerome Milgram 麻省理工学院海 洋工程教授，论文指导 .................... ....  ... Kamal Youcef-Toumi 麻省理工学院 机械工程教授 eebn~c 2-Q 指导 Christopher von Alt -ipal 工程师，WHOI 论文指导 接受人 ................  .................... Stael S. Triantafyllou 麻省理工学院/WHOI 海洋 工程教授，联合应用海洋科学与工程委员会主席 被...........................................接收 - 麻省理工学院 2001年11月27 日 图书馆 Ain A. Sonin 麻省理工学院机械工程教授，研究生委 员会主席 档案

---

## Page 3

Verification of a Six-Degree of Freedom Simulation Model for the REMUS Autonomous Underwater Vehicle by Timothy Prestero Submitted to the Joint Program in Applied Ocean Science and Engineering on 10 August 2001, in partial fulfillment of the requirements for the degrees of Master of Science in Ocean Engineering and Master of Science in Mechanical Engineering Abstract Improving the performance of modular, low-cost autonomous underwater vehicles (AUVs) in such applications as long-range oceanographic survey, autonomous docking, and shallow-water mine coun- termeasures requires improving the vehicles' maneuvering precision and battery life. These goals can be achieved through the improvement of the vehicle control system. A vehicle dynamics model based on a combination of theory and empirical data would provide an efficient platform for vehi- cle control system development, and an alternative to the typical trial-and-error method of vehicle control system field tuning. As there exists no standard procedure for vehicle modeling in industry, the simulation of each vehicle system represents a new challenge. Developed by von Alt and associates at the Woods Hole Oceanographic Institute, the REMUS AUV is a small, low-cost platform serving in a range of oceanographic applications. This thesis describes the development and verification of a six degree of freedom, non-linear simulation model for the REMUS vehicle, the first such model for this platform. In this model, the external forces and moments resulting from hydrostatics, hydrodynamic lift and drag, added mass, and the control inputs of the vehicle propeller and fins are all defined in terms of vehicle coefficients. This thesis describes the derivation of these coefficients in detail. The equations determining the coefficients, as well as those describing the vehicle rigid-body dynamics, are left in non-linear form to better simulate the inherently non-linear behavior of the vehicle. Simulation of the vehicle motion is achieved through numeric integration of the equations of motion. The simulator output is then checked against vehicle dynamics data collected in experiments performed at sea. The simulator is shown to accurately model the motion of the vehicle. Thesis Supervisor: Jerome Milgram Title: Professor of Ocean Engineering, MIT Thesis Supervisor: Kamal Youcef-Toumi Title: Professor of Mechanical Engineering, MIT Thesis Supervisor: Christopher von Alt Title: Principal Engineer, WHOI

---

## Page 4

蒂莫西·普雷斯特罗对REMUS自主水下航行器六自由度仿真模型的验证 于2001年8月10日提交至应用海洋科学与工程联合项目，以部分完成海洋 工程硕士和机械工程硕士学位的要求 摘要 提高模块化、低成本自主水下航行器（AUV）在远程海洋调查、自主对接和浅水水雷防御等应 用中的性能，需要提升车辆的操纵精度和电池寿命。这些目标可以通过改进车辆控制系统来实 现。基于理论与实证数据结合的车辆动力学模型将为车辆控制系统开发提供高效的平台，并为 传统的车辆控制系统现场调试的试错方法提供替代方案。由于工业界尚无车辆建模的标准程序 ，每个车辆系统的仿真都代表了新的挑战。 由沃尔夫·奥尔特及伍兹霍尔海洋研究所的同事开发，REMUS AUV 是一种小型、低成本平 台，可用于多种海洋学应用。本论文描述了 REMUS 车辆六自由度非线性仿真模型的开发与验 证，这是该平台的首个此类模型。在该模型中，由静水力、流体动力升力和阻力、附加质量， 以及车辆螺旋桨和舵控制输入产生的外力和力矩，均以车辆系数表示。本论文详细描述了这些 系数的推导。这些确定系数的方程，以及描述车辆刚体动力学的方程，保持非线性形式，以更 好地模拟车辆固有的非线性行为。车辆运动的仿真是 论文导师：杰罗姆·米尔格拉姆 职称：麻 省理工学院海洋工程教授 Thesis Supervisor: Kamal Youcef-Toumi Title: Professor of Mechanical Engineering, MIT Thesis Supervisor: Christopher von Alt Title: Principal Engineer, WHOI

---

## Page 5

Candide had been wounded by some splinters of stone; he was stretched out in the street and covered with debris. He said to Pangloss: "Alas, get me a little wine and oil, I am dying." "This earthquake is not a new thing," replied Pangloss. "The town of Lima suffered the same shocks in America last year; same causes, same effects; there is certainly a vein of sulfur underground from Lima to Lisbon." "Nothing is more probable," said Candide, "but for the love of God, a little oil and wine." "What do you mean, probable?" replied the philosopher. "I maintain that the matter is proved." Candide lost consciousness. -Candide, Voltaire Did I possess all the knowledge in the world, but had no love, how would this help me before God, who will judge me by my deeds? -The Imitation of Christ, Thomas d Kempis

---

## Page 6

Candide had been wounded by some splinters of stone; he was stretched out in the street and covered with debris. He said to Pangloss: "Alas, get me a little wine and oil, I am dying." "This earthquake is not a new thing," replied Pangloss. "The town of Lima suffered the same shocks in America last year; same causes, same effects; there is certainly a vein of sulfur underground from Lima to Lisbon." "Nothing is more probable," said Candide, "but for the love of God, a little oil and wine." "What do you mean, probable?" replied the philosopher. "I m aintain that the matter is proved." Candide lost consciousness. -《老实人》，Voltaire Did I possess all the knowledge in the world, but had no love, how would this help me before God, who will judge me by my deeds? -《效法基督》，Thomas d Kempis

---

## Page 7

Acknowledgments If not for the assistance and support of the following people, this work would have been much more difficult, if not impossible to accomplish. At MIT, I would first like to thank my advisor Prof. Jerry Milgram, for giving me a chance, for helping me to get started on such an interesting problem, and for allowing me the room to figure things out on my own. I would like to thank Prof. Kamal Youcef-Toumi for agreeing to read this thesis on top of what was already a very busy schedule. I would like to thank Prof. John Leonard for his humanity and his excellent advice. And finally, I have to thank the department administrators, Beth Tuths and Jean Sucharewicz, for their unfailing patience and courtesy in answering about a million emails from Africa. At Woods Hole, I would like to thank Chris von Alt for his sage advice, and for his patience as I figured out how to assemble this Heath Kit. I would like to thank Ben Allen for not telling anyone that I dropped the digital camera into the tow tank. I would like to thank Roger Stokey, Tom Austin, Ned Forrester, Mike Purcell and Greg Packard for all of their help with the vehicle experiments, and for swatting their share of the green flies in Tuckerton. I would like to thank Marga McElroy for helping me navigate the WHOI bureaucracy, and I have to thank Butch Grant for inducting me into the mysteries of the circuit board and soldering iron. I would like to thank Nuno Cruz for the excellent discussions about experimental methods, Oscar Pizarro, Chris Roman, and Fabian Tapia for solving the world's problems over dinner, and Tom Fulton and Chris Cassidy for the water-skiing lessons. And wherever he is now in Brooklyn, I have to thank Alexander Terry for that first kick in the pants. At home, I have to thank my family for their confidence and constant support, and Sheridan for first giving me the good news. And finally, I would like to thank Elizabeth for absolutely everything. TIMOTHY PRESTERO Cambridge, Massachusetts

---

## Page 8

致谢 如果没有以下人员的帮助和支持，本工作将会更加困难，甚至可能无法完成。 在麻省理工学院，我首先要感谢我的导师 Jerry Milgram 教授，感谢他给我机会，帮助我开始研究这样 一个有趣的问题，并允许我有空间自己去探索。我还要感谢 Kamal Youcef-Toumi 教授，在本已非常繁忙 的日程中，还同意阅读这篇论文。我想感谢 John Leonard 教授，他的人性关怀和出色的建议对我帮助很大 。最后，我必须感谢系里的行政人员 Beth Tuths 和 Jean Sucharewicz，感谢她们在回复来自非洲的将近一 百万封电子邮件时表现出的不懈耐心和礼貌。 在伍兹霍尔，我想感谢克里斯·冯·奥特给予的睿智建议，以及在我弄清楚如何组装这个Heath Kit时的耐 心。我想感谢本·艾伦没有告诉任何人我把数码相机掉进了拖曳水槽。我想感谢罗杰·斯托基、汤姆·奥斯汀 、内德·福雷斯特、迈克·珀塞尔和格雷格·帕卡德在车辆实验中提供的所有帮助，并感谢他们在塔克顿帮助 消灭绿蝇。我想感谢玛尔加·麦凯尔罗伊帮我应对WHOI的官僚程序，我还必须感谢巴奇·格兰特让我了解 电路板和焊锡的奥秘。 我想感谢努诺·克鲁兹（Nuno Cruz）就实验方法进行的出色讨论，奥斯卡·皮扎罗（Oscar Pizarro）、克 里斯·罗曼（Chris Roman）和法比安·塔皮亚（Fabian Tapia）在晚餐时一起解决世界问题，汤姆·富尔顿（T om Fulton）和克里斯·卡西迪（Chris Cassidy）提供的滑水课程。无论他现在身处布鲁克林的何处，我还要 感谢亚历山大·特里（Alexander Terry）给我的那一次象征性的激励。 在家里，我必须感谢我的家人对我的信任和持续的支持，也要感谢谢里丹首先告诉我这个好消息。最 后，我想感谢伊丽莎白为一切所做的一切。 提摩太·普雷斯特罗 Cambridge, Massachusetts

---

## Page 9

Contents 1 Introduction 12 1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 1.2 Vehicle Model Development . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 1.3 Research Platform . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 1.4 Model Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 1.5 Modeling Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 1.5.1 Environmental Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 1.5.2 Vehicle/Dynamics Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . 13 2 The REMUS Autonomous Underwater Vehicle 14 2.1 Vehicle Profile . . . . . . . . . . . . . ... . . . . . . . . . . . . . . . . . . . . . . . . . 14 2.2 Sonar Transducer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 2.3 Control Fins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 2.4 Vehicle W eight and Buoyancy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 2.5 Centers of Buoyancy and Gravity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 2.6 Inertia Tensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 2.7 Final Vehicle Profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 3 Elements of the Governing Equations 20 3.1 Body-Fixed Vehicle Coordinate System Origin . . . . . . . . . . . . . . . . . . . . . 20 3.2 Vehicle Kinematics......... ... ... ........... . . . . . . . . . .. 20 3.3 Vehicle Rigid-Body Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 3.4 Vehicle Mechanics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 4 Coefficient Derivation 24 4.1 Hydrostatics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 4.2 Hydrodynamic Damping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 4.2.1 Axial Drag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 4.2.2 Crossflow Drag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 4.2.3 Rolling Drag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 4.3 Added Mass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 4.3.1 Axial Added Mass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 4.3.2 Crossflow Added Mass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28 4.3.3 Rolling Added Mass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 4.3.4 Added Mass Cross-terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 4.4 Body Lift . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 4.4.1 Body Lift Force . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30 4.4.2 Body Lift Moment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31 4.5 Fin Lift . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31 4.6 Propulsion Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33 4.6.1 Propeller Thrust . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33 4.6.2 Propeller Torque . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33 4.7 Combined Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

---

## Page 10

内容 1 介绍 12 1.1  动机  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 1.2  车辆模型开发  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 1.3  研究平台  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 1.4 模型代码  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 1.5  建模假设  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 1.5.1  环境假设  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 1.5.2  车 辆/动力学假设  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 2 REMUS自主水下航行器 十四 2.1  车辆概况  . . . . . . . . . . . . . ...  . . . . . . . . . . . . . . . . . . . . . . . . . 14 2.2  声纳换能器  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 2.3  控制鳍  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 2.4  车辆重量与浮力  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 2.5  浮心与重心  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 2.6  惯性张量  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 2.7  最终车辆概况  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 控制方程的三个要素 20 3.1  车身固定坐标系原点 . . . . . . . . . . . . . . . . . . . . . 20 3.2  车辆运动学 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 3.3  车辆刚体动力学 . . . . . . . . . . . . . . . . . . . . . . . . . . 22 3.4  车辆力学 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 4 系数 推导 24 4.1 静水学 .................................................. 24 4.2 流体动力阻尼 ......................................... 25 4.2.1  轴向阻力 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 4.2.2  横向流阻力 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 4.2.3  滚动阻力 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 4.3 添加质量 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 4.3.1  轴向附加质量 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 4.3.2  横向流附加质量 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28 4.3.3  滚动附加质量 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 9 4.3.4  附加质量交叉项 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 4.4  机体升力 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 4.4.1  机体升力作用力 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 0 4.4.2  机体升力力矩 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31 4.5  鳍升力 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31 4.6  推进模型 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 3 4.6.1  螺旋桨推力 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33 4.6.2  螺旋桨

---

## Page 11

4.8 Total Vehicle Forces and Moments . . . . 5 Vehicle Tow Tank Experiments 5.1 M otivation . . . . . . . . . . . . . . . . . 5.2 Laboratory Facilities and Equipment . . . 5.2.1 Flexural Mount . . . . . . . . . . . 5.2.2 Tow Tank Carriage . . . . . . . . . 5.3 Drag Test Experimental Procedure . . . . 5.3.1 Instrument Calibration . . . . . . 5.3.2 Drag Runs . . . . . . . . . . . . . 5.3.3 Signal Processing . . . . . . . . . . 5.4 Experimental Results . . . . . . . . . . . . 5.5 Component-Based Drag Model . . . . . . 6 Vehicle Simulation 6.1 Combined Nonlinear Equations of Motion 6.2 Numerical Integration of the Equations of 6.2.1 Euler's Method . . . . . . . . . . . 6.2.2 Improved Euler's Method . . . . . 6.2.3 Runge-Kutta Method ....... 6.3 Computer Simulation . ........... 7 Field Experiments 7.1 Motivation. ................. 7.2 Measured States . . . . . . . . . . . . . . 7.3 Vehicle Sensors . . . . . . . . . . . . . . . 7.3.1 Heading: Magnetic Compass . . . 7.3.2 Yaw Rate: Tuning Fork Gyro . . . 7.3.3 Attitude: Tilt Sensor . . . . . . . . 7.3.4 Depth: Pressure Sensor . . . . . . 7.4 Experimental Procedure........... 7.4.1 Pre-launch Check List . . . . . . . 7.4.2 Trim and Ballast Check . . . . . . 7.4.3 Vehicle Mission Programming . . . 7.4.4 Compass Calibration . . . . . . . . 7.4.5 Vehicle Tracking . . . . . . . . . . 7.5 Experimental Results ............. 7.5.1 Horizontal-Plane Dynamics . . . . 7.5.2 Vertical-Plane Dynamics...... 8 Comparisons of Simulator Output and 8.1 Model Preparation............ 8.1.1 Initial Conditions......... 8.1.2 Coefficient Adjustments . 8.2 Uncertainties in Model Comparison . 8.3 Horizontal Plane Dynamics...... 8.4 Vertical Plane Dynamics . . . . . . . . 8.4.1 Vehicle Pitching Up . . . . . . 8.4.2 Vehicle Pitching Down . . . . . Experimental . . . . . 33 36 . . . . . 36 . . . . . 36 . . . . . 37 . . . . . 37 . . . . . 37 . . . . . 40 . . . . . 41 . . . . . 41 . . . . . 42 . . . . . 42 44 . . . . . 44 45 . . . . . 46 . . . . . 46 . . . . . 46 . . . . . 47 Motion Data '-4

---

## Page 12

4.8 总车辆力和力矩 5  车辆  拖车  坦克  实验 5.1 动机 . . . . . . . . . . . . . . . . . 5.2 实验室设施与设备 . . . 5.2.1 弯曲安装 . . . . . . . . . . . 5.2.2 拖曳水槽运载装置 . . . . . . . . . 5.3 阻力测试 实验程序 ...... 5.3.1 仪器校准 ...... 5.3.2 阻力运行 ............... 5.3.3 信号处理 .............. 5.4 实验 结果 ...................... 5.5 基于组件的阻力模型 ...... 6  车辆模拟 6.1  联合非线性运动方程 6.2  方程的数值积分 6.2.1 欧拉方法 . . . . . . . . . . . 6.2.2  改进的欧拉方法 . . . . . 6.2.3  龙格-库塔方法 ....... 6.3  计算机仿真 . ........... 7  田野实验 7.1 动机 .................. 7.2 测量状态 .................. 7.3 车 辆传感器 .................. 7.3.1 航向：磁罗盘 .................. 7.3.2 偏航率：音叉陀螺仪 .................. 7.3.3 姿态： 倾斜传感器 .................. 7.3.4 深度：压力传感器 ...... ............ 7.4 实验步骤 ........... 7.4.1 发射前检查清单 . . . . . . . 7.4.2 修整和压 载检查 . . . . . . 7.4.3 车辆任务编程 . . . 7.4.4 指 南针校准 . . . . . . . . 7.4.5 车辆跟踪 . . . . . . . . . . 7.5 实验结果 ............. 7.5.1 水平平面动力学 . . . . 7.5.2 垂直平面动力 学...... 8 模拟器输出的比较和 8.1 模型准备............ 8.1.1 初始条件......... 8.1.2 系数调整 . 8.2 模型比较中的不确定性 . 8.3 水平 面动力学...... 8.4 垂直面动力学 . . . . . . . . 8.4.1 车辆上仰 . . . . . . 8.4.2 车辆下俯 . . . . . 实验性的 . . . . . 33 三十六 . . . . . 36 . . . . . 36 . . . . . 37 . . . . . 37 . . . . . 37 . . . . . 40 . . . . . 41 . . . . . 41 . . . . . 4 2 . . . . . 42 四十四 . . . . . 4445 . . . . . 46 . . . . . 46 . . . . . 46 . . . . . 47 运动 数据 -4

---

## Page 13

9 Linearized Depth Plane Model and Controller 77 9.1 Linearizing the Vehicle Equations of Motion . . . . . . . . . . . . . . . . . . . . . . . 77 9.1.1 Vehicle Kinematics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77 9.1.2 Vehicle Rigid-Body Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 9.1.3 Vehicle Mechanics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 9.2 Linearized Coefficient Derivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79 9.2.1 H ydrostatics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79 9.2.2 A xial D rag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79 9.2.3 Crossflow D rag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79 9.2.4 A dded M ass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80 9.2.5 Body Lift Force and Moment . . . . . . . . . . . . . . . . . . . . . . . . . . . 81 9.2.6 F in Lift . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81 9.2.7 Combined Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82 9.2.8 Linearized Coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82 9.3 Linearized Equations of Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82 9.3.1 Equations of Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83 9.3.2 Four-term State Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84 9.3.3 Three-term State Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 9.4 Control System Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 9.4.1 Vehicle Transfer Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 9.4.2 Control Law . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86 9.4.3 Controller Design Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . 87 9.4.4 Pitch Loop Controller Gains . . . . . . . . . . . . . . . . . . . . . . . . . . . 87 9.4.5 Depth Loop Controller Gains . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 9.5 Real-World Phenomena . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 9.6 Controller Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 10 Conclusion 98 10.1 Expanded Tow Tank Measurements . . . . . . . . . . . . . . . . . . . . . . . . . . . 98 10.2 Future Experiments at Sea . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98 10.2.1 Improved Vehicle Instrumentation . . . . . . . . . . . . . . . . . . . . . . . . 99 10.2.2 Measurement of Vehicle Parameters . . . . . . . . . . . . . . . . . . . . . . . 99 10.2.3 Isolation of Vehicle Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 10.3 Controller-Based Model Comparison . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 10.4 Vehicle Sensor Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 10.5 Improved Coefficient-Based Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100 A Tables of Parameters 101 B Tables of Combined Non-Linear Coefficients 103 C Tables of Non-Linear Coefficients by Type 105 D Tables of Linearized Model Parameters 111 E MATLAB Code 113 E.1 Vehicle Simulation........ ... ... ... ... ......... . . . . . . .. 113 E.1.1 REMUSSIM.m . . . . . . ... ... .... ... ............... 113 E .1.2 REM U S.m . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116 F Example REMUS Mission File 119 F.1 REMUS Mission Code................ . . . . . . . . . . . . . . . . . . 119

---

## Page 14

9  线性化深度平面模型与控制器 77 9.1  车辆运动方程的线性化 . . . . . . . . . . . . . . . . . . . . . . . 77 9.1.1  车辆运动学 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77 9.1.2  车辆刚体动力学 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 9.1.3  车辆力学 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 9.2  线性化系数推导 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79 9.2.1  静水力学 .................................................. 79 9.2.2  轴向阻力 .......................................... ........ 79 9.2.3  横流阻力 .................................................. 79 9.2.4  附加质量 ............................ ...................... 80 9.2.5  机体升力和力矩 .......................................... 81 9.2.6  鳍升力 .............. .................................... 81 9.2.7  组合项 .................................................. 82 9.2.8  线性化系数 .................................................. 82 9.3  线性化运动方程 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82 9.3.1 运动方程 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83 9.3.2 四项状态向量 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84 9.3.3 三项状态向量 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 9.4 控制系统设计 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 9.4.1 车辆传递函数 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 9.4.2 控制定律 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86 9.4.3 控制器设计程序 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87 9.4.4 俯仰回路控制器增益 . . . . . . . . . . . . . . . . . . . . . . . . . . . 87 9.4.5 深度回路控制器增益 . . . . . . . . . . . . . . . . . . . . . . . . . . 88 9.5  现实世界现象 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 9.6  控制器实现 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 10  结论  98 10.1 扩展拖曳水箱测量 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98 10.2 海上未来实验 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98 10.2.1 改进的车辆仪器 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 10.2.2 车辆参数测量 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 10.2.3 车辆运动隔离 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 10.3 基于控制器的模型比较 . . . . . . . . . . . . . . . . . . . . . . . . . . 99 10.4 车辆传感器模型 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 10.5 改进的基于系数的模型 . . . . . . . . . . . . . . . . . . . . . . . . . . 100 A 参数表 101 B 组合非线性系数表 103 C 按类型的非线性系数表 105 D  线性化模型参数表 111 E MATLAB 代码 113 E.1  车辆仿真........  ...  ...  ...  ...  .........  . . . . . . . . 113 E.1.1  REMUSSIM.m  . . . . . . ....  ...  ....  ...  . ..............  113 E.1.2  REM U S.m  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116 F 示例 REMUS 任务 文件 119 F.1  REMUS  任务 代码................  . . . . . . . . . . . . . . . . . .. 119

---

## Page 15

List of Figures M yring P rofile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 REMUS Low-Frequency Sonar Transducer (XZ-plane)........ . . . . . . ... 16 REMUS Tail Fins (XY- and XZ-plane)................... . . . . . .. 16 STD REMUS Profile (XZ-plane) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 The REMUS Autonomous Underwater Vehicle.................. . .. 19 3-1 REMUS Body-Fixed and Inertial Coordinate Systems . . . 4-1 Effective Rudder Angle of Attack . . . . . . . . . . . . . . . 4-2 Effective Stern Plane Angle of Attack . . . . . . . . . . . . URI Tow Tank Layout . . . . . . . . . . . . . . . . . . . URI Tow Tank . . . . . . . . . . . . . . . . . . . . . . . Carriage Setup and Vehicle Mounting . . . . . . . . . . URI Tow Tank Carriage . . . . . . . . . . . . . . . . . . URI Tow Tank Carriage . . . . . . . . . . . . . . . . . . Unfiltered and Filtered Drag Data . . . . . . . . . . . . Forward Speed vs. Vehicle Axial and Lateral Drag . . . Vehicle Experiments at the Rutgers Marine Field Station REMUS Pre-Launch Checklist (Page One) . . . . . . . . REMUS Mission Data: Crash Plot . . . . . . . . . . . . Vehicle Experiments at WHOI . . . . . . . . . . . . . . The REMUS Ranger . . . . . . . . . . . . . . . . . . . . REMUS Mission Data: Closed-Loop Control . . . . . . REMUS Mission Data: Rudder . . . . . . . . . . . . . . REMUS Mission Data: Pitching Up . . . . . . . . . . . REMUS Mission Data: Pitching Down . . . . . . . . . . Horizontal Plane Simulation: Linear.......... Horizontal Plane Simulation: Angular . . . . . . . . . Horizontal Plane Simulation: Forces and Moments Horizontal Plane Simulation: Vehicle Trajectory . Horizontal Plane Simulation: Model Comparison . Vertical Plane Simulation: Vertical Plane Simulation: Vertical Plane Simulation: Vertical Plane Simulation: Vertical Plane Simulation: Vertical Plane Simulation: Vertical Plane Simulation: Vertical Plane Simulation: Vertical Plane Simulation: Vertical Plane Simulation: Linear . . . . . . . . . . . . Angular . . . . . . . . . . . Forces and Moments . . . . Vehicle Trajectory . . . . . Model Comparison . . . . . Linear . . . . . . . . . . . . Angular . . . . . . . . . . . Forces and Moments . . . . Vehicle Trajectory . . . . . Model Comparison . . . . . . . . . . . . . . . . . . . . . 3 7 . . . . . . . . . . . . . . . . 3 8 . . . . . . . . . . . . . . . . 3 9 . . . . . . . . . . . . . . . . 3 9 . . . . . . . . . . . . . . . . 4 0 . . . . . . . . . . . . . . . . 4 1 . . . . . . . . . . . . . . . . 4 2 . . . . . . . . . . . . . . . 4 8 . . . . . . . . . . . . . . . . 5 1 . . . . . . . . . . . . . . . . 5 3 . . . . . . . . . . . . . . . . 54 . . . . . . . . . . . . . . . . 5 4 . . . . . . . . . . . . . . . . 5 5 . . . . . . . . . . . . . . . . 56 . . . . . . . . . . . . . . . . 5 7 . . . . . . . . . . . . . . . . 58 5-1 5-2 5-3 5-4 5-5 5-6 5-7 7-1 7-2 7-3 7-4 7-5 7-6 7-7 7-8 7-9 8-1 8-2 8-3 8-4 8-5 8-6 8-7 8-8 8-9 8-10 8-11 8-12 8-13 8-14 8-15

---

## Page 16

图表列表 我的轮廓⋯⋯15 REMUS 低频声纳换能器（XZ 平面）⋯⋯16 REMUS 尾鳍（XY 平面 和 XZ 平面）⋯⋯16 标准 REMUS 轮廓（XZ 平面）⋯⋯19 REMUS 自主水下航行器⋯⋯19 3-1 REMUS 车体固定坐标系和惯性坐标系⋯⋯ 4-1 有效舵角攻角 . . . . . . . . . . . . . . . 4-2 有效尾舵面角攻角 . . . . . . . . . . . URI 拖曳水箱布局 . . . . . . . . . . . . . . . . . . URI 拖曳水箱 . . . . . . . . . . . . . . . . . . . . . . 运输架 设置和车辆安装 . . . . . . . . . . URI 拖曳水箱运输架 . . . . . . . . . . . . . . . . . . URI 拖曳水箱运输架 . . . . . . . . . . . . . . . . . . 未滤和滤波的阻力数据 . . . . . . . . . . . . 前进速度与车辆轴向和横向阻力 . . . 鲁格斯海洋实地站的车辆实验 REMUS 发射前检查表（第一页） . . . . . . . . REMUS 任务数据 ：撞击图 . . . . . . . . . . . . WHOI 的车辆实验 . . . . . . . . . . . . . . REMUS 游侠号 . . . . . . . . . . . . . . . . . . . . REMUS 任务数据：闭环控制 . . . . REMUS 任务数据：方向舵 . . . . . . . . . . . . REMUS 任 务数据：抬头俯仰 . . . . . . . . . . REMUS 任务数据：低头俯仰 . . . . . . . . . 水平平面模拟：

---

## Page 17

9-1 Perturbation Velocity Linearization . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80 9-2 Depth-Plane Control System Block Diagram . . . . . . . . . . . . . . . . . . . . . . . 86 9-3 Go Pole-Zero Plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89 9-4 Go Open-Loop Step Response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89 9-5 Go Root-Locus Plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90 9-6 Go Closed-Loop Step Response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90 9-7 GZ * Ho Pole-Zero Plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91 9-8 Gz * Ho Root-Locus Plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91 9-9 Gz * Ho Closed-Loop Step Response . . . . . . . . . . . . . . . . . . . . . . . . . . . 93 9-10 Modified Depth Plane Control System Block Diagram . . . . . . . . . . . . . . . . . 93 9-11 Vehicle Simulation: Case One . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94 9-12 Vehicle Simulation: Case Two . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95 9-13 Vehicle Simulation: Case Three . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96 9-14 Vehicle Simulation: Case Four . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97 10-1 Forces on the vehicle at an angle of attack . . . . . . . . . . . . . . . . . . . . . . . . 98 10-2 Vehicle performance limits as a function of depth and sea state...... . . . . .. 100

---

## Page 18

9-1 干扰速度线性化 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80 9-2 深度平面控制系统框图 . . . . . . . . . . . . . . . . . . . . . . . . 86 9-3 Go 极点零点图 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89 9-4 Go 开环阶跃响 应 . . . . . . . . . . . . . . . . . . . . . . . . . . . 89 9-5 Go 根轨迹图 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90 9-6 Go 闭环阶跃响应 . . . . . . . . . . . . . . . . . . . . . . . . . . . 90 9-7 GZ  * Ho  极点零点图 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91 9-8 Gz  * Ho  根轨迹图 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91 9-9 Gz  * Ho  闭环阶跃响应 . . . . . . . . . . . . . . . . . . . . . . . . . . . 93 9-10 改进的深度平面控制系统框图 . . . . . . . . 10-1 在迎角下作用于车辆的力 ........................................ 98 10-2 随深度和海况变化的车辆性能 极限 ......................... 100

---

## Page 19

List of Tables Myring Parameters for STD REMUS . . . REMUS Fin Parameters .......... STD REMUS Weight and Buoyancy STD REMUS Center of Buoyancy . STD REMUS Center of Gravity ...... STD REMUS Moments of Inertia . . . . . STD REMUS Hull Parameters . . . . . . Axial Added Mass Parameters a and 3 . . . . . . . . . . . . . STD REMUS Non-Linear Maneuvering Coefficients: Forces . . STD REMUS Non-Linear Maneuvering Coefficients: Moments 5.1 REMUS Drag Runs. . ... ............................ 5.2 REMUS Component-Based Drag Analysis - Standard Vehicle. ............. 5.3 REMUS Component-Based Drag Analysis - Sonar Vehicle. ............... 7.1 Vehicle Field Experiments . . . . . . . ........................ 8.1 REMUS Simulator Initial Conditions . . . ....................... 8.2 Vehicle Coefficient Adjustment Factors . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 Linearized Velocity Parameters. . .......................... 9.2 Combined Linearized Coefficients . . . ......................... 9.3 Linearized Maneuvering Coefficients. . ......................... 9.4 Percent Overshoot and Damping Ratio . . . . . . . . . . . . . . . . . . . . . . . . . . A.1 STD REMUS Hull Parameters....................... . . . . . .. A.2 Hull Coordinates for Limits of Integration................ .... . . .. A.3 STD REMUS Center of Buoyancy . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.4 STD REMUS Center of Gravity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.5 REMUS Fin Parameters.......... .......... ........ . . . . .. B.1 Non-Linear Force Coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B.2 Non-Linear Moment Coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.1 Axial D rag Coefficient . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.2 Crossflow Drag Coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.3 Rolling Resistance Coefficient . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.4 Body Lift and Moment Coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.5 Added M ass Coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.6 Added Mass Force Cross-term Coefficients . . . . . . . . . . . . . . . . . . . . . . . . C.7 Added Mass K-Moment Cross-term Coefficients . . . . . . . . . . . . . . . . . . . . . C.8 Added Mass M-, N-Moment Cross-term Coefficients . . . . . . . . . . . . . . . . . . C .9 P ropeller Term s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101 101 101 102 102 103 104 105 105 105 106 106 107 108 109 109 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

---

## Page 20

表格列表 Myring 参数用于 STD REMUS ...... REM US 鳍片参数 .......... STD REMUS 重量和 浮力 STD REMUS 浮心 . STD REMUS 重 心 ...... STD REMUS 惯性矩 ...... STD RE MUS 船体参数 ...... 轴向附加质量参数 a 和 3 . . . . . . . . . . . . STD REMUS 非线性操 纵系数：力 . . STD REMUS 非线性操纵系数：力矩 5.1  REMUS 阻力 运行 。。⋯⋯ ............................ 5.2  REMUS 基于组件的 阻力分析 - 标准车辆 。。。。。。。。。。 5.3  REMUS 基于组件的阻力 分析 - 声呐车辆 。。。。。。。。。。。。。。 7.1  车辆现场实验 ........................ 8.1 REMUS 模拟器初始条件........................... 8.2 车辆系数调整因子.................................... ....... 9.1  线性化速度参数 .......................... 9.2  线性化组合系数 ................................... 9.3  线性 化机动系数 ................................... 9.4  超调百分比和阻尼比 .................................. A.1  STD REMUS 船体参数.......................  . . . . . .. A.2  积分范围的船体坐标................  .... . . .. A.3  STD REMUS 浮心.................. . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.4  STD REMUS 重心.................. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.5  REMUS 鳍参数..........  ..........  ...... ..  . . . . .. B.1 非线性力系数 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B.2 非线性力矩系数 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.1  轴向阻力系数 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.2  横流阻力系数 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.3  滚动阻力系数 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.4  船体升力及力矩系数 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.5  附加质量系数 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.6  附加质量力交叉项系数 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.7  附加质量K力矩交叉项系数 . . . . . . . . . . . . . . . . . . . . . . . . . . C.8  附加质量M、 N力矩交叉项系数 . . . . . . . . . . . . . . . . . . . . . . . . . . C.9  螺旋桨项 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 1 1 01 10 1 1 02 10 210 3 1 04 10 5 1 05 10 5 1 06 10 6 1 07 10 8 1 09 10 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

---

## Page 21

C.10 Control Fin Coefficients....................... . . . . . . . . . ... 110 D.1 Linearized Combined Coefficients...................... . . . . .... 111 D.2 Linearized Maneuvering Coefficients................. . . . . . . . ... 112 11

---

## Page 22

C.10 控制鳍系数.............................. 110 D.1  线性化组合系数......................  . . . . .... 111 D.2  线性化机动系数..................  . . . . . . . ...  11 2 11

---

## Page 23

Chapter 1 Introduction 1.1 Motivation Improving the performance of modular, low-cost autonomous underwater vehicles (AUVs) in such applications as long-range oceanographic survey, autonomous docking, and shallow-water mine coun- termeasures requires improving the vehicles' maneuvering precision and battery life. These goals can be achieved through the improvement of the vehicle control system. A vehicle dynamics model based on a combination of theory and empirical data would provide an efficient platform for vehi- cle control system development, and an alternative to the typical trial-and-error method of vehicle control system field tuning. As there exists no standard procedure for vehicle modeling in industry, the simulation of each vehicle system represents a new challenge. 1.2 Vehicle Model Development This thesis describes the development and verification of a simulation model for the motion of the REMUS vehicle in six degrees of freedom. In this model, the external forces and moments resulting from hydrostatics, hydrodynamic lift and drag, added mass, and the control inputs of the vehicle propeller and fins are all defined in terms of vehicle coefficients. This thesis describes the derivation of these coefficients in detail, and describes the experimental measurement of the vehicle axial drag. The equations determining the coefficients, as well as those describing the vehicle rigid-body dynamics, are left in non-linear form to better simulate the inherently non-linear behavior of the vehicle. Simulation of the vehicle motion is achieved through numeric integration of the equations of motion. The simulator output is then checked against open-loop data collected in the field. This field data measured the vehicle response to step changes in control fin angle. The simulator is shown to accurately model the vehicle motion in six degrees of freedom. To demonstrate the intended application of this work, this thesis demonstrates the use of a linearized version of the vehicle model to develop a vehicle depth-plane control system. In closing, this thesis discusses plans for further experimental verification of the vehicle coeffi- cients, including tow tank lift and drag measurements, and precision inertial measurements of the vehicle open-water motion and sensor dynamics. 1.3 Research Platform The platform for this research is the REMUS AUV, developed by von Alt and associates at the Oceanographic Systems Laboratory at the Woods Hole Oceanographic Institution [31]. REMUS (Remote Environmental Monitoring Unit) is a low-cost, modular vehicle with applications in au- tonomous docking, long-range oceanographic survey, and shallow-water mine reconnaissance [30]. See Chapter 2 for the specifications of the REMUS vehicle.

---

## Page 24

第一章 介绍 1.1 动机 在远程海洋调查、自动对接和浅水水雷反制等应用中，提高模块化、低成本自主水下航行器（AUV）的 性能需要提升车辆的操纵精度和电池寿命。这些目标可以通过改进车辆控制系统来实现。基于理论和经验 数据相结合的车辆动力学模型将为车辆控制系统开发提供一个高效的平台，并且可替代典型的车辆控制系 统现场调试的试错方法。由于工业中不存在车辆建模的标准程序，每个车辆系统的仿真都代表着一个新的 挑战。 1.2  车辆模型开发 本论文描述了一个用于 REMUS 车辆六自由度运动的仿真模型的开发与验证。在该模型中，由静水力学、 流体动力升力和阻力、附加质量，以及车辆螺旋桨和舵的控制输入产生的外力和力矩，均以车辆系数的形 式定义。 本论文详细描述了这些系数的推导，并描述了车辆轴向阻力的实验测量。 确定系数的方程以及描述车辆刚体动力学的方程都保持非线性形式，以更好地模拟车辆固有的非线性 行为。车辆运动的仿真是通过对运动方程进行数值积分来实现的。然后将模拟器的输出与在现场收集的开 环数据进行对比检查。这些现场数据测量了车辆对控制鳍角阶跃变化的响应。结果表明，模拟器能够准确 地模拟车辆在六自由度下的运动。 为了展示这项工作的预期应用，本论文演示了使用车辆模型的线性化版本来开发车辆深度平面控制系 统。 总之，本论文讨论了进一步实验验证车辆系数的计划，包括牵引水池升力和阻力测量，以及车辆开阔 水域运动和传感器动态的精密惯性测量。 1.3 研究平台 本研究的平台是由冯·奥特及其同事在伍兹霍尔海洋研究所海洋系统实验室开发的 REMUS AUV[31]。REM US（远程环境监测单元）是一种低成本、模块化的车辆，可用于自主对接、远程海洋调查和浅水水域的水 雷侦察[30]。REMUS 车辆的规格请参见第2章。

---

## Page 25

REMUS currently uses a field-tuned PID controller; previous attempts to apply more advanced controllers to REMUS have been hampered by the lack of a mathematical model to describe the vehicle dynamics. 1.4 Model Code The author developed the simulator code using MATLAB. Although MATLAB runs slowly compared to other compilers, the program greatly facilitates data visualization. In developing the code, the author did not use any MATLAB-specific functions, so exporting the model code to another, faster language for controller development will be easy. 1.5 Modeling Assumptions In order to simplify the challenge of modeling an autonomous underwater vehicle, it is necessary to make some assumptions on which to base the model development. 1.5.1 Environmental Assumptions The author made the following assumptions about the vehicle with respect to its environment: * The vehicle is deeply submerged in a homogeneous, unbounded fluid. In other words, the vehicle is located far from free surface (no surface effects, i.e. no sea wave or vehicle wave-making loads), walls and bottom. * The vehicle does not experience memory effects. The simulator neglects the effects of the vehicle passing through its own wake. * The vehicle does not experience underwater currents. 1.5.2 Vehicle/Dynamics Assumptions The author made the following assumptions about the vehicle itself: * The vehicle is a rigid body of constant mass. In other words, the vehicle mass and mass distribution do not change during operation. " Control surface assumptions: We assume that the control fins do not stall regardless of angle of attack. We also assume an instantaneous fin response, meaning that that vehicle actuator time response is small in comparison with the vehicle attitude time response. " Thruster assumptions: We will be using an extremely simple propulsion model, which treats the vehicle propeller as a source of constant thrust and torque. " There exist no significant vehicle dynamics faster than 45 Hz (the modeling time step).

---

## Page 26

REMUS 目前使用基于现场调节的 PID 控制器；之前尝试将更先进的控制器应用于 REMUS 遭遇了困难，因为缺乏用于描述车辆动力学的数学模型。 1.4 型号 代码 作者使用 MATLAB 开发了模拟器代码。尽管与其他编译器相比，MATLAB 运行较慢，但该程 序极大地方便了数据可视化。在开发代码时，作者没有使用任何 MATLAB 特定的函数，因此将 模型代码导出到另一种更快速的语言进行控制器开发将很容易。 1.5 建模假设 为了简化自主水下航行器建模的挑战，有必要对模型开发的基础做出一些假设。 1.5.1 环境假设 作者对该车辆及其环境作出了以下假设： * The vehicle is deeply submerged in a homogeneous, unbounded fluid. 换句话说，车辆位于远离 自由表面（无表面效应，即无海浪或车辆造波载荷）、墙壁和底部的位置。 * The vehicle does not experience memory effects.  模拟器忽略了车辆穿越自身尾流的影响。 * The vehicle does not experience underwater currents. 1.5.2  车辆/动力学 假设 作者对车辆本身作出了以下假设： * The vehicle is a rigid body of constant mass. 换句话说，车辆的质量和质量分布在操作 过程中不会变化。我们假设控制鳍无论迎角如何都不会失速。我们还假设鳍的响应是瞬时的 ，这意味着车辆执行器的响应时间相比车辆姿态的响应时间很短。我们将使用一个极其简单 的推进模型，该模型将车辆的螺旋桨视为恒定推力和扭矩的来源。

---

## Page 27

Chapter 2 The REMUS Autonomous Underwater Vehicle In order to calculate the vehicle coefficients, we must first define the profile of the vehicle, determine its mass, mass distribution, and buoyancy, and finally identify the necessary control fin parameters. 2.1 Vehicle Profile The hull shape of the REMUS vehicle is based on the Myring hull profile equations [22}, which de- scribe a body contour with minimal drag coefficient for a given fineness ratio (body length/maximum diameter). These equations have been modified so as to be defined in terms of the following param- eters: 9 a, b, and c, the full lengths of the nose-section, constant-radius center-section, and tail-section of the vehicle, respectively * n, an exponential parameter which can be varied to give different body shapes. * 20, the included angle at the tip of the tail * d, the maximum body diameter These equations assume an origin at the nose of the vehicle. Nose shape is given by the modified semi-elliptical radius distribution 1= 1 -z+aoffset - a )(l where r is the radius of the vehicle hull measured normal to the centerline, B is the axial position along the centerline, and aoffset is the missing length of the vehicle nose. See Figure 2-1 for a diagram of these parameters, and see Figure 3-1 for a diagram of the vehicle coordinate system. Tail shape is given by the equation 1 F3d tanGl 2 d tan0l r(E) = -d - 2 3d _ )2 + 2 -f 3 (2.2) 2 2c 2 c c3 c2 where the forward body length lf = a + b - aoffset (2.3) and again, r is the vehicle hull radius and E is the axial position along the centerline. Note in Figure 2-1 that coffset is the missing length of the vehicle tail, where c is the full Myring tail length.

---

## Page 28

第二章 REMUS自主水下航行器 为了计算车辆系数，我们必须首先定义车辆的轮廓，确定其质量、质量分布和浮力，最后确定必要的控制 鳍参数。 2.1  车辆简介 REMUS 载具的船体形状基于 Myring 船体轮廓方程 [22]，这些方程描述了在给定细长比（船体长度/最大 直径）下具有最小阻力系数的船体轮廓。为了便于定义，这些方程已被修改为以以下参数表示： 9  a, b, 和 c,  分别为车辆的鼻部段、恒半径中段和尾部段的全长度 * n，一个指数参数，可以改变以得到不同的身体形状。 * 20，尾部尖端的夹角 * d, 最大体径 这些方程假设原点位于车辆的车头。 鼻子的形状由改进的半椭圆半径分布决定 1= 1 -z+aoffset - a )(l 其中 r  是沿中心线垂直方向测量的车辆船体半径，B 是沿中心线的轴向位置，aoffset  是车辆鼻 部缺失的长度。有关这些参数的示意图，请参见图 2-1；有关车辆坐标系的示意图，请参见图 3 -1。 尾部形状由下列方程给出 1 F3d tanGl 2 d tan0l r(E) = -d - 2 3d _ )2 + 2 -f 3 (2.2) 2 2c2 c c3 c2 前体长度在哪里 lf = a + b - aoffset (2.3) 再次，r  是车辆船体半径，E 是沿中心线的轴向位置。注意在图 2-1 中，coffset  是车辆 尾部缺失的长度，其中 c 是完整的 Myring 尾部长度。

---

## Page 29

aoffset a Coffset 4 C Figure 2-1: Myring Profile: vehicle hull radius as a function of axial position For reference, Myring [22, p. 189] assumes a total body length of 100 units, and classifies body types by a code of the form a/b/n/O/jd, where 9 is given in radians. REMUS is based on the Myring B hull contour, which is given by the code 15/55/1.25/0.4363/5. Table 2.1 gives the dimensionalized Myring parameters. Table 2.1: Myring Parameters for STD REMUS Parameter Value Units Description a +1.91e-001 m Nose Length aoffset +1.65e-002 m Nose Offset b +6.54e-001 m Midbody Length c +5.41e-001 m Tail Length Coffset +3.68e-002 m Tail Offset n +2.00 n/a Exponential Coefficient 0 +4.36e-001 radians Included Tail Angle d +1. 91e-001 m Maximum Hull Diameter if +8.28e-001 m Vehicle Forward Length 1 +1. 33e+000 m Vehicle Total Length 2.2 Sonar Transducer The REMUS vehicle is equipped with a forward sonar transducer, which is a cylinder 10.1 cm (4.0 in) diameter. The remaining transducer dimensions are given in Figure 2-2. 2.3 Control Fins The REMUS vehicle is equipped with four identical control fins, mounted in a cruciform pattern near the aft end of the hull. These fins have a NACA 0012 cross-section; their remaining dimensions are given in Figure 2-3. The relevant fin parameters are given in Table 2.2. 2.4 Vehicle Weight and Buoyancy The weight of the REMUS vehicle can change between missions, depending on the type of batteries used in the vehicle and the amount of ballast added. REMUS is typically ballasted with around 1.5 pounds of buoyancy, so that it will eventually float to the surface in the event of a computer or power failure. Typical values for the vehicle weight and buoyancy are given in Table 2.3.

---

## Page 30

aoffset a Coffset 4 C 图 2-1：Myring 剖面：车辆船体半径与轴向位置的关系 作为参考，Myring [22，第189页] 假设总体长度为100单位，并通过形式为 a/b/n/O /jd,  的 代码来分类体型，其中9以弧度表示。REMUS 基于 Myring B 型船体轮廓，该轮廓由代码 15/55/ 1.25/0.4363/5 给出。表 2.1 给出了量化的 Myring 参数。 表 2.1：STD REMUS 的鼓膜参数 Parameter Value Units Description a +1.91e-001 m Nose Length aoffset +1.65e-002 m Nose Offset b +6.54e-001 m Midbody Length c +5.41e-001 m Tail Length Coffset +3.68e-002 m Tail Offset n +2.00 n/a Exponential Coefficient 0 +4.36e-001 radians Included Tail Angle d +1. 91e-001 m Maximum Hull Diameter if +8.28e-001 m Vehicle Forward Length 1 +1. 33e+000 m Vehicle Total Length 2.2 声纳换能器 REMUS 车辆配备有一个前置声纳换能器，该换能器为一个直径为10.1厘米（4.0英寸）的圆柱 体。其余换能器的尺寸见图2-2。 2.3 控制翼 REMUS 载具配备了四个相同的控制鳍，安装在船体尾部附近，呈十字形排列。这些鳍具有 NA CA 0012 截面；其余尺寸见图 2-3。相关的鳍参数见表 2.2。 2.4  车辆重量与浮力 REMUS 车辆的重量可能会因任务而异，这取决于车辆使用的电池类型和添加的压载物数量。R EMUS 通常配重约 1.5 磅的浮力，以便在计算机或电源故障的情况下最终浮到水面。车辆重量 和浮力的典型值列于表 2.3。

---

## Page 31

12.6 cm 14.2 cm 5.0 cm R Figure 2-2: REMUS Low-Frequency Sonar Transducer (XZ-plane) 2.9 cm 11.2 cm 14.2 cm - 5.3 cm Figure 2-3: REMUS Tail Fins (XY- and XZ-plane) 6.2 cm 13.1 cm W_ - - - - - - - - - -

---

## Page 32

12.6 cm 14.2 cm 5.0 cm R 图 2-2：REMUS 低频声呐换能器（XZ平面） 2.9 cm 11.2 cm 14.2 cm - 5.3 cm 图 2-3：REMUS 尾鳍（XY 平面和 XZ 平面） 6.2 cm 13.1 cm W_ - - - - - - - - - -

---

## Page 33

Table 2.2: REMUS Fin Parameters Parameter Value Units Description Sfi +6.65e-003 m2 Planform Area bfi +8.57e-002 m Span Xfinpost -6.38e-001 m Moment Arm wrt Vehicle Origin at CB 6max +1. 36e+001 deg Maximum Fin Angle aan +5.14e+000 m Max Fin Height Above Centerline Cmean +7.47e-002 m Mean Chord Length t +6.54e-001 n/a Fin Taper Ratio (Whicker-Felner) cdf +5.58e-001 n/a Fin Crossflow Drag Coefficient ARe +2.21e+000 n/a Effective Aspect Ratio a +9.00e-001 n/a Lift Slope Parameter CLa +3.12e+000 n/a Fin Lift Slope Table 2.3: Vehicle Weight and Buoyancy Parameter Value Units W +2.99e+002 N B +3.06e+002 N 2.5 Centers of Buoyancy and Gravity For a given REMUS vehicle during field operations, the center of buoyancy stays roughly constant as there are rarely any changes made to the exterior of the hull. The vehicle center of gravity, on the other hand, can vary, as between missions it is often necessary to change the vehicle battery packs and re-ballast the vehicle. - The average values are given in Tables 2.4 and 2.5. Table 2.4: Center of Buoyancy wrt Origin at Vehicle Nose Parameter Value Units Xcb -6. 11e-001 m Ycb +0.00e+000 m Zcb +0.00e+000 m 2.6 Inertia Tensor The vehicle inertia tensor is defined with respect to the body-fixed origin at the vehicle center of buoyancy. As the products of inertia I 'Zy, and I.z are small compared to the moments of inertia I., Iyy, and Iz,, we will assume that they are zero, in effect assuming that the vehicle has two axial planes of symmetry. These values were estimated based on the vehicle weight list (a table listing the locations and weights of the various vehicle internal components). Although the changes in the vehicle center of gravity described above will obviously affect the vehicle moments of inertia, we will assume that these changes are small enough to be ignored. The estimated values are given in Table 2.6. 2.7 Final Vehicle Profile Figure 2-4 shows the complete vehicle profile, plotted over an ellipsoid for reference. Some additional hull parameters, mostly functions of hull geometry, are given in Table 2.7.

---

## Page 34

表 2.2：REMUS 翼鳍参数 Parameter Value Units Description Sfi +6.65e-003 m2 Planform Area bfi +8.57e-002 m Span Xfinpost -6.38e-001 m Moment Arm wrt Vehicle Origin at CB 6max +1. 36e+001 deg Maximum Fin Angle aan +5.14e+000 m Max Fin Height Above Centerline Cmean +7.47e-002 m Mean Chord Length t +6.54e-001 n/a Fin Taper Ratio (Whicker-Felner) cdf +5.58e-001 n/a Fin Crossflow Drag Coefficient ARe +2.21e+000 n/a Effective Aspect Ratio a +9.00e-001 n/a Lift Slope Parameter CLa +3.12e+000 n/a Fin Lift Slope 表 2.3：车辆重量和浮力 Parameter Value Units W +2.99e+002 N B +3.06e+002 N 2.5 浮力中心和重心 在现场操作中，对于特定的 REMUS 车辆，由于几乎很少对船体外部进行更改，其浮心位置大 致保持不变。另一方面，车辆重心可能会有所变化，因为在不同任务之间，通常需要更换车辆 电池组并重新配重车辆。 - 平均值见表 2.4 和表 2.5。 表 2.4：浮心相对于车辆前端的原点 Parameter Value Units Xcb -6. 11e-001 m Ycb +0.00e+000 m Zcb +0.00e+000 m 2.6 惯性张量 车辆惯性张量是相对于位于车辆浮心的车体固定原点定义的。由于惯性积 I'Zy,  和 I.z 相比于惯性 矩 I.Iyy,  和 Iz,,  很小，我们将假设它们为零，实际上假设车辆具有两个轴对称平面。 这些数值是根据车辆重量清单（列出各个车辆内部组件的位置和重量的表格）估算的。虽然 上文所述的车辆重心变化显然会影响车辆的惯性矩，但我们将假设这些变化足够小，可以忽略 不计。估算值见表2.6。 2.7 最终车辆概况 图 2-4 显示了完整车辆剖面，并绘制在椭球体上以作参考。表 2.7 给出了一些额外的船体参数， 大多是船体几何的函数。

---

## Page 35

Table 2.5: Center of Gravity wrt Origin at CB Parameter Value Units Xcg +0. 00e+000 m Ycg +0.00e+000 m zcg +1.96e-002 m Table 2.6: Moments of Inertia wrt Origin at CB Parameter Value Units I +1.77e-001 kg m2 Iyy +3.45e+000 kg - m2 Izz +3.45e+000 kg . 2 Note that the estimates for vehicle buoyancy and longitudinal center of buoyancy are based solely on the bare hull profile, and do not account for the vehicle fins and transponder, or the flooded sections in the vehicle nosecap. The Xcb value given in Table 2.4 and the total buoyancy B given in Table 2.3 are based on experimental measurements. Table 2.7: STD REMUS Hull Parameters Parameter Value Units Description p +1. 03e+003 kg/m 3 Seawater Density Af +2.85e-002 m 2 Hull Frontal Area AP +2.26e-001 In 2 Hull Projected Area (xz plane) S. +7.09e-001 m 2 Hull Wetted Surface Area V +3. 15e-002 m3 Estimated Hull Volume Best +3.17e+002 N Estimated Hull Buoyancy Xcb(est) +5. 54e-003 m Est. Long. Center of Buoyancy

---

## Page 36

表 2.5：重心关于中心盒原点的位置 Parameter Value Units Xcg +0. 00e+000 m Ycg +0.00e+000 m zcg +1.96e-002 m 表 2.6：关于 CB 原点的转动惯量 Parameter Value Units I +1.77e-001 kg m2 Iyy +3.45e+000 kg - m2 Izz +3.45e+000 kg . 2 请注意，车辆浮力和纵向浮心位置的估算仅基于裸船体轮廓，并未考虑车辆的鳍和应答器，也未考虑 车辆首盖中进水的部分。表 2.4 中给出的 Xcb  值以及表 2.3 中给出的总浮力 B 是基于实验测量得出的。 Table 2.7: STD REMUS 船体 参数 Parameter Value Units Description p +1. 03e+003 kg/m 3 Seawater Density Af +2.85e-002 m 2 Hull Frontal Area AP +2.26e-001 In 2 Hull Projected Area (xz plane) S. +7.09e-001 m 2 Hull Wetted Surface Area V +3. 15e-002 m3 Estimated Hull Volume Best +3.17e+002 N Estimated Hull Buoyancy Xcb(est) +5. 54e-003 m Est. Long. Center of Buoyancy

---

## Page 37

- - . - . .. . . -. . .. . .. . - . . . . . . . . . . . . . . - . . .. . . -. .. . . . . - . . .. . . - . . . . . . .. . . . 6.99 ity yancl - .-. - -0.2 -0.1 0 0.1 0.2 0.3 0.4 0.5 -0.6 - Hull Profile - Ellipsoid, I/d = + Center of Grav -. o Center of Buo ............................. I. -04-0. 0 - . -0.4 -0.2 0 0.2 x-axis (m) Figure 2-4: STD REMUS Profile (XZ-plane) Figure 2-5: The REMUS Autonomous Underwater Vehicle ...................................... I

---

## Page 38

- - . - . .. . . -. . .. . .. . - . . . . . . . . . . . . . . - . . .. . . -. .. . . . . - . . .. . . - . . . . . . .. . . . 6.99 ity yancl - .-. - -0.2 -0.1 0 0.1 0.2 0.3 0.4 0.5 -0.6 - Hull Profile - Ellipsoid, I/d = + Center of Grav -. o Center of Buo ............................. I . -04-0. 0 - . -0.4 -0.2 0 0.2 x-axis (m) 图 2-4：STD REMUS 轮廓（XZ 平面） 图 2-5：REMUS 自主水下航行器 ...................................... I

---

## Page 39

r Chapter 3 Elements of the Governing Equations In this chapter, we define the equations governing the motion of the vehicle. These equations consist of the following elements: * Kinematics: the geometric aspects of motion " Rigid-body Dynamics: the vehicle inertia matrix * Mechanics: forces and moments causing motion These elements are addressed in the following sections. 3.1 Body-Fixed Vehicle Coordinate System Origin Please note that in all future calculations, the origin of the vehicle body-fixed coordinate system is located at the vehicle center of buoyancy, as defined in Section 2.5 and illustrated in Figure 2-4. 3.2 Vehicle Kinematics The motion of the body-fixed frame of reference is described relative to an inertial or earth-fixed reference frame. The general motion of the vehicle in six degrees of freedom can be described by the following vectors: 71 [X Y z ] T; V1 UVW w]T; 1-1 = [ X y Z ]T; V2 = [p q r ] - 2 =[ K M N ]T where 77 describes the position and orientation of the vehicle with respect to the inertial or earth- fixed reference frame, v the translational and rotational velocities of the vehicle with respect to the body-fixed reference frame, and r the total forces and moments acting on the vehicle with respect to the body-fixed reference frame. See Figure 3-1 for a diagram of the vehicle coordinate system. The following coordinate transform relates translational velocities between body-fixed and iner- tial or earth-fixed coordinates: x1 9z u = , (31(2) V w (3.1)

---

## Page 40

r 第三章 控制方程的要素 在本章中，我们定义了控制车辆运动的方程。这些方程包括以下要素： * Kinematics: 运动的几何方面 " Rigid-body Dynamics:  车辆惯性矩阵 * Mechanics:  引起运动的力和力矩 这些元素将在以下章节中进行讨论。 3.1  车身固定坐标系原点 请注意，在所有后续计算中，车辆车身固定坐标系的原点位于车辆的浮心，如第2.5节所定义，并在图2-4 中所示。 3.2  车辆运动学 相对于惯性参考系或地球固定参考系，描述了刚体固定参考系的运动。车辆在六自由度中的一般运动可以 通过以下向量来描述： 71 [X Y z ] T; V1 U V W  w ] T ; 1-1 = [ X y Z ]T; V2 = [p q r ] - 2 = [ K M N ]T 其中77描述了车辆相对于惯性或地固定参考系的位置和姿态，v 描述了车辆相对于车体固定参考系的平移 和旋转速度，r 描述了作用在车辆上的总力和力矩相对于车体固定参考系。车辆坐标系的示意图见图3-1。 以下坐标变换将机体固定坐标系和惯性或地固定坐标系之间的平移速度联系起来： x1 9z u = , (31(2) V w (3.1)

---

## Page 41

Figure 3-1: REMUS Body-Fixed and Inertial Coordinate Systems where J1 (212)= cos cos 0 sin cos 9 - sin 9 - sin V@ cos $ + cos @ sin0 sin #) cos 0 cos q5 + sin V) sin 0 sin4) cos 9 sin 4) sint/ sin 4 + cos V@ sin0 cos p - cos 0 sin 4)+ sin sin 0 cos4) cos 0 cos $ Note that J 1 (q2) is orthogonal: (J 1 (q2)) 1 = (J 1 (q2) )T (3.3) The second coordinate transform relates rotational velocities between body-fixed and earth-fixed coordinates: = J2 (212) 1 sin 4tan0 J2 (72)= 0 os #5 0 sin0/ cos 0 P1 q r] (3.4) (3.5) cos 4)tan0 - sin 4 cos 0/ cos Note that J 2 (272) is not defined for pitch angle 0 = ±90*. This is not a problem, as the vehicle motion does not ordinarily approach this singularity. If we were in a situation where it became necessary to model the vehicle motion through extreme pitch angles, we could resort to an alternate kinematic representation such as quaternions or Rodriguez parameters [17]. (3.2) where 0

---

## Page 42

图 3-1：REMUS 车体固定坐标系和惯性坐标系 哪里 J1 (212)= cos cos 0 sin cos 9 - sin 9 - sin V@ cos $ + cos @ sin0 sin #) cos 0 cos q5 + sin V) sin 0 sin4) cos 9 sin 4) sin t/ sin 4 + cos V@ sin0 cos p - cos 0 sin 4)+ sin sin 0 cos4) cos 0 cos $ 注意 J 1 (q2)  是正交的： (J 1 (q2)) 1 = (J 1 (q2) )T (3.3) 第二个坐标变换将机体固定坐标系与地球固定坐标系之间的旋转速度联系起来： = J2 (212) 1 sin 4tan0 J2 (72)= 0 os #5 0 sin0/ cos 0 P1 q r] (3.4) (3.5) cos 4)tan0 - sin 4 cos 0/ cos 注意，J 2 (272)  在俯仰角为 0 时 = ±90*.  未定义。这不是问题，因为车辆运动通常 不会接近此奇异点。如果我们处于必须模拟车辆通过极端俯仰角运动的情况， 我们可以采用其他运动学表示方法，例如四元数或罗德里格斯参数 [17]。 (3.2) 哪里 0

---

## Page 43

3.3 Vehicle Rigid-Body Dynamics The locations of the vehicle centers of gravity and buoyancy are defined in terms of the body-fixed coordinate system as follows: Xg Xb rG Yg bB (3.6) j [ ZbJ Given that the origin of the body-fixed coordinate system is located at the center of buoyancy as noted in Section 3.1, the following represent equations of motion for a rigid body in six degrees of freedom, defined in terms of body-fixed coordinates: m [i - vr +wq - x,(q2 + r2)+ yg(pq - )+ zg(pr +)] =Xext m [ - wp + ur - yg(r 2 +P2) + zg(qr - + +xg(qp -|+ Yxt m [tb - uq + vp - zg (p2 + 2) + xg (rp - )+ yg (rq + )]=(Zext I.J + (Izz - Iyy)qr - (i' + pq)Iz + (r2 - q2)Iz + (pr - 4)I.y +m[yg (i - uq + vp) - zg ( - wp + ur)] = Kext (3.7) Ivy4 + (Izz - Izz)rp - (p + qr)Ixy + (p 2 _ r2 )Izz + (qp - )Iyz +M [ z (6 - yr + wq) - xg(ib - uq + vp)] = Mxt Izzj + (I~y - Izz)pq - (4 + rp)Iyz + (q2 _ p2)Iy + (rq - p)Iz +m[x(V' - wp+ur) - yg(it - yr +wq)] = Nxt where m is the vehicle mass. The first three equations represent translational motion, the second three rotational motion. Note that these equations neglect the zero-valued center of buoyancy terms. Given the body-fixed coordinate system centered at the vehicle center of buoyancy, we have the following, diagonal inertia tensor. IXX 0 0 I [0 I y 0 0 0 Izz This is based on the assumption, stated in Section 2.6, that the vehicle products of inertia of inertia are small. This simplifies the equations of motion to the following: m [it -vr +wq - x(q 2 +r 2 )+ y9 (pq - + zg(pr +4)] = Xext m [?-wp+ur - y,(r 2 ±p 2 ) + zg(qr - )+ xg(qp+ ]= Yext m [ -uq+vp- zg(p 2 +q 2 ) +xg(rp - 4) + yg(rq p)] - Zext (3.8) Ixjp+ (Izz - Iyy)qr + m [yg(ib - uq + vp) - zg(i7 - wp + ur)] = Kxt Iyyj + (Ix. - Izz)rp + m [zg(6* - vr + wq) - x.(ib - uq + vp)] =( Mext Izzi + (Ivy - Izz)pq + m [x 9(b - wp + ur) - yg(t - vr + wq)] = Next We can further simply these equations by assuming that y9 is small compared to the other terms. Given the layout of the internal components of the REMUS vehicle, unless the vehicle is specially ballasted yg is in fact negligible. This results in the following equations for the vehicle rigid body

---

## Page 44

3.3  车辆刚体动力学 车辆重心和浮力中心的位置在体固定坐标系中定义如下： Xg Xb rG Yg bB (3.6) j [ ZbJ 鉴于如第3.1节所述，固定于物体的坐标系的原点位于浮心处，以下表示了以物体固定坐标系定义的刚体 六自由度运动方程： m [i - vr +wq - x,(q2 + r2)+ yg(pq - )+ zg(pr +)] =Xext m [ - w p  + ur - y g ( r  2 +P2) + z g (q r  - + +xg(qp -|+ Y x t m [tb - uq + vp - zg (p2 + 2) + xg (rp - )+ yg (rq + )]=(Zext I.J + (Izz - Iyy)qr - (i' + pq)Iz + (r2 - q2)Iz + (p r - 4)I.y +m[yg (i - uq + vp) - zg ( - w p + ur)] = Kext (3.7) Ivy4 + (Izz - Izz)rp  - (p + qr)Ixy + (p2 _ r2 )Izz + (qp - )Iyz +M  [ z (6 - yr + wq) - xg(ib - uq + vp)] = M x t Izzj + (I~y - Izz)pq - (4 + rp)Iyz + (q2 _ p2)Iy + (rq - p )Iz + m [ x ( V ' - w p + u r )  - yg(it - yr +wq)] = N x t 其中 m  是车辆质量。前三个方程表示平移动作，后三个表示旋转动作。请注意，这些方程忽略了零值的 浮心项。 给定以车辆浮心为中心的机体固定坐标系，我们得到如下对角惯性张量。 IXX 0 0 I [0 I y 0 0 0 Izz 这是基于第2.6节中提出的假设，即车辆的惯性积很小。 这将运动方程简化为如下形式： m [it -vr +wq - x(q 2 +r 2 )+ y9 (pq - + zg(pr +4)] = Xext m [ ? -w p + u r  - y,(r 2 ±p 2 ) + zg(qr - )+ xg(qp+ ]= Yext m [ -u q + v p - zg(p2 +q 2 ) +xg(rp - 4) + yg(rq p)] - Zext (3.8) Ix jp +  (Izz - Iyy)qr + m [yg(ib - uq + vp) - zg(i7 - wp + ur)] = K x t Iyyj + (Ix. - Izz)rp + m [zg(6* - v r + wq) - x.(ib - uq + vp)] =( Mext Izzi + (Ivy - Izz)pq + m [x 9(b - wp + u r ) - yg(t - v r  + wq)] = Next 通过假设 y9  相对于其他项较小，我们可以进一步简化这些方程。考虑到 REMUS 车辆内部组件的布 局，除非车辆进行了特殊配重，否则 yg 实际上可以忽略不计。这导致了车辆刚体的以下方程。

---

## Page 45

dynamics: m [it - or +wq - xg(q 2 +r 2 )+ zg(pr +)] = Xext m [v -wp+ur +zg(gr -P)+xg(qp+ f)] =EYxt m [i - uq+vp - zg(p2 q 2 )+xg(rp-4)] = Zext (3.9) IxxP + (Izz - Iyy)qr + m [-zg(i - wp + ur)] = ( Kext Iyy4+ (Ix - Izz)rp +m [zg(i -vr +wq) - xg(t - uq +vp)] = Mext Izzr + (Ivy - Izx)pq + m [xg(b - wp + ur)] = ( Next 3.4 Vehicle Mechanics In the vehicle equations of motion, external forces and moments Fext = Fhydrostatic + Fft + Fdrag + +Fcontrol are described in terms of vehicle coefficients. For example, axial drag (d PCdAf ) uJl= XUjU 1u Jul . 1U = -O -Pd Fd- p u> 2pcAS These coefficients are based on a combination of theoretical equations and empirically-derived for- mulae. The actual values of these coefficients are derived Chapter 4.

---

## Page 46

动态： m [it - o r  +wq - xg(q 2 +r 2 )+ zg (p r +)] = Xext m [v -w p + u r  +zg(gr -P )+ xg (q p +  f)] = E Y x t m [i - u q + v p  - z g ( p 2 q 2 )+ x g (r p -4 )]  = Zext (3.9) IxxP + (Izz - Iyy)q r + m [ -z g (i - wp + ur)] = ( Kext Iyy4+ (Ix - Izz)rp +m [zg (i -vr +wq) - xg (t - uq +vp)] = Mext Izzr + (Ivy - Izx)pq + m [xg(b - w p + ur)] = ( Next 3.4  车辆力学 在车辆运动方程中，外力和力矩 Fext = Fhydrostatic + F ft + Fdrag + +Fcontrol 以车辆系数来描述。例如，轴向阻力 (d PCdAf ) u J l =  XUjU1u Jul . 1U = -O -Pd Fd- p u> 2 p c A S 这些系数是基于理论方程与经验公式的结合。 这些系数的实际数值是在第4章中得出的。

---

## Page 47

Chapter 4 Coefficient Derivation In this chapter, we derive the coefficients defining the forces and moments on the vehicle. The vehicle and fluid parameters necessary for calculating each coefficient are included either in the section describing the coefficient, or are listed in Appendix A. 4.1 Hydrostatics The vehicle experiences hydrostatic forces and moments as a result of the combined effects of the vehicle weight and buoyancy. Let m be the mass of the vehicle. Obviously, the vehicle weight W = mg. The vehicle buoyancy is expressed as B = pVg, where p is the density of the surrounding fluid and V the total volume displaced by the vehicle. It is necessary to express these forces and moments in terms of body-fixed coordinates. This is accomplished using the transformation matrix given in Equation 3.2: 0 0 fG(1 2 ) = [o 0 fB()2=Ji 0 (4.1) W B The hydrostatic forces and moments on the vehicle can be expressed as: FHS = fG- fB MHS = rG X fG~ -rB X fB These equations can be expanded to yield the nonlinear equations for hydrostatic forces and mo- ments: XHS =-(W -B)sinO YHS =(W - B) cosO sinp ZHS =(W - B)cos0 cos # KHS = - (YgW - ybB) cosO cos$ - (z 9W - zbB) cos 0 sin( MHS = - (zgW - ZbB) sinG - (xgW - XbB)cos0 cos# NHs = - (xgW - XbB) cos0sin# - (ygW - ybB) sinG Note that the hydrostatic moment is stabilizing in pitch and roll, meaning that the hydrostatic moment opposes deflections in those angular directions.

---

## Page 48

第四章 系数 推导 在本章中，我们推导了定义车辆上力和力矩的系数。计算每个系数所需的车辆和流体参数要么包含在描 述该系数的章节中，要么列在附录A中。 4.1 静力学 由于车辆重量和浮力的共同作用，车辆会受到静水力以及力矩的作用。设 m  为车辆的质量。显然，车辆 重量为 W = mg. 。车辆浮力表示为 B = pVg，其中 p 是周围流体的密度，V 是车辆排开的总容积。 有必要将这些力和力矩用体坐标系来表示。这可以通过使用方程3.2中给出的变换矩阵来完成： 0 0 fG(12) =  [o 0 fB ()2 = J i 0 (4.1) W B 这 车辆上的静水力和力矩可以表示 表示为： FHS = fG- fB M H S  = rG X f G ~  - r B X fB 这些方程可以展开，以得出静水力和力矩的非线性方程： X H S =-(W -B )sin O YHS = (W  - B) cosO sinp ZHS = (W  - B)cos0 cos # K H S = - (YgW - ybB) cosO cos$ - (z 9W - zbB) cos 0 sin( MHS = - (zgW - ZbB) sinG - (xgW  - XbB)cos0 cos# NHs = - (xgW - XbB) cos0sin# - (ygW  - ybB) sinG 注意，静水力矩在纵倾和横倾方向上是稳定的，这意味着静水力矩会抵抗这些角度方向的偏转。

---

## Page 49

4.2 Hydrodynamic Damping It is well known that the damping of an underwater vehicle moving at a high speed in six degrees of freedom is coupled and highly non-linear. In order to simplify modeling the vehicle, we will make the following assumptions: " We will neglect linear and angular coupled terms. We will assume that terms such as Yr, and Mr, are relatively small. Calculating these terms is beyond the scope of this work. " We will assume the vehicle is top-bottom (xy-plane) and port-starboard (xz-plane) symmetric. We will ignore the vehicle asymmetry caused by the sonar transducer. This allows us to neglect such drag-induced moments as Kvii and Muiui. " We will neglect any damping terms greater than second-order. This will allow us to drop such higher-order terms as Yvvv. The principal components of hydrodynamic damping are skin friction due to boundary layers, which are partially laminar and partially turbulent, and damping due to vortex shedding. Non- dimensional analysis helps us predict the type of flow around the vehicle. Reynolds number represents the ratio of inertial to viscous forces, and is given by the equation Ul Re = -- (4.4) 1/ where U is the vehicle operating speed, which for REMUS is typically 1.5 m/s (3 knots); 1 the characteristic length, which for REMUS is 1.7 meters; and v the fluid kinematic viscosity, which for seawater at 15'C, Newman [24] gives a value of 1.190 x 10-6 m2/s. This yields a Reynolds number of 1.3 x 106, which for a body with a smooth surface falls in the transition zone between laminar and turbulent flow. However, the hull of the REMUS vehicle is broken up by a number of seams, pockets, and bulges, which more than likely trip the flow around the vehicle into the turbulent regime. We can use this information to estimate the drag coefficient of the vehicle. Note that viscous drag always opposes vehicle motion. In order to result in the proper sign, it is necessary in all equations for drag to consider vI v, as opposed to v2 4.2.1 Axial Drag Vehicle axial drag can be expressed by the following empirical relationship: X = - (PcdAf) u |u| (4.5) This equation yields the following non-linear axial drag coefficient: Xuii = - pcdAf (4.6) where p is the density of the surrounding fluid, Af the vehicle frontal area, and cd the axial drag coefficient of the vehicle. Bottaccini [7, p. 26], Hoerner [15, pg. 3-12] and Triantafyllou [29] offer empirical formulae for calculating the axial drag coefficient. For example, Triantafyllou: cd = c"7 A, P1 + 60 (d'+0.0025 (Il(4.7) where c,, is Schoenherr's value for flat plate skin friction, A, = ld is the vehicle plan area, and Af is the vehicle frontal area. From Principles of Naval Architecture [20], we get an estimate for c,, of 3.397 x 10-3.

---

## Page 50

4.2 水动力阻尼 众所周知，在六自由度下高速运动的水下航行器的阻尼是耦合且高度非线性的。为了简化对航 行器的建模，我们将作出以下假设： " We will neglect linear and angular coupled terms. 我们将假设诸如 Yr,  和 Mr,  之类的项相对 较小。计算这些项超出了本工作的范围。 We will assume the vehicle is top-bottom (xy-plane) and port-starboard (xz-plane) symmetric.我 们将忽略声纳换能器引起的车辆不对称性。这使我们能够忽略由阻力引起的力矩，如 Kvii 和 Muiui。We will neglect any damping terms greater than second-order. 这将使我们能够舍弃诸 如 Yvvv 之类的高阶项。 水动力阻尼的主要组成部分是由于边界层产生的表面摩擦，这些边界层部分为层流，部分为 湍流，以及由涡流脱落引起的阻尼。无量纲分析帮助我们预测车辆周围的流动类型。雷诺数表 示惯性力与粘性力的比值，其表达式为 Ul Re = -- (4.4) 1/ 其中 U  是车辆运行速度，对于 REMUS 通常为 1.5 米/秒（3 节）；1  是特征长度，对于 REMU S 为 1.7 米；v  是流体运动粘度，对于 15°C 的海水，Newman [24] 给出的值为 1.190 x 10-6 m2/ 秒。 这产生了一个雷诺数为1.3 x 10^6，对于表面光滑的物体，这落在层流和湍流之间的过渡区。 然而，REMUS 车辆的船体被许多接缝、凹槽和凸起打断，这很可能会使车辆周围的流动进入湍 流状态。我们可以利用这些信息来估算车辆的阻力系数。 请注意，粘性阻力总是与车辆运动相反。为了得到正确的符号，在所有阻力方程中都必须考 虑 vI v，而不是 v2。 4.2.1  轴向阻力 车辆轴向阻力可以用以下经验关系来表示： X = - (PcdAf) u |u| (4.5) 该方程得出以下非线性轴向阻力系数： X u ii = - pcdAf (4.6) 其中 p 是周围流体的密度，Af  是车辆正面面积，cd  是车辆的轴向阻力系数。 Bottaccini [7, 第26页]、Hoerner [15, 第3-12页] 和 Triantafyllou [29] 提供了计算轴向阻力系数 的经验公式。例如，Triantafyllou： cd = c"7 A, P1 + 60 ( d '+ 0 .0 0 2 5  (Il(4.7) 其中 c,,  是 Schoenherr 对平板表面摩擦的值，A, = ld  是车辆的平面面积，Af 是车辆的 正面面积。从 Principles of Naval Architecture [20] 中，我们得到 c,, 的估计值为 3.397 x 10 ^-3。

---

## Page 51

These empirical equations yield a value for Cd in the range of 0.11 to 0.13. Experiments conducted at sea by the Oceanographic Systems Lab measuring the propulsion efficiency of the vehicle resulted in an estimate for Cd of 0.2. Full-scale tow tank measurements of the vehicle axial drag-conducted by the author at the University of Rhode Island and described in Chapter 5-yielded an axial drag coefficient of 0.27. This higher value reflects the drag of the vehicle hull plus the drag of sources neglected in the empirical estimate, such as the vehicle fins and sonar transponder, and the pockets in the vehicle nose section. We will use this higher, experimentally-measured value in the vehicle simulation. See Table C.1 for the final value of Xg g . 4.2.2 Crossflow Drag Vehicle crossflow drag is considered to be the sum of the hull crossflow drag plus the fin crossflow drag. The method used for calculating the hull drag is analogous to strip theory, the method used to calculate the hull added mass: the total hull drag is approximated as the sum of the drags on the two-dimensional cylindrical vehicle cross-sections. Slender body theory is a reasonably accurate method for calculating added mass, but for viscous terms it can be off by as much as 100% [29]. This method does, however, allow us to include all of the terms in the equations of motion. In conducting the vehicle simulation, we will attempt to correct any errors in the crossflow drag terms through comparison with experimental data and observations of the vehicle at sea. The nonlinear crossflow drag coefficients are expressed as follows: 1 122 MYI N I pcac X2 2xR(x)dx - 2 xfin - PSfinCdf I t Xb2(4.8) Y =- -Z pcdc 2xlx|R(x)dx - 2xfin IXfin - pSfincdf M Nrr - PCdc j 2x 3 R(x)dx - 2in - (PSficdf) where p is the seawater density, Cdc the drag coefficient of a cylinder, R(x) the hull radius as a function of axial position as given by Equations 2.1 and 2.2, Sfln the control fin planform area, and Cdf the crossflow drag coefficient of the control fins. See Table A.2 for the limits of integration. Hoerner [15] estimates the crossflow drag coefficient of a cylinder Cdc to be 1.1. The crossflow drag coefficient cdf is derived using the formula developed by Whicker and Fehlner [32]: Cdf = 0.1 + 0.7t (4.9) where t is the fin taper ratio, or the ratio of the widths of the top and bottom of the fin along the vehicle long axis. From this formula, we get an estimate for cdf of 0.56. See Table C.2 for the final coefficient values. 4.2.3 Rolling Drag We will approximate the rolling resistance of the vehicle by assuming that the principle component comes from the crossflow drag of the fins. F = (Yvvfrmean) reanp |p| (4.10) where Yvvf is the fin component of the vehicle crossflow drag coefficient, and rmean is the mean fin height above the vehicle centerline. This yields the following equation for the vehicle rolling drag

---

## Page 52

这些经验方程得出的Cd值在0.11到0.13的范围内。海洋系统实验室在海上进行的实验测量了该交通工 具的推进效率，得出了Cd 的估计值为0.2。 作者在罗德岛大学进行的车辆轴向阻力全尺寸拖曳水池测量，并在第5章中描述，得到的轴向阻力系数 为0.27。这个较高的数值反映了车辆船体的阻力以及经验估算中忽略的阻力来源，例如车辆的鳍片和声呐 应答器，以及车辆前端区域的空腔。我们将在车辆仿真中使用这个更高的、实验测得的数值。 请参见表 C.1 获取 X g  g . 的最终值 4.2.2 横流阻力 车辆横向流动阻力被认为是船体横向流动阻力与鳍横向流动阻力的总和。用于计算船体阻力的方法类似于 条带理论，用于计算船体附加质量的方法：总船体阻力近似为二维圆柱车辆横截面阻力之和。 细长体理论是一种计算附加质量的相当准确的方法，但对于黏性项，它的误差可能高达100% [29]。然 而，这种方法允许我们在运动方程中包含所有项。在进行车辆模拟时，我们将通过与实验数据和海上车辆 观测的比较，尝试纠正横流阻力项中的任何误差。 非线性交叉流阻力系数表示如下： 1 122 MYI N I pcac X2 2xR(x)dx - 2 x fin  - PSfinCdf I t Xb2(4.8) Y =- -Z pcdc 2xlx|R(x)dx - 2xfin IXfin - pSfincdf M Nrr - PCdc j 2x 3 R(x)dx - 2 i n  - (PSficdf) 其中 p 是海水密度，Cdc  是圆柱体的阻力系数，R(x)  是船体半径，作为轴向位置的函数，由方程 2.1 和 2. 2 给出，Sfln  是舵翼的平面面积，Cdf  是舵翼的横流阻力系数。积分的限制请参见表 A.2。 Hoerner [15] 估计圆柱 Cdc  的横流阻力系数为 1.1。横流阻力系数 cdf 是使用 Whicker 和 Fehlner [32] 开 发的公式推导得出的： Cdf = 0.1 + 0.7t (4.9) 其中 t 是鳍锥度比，或沿车辆纵向轴线鳍顶端和底端宽度的比值。根据这个公式，我们得到 cdf  的估算值 为 0.56。 请参见表 C.2 以获取最终系数值。 4.2.3 滚动阻力 我们将通过假设主要部分来自鳍片的横流阻力来近似车辆的滚动阻力。 F = (Yvvfrmean) r e a n p  |p| (4.10) 其中 Yvvf  是车辆横流阻力系数的鳍组件，rmean 是车辆中心线以上的平均鳍高度。这得出车辆滚动阻力 的以下方程

---

## Page 53

coefficient: KpIpi = Y"VV-rma (4.11) This is at best a rough approximation for the actual value. It would be better to use experimental data. See Table C.3 for the coefficient value based on this rough approximation. 4.3 Added Mass Added mass is a measure of the mass of the moving water when the vehicle accelerates. Ideal fluid forces and moments can be expressed by the equations: F = -imji - ejk1Uiikm1i Mi = -nimj±si - eFk1Uiikm1+3,i - Ejk1UkUimii (4.12) where i=1,2,3,4,5,6 and jkl=1,2,3 and where the alternating tensor Ejkl is equal to +1 if the indices are in cyclic order (123, 231, 312), -1 if the indices are acyclic (132, 213, 321), and zero if any pair of the indices are equal. See Newman [24] or Fossen [10] for the expansion of these equations. Due to body top-bottom and port-starboard symmetry, the vehicle added mass matrix reduces to: i 1 1 0 0 0 0 0 0 m22 0 0 0 m26 0 0 M3 3 0 M 3 5 0 (4.13) 0 0 0 M4 4 0 0 0 0 M 5 3 0 M 5 5 0 0 M6 2 0 0 0 M 6 6 which is equivalent to: Xn 0 0 0 0 0 0 Y, 0 0 0 N, 0 0 Zb 0 Mb 0 0 0 0 Kp 0 0 0 0 Z4 0 M 4 0 0 Y 0 0 0 N. Substituting these remaining terms into the expanded equations for fluid forces and moments from Equation 4.12 yields the following equations: XA = Xa + Zjwq + Z4q2 - Yvr -Yt2 YA =Y) +Y + Xjur - Zwwp - Z 4pq ZA = Z + Z4 - Xuq +Yvp +Yrp (4.15) KA = Kpp MA = Mbh + M44 - (Zli, - XA)uw - Yvp + (Kp - NI)rp - Zquq NA = Nbi+ Ne - (X, -Yo)uv+ Z4 wp - (K - M4)pq +Yur 4.3.1 Axial Added Mass To estimate axial added mass, we approximate the vehicle hull shape by an ellipsoid for which the major axis is half the vehicle length 1, and the minor axis half the vehicle diameter d. See Figure 2-4 for a comparison of the two shapes. Blevins [6, p.407] gives the following empirical formula for the

---

## Page 54

系数： KpIpi = Y"VV-rma (4.11) 这充其量只是实际值的粗略近似。最好使用实验数据。 根据这一粗略估算，请参见表 C.3 中的系数值。 4.3 添加的质量 附加质量是车辆加速时移动水质量的量度。理想液体的力和力矩可以用以下方程表示： F =  -im ji - ejk1Uiikm1i M i = -n im j± s i - eFk1Uiikm1+3,i - Ejk1UkUimii (4.12) where i=1,2,3,4,5,6 and jkl=1,2,3 其中，交替张量 Ejkl 在指标为循环顺序（123、231、312）时等于 +1，在指标 为非循环顺序（132、213、321）时等于 -1，如果任意一对指标相等则为零。有 关这些方程的展开，请参见 Newman [24] 或 Fossen [10]。 由于车体纵向和左右对称，车辆附加质量矩阵减少 收件人： i 1 1 0 0 0 0 0 0 m22 0 0 0 m26 0 0 M3 3 0 M 3 5 0 (4.13) 0 0 0 M4 4 0 0 0 0 M 5 3 0 M 5 5 0 0 M6 2 0 0 0 M 6 6 相当于： Xn 0 0 0 0 0 0 Y, 0 0 0 N, 0 0 Zb 0 Mb 0 0 0 0 Kp 0 0 0 0 Z4 0 M 4 0 0 Y 0 0 0 N. 将这些剩余项代入方程 4.12 中流体力和力矩的展开方程，得到以下方程： XA = Xa + Zjwq + Z4q2 - Y vr -Yt2 YA =Y) +Y + Xjur - Zwwp - Z 4pq ZA = Z + Z4 - Xuq +Yvp + Yrp (4.15) K A  = Kpp MA = M b h  + M 44 - (Zli, - XA)uw  - Yvp + (Kp - N I)rp - Zquq NA = N b i +  Ne - (X, -Yo)uv+ Z4 wp - (K - M4)pq + Yur 4.3.1  轴向附加质量 为了估算轴向附加质量，我们将车辆船体形状近似为一个椭球体，其长轴为车辆长度的一半 1, ，短轴为车辆直径的一半 d. 。有关两种形状的比较，请参见图 2-4。Blevins [6, 第407页] 给出了 以下经验公式用于

---

## Page 55

axial added mass of an ellipsoid: X = -m 11 - 4a pi ( I) ( 2 4Xpr ( =3 (4.16) (4.17) where p is the density of the surrounding fluid, and a and / are empirical parameters measured by Blevins and determined by the ratio of the vehicle length to diameter as shown in Table 4.1. Table 4.1: Axial Added Mass Parameters a and # l/d a #3 0.01 - 0.6348 0.1 6.148 0.6148 0.2 3.008 0.6016 0.4 1.428 0.5712 0.6 0.9078 0.5447 0.8 0.6514 0.5211 1.0 0.5000 0.5000 1.5 0.3038 0.4557 2.0 0.2100 0.4200 2.5 0.1563 0.3908 3.0 0.1220 0.3660 5.0 0.05912 0.2956 7.0 0.03585 0.2510 10.0 0.02071 0.2071 See Table C.5 for the final coefficient values. 4.3.2 Crossflow Added Mass Vehicle added mass is calculated using strip theory on both cylindrical and cruciform hull cross sections. From Newman [24], the added mass per unit length of a single cylindrical slice is given as: ma(x) = 7rpR(X) 2 (4.18) where p is the density of the surrounding fluid, and R(x) the hull radius as a function of axial position as given by Equations 2.1 and 2.2. The added mass of a circle with fins is given in Blevins [6] as: maf (X) = 7rp ain - R(x) 2 + 2 ) afin (4.19) where afin, as defined in Table 2.2, is the maximum height above the centerline of the vehicle fins. Integrating Equations 4.18 and 4.19 over the length of the vehicle, we arrive at the following

---

## Page 56

椭球的轴向附加质量： X = -m 11 - 4a p i ( I) ( 2 4Xpr ( =3 (4.16) (4.17) 其中 p 是周围流体的密度，a 和 / 是 Blevins 测量的经验参数，并由车辆长度与直径的比值确定，如表 4.1 所示。 表 4.1：轴向附加质量参数 a 和 # l/d a #3 0.01 - 0.6348 0.1 6.148 0.6148 0.2 3.008 0.6016 0.4 1.428 0.5712 0.6 0.9078 0.5447 0.8 0.6514 0.5211 1.0 0.5000 0.5000 1.5 0.3038 0.4557 2.0 0.2100 0.4200 2.5 0.1563 0.3908 3.0 0.1220 0.3660 5.0 0.05912 0.2956 7.0 0.03585 0.2510 10.0 0.02071 0.2071 请参见表 C.5 获取最终系数值。 4.3.2 横流附加质量 车辆附加质量是通过对圆柱形和十字形船体横截面使用条带理论计算的。根据Newman [24]，单个圆柱切 片的单位长度附加质量给出如下： ma(x) = 7rpR(X) 2 (4.18) 其中 p 是周围流体的密度，R(x)  是轴向位置的船体半径函数，如方程 2.1 和 2.2 所示。带鳍圆的附加质量 在 Blevins [6] 中给出如下： m a f (X) = 7rp ain  - R(x) 2 + 2 ) afin (4.19) 其中 afin，如表 2.2 所定义，是车辆鳍片中心线以上的最大高度。对车辆长度上的方程 4.18 和 4.19 进行 积分，我们得到以下结果

---

## Page 57

equations for crossflow added mass: Y, = -M22 = - ja ma(x)dx - j maf(x)dx - j ma(x)dx It Xi fIf2 Z. = -ms3 = -M22 = Y f Xf2 - b2 M, = -M53 = Itxmna(x)dx - xma5 (x)dx - f~2xma(x)dx N= -m62=m=g 53 = (4.20) Y = -n 2 6 = -n 6 2 =Ni Z4 = -n3 5 = -m 53 = Me fi fIffin2 Zbow2 M4 = -m 5 5 - / X2 ima(x)dx Xx 2 maf(x)dx - / x 2 ma(x)dx tail fin Ifin2 N, = -n 6 6 = -M55 = M4 See Table A.2 for the limits of integration. See Table C.5 for the final coefficient values. 4.3.3 Rolling Added Mass To estimate rolling added mass, we will assume that the relatively smooth sections of the vehicle hull do not generate any added mass in roll. We will also neglect the added mass generated by the sonar transponder and any other small protuberances. Given those assumptions, we need only consider the hull section containing the vehicle control fins. Blevins [6] offers the following empirical formula for the added mass of a rolling circle with fins: K = pa 4dx (4.21) x fin 7 where a is the fin height above the vehicle centerline, in this case averaged to be 0.1172 m. See Table A.2 for the limits of integration. See Table C.5 for the final coefficient value. 4.3.4 Added Mass Cross-terms The remaining cross-terms result from added mass coupling, and are listed below: X.q = Zw Xqq= Z4 X, = -Yi, Xr = -Yi (4.22) Yu, = X. YwP = - Z YPq = -Z4 (4.23) Zuq = -X. Zu, = Y ZrP = Ye (4.24) Muwa = -(Zb - Xa ) M', = -Y Mrp = (Kp - N) Muq = -Z 4 (4.25) Nuva = -(Xi -Y,) N.p = Z4 Npq = -(K6 - M4) Nur =Y (4.26) The added mass cross-terms Muwa and Nuva are known as the Munk Moment, and relates to the pure moment experienced by a body at an angle of attack in ideal, inviscid flow. See Tables C.6, C.7 and C.8 for the final coefficient values. 4.4 Body Lift Vehicle body lift results from the vehicle moving through the water at an angle of attack, causing flow separation and a subsequent drop in pressure along the aft, upper section of the vehicle hull. This pressure drop is modeled as a point force applied at the center of pressure. As this center of

---

## Page 58

横流附加质量的方程： Y, = -M22 = - j a ma(x)dx - j m af(x)dx - j ma(x)dx It X i fIf2 Z. = -ms3 = -M22 = Y f X f2 - b2 M, = -M53 = Itxm na(x)dx - x m a 5  (x)dx - f~2xma(x)dx N= -m62=m=g 53 = (4.20) Y = -n 2 6 = -n 6 2 = N i Z4 = -n3 5 = -m 53 = Me fi fIffin2 Zbow2 M4 = -m 5 5 - / X2 ima(x)dx Xx 2 maf(x)dx - / x 2 m a (x )d x ta il fin Ifin2 N, = -n 6 6 = -M 55 = M4 参见表 A.2 了解积分的界限。 请参见表 C.5 获取最终系数值。 4.3.3  翻滚附加质量 为了估算横摇附加质量，我们将假设车辆船体的相对光滑部分不会在横摇中产生任何附加质量 。我们还将忽略声纳应答器和任何其他小型突起产生的附加质量。基于这些假设，我们只需要 考虑包含车辆控制鳍的船体部分。 Blevins [6] 提出了带鳍滚动圆的附加质量的以下经验公式： K = pa 4dx (4.21) x fin 7 其中 a 是鳍片相对于车辆中心线的高度，在本例中平均为 0.1172 米。积分的限制见表 A.2。 请参见表 C.5 以获取最终系数值。 4.3.4 添加了质量交叉项 剩余的 交叉项是由附加质量耦合产生的，并且已列出 以下 ：X.q = Zw Xqq= Z4 X, = -Yi, Xr = -Yi (4.22) Yu, =X. YwP = - Z YPq = -Z4 (4.23) Zuq = -X. Zu, = Y ZrP = Ye (4.24) Muwa = -(Z b - X a  )  M'， =  -Y Mrp = (Kp  - N) Muq = -Z 4 (4.25) Nuva = -(Xi -Y,) N .p  = Z4 N p q  = -(K6 - M4) N u r = Y (4.26) 附加质量交叉项 Muwa  和 Nuva  被称为孟克力矩，并且与理想无粘流中物体在迎角下经历的 纯力矩有关。 请参见表 C.6、C.7 和 C.8 以获取最终系数值 . 4.4  车身提升 车辆车身升力源自车辆以迎角穿过水面移动，导致流动分离，并在车辆船体的尾部上方区域产 生随之而来的压力下降。这种压力下降被建模为作用于压力中心的点力。随着这个压力中心的

---

## Page 59

pressure does not line up with the origin of the vehicle-fixed coordinate system, this force also leads to a pitching moment about the origin. In determining the best method for calculating body lift, the author compared three empirical methods based on torpedo data [7, 9, 16], and one theoretical method [23]. Unfortunately, the estimates for body lift from the four methods ranged over an order of magnitude. Given the lack of agreement between the empirical methods, it would be preferable to base the body lift estimates on actual REMUS data, from perhaps tow tank tests or measurements of the vehicle mounted on a rotating arm. Until that happens, the author decided to use Hoerner's estimates [16], which appeared the most reliable. 4.4.1 Body Lift Force To calculate body lift, we will use the empirical formula developed by Hoerner [16], which states: Lbody = 1 2 cdu (4.27) where p is the density of the surrounding fluid, Ay the projected area of the vehicle hull, u the vehicle forward velocity, and cyd the body lift coefficient, which by Hoerner's notation is expressed as: Cyd = Cyd(/) = dc (4.28) d3 where # is the vehicle angle of attack in radians and is given by the relationship: tan 3 = - > #3- (4.29) U U Hoerner gives the following relationship for lift slope: dcod cyY= cy (4.30) where I is the vehicle length and d the maximum diameter. Hoerner [16, pg. 13-3] states that for 6.7 < <10, c = 0.003 (4.31) Note that in Equation 4.30 it is necessary to convert the Hoerner lift slope coefficients cyd/3 and c' from degree to radians. This results in the Hoerner lift slope coefficient cyd, defined in terms of radians as follows: 18 cyd, = cydI3 (180) (4.32) Substituting into Equation 4.27 the relationships given above, we are left with the following equation for vehicle body lift: Lbody p 2Cydgu (4.33) which results in the following body lift coefficients: 1 YUV = ZUWl = pd2cyd3 (4.34) See Table C.4 for the final coefficient values.

---

## Page 60

压力没有与车辆固定坐标系的原点对齐，这个力也会导致绕原点的俯仰力矩。 在确定计算机体升力的最佳方法时，作者比较了三种基于鱼雷数据的经验方法 [7, 9, 16] 和一种理论方 法 [23]。不幸的是，四种方法的机体升力估计值差异达一个数量级。鉴于经验方法之间缺乏一致性，最好 根据实际的 REMUS 数据来估算机体升力，可能来自拖曳水槽试验或测量安装在旋臂上的车辆。 在那之前，作者决定使用 Hoerner 的估算 [16]，因为它看起来最可靠。 4.4.1  车身升力 为了计算机体升力，我们将使用 Hoerner [16] 提出的经验公式，其内容如下： Lbody = 1 2 c d u (4.27) 其中 p 为周围流体的密度，Ay  为船体的投影面积，u  为车辆的前进速度，cyd  为车身升力系数，根据 Ho erner 的表示法表示为： Cyd = Cyd(/) = dc (4.28) d3 哪里  #  is the vehicle angle of attack in radians and is given by the relationship: tan 3 = - > #3- (4.29) U U Hoerner 给出了升力斜率的以下关系式： dcod cyY = cy (4.30) 其中 I 是车辆长度，d  是最大直径。Hoerner [16，第 13-3 页] 说明 for 6.7 < < 1 0 , c = 0.003 (4.31) 注意，在方程 4.30 中，有必要将 Hoerner 升力斜率系数 cyd/3  和 c' 从度转换为弧度。这导致了以弧度为单 位定义的 Hoerner 升力斜率系数 cyd, ，如下所示： 18 cyd, = cydI3 (180) (4.32) 将上述给出的关系代入方程 4.27 后，我们得到车辆车身升力的以下方程： Lbody p 2Cydgu (4.33) 这导致了以下车身升力系数： 1 YUV = ZUWl = pd2cyd3 (4.34) 请参见表 C.4 以获取最终系数值。

---

## Page 61

4.4.2 Body Lift Moment Hoerner estimates that for a body of revolution at an angle of attack, the viscous force is centered at a point between 0.6 and 0.7 of the total body length from the nose. His experimental findings suggest that the flow goes smoothly around the forward end of the hull, and that the lateral force only develops on the leeward side of the rear half of the hull. Following these findings, we will assume that, in body-fixed coordinates: xcp = -0. 6 51 - xzero (4.35) This results in the following equation for body lift moment: = -pd2cydoxcp (4.36) See Table C.4 for the final coefficient values. 4.5 Fin Lift The attitude of the REMUS vehicle is controlled by two horizontal fins, or stern planes, and two vertical fins, or rudders. The pairs of fins move together; in other words the stern planes do not move independently of each other, nor do the rudder planes. For the vehicle control fins, the empirical formula for fin lift is given as: T 1 =2 PCLSfinVe (4.37) Min = XfinLfin where CL is the fin lift coefficient, Sfi the fin planform area, Jc the effective fin angle in radians, ve the effective fin velocity, and Xfin the axial position of the fin post in body-referenced coordinates. Fin lift coefficient CL is a function of the effective fin angle of attack a. Hoerner [16, pg. 3-2] gives the following empirical formula for fin lift as a function of a in radians: dc, dcj+ [_1 (4.38) da, [2a7r (ARe) where the factor a was found by Hoerner to be of the order 0.9, and (ARe) is the effective fin aspect ratio, which is given by the formula: ARe = 2(AR) = 2 " (4.39) As the fin is located at some offset from the origin of the vehicle coordinate system, it experiences the following effective velocities: Ufin = u + Zfinq - yfinr Vfin = V + Xfinr - Zfinp (4.40) Wfin = W + YfinP - Xfinq where Xfin, yfin, and Zfin are the body-referenced coordinates of the fin posts. For the REMUS vehicle, we will drop the terms involving Yfin and Zfin as they are small compared to the vehicle translational velocities. The effective fin angles Jse and ire can be expressed as ire = 6r - Ore (4.41) ise = Js + /se

---

## Page 62

4.4.2  车身提升力矩 Hoerner 估计，对于一个有攻角的旋转体，粘性力的作用点位于从鼻端起到整个机体长度的 0.6 到 0.7 之间。他的实验结果表明，流体在船体前端能够顺畅流动，并且横向力只在船体后半部 分的背风侧产生。 根据这些发现，我们将假设在身体固定坐标中： xcp = -0. 6 51 - xzero (4.35) 这就导致了以下公式用于车体升力力矩： = -pd2cydoxcp (4.36) 请参见表 C.4 获取最终系数值。 4.5 鳍状升力 REMUS 车辆的姿态由两个水平鳍翼（或尾舵面）和两个垂直鳍翼（或方向舵）控制。这对鳍翼 会一起移动；换句话说，尾舵面不会互相独立移动，舵面也不会独立移动。 对于车辆控制鳍，鳍升力的经验公式给出如下： T 1 =2 PCLSfinVe (4.37) Min =  XfinLfin 其中 CL  是鳍升力系数，Sfi  是鳍的平面面积，Jc 是以弧度表示的有效鳍角，ve 是有效鳍速度， Xfin  是以机身参考坐标表示的鳍柱轴向位置。 鳍升力系数 CL  是有效鳍攻角 a 的函数。Hoerner [16，第 3-2 页] 给出了鳍升力作为 a（以弧 度计）函数的以下经验公式： dc, dcj+ [_1 (4.38) da, [2a7r (ARe) 其中因子 a 被 Hoerner 发现大约为 0.9，(ARe) 是有效鳍展长宽比，其由以下公式给出： ARe = 2(AR) = 2 " (4.39) 由于鳍位于车辆坐标系原点的某个偏移位置，它会经历以下有效速度： Ufin = u + Zfinq - yfinr Vfin = V + Xfinr - Zfinp (4 .4 0 ) Wfin = W +  YfinP - Xfinq 其中 Xfin, yfin,  和 Zfin  是鱼鳍支柱的车体参考坐标。对于 REMUS 车辆，我们将忽略涉及 Yfin 和 Zfin  的项，因为它们相比车辆平移速度很小。 有效鳍角 Jse  和 ire  可以表示为 ir e  = 6r - Ore (4.41) is e  = J s + /se

---

## Page 63

where J, and Jr are the fin angles referenced to the vehicle hull, ,se and 0,e the effective angles of attack of the fin zero plane, as shown in Figures 4-1 and 4-2. Assuming small angles, these effective angles can be expressed as: Ole = V 1n (V + onr) Ufin U (4.42) /se -- Wfi ~ ~ ~ Xfinq) fin based on Equation 4.40 U x r ue y Vfluid ,vi Figure 4-1: Effective Rudder Angle of Attack x U Pe 0 Vfluid ' "in Figure 4-2: Effective Stern Plane Angle of Attack Substituting the results of Equations 4.40, 4.41 and 4.42 into Equation 4.44 results in the following equations for fin lift and moment: 1 Y, = pctSfin [U 26, - UV - Xfn (Ur)] Z = - pcLaSfin [U 26 + uw - xfin (uq(4 1 22,(4.43) M,=2PCLaSfinxfin [U + UW -Xfin u) 1 N, = 1pcLaSfinxfin [U 2 6, ~ U - nXfn (Ur)] Finally, we can separate the equation into the following sets of fin lift coefficients: Yuu6, =-Yuv5 = PCLaSfin Zuus, Zuw5 = -pCLSfln (4.44) Yur= -Zuqf = -PCLaSfinXfin and fin moment coefficients: Muu,= Muwf = PCLaSfinXfin Nuus, -Nuvf = pcLaSfinxfin (4.45) Muqf Nurf -PCLaSfinXin

---

## Page 64

其中 J 和 Jr  是相对于飞行器机体的鳍角，,se  和 0,e  是鳍零平面的有效攻角，如图 4-1 和 4-2 所示。假设 角度较小，这些有效角度可以表示为： Ole = V 1n (V + onr) Ufin U (4.42) /se -- W fi ~ ~ ~ Xfinq) fin 基于方程 4.40 U x r ue y Vfluid ,vi 图 4-1：有效舵角攻角 x U Pe 0 Vfluid ' "in 图 4-2：有效尾舵平面攻角 将方程 4.40、4.41 和 4.42 的结果代入方程 4.44 得到叶片升力和力矩的以下方程： 1 Y, = p c t S f i n  [U26, - UV - Xfn (U r)] Z = - p cL a S fin  [U26 + uw  - xfin (uq(4 1 22,(4.43) M ,= 2PC LaSfinxfin [U + UW -X fin u) 1 N, = 1pcLaSfinxfin [U 2 6, ~ U - nXfn (Ur)] 最后，我们可以将该方程分解为以下几组鳍升力系数： Yuu6, =-Yuv5 = P C L aSfin Zuus, Zuw5 = -pC LSfln (4.44) Yur= -Z u q f = -PC LaSfinXfin 和鳍端力矩系数： M u u ,=  M uwf = PCLaSfinXfin Nuus, -Nuvf = pcLaSfinxfin (4.45) M u q f N u rf -PCLaSfinXin

---

## Page 65

See Table C.10 for the final coefficient values. 4.6 Propulsion Model We will use a very simple model for the REMUS propulsion system, which treats the propeller as a source of constant thrust and torque. The values for these coefficients are derived from both vehicle design-stage propeller bench tests conducted by Ben Allen at the Oceanographic Systems Laboratory, and from experiments at sea conducted by the author. This simple model is acceptable for small amplitude perturbations about the vehicle steady state. If examination of the simulator output indicates that a more sophisticated model is necessary, we can try replacing this with a propeller model, such as Yoerger and Slotine's [35], or with experimentally- derived values. 4.6.1 Propeller Thrust In tests at sea, the REMUS vehicle has been observed to maintain a forward speed of 1.51 m/s (3 knots) at a propeller speed of 1500 RPM. We will assume that at this steady velocity, the propeller thrust matches the vehicle axial drag. Xprop = -X[IU Jul (4.46) =-2.28Xulu For the purpose of simulation, we will assume that the vehicle makes only small deviations from this forward speed. See Table C.9 for the final coefficient value. 4.6.2 Propeller Torque In sea trials, the REMUS vehicle running at 1500 RPM in steady conditions and zero pitch angle was observed to maintain an average roll offset 4 of -5.3 degrees (-9.3 x 10-2 radians). We will assume that under these conditions, the propeller torque matches the hydrostatic roll moment. Kprop = -KHS = (ygW - ybB) cos cos + (zgW - ZbB) cos0sin$ (4.47) = 0.995(ygW - ybB) - 0.093(zgW - ZbB) See Table C.9 for the final coefficient value. 4.7 Combined Terms Combining like terms from Equations 4.22, 4.34, 4.36, 4.44 and 4.45, we get the following: Yu = Yuvi + Yuvf Yur = Yura + Yurf ZUW = ZUW1 + Z 5 Zuq = Zuqa + Zuqf Muw = Muwa + Muwl + Muwf Muq = Muqa + Muqf Nv = Nuva + Nuvl + Nuvf Nur = Nura + Nurf 4.8 Total Vehicle Forces and Moments Combining the coefficient equations for the vehicle

---

## Page 66

See Table C.10 for the final coefficient values. 4.6 推进模型 我们将为 REMUS 推进系统使用一个非常简单的模型，该模型将螺旋桨视为恒定推力和扭矩的 源。这些系数的数值来自 Ben Allen 在海洋系统实验室进行的车辆设计阶段螺旋桨试验，以及作 者在海上进行的实验。 这个简单的模型对于车辆稳态下的小幅扰动是可接受的。如果对模拟器输出的检查表明需要 更复杂的模型，我们可以尝试用螺旋桨模型替代，比如 Yoerger 和 Slotine 的模型 [35]，或者使 用实验获得的数值。 4.6.1 螺旋桨 推力 在海上测试中，已观察到 REMUS 车辆在螺旋桨转速为 1500 RPM 时能够保持 1.51 m/s（3 节） 的前进速度。我们将假设在这种稳定速度下，螺旋桨推力与车辆的轴向阻力相匹配。 Xprop = -X [IU  Jul (4.46) =-2.28Xulu 为了模拟的目的，我们将假设车辆仅在此前进速度上产生小的偏差。最终系数值见表 C.9。 4.6.2 螺旋桨扭矩 在海上试验中，REMUS 车辆在稳定条件下以 1500 转/分钟运行 且俯仰角为零时，被观察到保持平均横滚偏移 4 of -5.3 degrees (-9.3 x 10-2 radians). We will assume that under these conditions, the propeller torque matches the hydrostatic roll moment. Kprop = -KHS = (ygW  - ybB) cos cos + (zgW - ZbB) cos0sin$ (4.47) = 0.995(ygW  - ybB) - 0.093(zgW  - ZbB) 请参见表 C.9 获取最终系数值。 4.7  组合条款 将方程 4.22、4.34、4.36、4.44 和 4.45 中的同类项结合起来，我们得到如下结果： Yu = Yuvi +  Yuvf Yur = Yura + Yurf ZUW = ZUW1 + Z 5 Zuq = Zuqa + Zuqf Muw = Muwa + Muwl + M u w f Muq = Muqa + Muqf N v  = Nuva + Nuvl + Nuvf Nur = N ura + Nurf 4.8 总车辆力和力矩 结合车辆的系数方程

---

## Page 67

* Hydrostatics: Equation 4.3 " Hydrodynamic Damping: Equations 4.6, 4.8 and 4.11 " Added Mass: Equations 4.16, 4.20, 4.21 and 4.22 " Body Lift and Moment: Equations 4.34 and 4.36 " Fin Lift and Moment: Equations 4.44 and 4.45 " Propeller Thrust and Torque: Equations 4.46 and 4.47 the sum of the depth-plane forces and moments on the vehicle can be expressed as: Z Xext =XHS + Xuiu u UI + Xi,6 + Xwqwq + Xqqqq + Xvrvr + Xrrr + Xprop 3 Yxt =YHS + Yv~vjv vI + YrIrir |r| Y+Y + Y; + Yurur + YwpP + Ypqpq + Yuvuv + YuuS,u 2 6r > Zext =ZHS + Zwlw.w WI + Zqlqq Iql + ZG + Z q$ + Zuquq + Z pvp + Zrprp + Zuwuw + ZUUs6u 26 (4.49) ( Kext =KHS + KpIpIp IpI + K1p + Kprop SMext =MHS + Mw1 .1 w IwI + Mqjqjq IqI ± Mmii, + M44 + Muquq + M pvp + Mrprp + Muw uw + MUU5 u 26s ( Next =NHS + Nv1 Iv |VI + Nrjrjr Ir + Ni9 + Ni r + Nurur + N, pwp + Npqpq + Novuv + NuuSU 2 6r See Tables 4.2 and 4.3 for a list of the non-zero vehicle coefficients.

---

## Page 68

* Hydrostatics: 方程 4.3 Hydrodynamic Damping:  方程 4 .6、4.8 和 4.11 Added Mass:  方程 4.16、4.20、4.21 和 4.22 Body Lift and Moment:  方程 4.34 和 4.36 Fin Lift and Moment:  方程 4.44 和 4.45 Propeller Thrust and Torque:  方程 4.46 和 4.47 车辆上的深度平面力和力矩的总和可以表示为： Z Xext =XHS + X uiu u UI + Xi,6 + Xwqwq + Xqqqq + Xvrvr + X r r r + Xprop 3 Yxt =YHS + Yv~vjv vI + YrIrir |r| Y+Y + Y; + Yurur + Yw pP + Ypqpq + Yuvuv + YuuS,u 2 6r > Zext = Z H S  + Zwlw.w WI + Zqlqq Iql + ZG + Z q$ + Zuquq + Z pvp + Zrprp + Zuwuw + ZUUs6u 26 (4.49) ( Kext =KHS + KpIpIp IpI + K1p + Kprop SMext =MHS + Mw1 .1 w IwI + Mqjqjq IqI ± Mmii, + M44 + Muquq + M pvp + Mrprp + Muw uw + MUU5 u 26s ( Next =NH S + Nv1 Iv |VI + Nrjrjr Ir + Ni9 + Ni r + N urur + N, pwp + Npqpq + Novuv + NuuSU 2 6r 请参见表 4.2 和 4.3，了解非零车辆系数的列表 系数。

---

## Page 69

Table 4.2: STD REMUS Non-Linear Table 4.3: STD REMUS Non-Linear Units kg - m2/rad' kg - m2 /rad N.m kg kg- m2/rad2 kg kg - m kg -m2 /rad kg. m/rad kg. m/rad kg- m2/rad2 kg/rad kg kg -m2/rad2 kg kg - m kg -m 2/rad kg m/rad kg. m/rad kg- m2/rad2 kg/rad Maneuvering Coefficients: Moments Description Rolling Resistance Added Mass Propeller Torque Cross-flow Drag Cross-flow Drag Body and Fin Lift and Munk Moment Added Mass Added Mass Added Mass Cross Term and Fin Lift Added Mass Cross Term Added Mass Cross-term Fin Lift Moment Cross-flow Drag Cross-flow Drag Body and Fin Lift and Munk Moment Added Mass Added Mass Added Mass Cross Term and Fin Lift Added Mass Cross Term Added Mass Cross-term Fin Lift Moment Parameter K,, K, Kprop M.. Mqq M. Me M4p M., M,, Nur N,, NuN., Ni, Ns, N., N,4 Nuudr Value -1. 30e-003 -1. 41e-002 -5.43e-001 +3.18e+000 -9.40e+000 +2.40e+001 -1. 93e+000 -4.88e+000 -2.00e+000 -1. 93e+000 +4.86e+000 -6.15e+000 -3.18e+000 -9.40e+000 -2.40e+001 +1. 93e+000 -4.88e+000 -2. 00e+000 -1. 93e+000 -4.86e+000 -6.15e+000 Parameter XutL xuu X., Xwq Xqq Xvr Xrr Xprop Yvv Yrr Yu v Yi, Yr Y. YvP Yp q Yuudr zW Zqq zwb Z4 Zuq ZP Zrp Zuuds Value -1.62e+000 -9.30e-001 -3.55e+001 -1. 93e+000 +3.55e+001 -1.93e+000 +3.86e+000 -1.31e+002 +6. 32e-001 -2.86e+001 -3.55e+001 +1. 93e+000 +5.22e+000 +3.55e+001 +1. 93e+000 +9.64e+000 -1.31e+002 -6.32e-001 -2.86e+001 -3.55e+001 -1. 93e+000 -5.22e+000 -3.55e+001 +1. 93e+000 -9.64e+000 Units kg/m kg kg/rad kg -m/rad kg/rad kg -m/rad N kg/m kg - m/rad2 kg/m kg kg -m/rad kg/rad kg/rad kg -m/rad kg/(m - rad) kg/m kg -m/rad2 kg/m kg kg -m/rad kg/rad kg/rad kg/rad kg/(m - rad) Maneuvering Coefficients: Forces Description Cross-flow Drag Added Mass Added Mass Cross-term Added Mass Cross-term Added Mass Cross-term Added Mass Cross-term Propeller Thrust Cross-flow Drag Cross-flow Drag Body Lift Force and Fin Lift Added Mass Added Mass Added Mass Cross Term and Fin Lift Added Mass Cross-term Added Mass Cross-term Fin Lift Force Cross-flow Drag Cross-flow Drag Body Lift Force and Fin Lift Added Mass Added Mass Added Mass Cross-term and Fin Lift Added Mass Cross-term Added Mass Cross-term Fin Lift Force

---

## Page 70

标签第 4.2 节：STD REMUS 非线性 表 4.3：STD REMUS 非线性 Units kg - m2/rad' kg - m2 /rad N.m kg kg- m2/rad2 kg kg - m kg -m2 /rad kg. m /rad kg. m /rad kg- m2/rad2 kg/rad kg kg - m 2 /ra d 2 kg kg - m kg -m 2/rad kg m /rad kg. m /rad kg- m2/rad2 kg/rad 操纵系数：力矩 Description Rolling Resistance Added Mass Propeller Torque Cross-flow Drag Cross-flow Drag Body and Fin Lift and Munk Moment Added Mass Added Mass Added Mass Cross Term and Fin Lift Added Mass Cross Term Added Mass Cross-term Fin Lift Moment Cross-flow Drag Cross-flow Drag Body and Fin Lift and Munk Moment Added Mass Added Mass Added Mass Cross Term and Fin Lift Added Mass Cross Term Added Mass Cross-term Fin Lift Moment Parameter K,, K, K prop M.. Mqq M. Me M4p M., M,, N ur N,, NuN., Ni, Ns, N., N,4 N u u d r Value -1. 30e-003 -1. 41e-002 -5.43e-001 +3.18e+000 -9.40e+000 +2.40e+001 -1. 93e+000 -4.88e+000 -2.00e+000 -1. 93e+000 +4.86e+000 -6.15e+000 -3.18e+000 -9.40e+000 -2.40e+001 +1. 93e+000 -4.88e+000 -2. 00e+000 -1. 93e+000 -4.86e+000 -6.15e+000 Parameter XutL xuu X., Xwq Xqq X vr Xrr Xprop Yvv Yrr Yu v Yi, Yr Y. YvP Yp q Yuudr zW Zqq zwb Z4 Zuq ZP Z rp Zuuds Value -1.62e+000 -9.30e-001 -3.55e+001 -1. 93e+000 +3.55e+001 -1.93e+000 +3.86e+000 -1.31e+002 +6. 32e-001 -2.86e+001 -3.55e+001 +1. 93e+000 +5.22e+000 +3.55e+001 +1. 93e+000 +9.64e+000 -1.31e+002 -6.32e-001 -2.86e+001 -3.55e+001 -1. 93e+000 -5.22e+000 -3.55e+001 +1. 93e+000 -9.64e+000 Units kg/m kg kg/rad kg -m /rad kg/rad kg -m /rad N kg/m kg - m/rad2 kg/m kg kg -m/rad kg/rad kg/rad kg -m/rad kg/(m - rad) kg/m kg -m /rad 2 kg/m kg kg -m/rad kg/rad kg/rad kg/rad kg/(m - rad) 机动系数 : 力量 Description Cross-flow Drag Added Mass Added Mass Cross-term Added Mass Cross-term Added Mass Cross-term Added Mass Cross-term Propeller Thrust Cross-flow Drag Cross-flow Drag Body Lift Force and Fin Lift Added Mass Added Mass Added Mass Cross Term and Fin Lift Added Mass Cross-term Added Mass Cross-term Fin Lift Force Cross-flow Drag Cross-flow Drag Body Lift Force and Fin Lift Added Mass Added Mass Added Mass Cross-term and Fin Lift Added Mass Cross-term Added Mass Cross-term Fin Lift Force

---

## Page 71

Chapter 5 Vehicle Tow Tank Experiments In April through June of 1999, the author collaborated with Ben Allen from WHOI's Oceanographic Systems Lab on a series of tow tank experiments with a full-scale REMUS vehicle [3]. These experiments were intended to measure the vehicle axial drag coefficient and the thrust of the vehicle propeller, and to assist in estimating the overall efficiency of the vehicle propulsion system. The experiments involved recording axial and lateral drag data for a range of vehicle speeds and hull configurations, as well as thrust data from bollard pull tests for a range of propeller speeds. These experiments provided the author with an opportunity to experimentally measure the vehicle axial drag coefficient. 5.1 Motivation One of the more important attributes of any AUV is its endurance, or the range and speed that the vehicle has available to accomplish its mission. An increase in propulsion system efficiency corresponds to a longer range for a given speed, or the ability to cover the same distance in a reduced time. Any efforts to improve the overall efficiency will result in a more useful vehicle. REMUS is a low-cost, man-portable AUV design with approximately 1000 hours of water time over hundreds of missions on 10 vehicles [31, 30]. The vehicle design has been very successful in demonstrating the usefulness of AUVs in the ocean [28], however it is limited in its range and speed [2]. The existing design system used model airplane propellers with a DC brush motor, propeller shaft and shaft seal. A recent design effort entailed modifications to this design to provide significantly greater propulsion performance. It is not possible to determine the difference between effects of hull drag coefficient and propeller efficiency in open water vehicle tests when neither the actual vehicle drag coefficient nor propeller efficiencies are known. Therefore the first step in the design process entailed quantifying the sources of drag in a tow-tank on an existing vehicle, and then determining what improvements were possible. 5.2 Laboratory Facilities and Equipment The experiments were conducted at the University of Rhode Island Tow Tank, located in the Sheets Building on the Narragansett Bay Campus. The URI tow tank, which was filled with fresh water, is approximately 30 meters long by 3.5 meters wide by 1.5 meters deep (100 by 12 by 5 feet). The tow tank carriage had a useful run of almost 21 meters (70 feet). See Figure 5-1 for a diagram of the tow tank layout, and Figure 5-2 for a picture of the tank. Given the large size of the tank relative to the vehicle, we were able to use an actual REMUS vehicle during the tests, rather than a scale model. The vehicle was suspended in the water by a faired strut, which was connected to the towing carriage by the bottom plate of a flexural mount. See Figure 5-3 for a diagram of the carriage setup and vehicle mounting, and Figure 5-4 for a photo of the vehicle on the strut.

---

## Page 72

第5章 车辆拖曳坦克实验 在1999年4月至6月期间，作者与WHOI海洋系统实验室的Ben Allen合作，进行了一系列使用全尺寸REMU S车辆的游泳池实验[3]。这些实验旨在测量车辆的轴向阻力系数和推进器的推力，并帮助估算车辆推进系 统的整体效率。实验涉及记录一系列车辆速度和船体配置下的轴向和横向阻力数据，以及一系列推进器速 度下的系缆拉力测试推力数据。这些实验为作者提供了一个机会，来实验性地测量车辆的轴向阻力系数。 5.1 动机 任何自主水下航行器（AUV）更重要的特性之一是其续航能力，即该车辆完成任务时可用的航程和速度 。推进系统效率的提高意味着在给定速度下航程更长，或能够在更短时间内覆盖相同距离。任何提高整体 效率的努力都将使车辆更实用。 REMUS 是一种低成本、可人工携带的自动水下航行器（AUV）设计，经过 10 台设备在数百次任务中 累计约 1000 小时的水下使用时间 [31, 30]。该车辆设计在展示 AUV 在海洋中的实用性方面非常成功 [28] ，然而其航程和速度有限 [2]。现有设计系统使用模型飞机螺旋桨配合直流有刷电机、螺旋桨轴和轴封。 最近的一次设计工作对该设计进行了修改，以提供显著更高的推进性能。 当既不知道实际的车辆阻力系数也不知道螺旋桨效率时，在公开水域的车辆测试中无法确定船体阻力 系数和螺旋桨效率的影响差异。因此，设计过程的第一步是量化现有车辆在拖曳水槽中的阻力来源，然后 确定可能的改进措施。 5.2 实验室设施与设备 实验在罗德岛大学纳拉甘西特湾校区的Sheets大楼内的牵引水槽进行。罗德岛大学的牵引水槽注满了淡水 ，尺寸约为30米长、3.5米宽、1.5米深（100 x 12 x 5英尺）。水槽的牵引车的有效行程几乎为21米（70英 尺）。有关水槽布局的示意图，请参见图5-1；水槽的照片请参见图5-2。 考虑到水槽相对于车辆的较大尺寸，我们能够在测试中使用实际的REMUS车辆，而不是比例模型。车 辆通过一个流线型支撑架悬浮在水中，该支撑架通过挠性支座的底板连接到拖曳车上。有关拖曳车设置和 车辆安装的示意图，请参见图5-3；有关车辆在支撑架上的照片，请参见图5-4。

---

## Page 73

Tow tank carriage with REMUS vehicle suspended from flexural mount Data Station with carriage controls, strip-chart recorder and DAQ-equipped laptop PC Figure 5-1: URI Tow Tank Layout 5.2.1 Flexural Mount The flexural mount was a box consisting of two parallel, horizontal plates connected by flat vertical springs. The springs allowed the lower plate to move in the horizontal plane. The motion of plate relative to the carriage was measured with two orthogonally-mounted linear variable differential transformers (LVDTs), electromechanical transducers which converted the rectilinear motion of the plate along each horizontal axis into corresponding electrical signals. The LVDT output signals were amplified and electronically filtered, then transmitted to the data station where they were plotted on a strip chart recorder and sampled by an analog-to-digital board connected to a laptop PC. We were able to calibrate the axially-mounted LVDT to a significantly greater level of accuracy than the laterally-mounted instrument, due to the poor condition of the latter. As such, we only used the laterally-mounted LVDT for gross measurements of lateral drag, as an indicator of strut, vehicle or fin misalignment. 5.2.2 Tow Tank Carriage The tow tank carriage was a large flat cart with hard rubber wheels driven by an electric motor. Instead of rails, the carriage rolled along the flat tops of the tank walls. See Figure 5-5 for a picture of the tow tank carriage. The desired carriage speed was set by a rheostat at the data station. A simple motor controller measured the carriage speed using an encoder wheel and light sensor mounted on the axle of the motor shaft. On forward runs, the carriage was stopped when a protruding trigger switch was thrown by a flange mounted on the tank wall. On backing up, the cart was stopped only by the alert operators stabbing at the motor kill switch mounted at the data station. The speed at which we operated the carriage was limited more by the length of the tow tank than by the torque of the carriage motor. Our maximum speed was roughly 1.5 meters per second or 3 knots, the operating speed of the vehicle. At that velocity, the strut vibrations generated by the impulsive start took several seconds to damp out, leaving us with only a few seconds of useful data before the carriage began decelerating. The actual carriage speed was measured using a laser range finder mounted at the far end of the tank. The range finder, a Nova Ranger NR-100, did not measure time-of-flight; instead, it was calibrated to measure distance based on the location of the projected dot. For a given distance, the instrument output a corresponding voltage. The analog range finder signal was transmitted to the data station, where it too was sampled by the laptop PC's analog-to-digital board. Both digital signals were logged with data acquisition software, then processed with MATLAB. 5.3 Drag Test Experimental Procedure The drag test experimental procedure involved the following steps:

---

## Page 74

Tow tank carriage with REMUS vehicle suspended from flexural mount Data Station with carriage controls, strip-chart recorder and DAQ-equipped laptop PC 图 5-1：URI 拖车油箱布局 5.2.1 弯曲安装 挠性支座是一个由两个平行的水平板组成的盒子，这两个水平板通过平直的垂直弹簧连接。弹 簧允许下板在水平平面内移动。板相对于小车的运动通过两个正交安装的线性可变差动变压器 （LVDT）进行测量，这种机电换能器将板沿每个水平轴的直线运动转换为相应的电信号。 LVDT 输出信号被放大并进行电子滤波，然后传输到数据站，在那里它们被绘制在条形图记 录器上，并通过连接到笔记本电脑的模拟到数字转换板进行采样。 由于后者状况不佳，我们能够将轴向安装的 LVDT 校准到比横向安装仪器显著更高的精度。 因此，我们仅将横向安装的 LVDT 用于侧向阻力的粗略测量，作为支柱、车辆或鳍片错位的指 示。 5.2.2  拖罐车底盘 拖罐车是一种带有硬橡胶轮子的巨大平板车，由电动机驱动。车厢不是沿着铁轨行驶，而是在 油罐墙的平顶上滚动。 参见图 5-5 了解拖车水箱的图片。 所需的车厢速度由数据站的一个变阻器设定。一个简单的电动机控制器使用安装在电机轴上 的编码轮和光传感器来测量车厢速度。在前进行程中，当一个凸出的触发开关被安装在罐壁上 的法兰触发时，车厢会停止。在倒车时，车厢仅由警觉的操作员在数据站刺按电机停止开关来 停止。 我们操作滑车的速度更多地受限于牵引水槽的长度，而不是滑车电机的扭矩。我们的最大速 度大约是每秒1.5米或3节，这是车辆的操作速度。在那个速度下，由瞬时启动产生的支撑杆振动 需要几秒钟才能衰减，使我们在滑车开始减速之前只有几秒钟的有效数据。 实际的履带速度是使用安装在坦克远端的激光测距仪测量的。该测距仪为Nova Ranger NR-10 0，并不测量飞行时间；相反，它经过校准以根据投射点的位置测量距离。在给定距离下，该仪 器输出相应的电压。 模拟测距仪信号被传输到数据站，在那里它也被笔记本电脑的模数转换板采样。两个数字信 号都使用数据采集软件记录，然后用 MATLAB 处理。 5.3 阻力测试实验程序 阻力测试实验程序包括以下步骤：

---

## Page 75

Figure 5-2: URI Tow Tank [Photo courtesy of URI Ocean Engineering Department]

---

## Page 76

图 5-2：URI 托槽罐 [Photo courtesy of URI Ocean Engineering Department]

---

## Page 77

Figure 5-3: Carriage Setup and Vehicle Mounting Figure 5-4: URI Tow Tank Carriage

---

## Page 78

图 5-3：运输装置设置和车辆安装 图 5-4：URI 拖罐车底盘

---

## Page 79

Figure 5-5: URI Tow Tank Carriage " LVDT and strut pre-calibration * vehicle mount and alignment check " fin alignment check " vehicle drag runs * LVDT and strut post-calibration 5.3.1 Instrument Calibration In calibrating the LVDT, we would apply a range of known loads to the flexural carriage and record the output voltage. This was accomplished by hanging weights from a line tied to the aft end of the bottom flexural plate and run over a pulley. Given that there was a small amount of friction in the LVDT shaft, after hanging the weights we would whack the flexural mount and allow the vibrations to damp out, recording the average steady value after several whacks. During the tank runs, we would periodically check the output voltage of the LVDT power supply, as the output of the aging instrument seemed to vary slightly as it warmed up. In calibrating the strut, we would run the carriage through a range of speeds with just the bare strut in the water, recording the axial and lateral drag. If necessary, we would re-align the strut and run the test again. The measured strut drag as a function of carriage speed would later be subtracted from the total drag of each vehicle run, isolating the vehicle drag. After performing the instrument calibrations and mounting the vehicle, we would check the vehicle the yaw alignment with a plumb bob, and vehicle pitch alignment by sighting through a window in the side of the tank. In the initial experiments, we would check the alignment of the vehicle fins in a similar manner. Unfortunately, the fin drive chains on the WHOIl tail section were both loose, so it was difficult to keep the fins aligned properly. We tried switching to a different tail section with tighter fins, but it

---

## Page 80

图 5-5：URI 缓冲罐小车 LVDT 和支柱预校准 * 车辆安装和 对齐检查 "鳍片对齐检查" 车辆阻力 测试 * LVDT 和支柱后校准 5.3.1 仪器校准 在校准LVDT时，我们会对挠性滑架施加一系列已知载荷，并记录输出电压。这是通过将重量 挂在系在底部挠性板后端的一根绳子上，并通过滑轮实现的。鉴于LVDT轴上有少量摩擦，在 挂上重量后，我们会敲击挠性支架，让振动衰减，并在敲击几次后记录平均的稳定值。 在油箱运行期间，我们会定期检查LVDT电源的输出电压，因为老化仪器的输出似乎在加热 时略有变化。 在校准支柱时，我们会让小车以不同的速度运行，仅让裸支柱浸入水中，同时记录轴向和横 向阻力。如有必要，我们会重新调整支柱的对齐，并再次进行测试。随后测得的支柱阻力作为 小车速度的函数，将从每次车辆运行的总阻力中扣除，从而分离出车辆的阻力。 在完成仪器校准和安装车辆后，我们会用铅垂线检查车辆的偏航对准，并通过观察油箱侧窗 来检查车辆的俯仰对准。 在最初的实验中，我们将以类似的方式检查车辆鳍的对齐。不幸的是，WHOIl 尾部的鳍驱 动链条都很松，因此很难保持鳍正确对齐。我们尝试更换到一个鳍更紧的尾部，但它

---

## Page 81

was still difficult to sight the alignment of the lower rudder fin. In the end, we found it convenient to each day collect a data set with the fins removed, in order to verify the alignment of the vehicle. 5.3.2 Drag Runs The tow tank runs were conducted at five different speeds between 0 and 1.5 meters per second. Between runs, we would begin processing the drag data while we waited for the waves in the tank to damp out. After spending several sessions preparing the lab equipment and developing our calibration pro- cedure, we ran four days of vehicle tests. Table 5.1 gives the dates and details of these experimental runs. Table 5.1: REMUS Drag Runs Date Filename Vehicle (notes) 09 Jun 1999 remxfps7 WHOIl 16 Jun 1999 remdxfps8 WHOI1 (DOCK2 tail) 16 Jun 1999 remdxfps8b WHOI1 (DOCK2 tail) 16 Jun 1999 rnfdxfps8 WHOI1 (DOCK2 tail, no fins) 16 Jun 1999 rnfdxfps8b WHOI1 (DOCK2 tail, no fins) 5.3.3 Signal Processing For a given run, we would collect data from three channels simultaneously-vehicle axial drag, vehicle lateral drag, and carriage speed-at a frequency of 400 Hz per channel. To remove sensor noise and the high-frequency strut and carriage vibrations, we filtered the data using a zero-phase forwards and reverse digital filter of order 250 and with a cut-off frequency of 2.5 Hz. Figure 5-6 shows a comparison of the filtered and unfiltered data for a single channel. Figure 5-6: Vehicle Axial Drag. Carriage Speed 1.52 m/s. [remd5fps8b, 16 June 19991 0 5 10 Time in seconds

---

## Page 82

仍然很难观察到下舵鳍的对齐情况。最后，我们发现每天收集一次拆下鳍片的数据集是很方便 的，以便验证车辆的对齐情况。 5.3.2  拖拽跑 拖曳槽实验在五种不同的速度下进行，速度范围在0到1.5米每秒之间。实验之间，我们会开始 处理阻力数据，同时等待槽中的波浪消散。 在花了几次课时准备实验室设备并制定我们的校准程序之后，我们进行了为期四天的车辆测 试。表5.1给出了这些实验运行的日期和详细信息。 表 5.1：REMUS 拖曳实验 Date Filename Vehicle (notes) 09 Jun 1999 remxfps7 WHOIl 16 Jun 1999 remdxfps8 WHOI1 (DOCK2 tail) 16 Jun 1999 remdxfps8b WHOI1 (DOCK2 tail) 16 Jun 1999 rnfdxfps8 WHOI1 (DOCK2 tail, no fins) 16 Jun 1999 rnfdxfps8b WHOI1 (DOCK2 tail, no fins) 5.3.3 信号处理 对于给定的一次运行，我们会同时从三个通道收集数据——车辆轴向阻力、车辆横向阻力和车 厢速度——每个通道的采样频率为 400 Hz。为了去除传感器噪声以及高频的支撑杆和车厢振动 ，我们使用一个阶数为 250、截止频率为 2.5 Hz 的零相位前向和反向数字滤波器对数据进行了 滤波。图 5-6 显示了单个通道过滤前后数据的比较。 图 5-6：Ve 轴向阻力。车架速度 1.52 米/秒。[remd5fps8b, 16 June 19991 0 5 10 Time in seconds

---

## Page 83

5.4 Experimental Results Figure 5-7 shows a plot of forward speed versus vehicle axial drag for the different configurations. These data were averaged to find a relationship between forward velocity and axial drag, based on the following formula: (5.1) 2F= p Af v 2 where Fd is the measured drag force (after subtraction of strut drag), p the fluid density (999.1 kg/ms), Af the vehicle frontal area (0.029 meters), v the measured vehicle forward velocity, and Cd the vehicle drag coefficient. This resulted in an experimental average drag coefficient of 0.267. The resulting parabolic fit is also plotted in Figure 5-7. Again, Table 5.1 gives the dates and details of these experimental runs. Although the vehicle was towed at a depth of 2.3 body diameters, a significant amount of wave- making was noticed in the tank for carriage speeds above one meter per second. This additional wave-making drag can be seen in Figure 5-7 as a deviation in the experimental data from the parabolic curve fit at higher carriage speeds. Forward Velocity (m/s) Figure 5-7: Forward Speed vs. Vehicle Axial and Lateral Drag (See Table 5.1 for experiment details) 5.5 Component-Based Drag Model Bottaccini [7] and Hoerner [15] suggest a drag coefficient of 0.08 to 0.1 for torpedo shapes sim- ilar to REMUS, i.e. for fineness ratios (length over maximum diameter) of 6 to 11. Given the experimentally-measured drag coefficient of 0.267, it is obvious that the various hull protrusions contribute significantly to the total vehicle drag. Table 5.2 lists the different vehicle components and their estimated contributions to the total vehicle drag. The drag coefficient value for the vehicle hull is from Myring [22] for a 'B' hull contour. The drag coefficient estimates for the vehicle components are taken from Hoerner [15]. All estimates assume a vehicle operating speed of 1.54 meters per second (3 knots). The resulting estimate for

---

## Page 84

5.4 实验结果 图 5-7 显示了不同配置下前进速度与车辆轴向阻力的关系图。这些数据被平均以找到前进速度 与轴向阻力之间的关系，基于以下公式： (5.1) 2F= p Af v 2 其中 Fd  是测得的阻力（在减去支撑杆阻力后），p 是流体密度（999.1 kg/m³），Af  是车辆正面 面积（0.029 米²），v  是测得的车辆前进速度，C d  是车辆阻力系数。由此得到的实验平均阻力 系数为 0.267。所得的抛物线拟合也绘制在图 5-7 中。同样，表 5.1 给出了这些实验运行的日期 和详细信息。 尽管该车辆在2.3个车体直径的深度被牵引，但在车速超过每秒一米时，水槽中仍观察到明 显的波浪产生。在图5-7中，这种额外的波浪阻力可以看到为在较高车速下实验数据偏离抛物线 拟合曲线的现象。 Forward Velocity (m/s) 图5-7：前进速度与车辆轴向和横向阻力（实验详情见表5.1） 5.5 基于组件的阻力模型 Bottaccini [7] 和 Hoerner [15] 建议，对于类似 REMUS 的鱼雷形状，即长度与最大直径之比为 6 到 11 的细长比，阻力系数为 0.08 到 0.1。鉴于实验测得的阻力系数为 0.267，很明显，各种船 体突出部分对总车辆阻力贡献显著。 表 5.2 列出了不同的车辆组件及其对车辆总阻力的估计贡献。车辆船体的阻力系数值取自 M yring [22] 对 'B' 船体轮廓的研究。车辆组件的阻力系数估计取自 Hoerner [15]。所有估计均假设 车辆运行速度为 1.54 米每秒（3 节）。由此得到的估计值为

---

## Page 85

total drag yields, by Equation 5.1, an overall drag coefficient of 0.26, which compares well with the experimental results. In Table 5.3, a similar component-based analysis is performed to predict the total drag of the sidescan sonar-equipped REMUS vehicle. Table 5.2: REMUS Component-Based Drag Analysis - Standard Vehicle Qty Cd Length Width Diam. Area Drag m m m m2 N Myring Hull 1 0.10 0.19 2.E-04 3.39 Fins 4 0.02 0.09 0.08 5.E-05 0.62 LBL Transducer 1 1.20 0.03 0.05 1.E-05 2.07 Nose Pockets 3 1.17 0.03 4.E-06 2.68 Blunt Nose 1 ? Total Vehicle Drag: 8.77 Effective Cd: 0.26 Table 5.3: REMUS Component-Based Drag Analysis - Sonar Vehicle Qty Cd Length Width Diam. Area Drag m m m m2 N Myring Hull 1 0.10 0.19 2.E-04 3.39 Fins 4 0.02 0.09 0.08 5.E-05 0.62 LBL Transducer 1 1.20 0.03 0.05 1.E-05 2.07 Nose Pockets 3 1.17 0.03 4.E-06 2.68 Blunt Nose 1 ? 0.00 SSS Transducers 2 0.40 0.04 0.04 1.E-05 1.47 ADCP Transducers 8 0.20 0.05 1.E-05 3.86 Total Vehicle Drag: 14.09 Effective Cd: 0.42

---

## Page 86

根据方程5.1，总阻力得到的整体阻力系数为0.26，与实验结果比较接近。 在表 5.3 中，进行了类似的基于组件的分析，以预测配备侧扫声纳的 REMUS 车辆的总阻力 。 表 5.2：REMUS 基于组件的阻力分析 - 标准车辆 Qty Cd Length Width Diam. Area Drag m m m m2 N Myring Hull 1 0.10 0.19 2.E-04 3.39 Fins 4 0.02 0.09 0.08 5.E-05 0.62 LBL Transducer 1 1.20 0.03 0.05 1.E-05 2.07 Nose Pockets 3 1.17 0.03 4.E-06 2.68 Blunt Nose 1 ? Total Vehicle Drag: 8.77 Effective Cd: 0.26 表 5.3：基于组件的 REMUS 阻力分析 - 声纳车辆 Qty Cd Length Width Diam. Area Drag m m m m2 N Myring Hull 1 0.10 0.19 2.E-04 3.39 Fins 4 0.02 0.09 0.08 5.E-05 0.62 LBL Transducer 1 1.20 0.03 0.05 1.E-05 2.07 Nose Pockets 3 1.17 0.03 4.E-06 2.68 Blunt Nose 1 ? 0.00 SSS Transducers 2 0.40 0.04 0.04 1.E-05 1.47 ADCP Transducers 8 0.20 0.05 1.E-05 3.86 Total Vehicle Drag: 14.09 Effective Cd: 0.42

---

## Page 87

Chapter 6 Vehicle Simulation In this chapter, we begin by completing the equations governing vehicle motion. We then derive a numerical approximation for equations of motion and for the kinematic equations relating motion in the body-fixed coordinate frame to that of the inertial or Earth-fixed reference frame. Finally, we use that numerical approximation to write a computer simulation of the vehicle motion. 6.1 Combined Nonlinear Equations of Motion Combining the equations for the vehicle rigid-body dynamics (Equation 3.8) with the equations for the forces and moments on the vehicle (Equation 4.49), we arrive at the combined nonlinear equations of motion for the REMUS vehicle in six degrees of freedom. Surge, or translation along the x-axis: m [6 -vr +wq -xg(q 2 +r 2)+ yg(pq - )+ zg(pr +)] XHS - X.u.U Jul - Xin + Xwqwq + Xqqqq (6.1) + Xvrvr + Xrrrr + Xprop Sway, or translation along the y-axis: m [)-wp+ur-yg(r2 Ip 2 ) +zg(qr-3) +xg(qp+)]= YHS + Yvlviv Jvj + Yrrr In+ Y6) + Yi- (6.2) + Yurur + Ywpwp + Ypqpq + Yuuv + Yuu3 ,u 2 6,r Heave, or translation along the z-axis: m (tb - uq + vp - zg (p2 + 2')+ xg(rp - 4) + yg(rq + )= ZHS + Z~j jW |w| + Zqiq gi + Zjjb + Z44 (6.3) + Zuquq + ZvpVp + Zrprp + Zumuw + Zuu6,u26s Roll, or rotation about the x-axis: Ixjp+ (Izz - Iyy)qr +m [yg(b -uq +vp) - zg(i - wp+ur)] (6.4) KHS + Kpiipp|+ Kypr+ Kprop Pitch, or rotation about the y-axis: Iyy4+ (Ixx - Izz)rp + m [zg(ia - vr + wq) - xg(z - uq + vp)] MHS + M~wlww w| + Mqjqq q| + Mjji + Mq4 (6.5) + Muquq + Mvpvp + Mrprp + Muwu + Muus u26,

---

## Page 88

第6章 车辆模拟 在本章中，我们首先完成描述车辆运动的方程。然后，我们推导运动方程和将车体固定坐标系中的运动与 惯性或地面固定参考系中的运动联系起来的运动学方程的数值近似。最后，我们利用该数值近似编写车辆 运动的计算机模拟。 6.1 联合非线性运动方程 将车辆刚体动力学的方程（公式 3.8）与作用于车辆的力和力矩方程（公式 4.49）结合，我们得到 REMU S 车辆在六自由度下的非线性组合运动方程。 沿 x 轴的冲击或平移： m [6 -vr +wq -xg(q 2 +r 2)+ yg(pq - )+ zg(pr +)] XHS - X.u.U Jul - X in  + Xwqwq + Xqqqq (6.1) + Xvrvr + X rrrr + Xprop 沿 y 轴的摆动或平移： m [ ) - w p + u r - y g ( r2 Ip 2 ) + z g (q r -3 ) + x g (q p + )] = YHS + Yvlviv Jvj + Y rrr In+ Y6) + Yi- (6.2) + Y urur + Ywpwp + Ypqpq + Yuuv + Yuu3 ,u 2 6,r 沿 z 轴的升降或平移： m  (tb - uq + vp - zg (p2 + 2')+ x g ( r p  - 4) + yg(rq + )= ZHS + Z~j jW |w| + Zqiq gi + Zjjb + Z44 (6.3) + Zuquq + ZvpVp + Zrprp + Zumuw + Zuu6,u26s 滚转，或绕 x 轴旋转： Ixjp+  (Izz - Iyy)qr +m [yg(b -uq +vp) - zg (i - w p + u r)] (6.4) KHS + Kpiipp|+ Kypr+ Kprop 俯仰，或绕 y 轴的旋转： Iyy4+ (Ixx - Izz)rp  + m [zg(ia - vr + wq) - xg(z - uq + vp)] MHS + M~wlww w| + Mqjqq q| + M jji + Mq4 (6.5) + M uquq + Mvpvp + Mrprp + Muwu + Muus u26,

---

## Page 89

Yaw, or rotation about the z-axis: Izz' + (Iyy - Ix.)pq + m [xg(6 - wp + ur) - yg(ft - vr + wq)] = NHS + Nvl,|v |v| + N rr Ir + Njio + Nit (6.6) + Nurur + Nwpwp + Npqpq + Nuvuv + Nu5,uu 23r We will find it convenient to separate the acceleration terms from the other terms in the vehicle equations of motion. The equations can thus be re-written as: (m - Xi,)i6 + mzg4 - mygt = XHS + Xuuju Jul + (Xwq - m)wq + (Xqq + mxg)q 2 + (Xvr + m)vr + (Xrr + mxg)r 2 - mygpq - mzgpr + Xprop (m - Yj,)i' - mzgj3 + (mx9 - Yr)i4 = YHS + Yvjviv |vI + Yr|r Ir| + mygr 2 + (Yur - m)ur + (Yw, + m)wp + (Yq - mxg)pq + Yvuv -+ mygp 2 + mzgqr + YuubrU 26r (m - Zlb)tb + myg - (mx9 + Zg)4 = ZHS + ZjIW |WI + Zqqjq |q| + (Zuq + m)uq + (Zvp - m)vp + (Zrp - mxg)rp + Zuwum + mzg(p 2 + q 2) - mygrq + Zuus6u 2 S, (6.7) - mzg? + my9t + (Izx - K2)p = KHS + K,\,|pIp | - (Izz - Iyy)qr + m(uq - vp) - mzg(wp - ur) + Kprop mzgi - (mx9 + Ms )b + (IVY - M4)A = MHS + Mwj\lw IwI + Mqqq Jq| + (Muq - mxg)uq + (Mp ,mxg)vp + [Mrp - (I~x - Izz)] rp + mzg (vr - wq) + Muw uw + Muu68 u 268 - mygit + (mxg - Ni) + (Izz - N,-)i = NHS + Nv,lvi ±v+ Nrl,|r Ir| + (Nur - mxg)ur + (Nwp + mxg)wp + [Npq - (Iyy - Ix.)] pq - myg(vr - wq) + NUVUV + NUU6rU26r Finally, these equations can be summarized in matrix form as follows: F m- X4 0 0 0 mzg -myg 1 X o m-Yo 0 -mz9 0 mx -Yj K Y 0 0 m - Zb my9 -mxg - Z 4 0 _ ZI I6.8 0 -mzg my9 Ixx - K1 0 0 pI ~6.K) mz9 0 -mxg - Mb 0 IYY - M4 0 I M -myg mxg - N, 0 0 0 Iz -N. J [ . . EN or o m - X4 0 0 0 mzg -my - ZX 0 m -Y 0 -mz 9 0 mxg -Y ZY w0 0 m- Z& my9 -mxg - Z4 0 E Z (6.9) 0 -mz 9 my9 Ixx - K1 0 0 E K - mz9 0 -mxg - Mb 0 Iyy - M4 0 J M -myg mxg - No 0 0 0 IZZ - N,; . N 6.2 Numerical Integration of the Equations of Motion The nonlinear differential equations defining the vehicle accelerations (Equation 6.9) and the kine- matic equations ( Equations 3.1 and 3.4) give us the vehicle accelerations in the different reference frames. Given the complex and highly non-linear nature of these equations, we will use numerical integration to solve for the vehicle speed, position, and attitude in time.

---

## Page 90

偏航，或绕 z-axis: 的旋转 Izz' + (Iyy - Ix .)p q  + m [xg(6 - wp + u r )  - yg(ft - v r + wq)] = NHS + Nvl,|v |v| + N rr Ir + Njio + N it (6.6) + N urur + Nwpwp + Npqpq + Nuvuv + N u 5 ,u u23r 我们将发现将车辆运动方程中的加速度项与其他项分开会更方便。因此，这些方程可以重新写为： (m - Xi,)i6 + mzg4 - mygt = XHS + Xuuju Jul + (Xwq - m)wq + (Xqq + mxg)q 2 + (X vr + m )v r  + (X r r  + m xg)r 2 - m ygpq - m zg p r + X prop (m - Yj,)i' - mzgj3 + (mx9 - Yr)i4 = YHS + Yvjviv |vI + Yr|r Ir| + mygr 2 + (Yur - m )u r  + (Yw, + m)wp + (Yq - mxg)pq + Yvuv -+ mygp 2 + mzgqr + YuubrU 26r (m - Zlb)tb + myg - (mx 9 + Zg)4 = ZH S + Z jI W  |WI + Zqqjq |q| + (Zuq + m )uq  + (Zvp - m )vp  + (Zrp - m x g )rp  + Zuw um + mzg(p 2 + q 2) - mygrq + Zuus6u 2 S, (6.7) - mzg? + my 9t + (Izx - K2)p = K H S + K,\,|pIp | - (Izz - Iyy)qr + m (u q  - vp) - mzg(wp - u r )  + Kprop mzgi - (mx9 + M s )b + (IVY - M4)A = MHS + Mwj\lw IwI + Mqqq Jq| + (Muq - mxg)uq + ( M p  ,m xg)vp + [Mrp - (I~x - Izz)] rp + mzg (vr - wq) + Muw uw + Muu68 u 268 - mygit + (mxg - Ni) + (Izz - N,-)i = NHS + N v,lvi ±v+ N rl,|r Ir| + (N ur - m x g )u r + (N w p  + mxg)wp + [Npq - (Iyy - Ix.)] pq - m yg (vr - wq) + NUVUV + NUU6rU26r 最后，这些方程可以总结为如下矩阵形式： F m- X4 0 0 0 mzg -myg 1 X o m -Y o 0 -mz 9 0 m x -Yj K Y 0 0 m - Zb my9 -mxg - Z 4 0 _ ZI I6.8 0 -mzg my9 Ixx - K1 0 0 pI ~6.K) mz9 0 -mxg - Mb 0 IYY - M4 0 I M -myg mxg - N, 0 0 0 Iz -N. J [ . . EN 或者 o m - X4 0 0 0 mzg -my - ZX 0 m -Y 0 -mz 9 0 mxg -Y ZY w0 0 m- Z& my9 -mxg - Z4 0 E Z (6.9) 0 -mz 9 my9 Ixx - K1 0 0 E K - mz9 0 -mxg - Mb 0 Iyy - M4 0 J M -myg mxg - No 0 0 0 IZZ - N,; . N 6.2 运动方程的数值积分 定义车辆加速度的非线性微分方程（方程 6.9）和运动学方程（方程 3.1 和 3.4）给出了车辆在不同参考系 中的加速度。鉴于这些方程的复杂性和高度非线性特性，我们将使用数值积分来求解车辆随时间的速度、 位置和姿态。

---

## Page 91

Consider that at each time step, we can express Equation 6.9 as follows: :-n =f (x, U) (6.10) where x is the vehicle state vector: x = [ u v w p q r x y z # 0 $ ] (6.11) and u, is the input vector: Un =[s or Xprop Kprop ]T (6.12) Refer back to Section 3.2 for the definitions of the vehicle states and inputs, and to Figures 4-1 and 4-2 for the fin angle sign conventions. The following sections summarize three methods of numerical integration in order of increasing accuracy. 6.2.1 Euler's Method We will first consider Euler's method, a simple numerical approximation which consists of applying the iterative formula: on+1 = X + f (Xn, un) -At (6.13) where At is the modeling time step. Euler's method, although the least computationally intensive method, is unacceptable as it can lead to divergent solutions for large time steps. 6.2.2 Improved Euler's Method The following method improves the accuracy of Euler's method by averaging the tangent slope for two points along the line. We first calculate the following: ki = xn + f (xn, un) -At (6.14) k2 = f (ki, Un+ 1) And then combine them to calculate the new state vector: At on+1 = Xn + 2 (f (X,, un) + k 2 ) (6.15) This method is significantly more accurate than Euler's method. 6.2.3 Runge-Kutta Method This method further improves the accuracy of the approximation by averaging the slope at four points. We first calculate the following: k1 = Xn + f (xn, un) k2 = fx + 2 ki, un+ 1 ) (6.16) k3 = f (x+ 2 k2, Un+) k4 = f (x + Atk 3 , un+1 ) where the interpolated input vector 1 Un+ - = (un + un+1) (6.17) 22

---

## Page 92

考虑在每个时间步上，我们可以将方程6.9表示如下： :-n = f  (x, U) (6.10) 其中 x 是车辆状态向量： x = [ u v w p q r x y z # 0 $ ] (6.11) 并且 u,  是输入向量： Un =[s or Xprop Kprop ]T (6.12) 请参阅第3.2节以获取车辆状态和输入的定义，并参阅图4-1和图4-2以了解鳍角符号的约定。 以下各节按精度递增的顺序总结了三种数值积分方法。 6.2.1 欧拉方法 我们将首先考虑欧拉方法，这是一种简单的数值近似方法，其包括应用迭代公式： on+1 = X + f (Xn, un) -At (6.13) 其中 At 是建模时间步长。欧拉方法虽然计算量最小，但不可接受，因为它可能在较大的时间步长下导致 解发散。 6.2.2 改进的欧拉法 以下方法通过对沿直线的两个点的切线斜率进行平均来提高欧拉方法的精度。我们首先计算以下内容： ki = x n  + f ( x n , u n ) -A t (6.14) k2 = f (ki, Un+ 1) 然后将它们组合起来以计算新的状态向量： At on+1 = Xn + 2 (f (X,, un) + k 2 ) (6.15) 这种方法的准确性明显高于欧拉方法 方法。 6.2.3  龙格-库塔法 该方法通过对四个点的斜率进行平均，进一步提高了近似的准确性。我们首先计算如下内容： k1 = Xn + f (xn, un) k2 = fx + 2 ki, un+ 1) (6.16) k3 = f (x+ 2 k2, Un+) k4 = f (x + Atk 3 , un+1 ) 插值后的输入向量在哪里 1 Un+ - = (un + un+1) (6.17) 2 2

---

## Page 93

We combine the above equations to yield: n+1 = Xn + At (ki + 2k2 + 2k3 + k 4) (6.18) 6 This method is is the most accurate of the three. This is what we shall use in the vehicle model code. 6.3 Computer Simulation As described in the Introduction, the author implemented this numerical approximation using MAT- LAB. The model code can be seen in Appendix E. The model code works by calculating for each time step the forces and moments on the vehicle as a function of vehicle speed and attitude. These forces determine the vehicle body-fixed accelerations and earth-relative rates of change. These ac- celerations are then used to approximate the new vehicle velocities, which become the inputs for the next modeling time step. The vehicle model requires two inputs: " Initial conditions, or the starting vehicle state vector. " Control inputs, or the vehicle pitch fin and stern plane angles, either given as a pre-determined vector, when comparing the model output with field data, or calculated at each time step, in the case of control system design.

---

## Page 94

我们将上述方程结合起来得到： n+1 = Xn + At (ki + 2k2 + 2k3 + k 4) (6.18) 6 这种方法是三种方法中最准确的。这就是我们将在车辆模型代码中使用的方法。 6.3  计算机模拟 如引言中所述，作者使用 MATLAB 实现了这一数值近似。模型代码见附录 E。该模型代码的工 作原理是，对于每一个时间步，计算车辆的力和力矩，这些力和力矩是车辆速度和姿态的函数 。这些力决定了车辆相对于车体的加速度以及相对于地球的变化率。然后，这些加速度被用来 近似新的车辆速度，这些速度成为下一建模时间步的输入。 该车辆模型需要两个输入： “Initial conditions, 或起始车辆状态矢量。”Control inputs, 或车辆俯仰鳍和尾翼角度，这 些角度可作为预定矢量，用于比较模型输出与现场数据时，或在控制系统设计中每个时间步 计算。

---

## Page 95

Chapter Field Experiments 7.1 Motivation In order to verify the accuracy of the vehicle model, the author conducted a series of experiments at sea measuring the response of the vehicle to step changes in rudder and stern plane angle. These experiments were conducted with the assistance of the Oceanographic Systems Lab staff at both the Woods Hole Oceanographic Institution and at the Rutgers University Marine Field Station in Tuckerton, New Jersey. Figure 7-1: The author (left) and Mike Purcell from WHOI OSL, running vehicle experiments at the Rutgers Marine Field Station in Tuckerton, NJ [Photo courtesy of Nuno Cruz, Porto University] 7.2 Measured States In each experiment at sea we measured the vehicle depth and attitude, represented in the vehicle model by the following, globally-referenced vehicle states: x=[z > 0 ) V (7.1) In these experiments we also recorded the vehicle fin angles, represented in the vehicle model by the following vehicle-referenced control inputs: tn = [ Js 6, )] (7.2)

---

## Page 96

C章节 F田间试验 7.1动机 在 o为了验证车辆模型的准确性，作者进行了系列实验 在看测量车辆对舵角和尾平面角阶跃变化的响应。这些 体验实验在海洋系统实验室工作人员的协助下进行，地点包括 这伍兹霍尔海洋研究所以及罗格斯大学海洋实习站 图克新泽西州科尔顿 无花果 关于7-1：作者（左）和来自WHOI OSL的Mike Purcell，在进行车辆实验 这 位于新泽西州塔克顿的罗格斯海洋田野站 [Photo courtesy of Nuno Cruz, Porto University] 7.2测量状态 在 e在海上的每一次实验中，我们测量了车辆的深度和姿态，这些都在车辆中表示出来 模通过以下全球参考的车辆状态： x=[z > 0 ) V (7.1 ) 在 t 在这些实验中，我们还记录了车辆的鳍角，这在车辆模型中由⋯⋯表示 跟随机翼  车辆参考  控制输入： tn = [ J s 6, )] (7.2)

---

## Page 97

Refer to Figure 3-1 for a diagram of the vehicle coordinate system, and to Figures 4-1 and 4-2 for diagrams of the control fin sign conventions. Note that for all of the field tests described in this section, the vehicle propeller was not used as a control input, but was instead kept at a constant 1500 RPM. As propeller thrust and torque were difficult to estimate for different propeller RPMs, sticking to a constant value allowed us to remove a source of uncertainty from the vehicle model comparison. 7.3 Vehicle Sensors The following were the navigation sensors available during the author's field experiments. For each sensor, we will give the sensor's function, and its known limitations. Note that sensor accuracy is often a function of cost. Vehicles like REMUS are designed to be relatively inexpensive-a high precision gyro-compass, for example, might double the cost of the vehicle. The challenge in vehicle design is to identify the least expensive sensor suite that meets the vehicle's navigation requirements. 7.3.1 Heading: Magnetic Compass Vehicle heading was measured with a triaxial fluxgate magnetometer, which senses the orientation of the vehicle with respect to earth's magnetic vector. The magnetometer is sensitive to magnetic noise, such as is generated by the various electronic components within the vehicle housing. The calibration routine for this sensor has the vehicle drive in circles while pitching and rolling-by integrating the yaw rate and comparing it with the measured heading, a table of compass deviation as a function of vehicle heading can be made. This magnetic calibration can correct for constant sources of magnetic noise, such as the vehicle batteries, but not for intermittent signals such as the fin and propeller motors. As a result, heading measurements can be off by as much as five degrees. 7.3.2 Yaw Rate: Tuning Fork Gyro Vehicle yaw rate is measured with a tuning fork gyroscope. The integral of the sensor output to obtain heading is vulnerable to drift, and is therefore more accurate when measuring high frequency vehicle motions. By combining the low-pass filtered compass data with high-pass filtered and inte- grated yaw rate gyro data, we can arrive at a more accurate estimate for the vehicle heading. 7.3.3 Attitude: Tilt Sensor Vehicle pitch and roll are measured with an electrolytic tilt and roll sensor. This sensor measures the position of a blob of conducting fluid in a cup. For example, the vehicle pitching down is indicated by the fluid sloshing forward. This sensor is accurate for low-frequency motion, but will obviously have problems capturing high frequency motion due to the inertia of the conducting fluid. Furthermore, the motion of the fluid is coupled such that high vehicle yaw rates or surge accelerations give false pitch measurements. 7.3.4 Depth: Pressure Sensor The vehicle depth is measured by a pressure sensor. This instrument is somewhat sensitive to changes in the surrounding sea water temperature, but its errors are small in magnitude relative to the error in the compass and attitude sensors. 7.4 Experimental Procedure In this section, we describe the procedure used in the field experiment listed in Table 7.1. These experiments were run in roughly ten meters of water, both in Hadley's Cove near the Woods Hole

---

## Page 98

请参见图3-1了解车辆坐标系的示意图，参见图4-1和图4-2了解控制舵符号约定的示意图。 请注意，对于本节中描述的所有现场测试，车辆螺旋桨未被用作控制输入，而是保持在恒定 的1500转/分钟。由于不同螺旋桨转速下的螺旋桨推力和扭矩难以估算，坚持使用恒定值使我们 能够从车辆模型比较中消除一个不确定性来源。 7.3  车辆传感器 在作者的实地实验中，可用的导航传感器如下。对于每个传感器，我们将介绍传感器的功能及 其已知的限制。 请注意，传感器的精度通常与成本相关。例如，像 REMUS 这样的车辆被设计为相对低成本 ——一个高精度的陀螺罗盘可能会使车辆成本翻倍。车辆设计中的挑战是确定能够满足车辆导 航需求的最廉价的传感器组合。 7.3.1 标题：磁性罗盘 车辆航向是通过三轴磁通门磁力计测量的，该磁力计感知车辆相对于地球磁矢量的方向。磁力 计对磁噪声很敏感，例如车辆内部各种电子元件产生的噪声。该传感器的校准程序要求车辆绕 圈行驶，同时进行俯仰和滚转——通过积分偏航角速度并将其与测得的航向进行比较，可以制作 一张航向偏差随车辆航向变化的表格。 这种磁校准可以校正恒定的磁噪声来源，例如车辆电池，但不能校正间歇信号，例如鳍和螺 旋桨电机。因此，航向测量可能会偏差多达五度。 7.3.2 偏航率：音叉陀螺 车辆偏航率使用音叉陀螺仪测量。通过对传感器输出进行积分以获得航向容易受到漂移的影响 ，因此在测量高频车辆运动时更为准确。通过将低通滤波的指南针数据与高通滤波并积分后的 偏航率陀螺仪数据结合，我们可以得出车辆航向的更准确估计。 7.3.3  姿态：倾斜传感器 车辆的俯仰和横滚是通过电解倾斜和横滚传感器测量的。该传感器测量杯中导电液体团的位置 。例如，车辆前倾时，液体向前晃动即可指示车辆俯仰向下。 该传感器对于低频运动非常准确，但由于导电液体的惯性，在捕捉高频运动时显然会有问题 。此外，液体的运动是耦合的，因此高车辆偏航率或纵向加速度会产生错误的俯仰测量。 7.3.4 深度：压力传感器 车辆深度由压力传感器测量。该仪器对周围海水温度的变化有一定的敏感性，但其误差相对于 指南针和姿态传感器的误差来说，幅度较小。 7.4 实验步骤 在本节中，我们描述了表7.1中列出的现场实验所使用的程序。这些实验在大约十米深的水中进 行，地点包括伍兹霍尔附近的哈德利湾

---

## Page 99

Oceanographic Institution, and off the Atlantic coast near the Rutgers Marine Field Station in Rutgers, New Jersey. Table 7.1: Vehicle Field Experiments Date Filename Vehicle Location 29 Jul 1998 d980729a STD REMUS (Dock1) RUMFS 29 Jul 1998 d980729b STD REMUS (Dock1) RUMFS 27 Oct 1998 d981027 STD REMUS (Dock1) Hadley's 28 Oct 1998 d981028 STD REMUS (Dock1) Hadley's 26 Jul 1999 a990726 NSW REMUS (NSW) RUMFS 27 Jul 1999 a990727 NSW REMUS (NSW) RUMFS 7.4.1 Pre-launch Check List Before each mission, the author ran through the checklist shown in Figure 7-2 to check the vehicle housing seals, and to verify operation of the vehicle sensors and communications. 7.4.2 Trim and Ballast Check Following the pre-launch checklist, the author weighted the vehicle and measured the longitudinal center of gravity, xg, on a balance. The vehicle buoyancy was measured in a sea water tank, and the vehicle ballast adjusted to achieve 1.5 pounds of positive buoyancy as described in Section 2.4. 7.4.3 Vehicle Mission Programming The REMUS vehicle uses a component-based mission programming architecture. Each element in the mission is called an objective. The following types of objectives were used in the thesis experiments: * SET POSITION: This command gives the vehicle its starting position as a range and bearing from a given latitude and longitude. * WAIT PROP: This command tells the vehicle to remain on standby until it detects the given propeller RPM. This allows us to start the vehicle mission by reaching into the water and spinning the vehicle propeller. The mission program starts, the propeller starts spinning on its own, we push the vehicle underwater and it is on its way. " LONG BASELINE: This command tells the vehicle to navigate to the given latitude and longitude, using the given transponder beacons. In this mode, the vehicle uses long baseline navigation, dead-reckoning its position between acoustic fixes. See Roger Stokey's paper [28] for details on REMUS navigation. " TIMER: This command tells the vehicle to maintain the given depth or heading using feed- back control, or to maintain a given, fixed fin angle or propeller RPM. The timer commands represent the experimental sections of each mission. These objectives are edited and sent to the vehicle as a text files. See Appendix F for an example mission file. In order to measure the vehicle response to step changes in fin angle, the vehicle was given the following commands: o Timer to desired depth For "pitch up", the vehicle was commanded to six meters depth, to avoid breaking the surface. For "pitch down" commands, the vehicle was commanded to 2 meters depth.

---

## Page 100

海洋学机构，以及在新泽西州罗格斯的罗格斯海洋实地站附近的大西洋海岸。 表 7.1：车辆实地实验 Date Filename Vehicle Location 29 Jul 1998 d980729a STD REMUS (Dock1) RUMFS 29 Jul 1998 d980729b STD REMUS (Dock1) RUMFS 27 Oct 1998 d981027 STD REMUS (Dock1) Hadley's 28 Oct 1998 d981028 STD REMUS (Dock1) Hadley's 26 Jul 1999 a990726 NSW REMUS (NSW) RUMFS 27 Jul 1999 a990727 NSW REMUS (NSW) RUMFS 7.4.1  发射前检查清单 在每次任务之前，作者都会按照图 7-2 所示的清单逐项检查，以检查车辆壳体密封，并验证车辆传感器和 通信的运行情况。 7.4.2 修边和压舱检查 按照预启动清单，作者称重了车辆并在平衡仪上测量了纵向重心xg。车辆的浮力在海水池中进行了测量， 并调整了车辆的压载以实现第2.4节所述的1.5磅正浮力。 7.4.3  车辆任务编程 REMUS 车辆使用基于组件的任务编程架构。任务中的每个元素都称为目标。论文实验中使用了以下类型 的目标： * 设置位置：此命令为车辆提供起始位置，以给定的纬度和经度为基准的距离和方位。* 等待螺旋桨转 速：此命令指示车辆保持待机状态，直到检测到指定的螺旋桨转速。这允许我们通过将车辆推进水中 并启动车辆螺旋桨来开始任务。任务程序启动后，螺旋桨自行开始旋转，我们将车辆推进水中，它便 开始任务。* 长基线：此命令指示车辆使用给定的应答器信标导航到指定的纬度和经度。在此模式下 ，车辆使用长基线导航，在声学定位间进行估算航位。如需有关REMUS导航的详细信息，请参见Roge r Stokey的论文[28]。* 定时器：此命令指示车辆使用反馈控制维持给定深度或航向。 这些目标被编辑并作为文本文件发送到车辆。有关示例任务文件，请参见附录F。 为了测量车辆对翅片角度阶跃变化的响应，车辆被下达了以下指令： 对于“抬头”命令，车辆被指令潜入六米深，以避免破水面。对于“低头”命令，车辆被指令潜入两 米深。

---

## Page 101

TH E SIS E XPE RIMENT PR E -LIN CH CH ECK L IST EATE: M ISSIOR OPERATOR: M ISSIONOBJ BTIV E REMUS: HOUSING OPEN o WbNcle cnshore power. O Check MUalgirrentin rroting bracket. E Align batery side to rrerks on chassis scrn hcdes. O Check sce s on chassis bind-rge connectr rrounting plate. El Check IMU serial and power connections. tiewrap corrpass serial conrector. LI Check MUccTpss calbration ASIcorrndsthroug serialdebug: - clears had ron oaibrtion bakt - stops poln 'cc' - clears compasscal Iestart' - restarts corrpass Q Check MUoperalion in heading, pitch, and rdI O rrpass light GREEN? o Check 9V scrar back-up battery vdltage. Replace if necesary. EI Check foward and aft 0-rirgs for ricks. lubricae if necessary. Q Nte AMtMail section:_ REMUS: HOUSING CLOSED C Check rridbody housirg forward and aft for pnched -rings Q Be sure that dd liles hme been gpIcaded and archiNved. ClIe Cverrus.rtf Cadcp da Cgps dat Archive CAshadaw rissicnrnissinrilf CAhadcw 'rissionlocation.rif Cshadaw rerrus_vini CAdcp xt 0 Set batterytjpe in remus_v.nille Gea- battery if new or fresh charge Figure 7-2: REMUS Pre-Launch Checklist (Page One) 0 Check ehicle dock Feset if necessay. C1 Ceekth the OBSis worng (3 Check pressure gauge: shold have vhide attude < 031 m C Check that CTO daa rrdees sense in ar: Cbnd; Terrp: _ Press: E] eccrd corrpass pitch and rdl ofsets: PtRch: FIl: l Check ADCPcperalion Lstenforiransissionpings Ehserrbles being colected in tet widow. O Check acoustbs on bench. Lhocrnmnt ATS dgIostics in rrission file. Set rerrus ranger (rage jft) TRAkNS PO NDmode Pacetrarsducers I nches apat Check runbers: S/N> 75 j00 Attenuati c> 45 (Chop <26when removed) IBS/N>6 P-ak > 28000 Turn RANGERoif. rifyattenutor drps below 2. Cbrnrent ATS diagnostics backout of rrission file (3 \wrify REMUSrager operation on 5seconds. o brify RBAUSranger abort. Make surethe prop isclearthen sendi pings 13 Set datare tomrraxinrn inrernusvini Set "Log every nth mtus rrsif= 1 l Check pitch and rudderin algrnts. Reccrd offsets frcrnrerrus vini Rtch: Ridder: n logram LOCATIONle. Triple check all buoy LAT/LONG, be au are of offses and alu ays use 1he tue latlong locations indicated in the LOCATION INFO pull dow n. I lograrrMISSIDN1fle [3 Check rission usng RDUTE IfO. \Wrify DEPTH, C6iance and RPMfor each leg wrifetotatre of rrission. lear al faut rressages. l RESTART veicle. C Checktht allights are GR EE Pead any fult messages that appear. C (heck bateryvdtage byturring off etermal power supply. Shodd be 224\6Wts. Pecord batteryvege:

---

## Page 102

T H E  SIS E  X PE R IM E N T PR E  -L IN C H C H E C K L  IST EATE: M ISSIOR OPERATOR: M ISSIONOBJ BTIV E REMUS: HOUSING OPEN o WbNcle cnshore power. O Check MUalgirrentin rroting bracket. E Align batery side to rrerks on chassis scrn hcdes. O Check sce s on chassis bind-rge connectr rrounting plate. El Check IMU serial and power connections. tiewrap corrpass serial conrector. LI Check MUccTpss calbration ASIcorrndsthroug serialdebug: - clears had ron oaibrtion bakt - stops poln 'cc' - clears compasscal Iestart' - restarts corrpass Q Check MUoperalion in heading, pitch, and rdI O rrpass light GREEN? o Check 9V scrar back-up battery vdltage. Replace if necesary. EI Check foward and aft 0-rirgs for ricks. lubricae if necessary. Q Nte AMtMail section:_ REMUS: HOUSING CLOSED C Check rridbody housirg forward and aft for pnched -rings Q Be sure that dd liles hme been gpIcaded and archiNved. ClIe Cverrus.rtf Cadcp da Cgps dat Archive CAshadaw rissicnrnissinrilf CAhadcw 'rissionlocation.rif Cshadaw rerrus_vini CAdcp xt 0 Set batterytjpe in remus_v.nille Gea- battery if new or fresh charge 图 7-2：REMUS 发射前检查表（第 1 页） 0 Check ehicle dock Feset if necessay. C1 Ceekth the OBSis worng (3 Check pressure gauge: shold have vhide attude < 031 m C Check that CTO daa rrdees sense in ar: Cbnd; Terrp: _ Press: E] eccrd corrpass pitch and rdl ofsets: PtRch: FIl: l Check ADCPcperalion Lstenforiransissionpings Ehserrbles being colected in tet widow. O Check acoustbs on bench. Lhocrnmnt ATS dgIostics in rrission file. Set rerrus ranger (rage jft) TRAkNS PO NDmode Pacetrarsducers I nches apat Check runbers: S/N> 75 j00 Attenuati c>  45 (Chop <26when removed) IBS/N>6 P-ak > 28000 Turn RANGERoif. rifyattenutor drps below 2. Cbrnrent ATS diagnostics backout of rrission file (3 \wrify REMUSrager operation on 5seconds. o brify RBAUSranger abort. Make surethe prop isclearthen sendi pings 13 Set datare tomrraxinrn inrernusvini Set "Log every nth mtus rrsif= 1 l Check pitch and rudderin algrnts. Reccrd offsets frcrnrerrus vini Rtch: Ridder: n logram LOCATIONle. Triple check all buoy LAT/LONG, be au are of offses and alu ays use 1he tue latlong locations indicated in the LOCATION INFO pull dow n. I lograrrMISSIDN1fle [3 Check rission usng RDUTE IfO . \Wrify DEPTH, C6iance and RPMfor each leg wrifetotatre of rrission. lear al faut rressages. l RESTART veicle. C Checktht allights are GR EE Pead any fult messages that appear. C (heck bateryvdtage byturring off etermal power supply. Shodd be 224\6Wts. Pecord batteryvege:

---

## Page 103

* Step change in fin angle Upon achieving depth, the vehicle was commanded to hold a certain fin angle for two seconds in the case of vertical plane response, or longer for horizontal plane response. The fin angle duration of two seconds was chosen as a result of the experimental run shown in Figure 7-3. In the depth plot right around the seven-second mark, you can see that the vehicle ran into and bounced off the bottom. Given the unpredictable vehicle open-loop response, the author thought it wise to use short periods. 7.4.4 Compass Calibration As described in Section 7.3.1, it was periodically necessary to update the vehicle compass calibration. The compass calibration objective could be included at the start of any mission file. 7.4.5 Vehicle Tracking During the mission, the vehicle was tracked using a sonar transponder. See Figure 7-5 for a photo of the tracking equipment. At the end of the mission, the vehicle would be recovered from the surface, and reprogrammed and relaunched if necessary. 7.5 Experimental Results From these vehicle experiments, we get measurements for the vehicle response to temporary step changes in rudder and stern plane angle. It is important to note that during straight and level flight, the vehicle operates at a roll offset of negative five degrees (< = -5) due to the propeller torque. As a result, we never get pure vertical- or horizontal-plane motion. That said, the vehicle roll is small enough that we are still able identify the vehicle behavior in pitch and yaw. See Figure 7-6 for REMUS motion while operating under closed-loop control, for comparison with the open-loop, step response data. In the example shown, the vehicle was commanded to maintain a depth of two meters. 7.5.1 Horizontal-Plane Dynamics The vehicle response to a step change in rudder angle is shown in Figure 7-7. For the objective shown, the rudder fin was fixed at four degrees, and the vehicle was commanded to maintain constant depth through closed-loop control.. The relevant information in this set of plots is that, for a rudder angle (J,) of roughly four degrees, the vehicle yaw rate was approximately 10 degrees/second. 7.5.2 Vertical-Plane Dynamics Figures 7-8 and 7-9 show the vehicle response to different temporary step changes in fin angle. In both cases, the vehicle was operating under closed-loop depth control until the step change command was given. The time scale on each plot has been shifted such that the step change command occurs at time t = 2 seconds. In Figure 7-8, the vehicle pitch fin (stern plane) angle J, was fixed at negative two degrees. The vehicle is seen to rise roughly 0.5 meters, and that the pitch change is roughly 20 degrees. At the end of the interval, both the depth and pitch rates were increasing. The vehicle is show to have a slightly negative depth rate (rising at roughly 0.5 meters per second) at the instant of the fin step change. In Figure 7-9, the vehicle pitch fin angle o, was fixed at eight degrees. The vehicle is seen to dive roughly 0.4 meters, and the pitch change is roughly 18 degrees. Again, at the end of the interval, both the depth and pitch rates were increasing.

---

## Page 104

* Step change in fin angle 在达到深度后，车辆被指令在垂直平面响应的情况下保持一定的舵角两 秒，或者在水平平面响应的情况下保持更长时间。 鳍角持续时间选择为两秒，这是根据图7-3所示的实验运行结果得出的。在接近七秒的深度图中，可以看 到车辆撞到底部并反弹。鉴于车辆的开环响应不可预测，作者认为使用较短的时间段是明智的。 7.4.4 罗盘校准 如第7.3.1节所述，定期需要更新车辆指南针校准。指南针校准目标可以包含在任何任务文件的开头。 7.4.5  车辆跟踪 在任务期间，该车辆使用声纳应答器进行跟踪。有关跟踪设备的照片，请参见图 7-5。 在任务结束时，飞行器将从地面回收，并在必要时重新编程和再次发射。 7.5 实验结果 通过这些车辆实验，我们获得了车辆对舵面和尾舵角临时阶跃变化的响应测量。需要注意的是，在平直水 平飞行过程中，由于螺旋桨的扭矩，车辆以负五度（< = -5）的横滚偏移运行。因此，我们从未得到纯垂 直面或水平面的运动。尽管如此，车辆的横滚足够小，我们仍然能够识别车辆在俯仰和偏航方向上的行为 。 参见图7-6了解REMUS在闭环控制下的运动情况，以便与开环阶跃响应数据进行比较。在所示示例中 ，指令要求车辆保持两米的深度。 7.5.1 水平面动力学 车辆对舵角阶跃变化的响应如图7-7所示。对于所示目标，舵鳍被固定在四度，并通过闭环控制指令车辆 保持恒定深度。 这组图表中的相关信息是，对于大约四度的舵角 (J,) ，车辆偏航率约为每秒 10 度。 7.5.2 垂直平面动力学 图 7-8 和 7-9 显示了车辆对鳍角不同暂态阶跃变化的响应。在这两种情况下，车辆在阶跃变化指令发出之 前都处于闭环深度控制下。每个图上的时间刻度已被调整，使阶跃变化指令在时间 t = 2 秒时发生。 在图 7-8 中，车辆俯仰鳍（尾平面）角 J 被固定为负二度。可以看到车辆上升了大约 0.5 米，俯仰变化 大约为 20 度。在该时间间隔结束时，深度和俯仰速度都在增加。在鳍步变的瞬间，车辆显示出略微负的 深度速度（以大约 0.5 米/秒的速度上升）。 在图 7-9 中，车辆纵摆翅角 o， was fixed at eight degrees. The vehicle is seen to dive roughly 0.4 meters, and the pitch change is roughly 18 degrees. Again, at the end of the interval, both the depth and pitch rates were increasing.

---

## Page 105

Fin Angles vs. Time 5 - - - - - -- - - - --- pitch fin 0 .........- -. rudde 0 - . -.. . -.- -. .-. .-.- --..- - ~ ~ ~ ~ ......... ...... ...... .........- n........1. a' 1.-..- .1 0. . . ... . . . 0 1 2 3 4 5 6 7 8 9 10 Vehicle Depth vs. Time ... ..- -. ---. . . . .. . . . . . . .. . . . . . . --. .-- ------.-.-- -.-.-- F-- depthl -. . . . . . . . . -. . . - .. . . . .. . . . . . -. . . -.-.-- -- -.- -.- 1 2 3 4 5 6 7 8 9 10 Vehicle Yaw vs. Time - - -.-.- y a w . . . . . .. .. . ... . . . ... . . . .. . . . .. . . . . . . . -. . ... -. ...-. . ..-. ..-. -........... -................... -... -.... -........ - .. . . . . -.. . . . . . . . . . . . . . -. . . . .. . . . . -. . . . . . . . . -. . . . . -. . ... . . . .. . . . ... . . . . . . . . . . . . -...... -..... -..... -...-. 0 1 2 3 4 5 6 7 8 9 10 Vehicle Pitch and Roll vs. Time -. . .. . . .. . . . .. . . . . - - - ....... ...... ..... .... ...... ... .... ... ..... .... ... ... ... ... ... . . ... ....... ... ..- -.. . . ... . . . .. . . . p itch.. .. .... . - ..-.- . .-.- . -. ..o l. -. - . .. . -. . . . . . .. . . . . . . .. . . . . . . . . . . a) 0 a)-5 0 O -10 cc -15 2 -20 5 0 1 2 3 4 5 Time (seconds) 6 7 8 9 10 Figure 7-3: REMUS Mission Data: Vehicle bounces off the bottom [d980729a, Obj. 6) - 0 E0.5 Ca 0 15 0 120 D3100 80 60 Ca >-40 20- > 0 -C

---

## Page 106

Fin Angles vs. Time 5 - - - - - -- - - - --- pitch fin 0 .........- -. rudde 0 - . -.. . -.- -. .-. .-.- --..- - ~ ~ ~ ~ ......... . . . . . . . . . . . . .........- n........1. a' 1.-..- . 1 0. . . ... . . . 0 1 2 3 4 5 6 7 8 9 10 Vehicle Depth vs. Time ... ..- -. ---. . . . .. . . . . . . .. . . . . . . --. .-- ------.-.-- -.-.-- F - -  depthl -. . . . . . . . . -. . . - .. . . . .. . . . . . -. . . -.-.-- -- -.- -.- 1 2 3 4 5 6 7 8 9 10 Vehicle Yaw vs. Time - - - . - . - y a w . . . . . .. .. . ... . . . ... . . . .. . . . .. . . . . . . . -. . ... -. ...-. . ..-. ..-. - . . . . . . . . . . .  - . . . . . . . . . . . . . . . . . . . -... - . . . . - . . . . . . . . - .. . . . . -.. . . . . . . . . . . . . . -. . . . .. . . . . -. . . . . . . . . -. . . . . -. . ... . . . .. . . . ... . . . . . . . . . . . . - . . . . . . - . . . . . - . . . . . - . . . - . 0 1 2 3 4 5 6 7 8 9 10 Vehicle Pitch and Roll vs. Time -. . .. . . .. . . . .. . . . . - - - ....... ...... ..... .... ...... ... .... ... ..... .... ... ... ... ... ... . . ... ....... ... ..- -.. . . ... . . . .. . . . p itch.. .. .... . - ..-.- . .-.- . -. ..o l. -. - . .. . -. . . . . . .. . . . . . . .. . . . . . . . . . . a) 0 a)-5 0 O -10 cc -15 2 -20 5 0 1 2 3 4 5 Time (seconds) 6 7 8 9 10 图 7-3：REMUS 任务数据：载具从底部反弹 [d980729a, Obj. 6) - 0 E0.5 Ca 0 15 0 120 D3100 80 60 Ca >-40 20- > 0 -C

---

## Page 107

Figure 7-4: Launching and recovering the REMUS vehicle. [Photo courtesy of Rob Goldsborough, WHOI OSL] Figure 7-5: The REMUS Ranger Also in Figure 7-9, the vehicle is shown to require a fin angle of positive four degrees in order to maintain a constant depth in the first two seconds. This suggests that the vehicle was ballasted slightly nose-down. This may be due to internal ballast weights shifting during the launch of the vehicle. Despite the fact that the vehicle was operating under closed-loop heading control at all times, you will notice some heading drift in the data. It is not clear whether this reflects actual vehicle motion, or instrument error.

---

## Page 108

图 7-4：发射和回收 REMUS 车辆。 [Photo courtesy of Rob Goldsborough, WHOI OSL] 图 7-5：REMUS 游侠 在图7-9中，还显示车辆在前两秒内为了保持恒定深度，需要调整鳍角为正四度。这表明车 辆的配重略微向前倾。这可能是由于车辆发射过程中内部配重的移动造成的。 尽管该车辆在整个过程中都处于闭环航向控制下，但您会在数据中注意到一些航向漂移。目 前尚不清楚这是否反映了实际车辆运动，还是仪器误差。

---

## Page 109

Fin Angles vs. Time 0 Cm Vehicle Depth vs Time 0V -e-i-c-l Yaw vs . aLA 0 0.1 0 5 10 15 20 25 Vehicle han vs. Time 0- *0. 0 5 10 15 20 25 Vehicle u and lvs Time -5o 0 5 10 15 20 25 Figure -6: REM S Missin Data:Vehicle u nde col s ie-opcnrl d977 b.4

---

## Page 110

Fin Angles vs. Time 0 Cm Vehicle Depth vs Time 0V -e-i-c-l Yaw vs . aLA 0 0.1 0 5 10 15 20 25 Vehicle han vs. Time 0- *0. 0 5 10 15 20 25 Vehicle u and lvs Time -5o 0 5 10 15 20 25 Figure -6: REM S Missin Data:Vehicle u nde col s ie-opcnrl d977 b.4

---

## Page 111

] Fin Angles vs. Time LL pitch fin 2 0 -. .. - . -. . .. . .- . . .. .-. . .. .-. . .. .-. . .. .-...-...- ...- ru d d e r -2 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Vehicle Depth vs. Time .2 0 .0 2 - . .. - -.. . . . . . . . . . . . . . . . . -. . .. . -. . .. . -. .-.-.-..-.-.- (D E depth 0 .0 4 - -.. -.. . . . . -. -.. . . . . . . . - . .. . . . ..- . .. . . . ..-. . . . . . . ..-. . . 0.1 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Vehicle Yaw vs. Time -20 -.-.-.-.-.-.-.-.-.-.- yaw 00 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Time (seconds) Vehicle Pitch and Roll vs. Time a -10 -60 - -- - o 3. - -. - . . . Time (seconds) Figure 7-7: REMUS Mission Data: Step change in rudder angle. {d981028, Obj. 25]

---

## Page 112

] Fin Angles vs. Time LL pitch fin 2 0 -. .. - . -. . .. . .- . . .. .-. . .. .-. . .. .-. . .. .-...-...- ...- ru d d e r -2 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Vehicle Depth vs. Time .2 0 .0 2 - . .. - -.. . . . . . . . . . . . . . . . . -. . .. . -. . .. . -. .-.-.-..-.-.- (D E depth 0 .0 4 - -.. -.. . . . . -. -.. . . . . . . . - . .. . . . ..- . .. . . . ..-. . . . . . . ..-. . . 0.1 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Vehicle Yaw vs. Time -20 -.-.-.-.-.-.-.-.-.-.- y a w 00 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Time (seconds) Vehicle Pitch and Roll vs. Time a -10 -60 - -- - o 3. - -. - . . . Time (seconds) 图 7-7：REMUS 任务数据：舵角的阶跃变化。{d981028, Obj. 25]

---

## Page 113

Fin Angles vs. Time - pitch tin = 5 -rudder -5 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Depth vs. Time -08-depth ...-..-.- E - 0 .6 -. .. . .. .. . .. .-. . . . . . -. . . . . .-. . . . . .. . . . . .-. -.-.-.- CM 0 0- 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Yaw vs. Time "yawl -510 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Pitch and Roll vs. Time 08 - depth 0 0 0.5 1 1.5 2 2.5 3 3.5 4 Figure 7-8: REMUS Miss hicleaYaw vs.cl Timeigu.{9079,Oj 4 e57 .. . . . . .. . . . . .. .. . . 2 0 . . . . . . . .. .. a. . . . .. ,. . . . . . 1 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . .. . . . . . . . . . .. . . . . . . . . . . . . . . . 0 .............. .. . ... 10......... d: 10 0U 0. . . . ime (seconds) Figure 7-8: REMUS Mission Data: Vehicle pitching up. [d980729b, Obj. 14] 57

---

## Page 114

Fin Angles vs. Time - pitch tin = 5 -rudder -5 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Depth vs. Time - 0 8 - d e p t h ...-..-.- E - 0 .6 -. .. . .. .. . .. .-. . . . . . -. . . . . .-. . . . . .. . . . . .-. -.-.-.- CM 0 0- 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Yaw vs. Time "yawl -510 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Pitch and Roll vs. Time 08 - depth 0 0 0.5 1 1.5 2 2.5 3 3.5 4 Figure 7-8: REMUS Miss hicleaYaw vs.cl Timeigu.{9079,Oj 4 e57 .. . . . . .. . . . . .. .. . . 2 0 . . . . . . . .. .. a. . . . .. ,. . . . . . 1 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . .. . . . . . . . . . .. . . . . . . . . . . . . . . . 0 .............. .. . ... 10......... d: 10 0U 0. . . . ime (seconds) 图 7-8：REMUS 任务数据：车辆抬头。[d980729b, Obj. 14] 57

---

## Page 115

Fin Angles vs. Time W - pitch fin 8 - - rudder . 0 0 0 0 0.5 1 1.5 2 2.5 3 35 4 Vehicle Depth vs. Time depth 0 62 - -.. .... . -- -.-.-.- Ca 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Yaw vs. Time 2 - - --.. ...... .. -.. . -2 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Pitch and Rol vs. Time -5 - - -.. .. - --.. . . .. . -.. ... -.. . . . . . . . . -. .-.-.-.- .8 -- pitch a-- roll -20 0 0.5 1 1.5 2 2.5 3 3.5 4 Time (seconds) Figure 7-9: REMUS Mission Data: Vehicle pitching down. [d980729b, Obj. 22]

---

## Page 116

Fin Angles vs. Time W - pitch fin 8 - - rudder . 0 0 0 0 0.5 1 1.5 2 2.5 3 35 4 Vehicle Depth vs. Time depth 0 62 - -.. .... . -- -.-.-.- Ca 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Yaw vs. Time 2 - - --.. ...... .. -.. . -2 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Pitch and Rol vs. Time -5 - - -.. .. - --.. . . .. . -.. ... -.. . . . . . . . . -. .-.-.-.- .8 -- pitch a-- roll -20 0 0.5 1 1.5 2 2.5 3 3.5 4 Time (seconds) 图 7-9：REMUS 任务数据：车辆俯冲。[d980729b, Obj. 22]

---

## Page 117

Chapter 8 Comparisons of Simulator Output and Experimental Data In this chapter, we will compare the simulator output with the vehicle response data described in Chapter 7. We discuss the discrepancies between the two data sets, and the coefficient adjustments used to correct for them. 8.1 Model Preparation The model was given initial conditions and fin inputs matching the experimental data. Early model comparisons lead the author to adjust some of the vehicle coefficients. 8.1.1 Initial Conditions Each run of the model was given the following initial conditions: Table 8.1: REMUS Parameter Value Simulator Initial Conditions Units Description zg +1. 96e-002 m vertical center of gravity u +1.54e+000 m/s Forward velocity < -5. 00e+000 deg Roll Angle The forward velocity of 1.54 m/s (3 knots) is the operating speed of the vehicle at a propeller RPM of 1500. The initial roll angle is the experimentally-measured steady-state roll offset due to propeller torque. The remaining angles, angular rates, and velocities were entered as zero. Although vehicle rates and velocities were not measured directly in the experiments, it is assumed that they were small. 8.1.2 Coefficient Adjustments The author found it necessary to adjust a subset of the vehicle coefficients derived in Chapter 4 by the factors listed below in Table 8.2. These adjustments were based on comparisons with the experimental data, and were not entirely unexpected. The methods used in Sections 4.2.3 and 4.3.3 to calculate rolling resistance had a high degree of uncertainty. More accurate methods to calculate this rolling resistance and added mass should be explored. Similarly, the strip integration method used in Section 4.2.2 to estimate crossflow drag was understood to be inaccurate. Note that Tables 4.2 and 4.3 list the unadjusted vehicle coefficients, while Appendices B and C list the adjusted vehicle coefficients.

---

## Page 118

第八章 模拟器输出与实验数据的比较 在本章中，我们将把模拟器输出与第7章中描述的车辆响应数据进行比较。我们讨论这两组数据 之间的差异，以及用于纠正这些差异的系数调整。 8.1 模型准备 模型被给予与实验数据相匹配的初始条件和最终输入。早期模型的比较促使作者调整了一些车 辆系数。 8.1.1 初始条件 模型的每一次运行都给出了以下初始条件： Table 8.1: REMUS Parameter Value Simulator Initial Conditions Units Description zg + 1 . 96e-002 m vertical center of gravity u +1.54e+000 m /s Forward velocity < -5. 00e+000 deg Roll Angle 推进器转速为1500 RPM时，车辆的前进速度为1.54米/秒（3节）。初始横滚角是由于推进器 扭矩引起的实验测量的稳态横滚偏移。 其余的角度、角速度和速度被输入为零。虽然在实验中没有直接测量车辆的角速度和速度， 但假设它们很小。 8.1.2 系数调整 作者认为有必要根据下表 8.2 中列出的系数，对第 4 章中得出的部分车辆系数进行调整。 这些调整是基于与实验数据的比较，并且并不完全令人意外。第4.2.3节和第4.3.3节中用于计 算滚动阻力的方法具有很高的不确定性。应当探索更准确的方法来计算这种滚动阻力和附加质 量。同样，第4.2.2节中用于估算横流阻力的条带积分法也被认为是不准确的。 请注意，表 4.2 和 4.3 列出了未调整的车辆系数，而附录 B 和 C 列出了已调整的车辆系数。

---

## Page 119

Table 8.2: Vehicle Coefficient Adjustment Factors Coefficient Adjustment Factor Description K,, 100 Rolling Resistance Moment K 5 Roll Added Mass Moment Y, 10 Sway Resistance Force ZW, 10 Heave Resistance Force Mqq 12.5 Pitch Rate Resistance Moment N,, 10 Yaw Rate Resistance Moment 8.2 Uncertainties in Model Comparison The following uncertainties affected the accuracy of the model comparison: * Vehicle Initial Conditions The greatest uncertainty was the vehicle state at the start of each ex- perimental objective. We were unable to measure currents, wave effects, and non-axial vehicle velocities. which would have all affected the vehicle motion during open-loop maneuvers. * Control Fin Alignment Although the alignment of the vehicle fins was checked before each experimental mission, it was difficult to keep the vehicle control fins from getting knocked during vehicle transportation and launch. This could have resulted in fin misalignments as great as five degrees. " Attitude Sensor Dynamics The vehicle attitude sensor was sensitive to coupling due to vehicle accelerations. Although most likely a small effect, the author did not have the opportunity to characterize these sensor dynamics. 8.3 Horizontal Plane Dynamics Figures 8-1 through 8-5 show the vehicle response to step changes in rudder angle. In Figures 8-1 through 8-4, the vehicle was given zero fin inputs for ten seconds, then four degrees of positive rudder for 25 seconds, then four degrees of negative rudder for 30 seconds. The lower plot in Figure 8-2 shows a vehicle yaw rate of roughly ten degrees per second, which compares well with the experimental data in Figure 7-7, Section 7.5.1. Figure 8-5 shows a direct comparison of the experiment and simulator data. The simulated vehicle yaw rate is shown to be a very close match to the experiment. Discrepancies between the vehicle depth rates, and vehicle pitch and roll angles likely have to do with differences in the simulator initial conditions. 8.4 Vertical Plane Dynamics Unlike the horizontal plane motion, it is important to carefully consider the vehicle response to both positive and negative pitch fin angles, due to the effect of the vehicle center of gravity-center of buoyancy separation. 8.4.1 Vehicle Pitching Up Figures 8-6 through 8-10 show the vehicle response to a step change in pitch fin angle. As shown in Figure 8-10, the vehicle was given zero fin inputs for two seconds, then four degrees of negative pitch fin for two seconds. Figure 8-10 shows a vehicle depth change of roughly 0.5 meters and a pitch change of twenty degrees, which both compare well with the experimental data in Figure 7-8, Section 7.5.2.

---

## Page 120

表 8.2：车辆系数调整因子 Coefficient Adjustment Factor Description K,, 100 Rolling Resistance Moment K 5 Roll Added Mass Moment Y, 10 Sway Resistance Force ZW, 10 Heave Resistance Force Mqq 12.5 Pitch Rate Resistance Moment N,, 10 Yaw Rate Resistance Moment 8.2 模型比较中的不确定性 以下不确定性影响了模型比较的准确性： * Vehicle Initial Conditions 最大的不确定性是在每个实验目标开始时车辆的状态。我们无法测量电 流、波浪影响以及非轴向车辆速度，这些都会影响车辆在开环操作过程中的运动。 * Control Fin Alignment 尽管在每次实验任务之前都检查了车辆鳍片的对齐情况，但在车辆运输和 发射过程中，很难防止车辆控制鳍片被撞击。这可能导致鳍片的错位达到五度之多。 Attitude Sensor Dynamics 车辆姿态传感器对由于车辆加速度引起的耦合很敏感。虽然最可能是一个 小影响，但作者没有机会去刻画这些传感器的动态特性。 8.3 水平面动力学 图 8-1 到图 8-5 显示了车辆对舵角阶跃变化的响应。在图 8-1 到图 8-4 中，车辆在十秒内没有舵鳍输入， 然后舵角为正四度持续 25 秒，再然后舵角为负四度持续 30 秒。 图 8-2 中下方的图显示车辆偏航率大约为每秒十度，这与第 7.5.1 节图 7-7 中的实验数据比较吻合。 图 8-5 显示了实验数据与模拟数据的直接比较。模拟车辆的偏航角速度显示与实验非常接近。车辆纵 向速度以及车辆俯仰角和横滚角的差异可能与模拟器初始条件的不同有关。 8.4 垂直平面动力学 与水平面运动不同，由于车辆重心与浮心分离的影响，必须仔细考虑车辆对正负俯仰鳍角的响应。 8.4.1 车辆抬头 图 8-6 到图 8-10 显示了车辆对俯仰舵角阶跃变化的响应。如图 8-10 所示，车辆在两秒钟内没有舵面输入 ，然后在两秒钟内施加了四度的负俯仰舵角。 图 8-10 显示了车辆深度约为 0.5 米的变化和约二十度的俯仰变化，这两者与第 7.5.2 节图 7-8 中的实验 数据相比较，都符合得很好。

---

## Page 121

4 0 - - .- - - - -- -. ... . -e- x-pos E E 0 CO 200 1 10 2 10 3 10 40 5 10 6 10 70 aL) 1 2 - - - - -.. ... -.. ... .. . . . . -.. . . . . .. . . . . . . 0 8 - -- e-Surge u -- Sway v : -4- Heave w -0 210' 20 30 40 50 60 70 Time in seconds Figure 8-1: REMUS Simulator Data: Linear displacements and velocities for vehicle response in the horizontal plane 61

---

## Page 122

4 0 - - .- - - - -- -. ... . -e- x-pos E E 0 CO 200 1 10 2 10 3 10 40 5 10 6 10 70 aL) 1 2 - - - - -.. ... -.. ... .. . . . . -.. . . . . .. . . . . . . 0 8 - -- e-Surge u -- Sway v : -4- Heave w -0 210' 20 30 40 50 60 70 Time in seconds 图 8-1：REMUS 仿真器数据：车辆在水平面响应的线性位移和速度 61

---

## Page 123

c) 2 -50 - - ----- C0)E 0)- -100-- M)-150 - - - - - - C -200 - -e- Roll $ A Pitch 0 -+- Yawy -250 0 10 20 30 40 50 60 70 10 - -e- Roll rate p -8 - - - - --- ------ '- - A-- Pitch rate q +4 Yaw rate r -10 . . 0 10 20 30 40 50 60 70 Time in seconds Figure 8-2: REMUS Simulator Data: Angular displacements and velocities for vehicle response in the horizontal plane 62 ............. . . . . . . . .

---

## Page 124

c) 2 -50 - - ----- C0)E 0)- -100-- M)-150 - - - - - - C -200 - -e- Roll $ A Pitch 0 -+- Yawy -250 0 10 20 30 40 50 60 70 10 - -e- Roll rate p -8 - - - - --- ------ '- - A-- Pitch rate q +4 Yaw rate r -10 . . 0 10 20 30 40 50 60 70 Time in seconds 图 8-2：REMUS 仿真器数据：车辆在水平面响应的角位移和角速度 62 ............. . . . . . . . .

---

## Page 125

4 .. . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . .v 2 ......... .. ...... : .... I... ikK 0 - -3. 0 10 20 30 40 50 60 70 1.5................. 1................... E 0 10 20 30 40 50 60 70 Time in seconds Figure 8-3: REMUS Simulator Data: Forces and moments for vehicle response in the horizontal plane

---

## Page 126

4 .. . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . .v 2 ......... .. . . . . . . : .... I... ikK 0 - -3. 0 10 20 30 40 50 60 70 1.5................. 1................... E 0 10 20 30 40 50 60 70 Time in seconds 图 8-3：REMUS 模拟器数据：车辆在水平面响应的力和力矩

---

## Page 127

SIMULATOR XYZ Plot N 30 15 20 105 10 0 0 x XZ PLOT 0 10 20 30 X: Forward Displacement [in] -6 -4 P-2 a0 C) N 4 6 8 5 0 E -5 0-10 -15 -20 YZ PLOT -15 - - - 5 -- -..... ..... -..... -15 -10 -5 0 Y: Lateral Displacement [m] XY PLOT 0 - 0 - -2 0 10 20 3C X: Forward Displacement [m] Figure 8-4: REMUS Simulator Data: Vehicle trajectory for vehicle response in the horizontal plane 64

---

## Page 128

SIMULATOR XYZ Plot N 30 15 20 105 10 0 0 x XZ PLOT 0 10 20 30 X: Forward Displacement [in] -6 -4 P-2 a0 C) N 4 6 8 5 0 E -5 0 -1 0 -15 -20 YZ PLOT -15 - - - 5 -- -..... ..... -..... -15 -10 -5 0 Y: Lateral Displacement [m] XY PLOT 0 - 0 - -2 0 10 20 3C X: Forward Displacement [m] 图 8-4：REMUS 模拟器数据：车辆在水平面上的车辆响应轨迹 64

---

## Page 129

-1 - 0 simulat ion o 0.5 1.. . . 15... . . .. . . 2.. .. . 2.. . . . . . ..5 3 . . .. . 35 . 4.4.5.5 05- - - - - -- - - - - - - - . - - - experiment 1 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 --simulation -- experimentI 0 ....................................... 00 -20' 0 0.5 1 1.5 2 25 3 35 4 4.5 5 simulation ---experimen~t : 'ti -- - - - - -- - - - -i 1 0 - - - - . . . - -. ..- -. .- -.-.-- - - -. .-.-- - - - -. .-- - - - - - -. .-- - - - - - -. ..-..-- -.-- - -. .-.-.-.- - -20 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Vehicle Pitch and Roll vs. Time -ssimulation _g . .. .. .. ... .... . . ... .. . . .... ..... .. ........ ...... ..... e.m e . 9? - 6 - -- - - - - - - - -- - - - - - - -- - -- - - - - -- - - - -- - - - 6 . . ... .- -- - .. - . . . . . . . .. .. . . . . ----. .. - - - -. --- - - -10 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Time (seconds) Figure 8-5: REMUS Simulator Data: Comparison plots for vehicle response in the yaw plane 65

---

## Page 130

-1 - 0 simulat ion o 0.5 1.. . . 15... . . .. . . 2.. .. . 2.. . . . . . ..5 3 . . .. . 35 . 4.4.5.5 05- - - - - -- - - - - - - - . - - - experiment 1 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 --simulation -- experimentI 0 ....................................... 00 -20' 0 0.5 1 1.5 2 25 3 35 4 4.5 5 simulation ---experimen~t : 'ti -- - - - - -- - - - -i 1 0 - - - - . . . - -. ..- -. .- - . - . - -  - - -. .-.-- - - - -. .-- - - - - - -. .-- - - - - - -...-..-- -.--  - -. .-.-.-.- - -200 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Vehicle Pitch and Roll vs. Time -ssimulation _g . .. .. .. ... .... . . ... .. . . .... ..... .. ........ ...... ..... e.我  。 9? - 6 - -- - - - - - - - -- - - - - - - -- - -- - - - - -- - - - -- - - - 6 . . ... .- -- - .. - . . . . . . . .. .. . . . . ----. .. - - - -. --- - - -10 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 Time (seconds) 图 8-5：REMUS 模拟器数据：车辆在偏航平面响应的比较图 65

---

## Page 131

-1 1.4 1 .2 - -.-.- -. Ca ~0.8 - -0------ Surge u -- Sway v 2 0.6..... -.-.. H............ Heave w 0. ......... ......................... 0 2 - -- -i -~ - - -0.2 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds Figure 8-6: REMUS Simulator Data: Linear displacements and velocities for vehicle pitching up 66 -e- x-pos -A- y-pos - +e z-pos - - . . . . . - - . . . . . . . .

---

## Page 132

-1 1.4 1 .2 - -.-.- -. C a ~0.8 - -0------ Surge u -- Sway v 2 0 .6 ..... -.-.. H............ Heave w 0. . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . 0 2 - -- -i -~ - - -0.2 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds 图 8-6：REMUS 模拟器数据：车辆俯仰向上时的线性位移和速度 66 -e- x-pos -A- y-pos - +e z-pos - - . . . . . - - . . . . . . . .

---

## Page 133

25 -. - - - - -e- Rollo Pitch 0 20 - - - -.- Yaw E 1 0 - .... .. --.. .... ....- -. . . . . -- -. . . . . - . . .. . . . . -5 -10- 0 0.5 1 1.5 2 2.5 3 3.5 4 -&- Roll rate p 8 - - - - - - - --- + Pitch rate q 'a- -0 Yaw rate r : -2- 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds Figure 8-7: REMUS Simulator Data: Angular displacements and velocities for vehicle pitching up 67

---

## Page 134

25 -. - - - - -e- Rollo Pitch 0 20 - - - -.- Yaw E 1 0 - .... .. --.. .... ....- -. . . . . -- -. . . . . - . . .. . . . . -5 -10- 0 0.5 1 1.5 2 2.5 3 3.5 4 -&- Roll rate p 8 - - - - - - - --- + Pitch rate q 'a- -0 Yaw rate r : -2- 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds 图 8-7：REMUS 模拟器数据：车辆俯仰上抬的角位移和速度 67

---

## Page 135

-ex 0 0. 1 1.- 253-. 4" - ... . .. . .. .. -. -.. . .. . . -.Z 1.4 - - 1 .2 -. -. - -- - .- . * E L- -..... .... -... - 02- 05 1 1.5 2 2.5 3 3.5 4 Time in seconds Figure 8-8: REMUS Simulator Data: Forces and moments for vehicle pitching up

---

## Page 136

-ex 0 0. 1 1.- 253-. 4" - ... . .. . .. .. -. -.. . .. . . -.Z 1.4 - - 1 .2 -. -. - -- - .- . * E L- -..... .... -... - 02- 05 1 1.5 2 2.5 3 3.5 4 Time in seconds 图 8-8：REMUS 模拟器数据：车辆俯仰向上时的力和力矩

---

## Page 137

SIMULATOR XYZ Plot -5 - PO 4 23 N2 X 0 XZ PLOT -2 aOt 0 1 2 3 4 5 X: Forward Displacement [m] -0.4 _0.3 0.0-0.2 -0.1 YZ PLOT .. . . . .. . . . . -- -...... - -... -. .- .. -. -. . -. . -. -. .- -0.2 -0.1 0 0.1 0.2 0.3 Y: Lateral Displacement [m] XY PLOT E 0 1 2.. . .. . . . 3.. . 4.. . 5. 0 F X: Forward Displacement [in] Figure 8-9: REMUS Simulator Data: Vehicle trajectory for vehicle pitching up 69 ............... ..................... ........ ..................... ....... ...... .. ....... . .... ........ .......

---

## Page 138

SIMULATOR XYZ Plot -5 - PO 4 23 N2 X 0 XZ PLOT -2 aOt 0 1 2 3 4 5 X: Forward Displacement [m] -0.4 _0.3 0.0 -0 .2 -0.1 YZ PLOT .. . . . .. . . . . -- -...... - -... -. .- .. -. -. . -. . -. -. .- -0.2 -0.1 0 0.1 0.2 0.3 Y: Lateral Displacement [m] XY PLOT E 0 1 2.. . .. . . . 3.. . 4.. . 5. 0 F X: Forward Displacement [in] 图 8-9：REMUS 仿真器数据：车辆俯仰上升的车辆轨迹 69 ............... ..................... ........ ..................... ....... ...... .. ....... . .... ........ .......

---

## Page 139

lA simulation -0.5 - experiment . C a 0 0 -.. .. . . - . . 0.5 0 0.5 1 1.5 2 2.5 3 3.5 4 5 - -- - - - . -. -. ---. - -. -.. . . --.. . .. . -.- -.-.- -.- . C - - -- simulation (-D experiment -5- 0 0.5 1 1.5 2 2.5 3 3.5 4 4 0 - -.. . . - -.. . . . . -.. .. .. . . . -- simulation 30 - --. experiment] --. . -.... . .. . . - 0 - -- - . -20 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Pitch and Roll vs. Time ~0-- --- simulation -2- - - experiment -8- . 30 . experim ent ... .... . . . . . .. . . . . 01 -100 0.5 1 1.5 2 2.5 3 3.5 4 Time (seconds) Figure 8-10: REMUS Simulator Data: Comparison plots for vehicle pitching up

---

## Page 140

啦 simulation -0.5 - experiment . C a 0 0 -.. .. . . - . . 0.5 0 0.5 1 1.5 2 2.5 3 3.5 4 5 - -- - - - . -. -. ---. - -. -.. . . --.. . .. . -.- -.-.- -.- . C - - -- simulation (-D experiment -5- 0 0.5 1 1.5 2 2.5 3 3.5 4 4 0 - -.. . . - -.. . . . . -.. .. .. . . . -- simulation 30 - --. experiment] --. . -.... . .. . . - 0 - -- - . -20 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Pitch and Roll vs. Time ~0-- --- simulation -2- - - experiment -8- . 30 . experim ent ... .... . . . . . .. . . . . 01 -100 0.5 1 1.5 2 2.5 3 3.5 4 Time (seconds) 图 8-10：REMUS 模拟器数据：车辆俯仰上仰比较图

---

## Page 141

8.4.2 Vehicle Pitching Down Figures 8-11 through 8-15 show the vehicle response to a step change in pitch fin angle. As shown in Figure 8-15, the vehicle was given zero fin inputs for two seconds, then eight degrees of positive pitch fin for two seconds. Figure 8-15 shows a vehicle depth change of roughly 0.6 meters and a pitch change of thirty degrees, which both compare well with the experimental data in Figure 7-9, Section 7.5.2. The model pitch rate is slightly higher than the experimental data, but this could be due a difference in initial conditions.

---

## Page 142

8.4.2  车辆前倾 图 8-11 到 8-15 显示了车辆对俯仰舵角阶跃变化的响应。如图 8-15 所示，车辆在两秒钟内未给 舵输入，然后在两秒钟内给出八度正俯仰舵角。 图 8-15 显示车辆深度变化约为 0.6 米，俯仰角变化为 30 度，这两者与第 7.5.2 节 图 7-9 中的 实验数据比较吻合。模型俯仰角变化率略高于实验数据，但这可能是由于初始条件的差异造成 的。

---

## Page 143

pos I 4 . . . .. . .. . . .. . . . . . . =. . . . . . . . ".*.*.-. . CL as 0 0.5 1 1.5 2 2.5 3 3.5 4 1 .2 -. .. .. . - . . -. . . . - . . . . .. . . . 0 .8 -.. .. . .- .. . -.. . - -6- Surge u 0.6 .- - -- ---- ,r Sway v -- 0+ Heave w 0 .4 - -.. . . . . . . . . . .. . . . . .. . . -0 .2 - -.. ..-. -0.2--4 -. 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds Figure 8-11: REMUS Simulator Data: Linear displacements and velocities for vehicle pitching down 72 -e- x- I - - .... ,..-.y 5 ... ....... ...- .... . .......... .. . . . . . . . . .. . . . . . . . . ... . . ............ ....... ............ ...............

---

## Page 144

pos I 4 . . . .. . .. . . .. . . . . . . =. . . . . . . . ".*.*.-. . CL as 0 0.5 1 1.5 2 2.5 3 3.5 4 1 .2 -. .. .. . - . . -. . . . - . . . . .. . . . 0 .8 -.. .. . .- .. . -.. . - -6- Surge u 0.6 .- - -- ---- ,r Sway v -- 0+ Heave w 0 .4 - -.. . . . . . . . . . .. . . . . .. . . -0 .2 - -.. ..-. -0.2--4 -. 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds 图 8-11：REMUS 模拟器数据：车辆俯仰向下的线性位移和速度 72 -e- x- I - - .... ,..-.y 5 ... ....... ...- .... . .......... .. . . . . . . . . .. . . . . . . . . ... . . ............ ....... ............ ...............

---

## Page 145

~1 00 ~-205 CL - 3 0 - -. - -.- -. -e- RolloI -3 -A- Pitch 0 +0 Yawx -40 0 0.5 1 1.5 2 2.5 3 3.5 4 -E)- Roll rate p .... .... ....... ... .... ... .... ... .. .... ... .A - P itch rate q Yaw rate r - 2 - . . .. ... . .. . .-. .-.-.- - -. . .-. ... . 0) CD - -6 -... -..- - 8 -. . . . -. . . -.-. .-.- -.-. ..4 .. ..... . ...... . .. .... . -.- -.-. .-.- -.-. .-. .-.- -.-. .-.- -.-. .-. '.*.* *....-.* *.-. .... * *..*. -16 - -- 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds Figure 8-12: REMUS Simulator Data: Angular displacements and velocities for vehicle pitching down

---

## Page 146

~一 00 ~-205 C L - 3 0 - -. - -.- -. -e- RolloI -3 -A- Pitch 0 +0 Yawx -40 0 0.5 1 1.5 2 2.5 3 3.5 4 -E)- Roll rate p .... .... ....... ... .... ... .... ... .. .... ... .A - P itch rate q Yaw rate r - 2 - . . .. ... . .. . .-. .-.-.- - -. . .-. ... . 0) C D - -6 -... -..- - 8 -. . . . -. . . -.-. .-.- -.-. ..4 .. ..... . ...... . .. .... . -.- -.-. .-.- -.-. .-. .-.- -.-. .-.- -.-. .-. '.*.* *....-.* *.-. .... * *..*. -16 - -- 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds 图 8-12：REMUS 模拟器数据：车辆俯仰向下的角位移和角速度

---

## Page 147

2 -.-..-.- -.- - ex -Y ... ...... ...... .. .. .. .. .. .. .. .. .. .. .. .. . .. .. .. . .. .- z. . -2 -- - -- - Z - 5 - -.. . . . - ..- .-. .-.- 0 0.5 1 1.5 2 2.5 3 3.5 4 z S-0.5 C E -1 c) 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds Figure 8-13: REMUS Simulator Data: Forces and moments for vehicle pitching down 74 ....................... . . . . . . . . . . . . . . . . . . ... . . . . . . . . . . . . . . . . . . . . .. .. . . .

---

## Page 148

2 -.-..-.- -.- - ex -Y ... ...... ...... .. .. .. .. .. .. .. .. .. .. .. .. . .. .. .. . .. .- z. . -2 -- - -- - Z - 5 - -.. . . . - ..- .-. .-.- 0 0.5 1 1.5 2 2.5 3 3.5 4 z S - 0 .5 C E -1 c) 0 0.5 1 1.5 2 2.5 3 3.5 4 Time in seconds 图 8-13：REMUS 模拟器数据：车辆俯仰向下的力和力矩 74 ....................... . . . . . . . . . . . . . . . . . . ... . . . . . . . . . . . . . . . . . . . . .. .. . . .

---

## Page 149

YZ PLOT -0. -02 0-. -. . . . . .. . . . . -. . .. ..-. . SIMULATOR XYZ Plot XZ PLOT 1 2 3 4 X: Forward Displacement [m] 0. 0 L 0. 0 0 0 0 CE * 0 1 2 3 4 .5 .6 0 -0.4 -0.2 0 0.2 Y: Lateral Displacement [m] XY PLOT 1 2 3 4 X: Forward Displacement [m] Figure 8-14: REMUS Simulator Data: Vehicle trajectory for vehicle pitching down -1.5 -1 0 -- 0.5- E 0. Ni 1.5- 2 0 2......... I.................. 1.. ................. ...... 2 - - --.-.- --. . - . . . . - , ....... ... ..= -.. ... .- ."

---

## Page 150

YZ PLOT -0. -02 0-. -. . . . . .. . . . . -. . .. ..-. . SIMULATOR XYZ Plot XZ PLOT 1 2 3 4 X: Forward Displacement [m] 0. 0 L 0. 0 0 0 0 CE * 0 1 2 3 4 .5 .6 0 -0.4 -0.2 0 0.2 Y: Lateral Displacement [m] XY PLOT 1 2 3 4 X: Forward Displacement [m] 图 8-14：REMUS 仿真器数据：车辆俯仰下沉的车辆轨迹 -1.5 -1 0 -- 0.5- E 0. Ni 1.5- 2 0 2......... I.................. 1.. ................. ...... 2 - - --.-.- --. . - . . . . - , ....... ... ..= - . . ... .- ."

---

## Page 151

- 0 .5 --. . . . .. . . . . ... . . . . -simulation E 0 -. -. experiment 0 .5 - -.. . . .. . .. . . . . . . . . a.a 0 0.5 1 1.5 2 2.5 3 3.5 4 05 - i!! -5 -.. .- .0 U)D - simulation - experiment -10 - 0 0.5 1 1.5 2 2.5 3 3.5 4 0 2 0 - - . . . ... . . . -. . .. . -. .. . . .. . .. . . -. ..- -, -20 - simulation - - . experment d- -40- -0 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Pitch and Roll vs. Time 0 -. . . .. . . . .. .. . . . -simulation - experiment -42- -6 0) -8 -.. ..... . ... . . . . . . -100 0.5 1 1.5 2 2.5 3 3.5 4 Time (seconds) Figure 8-15: REMUS Simulator Data: Comparison plots for vehicle pitching down

---

## Page 152

- 0 .5 --. . . . .. . . . . ... . . . . -simulation E 0 -. -. experiment 0 .5 - -.. . . .. . .. . . . . . . . . a.a 0 0.5 1 1.5 2 2.5 3 3.5 4 05 - i!! -5 -.. .- .0 U)D - simulation - experiment -10 - 0 0.5 1 1.5 2 2.5 3 3.5 4 0 2 0 - - . . . ... . . . -. . .. . -. .. . . .. . .. . . -. ..- -, -20 - simulation - - . experment d- -40- -0 0 0.5 1 1.5 2 2.5 3 3.5 4 Vehicle Pitch and Roll vs. Time 0 -. . . .. . . . .. .. . . . -simulation - experiment -42- -6 0) -8 -.. ..... . ... . . . . . . -100 0.5 1 1.5 2 2.5 3 3.5 4 Time (seconds) 图 8-15：REMUS 模拟器数据：车辆俯仰向下的比较图

---

## Page 153

Chapter 9 Linearized Depth Plane Model and Controller This chapter describes the depth-plane linearization of the vehicle equations of motion and the coefficients used in those equations. It demonstrates the use of that model to design a simple inner- and-outer (pitch-and-depth) loop PD depth controller. Finally, this chapter shows how real world effects such as environmental disturbances, sensor noise and actuator non-linearities can be added to the model. Although this chapter covers only the depth-plane model, the equations of motion and vehi- cle coefficients are explained in sufficient detail to allow the development of a more sophisticated linearized, decoupled model in five degrees of freedom (disallowing vehicle roll). 9.1 Linearizing the Vehicle Equations of Motion The equations governing the motion of the vehicle are described in Chapter 3. We will briefly describe the linearization of the vehicle kinematics, rigid-body dynamics, and mechanics. 9.1.1 Vehicle Kinematics The vehicle kinematic equations are developed in Section 3.2. Note that the rotational coordinate transform matrix J 2 (r 2), described in Equation 3.5, is not defined for cos9 = '. This will not be a problem, given that when we linearize the model we will be assuming small vehicle perturbations about 0 = 0. As we are assuming pure depth-plane motion, we need only consider the body-relative surge velocity u, heave velocity w, and pitch rate q, and the earth-relative vehicle forward position x, depth z, and pitch angle 0. We will set to zero all other velocities (v, p, r), and drop the equations for any out-of-plane terms. By these assumptions, Equation 3.1 and Equation 3.4 result in the following relationships between body- and earth-fixed vehicle velocities: cos Ou + sin Ow z = - sin u + cos Ow (9.1) O=q We will linearize these equations by assuming that the vehicle motion consists of small perturbations around a steady point. U in this case represents the steady-state forward velocity of the vehicle;

---

## Page 154

第九章 线性化深度平面模型与控制器 本章介绍了车辆运动方程在深度平面上的线性化以及这些方程中使用的系数。它演示了如何使 用该模型设计一个简单的内外（俯仰和深度）回路 PD 深度控制器。最后，本章展示了如何将现 实世界的影响因素，如环境干扰、传感器噪声和执行器非线性，添加到模型中。 尽管本章仅涵盖深度平面模型，但运动方程和车辆系数的解释足够详细，可用于开发更复杂 的线性化、解耦的五自由度模型（不允许车辆侧倾）。 9.1  车辆运动方程的线性化 车辆运动的方程在第3章中进行了描述。我们将简要描述车辆运动学、刚体动力学和力学的线性 化。 9.1.1  车辆运动学 车辆运动学方程在第3.2节中进行了推导。注意，公式3.5中描述的旋转坐标变换矩阵 J 2 (r 2) 对 c os9 =' 未定义。这不会成为问题，因为当我们对模型进行线性化时，我们将假设车辆在 0 = 0 附 近有小扰动。 由于我们假设纯深度平面运动，我们只需要考虑相对于船体的纵向速度 u, 、升降速度 w,  和 俯仰角速度 q，以及相对于地面的车辆前向位置 x、深度 z,  和俯仰角 0。我们将把所有其他速度 (v, p, r),  设为零，并去掉任何平面外项的方程。 根据这些假设，方程 3.1 和方程 3.4 导致了车体固定和地球固定车辆速度之间的以下关系： cos Ou + sin Ow z =  - sin u + cos Ow (9.1) O=q 我们将通过假设车辆运动由围绕稳态点的小扰动组成来线性化这些方程。在这种情况下，U  表 示车辆的稳态前进速度；

---

## Page 155

heave and pitch are linearized about zero. U= U + U' w w' (9.2) q q We will also use the Maclaurin expansion of the trigonometric terms: 03 05 sinG =0-- +- - 3! 5! (9.3) o2 g4 cos0= 1 - + + ... Applying these linearizations and dropping any higher-order terms results in the following linearized kinematic relationships between earth- and body-fixed velocities: x-U + Ow -UO + w (9.4) 0=q 9.1.2 Vehicle Rigid-Body Dynamics The vehicle kinematic equations are developed in Section 3.3. As in the equations for vehicle kinematics, we will simplify the equations for the rigid body dynamics (Equation 3.8) to a description of pure depth-plane motion. We will set to zero all unrelated terms (v, p, r, yg), and drop the equations for out-of-plane vehicle motion: ( Xz= m(i6+wq-xgq2 +zg4) SZ= m (w -uq-z gq2 _ xg4) (9.5) E M = Iy4 + m[zg(it + wq) - xg(ti - uq)] Substituting the linearized velocities from Equation 9.2 and dropping any higher-order terms results in the following linearized equations of motion: ( X= m[it+zg4] (:Z= m[tb-x,4-Uq] (9.6) (3 M =Iyy + m[zgit - xg( - Uq)} 9.1.3 Vehicle Mechanics Our assumptions about the vehicle mechanics are identical to those developed in Section 3.4. In the linearized vehicle equations of motion, external forces and moments ( Fext = Fhydrostatic + Fft + Fdrag + Fcontroi + Fdisturbance are described in terms of vehicle coefficients. For example, linearized axial drag I- 1 Fd 1 Fd - pcdA U u = XUU - X" = = pc PdAf U These linearized coefficients are based on a combination of theoretical equations and empirically- derived formulae. Note that we neglect the forward force due to body lift as it is a nonlinear term.

---

## Page 156

纵摇和横摇在零点附近被线性化。 U= U + U' w w' (9.2) q q 我们还将使用三角项的麦克劳林展开式： 03 05 sinG =0-- +- - 3! 5! (9.3) o2 g4 c o s 0 =  1 - + + ... 应用这些线性化并去掉任何高阶项，得到地固系和体固系速度之间的以下线性化运动学关系： x-U + Ow -UO + w (9.4) 0=q 9.1.2  车辆刚体动力学 车辆运动学方程在第3.3节中进行了推导。与车辆运动学方程一样，我们将把刚体动力学方程（方程3.8） 简化为纯深度平面运动的描述。我们将把所有无关项 (v, p, r, yg),  设为零，并删除关于车辆平面外运动 的方程： ( Xz= m(i6+wq-xgq2 + zg 4 ) SZ= m (w -uq-z gq2 _ x g 4 ) (9.5) E M = Iy 4  + m [zg(it + wq) - xg(ti - uq)] 将方程 9.2 中线性化的速度代入，并去掉任何高阶项，得到以下线性化运动方程： ( X= m[it+zg4] (:Z= m [ tb - x ,4 - U q ] (9.6) (3 M  = I y y  + m[zgit - xg( - Uq)} 9.1.3  车辆机械 我们关于车辆力学的假设与第3.4节中提出的假设完全相同。在线性化的车辆运动方程中，外部力和力矩 ( Fext = Fhydrostatic + Fft + Fdrag + Fcontroi + Fdisturbance 以车辆系数来描述。例如，线性化的轴向阻力 I- 1 Fd 1 Fd - pcdA U u = XUU - X" = = pc PdAf U 这些线性化系数基于理论方程和经验推导公式的结合。注意，我们忽略了由于机体升力产生的前向力 ，因为它是一个非线性项。

---

## Page 157

9.2 Linearized Coefficient Derivation The various parameters necessary to derive the vehicle coefficients are either included in the section describing the coefficient, or are listed in the Appendix. 9.2.1 Hydrostatics The nonlinear equations for hydrostatic forces and moments (see Equation 4.3) are developed in Section 4.1. We will simplify these by dropping the out-of-plane terms, assuming that Xg Xb, and using the Maclaurin expansion of the trigonometric terms (see Equation 9.3). We then drop the higher-order terms, as well as any resulting constant terms. This yields the following linearized hydrostatic equations: Xo = - (W - B)( MO = - (zgW - ZbB)O 9.2.2 Axial Drag Vehicle axial drag can be expressed in Equation 4.6. Linearizing this equation using the relationship given in Equation 9.2, results in the following: 1 X = -- pcdAf (U +u)|U +uI 2 (9.8) X = - 1pCdAf (U2 + 2Uu+U2) Assuming u<U, U>0 (9.9) and dropping any constant terms results in the following linearized axial drag coefficient: X p = -pCdAf U (9.10) 9.2.3 Crossflow Drag Vehicle crossflow drag is discussed in Section 4.2.2. In order to linearize the quadratic crossflow drag coefficients described in Equation 4.8, we must linearize the heave and pitch perturbation velocities about zero. This is accomplished by fitting a slope to the parabolic velocity-squared curve, as show in Figure 9-1. W2 (9.11) q 2 mqq The actual values used in this parameterization are given in Table 9.1. The estimates for maxi- mum expected heave and pitch velocity were taken from field data. Table 9.1: Linearized Velocity Parameters Parameter Value Units Description Wmax +2. 00e-001 m/s Maximum Heave Perturbation qmax +5.00e-001 rad/s Maximum Pitch Perturbation mW +1.20e-001 m/s Heave Coefficient mq +3. Ooe-001 rad/s Pitch Coefficient

---

## Page 158

9.2 线性化系数推导 推导车辆系数所需的各种参数要么包含在描述该系数的部分，要么列在附录中。 9.2.1 静力学 在第4.1节中，提出了水静力作用力和力矩的非线性方程（见方程4.3）。我们将通过忽略面外项 、假设 Xg Xb,  并使用三角函数项的Maclaurin展开（见方程9.3）来简化这些方程。然后我们去 掉高阶项以及任何由此产生的常数项。这样得到了以下线性化的水静力方程： X o  = - (W - B)( MO = - (zgW  - ZbB)O 9.2.2  轴向阻力 车辆轴向阻力可以用方程4.6表示。利用方程9.2给出的关系对该方程线性化，得到如下结果： 1 X = -- pcdAf (U +u)|U +uI 2 (9.8) X = - 1pCdAf (U2 + 2Uu+U2) 假设 u < U , U > 0 (9.9) 去掉任何常数项后，得到以下线性化轴向阻力系数： X p = -pCdAf U (9.10) 9.2.3 横流阻力 车辆横向阻力在第4.2.2节中进行了讨论。为了对方程4.8中描述的二次横向阻力系数进行线性化 ，我们必须围绕零对升沉和俯仰扰动速度进行线性化。这可以通过对抛物线型速度平方曲线拟 合斜率来实现，如图9-1所示。 W2 (9.11) q 2  mqq 在此参数化中使用的实际数值列于表9.1中。最大预期升沉和纵摇速度的估计值取自现场数 据。 表 9.1：线性化速度参数 Parameter Value Units Description Wmax +2. 00e-001 m/s Maximum Heave Perturbation qmax +5.00e-001 rad/s Maximum Pitch Perturbation mW +1.20e-001 m/s Heave Coefficient mq +3. Ooe-001 rad/s Pitch Coefficient

---

## Page 159

0.025- . 0.02 - - - - - - - 0 .0 15 - - - --- - - - - - - - 0.01- 0.005 - 0 0 0.02 0.04 006 0.08 01 0.12 0.14 0.16 0.18 0.2 Linear Velocity (m/s) Figure 9-1: Perturbation Velocity Linearization Substituting these parameters results in the following linear equations for crossflow drag: 1 2 Ze = 2 Pdcw j 2R(x)dx - 2 - PSfincdfmw 1 f1 2 ( Me = PCd cmw 2xR(x)dx - 2 xfin- pSancamw) (9.12) Zqc 2 pcacmq J 2xlx|R(x)dx - 2xfin Ixfinn - PSfincdfmq) Me - -pcdm jXb 2 2X 3R(x)dx - 2x3n ( pSfncdfm) See Table A.2 for the limits of integration. 9.2.4 Added Mass Vehicle added mass is discussed in Section 4.3. By substituting linearized velocities and dropping the out-of-plane and higher-order terms, the non-linear equations (see Equation 4.15) reduce to the following: XA = X0u6 + Z 4mqq ZA = Zoe + Z4q - XaUq (9.13) MA = Mwh + Mq - (Z, - X,)Uw - ZqUq Linearized axial added mass is still given by the equation: Xu = -mn (9.14)

---

## Page 160

0.025- . 0.02 - - - - - - - 0 .0 15 - - - --- - - - - - - - 0.01- 0.005 - 0 0 0.02 0.04 006 0.08 01 0.12 0.14 0.16 0.18 0.2 Linear Velocity (m/s) 图 9-1：扰动速度线性化 代入这些参数得到交叉流阻力的以下线性方程： 1 2 Z e  = 2 P d c w  j 2R(x)dx - 2 - PSfincdfmw 1 f1 2 ( M e  = PCd cm w 2 x R (x )d x  - 2 xfin- pSancam w ) (9.12) Zqc 2 pcacmq J 2xlx|R(x)dx - 2xfin Ixfinn - PSfincdfm q) M e - -p c d m jXb 2 2X 3R(x)dx - 2x3n ( p S fn c d fm ) 参见表 A.2 了解积分的界限。 9.2.4 添加的质量 车辆附加质量在第4.3节中讨论。通过代入线性化速度并去掉面外和高阶项，非线性方程（见方程4.15）简 化为如下形式： XA = X0u6 + Z 4mqq ZA = Zoe + Z4q - XaUq (9.13) MA = Mwh + Mq - (Z, - X ,)U w  - ZqUq 线性化轴向附加质量仍由以下方程给出： X u  = -mn (9 .1 4 )

---

## Page 161

and crossflow added masses are given by the equations: /2f of2 b2 Z. = -- m 22(x)dx - m 2 2f (x)dx - m 2 2(x)dx X t I f fif2 Mb = Z4 = - xm 22 (x)dx - j xm 22f(x)dx - j xm 2 2 (x)dx (9.15) / f Xf2 Xb2 M,= -- x 2 m 22(x)dx- x 2 m 22f(x)dx- x 2 m 22 (x)dx It f Tf2 See Table A.2 for the limits of integration. The remaining cross-terms result from added mass coupling: Xqa = Z4mq Zqa = -XiU Mwa = -(ZI, - Xa)U Mqa = -Z4U The added mass cross-term MA is also called the Munk Moment, and relates to the pure moment experienced by a body in ideal, inviscid flow at an angle of attack. 9.2.5 Body Lift Force and Moment The non-linear equations for vehicle body lift are discussed in Section 4.4. Linearizing the vehicle velocities according to Equation 9.2 and substituting into Equation 4.27 the relationships given above, we are left with the following, linearized equations for vehicle body lift: ZL - pd 2cydpUw (9.17) which results in the body lift coefficient : Zw= pd 2C ydfU (9.18) and body lift moment: M. = pdcdgXcU (9.19) 9.2.6 Fin Lift Vehicle fin lift is discussed in Section 4.5 Dropping the out-of-plane terms in the equations for effective fin velocities (see Equation 4.40) leads to the following: Ufin = U (9.20) wnn = W - Xfnnq Effective fin angle 6c can be expressed as 5c = Js + #e (9.21) where 6, is the stern plane angle, and 3e the effective angle of attack of the fin zero plane, as shown

---

## Page 162

并且横向流增加的质量由以下方程给出：/2f of2 b 2 Z. = -- m 22(x)dx - m 2 2f (x)dx - m 2 2(x)dx X t I f fif2 M b  = Z4 = - xm 22 (x)dx - j xm 22f(x)dx - j xm 2 2 (x)dx (9.15) / f Xf2 Xb2 M ,=  -- x 2 m 22(x)dx- x 2 m 22f(x)dx- x 2 m 22 (x)dx It f Tf2 有关积分限，请参见表 A.2。 剩余的交叉项是由附加质量耦合产生的： X qa = Z4mq Zqa = - X i U Mwa = -(ZI, - Xa)U Mqa = -Z4U 附加质量交叉项 MA  也称为 Munk 力矩，并与物体在理想不可压流中以攻角所经历的纯力 矩有关。 9.2.5  车身提升力和力矩 第4.4节讨论了车辆车身升力的非线性方程。根据方程9.2对车辆速度进行线性化，并将上述关系 代入方程4.27后，我们得到以下车辆车身升力的线性化方程： ZL - pd 2cydpUw (9.17) 这导致了车身升力系数： Zw = pd 2C y d f U (9.18) 车身抬升时刻： M. = pdcdgXcU (9.19) 9.2.6 鳍升力 车辆鳍升力在第4.5节中讨论 在有效翅片速度的方程中（见方程4.40）去掉平面外项，得到以下结果： Ufin = U (9.20) wnn = W - Xfnnq 有效鳍角 6c  可以表示为 5 c = J s  + #e (9.21) 其中 6,  是尾舵平面角，3 是鳍零平面的有效攻角，如图所示

---

## Page 163

in Figure 4-2. This effective angle is expressed as #e = _- I (w - xfnq) (9.22) Ufin U After linearizing the velocities in Equations 4.44 and 4.45 according to Equation 9.2 results in the following sets of fin lift coefficients: Z6, = -pcL.Sfi.nU2 1 Zf = 2 pcL.SfinnU (9.23) Zqf = PCLaSfinXfinU and fin moment coefficients: M., = PCLaSfinXfinU 1 Mf = IpcL aSfnxnfinU (9.24) 1 Mf = PCLaSfinXflnU 9.2.7 Combined Terms The sum of the depth-plane forces and moments on the vehicle can be expressed as: S X = X?6 + Xuu+ Xqq+ Xo9 ( Z = Zee + Z4q + Zww + Zqq + Z6,6 (9.25) ( M = Mmeb + M74q + Muw + Mqq + Mo0 + M6,6, where Z" = Z"e + Z., + Z.5 Mf. = M.e + M.a + M.i + M,5(926 Mwc±Ma±Mw±Mwf(9.26) Zq = Zqc + Zqa + Zqf Mq = Mqc + Mqa + Mqf The values for these combined terms are given in Table 9.2. 9.2.8 Linearized Coefficients The final values for the linearized coefficients are given below in Table 9.3. 9.3 Linearized Equations of Motion We will now combine the equations developed in the preceding chapters to develop the linearized equations of motion.

---

## Page 164

在图 4-2 中。这个有效角度表示为 #e = _- I (w - xfnq) (9.22) Ufin U 按照方程 9.2 对方程 4.44 和 4.45 中的速度线性化后，得到以下一组鳍升力系数： Z6, = -pcL .Sfi.nU 2 1 Zf = 2 pcL.SfinnU (9.23) Zqf = PCLaSfinXfinU 和鳍端力矩系数： M ., = PCLaSfinXfinU 1 Mf = IpcL  aSfnxnfinU (9.24) 1 M f  = PCLaSfinXflnU 9.2.7  联合条款 车辆在纵深平面上的力和力矩之和可以表示为： S X = X?6 + Xuu+  Xqq+ Xo9 ( Z  = Z ee + Z4q + Zww + Zqq + Z6,6 (9.25) ( M  =  Mmeb + M74q + M uw + Mqq + Mo0 + M6,6, 哪里 Z" = Z"e + Z., + Z.5 Mf. = M .e + M .a  + M .i + M,5(92六 Mwc±Ma±Mw±Mwf(9.26) Zq = Zqc + Zqa + Zqf Mq = Mqc + Mqa + Mqf 这些组合项的数值见表9.2。 9.2.8  线性化系数 那个 fi线性化系数的最终值如下所示，以 T 为单位 能够 9.3. 9.3  线性化运动方程 我们现在将结合前几章中推导的方程，以推导运动的线性化方程。

---

## Page 165

Table 9.2: Combined Linearized Coefficients Value -1. 57e+001 -3.45e+001 -1.64e+001 +1.20e-001 +1. 44e+000 -1. 12e+001 M.c -4.03e-001 Ma +5.34e+001 MWI -1.11le+001 Mef -1.12e+001 Mqc -2.16e+000 Mqa +2.97e+000 Mqf -7.68e+000 Units kg/s kg m/s kg m/s kg m/s kg m/s kg m/s kg m/s kg -m/s kg m/s kg -m/s kg- m2/s kg- m2/s kg .m 2/s Description Crossflow Drag Body Lift Fin Lift Crossflow Drag Added Mass Cross Term Fin Lift Crossflow Drag Added Mass Cross Term Body Lift Fin Lift Crossflow Drag Added Mass Cross Term Fin Lift 9.3.1 Equations of Motion Combining Equations 9.6 and 9.25 results in the following linearized vehicle equations of motion: (m- Xi)nit+mzg4-Xuu-Xqq-XoO=0 (m-Zb) tb-(mxg+Z4)4-Zw-(mU+Zq)q=Z6.6, mzgi - (mxg + Mb) tb + (IVy - M4) 4 (9.27) - Mww + (mxgU - M) q - Mo9 = Ms., if we assume zg is small compared to the other terms, we can decouple heave and pitch from surge, resulting in the following equations of motion: (m - Zi) W -(mx + Z4 ) 4--Zww - (mU + Z) q = Zs.6, - (mx9 + M) + (IYY - M 4 - Mww + (mxgU - Mq) q - MOO = Similarly, the kinematic equations of motion from Equation 9.4 reduce to: = w-U (9.28) (9.29) Parameter Zwc Zw' Zef Zqc Zqf

---

## Page 166

表 9.2：组合线性化系数 Value -1. 57e+001 -3.45e+001 -1.64e+ 001 +1.20e-001 +1. 44e+000 -1. 12e+001 M.c -4.03e-001 Ma +5.34e+001 MWI -1.11le+001 Mef -1.12e+001 Mqc -2.16e+000 Mqa +2.97e+000 Mqf -7.68e+000 Units kg/s kg m/s kg m/s kg m/s kg m/s kg m/s kg m/s kg -m/s kg m/s kg -m/s kg- m2/s kg- m2/s kg .m 2/s Description Crossflow Drag Body Lift Fin Lift Crossflow Drag Added Mass Cross Term Fin Lift Crossflow Drag Added Mass Cross Term Body Lift Fin Lift Crossflow Drag Added Mass Cross Term Fin Lift 9.3.1 运动方程 将方程 9.6 和 9.25 结合得到以下线性化车辆运动方程： (m- X i)n it+ m zg 4 -X u u -X q q -X o O = 0 ( m - Z b )  tb -(m x g + Z 4 )4 -Z w -(m U + Z q )q = Z 6 .6 , mzgi - (mxg + Mb) tb + (IVy - M4) 4 (9.27) - Mww + (mxgU - M) q - Mo9 = Ms., 如果我们假设 zg  相对于其他项较小，我们可以将升沉和纵倾与前冲运动解耦，从而得到如下运 动方程： (m - Z i) W -(mx + Z4 ) 4--Z w w  - (mU + Z) q = Zs.6, - (mx9 + M ) + (IYY - M 4 - M ww + (m xg U  - Mq) q - MOO = 类似地，方程 9.4 的运动学运动方程简化为： = w-U (9.28) (9.29) Parameter Zwc Zw' Zef Zqc Zqf

---

## Page 167

Table 9.3: Linearized Maneuvering Coefficients Parameter Value Units Description X0 +8.90e+000 kg -m/s 2 Hydrostatic XU -1. 35e+001 kg/s Axial Drag Xn -9.30e-001 kg Added Mass Xq -5.78e-001 kg -m/s Added Mass Cross Term Z. -6.66e+001 kg/s Combined Term Zq -9.67e+000 kg -m/s Combined Term Ze -3.55e+001 kg Added Mass Z4 -1.93e+000 kg -m Added Mass Z3, -5.06e+001 kg- m/s 2 Fin Lift MO -5.77e+000 kg -m2/s 2 Hydrostatic M. +3.07e+001 kg. m/s Combined Term Mq -6.87e+000 kg- m2 /s Combined Term M; -1.93e+000 kg m Added Mass M4 -4.88e+000 kg -M 2 Added Mass Z6, -3.46e+001 kg - m2/s 2 Fin Lift 9.3.2 Four-term State Vector We will find it convenient to combine Equations 9.28 and as follows: mn - X,,, -(mx+Z 4) 0 0 ' -(mx + M) IV- M4 0 0 ji 0 0 1 0 0 0 0 1 Zw mU+ Zq M" -mx9U + M 1 0 0 1 Given the state vector and the input vector we can write Equation 9.30 as 9.29 into a single equation in matrix form, 0 MO -U 0 q _ M 6 ] z 0 Vl 0 0 x= [ w q z T U {3S]T Mi - CdX = Du i = M~ 1 CdX + M- 1Du which is typically represented using the notation i=Ax+Bu (9.35) Substituting the coefficient values developed in Chapter 4 and listed in Appendix D, we arrive (9.30) (9.31) (9.32) (9.33) (9.34)

---

## Page 168

表 9.3：线性化操纵系数 Parameter Value Units Description X0 +8.90e+000 kg -m/s 2 Hydrostatic XU -1. 35e+001 kg/s Axial Drag Xn -9.30e-001 kg Added Mass Xq -5.78e-001 kg -m /s Added Mass Cross Term Z. -6.66e+001 kg/s Combined Term Zq -9.67e+000 kg -m /s Combined Term Ze -3.55e+001 kg Added Mass Z4 -1.93e+000 kg -m Added Mass Z3, -5.06e+001 kg- m/s 2 Fin Lift MO -5.77e+000 kg -m2/s 2 Hydrostatic M. +3.07e+001 kg. m /s Combined Term Mq -6.87e+000 kg- m2 /s Combined Term M; -1.93e+000 kg m Added Mass M4 -4.88e+000 kg -M 2 Added Mass Z6, -3.46e+001 kg - m2/s 2 Fin Lift 9.3.2 四项态向量 我们将发现将方程 9.28 和如下结合是方便的： mn - X,,, -(m x+ Z 4) 0 0 ' -(mx + M) IV- M4 0 0 ji 0 0 1 0 0 0 0 1 Zw mU+ Z q M" -mx9U + M 1 0 0 1 给定状态向量 和输入向量 我们可以将方程 9.30 写成 将 9.29 转化为矩阵形式的单个方程， 0 MO -U 0 q _ M 6 ] z 0 Vl 0 0 x =  [ w q z T U {3S]T Mi - CdX = Du i = M~ 1 CdX + M- 1Du 通常用符号表示的 i= A x + B u (9.35) 将第4章中开发并在附录D列出的系数值代入，我们得到 (9.30) (9.31) (9.32) (9.33) (9.34)

---

## Page 169

at the following matrices: --2.38 +1.26 +0.00 +0.04 A = M 1 Cd = +4.23 -1.12 +0.00 -0.70 +1.00 +0.00 +0.00 -1.54 +0.00 +1.00 +0.00 +0.00 -1.3- (9.36) [-1.381 B=M'D= -3.84 +0.00 +0.00 9.3.3 Three-term State Vector Assuming that the heave velocities are small compared to the other terms, we can further reduce the equations of motion to the following: IYY -M4 0 0 q 0 1 0 0 0 1 -M, 0 -MO~~ q 'Mb + 0 0 U z = 0 [JS] (9.37) -1 0 0 0 0 which we can simply to: .- Mg g me - - - - M.5 - q IvY-M4 IYY -M4 q IYY-M4 z = 0 0 -U z + 0 [o,} (9.38) 1 0 0 0 0 Again substituting the coefficient values developed in Chapter 4 and listed in Appendix D, and applying the form: i = Ax + Bu (9.39) we arrive at the following matrices: -0.82 +0.00 -0.69 A = +0.00 +0.00 -1.54 +1.00 +0.00 +0.00 -4.16(9.40) -4.161 B = +0.00 +0.00 9.4 Control System Design We will now look at the design of a simple vehicle controller, using the state equations developed for the three-term state vector model (see Equation 9.38). The example controller, which is similar to the actual vehicle controller, consists of an inner proportional and derivative (PD) pitch loop, and an outer proportional depth loop. We will address the design of each of these controllers in turn. 9.4.1 Vehicle Transfer Functions The first step in designing the vehicle control system is to derive the vehicle transfer functions. First, we want to derive the transfer function for the inner pitch loop, relating input stern plane angle o, to the output vehicle pitch angle 0. By taking the Laplace transform of Equation 9.38, we can

---

## Page 170

在以下矩阵中： --2.38 +1.26 +0.00 +0.04 A = M 1 Cd = +4.23 -1.12 +0.00 -0.70 +1.00 +0.00 +0.00 -1.54 +0.00 +1.00 +0.00 +0.00 -1.3- (9.36) [-1.381 B = M ' D = -3.84 +0.00 +0.00 9.3.3 三项态矢量 假设升沉速度相比其他项较小，我们可以将运动方程进一步简化为如下形式： IYY -M4 0 0 q 0 1 0 0 0 1 -M, 0 - M O ~ ~  q 'Mb + 0 0 U z = 0 [JS] (9.37) -1 0 0 0 0 我们可以简单地简化为： .- M g g m e - - - - M.5 - q IvY-M4 IYY -M4 q IYY-M4 z = 0 0 -U z + 0 [o,} (9.38) 1 0 0 0 0 再次代入第4章中得出的系数值，并列在附录D中，并应用以下形式： i = Ax + Bu (9.39) 我们得到以下矩阵： -0.82 +0.00 -0.69 A = +0.00 +0.00 -1.54 +1.00 +0.00 +0.00 -4.16(9.40) -4.161 B = +0.00 +0.00 9.4 控制系统设计 我们现在将看看一个简单车辆控制器的设计，使用为三项状态向量模型开发的状态方程（参见 方程 9.38）。这个示例控制器，与实际车辆控制器类似，由一个内部比例-微分（PD）俯仰回路 和一个外部比例深度回路组成。我们将依次讨论每个控制器的设计。 9.4.1  车辆传输功能 设计车辆控制系统的第一步是推导车辆传递函数。首先，我 们希望推导内俯仰回路的传递函数，将输入舵面角度 o 与 to the output vehicle pitch angle 0. By taking the Laplace transform of Equation 9.38, we can 相关联。

---

## Page 171

express this open-loop transfer function as: M6, Go6(s) = =2 Mq M (9.41) s-I'Y -M4 S IY -M4 Next we want to find the transfer function of the outer depth loop, which relates the input vehicle pitch angle Od to the output vehicle depth z. In actuality, the inner pitch loop responds sufficiently fast enough compared to the outer depth loop that we can consider the desired vehicle pitch Od to be the same as the actual vehicle pitch 0. Again taking the Laplace transform of the vehicle state equations, Equation 9.38, we arrive at the desired open-loop transfer function: Gz(s) S U (9.42) 0(s) s 9.4.2 Control Law We will now define the control law for the inner and outer loops. As stated in at the beginning of this chapter, we will design a proportional-derivative (PD) inner loop, and a proportional outer loop. The control law, then, for the inner loop can be expressed as: 3.s (s)_ 6'(S) - K, (rds + 1) (9.43) eo (S) where eo = Od - 0 (9.44) K, is the proportional gain, and rd the derivative time constant in seconds. There is a minus sign applied to the proportional gain due to the difference in sign conventions between the stern plane angle and vehicle pitch angle. Positive stern plane angle will generate a negative moment about the y-axis, forcing the vehicle to pitch down (negative pitch rate). The control law for the outer loop can be expressed as: 0(s) S(S) (9.45) ez(s) where ez = zd - Z (9.46) and -y is the proportional gain. We can express the vehicle control system as a block diagram: Outer Depth Loop (Slow) Inner Pitch Loop (Fast) Z z ed 10 e Os 8 dd 0d 0 0 z + + -KP( Tds+l) G0 G -_ Gain - PD Controller Plant Plant I F ---- -- epth---------------------------- Figure 9-2: Depth-Plane Control System Block Diagram

---

## Page 172

将此开环传递函数表示为： M6, Go6(s) = =2 Mq M (9.41) s-I'Y -M 4  S IY -M 4 接下来，我们想要找到外层深度回路的传递函数，它将输入车辆俯仰角 Od  与输出车 辆深度 z 关联起来。实际上，与外层深度回路相比，内层俯仰回路的响应速度足够快 ，因此我们可以将期望车辆俯仰角 Od  视为与实际车辆俯仰角相同。再次对车辆状态方 程（方程 9.38）进行拉普拉斯变换，我们得到了所需的开环传递函数： G z(s) S U (9.42) 0(s) s 9.4.2 控制律 我们现在将为内环和外环定义控制律。如本章开头所述，我们将设计一个比例-微分（PD）内环和一个比 例外环。因此，内环的控制律可以表示为： 3.s (s)_ 6'(S) - K, (rds + 1) (9.43) eo (S) 哪里 eo = Od - 0 (9.44) K 是比例增益，rd  是微分时间常数（以秒为单位）。 由于尾舵角和车辆俯仰角之间符号约定的差异，比例增益上应用了负号。正的尾舵角会在 y 轴上产生 一个负的力矩，使车辆俯仰向下（负俯仰角速度）。 外环的控制律可以表示为： 0(s) S(S) (9.45) ez(s) 哪里 ez = zd - Z (9.46) 而 -y 是比例增益。 我们可以将车辆控制系统表示为一个框图： Outer Depth Loop (Slow) Inner Pitch Loop (Fast) Z z ed 1 0 e Os 8 dd 0d 0 0 z + + -KP( Tds+l) G 0 G -_ Gain - PD Controller Plant Plant I F ---- -- epth---------------------------- 图 9-2：深度平面控制系统框图

---

## Page 173

9.4.3 Controller Design Procedure Before getting into the specifics of selecting the vehicle controller gains, we will first review a general controller design procedure. This procedure assumes that the system has a second order response. Given that we have chosen to work with the three-term state vector, this is true for the inner pitch loop. This assumption is also valid for higher-order systems, provided the higher order poles are at least five times further from the origin of the s-plane than the two dominant poles. We will design our controller to have a specific second-order response in terms of natural frequency w, and damping ratio (, where, for a second order system: G(s) = (9.47) s2 + 2(ows + W2 Percent Overshoot and Settling or Peak Time Our primary consideration in choosing a system response will be the percentage overshoot, %OS, and peak or settling time, T, or T. See Nise [25] for a graphical explanation of these terms. Our desired damping ratio is a function of percent overshoot, and is given by the equation: In 100 (= ln os (9.48) 7r2 +ln 2y Table 9.4 gives a range of values. One can also plot lines of constant damping ratio on the pole-zero diagram. Table 9.4: Percent Overshoot and Damping Ratio %OS 5 1 10 1 15 1 20 1 25 30 ( 0.690 0.591 0.517 0.456 0.404 0.358 Given the desired damping ratio, our desired natural frequency can be found through the equa- tion: on = (9.49) T~ 1-2 TV/ - (2 or n = (9.50) (T. Desired Poles From Equation 9.47, the second order transfer function, we can now find the desired pole locations through the quadratic formula: 1 S1,2 = -Con ±t 4( 2w - 4w2 (9.51) 2 n n 9.4.4 Pitch Loop Controller Gains Substituting the coefficient values from Table 9.3 into Equation 9.41 results in the following open- loop transfer function: -3.18 s2 + 1.09s + 0.52 and the following open-loop poles. s1,2 = -0.55 ± 0.47i (9.53)

---

## Page 174

9.4.3 控制器设计程序 在进入选择车辆控制器增益的具体内容之前，我们将首先回顾一般的控制器设计程序。 此过程假设系统具有二阶响应。鉴于我们选择使用三项状态向量，这对于内俯仰环是成立的 。对于高阶系统，这一假设同样有效，前提是高阶极点至少比两个主导极点距离 s 平面原点远 五倍以上。 我们将设计我们的控制器，使其具有特定的二阶响应，以自然频率 w,  和阻尼比 (的形式，其 中，对于二阶系统： G(s) = (9.47) s2 + 2(ows + W2 超调百分比与稳态时间或峰值时间 我们在选择系统响应时的主要考虑因素将是百分比超调，%OS，以及峰值或整定时间，T, 或T. 。有关这些术语的图解说明，请参见 Nise [25]。 我们期望的阻尼比是超调百分比的函数，其由下列方程给出： In 100 (= ln os (9.48) 7r2 +ln 2y 表 9.4 给出了一个数值范围。也可以在极点-零点图上绘制恒定阻尼比的线。 表 9.4：超调百分比和阻尼比 %OS 5 1 10 1 15 1 20 1 25 30 ( 0.690 0.591 0.517 0.456 0.404 0.358 给定所需的阻尼比，我们所需的固有频率可以通过以下方程求得： on = (9.49) T ~  1-2 TV/ - (2 或者 n = (9.50) (T. 所需极点 从方程 9.47，即二阶传递函数，我们现在可以通过二次公式找到所需的极点位置： 1 S1,2 = -Con ±t 4( 2w - 4w2 (9.51) 2 n n 9.4.4 音高循环控制器增益 将表 9.3 中的系数值代入方程 9.41 得到以下开环传递函数： -3.18 s2 + 1.09s + 0.52 以及以下开环极点。 s1,2 = -0.55 ± 0.47i (9.53)

---

## Page 175

Figure 9-3 plots these open-loop poles. Figure 9-4 shows the open-loop step response. Given that the REMUS vehicle operates in shallow water and cannot tolerate significant depth overshoot, I chose the following parameters in designing the vehicle pitch controller: %OS = 0.05 T, = 0.75 seconds (9.54) These values resulted in the damping ratio ( and natural frequency W, shown in the legend of the root-locus plot on Figure 9-5. There are many systematic methods for generating the necessary controller gains-in this case, I set the derivative time constant Td, and used the root-locus plot to find the necessary gain K. The resulting controller values are also shown in the legend of Figure 9-5. The resulting closed loop response of the pitch loop transfer function plus controller, Ho, is shown in Figure 9-6. 9.4.5 Depth Loop Controller Gains The method used to find the depth loop controller gains is similar to that of the previous section. The depth transfer function Gz adds a third pole, as shown in the pole-zero plot in Figure 9-7. In order to ensure that the pitch loop response is sufficiently faster than the depth loop response, we must ensure that the pitch loop poles end up at least five times further away from the origin than the depth loop pole. This was accomplished using a root-locus plot to identify the appropriate proportional gain y. The resulting value can be found in the legend of the root-locus plot shown in Figure 9-8. The resulting closed loop response can be seen in Figure 9-9. 9.5 Real-World Phenomena Although this controller appears to exhibit ideal performance characteristics, it is not of much use in the real world. For example, if the controller was given a sufficiently large depth error, there would be nothing to prevent it from commanding preposterous pitch and stern plane angles of greater than 180 degrees. In other words, as designed, the controller assumes the transfer function relationships to be linear out to infinity. In reality, the stern planes will stall at an effective fin angle of greater than about 12 degrees. Similarly, the REMUS vehicle shuts down at greater than 30 degrees of pitch angle, as the software assumes that something has gone disastrously wrong with the vehicle mission. Furthermore, the simulation assumes that the vehicle sensors are free from noise, and the vehicle experiences no unmodeled disturbances. In reality, this is rarely the case. It is an interesting exercise to discretize the transfer functions, and attempt to incorporate some of these real-world effects into the vehicle model. Figure 9-10 shows a block diagram which incorporates the saturation of the commanded stern plane and vehicle pitch angles, as well as pitch sensor noise and environmental disturbances. Figures 9-11 and 9-14 show the results of this kind of a simulation. In Figure 9-11, the model is run without disturbances or actuator saturation. Notice that the controller commands nonsensical vehicle fin angles in excess of 180 degrees. In reality, the vehicle fins stall at an angle of attack less than 15 degrees. In Figure 9-14, the model incorporates fin angle saturation, random pitch sensor noise, and the effects of a 1 knot vertical current. Notice that the vehicle response is slower, and that the fins exhibit a considerable amount of "flutter". 9.6 Controller Implementation In this chapter we have shown the development of vehicle depth control system based on a linearized model of the vehicle dynamics. Although in simulation the controller appears to achieve the desired response, it remains to be seen if it would work as well on the actual vehicle. ± a - __ -_

---

## Page 176

图 9-3 绘制了这些开环极点。图 9-4 显示了开环阶跃响应。 鉴于REMUS车辆在浅水中运行且无法承受显著的深度超调，我在设计车辆俯仰控制器时选择了以下 参数： %OS = 0.05 T, = 0.75 seconds (9.54) 这些数值得出了阻尼比（以及自然频率 W, ，如图 9-5 根轨迹图例所示）。 有许多系统的方法可以生成所需的控制器增益——在这种情况下，我设定了微分时间常数 Td，并使用 根轨迹图来找到所需的增益 K. 。生成的控制器值也显示在图 9-5 的图例中。 由俯仰回路传递函数加控制器 Ho,  所得到的闭环响应如图 9-6 所示。 9.4.5 深度回路控制器增益 用于寻找深度回路控制器增益的方法与前一节的方法类似。深度传递函数 Gz 增加了第三个极点，如图 9- 7 的极零图所示。 为了确保俯仰回路响应比深度回路响应快得多，我们必须确保俯仰回路的极点至少比深度回路的极点 离原点远五倍。 这是通过使用根轨迹图来确定适当的比例增益 y 实现的。得到的数值可以在图 9-8 所示的根轨迹图的 图例中找到。由此得到的闭环响应可以在图 9-9 中看到。 9.5  现实世界现象 尽管该控制器似乎表现出理想的性能特征，但在现实世界中并没有太大用处。例如，如果控制器遇到足够 大的深度误差，没有任何东西可以阻止它发出荒谬的俯仰角和尾舵角命令，角度可能超过180度。换句话 说，按照设计，该控制器假设传递函数关系在无限范围内都是线性的。实际上，尾舵在有效鳍角大于大约 12度时就会失速。同样，REMUS 车辆在俯仰角大于30度时会关闭，因为软件假设车辆任务发生了灾难性 的错误。 此外，模拟假设车辆传感器没有噪声，并且车辆没有经历未建模的干扰。实际上，情况很少是这样。 将传递函数离散化并尝试将一些这些现实世界的影响纳入车辆模型是一项有趣的练习。图 9-10 显示了 一个方框图，该图结合了舵面的指令饱和和车辆俯仰角，以及俯仰传感器噪声和环境干扰。图 9-11 和 9-1 4 显示了这种类型仿真的结果。在图 9-11 中，模型在没有干扰或执行器饱和的情况下运行。注意控制器指 令车辆舵角超过 180 度，这在实际中是无意义的。实际上，车辆舵叶在攻角小于 15 度时就会失速。 在图9-14中，模型包含了鳍角饱和、随机俯仰传感器噪声以及1节垂直水流的影响。注意，飞行器的响 应较慢，并且鳍片表现出相当大的“颤动”。 9.6 控制器实现 在本章中，我们展示了基于车辆动力学线性化模型的车辆深度控制系统的发展。尽管在仿真中控制器似乎 能够达到期望的响应，但仍有待观察它在实际车辆上是否同样有效。 ±a  - __  -_  - - -

---

## Page 177

Real Axis Figure 9-3: Go Pole-Zero Plot Time (s) Figure 9-4: G0 Open-Loop Step Response

---

## Page 178

Real Axis 图 9-3：Go 极点-零点图 Time (s) 图 9-4：G0 开环阶跃响应

---

## Page 179

4 2 0 x i-2 E -4 -6 _F I I - I I ~10 -9 -8 -7 -6 -5 Real Axis -4 -3 -2 -1 0 Figure 9-5: Go Root-Locus Plot Time (s) Figure 9-6: Go Closed-Loop Step Response -x x x<..x X x x .x xx x x x -x x x x xx xx xx x - x x -x x xx x x x Damping Ratio ( =0.6901, %OS = +5.0%, Lines intersect at Tp = 0.8 s or Nati Freq o =+5.79 racj s x Desired Poles: td =0.210, Kp = 10.345 - |

---

## Page 180

4 2 0 x i-2 E -4 -6 _F I I - I I ~10 -9 -8 -7 -6 -5 Real Axis -4 -3 -2 -1 0 图 9-5：Go 根轨迹图 Time (s) 图 9-6：闭环阶跃响应 -x x x<..x X x x .x xx x x x -x x x x xx xx xx x - x  x -x x x x x x x Damping Ratio ( =0.6901, %OS = +5.0%, Lines intersect at Tp = 0.8 s or Nati Freq o =+5.79 racj s x Desired Poles: td =0.210, Kp = 10.345 - |

---

## Page 181

2 Real Axis Figure 9-7: G, * HO Pole-Zero Plot xx 4- 2- 0o.. 0...... .................................. .. 5 X .XO0i. CB2 - E- -4 -- -6 -- Damping Ratio (=0.6901, %OS =+5.0 %, Lines intersect at Tp = 0.8 s or Nati Freq , +579 ra s x Desired Poles, y =-0.772 -8-7 -6 -5 -4 -3 -2 -1 0 Real Axis Figure 9-8: G2, * Ho Root-Locus Plot 91

---

## Page 182

2 Real Axis 图 9-7：G,  * HO  极零图 xx 4- 2- 0o.. 0...... .................................. .. 5 X .X O 0i. CB 2  - E- -4 -- -6 -- Damping Ratio (=0.6901, %OS =+5.0 %, Lines intersect at Tp = 0.8 s or Nati Freq , +579 ra s x Desired Poles, y =-0.772 -8-7 -6 -5 -4 -3 -2 -1 0 Real Axis 图 9-8：G2, * Ho  根轨迹图 91

---

## Page 183

II The next step in testing the controller would be to replace the linearized depth-plane plant in Figure 9-10 with the non-linear, six degree of freedom vehicle model developed in the earlier chapters. This would allow us to gauge how well the controller handles vehicle behavior outside the linearized regime of small angles and small accelerations. The final step would be to test the depth-plane controller on the actual vehicle at sea.

---

## Page 184

二 测试控制器的下一步是将图9-10中的线性化深度平面模型替换为前面章节中开发的非线性六 自由度车辆模型。这将使我们能够评估控制器在小角度和小加速度的线性化范围之外，处理车 辆行为的能力。 最后一步是在实际的海上车辆上测试深度平面控制器。

---

## Page 185

CL 7 - - --- 8 - - 9 - -. 10 0 1 2 3 4 5 6 7 8 9 10 Time (s) Figure 9-9: G, * HO Closed-Loop Step Response d Environmental Disturbance z eA e S A + d z Y - dTdP(S+1) 8s + Go Gzz - Gain Pitch - PID Controller Fin Plant + Plant Saturation Saturation+ n Sensor Noise Figure 9-10: Depth-Plane Control System Block Diagram with Actuator Limits, Environmental Disturbance, and Sensor Noise

---

## Page 186

C L 7 - - --- 8 - - 9 - -. 10 0 1 2 3 4 5 6 7 8 9 10 Time (s) 图 9-9：G,  * HO  闭环阶跃响应 d Environmental Disturbance z eA e S A + d  z Y - dTdP(S+1) 8s + Go Gzz - Gain Pitch - PID Controller Fin Plant + Plant Saturation Saturation+ n Sensor Noise 图 9-10：具有执行器限制、环境干扰和传感器噪声的深度平面控制系统框图

---

## Page 187

- theta actual theta command 0 1 2 3 4 5 6 7 8 9 1( depth actual - depth command 0 1 2 3 4 5 6 7 8 9 1( Heave Rate .- 0 1 2 3 4 5 6 7 8 - Fin Angle] 2 3 4 5 6 Time 8 9 10 Figure 9-11: Vehicle Simulation, based on basic block diagram 0 -0.5 . -1. -2 -1 -0.5 0 o 0.5 > 1.5 0.2 0 -0.2 ( - cc 4 0 . 600 400 200 e i0 0 -200

---

## Page 188

- theta actual theta command 0 1 2 3 4 5 6 7 8 9 1( depth actual - depth command 0 1 2 3 4 5 6 7 8 9 1( Heave Rate .- 0 1 2 3 4 5 6 7 8 - Fin Angle] 2 3 4 5 6 Time 8 9 10 图 9-11：基于基本方框图的车辆模拟 0 -0.5 . -1. -2 -1 -0.5 0 o 0.5 > 1.5 0.2 0 -0.2 ( - cc 4 0 . 600 400 2 0 0 e i0 0 -200

---

## Page 189

.8 -0.5 S-1.5 -0 a 0 >1 0 N theta actual theta command 0 1 2 3 4 5 6 7 8 9 1C -1- depth actual .5- depth command 0 .5- .5 - 0 1 2 3 4 5 6 7 8 9 1C 1.2 - - Heave Rate . - a -0.1 - Z -0.2- -0.3 -0 1 2 3 4 5 6 7 8 9 10 Figure 9-12: Vehicle Simulation, with fin angle saturation 0 1 2 3 4 5 6 7 8 9 10 Time

---

## Page 190

.8 -0.5 S-1.5 -0 a 0 >1 0 N theta actual theta command 0 1 2 3 4 5 6 7 8 9 1C -1- depth actual .5- depth command 0 .5- .5 - 0 1 2 3 4 5 6 7 8 9 1C 1.2 - - Heave Rate . - a -0.1 - Z -0.2- -0.3 -0 1 2 3 4 5 6 7 8 9 10 图 9-12：车辆仿真，带鳍角饱和 0 1 2 3 4 5 6 7 8 9 10 Time

---

## Page 191

0- .D -0.5- R 0 -1 0 O 1. -0.5 - 0 0- C. co 0.5 - >1.5 - theta actual theta command 1 2 3 4 5 6 7 8 9 10 depth actual depth command 0 1 2 3 4 5 6 7 8 9 10 0.2- Heave Rate S0.1 - 0 o-0.1 -0.2- 03 2 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 10 2 3 4 5 6 7 8 9 10 Time Figure 9-13: Vehicle Simulation, with fin angle saturation and random pitch sensor noise

---

## Page 192

0- .D -0.5- R 0 -1 0 O 1. -0.5 - 0 0- C. co 0.5 - > 1.5 - theta actual theta command 1 2 3 4 5 6 7 8 9 10 depth actual depth command 0 1 2 3 4 5 6 7 8 9 10 0.2- Heave Rate S 0 . 1  - 0 o -0 .1 -0 .2 - 03 2 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 10 2 3 4 5 6 7 8 9 10 Time 图 9-13：车辆仿真，带有鳍角饱和和随机俯仰传感器噪声

---

## Page 193

0.5 0 -0.5 . > 1.5 a. E 10 'U' to 4) x theta actual theta command 0 1 2 3 4 5 6 7 8 9 1C -1 depth actual -0.5 depth command 05 0.5 2 ------------ ----------- 0 1 2 3 4 5 6 7 8 9 1C 0.1 - - Heave Rate 0 -0.1 - -0.2 - -0.3- -0.4 0 1 2 3 4 5 6 7 8 9 1C 10 - 0 -5 - 0 1 2 3 4 5 Time Figure 9-14: Vehicle Simulation, incorporating fin angle saturation, random pitch sensor noise, and 1 knot vertical current a.mmmmmmm=s.. - 6 7 8 9 10

---

## Page 194

0.5 0 -0.5 . > 1.5 a. E 10 'U' to 4) x theta actual theta command 0 1 2 3 4 5 6 7 8 9 1C -1 depth actual -0.5 depth command 05 0.5 2 ------------ ----------- 0 1 2 3 4 5 6 7 8 9 1C 0.1 - - Heave Rate 0 -0.1 - -0.2 - -0.3- -0.4 0 1 2 3 4 5 6 7 8 9 1C 10 - 0 -5 - 0 1 2 3 4 5 Time 图 9-14：车辆仿真，包括鳍角饱和、随机纵倾传感器噪声以及 1 节垂直流 mmmmmm= s.. - 6 7 8 9 10

---

## Page 195

Vi Chapter 10 Conclusion In the preceding chapters, we have demonstrated the development of a mathematical model for the dynamics of an autonomous underwater vehicle. We have examined methods for validating the performance of this model. Finally, we have seen how such a model can be applied to the development of a vehicle control system. In the following sections, we outline a series of recommendations for expanding upon this work. 10.1 Expanded Tow Tank Measurements In the previous chapter, the author outlined the limitations of vehicle coefficients based solely upon semi-empirical formulae. The most significant source of error is in the way coefficients are used to model the vehicle moving at some angle of attack, as shown in Figure 10-1. The fluid effects are Body Lift Crossflow Drag Fluid Axial Velocity Drag Figure 10-1: Forces on the vehicle at an angle of attack broken up into vehicle body lift, vehicle crossflow drag, and vehicle axial drag. Of these, the author had the most difficulty estimating body lift. The semi-empirical methods of calculating the body lift coefficient used by Hoerner [16], Bottac- cini [7], and Nahon [23], explored in the development of this thesis, were found to differ by an order of magnitude. It will therefore be important to experimentally measure forces and moments on the vehicle moving at an angle of attack, in order to verify the empirical estimates. 10.2 Future Experiments at Sea The following are recommendations for future experiments at sea, derived from the author's expe- rience and consultation with experts in the field.

---

## Page 196

Vi 第10章 结论 在前几章中，我们已经展示了自主水下航行器动力学数学模型的开发过程。我们已经研究了验证该模型性 能的方法。最后，我们已经看到这样的模型如何应用于航行器控制系统的开发。 在以下各节中，我们概述了一系列关于扩展这项工作的建议。 10.1 扩展拖车油箱测量 在上一章中，作者概述了仅基于半经验公式的车辆系数的局限性。最显著的误差来源在于系数用于模拟 车辆在某个攻角运动的方式，如图 10-1 所示。流体效应是 Body Lift Crossflow Drag Fluid Axial Velocity Drag 图 10-1：车辆在迎角下的受力情况 分为车身升力、车辆横向流动阻力和车辆轴向阻力。在这些方面，作者在估算车身升力时遇到的困难最大 。 Hoerner [16]、Bottaccini [7] 和 Nahon [23] 使用的计算机身升力系数的半经验方法，在本论文的研究过 程中发现，结果相差一个数量级。因此，实验测量车辆在迎角移动时的力和力矩，将对于验证经验估算非 常重要。 10.2 海上未来实验 以下是根据作者的经验以及与该领域专家的咨询，对未来海上实验的建议。

---

## Page 197

10.2.1 Improved Vehicle Instrumentation The vehicle dynamics data collected in the experiments described in Chapter 7 were limited in the number of vehicle states recorded, and the accuracy of those measurements. This made it extremely difficult to judge the validity of the model comparison. For future experiments, the author has augmented the standard REMUS sensors described in Section 7.3 with an inertial measurement unit: the Crossbow DMU-AHRS (Dynamic Measurement Unit-Attitude and Heading Reference System). This instrument outputs magnetic orientation, accelerations and angular rates on three axes. From this instrument, we will be able to accurately measure or derive the following vehicle states. x= it tb u v w p q r (10.1) This will significantly improve our ability to measure the vehicle initial conditions in particular, and the vehicle motion in general. 10.2.2 Measurement of Vehicle Parameters With the exception of the longitudinal center of gravity %c, which was measured before each exper- iment using a balance, the author's estimates for the vehicle mass distribution were calculated using the vehicle weight list. Similarly, the estimates for the vehicle center of buoyancy were calculated using the Myring hull shape. To reduce uncertainty in future experiments, it will be necessary to measure these values exper- imentally, preferably before each experiment. 10.2.3 Isolation of Vehicle Motion One limitation of the experimental step response data used in the model validation was imperfect knowledge of the vehicle initial conditions. At the time of the experiments, the author had no way of measuring the vehicle accelerations and angular rates prior to the changes in fin angles. These vehicle motions resulted from two sources: vehicle control inputs and external disturbances. In future experiments, every effort should be made to minimize these motions. To minimize vehicle control motions, it is important to understand the vehicle steady-state conditions. AUVs like REMUS can be unstable when operating without control. Using the inertial measurement unit, it will be possible to identify the propeller RPM and fixed fin angles which result in straight and level vehicle flight. These settings should then be used at the start of every experimental run. To minimize environmental disturbances, the experiments could be run in an area known to be free of currents, and at sufficient depth to avoid free surface interactions. Two locations meeting these criteria would be deep lakes and flooded sinkholes. 10.3 Controller-Based Model Comparison The vehicle model is particularly useful as a tool in developing vehicle control systems. To that end, rather than comparing the model output to vehicle data collected during open-loop maneuvers, it would be more useful to compare the model to the vehicle behavior during closed-loop control. This would mean incorporating the vehicle controller as the interface to the model code. Rather than actuator states such as the vehicle fin angles 5, and deltar, the model inputs would instead be the commanded states, such as desired depth zd or desired heading 1bd. 10.4 Vehicle Sensor Model Developing a vehicle sensor model would enable us to improve the vehicle performance without nec- essarily improving the vehicle sensors. As part of the vehicle tow tank experiments and experiments

---

## Page 198

10.2.1 改进的车辆仪表 在第 7  章中描述的实验中收集的车辆动力学数据，在记录的车辆状态数量和测量的准确性方面 都有限。这使得判断模型比较的有效性变得极为困难。 在未来的实验中，作者在第7.3节中描述的标准REMUS传感器基础上增加了一个惯性测量单 元：Crossbow DMU-AHRS（动态测量单元-姿态与航向参考系统）。该仪器可以输出三轴的磁 力方向、加速度和角速度。通过该仪器，我们将能够准确地测量或推导出以下车辆状态。 x= it t b  u v w p q r (10.1) 这将显著提高我们特别是测量车辆初始条件的能力，以及总体上测量车辆运动的能力。 10.2.2  车辆参数的测量 除了纵向重心 %c,  是在每次实验前使用天平测量的之外，作者对车辆质量分布的估算是使用车 辆重量清单计算的。同样，车辆浮心的估算是使用 Myring 船体形状计算的。 为了减少未来实验中的不确定性，有必要通过实验测量这些数值，最好在每次实验之前进行 。 10.2.3  车辆运动的隔离 用于模型验证的实验阶跃响应数据的一个限制是对车辆初始状态的了解不完全。在进行实验时 ，作者无法在鳍角变化之前测量车辆的加速度和角速度。 这些车辆运动来源于两个方面：车辆控制输入和外部干扰。在未来的实验中，应尽一切努力 尽量减少这些运动。 为了最小化车辆控制动作，理解车辆的稳态条件非常重要。像 REMUS 这样的自主水下航行 器在无控制操作时可能是不稳定的。使用惯性测量单元，可以确定导致车辆直线和平稳飞行的 螺旋桨转速和固定鳍角。这些设置应在每次实验运行开始时使用。 为了尽量减少对环境的干扰，实验可以在已知无水流的区域进行，并且在足够深的水域以避 免自由表面相互作用。符合这些条件的两个地点是深湖和被淹没的天坑。 十.3 基于控制器的模型比较 伊森 该车辆模型在开发车辆控制系统方面特别有用。为此，与其将模型输出与在开环操作期间收集 的车辆数据进行比较，不如将模型与闭环控制期间的车辆行为进行比较会更有用。这意味着需 要将车辆控制器作为模型代码的接口。与使用诸如车辆舵角等执行器状态不同，模型输入将是 命令状态，例如期望深度或期望航向。 10.4  车辆传感器模型 开发车辆传感器模型将使我们能够在不必改进车辆传感器的情况下提高车辆性能。作为车辆拖 车水槽实验和实验的一部分

---

## Page 199

100 at sea, precision vehicle inertial measurements could be used to calibrate the other vehicle sensors and estimate their dynamic response. 10.5 Improved Coefficient-Based Model Mission planning for the shallow water operation of AUVs depends on an accurate knowledge of the performance limits of these vehicles in terms of water depth and sea state. A map of this two- dimensional space for shallow water is illustrated in Figure 10-2. At present, these limits are not known. Vehicle doesn't work Sea State / Vehicle works Vehicle Depth Figure 10-2: Vehicle performance limits as a function of depth and sea state A vehicle model based on vehicle state- and environment-dependent transfer functions could prove an effective method for simulating the dynamics of underwater vehicles near the surf zone. The transfer functions for such a vehicle model would themselves be functions of the operating state of the vehicle, the water depth and the sea state. These transfer functions could be derived from a combination of existing data sets for AUVs in shallow water and waves [4, 27, 33] and numerical vehicle model codes [26, 13, 34, 21]. Given such a model and a method for simulating the disturbances caused by a random wave field, one could predict the probabilistic deviation of an underwater vehicle from a given desired trajectory. Control system designers and mission planners could use this stochastic analysis to determine the operating limits of their vehicles.

---

## Page 200

100 在海上，精密车辆惯性测量可以用于校准其他车辆传感器并估算它们的动态响应。 一0.5 改进的基于系数的 Mo 删除 用于自主水下航行器（AUV）浅水作业的任务规划依赖于对这些车辆在水深和海况方面性能极 限的准确了解。图 10-2 展示了浅水区域中这一二维空间的示意图。目前，这些极限尚不明确。 Vehicle doesn't work Sea State / Vehicle works Vehicle Depth 图10-2：车辆性能极限随深度和海况的变化 基于车辆状态和环境依赖传递函数的车辆模型可能是一种有效的方法，用于模拟近岸水域水 下车辆的动力学。这种车辆模型的传递函数本身将是车辆运行状态、水深和海况的函数。 这些传递函数可以通过结合浅水中AUV的现有数据集和波浪 [4, 27, 33] 以及数值车辆模型代 码 [26, 13, 34, 21] 推导出来。 给定这样一个模型以及一种用于模拟由随机波浪场引起的扰动的方法，可以预测水下车辆偏 离给定期望轨迹的概率偏差。控制系统设计人员和任务规划者可以使用这种随机分析来确定其 车辆的运行限制。

---

## Page 201

Appendix A Tables of Parameters Table A. 1: STD REMUS Hull Parameters Value +1. 03e+003 +2.85e-002 +2.26e-001 +7.09e-001 +3.15e-002 +2.99e+002 +3.08e+002 +3. 17e+002 +5.54e-003 +3. Oe-001 +1. 10e+000 +1. 20e+000 -3.21e-001 +3.59e-002 Units m3 N N N m n/a n/a n/a n/a n/a Description Seawater Density Hull Frontal Area Hull Projected Area (xz plane) Hull Wetted Surface Area Estimated Hull Volume Measured Vehicle Weight Measured Vehicle Buoyancy Estimated Hull Buoyancy Est. Long. Center of Buoyancy REMUS Axial Drag Coeff. Cylinder Crossflow Drag Coeff. Hoerner Body Lift Coeff. Center of Pressure Ellipsoid Added Mass Coeff. Table A.2: Hull Coordinates for Limits of Integration Parameter Value Units Description Xt -7.21e-001 m Aft End of Tail Section Xt2 -2.18e-001 m Forward End of Tail Section Xf -6.85e-001 m Aft End of Fin Section Xf2 -6. l1e-001 m Forward End of Fin Section Xb +4.37e-001 m Aft End of Bow Section Xb2 +6. 10e-001 m Forward End of Bow Section Table A.3: Center of Buoyancy wrt Origin at Vehicle Nose Parameter Value Units Xcb -6. 11e-001 m Ycb +0. 00e+000 m Zcb +0.00e+000 m 101 Parameter P Ap SI- W B Best Xcb(est) Cd Cdc Cyd#l xcp

---

## Page 202

附录 A 参数表 表 A.1：STD REMUS 船体参数 Value +1. 03e+003 +2.85e-002 +2.26e-001 +7.09e-001 +3.15e-002 +2.99e+002 +3.08e+002 +3. 17e+002 +5.54e-003 +3. O e-001 +1. 10e+000 +1. 20e+000 -3.21e-001 +3.59e-002 Units m3 N N N m n/a n/a n/a n/a n/a Description Seawater Density Hull Frontal Area Hull Projected Area (xz plane) Hull Wetted Surface Area Estimated Hull Volume Measured Vehicle Weight Measured Vehicle Buoyancy Estimated Hull Buoyancy Est. Long. Center of Buoyancy REMUS Axial Drag Coeff. Cylinder Crossflow Drag Coeff. Hoerner Body Lift Coeff. Center of Pressure Ellipsoid Added Mass Coeff. 表 A.2：积分极限的船体坐标 Parameter Value Units Description Xt -7.21e-001 m Aft End of Tail Section Xt2 -2.18e-001 m Forward End of Tail Section Xf -6.85e-001 m Aft End of Fin Section Xf2 -6. l1e-001 m Forward End of Fin Section Xb +4.37e-001 m Aft End of Bow Section Xb2 +6. 10e-001 m Forward End of Bow Section 表 A.3：浮力中心相对于车辆前端原点的位置 Parameter Value Units Xcb -6. 11e-001 m Ycb +0. 00e+000 m Zcb +0.00e+000 m 101 Parameter P Ap SI- W B Best X cb(est) Cd Cdc Cyd#l xcp

---

## Page 203

at CB Table A.5: REMUS Fin Parameters Parameter Value Units Description Sfi +6.65e-003 m2 Planform Area bfi, +8.57e-002 m Span Xfinpost -6.38e-001 m Moment Arm wrt Vehicle Origin at CB imax +1 . 36e+001 deg Maximum Fin Angle afin +5.14e+000 m Max Fin Height Above Centerline Cmean +7.47e-002 m Mean Chord Length t +6.54e-001 n/a Fin Taper Ratio (Whicker-Felner) cdf +5.58e-001 n/a Fin Crossflow Drag Coefficient ARe +2.21e+000 n/a Effective Aspect Ratio a +9.00e-001 n/a Lift Slope Parameter CLQ +3.12e+000 n/a Fin Lift Slope 102 Table A.4: Center of Gravity wrt Origin Parameter Value Units Xcg +0.00e+000 m ycg +0.00e+000 m Zcg +1. 96e-002 m

---

## Page 204

在 CB 表 A.5：REMUS 鳍参数 Parameter Value Units Description Sfi +6.65e-003 m2 Planform Area bfi, +8.57e-002 m Span Xfinpost -6 .3 8 e -0 0 1 m Moment Arm wrt Vehicle Origin at CB imax +1 . 36e+001 deg Maximum Fin Angle afin +5.14e+000 m Max Fin Height Above Centerline Cmean +7.47e-002 m Mean Chord Length t +6.54e-001 n/a Fin Taper Ratio (Whicker-Felner) cdf +5.58e-001 n/a Fin Crossflow Drag Coefficient ARe +2.21e+000 n/a Effective Aspect Ratio a +9.00e-001 n/a Lift Slope Parameter CLQ +3.12e+000 n /a Fin Lift Slope 102 表 A.4：相对于原点的重心 Parameter Value Units Xcg +0.00e+000 m ycg +0.00e+000 m Zcg +1. 96e-002 m

---

## Page 205

Appendix B Tables of Combined Non-Linear Coefficients Note that all coefficients are calculated for the STD REMUS hull profile. Unlike those given in Tables 4.2 and 4.3, these values include the correction factors described in Section 8.1.2. Table B.1: Non-Linear Force Coefficients Value -1.62e+000 -9.30e-001 -3.55e+001 -1. 93e+000 +3.55e+001 -1. 93e+000 +3.86e+000 -1.31e+003 +6. 32e-001 -2.86e+001 -3.55e+001 +1. 93e+000 +5.22e+000 +3.55e+001 +1.93e+000 +9.64e+000 -1.31e+002 -6.32e-001 -2.86e+001 -3.55e+001 -1. 93e+000 -5.22e+000 -3.55e+001 +1. 93e+000 -9.64e+00 0 Units kg/m kg kg/rad kg -m/rad kg/rad kg -m/rad N kg/m kg -m/rad2 kg/m kg kg -m/rad kg/rad kg/rad kg -m/rad kg/(m - rad) kg/m kg -m/rad2 kg/m kg kg -m/rad kg/rad kg/rad kg/rad kg/(m -rad) Description Cross-flow Drag Added Mass Added Mass Cross-term Added Mass Cross-term Added Mass Cross-term Added Mass Cross-term Propeller Thrust Cross-flow Drag Cross-flow Drag Body Lift Force and Fin Lift Added Mass Added Mass Added Mass Cross Term and Fin Lift Added Mass Cross-term Added Mass Cross-term Fin Lift Force Cross-flow Drag Cross-flow Drag Body Lift Force and Fin Lift Added Mass Added Mass Added Mass Cross-term and Fin Lift Added Mass Cross-term Added Mass Cross-term Fin Lift Force 103 Parameter X2, X, Xwq Xqq Xvr Xrr Y I Yr Yu Yi, Y, Yu r YWaYpq Yuudr Z.. Zqq Zuw Ze , Z4 Zuq ZIP Zrp Zuuds

---

## Page 206

附录 B 非线性组合系数表 请注意，所有系数都是针对STD REMUS船体轮廓计算的。与表4.2和4.3中给出的数值不同，这 些数值包括第8.1.2节中描述的修正因子。 Table B.1: Non-Linear Force Coefficients Value -1.62e+000 -9.30e-001 -3.55e+001 -1. 93e+000 +3.55e+001 -1. 93e+000 +3.86e+000 -1.31e+003 +6. 32e-001 -2.86e+001 -3.55e+001 +1. 93e+000 +5.22e+000 +3.55e+001 +1.93e+000 +9.64e+000 -1.31e+002 -6.32e-001 -2.86e+001 -3.55e+001 -1. 93e+000 -5.22e+000 -3.55e+001 +1. 93e+000 -9.64e+00 0 Units kg/m kg kg/rad kg -m/rad kg/rad kg -m /rad N kg/m kg -m/rad 2 kg/m kg kg -m/rad kg/rad kg/rad kg -m/rad kg/(m - rad) kg/m kg -m/rad 2 kg/m kg kg -m/rad kg/rad kg/rad kg/rad kg/(m -rad) Description Cross-flow Drag Added Mass Added Mass Cross-term Added Mass Cross-term Added Mass Cross-term Added Mass Cross-term Propeller Thrust Cross-flow Drag Cross-flow Drag Body Lift Force and Fin Lift Added Mass Added Mass Added Mass Cross Term and Fin Lift Added Mass Cross-term Added Mass Cross-term Fin Lift Force Cross-flow Drag Cross-flow Drag Body Lift Force and Fin Lift Added Mass Added Mass Added Mass Cross-term and Fin Lift Added Mass Cross-term Added Mass Cross-term Fin Lift Force 103 Parameter X2, X, Xwq Xqq Xvr X rr Y I Yr Yu Yi, Y, Yu r YWaYpq Yuudr Z.. Zqq Zuw Z e  , Z4 Zuq Z I P Z rp Z u u d s

---

## Page 207

Table B.2: Non-Linear Moment Coefficients Parameter Value Units Description K,, -1. 30e-001 kg. m2 /rad 2 Rolling Resistance K, -7.04e-002 kg. m2 /rad Added Mass Krop -5. 43e-001 N m Propeller Torque M.. +3. 18e+000 kg Cross-flow Drag Mqq -1. 88e+002 kg- m2/rad 2 Cross-flow Drag M. +2.40e+001 kg Body and Fin Lift and Munk Moment Me -1.93e+000 kg-m Added Mass M -4. 88e+000 kg- m 2/rad Added Mass Muq -2. 00e+000 kg. m/rad Added Mass Cross Term and Fin Lift M., -1. 93e+000 kg. m/rad Added Mass Cross Term Mrp +4. 86e+000 kg -m2 /rad2 Added Mass Cross-term Muds -6.15e+000 kg/rad Fin Lift Moment Nov -3.18e+000 kg Cross-flow Drag N, -9.40e+001 kg -m2 /rad2 Cross-flow Drag Nuv -2.40e+001 kg Body and Fin Lift and Munk Moment Nj, +1.93e+000 kg m Added Mass N -4.88e+000 kg -m2 /rad Added Mass Nur -2. 00e+000 kg. m/rad Added Mass Cross Term and Fin Lift N., -1. 93e+000 kg. m/rad Added Mass Cross Term Npq -4.86e+000 kg -m2/rad2 Added Mass Cross-term Nuudr -6. 15e+and kg/rad Fin Lift Moment 104

---

## Page 208

表 B.2：非线性弯矩系数 Parameter Value Units Description K,, -1. 30e-001 kg. m2 /rad 2 Rolling Resistance K, -7.04e-002 kg. m2 /rad Added Mass K rop -5. 43e-001 N m Propeller Torque M .. +3. 18e+000 kg Cross-flow Drag Mqq -1. 88e+002 kg- m2/rad 2 Cross-flow Drag M. +2.40e+001 kg Body and Fin Lift and Munk Moment Me -1.93e+000 kg-m Added Mass M -4. 88e+000 kg- m 2/rad Added Mass Muq -2. 00e+000 kg. m /rad Added Mass Cross Term and Fin Lift M., -1. 93e+000 kg. m /rad Added Mass Cross Term Mrp +4. 86e+000 kg -m2 /rad2 Added Mass Cross-term Muds -6.15e+000 kg/rad Fin Lift Moment Nov -3.18e+000 kg Cross-flow Drag N, -9.40e+001 kg -m2 /rad2 Cross-flow Drag Nuv -2.40e+001 kg Body and Fin Lift and Munk Moment Nj, +1.93e+000 kg m Added Mass N -4.88e+000 kg -m2 /rad Added Mass Nur -2. 00e+000 kg. m /rad Added Mass Cross Term and Fin Lift N ., -1. 93e+000 kg. m /rad Added Mass Cross Term Npq -4.86e+000 kg -m2/rad2 Added Mass Cross-term Nuudr -6. 15e+and kg/rad Fin Lift Moment 104

---

## Page 209

Appendix C Tables of Non-Linear Coefficients by Type Note that all coefficients are calculated for the STD REMUS hull profile. Unlike those given in Tables 4.2 and 4.3, these values include the correction factors described in Section 8.1.2. Table C.1: Axial Drag Coefficient Parameter Value Units XU -1.62e+000 kg/m Table C.2: Crossflow Drag Coefficients Parameter Value Units Yv -1.31e+003 kg/m Y,,d +6.32e-001 kg -m/rad2 Z.W -1.31e+002 kg/m Zqqd -6.32e-001 kg m/rad2 Mmmd +3.18e+000 kg Mqq -1.88e+002 kg m2/rad2 Novd -3.18e+000 kg Nrr -9.40e+001 kg.m2/rad2 Table C.3: Rolling Resistance Coefficient Parameter Value Units K,, -1.30e-001 kg -m2/rad'

---

## Page 210

附录 C 按类型分类的非线性系数表 请注意，所有系数都是根据 STD REMUS 船体型线计算的。与 Tables 4 . 2  and 4 . 3 ,  these values include the correction factors described in Section 8 . 1 . 2 . 中给出的 不同 Table C.1: Axial Drag Coefficient Parameter Value Units XU -1.62e+000 kg/m 表 C.2：横流阻力系数 Parameter Value Units Yv -1.31e+003 kg/m Y,,d +6.32e-001 kg -m/rad 2 Z.W -1.31e+002 kg/m Zqqd -6.32e-001 kg m/rad 2 Mmmd +3.18e+000 kg Mqq -1.88e+002 kg m2/rad2 Novd -3.18e+000 kg Nrr -9.40e+001 kg.m2/rad 2 表 C.3：滚动阻力系数 Parameter Value Units K,, -1.30e-001 kg -m2/rad'

---

## Page 211

Table C.4: Body Lift and Moment Coefficients Parameter Value Units Y. v -2.86e+001 kg/m Z2. -2.86e+001 kg/m Mawb -4.47e+000 kg Navb +4.47e+000 kg able C.5: Added Mass rameter Value Xa, -9.30e-001 Xj, +0.00e+000 Xej, +0.00e+000 X +0.00e+000 X4 +0.00e+000 X, +0.00e+000 YU +0.00e+000 Y& -3.55e+001 Yoi, +0.00e+000 Yp +0.00e+000 Y4 +0.00e+000 Yr +1.93e+000 Zi, +0.00e+000 Zo, +0.00e+000 Zeb -3.55e+001 Z4 +0.00e+000 Z4 -1.93e+000 Zr +0.00e+000 Kj, +0.00e+000 Ki, +0.00e+000 Kmb +0.00e+000 Kp -7.04e-002 K 4 +0.00e+000 Kr +0.00e+000 Mai +0.00e+000 Mi, +0.00e+000 Mb -1.93e+000 Mp +0.00e+000 M4 -4.88e+000 M1% +0.00e+000 Na, +0.00e+000 Ni, +1.93e+000 No, +0.00e+000 Np +0.00e+000 N4 +0.00e+000 N,% -4.88e+000 Coefficients Units kg kg kg kg m/rad kg. m/rad kg. m/rad kg kg kg kg. m/rad kg. m/rad kg. m/rad kg kg kg kg m/rad kg. m/rad kg. m/rad kg- m kg -m kg -m kg -m2 /rad kg -m2 /rad kg -m2 /rad kg -m kg -m kg -m kg -m2 /rad kg -m2 /rad kg -m2 /rad kg -m kg -m kg -m kg -m2 /rad kg -m2 /rad kg .m2 /rad 106 T Pai

---

## Page 212

表 C.4：机体升力和力矩系数 Parameter Value Units Y. v -2.86e+001 kg/m Z2. -2.86e+001 kg/m Mawb -4.47e+000 kg Navb +4.47e+000 kg able C.5：已添加Mass rameter Value Xa, -9.30e-001 Xj, +0.00e+000 Xej, +0.00e+000 X +0.00e+000 X4 +0.00e+000 X, +0.00e+000 YU + 0.00e+ 000 Y& -3.55e+001 Yoi, +0.00e+000 Yp +0.00e+000 Y4 +0.00e+000 Yr +1.93e+000 Zi, +0.00e+000 Zo, +0.00e+000 Zeb -3.55e+001 Z4 +0.00e+000 Z4 -1.93e+000 Zr +0.00e+000 K j, +0.00e+000 K i, +0.00e+000 Kmb +0.00e+000 Kp -7.04e-002 K 4 +0.00e+000 Kr +0.00e+000 Mai +0.00e+000 Mi, +0.00e+000 Mb -1.93e+000 Mp +0.00e+000 M4 -4.88e+000 M1% +0.00e+000 Na, +0.00e+000 Ni, +1.93e+000 No, +0.00e+000 Np +0.00e+000 N4 +0.00e+000 N,% -4.88e+000 Coefficients Units kg kg kg kg m /rad kg. m /rad kg. m /rad kg kg kg kg. m /rad kg. m /rad kg. m /rad kg kg kg kg m /rad kg. m /rad kg. m /rad kg- m kg -m kg -m kg -m2 /rad kg -m2 /rad kg -m2 /rad kg -m kg -m kg -m kg -m2 /rad kg -m2 /rad kg -m2 /rad kg -m kg -m kg -m kg -m2 /rad kg -m2 /rad kg .m2 /rad 106 T Pai

---

## Page 213

Table C.6: Added Mass Force Cross-term Coefficients Parameter Value Units Xq +0.00e+000 kg/rad Xwq -3.55e+001 kg/rad Xqq -1.93e+000 kg -m/rad Xvr +3.55e+001 kg/rad Xrp +0. 00e+000 kg m/rad Xr -1.93e+000 kg m/rad Xur +0.00e+000 kg/rad Xwr +0.00e+000 kg/rad Xvq +0.00e+000 kg/rad Xpq +0. 00e+000 kg m/rad Xqr +0. 00e+000 kg m/rad Yv, +0.00e+000 kg/rad Yo, +0.00e+000 kg/rad Yrra +0. 00e+000 kg-m/rad Y, +0. 00e+000 kg/rad Y,, +0.00e+000 kg -m/rad Yu, +0. 00e+000 kg/rad Ywr +0.00e+000 kg/rad Yura -9.30e-001 kg/rad YWP +3.55e+001 kg/rad Yp +1.93e+000 kg m/rad Yq, +0.00e+000 kg .m/rad Zwq +0.00e+000 kg/rad Zuqa +9.30e-001 kg/rad Zqqa +0.00e+000 kg - m/rad ZI, -3.55e+001 kg/rad ZIP +1.93e+000 kg/rad Z,, +0.00e+000 kg - m/rad Z., +0.00e+000 kg/rad Z.p +0.00e+000 kg/rad Zq +0.00e+000 kg/rad Zpq +0.00e+000 kg m/rad Zqr +0.00e+000 kg m/rad 107

---

## Page 214

表 C.6：附加质量力交叉项系数 Parameter Value Units X q +0.00e+000 kg/rad Xwq -3.55e+001 kg/rad Xqq -1.93e+000 kg -m /rad Xvr +3.55e+001 kg/rad Xrp +0. 00e+000 kg m /rad Xr -1.93e+000 kg m /rad Xur +0.00e+000 kg/rad Xwr +0.00e+000 kg/rad X vq +0.00e+000 kg/rad Xpq +0. 00e+000 kg m /rad Xqr +0. 00e+000 kg m /rad Yv, +0.00e+000 kg/rad Yo, +0.00e+000 kg/rad Yrra +0. 00e+000 k g -m /rad Y, +0. 00e+000 kg/rad Y,, +0.00e+000 kg -m /rad Yu, +0. 00e+000 kg/rad Ywr +0.00e+000 kg/rad Yura -9.30e-001 kg/rad YWP +3.55e+001 kg/rad Yp +1.93e+000 kg m /rad Yq, +0.00e+000 kg .m /rad Zwq +0.00e+000 kg/rad Zuqa +9.30e-001 kg/rad Zqqa +0.00e+000 kg - m /rad ZI, -3.55e+001 kg/rad ZIP +1.93e+000 kg/rad Z,, +0.00e+000 kg - m /rad Z., +0.00e+000 kg/rad Z.p +0.00e+000 kg/rad Zq +0.00e+000 kg/rad Zpq +0.00e+000 kg m /rad Zqr +0.00e+000 kg m /rad 107

---

## Page 215

Table C.7: Added Mass K-Moment Parameter Value Kw. +0.00e+000 K.q +0.00e+000 Kww +0.00e+000 Kwq +0.00e+000 Kqq +0.00e+000 K,, +0.00e+000 Kv, +0.00e+000 K., +0.00e+000 K, +0.00e+000 Kp +0.00e+000 K,, +0.00e+000 Kow +0.00e+000 Kw, +0.00e+000 Kw, +0.00e+000 Kur +0.00e+000 Kq +0.00e+000 Kpq +0.00e+000 Kqr +0.00e+000 Cross-term Coefficients Units kg kg- m/rad kg kg- m/rad kg -m2/rad2 kg kg- m/rad kg. m/rad kg- m2/rad2 kg. m2/rad2 kg kg kg. m/rad kg. m/rad kg. m/rad kg - m/rad kg. m2/rad2 kg. m2/rad2 108

---

## Page 216

表 C.7：附加质量 K-力矩 Parameter Value Kw. +0.00e+000 K .q +0.00e+000 Kww +0.00e+000 K w q +0.00e+000 Kqq +0.00e+000 K,, +0.00e+000 K v, +0.00e+000 K ., +0.00e+000 K, +0.00e+000 K p +0.00e+000 K,, +0.00e+000 Kow +0.00e+000 Kw, +0.00e+000 Kw, +0.00e+000 K u r +0.00e+000 K q +0.00e+000 Kpq +0.00e+000 Kqr +0.00e+000 交叉项系数 Units kg kg- m /rad kg kg- m /rad kg -m2/rad2 kg kg- m /rad kg. m /rad kg- m2/rad 2 kg. m2/rad 2 kg kg kg. m /rad kg. m /rad kg. m /rad kg - m /ra d kg. m2/rad 2 kg. m2/rad 2 108

---

## Page 217

Table C.8: Added Mass Parameter Mwq Muqa Mwwa Muwa Mv, M,, Mrp M, Mao Mur MpqW M., Mu MW, M., Mq Mg, Nas Nw. Naq Nw, Nqq Nova Na Nv, Nrp .N,, Nuva N,. N., Nura Nvq .Np~q N,qr M-, N-Moment Value +0.00e+000 +1. 93e+000 +0. 00e+000 +0.00e+000 +3.46e+001 +0.00e+000 -1. 93e+000 +0.00e+000 +0. 00e+000 +4.86e+000 +0.00e+000 +0.00e+000 +0. 00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0. 00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0. 00e+000 +0. 00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0.00e+000 -3.46e+001 +0.00e+000 +0.00e+000 +1. 93e+000 -1.93e+000 +0.00e+000 -4.86e+000 +0.00e+000 Table C.9: Propeller Terms Parameter Value Units Xprop +3.86e+000 N Kprop -5.43e-001 N-m Cross-term Coefficients Units kg m/rad kg m/rad kg kg kg kg m/rad kg -m/rad kg- m2/rad2 kg. m2/rad2 kg- m2/rad2 kg kg kg m/rad kg m/rad kg m/rad kg m/rad kg. m2/rad2 kg- m2/rad2 kg kg kg-m/rad kg m/rad kg. m2 /rad 2 kg kg-m/rad kg .m/rad kg- m2/rad2 kg -m2/rad2 kg kg kg -m/rad kg -m/rad kg -m/rad kg -m/rad kg- m2/rad2 kg- m2/rad2

---

## Page 218

表 C.8：附加质量 Parameter Mwq Muqa Mwwa Muwa Mv, M,, Mrp M, M a o Mur MpqW M., Mu MW, M., Mq M g , Nas Nw. N a q N w , Nqq Nova Na Nv, N rp .N,, Nuva N,. N., N ura Nvq .Np~q N,qr 等一下，稍等 Value +0.00e+000 +1. 93e+000 +0. 00e+000 +0.00e+000 +3.46e+001 +0.00e+000 -1. 93e+000 +0.00e+000 +0. 00e+000 +4.86e+000 +0.00e+000 +0.00e+000 +0. 00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0. 00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0. 00e+000 +0. 00e+000 +0.00e+000 +0.00e+000 +0.00e+000 +0.00e+000 -3.46e+001 +0.00e+000 +0.00e+000 +1. 93e+000 -1.93e+000 +0.00e+000 -4.86e+000 +0.00e+000 表 C.9：螺旋桨术语 Parameter Value Units Xprop +3.86e+000 N Kprop -5.43e-001 N-m 交叉项系数 Units kg m/rad kg m/rad kg kg kg kg m/rad kg -m/rad kg- m2/rad2 kg. m2/rad2 kg- m2/rad2 kg kg kg m/rad kg m/rad kg m/rad kg m/rad kg. m2/rad2 kg- m2/rad2 kg kg kg-m/rad kg m/rad kg. m2 /rad 2 kg kg-m/rad kg .m/rad kg- m2/rad2 kg -m2/rad2 kg kg kg -m/rad kg -m/rad kg -m/rad kg -m/rad kg- m2/rad2 kg- m2/rad2

---

## Page 219

Table C.10: Control Fin Parameter Value Yuudr +9.64e+000 Zuuds -9.64e+000 Mudsd -6.15e+000 Nuudr -6.15e+000 Yuvf -9.64e+000 ZUnf -9.64e+000 Yurf +6.15e+000 Zuqf -6.15e+000 MU.f -6.15e+000 Nuvf +6.15e+000 Muqf -3.93e+000 Nurf -3.93e+000 Coefficients Units kg/(m- rad) kg/(m- rad) kg/rad kg/rad kg/m kg/m kg/rad kg/rad kg kg kg m/rad kg- m/rad 110

---

## Page 220

表 C.10：控制翼 Parameter Value Yuudr +9.64e+000 Zuuds -9.64e+000 Mudsd -6.15e+000 Nuudr -6.15e+000 Yuvf -9.64e+000 ZUnf -9.64e+000 Yurf +6.15e+000 Zuqf -6.15e+000 M U .f -6.15e+000 N uvf +6.15e+000 M u q f -3.93e+000 Nurf -3.93e+000 系数 Units kg/(m - rad) kg/(m - rad) kg/rad kg/rad kg/m kg/m kg/rad kg/rad kg kg kg m /rad kg- m /rad 110

---

## Page 221

Appendix D Tables of Linearized Model Parameters Note that all coefficients are calculated for the STD REMUS hull profile. Table D.1: Linearized Combined Coefficients Parameter Z.c ZW1 Z.f Zqc Zqa Zqf Mwc M.. Mwf Msg Value -1.57e+001 -3.45e+001 -1.64e+001 +1.20e-001 +1.44e+000 -1. 12e+001 -4.03e-001 +5.34e+001 -1. 11e+001 -1. 12e+001 Mqc -2.16e+000 Mqa +2.97e+000 Mqf -7.68e+000 Units kg/s kg m/s kg m/s kg m/s kg- m/s kg m/s kg m/s kg m/s kg- m/s kg m/s kg -m2/s kg- m2/s kg rn 2/s Description Crossflow Drag Body Lift Fin Lift Crossflow Drag Added Mass Cross Term Fin Lift Crossflow Drag Added Mass Cross Term Body Lift Fin Lift Crossflow Drag Added Mass Cross Term Fin Lift

---

## Page 222

附录 D 线性化模型参数表 请注意，所有系数都是针对STD REMUS船体轮廓计算的。 Table D.1: Linearized Combined Coefficients Parameter Z.c ZW1 Z.f Zqc Zqa Zqf Mwc M.. Mwf M s g Value -1.57e+001 -3.45e+001 -1.64e+001 +1.20e-001 +1.44e+000 -1. 12e+001 -4.03e-001 +5.34e+001 -1. 11e+001 -1. 12e+001 Mqc -2.16e+000 Mqa +2.97e+000 Mqf -7.68e+000 Units kg/s kg m/s kg m/s kg m/s kg- m/s kg m/s kg m/s kg m/s kg- m/s kg m/s kg -m2/s kg- m2/s kg rn 2/s Description Crossflow Drag Body Lift Fin Lift Crossflow Drag Added Mass Cross Term Fin Lift Crossflow Drag Added Mass Cross Term Body Lift Fin Lift Crossflow Drag Added Mass Cross Term Fin Lift

---

## Page 223

Table D.2: Linearized Maneuvering Coefficients Parameter Value Units Description X0 +8. 90e+000 kg -m/s 2 Hydrostatic X -1. 35e+001 kg/s Axial Drag Xi -9.30e-001 kg Added Mass Xq -5.78e-001 kg -m/s Added Mass Cross Term Zw -6.66e+001 kg/s Combined Term Zq -9.67e+000 kg -m/s Combined Term Zi -3.55e+001 kg Added Mass Z4 -1.93e+000 kg -m Added Mass Z, -5.06e+001 kg- m/s 2  Fin Lift MO -5.77e+000 kg- m2/s 2 Hydrostatic M. +3.07e+001 kg m/s Combined Term Mq -6.87e+000 kg. m 2/s Combined Term Mb -1. 93e+000 kg m Added Mass M4 -4.88e+000 kg- m 2 Added Mass Z,, -3.46e+001 kg -m2/s2 Fin Lift 112

---

## Page 224

表 D.2：线性化机动系数 Parameter Value Units Description X0 +8. 90e+000 kg -m/s 2 Hydrostatic X -1. 35e+001 kg/s Axial Drag X i -9.30e-001 kg Added Mass Xq -5.78e-001 kg -m /s Added Mass Cross Term Zw -6.66e+001 kg/s Combined Term Zq -9.67e+000 kg -m /s Combined Term Z i -3.55e+001 kg Added Mass Z4 -1.93e+000 kg -m Added Mass Z, -5.06e+001 kg- m/s 2  Fin Lift MO -5.77e+000 kg- m2/s 2 Hydrostatic M. +3.07e+001 kg m /s Combined Term Mq -6.87e+000 kg. m 2/s Combined Term Mb -1. 93e+000 kg m Added Mass M4 -4.88e+000 kg- m 2 Added Mass Z,, -3.46e+001 kg -m2/s2 Fin Lift 112

---

## Page 225

Appendix E MATLAB Code E.1 Vehicle Simulation The REMUS simulator program was written using MATLAB. The first program, REMUSSIM.m, loads the vehicle initial conditions and tracks the vehicle state. The second program, REMUS.m, calculates the new vehicle accelerations based on the vehicle state and control inputs. E.1.1 REMUS-SIM.m X REMUSSIM.M Vehicle Simulator % M-FILE INPUTS X + coeffs.mat - generated by COEFFS.M, typically for each run % + vdata.mat - generated by COEFFS.M, typically for each run clear ; X clear all variables clc ; disp(sprintf('\n\n REMUS DYNAMICS SIMULATOR')) disp(sprintf (' Timothy Prestero, MIT/WHOI\n\n')) load vehicle-type ; disp(sprintf(' NOTE: Model using Xs REMUS dimensions.\n\n', vehicle)) % Check coeffs, initial conditions, and control input vector choose-setup = input(' Run set-up (y/n):','s') ; if choose-setup == y' sim-setup else showall end X Output flags show-step = 1 ; show-speed run-savedata = 0 ; run-plots Xchoosesetup = 1 ; = 0 showpos = 0 chooseint =0; =0;

---

## Page 226

附录 E MATLAB 代码 E.1  车辆仿真 REMUS 模拟器程序是用 MATLAB 编写的。第一个程序 REMUSSIM.m 加载车辆初始条件并跟 踪车辆状态。第二个程序 REMUS.m 根据车辆状态和控制输入计算新的车辆加速度。 E.1.1  REMUS-SIM.m X  REMUSSIM.M  车辆模拟器 % M-FILE 输入 X +  coeffs.mat - 由 COEFFS.M 生成，通常用于每次运行 % + vdata.mat - 由 COEFFS.M 生成，通常用于每次运行 清除 ； X  清除  所有变量 clc ； disp(sprintf('\n\n  REMUS 动力学模拟器')) disp(sprintf (' Timothy Prestero, MIT/WHOI\n\n')) loa d vehicle-type  ; disp(sprintf('  注意：模型使用 Xs REMUS 尺寸。\n\n',  vehicle)) % 检查系数，初始条件，以及控制输入向量 choose-setup = input('  运行设置 (y/n):','s')  ; 如果 choose-setup == y'sim-setup 否则 showall end X 输出标志 show-step = 1 ; show-speed run-savedata = 0 ; run-plots Xchoose setup = 1 ; = 0 showpos = 0 chooseint = 0; = 0;

---

## Page 227

X SET INTEGRATION METHOD int-list = {'Basic Euler' 'Improved Euler' 'Fourth-Order Runge-Kutta'} ; intmethods = {'euler' 'imp-euler' 'rkutta' }; if chooseint disp(sprintf(' Integration Method:\n')) for i = 1:size(int-list,2) ; disp(sprintf(' Xi - Xs', i, char(intjlist(i)))) end d = input('\n Enter a number: ') else d =3 end int_method = char(int-methods(d)) X check working directory cd-outputs ; X create .mat files d = clock ; yy = d(1) ; mo = d(2) ; dd = d(3) ; hh = d(4) ; mm = d(5) ; ss = d(6) ; date-string = datestr(datenum(yy,mo,dd),i) time-string = datestr(datenum(yy,mo,dd,hh,mm,ss),13) XX generate random filename X [dummy, file-string, dummy, dummy] = fileparts(tempname) Xdisp(sprintf('\nCurrent simulator data files:')); Xs *.mat; Xfile-string = input(sprintf('\nEnter name for data file: '), 's') temp-str = datestr(now,O) ; file-string = strcat('sim-',temp-str(1:2),temp-str(4:6),temp-str(10:11),'-',... tempstr(13:14), temp-str(16:17)) ; disp(sprintf('\nData file saved as\n Xs\\Xs.mat', cd, file-string)); X EXPERIMENTAL/ASSIGNED VALUES: initial conditions, input vector X -------------------------------------------------------------- X loading model inputs, generated in SIMSETUP.M load input-vector ; X data from FININPUTS.M on mission files load timestep load initialstate ; X data from INITIALCONDITIONS.M on above pitch_max = 90 X RUN MODEL %X--------------------------------------------------------------------- X Initialize number of steps and storage matrix if strcmp(intmethod,'euler') n-steps = size(ui,2) else n-steps = size(ui,2)-1 end output-table = zeros(n-steps,size(x,i)+size(ui,i)+7); disp(sprintf('\n Simulator running...')); X MAIN PROGRAM for i = 1:n-steps, X Print current step for error checking if show-step == 1 if ~rem(i*10,nsteps) disp( sprintf( ' Steps Completed : X02d XX ', i/n-steps*100)); end

---

## Page 228

X 设置积分方法 int-list  =  {'基本欧拉'  '改进欧拉'  '四阶龙格-库塔'}  ;  intmethods  =  {'eul er'  'imp-euler'  'rkutta'};  如果 chooseint 显示(sprintf('  积分方法: ')) 对 i =  1:size(int-list,2)  ; 显示(sprintf('  Xi  - Xs',  i,  char(intjlist(i)))) 结束 d =  输入('   输入一个数字:  ') 否则 d =3 结 束 int_method = char(int-methods(d)) X 检查工作目录 cd-outputs ; X 创建 .mat 文件 d = 时钟 ; yy = d(1) ; mo = d(2) ; dd =  d(3) ; hh = d(4) ; mm = d(5) ; ss =  d(6) ; 日期字符串 = datestr(datenum(yy,mo,dd),i) 时间字符串 = datestr(datenu m(yy,mo,dd,hh,mm,ss),13) XX 生成 随机 文件名 X [dummy, file-string, dummy, du mmy] = fileparts(tempname) Xdisp(sprintf(' 当前模拟器数据文件 :')); Xs *.mat; Xfile -string = input(sprintf(' 输入数据文件名称 : '), 's') temp-str = datestr(now,O) ; file-stri ng = strcat('sim-',temp-str(1:2),temp-str(4:6),temp-str(10:11),'-',... tempstr(13:14), tem p-str(16:17)) ; disp(sprintf(' 数据文件已保存为  Xs\Xs.mat', cd, file-string)); X  实验/指定值：初始条件，输入向量 X  ------------------------------------------ ------------- ------- X 加载模型输入，在 SIMSETUP.M 中生成 load 输入向量；X 数据来自 F ININPUTS.M 上的任务文件 load 时间步长 load 初始状态；X 数据来自 I NITIALCONDITIONS.M 上述内容 pitch_max =  90 X 运行 模型 %X--------------------------------------------------------------------- X 初始化步 数和存储矩阵 如果 strcmp(intmethod,'euler') n-steps = s i z e ( u i , 2 ) 否则步数 = size(ui, 2)-1 结束 输出表 = zeros(n-steps,size(x,i)+ size(ui,i)+ 7); disp(sprintf('\n  模拟器运行中. ..')); X 主程序 对于 i =  1:n-steps, X 打印 当前步骤 用于 错误检查 if sh o w -ste p  == 1 如果 ~ rem(i*10,nsteps) disp(sprintf('步骤完成：X02d XX ',  i/n-steps*100')); 结束

---

## Page 229

end X Store current states x(n), inputs ui(n), and time in seconds output-table(i,1:14) = [x' ui(:,i)'] ; outputtable(i,21) = (i-1)*time-step ; X Calculate forces, accelerations X ** CALLS REMUS.M X xdot(i) = f(x(i),u(i)) [xdot,forces] = remus(x,ui(:,i)'); X Store forces at step n outputtable(i,15:20) = [forces'] if strcmp(int-method,'euler') XX EULER INTEGRATION to calculate new states x(n+1) XX x(i+i) = x(i) + dx/dt*delta_t XX NOTE: overwriting old states with new states, saving back at the top of the loop x = x + (xdot .* time-step) ; elseif strcmp(int-method,'impeuler') XX IMPROVED EULER INTEGRATION to calculate new states ki_vec = x + (xdot .* timestep) ; k2_vec = remus(klvec, ui(:,(i+1))') x = x + 0.5.*timestep.*(xdot + k2_vec) elseif strcmp(int-method,'rkutta') XX RUNGE-KUTTA APPROXIMATION to calculate new states XX NOTE: ideally, should be approximating ui values for k2,k3 XX ie (ui(:,i)+ui(:,i+1))/2 kivec = xdot k2_vec = remus(x+(0.5.*time-step.*k1.vec), ((ui(:,i)+ui(:,i+1))./2)') ; k3_vec = remus(x+(0.5.*time-step.*k2_vec), ((ui(:,i)+ui(:,i+1))./2)') ; k4_vec = remus(x+(time-step.*k3_vec), ui(:,i+1)') x = x + time-step/6.*(kvec +2.*k2_vec +2.*k3-vec +k4-vec) X ki-vec = xdot ; X k2_vec = remus(x+(0.5.*time-step.*k1.vec), ((ui(:,i)+ui(:,i+1))./2)') X k3_vec = remus(x+(0.5.*time-step.*k2.vec), ui(:,i)') X k4_vec = remus(x+(timestep.*k3_vec), ui(:,i)') ; X x = x + time-step/6.*(ki_vec +2.*k2.vec +2.*k3_vec +k4_vec) end end X SAVE SIMULATOR OUTPUT X model coefficients and vehicle parameters loaded in REMUS.M load vdata ; load vehicle-type ; load inv-mass-matrix ; load vehiclecoeffs save(filestring, 'output-table', 'filestring', 'date-string', 'time-string', 'timestep', 'x', 'ui', ... 'W', 'Minv', 'B', 'm', 'g', 'rho', 'xg', 'yg', 'zg', 'xb', 'yb', 'zb', Ixx', 'Iyy', 'Izz', 'delta-max',... 'Xuu', 'Xudot', 'Xwq', 'Xqq', 'Xvr', 'Xrr', 'Xprop', 'Yvv', 'Yrr', 'Yuv', 'Yvdot', 'Yrdot', 'Yur', 'Ywp', 'Ypq', 'Yuudr', 'Zww', 'Zqq', 'Zuw', 'Zwdot', 'Zqdot', 'Zuq', 'Zvp', 'Zrp', 'Zuuds', 'Kpdot', 'Kprop', 'Kpp', ... 'Mww', 'Mqq', 'Muw', 'Mwdot', 'Mqdot', 'Muq', 'Mvp', 'Mrp', 'Muuds', 115

---

## Page 230

结束 X 存储当前状态 x(n)、输入 ui(n) 和以秒为单位的时间 output-table(i,1:14) = [x' ui(: ,i)'] ; outputtable(i,21) = (i-1)*时间步长 ; X  计算  力， 加速度 X  **  调用 REMUS.M X  xdot(i) =  f(x(i),u(i)) [xdot,forces]  =  remus( x,ui(:,i)'); 步骤 n 的 X 店力量 outputtable(i,15:20) = [f orces'] 如果 strcmp(int-method,'euler') XX 欧拉积分用于计算新状态 x(n+1) XX x(i+i) = x(i) + dx/dt*delta_t X X 注意：将旧状态覆盖为新状态，循环顶部保存 x = x + (xdot .* 时间步长) ; elseif strcmp(int-method, 'impeuler') XX 改进的欧拉积分用于计算新状态 ki_vec = x + (xdot .* 时间步长) ; k2_vec = remus(klvec , ui(:,(i+1))') x = x + 0.5.*时间步长.*(xdot + k2_vec) elseif strcmp(int-method,'rkutta') XX 龙格-库塔近似 用于计算新状态 XX 注意：理想情况下，应近似计算 k2,k3 的 ui 值 XX 即 (ui(:,i)+ ui(:,i+ 1))/2 kivec = xdot k2_vec = remus(x+(0.5.*时间步长.*k1.vec), ((ui(:,i)+ui(:,i+1))./2)') ; k3_vec = remus(x+(0.5.*时 间步长.*k2_vec), ((ui(:,i)+ui(:,i+1))./2)') ; k4_vec = remus(x+(时间步长.*k3_vec), ui(:,i+1)') x = x + 时 间步 e恩迪 X 保存模拟器输出 X 模型系数和车辆参数已加载到 REMUS.M 中 load vdata；加载车辆类型；加载 逆质量矩阵；加载车辆系数 保存(filestring, '输出表格', 'filestring', '日期字符串', '时间字符串', '时间步长', 'x', 'ui', ... 'W', 'Minv', 'B', 'm', 'g', 'rho', 'xg', 'yg', 'zg', 'xb', 'yb', 'zb', 'Ixx', 'Iyy', 'Izz', '最大偏差', ... 'Xu u', 'Xudot', 'Xwq', 'Xqq', 'Xvr', 'Xrr', 'Xprop', 'Yvv', 'Yrr', 'Yuv', 'Yvdot', 'Yrdot', 'Yur', 'Yw p', 'Ypq', 'Yuudr', 'Zww', 'Zqq', 'Zuw', 'Zwdot', 'Zqdot', 'Zuq', 'Zvp', 'Zrp', 'Zuuds', 'Kpdot', ' Kprop', 'Kpp', ... 'Mww', 'Mqq', 'Muw', 'Mwdot', 'Mqdot', 'Muq', 'Mvp', 'Mrp', 'Muuds'} 115

---

## Page 231

'Nvv', 'Nrr', 'Nuv', 'Nvdot', 'Nrdot', 'Nur', 'Nwp', 'Npq', 'Nuudr') % return to working directory cdmodel ; X save text file of ismulator inputs if runsavedata savedata end X Plot output figstart = input('\n Starting Figure Number ') figstart = figstart - 1; remusplots simplot if run-plots fmplot end disp(sprintf('\n')) return E.1.2 REMUS.m X REMUS.M Vehicle Simulator, returns the time derivative of the state vector function [ACCELERATIONS,FORCES] = remus(x,ui) X TERMS % --------------------------------------------------------------------- X STATE VECTOR: X x = [u v w p q r xpos ypos zpos phi theta psi]' X Body-referenced Coordinates X u = Surge velocity [m/sec] X v = Sway velocity [m/sec] X w = Heave velocity [m/sec] X p = Roll rate [rad/sec] X q = Pitch rate [rad/sec] X r = Yaw rate [rad/sec] X Earth-fixed coordinates % xpos = Position in x-direction [m] X ypos = Position in y-direction [m] X zpos = Position in z-direction [m] X phi = Roll angle [rad] X theta = Pitch angle [rad] X psi = Yaw angle [rad] X INPUT VECTOR X ui = [deltas delta_r]' X Control Fin Angles % delta-s = angle of stern planes [rad] X delta-r = angle of rudder planes [rad] X Initialize global variables %7--------------------------------------------------------------------- load vdata ;% W and B, CG and CB coords load inv-massmatrix ;% Minv matrix 116

---

## Page 232

'Nvv', 'Nrr', 'Nuv', 'Nvdot', 'Nrdot', 'Nur', 'Nwp', 'Npq', 'Nuudr' % 返回工作目录 cdmodel  ; X 保存模拟器输入的文本文件，如果运行保存 数据 savedata 结束 X  绘图  输出  figstart  =  输入('   起始图形编号  ')  figstart = figstart  - 1; remusplots simplot  如果 run-plots fmplot 结束 显示(sprintf(' ')) 返回 E.1.2  REMUS.m X  REMUS.M  车辆模拟器，返回状态向量的时间导数 函数 [加速度, 力] = remus(x, ui) X  术语 % --------------------------------------------------------------------- X 状态向量: X  x =  [u  v w p q r xpos  ypos  zpos  phi theta psi]' X  机体参考坐 标 X  u  =  前进速度 [米/秒] X  v  =  横向速度 [米/秒] X  w  =  垂向速度 [米/ 秒] X  p  =  横滚角速率 [弧度/秒] X  q  =  纵俯角速率 [弧度/秒] X  r  =  偏航 角速率 [弧度/秒] X  地固定坐标 %  xpos  =  x方向位置 [米] X  ypos  =  y方向 位置 [米] X  zpos  =  z方向位置 [米] X  phi  =  横滚角 [弧度] X  theta  =  纵俯 角 [弧度] X  psi  =  偏航角 [弧度] X  输入向量 X ui  =  [deltas delta_r]' X  控 制舵角 %  delta-s  =  尾面舵角 [弧度] X  delta-r  =  舵面角 [弧度] X  初始化全局变量 %7--------------------------------------------------------------------- 加载 vdata  ;%  W 和 B，CG 和 CB 坐标 加载  逆质量矩阵  ;%  Minv 矩阵 116

---

## Page 233

load vehicle-coeffs ; non-zero vehicle coefficients only X Output flags showforces = 10 X Get and check state variables and control inputs X Get state variables u =x(1) ;v =x(2) ;w =x(3) ;p =x(4) q = x(5) ; r = x(6) phi = x(10) theta = x(11) ; psi = x(12) X Get control inputs delta-s = ui(1) ; deltar = ui(2) X Check control inputs (useful later) if delta-s > deltamax delta-s = sign(delta-s)*deltamax end if delta-r > delta-max delta-r = sign(delta-r)*delta-max end X Initialize elements of coordinate system transform matrix c1 = cos(phi); c2 = cos(theta); c3 = cos(psi); s1 = sin(phi); s2 = sin(theta); s3 = sin(psi); t2 = tan(theta); X Set total forces from equations of motion X = -(W-B)*sin(theta) + Xuu*u*abs(u) + (Xwq-m)*w*q + (Xqq + m*xg)*q^2 ... + (Xvr+m)*v*r + (Xrr + m*xg)*r^2 -m*yg*p*q - m*zg*p*r ... + Xprop Y = (W-B)*cos(theta)*sin(phi) + Yvv*v*abs(v) + Yrr*r*abs(r) + Yuv*u*v ... + (Ywp+m)*w*p + (Yur-m)*u*r - (m*zg)*q*r + (Ypq - m*xg)*p*q ... + Yuudr*u^2*delta-r Z = (W-B)*cos(theta)*cos(phi) + Zww*w*abs(w) + Zqq*q*abs(q)+ Zuw*u*w ... + (Zuq+m)*u*q + (Zvp-m)*v*p + (m*zg)*p^2 + (m*zg)*q^2 ... + (Zrp - m*xg)*r*p + Zuuds*u^2*delta-s K = -(yg*W-yb*B)*cos(theta)*cos(phi) - (zg*W-zb*B)*cos(theta)*sin(phi) ... + Kpp*p*abs(p) - (Izz-Iyy)*q*r - (m*zg)*w*p + (m*zg)*u*r + Kprop M = -(zg*W-zb*B)*sin(theta) - (xg*W-xb*B)*cos(theta)*cos(phi) + Mww*w*abs(w) ... + Mqq*q*abs(q) + (Mrp - (Ixx-Izz))*r*p + (m*zg)*v*r - (m*zg)*w*q ... + (Muq - m*xg)*u*q + Muw*u*w + (Mvp + m*xg)*v*p ... + Muuds*u^2*delta s N = -(xg*W-xb*B)*cos(theta)*sin(phi) - (yg*W-yb*B)*sin(theta) ... + Nvv*v*abs(v) + Nrr*r*abs(r) + Nuv*u*v ... + (Npq - (Iyy-Ixx))*p*q + (Nwp - m*xg)*w*p + (Nur + m*xg)*u*r ... + Nuudr*u^2*delta-r ; FORCES = [X Y Z K M N]'

---

## Page 234

load vehicle-coeffs ; non-zero vehicle coefficients only X 输出标志 showforc es  =  10 X 获取并检查状态变量和控制输入 X 获取状态变量 u  =x(1)  ;v  =x(2)  ;w  =x(3)  ;p  =x(4)  q  = x(5)  ;  r  = x(6)  phi  =  x(10)  theta =  x(11)  ;  psi =  x(12) X 获取控制输入 delta-s = ui(1) ; deltar = ui(2) X  检查控制输入（稍后有用） 如果 delta-s  >  d eltamax delta-s  =  sign(delta-s)*deltamax 结束 如 果 delta-r  >  delta-max delta-r  =  sign(delta-r)*delt a-max 结束 X 初始化坐标系变换矩阵的元素 c1  =  cos(phi);  c2  =  cos(theta);  c3  =  cos(psi);  s1  =  sin(phi);  s2  =  sin(theta);  s3  =  sin( psi);  t2  =  tan(theta); X  从运动方程中设定总力 X =  -(W-B)*sin(θ)  +  Xuu*u*abs(u) +  (Xwq-m)*w*q +  (Xqq + m*xg)*q^2  ... +  (Xvr+m)*v*r +  (Xrr +  m*xg)*r^2 -m*yg*p*q - m*zg*p*r  ... +  Xprop Y =  (W-B)*cos(θ)*sin(φ) +  Yvv*v*abs(v) +  Yrr*r*abs(r)  + Yuv*u*v  ... +  (Ywp+m)*w*p +  (Y u r-m )* u * r  - (m*zg)*q*r  +  (Ypq  - m*xg)*p*q  ... +  Yuudr *u^2*delta-r Z =  (W-B)*cos(theta)*cos(phi) +  Zww*w*abs(w)  +  Zqq*q*a bs(q)+ Zuw*u*w  ... +  (Zuq+m)*u*q +  (Zvp-m)*v*p +  (m*zg)*p^2  +  (m*zg)*q^2  ... +  (Zrp - m* xg)*r*p +  Zuuds*u^2*delta-s K =  -(yg*W-yb*B)*cos(theta)*cos(phi)  - (zg*W-zb*B)*cos(theta)*sin(phi)  ... +  Kpp*p*a bs(p)  - (Izz-Iyy)*q*r - (m*zg)*w*p +  (m*zg)*u*r +  Kprop M =  -(zg*W-zb*B)*sin(theta)  - (xg*W-xb*B)*cos(theta)*cos(phi)  + Mww*w*abs(w) ... +  Mqq*q*abs(q) +  (Mrp - (Ixx-Izz))*r*p  +  (m*zg)*v*r - (m*zg)*w*q ... +  (Muq - m*xg)* u*q +  Muw*u*w +  (Mvp +  m*xg)*v*p  ... +  Muuds*u^2*delta  s N =  -(xg*W-xb*B)*cos(theta)*sin(phi)  - (yg*W-yb*B)*sin(theta)  ... +  Nvv*v*abs(v) + Nrr*r*abs(r) +  Nuv*u*v  ... +  (Npq - (Iyy-Ixx))*p*q +  (Nwp - m*xg)*w*p +  (Nur +  m*x g)*u*r  ... +  Nuudr*u^2*delta-r  ; 力 =  [X  Y  Z  K  M N]’

---

## Page 235

ACCELERATIONS =.. [Minv(1,1)*X+Minv(1,2)*Y+Mflv(1,3)*Z+Milv(1,4)*K+Milv(1,5)*M+Miflv(1,6)*N Minv(2,1)*X+Milv(2,2)*Y+Mjflv(2,3)*Z+Mjflv(2,4)*K+Mlflv(2,5)*M+Mjflv(2,6)*N Minv(3,1)*X+Minv(3,2)*Y+Minv(3,3)*Z+Minv(3,4)*K+Milv(3,5)*M+Milv(3,6)*N Minv(4,1)*X+Minv(4,2)*Y+Minv(4,3)*Z+Minv(4,4)*K+Minv(4,5)*M+Minv(4,6)*N Minv(5,1)*X+Minv(5,2)*Y+Miflv(5,3)*Z+Mjr'v(5,4)*K+Minv(5,5)*M+Milv(5,6)*N Minv(6,1)*X+Milv(6,2)*Y+Milv(6,3)*Z+Mflv(6,4)*K+Mflv(6,5)*M+Mflv(6,6)*N c3*c2*u + (c3*s2*sl-s3*cl)*v + (s3*sl+c3*cl*s2)*w s3*c2*u + (cl*c3+sl*s2*s3)*v + (cl*s2*s3-c3*sl)*w -s2*u + c2*sl*v + cl*c2*w p + sl*t2*q + cl*t2*r cl*q - sl*r sl/c2*q + cl/c2*r]

---

## Page 236

加速度 =.. [Minv(1,1)*X+ Minv(1,2)*Y+ Mflv(1,3)*Z+ Milv(1,4)*K+ Milv(1,5)*M+ Miflv(1,6)*N Minv(2,1)*X+ Milv(2,2)*Y+ Mjflv(2,3)*Z+ Mjflv(2,4)*K+ Mlflv(2,5)*M+ Mjflv(2,6)*N Minv(3,1)*X + Minv(3,2)*Y+ Minv(3,3)*Z+ Minv(3,4)*K+ Milv(3,5)*M+ Milv(3,6)*N Minv(4,1)*X+ Minv(4,2)* Y+ Minv(4,3)*Z+ Minv(4,4)*K+ Minv(4,5)*M+ Minv(4,6)*N Minv(5,1)*X+ Minv(5,2)*Y+ Miflv(5,3 )*Z+ Mjr'v(5,4)*K+ Minv(5,5)*M+ Milv(5,6)*N Minv(6,1)*X+ Milv(6,2)*Y+ Milv(6,3)*Z+ Mflv(6,4) *K+ Mflv(6,5)*M+ Mflv(6,6)*N c3*c2*u +  (c3*s2*sl-s3*cl)*v +  (s3*sl+c3*cl*s2)*w s3*c2*u +  (cl* c3+sl*s2*s3)*v +  (cl*s2*s3-c3*sl)*w -s2*u +  c2*sl*v +  cl*c2*w p +  sl*t2*q +  cl*t2*r cl*q  - sl*r sl/ c2*q +  cl/c2*r]

---

## Page 237

Appendix F Example REMUS Mission File The following is an example REMUS mission file, taken from the thesis field experiment conducted on 27 July 1999. The goals of this particular experiment were to measure: " the vehicle behaviour with zeroed fins * the vehicle response to step changes in stern plane and rudder angle * the vehicle turn radius as a function of steady-state rudder angle " the vehicle roll offset as a function of propeller RPM See Section 7.4.3 for the details of mission programming. F.1 REMUS Mission Code [Types of objectives] Timer=Waits <DELAY> seconds before completing Wait for event=Waits for a flag to be set Dead Reckon=Dead Reckons the vehicle to a LAT/LON goal Set position=Sets the position of the vehicle to a LAT/LON Wait depth=Waits until the vehicle is deeper than a depth before continuing Transponder Home=Uses a transponder to home the vehicle to a LAT/LON goal Test ping=Generates a test ping on the selected channel. Wait transponder=Waits until acquires the selected transponder Dock=Docks the vehicle Undock=Undocks the vehicle ATS diagnostic=Creates ATS matlab file for diagnostic purposes Surf ace=Surfaces the vehicle Selftest=Performs offline vehicle diagnostics Wait prop=Waits until the vehicle's prop is spun before continuing Compass cal=Does an in water calibration of the PNI compass Long Baseline=Uses range to 2 transponders to navigate the vehicle LBL rows=Uses LBL nav to mow the lawn [Objective] type=Set Position Destination name=START Destination latitude= Destination longitude= Offset direction=131 Offset distance (Meters)=0 Offset Y axis (Meters)=O 119

---

## Page 238

附录 F 示例 REMUS 任务 文件 以下是一个 REMUS 任务文件示例，取自 1999 年 7 月 27 日进行的论文现场实验。本次实验的 具体目标是测量： ‧ 在鳍片归零的情况下的车辆行为 ‧ 车辆对尾舵平面和舵角阶跃变 化的响应 ‧ 车辆转弯半径与稳态舵角的关系 车辆滚动偏移作为螺旋桨转速的函数 请参阅第7.4.3节以了解任务编程的详细信息。 F.1  REMUS  任务 代码 [目标类型] 定时器=等待 <延迟> 秒后完成 事件等待=等待标志被设置 死推算=将车辆死推算到 LA T/LON 目标 设置位置=将车辆位置设置为 LAT/LON 等待深度=等待车辆达到指定深度后继续 使用 应答器回航=使用应答器将车辆回航到 LAT/LON 目标 测试声呐=在选定通道生成测试声呐 等待应 答器=等待获取选定的应答器 停靠=将车辆停靠 停车=将车辆脱离停靠 ATS 诊断=创建用于诊断的 ATS Matlab 文件 浮出水面=使车辆浮出水面 自检=执行离线车辆诊断 等待推进器=等待车辆推进 器旋转后继续 指南针校准=对 PNI 指南针进行水中校准 长基线=使用与两个应答器的测距导航车 辆 LBL 行= [目标] 类型=设置 位置 目的地 名 称=开始 目的地 纬度= 目的地 经 度= 偏移 方向=131 偏移 距离（米 ）=0 偏移 Y 轴（米）=O 119

---

## Page 239

[Objective] type=Wait prop Required rpm=60 Auto calibrate depth sensor=NO [Objective] ## GET TO START DEPTH (2M) AND HEADING (130) ########## type=Long baseline Destination name=START Destination latitude= Destination longitude= Offset direction=130 Offset distance (Meters)=200 Offset Y axis (Meters)=O Minimum range (M.)=10 Depth control mode=normal #normal triangle altitude Depth=2.0 RPM=1500 timeout (seconds)=-1 Trackline follow meters=200 Track ping interval (secs.)=5.0 Transponder #1=NOPP_Al Transponder #2=NOPP.A2 [Objective] ## CONTROLLED LEVEL FLIGHT ########## type=Timer Delay in seconds=180.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=2.0 Heading command=130.0 [Objective] ## ZERO ALL FINS ########## type=Timer Delay in seconds=2.0 Keep current commands=NO Direct (pitch rudder thruster)=pitch rudder Direct pitch command=O Direct rudder command=O RPM command=1500.0 [Objective] ## TIMER TO DEPTH 2M type=Timer Delay in seconds=60.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=2.0 Heading command=130.0 [Objective] #### PITCH DOWN 2, HEADING ########## type=Timer Delay in seconds=4.0 Keep current commands=NO Direct (pitch rudder thruster)=pitch Direct pitch command=10 Heading command=130.0 RPM command=1500.0

---

## Page 240

[目标] 类型=等待  属性 必需 转速=60 自动 校准 深度传感器=否 [目标]  ## 到达起始深度 (2米) 和航向 (130)  ########## 类型=长基线 目的地名称=起点 目的地纬度= 目的地经度= 偏移方向=130 偏移距离 (米)=200 偏移Y轴 (米)=最小范围 (米 )=10 深度控制模式=正常 #正常 三角形 海⾋深度=2.0 转速=1500 超时时间 (秒)=-1 跟踪 线跟随米=200 跟踪ping间隔 (秒)=5.0 应答器 #1=NOPP_Al 应答器 #2=NOPP.A2 [目标]  ##  控制水平飞行  ########## 类型=定时器延迟（秒） =180.0 保持当前指令=否 直接（俯仰 方向舵 推进器）=无 转速 指令=1500.0 水深指令=2.0 航向指令=130.0 [目标]  ##  清零  所有  翼鳍  ########## 类型=定时器 延迟（秒）=2.0 保持当前命令=否 直接（俯仰 方向舵 推进器）= 俯仰 方向舵 直接 俯仰命令=0 直接方向舵命 令=0 转速命令=1500.0 [目标]  ##  深度 2米的定时器 类型=定时器 延 时（秒）=60.0 保持当前指令=否 直接（纵倾 舵、方向舵、推进器）=无 转速指令=1500.0 深度指令=2.0 航向指令=130.0 [目标] #### 俯仰下降 2，航向 ########## 类型=定时器 延迟（ 秒）=4.0 保持当前命令=否 直接（俯仰、方向舵、推进器）= 直 接俯仰指令=10 航向指令=130.0 转速指令=1500.0

---

## Page 241

[Objective] ## TIMER TO DEPTH 6M type=Timer Delay in seconds=90.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=6.0 Heading command=130.0 [Objective] ## PITCH UP 2, HEADING type=Timer Delay in seconds=10.0 Keep current commands=NO Direct (pitch rudder thruster)=pitch Direct pitch command=-10 Heading command=130.0 RPM command=1500.0 [Objective] ## TIMER TO DEPTH 2M type=Timer Delay in seconds=90.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=2.0 Heading command=130.0 [Objective] #### PITCH DOWN 4, HEADING *######### type=Timer Delay in seconds=6.0 Keep current commands=NO Direct (pitch rudder thruster)=pitch Direct pitch command=20 Heading command=130.0 RPM command=1500.0 [Objective] ## TIMER TO DEPTH 6M type=Timer Delay in seconds=90.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=6.0 Heading command=130.0 [Objective] ## PITCH UP 4, HEADING type=Timer Delay in seconds=8.0 Keep current commands=NO Direct (pitch rudder thruster)=pitch Direct pitch command=-20 Heading command=130.0 RPM command=1500.0 [Objective] ## TIMER TO DEPTH 3M type=Timer Delay in seconds=90.0 Keep current commands=NO

---

## Page 242

[目标]  ##  定时器 到 深度 6米 类型=定时器 延迟（秒）=90.0 保持当前命令=否 直接（俯 仰 舵推进器）=无 转速命令=1500.0 深度命令 =6.0 航向命令=130.0 [目标]  ## 俯仰 2，航向 类型=定时器延迟（秒 ）=10.0 保持当前命令=否 直接（俯仰 方向舵 推进器）= 俯仰 直接俯仰命令=-10 航向命令=1 30.0 转速命令=1500.0 [目标]  ## 定时器至深度 2米 类型=定时器 延 迟（秒）=90.0 保持当前命令=否 直接（俯仰 方向舵 推进器）=无 转速命令=1500.0 深度命 令=2.0 航向命令=130.0 [目标] #### 下俯 4，航向 *######### 类型=定时器 延时（秒）= 6.0 保持当前指令=否 直接（俯仰 方向舵 推进器）= 俯仰 直接 俯 仰 指令=20 航向 指令=130.0 转速 指令=1500.0 [目标]  ##  深度6米定时器 类型= 定时器延迟 （秒）=90.0 保持当前指令=否 直接控制（俯 仰、方向舵、推进器）=无 转速指令=1500.0 深度指令=6.0 航向指令=130.0 [目标]  ##  上仰 4， 航向 类型=定时器延时（ 秒）=8.0 保持当前指令=否 直接（俯仰方向舵 推进器）=俯仰 直接俯仰指令=-20 航向 指令=1 30.0 转速 指令=1500.0 [目标]  ##  定时器 到深度 3米 类型= 定时 器延时（秒）=90.0 保持当前命令=否

---

## Page 243

Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=3.0 Heading command=130.0 [Objective] #### PITCH DOWN 6, HEADING ########## type=Timer Delay in seconds=3.0 Keep current commands=NO Direct (pitch rudder thruster)=pitch Direct pitch command=20 Heading command=130.0 RPM command=1500.0 [Objective] ## TIMER TO DEPTH 6M type=Timer Delay in seconds=90.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=6.0 Heading command=130.0 [Objective] ## PITCH UP 6, HEADING type=Timer Delay in seconds=4.0 Keep current commands=NO Direct (pitch rudder thruster)=pitch Direct pitch command=-20 Heading command=130.0 RPM command=1500.0 [Objective] ## TIMER TO DEPTH 3M type=Timer Delay in seconds=90.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=3.0 Heading command=130.0 [Objective] #### RUDDER CIRCLE PORT, FIXED PITCH ########## type=Timer Delay in seconds=20.0 Keep current commands=NO Direct (pitch rudder thruster)=pitch rudder Direct pitch command=10 Direct rudder command=40 RPM command=1500.0 [Objective] ## TIMER TO DEPTH 3M, HEADING 130 type=Timer Delay in seconds=120.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=3.0 Heading command=130.0 122

---

## Page 244

直接（方向舵推进器）=非 e 转速命令=1500.0 深度命令 =3.0 航向命令=130.0 [目标] #### 俯仰下调 6，航向 ######### # type=定时器延迟（秒）=3.0 保持当前命令=否 直接（俯仰 方向舵 推进器）= 俯仰 直接俯仰 命令=20 航向命令=130.0 转速命令=1500.0 [目标]  ##  定时器 到深度 6米 类型=定时器 延迟（秒）=90.0 保持当前命令=否 直接（ 俯仰 襟舵 推进器）= 无 e 转速命令=1500.0 深度命令 =6.0 航向命令=130.0 [目标]  ## 向上俯仰 6，航向 类型=计时延迟 秒=4.0 保持当前命令=否 直接（俯仰 方向舵 推进器）= 俯仰 直接俯仰命令=-20 航向命令=1 30.0 转速命令=1500.0 [目标]  ## 到深度计时  3米 类型=计时器 延 迟 以秒为单位=90.0 保持当前指令=否 直接 （升降舵 方向舵 推进器）=无 e 转速命令=1500.0 深度命 令=3.0 航向命令=130.0 [目标] ####舵轮端口，固定螺距######### # 类型=定时器延迟（秒）=20.0 保持当前命令=否 直接（ 俯仰 舵 推进器）=俯仰 舵 直接俯仰命令=10 直接舵命 令=40 转速命令=1500.0 [目标]  ##  定时器 到深度3米，航向13 零 类型=定时器延迟（秒）=120.0 保持当前命令 =否 直接（舵面 螺旋桨 推进器）=无 转速命 令=1500.0 深度命令=3.0 航向命令=130.0 12二

---

## Page 245

[Objective] ## RUDDER CIRCLE STBD, FIXED PITCH type=Timer Delay in seconds=20.0 Keep current commands=NO Direct (pitch rudder thruster)=pitch rudder Direct pitch command=0 Direct rudder command=-40 RPM command=1500.0 [Objective] ## TIMER TO DEPTH 3M, HEADING 130 type=Timer Delay in seconds=120.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1500.0 Depth command=3.0 Heading command=130.0 [Objective] ## ZERO RUDDER, DEPTH type=Timer Delay in seconds=120.0 Keep current commands=NO Direct (pitch rudder thruster)=rudder Direct rudder command=0 Depth command=3.0 RPM command=1500.0 [Objective] ## SPIN DOWN PROP 1250 ########## type=Timer Delay in seconds=120.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1250.0 Depth command=3.0 Heading command=130.0 [Objective] ## SPIN DOWN PROP 1000 type=Timer Delay in seconds=120.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=1000.0 Depth command=3.0 Heading command=130.0 [Objective] ## SPIN DOWN PROP 750 type=Timer Delay in seconds=120.0 Keep current commands=NO Direct (pitch rudder thruster)=none RPM command=750.0 Depth command=3.0 Heading command=130.0 [Objective] ## SPIN DOWN PROP 500 type=Timer Delay in seconds=120.0 Keep current commands=NO Direct (pitch rudder thruster)=none 123

---

## Page 246

[目标]  ## 方向舵圆盘 右舷，固定桨距 类型=计时器延迟（秒 ）=20.0 保持当前指令=否 直接（桨距方向舵推进器）=桨距 方向舵 直接桨距指令=0 直接方向舵指令=-40 转速指令=1500. 0 [目标]  ## 定时器至深度 3米，航向 130 类型=定时器延迟（ 秒）=120.0 保持当前指令=否 直接（俯仰 舵机 推进器）= 无 转速指令=1500.0 深度指令=3.0 航向指令=130.0 [目标]  ##  零方向舵，深度 类型=计时器延迟 （秒）=120.0 保持当前指令=否 直接（俯仰 舵 推进器）= 舵 直接舵指令=0 深度指令=3.0 转速 指令=1500.0 [目标]  ##  螺旋桨降速 1250 ########## 类型=计时器 延 迟（秒）=120.0 保持当前指令=否 直接（俯仰 方向舵 推进 器）= 无 转速指令=1250.0 深度指令=3.0 航向指令=130.0 [目标]  ## SPIN DOWN PROP  1000 类型=计 时器延迟（秒）=120.0 保持当前指令=否 直接 （俯仰 方向舵 推进器）= 无 RPM 指令=1000. 0 深度指令=3.0 航向指令=130.0 [目标]  ##  旋转停止螺旋桨 750 型 = 定时器 延迟（秒）=120.0 保持当前指令=否 直接（ 俯仰 襟舵 推进器）= 无 转速指令=750.0 深度 指令=3.0 航向指令=130.0 [目标]  ##  SPIN  DOWN  PROP  500 类型=计 时器延迟（秒）=120.0 保持当前命令=否 直接 （俯仰方向舵推进器）=无 123

---

## Page 247

RPM command=500.0 Depth command=3.0 Heading command=130.0 [Objective] type=END 124

---

## Page 248

转速命令=500.0 深度命令 =3.0 航向命令=130.0 [目标] 类型= 结束 124

---

## Page 249

Bibliography [1] Martin Abkowitz. Stability and Motion Control of Ocean Vehicles. MIT Press, Cambridge, MA, 1972. [2] B. Allen, R. Stokey, T. Austin, N. Forrester, R. Goldsborough, M. Purcell, and C. von Alt. REMUS: A small, low cost AUV; system description, field trials and performance results. In Proceedings MTS/IEEE Oceans 1997, Halifax, Canada, 1997. 36 [3] B. Allen, W. Vorus, and T. Prestero. Propulsion system performance enhancements on REMUS AUVs. In Proceedings MTS/IEEE Oceans 2000, Providence, Rhode Island, September 2000. 36 [4] P. Edgar An. An experimental self-motion study of the Ocean Explorer AUV in controlled sea states. IEEE Journal of Oceanic Engineering, 23(3):274-284, 1998. 100 [5] P. Ananthakrishnan. Dynamic response of an underwater body to surface waves. In Proceedings ASME Forum on Advances in Free Surface and Interface Fluid Dyanamics, San Francisco, CA, 1999. [6] Robert D. Blevins. Formulas for Natural Frequency and Mode Shape. Kreiger Publishing, Florida, 1979. 27, 28, 29 [7] M. R. Bottaccini. The stability coefficients of standard torpedoes. NAVORD Report 3346, U.S. Naval Ordnance Test Station, China Lake, CA, 1954. 25, 30, 42, 98 [8] J. Feldman. Revised standard submarine equations of motion. Report DTNSRDC/SPD-0393- 09, David W. Taylor Naval Ship Research and Development Center, Bethesda, MD, June 1979. [9] John E. Fidler and Charles A. Smith. Methods for predicting submersible hydrodynamic char- acteristics. Report NCSC TM-238-78, Naval Coastal Systems Laboratory, Panama City, FL, 1978. 30 [10] Thor I. Fossen. Guidance and Control of Ocean Vehicles. John Wiley & Sons, New York, 1994. 27 [11] R. W. Fox and A. T. McDonald. Introduction to Fluid Mechanics. J. Wiley and Sons, New York, 4th edition, 1992. [12] M. Gertler and G. Hagen. Standard equations of motion for submarine simulation. Report DTNSRDC 2510, David W. Taylor Naval Ship Research and Development Center, Bethesda, MD, June 1967. [13] Michael J. Griffin. Numerical prediction of the forces and moments on submerged bodies operating near the free surface. In Proceedings of the 2000 SNAME/ASNE Student Paper Night, Massachusetts Institute of Technology, January 2000. SNAME. 100 [14] Michael F. Hajosy. Six Degree of Freedom Vehicle Controller Design for the Operation of an Unmanned Underwater Vehicle in a Shallow Water Environment. Ocean Engineer's thesis, Massachusetts Institute of Technology, Department of Ocean Engineering, May 1994. 125

---

## Page 250

参考文献 [1] Martin Abkowitz. Stability and Motion Control of Ocean Vehicles.  麻省理工学院出版社，剑 桥，马萨诸塞州，1972年。 [2] B. Allen, R. Stokey, T. Austin, N. Forrester, R. Goldsborough, M. Purcell, C. von Alt. REMUS： 一种小型、低成本的自航水下机器人；系统描述、现场试验及性能结果。发表于加拿大哈利法 克斯，1997年。36 [3]  B. Allen，W. Vorus 和 T. Prestero。REMUS AUV 的推进系统性能提升。在 Proceedings M T S/IE E E  Oceans 2000,  罗德岛州普罗维登斯，2000 年 9 月。36 [4] P. Edgar An. 《Ocean Explorer AUV在受控海况下的实验性自运动研究》. IEEE Journal of Oceanic Engineering, 23(3):274-284, 1998. 100 [5] P. Ananthakrishnan. 水下物体对水面波的动态响应。发表于 Proceedings ASME Forum on Advances in Free Surface and Interface Fluid Dyanamics,  旧金山，加利福尼 亚州，1999年。 [6] 罗伯特·D·布莱文斯。Formulas for Natural Frequency and Mode Shape.  克里格出版社，佛 罗里达，1979年。27，28，29 [7] M. R. Bottaccini. 标准鱼雷的稳定系数。NAVORD 报告 3346，美国海军军械测试站，中国 湖，加利福尼亚州，1954年。25, 30, 42, 98 [8] J. Feldman. 修订标准潜艇运动方程。报告 DTNSRDC/SPD-0393-09，David W. Taylor 海军 舰船研究与开发中心，马里兰州贝塞斯达，1979 年 6 月。 [9] 约翰·E·菲德勒和查尔斯·A·史密斯。用于预测潜水器水动力特性的 方法。报告 NCSC TM-23 8-78，海军沿海系统实验室，佛罗里达州巴拿马城，1978 年。30 [10] 托尔·I·福森. Guidance and Control of Ocean Vehicles.  约翰·威利父子公司, 纽约, 1994. 27 [11] R. W. 福克斯 和 A. T. 麦克唐纳. Introduction to Fluid Mechanics.  约翰·威利与儿子公司, 纽 约, 第4版, 1992. [12] M. Gertler 和 G. Hagen。用于潜艇仿真的标准运动方程。报告 DTNSRDC 2510，美国马里 兰州贝塞斯达大卫·W·泰勒海军船舶研究与发展中心，1967年6月。 [13]  Michael J. Griffin. 潜水体在接近自由水面操作时的力和力矩的数值预测。发表于 Proceedings of the 2000 SNAME/ASNE Student Paper Night,  麻省理工学院, 2000年1月。SNA ME. 100 [14]  Michael F. Hajosy. Six Degree of Freedom Vehicle Controller Design for the Operation of an Unmanned Underwater Vehicle in a Shallow Water Environment.  海洋工程师论文，麻省理工 学院，海洋工程系，1994年5月。 125

---

## Page 251

[15] Sighard F. Hoerner. Fluid Dynamic Drag. Published by author, 1965. 25, 26, 42 [16] Sighard F. Hoerner and Henry V. Borst. Fluid Dynamic Lift. Published by author, second edition, 1985. 30, 31, 98 [17] P. C. Hughes. Spacecraft Attitude Dynamics. John Wiley and Sons, New York, 1986. 21 [18] D. E. Humphreys. Development of the equations of motion and transfer functions for underwater vehicles. Report NCSL 287-76, Naval Coastal Systems Laboratory, Panama City, FL, July 1976. [19] D. E. Humphreys. Dynamics and hydrodynamics of ocean vehicles. In Proceedings MTS/IEEE Oceans 2000, Providence, Rhode Island, September 2000. [20] E. V. Lewis, editor. Principles of Naval Architecture. Society of Naval Architects and Marine Engineers, Jersey City, New Jersey, second edition, 1988. 25 [21] Woei-Min Lin and Dick Y. P. K. Yue. Numerical solutions for large-amplitude ship motions in the time domain. In Proceedings Eighteenth Symposium on Naval Hydrodynamics, Ann Arbor, Michigan, 1990. 100 [22] D. F. Myring. A theoretical study of body drag in subcritical axisymmetric flow. Aeronautical Quarterly, 27(3):186-94, August 1976. 14, 15, 42 [23] Meyer Nahon. A simplified dynamics model for autonomous underwater vehicles. In Proceedings 1996 Symposium on Autonomous Underwater Vehicle Technology, pages 373-379, June 1996. 30, 98 [24] J. N. Newman. Marine Hydrodynamics. MIT Press, Massachusetts, 1977. 25, 27, 28 [25] Norman S. Nise. Control Systems Engineering. Benjamin/Cummings, San Francisco, CA, first edition, 1992. 87 [26] William D. Ramsey. Boundary Integral Methods for Lifting Bodies with Vortex Wakes. PhD dissertation, Massachusetts Institute of Technology, Department of Ocean Engineering, May 1996. 100 [27] Jeffery S. Riedel. Seaway Learning and Motion Compensation in Shallow Waters for Small A UVs. PhD dissertation, Naval Postgraduate School, Department of Ocean Engineering, June 1999. 100 [28] R. Stokey and T. Austin. Sequential long baseline navigation for REMUS, an autonomous underwater vehicle. In Proceedings Information Systems for Navy Divers and A UVs Operating in Very Shallow Water and Surf Zone Regions, April 1999. 36, 50 [29] Michael S. Triantafyllou. Maneuvering and control of surface and underwater vehicles. Lecture Notes for MIT Ocean Engineering Course 13.49, 1996. 25, 26 [30] C. von Alt, B. Allen, T. Austin, and R. Stokey. Remote environmental monitoring units. In Proceedings MTS/IEEE Oceans 1994, Cambridge, MA, 1994. 12, 36 [31] C. von Alt and J.F. Grassle. LEO-15: An unmanned long term environmental observatory. In Proceedings MTS/IEEE Oceans 1992, Newport, RI, 1992. 12, 36 [32] L. F. Whicker and L. F. Fehlner. Free-stream characteristics of a family of low-aspect ratio control surfaces. Technical Report 933, David Taylor Model Basin, 1958. NC. 26 [33] Christopher J. Willy. Attitude Control of an Underwater Vehicle Subjected to Waves. Ocean Engineer's thesis, Massachusetts Institute of Technology, Department of Ocean Engineering, May 1994. 100 126

---

## Page 252

[15] 希加德·F·赫尔纳。Fluid Dynamic Drag.  作者出版，1965年。25，26，42 [16] 西加德·F·赫尔纳和亨利·V·博斯特。Fluid Dynamic Lift.  作者出版，第二版，1985年。30, 31, 98 [17] P. C. Hughes. Spacecraft Attitude Dynamics.  约翰·威利与子公司，纽约，1986年。21 [18] D. E. Humphreys. 水下车辆运动方程和传递函数的发展。报告 NCSL 287-76，海军沿海系统实验室， 美国佛罗里达州巴拿马城，1976年7月。 [19] D. E. Humphreys。《海洋载具的动力学与流体动力学》。发表于Proceedings MTS/IEEE Oceans 2000,  罗德岛普罗维登斯，2000年9月。 [20] E. V. Lewis，编辑。《海军建筑师与船舶工程师学会》，新泽西州泽西城市，第2版，1988年，25 [21] 林维民, 余迪克 Y. P. K. 大振幅船舶运动的时间域数值解法. 于 Proceedings Eighteenth Symposium on Naval Hydrodynamics,  密歇根州安娜堡, 1990. 100 [22] D. F. Myring. 关于亚临界轴对称流动中物体阻力的理论研究。Aeronautical Quarterly, 27(3):186-94, 1976年8月. 14, 15, 42 [23] Meyer Nahon. 一种用于自主水下航行器的简化动力学模型. 收录于 Proceedings 1996 Symposium on Autonomous Underwater Vehicle Technology,  页 373-379, 1996年6月. 30, 98 [24]  J. N. Newman. Marine Hydrodynamics.  麻省理工学院出版社，马萨诸塞州，1977年。25, 27, 28 [25] Norman S. Nise. Control Systems Engineering.  Benjamin/Cummings, 旧金山，加利福尼亚州，第一 版，1992年。87 [26] 威廉·D·拉姆齐。Boundary Integral Methods for Lifting Bodies with Vortex Wakes.  博士论文， 麻省理工学院，海洋工程系，1996年5月。100 [27] 杰弗里·S·里德尔. Seaway Learning and Motion Compensation in Shallow Waters for Small A UVs.  博士论文，美国海军研究生院，海洋工程系，1999年6月. 100 [28] R. Stokey 和 T. Austin. 用于 REMUS（自主水下航行器）的连续长基线导航。发表于 Proceedings Information Systems for Navy Divers and A UVs Operating in Very Shallow Water and Surf Zone Regions,  1999 年 4 月。36, 50 [29]  Michael S. Triantafyllou. 水面和水下车辆的机动与控制。麻省理工学院海洋工程课程13.49讲义，1996 年。25, 26 [30] C. von Alt, B. Allen, T. Austin, 和 R. Stokey. 远程环境监测单元. 载于 Proceedings M TS/IE E E  Oceans 1994,  剑桥, MA, 1994. 12, 36 [31] C. von Alt 和 J.F. Grassle. LEO-15：一个无人长期环境观测站。在 Proceedings M TS/IE E E  Oceans 1992,  Newport, RI, 1992. 12, 36 [32] L. F. Whicker 和 L. F. Fehlner. 一系列低纵横比控制面的自由流特性. 技术报告 933, 大卫·泰勒模型盆, 1 958. NC. 26 [33]  克里斯托弗·J·威利。Attitude Control of an Underwater Vehicle Subjected to Waves.  《海洋工 程师论文》，麻省理工学院，海洋工程系，1994年5月。100 126

---

## Page 253

[34] Ming Xue. Three-dimensional fully non-linear simulation of waves and wave-body interactions. PhD dissertation, Massachusetts Institute of Technology, Department of Ocean Engineering, May 1997. 100 [35] D. R. Yoerger, J.G. Cooke, and J.-J. E. Slotine. The influence of thruster dynamics on un- derwater vehicle behavior and their incorporation into control system design. IEEE Journal of Oceanic Engineering, 15:167-178, July 1990. 33 127

---

## Page 254

[34] 明学. Three-dimensional fully non-linear simulation of waves and wave-body interactions. 博士 论文, 麻省理工学院, 海洋工程系, 1997年5月. 100 [35] D. R. Yoerger, J.G. Cooke, 和 J.-J. E. Slotine. 推进器动态对水下航行器行为的影响及其在控制系统设计中的应用. IEEE Journal of Oceanic Engineering, 15:167-178, 1990年7月. 33 127

---
