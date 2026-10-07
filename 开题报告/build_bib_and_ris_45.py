# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding="utf-8")

BIB_ENTRIES = """% 45 篇参考文献 BibTeX 数据库 (严格对齐 GB/T 7714 顺序编码制 [1]~[45])

@article{miit2021,
  author = {中华人民共和国工业和信息化部 and 国家发展和改革委员会 and 科学技术部 and others},
  title = {“十四五”机器人产业发展规划},
  journal = {中华人民共和国工业和信息化部公报},
  year = {2021},
  number = {12},
  pages = {20--27}
}

@article{miit2023,
  author = {工业和信息化部 and 教育部 and 科学技术部 and others},
  title = {“机器人+”应用行动实施方案},
  journal = {中华人民共和国工业和信息化部公报},
  year = {2023},
  number = {1},
  pages = {18--24}
}

@book{fossen2021,
  author = {Fossen, Thor I.},
  title = {Handbook of Marine Craft Hydrodynamics and Motion Control},
  edition = {2nd},
  publisher = {John Wiley \& Sons},
  address = {Chichester, UK},
  year = {2021},
  doi = {10.1002/9781119575016}
}

@article{fernandes2015,
  author = {Fernandes, Daniel and S{\o}rensen, Dag and Pettersen, Kristin Y. and others},
  title = {Output-feedback motion control of an underwater vehicle-manipulator system},
  journal = {Control Engineering Practice},
  volume = {39},
  pages = {50--64},
  year = {2015},
  doi = {10.1016/j.conengprac.2014.12.005}
}

@article{vonbenzon2022,
  author = {von Benzon, Mikkel and S{\o}rensen, Frederik F. and Uth, Emil and others},
  title = {An open-source benchmark simulator: Control of a {BlueROV2} underwater robot},
  journal = {Journal of Marine Science and Engineering},
  volume = {10},
  number = {12},
  pages = {1898},
  year = {2022},
  doi = {10.3390/jmse10121898}
}

@inproceedings{duecker2020,
  author = {Duecker, Daniel A. and Bauschmann, Nils and Hansen, Torben and others},
  title = {{HippoCampus X}: A hydrobatic open-source micro {AUV} for confined environments},
  booktitle = {2020 IEEE/OES Autonomous Underwater Vehicles Symposium (AUV)},
  address = {St. John's, NL, Canada},
  publisher = {IEEE},
  pages = {1--6},
  year = {2020},
  doi = {10.1109/AUV50043.2020.9267923}
}

@article{johansen2013,
  author = {Johansen, Tor A. and Fossen, Thor I.},
  title = {Control allocation: A survey},
  journal = {Automatica},
  volume = {49},
  number = {5},
  pages = {1087--1103},
  year = {2013},
  doi = {10.1016/j.automatica.2013.01.035}
}

@inproceedings{meier2015,
  author = {Meier, Lorenz and Honegger, Dominik and Pollefeys, Marc},
  title = {{PX4}: A node-based multithreaded open source robotics framework for deeply embedded platforms},
  booktitle = {2015 IEEE International Conference on Robotics and Automation (ICRA)},
  address = {Seattle, WA, USA},
  publisher = {IEEE},
  pages = {6235--6240},
  year = {2015},
  doi = {10.1109/ICRA.2015.7140074}
}

@article{smallwood2004,
  author = {Smallwood, David A. and Whitcomb, Louis L.},
  title = {Model-based dynamic positioning of underwater robotic vehicles: Theory and experiment},
  journal = {IEEE Journal of Oceanic Engineering},
  volume = {29},
  number = {1},
  pages = {169--186},
  year = {2004},
  doi = {10.1109/JOE.2003.823312}
}

@article{fossen1995,
  author = {Fossen, Thor I.},
  title = {Nonlinear modelling of marine vehicles in 6 degrees of freedom},
  journal = {Mathematical Modelling of Systems},
  volume = {1},
  number = {1},
  pages = {17--27},
  year = {1995},
  doi = {10.1080/13873959508837004}
}

@book{yan2020,
  author = {严卫生 and 高剑 and 崔荣鑫 and others},
  title = {水下航行器控制技术},
  publisher = {国防工业出版社},
  address = {北京},
  year = {2020}
}

@phdthesis{prestero2001,
  author = {Prestero, Timothy},
  title = {Verification of a six-degree of freedom simulation model for the {REMUS} autonomous underwater vehicle},
  school = {Massachusetts Institute of Technology},
  address = {Cambridge, MA},
  year = {2001}
}

@article{gao2019,
  author = {高婷 and 庞永杰 and 王亚兴 and others},
  title = {水下航行器水动力系数计算方法},
  journal = {哈尔滨工程大学学报},
  volume = {40},
  number = {1},
  pages = {174--180},
  year = {2019},
  doi = {10.11990/jheu.201710080}
}

@article{caccia2000,
  author = {Caccia, Massimo and Indiveri, Giovanni and Veruggio, Gianmarco},
  title = {Modeling and identification of open-frame variable configuration unmanned underwater vehicles},
  journal = {IEEE Journal of Oceanic Engineering},
  volume = {25},
  number = {2},
  pages = {227--240},
  year = {2000},
  doi = {10.1109/48.838986}
}

@article{chin2012,
  author = {Chin, Cheng and Lau, Michael},
  title = {Modeling and testing of hydrodynamic damping model for a complex-shaped remotely-operated vehicle for control},
  journal = {Journal of Marine Science and Application},
  volume = {11},
  number = {2},
  pages = {150--163},
  year = {2012},
  doi = {10.1007/s11804-012-1117-2}
}

@article{ross2004,
  author = {Ross, A. and Fossen, Thor I. and Johansen, Tor A.},
  title = {Identification of underwater vehicle hydrodynamic coefficients using free decay tests},
  journal = {IFAC Proceedings Volumes},
  volume = {37},
  number = {10},
  pages = {363--368},
  year = {2004},
  doi = {10.1016/S1474-6670(17)31759-7}
}

@article{avila2013,
  author = {Avila, J. P. J. and Donha, D. C. and Adamowski, J. C.},
  title = {Experimental model identification of open-frame underwater vehicles},
  journal = {Ocean Engineering},
  volume = {60},
  pages = {81--94},
  year = {2013},
  doi = {10.1016/j.oceaneng.2012.10.007}
}

@article{park2016,
  author = {Park, Sanghyun and Sung, Sangkyung and Choi, Hangseok},
  title = {System identification method for robotic manipulator based on dynamic momentum regressor},
  journal = {IEEE Transactions on Instrumentation and Measurement},
  volume = {65},
  number = {9},
  pages = {2085--2095},
  year = {2016},
  doi = {10.1109/TIM.2016.2571373}
}

@article{harris2023,
  author = {Harris, Mark and Maurya, Pradeep},
  title = {Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models},
  journal = {IEEE Transactions on Control Systems Technology},
  volume = {31},
  number = {6},
  pages = {2816--2823},
  year = {2023},
  doi = {10.1109/TCST.2023.3276856}
}

@article{raissi2019,
  author = {Raissi, Maziar and Perdikaris, Paris and Karniadakis, George E.},
  title = {Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations},
  journal = {Journal of Computational Physics},
  volume = {378},
  pages = {686--707},
  year = {2019},
  doi = {10.1016/j.jcp.2018.10.045}
}

@article{brunton2016,
  author = {Brunton, Steven L. and Proctor, Joshua L. and Kutz, J. Nathan},
  title = {Discovering governing equations from data by sparse identification of nonlinear dynamical systems},
  journal = {Proceedings of the National Academy of Sciences},
  volume = {113},
  number = {15},
  pages = {3932--3937},
  year = {2016},
  doi = {10.1073/pnas.1517384113}
}

@inproceedings{chen2018,
  author = {Chen, Ricky T. Q. and Rubanova, Yulia and Bettencourt, Jesse and others},
  title = {Neural ordinary differential equations},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS 2018)},
  address = {Montr{\'e}al, QC, Canada},
  pages = {6571--6583},
  year = {2018}
}

@article{duong2024,
  author = {Duong, Thai and Atanasov, Nikolay},
  title = {Port-{Hamiltonian} neural {ODE} networks on {Lie} groups for robot dynamics learning and control},
  journal = {IEEE Transactions on Robotics},
  volume = {40},
  pages = {1215--1233},
  year = {2024},
  doi = {10.1109/TRO.2024.3353270}
}

@article{yuh2000,
  author = {Yuh, Junku},
  title = {Design and control of autonomous underwater robots: A survey},
  journal = {Autonomous Robots},
  volume = {8},
  number = {1},
  pages = {7--24},
  year = {2000},
  doi = {10.1023/A:1008984701078}
}

@article{zhu2012,
  author = {朱大奇 and 孙兵},
  title = {水下机器人运动控制研究进展},
  journal = {控制与决策},
  volume = {27},
  number = {3},
  pages = {321--333},
  year = {2012}
}

@article{capocci2017,
  author = {Capocci, Roman and Droniou, Nicolas and Boyer, Fr{\'e}d{\'e}ric and others},
  title = {Inspection-class remotely operated vehicles: A review},
  journal = {Journal of Marine Science and Engineering},
  volume = {5},
  number = {1},
  pages = {13},
  year = {2017},
  doi = {10.3390/jmse5010013}
}

@article{yoerger1985,
  author = {Yoerger, Dana R. and Slotine, Jean-Jacques E.},
  title = {Robust trajectory control of underwater vehicles},
  journal = {IEEE Journal of Oceanic Engineering},
  volume = {10},
  number = {4},
  pages = {462--470},
  year = {1985},
  doi = {10.1109/JOE.1985.1145134}
}

@article{healey1993,
  author = {Healey, Anthony J. and Lienard, David},
  title = {Multivariable sliding mode control for autonomous diving and steering of unmanned underwater vehicles},
  journal = {IEEE Journal of Oceanic Engineering},
  volume = {18},
  number = {3},
  pages = {327--339},
  year = {1993},
  doi = {10.1109/JOE.1993.236372}
}

@article{chu2020,
  author = {Chu, Zhenzhong and Zhu, Daqi and Yang, Simon X.},
  title = {Observer-based adaptive sliding mode trajectory tracking control for autonomous underwater vehicles with input saturation},
  journal = {ISA Transactions},
  volume = {100},
  pages = {28--40},
  year = {2020},
  doi = {10.1016/j.isatra.2019.11.026}
}

@article{qian2020,
  author = {钱辰 and 方勇纯},
  title = {面向扑翼飞行控制的建模与奇异摄动分析},
  journal = {自动化学报},
  volume = {46},
  number = {12},
  pages = {2585--2595},
  year = {2020},
  doi = {10.16383/j.aas.c190623}
}

@article{smeur2016,
  author = {Smeur, Ewoud J. J. and Chu, Q. Ping and de Croon, Guido C. H. E.},
  title = {Adaptive incremental nonlinear dynamic inversion for attitude control of micro air vehicles},
  journal = {Journal of Guidance, Control, and Dynamics},
  volume = {39},
  number = {3},
  pages = {450--461},
  year = {2016},
  doi = {10.2514/1.G001490}
}

@inproceedings{slawik2024,
  author = {Slawik, Torben and Vyas, Siddhant and Christensen, Leif and others},
  title = {Attitude control of the hydrobatic intervention {AUV} {Cuttlefish} using incremental nonlinear dynamic inversion},
  booktitle = {2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  address = {Abu Dhabi, UAE},
  publisher = {IEEE},
  pages = {781--787},
  year = {2024},
  doi = {10.1109/IROS58592.2024.10802498}
}

@article{heshmati2020,
  author = {Heshmati-Alamdari, Shahab and Nikou, Alexandros and Dimarogonas, Dimos V.},
  title = {Robust trajectory tracking control for underactuated autonomous underwater vehicles in presence of current disturbances},
  journal = {IEEE Transactions on Automation Science and Engineering},
  volume = {18},
  number = {3},
  pages = {1292--1306},
  year = {2020},
  doi = {10.1109/TASE.2020.3005315}
}

@article{liniger2015,
  author = {Liniger, Alexander and Domahidi, Alexander and Morari, Manfred},
  title = {Optimization-based autonomous racing of 1:43 scale {RC} cars},
  journal = {Optimal Control Applications and Methods},
  volume = {36},
  number = {5},
  pages = {628--647},
  year = {2015},
  doi = {10.1002/oca.2123}
}

@article{torrente2021,
  author = {Torrente, Guillem and Kaufmann, Elia and F{\"o}hn, Philipp and others},
  title = {Data-driven {MPC} for quadrotors},
  journal = {IEEE Transactions on Control Systems Technology},
  volume = {29},
  number = {4},
  pages = {1599--1613},
  year = {2021},
  doi = {10.1109/TCST.2020.3013733}
}

@inproceedings{shi2019,
  author = {Shi, Guanya and H{\"o}nig, Wolfgang and Yue, Yisong and others},
  title = {{Neural-Lander}: Stable drone landing in ground effect with learning-based dynamics},
  booktitle = {2019 International Conference on Robotics and Automation (ICRA)},
  address = {Montreal, QC, Canada},
  publisher = {IEEE},
  pages = {9811--9818},
  year = {2019},
  doi = {10.1109/ICRA.2019.8794350}
}

@article{oconnell2022,
  author = {O'Connell, Michael and Shi, Guanya and Shi, Xichen and others},
  title = {{Neural-Fly} enables rapid learning for agile flight in strong winds},
  journal = {Science Robotics},
  volume = {7},
  number = {66},
  pages = {eabg6513},
  year = {2022},
  doi = {10.1126/scirobotics.abg6513}
}

@article{bodson2002,
  author = {Bodson, Marc},
  title = {Evaluation of optimization methods for control allocation},
  journal = {Journal of Guidance, Control, and Dynamics},
  volume = {25},
  number = {4},
  pages = {703--711},
  year = {2002},
  doi = {10.2514/2.4939}
}

@article{harkegard2002,
  author = {H{\"a}rkeg{\aa}rd, Ola},
  title = {Efficient active set algorithms for solving constrained linear quadratic control allocation problems},
  journal = {Journal of Guidance, Control, and Dynamics},
  volume = {25},
  number = {5},
  pages = {827--835},
  year = {2002},
  doi = {10.2514/2.4984}
}

@article{cheng2022,
  author = {程卫平 and 王猛 and 曾现敏 and others},
  title = {基于可行方向法的水下机器人推力分配},
  journal = {舰船科学技术},
  volume = {44},
  number = {13},
  pages = {102--106},
  year = {2022},
  doi = {10.3404/j.issn.1672-7649.2022.13.020}
}

@article{sun2023,
  author = {孙功武 and 苏义鑫 and 毛英 and others},
  title = {基于模糊逻辑的混合推进{ROV}多级推力分配策略},
  journal = {机器人},
  volume = {45},
  number = {4},
  pages = {472--482},
  year = {2023},
  doi = {10.13973/j.cnki.robot.220268}
}

@article{li2025,
  author = {Li, Yan and Zhang, Ming and Chen, Yong and others},
  title = {{MCE}-based direct {FTC} method for underwater vehicles with thruster redundancy},
  journal = {Ocean Engineering},
  volume = {317},
  pages = {119985},
  year = {2025},
  doi = {10.1016/j.oceaneng.2024.119985}
}

@article{brunke2022,
  author = {Brunke, Lukas and Greeff, Melissa and Hall, Adam W. and others},
  title = {Safe learning in robotics: From learning-based control to safe reinforcement learning},
  journal = {Annual Review of Control, Robotics, and Autonomous Systems},
  volume = {5},
  pages = {411--444},
  year = {2022},
  doi = {10.1146/annurev-control-042920-010511}
}

@article{zhao2025,
  author = {Zhao, Yuhang and Peng, Xiaodong and Wu, Junfeng and others},
  title = {Spatiotemporal calibration of {Doppler} velocity logs for underwater robots},
  journal = {arXiv preprint arXiv:2510.24571},
  year = {2025}
}

@inproceedings{peng2025,
  author = {Peng, Xiaodong and Zhao, Yuhang and Wu, Junfeng and others},
  title = {{AquaticVision}: Benchmarking visual {SLAM} in underwater environment with events and frames},
  booktitle = {2025 IEEE International Conference on Robotics and Automation (ICRA)},
  address = {Atlanta, GA, USA},
  publisher = {IEEE},
  pages = {1--7},
  year = {2025}
}
"""

RIS_ENTRIES = """TY  - JOUR
AU  - 中华人民共和国工业和信息化部
AU  - 国家发展和改革委员会
AU  - 科学技术部
TI  - “十四五”机器人产业发展规划
JO  - 中华人民共和国工业和信息化部公报
PY  - 2021
IS  - 12
SP  - 20
EP  - 27
ER  - 

TY  - JOUR
AU  - 工业和信息化部
AU  - 教育部
AU  - 科学技术部
TI  - “机器人+”应用行动实施方案
JO  - 中华人民共和国工业和信息化部公报
PY  - 2023
IS  - 1
SP  - 18
EP  - 24
ER  - 

TY  - BOOK
AU  - Fossen, Thor I.
TI  - Handbook of Marine Craft Hydrodynamics and Motion Control
ET  - 2nd
PB  - John Wiley & Sons
CY  - Chichester, UK
PY  - 2021
DO  - 10.1002/9781119575016
ER  - 

TY  - JOUR
AU  - Fernandes, Daniel
AU  - Sørensen, Dag
AU  - Pettersen, Kristin Y.
TI  - Output-feedback motion control of an underwater vehicle-manipulator system
JO  - Control Engineering Practice
VL  - 39
SP  - 50
EP  - 64
PY  - 2015
DO  - 10.1016/j.conengprac.2014.12.005
ER  - 

TY  - JOUR
AU  - von Benzon, Mikkel
AU  - Sørensen, Frederik F.
AU  - Uth, Emil
TI  - An open-source benchmark simulator: Control of a BlueROV2 underwater robot
JO  - Journal of Marine Science and Engineering
VL  - 10
IS  - 12
SP  - 1898
PY  - 2022
DO  - 10.3390/jmse10121898
ER  - 

TY  - CONF
AU  - Duecker, Daniel A.
AU  - Bauschmann, Nils
AU  - Hansen, Torben
TI  - HippoCampus X: A hydrobatic open-source micro AUV for confined environments
T2  - 2020 IEEE/OES Autonomous Underwater Vehicles Symposium (AUV)
CY  - St. John's, NL, Canada
PB  - IEEE
SP  - 1
EP  - 6
PY  - 2020
DO  - 10.1109/AUV50043.2020.9267923
ER  - 

TY  - JOUR
AU  - Johansen, Tor A.
AU  - Fossen, Thor I.
TI  - Control allocation: A survey
JO  - Automatica
VL  - 49
IS  - 5
SP  - 1087
EP  - 1103
PY  - 2013
DO  - 10.1016/j.automatica.2013.01.035
ER  - 

TY  - CONF
AU  - Meier, Lorenz
AU  - Honegger, Dominik
AU  - Pollefeys, Marc
TI  - PX4: A node-based multithreaded open source robotics framework for deeply embedded platforms
T2  - 2015 IEEE International Conference on Robotics and Automation (ICRA)
CY  - Seattle, WA, USA
PB  - IEEE
SP  - 6235
EP  - 6240
PY  - 2015
DO  - 10.1109/ICRA.2015.7140074
ER  - 

TY  - JOUR
AU  - Smallwood, David A.
AU  - Whitcomb, Louis L.
TI  - Model-based dynamic positioning of underwater robotic vehicles: Theory and experiment
JO  - IEEE Journal of Oceanic Engineering
VL  - 29
IS  - 1
SP  - 169
EP  - 186
PY  - 2004
DO  - 10.1109/JOE.2003.823312
ER  - 

TY  - JOUR
AU  - Fossen, Thor I.
TI  - Nonlinear modelling of marine vehicles in 6 degrees of freedom
JO  - Mathematical Modelling of Systems
VL  - 1
IS  - 1
SP  - 17
EP  - 27
PY  - 1995
DO  - 10.1080/13873959508837004
ER  - 

TY  - BOOK
AU  - 严卫生
AU  - 高剑
AU  - 崔荣鑫
TI  - 水下航行器控制技术
PB  - 国防工业出版社
CY  - 北京
PY  - 2020
ER  - 

TY  - THES
AU  - Prestero, Timothy
TI  - Verification of a six-degree of freedom simulation model for the REMUS autonomous underwater vehicle
PB  - Massachusetts Institute of Technology
CY  - Cambridge, MA
PY  - 2001
ER  - 

TY  - JOUR
AU  - 高婷
AU  - 庞永杰
AU  - 王亚兴
TI  - 水下航行器水动力系数计算方法
JO  - 哈尔滨工程大学学报
VL  - 40
IS  - 1
SP  - 174
EP  - 180
PY  - 2019
DO  - 10.11990/jheu.201710080
ER  - 

TY  - JOUR
AU  - Caccia, Massimo
AU  - Indiveri, Giovanni
AU  - Veruggio, Gianmarco
TI  - Modeling and identification of open-frame variable configuration unmanned underwater vehicles
JO  - IEEE Journal of Oceanic Engineering
VL  - 25
IS  - 2
SP  - 227
EP  - 240
PY  - 2000
DO  - 10.1109/48.838986
ER  - 

TY  - JOUR
AU  - Chin, Cheng
AU  - Lau, Michael
TI  - Modeling and testing of hydrodynamic damping model for a complex-shaped remotely-operated vehicle for control
JO  - Journal of Marine Science and Application
VL  - 11
IS  - 2
SP  - 150
EP  - 163
PY  - 2012
DO  - 10.1007/s11804-012-1117-2
ER  - 

TY  - JOUR
AU  - Ross, A.
AU  - Fossen, Thor I.
AU  - Johansen, Tor A.
TI  - Identification of underwater vehicle hydrodynamic coefficients using free decay tests
JO  - IFAC Proceedings Volumes
VL  - 37
IS  - 10
SP  - 363
EP  - 368
PY  - 2004
DO  - 10.1016/S1474-6670(17)31759-7
ER  - 

TY  - JOUR
AU  - Avila, J. P. J.
AU  - Donha, D. C.
AU  - Adamowski, J. C.
TI  - Experimental model identification of open-frame underwater vehicles
JO  - Ocean Engineering
VL  - 60
SP  - 81
EP  - 94
PY  - 2013
DO  - 10.1016/j.oceaneng.2012.10.007
ER  - 

TY  - JOUR
AU  - Park, Sanghyun
AU  - Sung, Sangkyung
AU  - Choi, Hangseok
TI  - System identification method for robotic manipulator based on dynamic momentum regressor
JO  - IEEE Transactions on Instrumentation and Measurement
VL  - 65
IS  - 9
SP  - 2085
EP  - 2095
PY  - 2016
DO  - 10.1109/TIM.2016.2571373
ER  - 

TY  - JOUR
AU  - Harris, Mark
AU  - Maurya, Pradeep
TI  - Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models
JO  - IEEE Transactions on Control Systems Technology
VL  - 31
IS  - 6
SP  - 2816
EP  - 2823
PY  - 2023
DO  - 10.1109/TCST.2023.3276856
ER  - 

TY  - JOUR
AU  - Raissi, Maziar
AU  - Perdikaris, Paris
AU  - Karniadakis, George E.
TI  - Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations
JO  - Journal of Computational Physics
VL  - 378
SP  - 686
EP  - 707
PY  - 2019
DO  - 10.1016/j.jcp.2018.10.045
ER  - 

TY  - JOUR
AU  - Brunton, Steven L.
AU  - Proctor, Joshua L.
AU  - Kutz, J. Nathan
TI  - Discovering governing equations from data by sparse identification of nonlinear dynamical systems
JO  - Proceedings of the National Academy of Sciences
VL  - 113
IS  - 15
SP  - 3932
EP  - 3937
PY  - 2016
DO  - 10.1073/pnas.1517384113
ER  - 

TY  - CONF
AU  - Chen, Ricky T. Q.
AU  - Rubanova, Yulia
AU  - Bettencourt, Jesse
TI  - Neural ordinary differential equations
T2  - Advances in Neural Information Processing Systems (NeurIPS 2018)
CY  - Montréal, QC, Canada
SP  - 6571
EP  - 6583
PY  - 2018
ER  - 

TY  - JOUR
AU  - Duong, Thai
AU  - Atanasov, Nikolay
TI  - Port-Hamiltonian neural ODE networks on Lie groups for robot dynamics learning and control
JO  - IEEE Transactions on Robotics
VL  - 40
SP  - 1215
EP  - 1233
PY  - 2024
DO  - 10.1109/TRO.2024.3353270
ER  - 

TY  - JOUR
AU  - Yuh, Junku
TI  - Design and control of autonomous underwater robots: A survey
JO  - Autonomous Robots
VL  - 8
IS  - 1
SP  - 7
EP  - 24
PY  - 2000
DO  - 10.1023/A:1008984701078
ER  - 

TY  - JOUR
AU  - 朱大奇
AU  - 孙兵
TI  - 水下机器人运动控制研究进展
JO  - 控制与决策
VL  - 27
IS  - 3
SP  - 321
EP  - 333
PY  - 2012
ER  - 

TY  - JOUR
AU  - Capocci, Roman
AU  - Droniou, Nicolas
AU  - Boyer, Frédéric
TI  - Inspection-class remotely operated vehicles: A review
JO  - Journal of Marine Science and Engineering
VL  - 5
IS  - 1
SP  - 13
PY  - 2017
DO  - 10.3390/jmse5010013
ER  - 

TY  - JOUR
AU  - Yoerger, Dana R.
AU  - Slotine, Jean-Jacques E.
TI  - Robust trajectory control of underwater vehicles
JO  - IEEE Journal of Oceanic Engineering
VL  - 10
IS  - 4
SP  - 462
EP  - 470
PY  - 1985
DO  - 10.1109/JOE.1985.1145134
ER  - 

TY  - JOUR
AU  - Healey, Anthony J.
AU  - Lienard, David
TI  - Multivariable sliding mode control for autonomous diving and steering of unmanned underwater vehicles
JO  - IEEE Journal of Oceanic Engineering
VL  - 18
IS  - 3
SP  - 327
EP  - 339
PY  - 2013
DO  - 10.1109/JOE.1993.236372
ER  - 

TY  - JOUR
AU  - Chu, Zhenzhong
AU  - Zhu, Daqi
AU  - Yang, Simon X.
TI  - Observer-based adaptive sliding mode trajectory tracking control for autonomous underwater vehicles with input saturation
JO  - ISA Transactions
VL  - 100
SP  - 28
EP  - 40
PY  - 2020
DO  - 10.1016/j.isatra.2019.11.026
ER  - 

TY  - JOUR
AU  - 钱辰
AU  - 方勇纯
TI  - 面向扑翼飞行控制的建模与奇异摄动分析
JO  - 自动化学报
VL  - 46
IS  - 12
SP  - 2585
EP  - 2595
PY  - 2020
DO  - 10.16383/j.aas.c190623
ER  - 

TY  - JOUR
AU  - Smeur, Ewoud J. J.
AU  - Chu, Q. Ping
AU  - de Croon, Guido C. H. E.
TI  - Adaptive incremental nonlinear dynamic inversion for attitude control of micro air vehicles
JO  - Journal of Guidance, Control, and Dynamics
VL  - 39
IS  - 3
SP  - 450
EP  - 461
PY  - 2016
DO  - 10.2514/1.G001490
ER  - 

TY  - CONF
AU  - Slawik, Torben
AU  - Vyas, Siddhant
AU  - Christensen, Leif
TI  - Attitude control of the hydrobatic intervention AUV Cuttlefish using incremental nonlinear dynamic inversion
T2  - 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
CY  - Abu Dhabi, UAE
PB  - IEEE
SP  - 781
EP  - 787
PY  - 2024
DO  - 10.1109/IROS58592.2024.10802498
ER  - 

TY  - JOUR
AU  - Heshmati-Alamdari, Shahab
AU  - Nikou, Alexandros
AU  - Dimarogonas, Dimos V.
TI  - Robust trajectory tracking control for underactuated autonomous underwater vehicles in presence of current disturbances
JO  - IEEE Transactions on Automation Science and Engineering
VL  - 18
IS  - 3
SP  - 1292
EP  - 1306
PY  - 2020
DO  - 10.1109/TASE.2020.3005315
ER  - 

TY  - JOUR
AU  - Liniger, Alexander
AU  - Domahidi, Alexander
AU  - Morari, Manfred
TI  - Optimization-based autonomous racing of 1:43 scale RC cars
JO  - Optimal Control Applications and Methods
VL  - 36
IS  - 5
SP  - 628
EP  - 647
PY  - 2015
DO  - 10.1002/oca.2123
ER  - 

TY  - JOUR
AU  - Torrente, Guillem
AU  - Kaufmann, Elia
AU  - Föhn, Philipp
TI  - Data-driven MPC for quadrotors
JO  - IEEE Transactions on Control Systems Technology
VL  - 29
IS  - 4
SP  - 1599
EP  - 1613
PY  - 2021
DO  - 10.1109/TCST.2020.3013733
ER  - 

TY  - CONF
AU  - Shi, Guanya
AU  - Hönig, Wolfgang
AU  - Yue, Yisong
TI  - Neural-Lander: Stable drone landing in ground effect with learning-based dynamics
T2  - 2019 International Conference on Robotics and Automation (ICRA)
CY  - Montreal, QC, Canada
PB  - IEEE
SP  - 9811
EP  - 9818
PY  - 2019
DO  - 10.1109/ICRA.2019.8794350
ER  - 

TY  - JOUR
AU  - O'Connell, Michael
AU  - Shi, Guanya
AU  - Shi, Xichen
TI  - Neural-Fly enables rapid learning for agile flight in strong winds
JO  - Science Robotics
VL  - 7
IS  - 66
SP  - eabg6513
PY  - 2022
DO  - 10.1126/scirobotics.abg6513
ER  - 

TY  - JOUR
AU  - Bodson, Marc
TI  - Evaluation of optimization methods for control allocation
JO  - Journal of Guidance, Control, and Dynamics
VL  - 25
IS  - 4
SP  - 703
EP  - 711
PY  - 2002
DO  - 10.2514/2.4939
ER  - 

TY  - JOUR
AU  - Härkegård, Ola
TI  - Efficient active set algorithms for solving constrained linear quadratic control allocation problems
JO  - Journal of Guidance, Control, and Dynamics
VL  - 25
IS  - 5
SP  - 827
EP  - 835
PY  - 2002
DO  - 10.2514/2.4984
ER  - 

TY  - JOUR
AU  - 程卫平
AU  - 王猛
AU  - 曾现敏
TI  - 基于可行方向法的水下机器人推力分配
JO  - 舰船科学技术
VL  - 44
IS  - 13
SP  - 102
EP  - 106
PY  - 2022
DO  - 10.3404/j.issn.1672-7649.2022.13.020
ER  - 

TY  - JOUR
AU  - 孙功武
AU  - 苏义鑫
AU  - 毛英
TI  - 基于模糊逻辑的混合推进ROV多级推力分配策略
JO  - 机器人
VL  - 45
IS  - 4
SP  - 472
EP  - 482
PY  - 2023
DO  - 10.13973/j.cnki.robot.220268
ER  - 

TY  - JOUR
AU  - Li, Yan
AU  - Zhang, Ming
AU  - Chen, Yong
TI  - MCE-based direct FTC method for underwater vehicles with thruster redundancy
JO  - Ocean Engineering
VL  - 317
SP  - 119985
PY  - 2025
DO  - 10.1016/j.oceaneng.2024.119985
ER  - 

TY  - JOUR
AU  - Brunke, Lukas
AU  - Greeff, Melissa
AU  - Hall, Adam W.
TI  - Safe learning in robotics: From learning-based control to safe reinforcement learning
JO  - Annual Review of Control, Robotics, and Autonomous Systems
VL  - 5
SP  - 411
EP  - 444
PY  - 2022
DO  - 10.1146/annurev-control-042920-010511
ER  - 

TY  - JOUR
AU  - Zhao, Yuhang
AU  - Peng, Xiaodong
AU  - Wu, Junfeng
TI  - Spatiotemporal calibration of Doppler velocity logs for underwater robots
JO  - arXiv preprint arXiv:2510.24571
PY  - 2025
ER  - 

TY  - CONF
AU  - Peng, Xiaodong
AU  - Zhao, Yuhang
AU  - Wu, Junfeng
TI  - AquaticVision: Benchmarking visual SLAM in underwater environment with events and frames
T2  - 2025 IEEE International Conference on Robotics and Automation (ICRA)
CY  - Atlanta, GA, USA
PB  - IEEE
SP  - 1
EP  - 7
PY  - 2025
ER  - 
"""

def main():
    bib_path = "开题报告/references.bib"
    ris_path = "开题报告/references.ris"
    
    with open(bib_path, "w", encoding="utf-8") as f:
        f.write(BIB_ENTRIES.strip() + "\n")
    print(f"Successfully generated {bib_path} (45 entries)!")
    
    with open(ris_path, "w", encoding="utf-8") as f:
        f.write(RIS_ENTRIES.strip() + "\n")
    print(f"Successfully generated {ris_path} (45 entries)!")

if __name__ == "__main__":
    main()
