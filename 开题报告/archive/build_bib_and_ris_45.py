# -*- coding: utf-8 -*-
"""
生成 45 篇参考文献对应的 BibTeX (references.bib) 与 RIS (references.ris)
严格与《开题报告_正文起草稿.md》中 [1]~[45] 一一对应
"""
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")

BIB_PATH = r"开题报告/references.bib"
RIS_PATH = r"开题报告/references.ris"
BUILD_SCRIPT_PATH = r"开题报告/build_bib_and_ris_45.py"

BIB_CONTENT = """% 45 篇参考文献 BibTeX 数据库 (严格对齐 GB/T 7714 顺序编码制 [1]~[45])

@article{miit2021,
  author = {工业和信息化部 and 国家发展和改革委员会 and 科学技术部 and others},
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
  publisher = {John Wiley \\& Sons},
  address = {Chichester, UK},
  year = {2021},
  doi = {10.1002/9781119575016}
}

@online{px4_uuv,
  author = {{PX4 Development Team}},
  title = {Submarines (Unmanned Underwater Vehicles---UUV)},
  year = {2024},
  url = {https://docs.px4.io/main/en/frames_sub/index},
  urldate = {2026-10-10}
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

@inproceedings{chin2012,
  author = {Chin, Cheng S. and Lau, Michael W. S.},
  title = {Modeling and testing of hydrodynamic damping for a complex-shaped underwater robot operating at low speed},
  booktitle = {2012 Oceans - Yeosu},
  address = {Yeosu, Korea},
  publisher = {IEEE},
  pages = {1--7},
  year = {2012},
  doi = {10.1109/OCEANS-Yeosu.2012.6263445}
}

@inproceedings{ross2004,
  author = {Ross, A. and Fossen, Thor I. and Johansen, Tor A.},
  title = {Identification of underwater vehicle hydrodynamic coefficients using free decay tests},
  booktitle = {IFAC Conference on Control Applications in Marine Systems},
  address = {Ancona, Italy},
  publisher = {IFAC},
  pages = {363--368},
  year = {2004}
}

@inproceedings{avila2013,
  author = {Avila, J. P. J. and Adamowski, J. C.},
  title = {Experimental model identification of open-frame unmanned underwater vehicles},
  booktitle = {2013 Oceans - San Diego},
  address = {San Diego, CA, USA},
  publisher = {IEEE},
  pages = {1--7},
  year = {2013},
  doi = {10.23919/OCEANS.2013.6741162}
}

@article{park2016,
  author = {Park, Sanghyun and Sung, Sangkyung and Choi, H. Jin},
  title = {System identification method for robotic manipulator based on dynamic momentum regressor},
  journal = {IEEE Transactions on Instrumentation and Measurement},
  volume = {65},
  number = {9},
  pages = {2085--2095},
  year = {2016},
  doi = {10.1109/TIM.2016.2570386}
}

@article{harris2023,
  author = {Harris, Zachary J. and Mao, Annie M. and Paine, Tyler M. and Whitcomb, Louis L.},
  title = {Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models for underactuated vehicles: Theory and experimental evaluation},
  journal = {The International Journal of Robotics Research},
  volume = {42},
  number = {12},
  pages = {1070--1093},
  year = {2023},
  doi = {10.1177/02783649231191184}
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

@article{raissi2019,
  author = {Raissi, Maziar and Perdikaris, Paris and Karniadakis, George E.},
  title = {Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations},
  journal = {Journal of Computational Physics},
  volume = {378},
  pages = {686--707},
  year = {2019},
  doi = {10.1016/j.jcp.2018.10.045}
}

@inproceedings{chen2018,
  author = {Chen, Ricky T. Q. and Rubanova, Yulia and Bettencourt, Jesse and Duvenaud, David},
  title = {Neural ordinary differential equations},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS 2018)},
  address = {Montréal, QC, Canada},
  pages = {6571--6583},
  year = {2018}
}

@article{liu2026,
  author = {Liu, Ang and Zhang, Xianrui and Xiao, Fengqi and Cui, Guangming and Mao, Baijin and Yang, Yunjie and Qu, Juntian},
  title = {Koopman-based online identification with {Sim2Real} transfer for hydrodynamic modeling of turtle-inspired robot},
  journal = {IEEE Robotics and Automation Letters},
  volume = {11},
  number = {6},
  pages = {6632--6639},
  year = {2026},
  doi = {10.1109/LRA.2026.3682620}
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

@article{fernandes2015,
  author = {Fernandes, Daniel and S{\o}rensen, Dag and Pettersen, Kristin Y. and others},
  title = {Output-feedback motion control of an underwater vehicle-manipulator system},
  journal = {Control Engineering Practice},
  volume = {39},
  pages = {50--64},
  year = {2015},
  doi = {10.1016/j.conengprac.2014.12.005}
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
  author = {Chu, Zhenzhong and Xiang, Xianbo and Zhu, Dacheng and others},
  title = {Adaptive trajectory tracking control for remotely operated vehicles considering thruster dynamics and saturation constraints},
  journal = {ISA Transactions},
  volume = {100},
  pages = {28--37},
  year = {2020},
  doi = {10.1016/j.isatra.2019.11.032}
}

@article{qian2020,
  author = {钱辰 and 方勇纯},
  title = {面向扑翼飞行控制的建模与奇异摄动分析},
  journal = {自动化学报},
  volume = {46},
  number = {12},
  pages = {2585--2595},
  year = {2020},
  doi = {10.16383/j.aas.c190807}
}

@article{smeur2016,
  author = {Smeur, Ewoud J. J. and Chu, Q. P. and de Croon, G. C. H. E.},
  title = {Adaptive incremental nonlinear dynamic inversion for attitude control of micro air vehicles},
  journal = {Journal of Guidance, Control, and Dynamics},
  volume = {39},
  number = {3},
  pages = {450--461},
  year = {2016},
  doi = {10.2514/1.G001490}
}

@inproceedings{slawik2024,
  author = {Slawik, Torben and Vyas, S. and Christensen, L. and others},
  title = {Attitude control of the hydrobatic intervention {AUV Cuttlefish} using incremental nonlinear dynamic inversion},
  booktitle = {2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  address = {Abu Dhabi, UAE},
  publisher = {IEEE},
  pages = {781--787},
  year = {2024},
  doi = {10.1109/IROS58592.2024.10802082}
}

@article{zhang2018,
  author = {张磊 and 严卫生 and 付明玉},
  title = {自主水下航行器模型预测控制研究现状与展望},
  journal = {控制理论与应用},
  volume = {35},
  number = {9},
  pages = {1181--1192},
  year = {2018},
  doi = {10.7641/CTA.2018.80287}
}

@inproceedings{heshmati2018,
  author = {Heshmati-Alamdari, Shahab and Karras, George C. and Marantos, Panagiotis and others},
  title = {A robust model predictive control approach for autonomous underwater vehicles operating in a constrained workspace},
  booktitle = {2018 IEEE International Conference on Robotics and Automation (ICRA)},
  address = {Brisbane, QLD, Australia},
  publisher = {IEEE},
  pages = {6183--6188},
  year = {2018},
  doi = {10.1109/ICRA.2018.8460548}
}

@article{heshmati2020,
  author = {Heshmati-Alamdari, Shahab and Nikou, Alexandros and Dimarogonas, Dimos V.},
  title = {Robust trajectory tracking control for underactuated autonomous underwater vehicles in uncertain environments},
  journal = {IEEE Transactions on Automation Science and Engineering},
  volume = {18},
  number = {3},
  pages = {1288--1301},
  year = {2020},
  doi = {10.1109/TASE.2020.3005888}
}

@article{torrente2021,
  author = {Torrente, Gabriel and Kaufmann, Elia and F{\"o}hn, Philipp and Scaramuzza, Davide},
  title = {Data-driven {MPC} for quadrotors},
  journal = {IEEE Robotics and Automation Letters},
  volume = {6},
  number = {2},
  pages = {3769--3776},
  year = {2021},
  doi = {10.1109/LRA.2021.3061988}
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

@inproceedings{shi2019,
  author = {Shi, Guanya and Shi, Xichen and O'Connell, Michael and Yu, Rose and Azizzadenesheli, Kamyar and Anandkumar, Animashree and Yue, Yisong and Chung, Soon-Jo},
  title = {{Neural-Lander}: Stable drone landing control using learned dynamics},
  booktitle = {2019 International Conference on Robotics and Automation (ICRA)},
  address = {Montreal, QC, Canada},
  publisher = {IEEE},
  pages = {9784--9790},
  year = {2019},
  doi = {10.1109/ICRA.2019.8794356}
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

@article{brunke2022,
  author = {Brunke, Lukas and Greeff, Melissa and Hall, Adam W. and others},
  title = {Safe learning in robotics: From learning-based control to safe reinforcement learning},
  journal = {Annual Review of Control, Robotics, and Autonomous Systems},
  volume = {5},
  pages = {411--444},
  year = {2022},
  doi = {10.1146/annurev-control-042920-020211}
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

@article{bodson2002,
  author = {Bodson, Marc},
  title = {Evaluation of optimization methods for control allocation},
  journal = {Journal of Guidance, Control, and Dynamics},
  volume = {25},
  number = {4},
  pages = {703--711},
  year = {2002},
  doi = {10.2514/2.4937}
}

@article{harkegard2002,
  author = {H{\"a}rkeg{\aa}rd, Ola},
  title = {Efficient active set algorithms for solving constrained linear quadratic control allocation problems},
  journal = {Journal of Guidance, Control, and Dynamics},
  volume = {25},
  number = {5},
  pages = {827--835},
  year = {2002},
  doi = {10.2514/2.4974}
}

@article{cheng2022,
  author = {程卫平 and 王猛 and 曾现敏 and others},
  title = {基于可行方向法的水下机器人推力分配},
  journal = {舰船科学技术},
  volume = {44},
  number = {13},
  pages = {102--106},
  year = {2022},
  doi = {10.3404/j.issn.1672-7649.2022.13.021}
}

@article{sun2023,
  author = {孙功武 and 苏义鑫 and 毛英 and others},
  title = {基于模糊逻辑的混合推进{ROV}多级推力分配策略},
  journal = {机器人},
  volume = {45},
  number = {4},
  pages = {472--482},
  year = {2023},
  doi = {10.13973/j.cnki.robot.220379}
}

@inproceedings{li2025,
  author = {Li, Ji-Hong and Lee, Mun-Jik and Kim, Min-Gyu and Kang, Hyung-Joo and Jin, Hansol and Park, JungHyeun and Cho, Gun Rae},
  title = {{MCE}-based direct {FTC} method for dynamic positioning of underwater vehicles with thruster redundancy},
  booktitle = {2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  address = {Abu Dhabi, UAE},
  publisher = {IEEE},
  pages = {arXiv:2503.18348},
  year = {2025}
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

@inproceedings{duecker2020,
  author = {Duecker, Daniel A. and Bauschmann, Nils and Hansen, Torben and others},
  title = {{HippoCampus X}---A hydrobatic open-source micro {AUV} for confined environments},
  booktitle = {2020 IEEE/OES Autonomous Underwater Vehicles Symposium (AUV)},
  address = {St. John's, NL, Canada},
  publisher = {IEEE},
  pages = {1--6},
  year = {2020},
  doi = {10.1109/AUV50043.2020.9267923}
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
"""

def generate_ris():
    # Helper to generate RIS entries
    entries = [
        ("JOUR", "miit2021", "“十四五”机器人产业发展规划", ["工业和信息化部", "国家发展和改革委员会", "科学技术部"], "中华人民共和国工业和信息化部公报", "2021", "", "12", "20-27", ""),
        ("JOUR", "miit2023", "“机器人+”应用行动实施方案", ["工业和信息化部", "教育部", "科学技术部"], "中华人民共和国工业和信息化部公报", "2023", "", "1", "18-24", ""),
        ("BOOK", "fossen2021", "Handbook of Marine Craft Hydrodynamics and Motion Control", ["Fossen, Thor I."], "John Wiley & Sons", "2021", "", "", "", "10.1002/9781119575016"),
        ("ELEC", "px4_uuv", "Submarines (Unmanned Underwater Vehicles—UUV)", ["PX4 Development Team"], "PX4 Guide", "2024", "", "", "", ""),
        ("JOUR", "fossen1995", "Nonlinear modelling of marine vehicles in 6 degrees of freedom", ["Fossen, Thor I."], "Mathematical Modelling of Systems", "1995", "1", "1", "17-27", "10.1080/13873959508837004"),
        ("BOOK", "yan2020", "水下航行器控制技术", ["严卫生", "高剑", "崔荣鑫"], "国防工业出版社", "2020", "", "", "", ""),
        ("THES", "prestero2001", "Verification of a six-degree of freedom simulation model for the REMUS autonomous underwater vehicle", ["Prestero, Timothy"], "Massachusetts Institute of Technology", "2001", "", "", "", ""),
        ("JOUR", "caccia2000", "Modeling and identification of open-frame variable configuration unmanned underwater vehicles", ["Caccia, Massimo", "Indiveri, Giovanni", "Veruggio, Gianmarco"], "IEEE Journal of Oceanic Engineering", "2000", "25", "2", "227-240", "10.1109/48.838986"),
        ("JOUR", "smallwood2004", "Model-based dynamic positioning of underwater robotic vehicles: Theory and experiment", ["Smallwood, David A.", "Whitcomb, Louis L."], "IEEE Journal of Oceanic Engineering", "2004", "29", "1", "169-186", "10.1109/JOE.2003.823312"),
        ("JOUR", "gao2019", "水下航行器水动力系数计算方法", ["高婷", "庞永杰", "王亚兴"], "哈尔滨工程大学学报", "2019", "40", "1", "174-180", "10.11990/jheu.201710080"),
        ("CONF", "chin2012", "Modeling and testing of hydrodynamic damping for a complex-shaped underwater robot operating at low speed", ["Chin, Cheng S.", "Lau, Michael W. S."], "2012 Oceans - Yeosu", "2012", "", "", "1-7", "10.1109/OCEANS-Yeosu.2012.6263445"),
        ("CONF", "ross2004", "Identification of underwater vehicle hydrodynamic coefficients using free decay tests", ["Ross, A.", "Fossen, Thor I.", "Johansen, Tor A."], "IFAC Conference on Control Applications in Marine Systems", "2004", "", "", "363-368", ""),
        ("CONF", "avila2013", "Experimental model identification of open-frame unmanned underwater vehicles", ["Avila, J. P. J.", "Adamowski, J. C."], "2013 Oceans - San Diego", "2013", "", "", "1-7", "10.23919/OCEANS.2013.6741162"),
        ("JOUR", "park2016", "System identification method for robotic manipulator based on dynamic momentum regressor", ["Park, Sanghyun", "Sung, Sangkyung", "Choi, H. Jin"], "IEEE Transactions on Instrumentation and Measurement", "2016", "65", "9", "2085-2095", "10.1109/TIM.2016.2570386"),
        ("JOUR", "harris2023", "Stable nullspace adaptive parameter identification of 6 degree-of-freedom plant and actuator models for underactuated vehicles: Theory and experimental evaluation", ["Harris, Zachary J.", "Mao, Annie M.", "Paine, Tyler M.", "Whitcomb, Louis L."], "The International Journal of Robotics Research", "2023", "42", "12", "1070-1093", "10.1177/02783649231191184"),
        ("JOUR", "brunton2016", "Discovering governing equations from data by sparse identification of nonlinear dynamical systems", ["Brunton, Steven L.", "Proctor, Joshua L.", "Kutz, J. Nathan"], "Proceedings of the National Academy of Sciences", "2016", "113", "15", "3932-3937", "10.1073/pnas.1517384113"),
        ("JOUR", "raissi2019", "Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations", ["Raissi, Maziar", "Perdikaris, Paris", "Karniadakis, George E."], "Journal of Computational Physics", "2019", "378", "", "686-707", "10.1016/j.jcp.2018.10.045"),
        ("CONF", "chen2018", "Neural ordinary differential equations", ["Chen, Ricky T. Q.", "Rubanova, Yulia", "Bettencourt, Jesse", "Duvenaud, David"], "Advances in Neural Information Processing Systems (NeurIPS 2018)", "2018", "", "", "6571-6583", ""),
        ("JOUR", "liu2026", "Koopman-based online identification with Sim2Real transfer for hydrodynamic modeling of turtle-inspired robot", ["Liu, Ang", "Zhang, Xianrui", "Xiao, Fengqi", "Cui, Guangming", "Mao, Baijin", "Yang, Yunjie", "Qu, Juntian"], "IEEE Robotics and Automation Letters", "2026", "11", "6", "6632-6639", "10.1109/LRA.2026.3682620"),
        ("JOUR", "yuh2000", "Design and control of autonomous underwater robots: A survey", ["Yuh, Junku"], "Autonomous Robots", "2000", "8", "1", "7-24", "10.1023/A:1008984701078"),
        ("JOUR", "zhu2012", "水下机器人运动控制研究进展", ["朱大奇", "孙兵"], "控制与决策", "2012", "27", "3", "321-333", ""),
        ("JOUR", "fernandes2015", "Output-feedback motion control of an underwater vehicle-manipulator system", ["Fernandes, Daniel", "Sørensen, Dag", "Pettersen, Kristin Y."], "Control Engineering Practice", "2015", "39", "", "50-64", "10.1016/j.conengprac.2014.12.005"),
        ("JOUR", "yoerger1985", "Robust trajectory control of underwater vehicles", ["Yoerger, Dana R.", "Slotine, Jean-Jacques E."], "IEEE Journal of Oceanic Engineering", "1985", "10", "4", "462-470", "10.1109/JOE.1985.1145134"),
        ("JOUR", "healey1993", "Multivariable sliding mode control for autonomous diving and steering of unmanned underwater vehicles", ["Healey, Anthony J.", "Lienard, David"], "IEEE Journal of Oceanic Engineering", "1993", "18", "3", "327-339", "10.1109/JOE.1993.236372"),
        ("JOUR", "chu2020", "Adaptive trajectory tracking control for remotely operated vehicles considering thruster dynamics and saturation constraints", ["Chu, Zhenzhong", "Xiang, Xianbo", "Zhu, Dacheng"], "ISA Transactions", "2020", "100", "", "28-37", "10.1016/j.isatra.2019.11.032"),
        ("JOUR", "qian2020", "面向扑翼飞行控制的建模与奇异摄动分析", ["钱辰", "方勇纯"], "自动化学报", "2020", "46", "12", "2585-2595", "10.16383/j.aas.c190807"),
        ("JOUR", "smeur2016", "Adaptive incremental nonlinear dynamic inversion for attitude control of micro air vehicles", ["Smeur, Ewoud J. J.", "Chu, Q. P.", "de Croon, G. C. H. E."], "Journal of Guidance, Control, and Dynamics", "2016", "39", "3", "450-461", "10.2514/1.G001490"),
        ("CONF", "slawik2024", "Attitude control of the hydrobatic intervention AUV Cuttlefish using incremental nonlinear dynamic inversion", ["Slawik, Torben", "Vyas, S.", "Christensen, L."], "2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)", "2024", "", "", "781-787", "10.1109/IROS58592.2024.10802082"),
        ("JOUR", "zhang2018", "自主水下航行器模型预测控制研究现状与展望", ["张磊", "严卫生", "付明玉"], "控制理论与应用", "2018", "35", "9", "1181-1192", "10.7641/CTA.2018.80287"),
        ("CONF", "heshmati2018", "A robust model predictive control approach for autonomous underwater vehicles operating in a constrained workspace", ["Heshmati-Alamdari, Shahab", "Karras, George C.", "Marantos, Panagiotis"], "2018 IEEE International Conference on Robotics and Automation (ICRA)", "2018", "", "", "6183-6188", "10.1109/ICRA.2018.8460548"),
        ("JOUR", "heshmati2020", "Robust trajectory tracking control for underactuated autonomous underwater vehicles in uncertain environments", ["Heshmati-Alamdari, Shahab", "Nikou, Alexandros", "Dimarogonas, Dimos V."], "IEEE Transactions on Automation Science and Engineering", "2020", "18", "3", "1288-1301", "10.1109/TASE.2020.3005888"),
        ("JOUR", "torrente2021", "Data-driven MPC for quadrotors", ["Torrente, Gabriel", "Kaufmann, Elia", "Föhn, Philipp", "Scaramuzza, Davide"], "IEEE Robotics and Automation Letters", "2021", "6", "2", "3769-3776", "10.1109/LRA.2021.3061988"),
        ("JOUR", "liniger2015", "Optimization-based autonomous racing of 1:43 scale RC cars", ["Liniger, Alexander", "Domahidi, Alexander", "Morari, Manfred"], "Optimal Control Applications and Methods", "2015", "36", "5", "628-647", "10.1002/oca.2123"),
        ("CONF", "shi2019", "Neural-Lander: Stable drone landing control using learned dynamics", ["Shi, Guanya", "Shi, Xichen", "O'Connell, Michael", "Yu, Rose", "Azizzadenesheli, Kamyar", "Anandkumar, Animashree", "Yue, Yisong", "Chung, Soon-Jo"], "2019 International Conference on Robotics and Automation (ICRA)", "2019", "", "", "9784-9790", "10.1109/ICRA.2019.8794356"),
        ("JOUR", "oconnell2022", "Neural-Fly enables rapid learning for agile flight in strong winds", ["O'Connell, Michael", "Shi, Guanya", "Shi, Xichen"], "Science Robotics", "2022", "7", "66", "eabg6513", "10.1126/scirobotics.abg6513"),
        ("JOUR", "brunke2022", "Safe learning in robotics: From learning-based control to safe reinforcement learning", ["Brunke, Lukas", "Greeff, Melissa", "Hall, Adam W."], "Annual Review of Control, Robotics, and Autonomous Systems", "2022", "5", "", "411-444", "10.1146/annurev-control-042920-020211"),
        ("JOUR", "johansen2013", "Control allocation: A survey", ["Johansen, Tor A.", "Fossen, Thor I."], "Automatica", "2013", "49", "5", "1087-1103", "10.1016/j.automatica.2013.01.035"),
        ("JOUR", "bodson2002", "Evaluation of optimization methods for control allocation", ["Bodson, Marc"], "Journal of Guidance, Control, and Dynamics", "2002", "25", "4", "703-711", "10.2514/2.4937"),
        ("JOUR", "harkegard2002", "Efficient active set algorithms for solving constrained linear quadratic control allocation problems", ["Härkegård, Ola"], "Journal of Guidance, Control, and Dynamics", "2002", "25", "5", "827-835", "10.2514/2.4974"),
        ("JOUR", "cheng2022", "基于可行方向法的水下机器人推力分配", ["程卫平", "王猛", "曾现敏"], "舰船科学技术", "2022", "44", "13", "102-106", "10.3404/j.issn.1672-7649.2022.13.021"),
        ("JOUR", "sun2023", "基于模糊逻辑的混合推进ROV多级推力分配策略", ["孙功武", "苏义鑫", "毛英"], "机器人", "2023", "45", "4", "472-482", "10.13973/j.cnki.robot.220379"),
        ("CONF", "li2025", "MCE-based direct FTC method for dynamic positioning of underwater vehicles with thruster redundancy", ["Li, Ji-Hong", "Lee, Mun-Jik", "Kim, Min-Gyu", "Kang, Hyung-Joo", "Jin, Hansol", "Park, JungHyeun", "Cho, Gun Rae"], "2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)", "2025", "", "", "arXiv:2503.18348", ""),
        ("CONF", "meier2015", "PX4: A node-based multithreaded open source robotics framework for deeply embedded platforms", ["Meier, Lorenz", "Honegger, Dominik", "Pollefeys, Marc"], "2015 IEEE International Conference on Robotics and Automation (ICRA)", "2015", "", "", "6235-6240", "10.1109/ICRA.2015.7140074"),
        ("CONF", "duecker2020", "HippoCampus X—A hydrobatic open-source micro AUV for confined environments", ["Duecker, Daniel A.", "Bauschmann, Nils", "Hansen, Torben"], "2020 IEEE/OES Autonomous Underwater Vehicles Symposium (AUV)", "2020", "", "", "1-6", "10.1109/AUV50043.2020.9267923"),
        ("JOUR", "vonbenzon2022", "An open-source benchmark simulator: Control of a BlueROV2 underwater robot", ["von Benzon, Mikkel", "Sørensen, Frederik F.", "Uth, Emil"], "Journal of Marine Science and Engineering", "2022", "10", "12", "1898", "10.3390/jmse10121898")
    ]
    
    ris_lines = []
    for typ, key, title, authors, sec_title, yr, vol, is_no, sp_ep, doi in entries:
        ris_lines.append(f"TY  - {typ}")
        ris_lines.append(f"ID  - {key}")
        ris_lines.append(f"TI  - {title}")
        for a in authors:
            ris_lines.append(f"AU  - {a}")
        if typ in ["JOUR"]:
            ris_lines.append(f"JO  - {sec_title}")
        elif typ in ["CONF"]:
            ris_lines.append(f"T2  - {sec_title}")
        elif typ in ["BOOK"]:
            ris_lines.append(f"PB  - {sec_title}")
        elif typ in ["THES"]:
            ris_lines.append(f"PB  - {sec_title}")
        elif typ in ["ELEC"]:
            ris_lines.append(f"PB  - {sec_title}")
            ris_lines.append(f"UR  - https://docs.px4.io/main/en/frames_sub/index")
        ris_lines.append(f"PY  - {yr}")
        if vol:
            ris_lines.append(f"VL  - {vol}")
        if is_no:
            ris_lines.append(f"IS  - {is_no}")
        if sp_ep:
            if "-" in sp_ep:
                sp, ep = sp_ep.split("-", 1)
                ris_lines.append(f"SP  - {sp}")
                ris_lines.append(f"EP  - {ep}")
            else:
                ris_lines.append(f"SP  - {sp_ep}")
        if doi:
            ris_lines.append(f"DO  - {doi}")
        ris_lines.append("ER  - \n")
    return "\n".join(ris_lines)

def main():
    # 1. 写入 references.bib
    with open(BIB_PATH, "w", encoding="utf-8") as f:
        f.write(BIB_CONTENT.strip() + "\n")
    print(f"已更新 {BIB_PATH}，共 45 篇 BibTeX 词条。")

    # 2. 写入 references.ris
    ris_text = generate_ris()
    with open(RIS_PATH, "w", encoding="utf-8") as f:
        f.write(ris_text.strip() + "\n")
    print(f"已更新 {RIS_PATH}，共 45 篇 RIS 词条。")

if __name__ == "__main__":
    main()
