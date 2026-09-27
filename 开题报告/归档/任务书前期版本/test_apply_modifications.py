import win32com.client
import os
import sys

def apply_modifications(doc_path):
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    word.DisplayAlerts = 0
    
    try:
        doc = word.Documents.Open(doc_path)
        
        # 1. Update Table 1 (Title cell: Row 1, Cell 2)
        t1 = doc.Tables(1)
        c_title = t1.Cell(1, 2)
        # Update title text
        title_text = "基于PX4的水下航行器\r动力学建模、系统辨识、运动控制与推力分配研究"
        # Preserve font formatting
        rng_title = doc.Range(c_title.Range.Start, c_title.Range.End - 1)
        font_name = rng_title.Font.Name
        font_size = rng_title.Font.Size
        rng_title.Text = title_text
        rng_title.Font.Name = font_name
        rng_title.Font.Size = font_size
        rng_title.HighlightColorIndex = 0 # No highlight
        print("Updated Title cell")
        
        # 2. Update Table 3 (Schedule Table: Row 5, Cell 2)
        t_sched = doc.Tables(3)
        c_sched_5 = t_sched.Rows(5).Cells(2)
        sched_5_text = "水下航行器动力学与推进器建模、PX4/SITL基础环境搭建"
        rng_sched_5 = doc.Range(c_sched_5.Range.Start, c_sched_5.Range.End - 1)
        f_name_s = rng_sched_5.Font.Name
        f_size_s = rng_sched_5.Font.Size
        rng_sched_5.Text = sched_5_text
        rng_sched_5.Font.Name = f_name_s
        rng_sched_5.Font.Size = f_size_s
        rng_sched_5.HighlightColorIndex = 0
        print("Updated Schedule Row 5")
        
        # 3. Find and update body paragraphs
        # We will map by exact original text prefix or paragraph content
        body_updates = [
            # P57 (Background 1)
            ("水下无人航行器（UUV/ROV）在海洋资源勘查",
             "水下无人航行器（UUV/ROV）在海洋资源勘查、海底管道巡检、水下结构物检测和海洋牧场维护等领域具有广泛应用。面向复杂水下作业，航行器需要完成悬停、姿态保持、定深和定航等任务，对运动控制的精度、稳定性及执行机构协调能力提出了要求。本课题依托已有八推进器水下航行器平台开展研究，在现有平台基础上进行动力学建模、系统辨识、运动控制、推进器控制分配及PX4/SITL闭环仿真验证。"),
            
            # P58 (Background 2)
            ("水下航行器运动具有六自由度耦合和非线性特征，其动力学同时受到刚体惯性、附加质量、科氏力与向心力、水动力阻尼、重力与浮力恢复作用以及外部水流扰动的影响",
             "水下航行器运动具有六自由度耦合和非线性特征，其动力学同时受到刚体惯性、附加质量、科氏力与向心力、水动力阻尼、重力与浮力恢复作用以及外部水流扰动等因素影响。合理描述上述主要动力学作用及其相互关系，是分析航行器动态响应、开展系统辨识、设计运动控制系统和进行闭环仿真的基础。"),
            
            # P59 (Background 3)
            ("实际平台的部分质量与惯性参数",
             "受模型参数获取方式、制造误差及运行条件等因素影响，理论模型与平台实际动态特性之间可能存在偏差。因此，需要在理论动力学建模基础上明确系统辨识所需的输入、输出及相关数据，结合已有平台参数资料及相关数据开展系统辨识，获得能够反映航行器主要动态特性的模型，并通过模型输出与相关数据或典型动态响应的比较进行基本验证，分析模型误差及适用范围，为后续运动控制设计和闭环仿真提供模型基础。"),
            
            # P60 (Background 4)
            ("在动力学建模与模型验证的基础上，本课题研究基于动力学模型和状态反馈",
             "在经验证的航行器模型基础上，运动控制部分根据参考状态与当前状态之间的误差，结合模型信息和状态反馈计算航行器所需的期望广义力和力矩，实现姿态、深度和航向等基本运动状态的闭环控制。针对已有平台的八推进器配置，根据推进器安装位置、推力方向及力臂关系建立控制分配模型，将期望广义力和力矩转换为各推进器推力指令，并考虑推进器基本推力输出范围。"),
            
            # P61 (Background 5)
            ("PX4具有模块化软件架构，可通过uORB实现状态信息、控制量和执行器指令",
             "PX4具有模块化软件架构，可通过uORB实现状态信息、控制量和推进器指令的数据交互，并支持SITL软件在环仿真。本课题将航行器模型、运动控制和八推进器控制分配模块在PX4/SITL环境中进行闭环集成，通过姿态、深度、航向等典型运动工况及适量外部扰动工况开展仿真验证，形成“已有平台—建模与系统辨识—模型验证—运动控制—控制分配—PX4/SITL闭环验证”的研究链路。"),
            
            # P63 (Section 2.1 heading)
            ("2.1 水下航行器动力学与系统辨识",
             "2.1 水下航行器动力学建模与系统辨识"),
            
            # P64 (Section 2.1 content)
            ("以八推进器水下航行器为对象，建立六自由度运动学与动力学模型",
             "依托已有八推进器水下航行器平台，建立六自由度运动学与动力学模型，考虑刚体惯性、附加质量、科氏力与向心力、水动力阻尼、重力与浮力恢复作用等主要动力学因素，并结合已有平台推进器特性建立单个推进器或执行机构的必要模型。在理论建模基础上梳理影响航行器主要动态特性的模型因素，明确系统辨识所需的输入、输出及相关数据，结合已有平台参数资料及相关数据开展系统辨识，获得满足后续运动控制和闭环仿真需要的航行器模型。通过模型输出与相关数据或典型动态响应进行比较，对模型进行基本验证，并分析模型误差及适用范围，为后续运动控制设计和PX4/SITL闭环仿真提供模型基础。"),
            
            # P66 (Section 2.2 content)
            ("以建立并验证的动力学模型为基础，研究基于模型信息与状态反馈的水下航行器闭环运动控制方法",
             "以2.1建立并验证的航行器模型为基础，结合航行器状态反馈构建闭环运动控制系统。根据参考状态与当前状态之间的误差进行控制计算，形成航行器所需的期望广义力和力矩，实现姿态、深度和航向等基本运动状态的闭环控制。通过典型运动工况分析系统的跟踪性能和动态响应，并适当分析模型误差及外部扰动对闭环性能的影响。"),
            
            # P67 (Section 2.3 heading)
            ("2.3 多推进器控制分配与执行器约束",
             "2.3 八推进器控制分配"),
            
            # P68 (Section 2.3 content)
            ("依据八推进器布局建立控制分配矩阵，分析推进器布置对各自由度广义力与力矩生成能力的影响",
             "根据已有八推进器平台的推进器安装位置、推力方向及力臂关系，建立各推进器推力与航行器广义力、力矩之间的映射关系及八推进器控制分配矩阵。在冗余推进器配置下，将2.2输出的期望广义力和力矩转换为各推进器推力指令，并结合推进器实际输出范围考虑基本推力约束。通过控制分配误差及各推进器输出情况分析分配效果，为PX4/SITL闭环仿真提供推进器指令。"),
            
            # P69 (Section 2.4 heading)
            ("2.4 PX4控制系统实现与SITL闭环仿真验证",
             "2.4 PX4/SITL闭环仿真与系统验证"),
            
            # P70 (Section 2.4 content)
            ("按照PX4软件架构及模块开发规范",
             "基于PX4软件框架搭建水下航行器闭环仿真系统，通过uORB完成必要的状态信息、控制量和推进器指令的数据交互，将2.1建立的航行器模型、2.2运动控制模块和2.3八推进器控制分配模块进行闭环集成。在PX4/SITL环境中开展姿态、深度、航向等典型运动工况仿真，并结合适量外部扰动工况评价系统响应。根据实际需要采用跟踪误差、动态响应和控制分配误差等指标进行性能分析，验证完整闭环系统的控制效果。"),
             
            # P73 (Req 1)
            ("（1）查阅水下航行器六自由度动力学、系统辨识",
             "（1）查阅水下航行器动力学、系统辨识、运动控制、推进器建模、控制分配及PX4软件架构等相关中外文献，归纳相关研究方法及其适用条件，完成文献综述。"),
             
            # P74 (Req 2)
            ("（2）完成开题报告，明确研究目标、总体方案、技术路线、数据来源和进度计划",
             "（2）完成开题报告，明确研究目标、总体方案、技术路线和进度计划，参加开题答辩。"),
             
            # P75 (Req 3)
            ("（3）建立水下航行器六自由度动力学模型、推进器模型及八推进器控制分配模型",
             "（3）依托已有八推进器水下航行器平台，建立六自由度动力学模型和必要的推进器模型，分析影响航行器运动的主要动力学因素。"),
             
            # P76 (Req 4)
            ("（4）明确模型辨识的输入输出关系，利用已有平台数据",
             "（4）明确系统辨识的输入输出关系，结合已有平台参数资料及相关数据开展系统辨识和模型验证，分析模型误差及适用范围，为运动控制设计和闭环仿真提供模型基础。"),
             
            # P77 (Req 5)
            ("（5）基于动力学模型与状态反馈设计运动控制系统",
             "（5）基于航行器模型和状态反馈设计运动控制方法，实现姿态、深度和航向等基本运动状态的闭环控制，并分析典型工况下的动态响应及适量外部扰动影响。"),
             
            # P78 (Req 6)
            ("（6）研究八推进器冗余控制分配及推力幅值、变化率等执行器约束",
             "（6）根据已有平台的八推进器布局建立控制分配模型，实现期望广义力、力矩到各推进器推力指令的分配，并考虑推进器基本推力输出范围，分析控制分配误差及推进器输出情况。"),
             
            # P79 (Req 7)
            ("（7）搭建PX4/SITL闭环仿真环境，集成动力学模型",
             "（7）基于PX4/SITL完成航行器模型、运动控制和八推进器控制分配模块的闭环集成，通过典型运动工况及适量外部扰动工况开展仿真验证和性能分析。"),
             
            # P80 (Req 8)
            ("（8）整理模型文件、程序代码、仿真数据与研究结果",
             "（8）整理模型、程序、仿真数据及研究结果，完成毕业论文撰写、修改、查重和答辩。"),
             
            # P155 (Other requirements)
            ("本课题以八推进器水下航行器六自由度动力学建模、关键参数辨识与模型验证",
             "本课题依托已有八推进器水下航行器平台，以六自由度动力学建模、系统辨识与模型验证、基于模型和状态反馈的运动控制、八推进器控制分配以及PX4/SITL闭环仿真为主要验收内容。应提交能够支撑研究结论的航行器与推进器模型、系统辨识及模型验证结果、运动控制与控制分配程序、典型工况仿真数据和性能分析，并在毕业论文中说明模型假设、参数资料来源、实现流程及评价指标。")
        ]
        
        for p_idx in range(1, doc.Paragraphs.Count + 1):
            p = doc.Paragraphs(p_idx)
            t = p.Range.Text.strip().replace('\r', '').replace('\x07', '')
            for prefix, new_content in body_updates:
                if t.startswith(prefix) or prefix in t:
                    rng = doc.Range(p.Range.Start, p.Range.End - 1)
                    f_name = rng.Font.Name
                    f_size = rng.Font.Size
                    f_bold = rng.Font.Bold
                    rng.Text = new_content
                    rng.Font.Name = f_name
                    rng.Font.Size = f_size
                    rng.Font.Bold = f_bold
                    rng.HighlightColorIndex = 0 # Ensure NO yellow highlight!
                    print(f"Updated paragraph matching '{prefix[:20]}...'")
                    break

        # 4. Update References (Section 5)
        # Find heading paragraph "五、毕业论文应收集的资料及主要参考文献"
        ref_h_idx = -1
        for i in range(1, doc.Paragraphs.Count + 1):
            t = doc.Paragraphs(i).Range.Text.strip().replace('\r', '').replace('\x07', '')
            if "五、毕业论文应收集的资料及主要参考文献" in t:
                ref_h_idx = i
                break
                
        print(f"References heading at paragraph {ref_h_idx}")
        
        revised_refs_9 = [
            "[1] Fossen T I. Handbook of Marine Craft Hydrodynamics and Motion Control[M]. 2nd ed. Chichester, UK: John Wiley & Sons, 2021. DOI: 10.1002/9781119575016.",
            "[2] Caccia M, Indiveri G, Veruggio G. Modeling and identification of open-frame variable configuration unmanned underwater vehicles[J]. IEEE Journal of Oceanic Engineering, 2000, 25(2): 227-240. DOI: 10.1109/48.838986.",
            "[3] Ross A, Fossen T I, Johansen T A. Identification of underwater vehicle hydrodynamic coefficients using free decay tests[J]. IFAC Proceedings Volumes, 2004, 37(10): 363-368. DOI: 10.1016/S1474-6670(17)31759-7.",
            "[4] Avila J P J, Donha D C, Adamowski J C. Experimental model identification of open-frame underwater vehicles[J]. Ocean Engineering, 2013, 60: 81-94. DOI: 10.1016/j.oceaneng.2012.10.007.",
            "[5] Liu J C, Liu X M, Xu Y R. Application of ML to system identification for underwater vehicle[J]. Journal of Marine Science and Application, 2002, 1(1): 21-25. DOI: 10.1007/BF02921412.",
            "[6] Chin C, Lau M. Modeling and testing of hydrodynamic damping model for a complex-shaped remotely-operated vehicle for control[J]. Journal of Marine Science and Application, 2012, 11(2): 150-163. DOI: 10.1007/s11804-012-1117-2.",
            "[7] Fernandes D A, Srensen A J, Pettersen K Y, Donha D C. Output feedback motion control system for observation class ROVs based on a high-gain state observer: Theoretical and experimental results[J]. Control Engineering Practice, 2015, 39: 90-102. DOI: 10.1016/j.conengprac.2014.12.005.",
            "[8] Johansen T A, Fossen T I. Control allocation—A survey[J]. Automatica, 2013, 49(5): 1087-1103. DOI: 10.1016/j.automatica.2013.01.035.",
            "[9] Meier L, Honegger D, Pollefeys M. PX4: A node-based multithreaded open source robotics framework for deeply embedded platforms[C]//2015 IEEE International Conference on Robotics and Automation (ICRA). Seattle, WA: IEEE, 2015: 6235-6240. DOI: 10.1109/ICRA.2015.7140074."
        ]
        
        # Identify existing reference paragraphs
        # In target doc, references are between ref_h_idx and "六、其他要求"
        ref_p_indices = []
        for i in range(ref_h_idx + 1, doc.Paragraphs.Count + 1):
            t = doc.Paragraphs(i).Range.Text.strip().replace('\r', '').replace('\x07', '')
            if t.startswith("六、其他要求"):
                break
            if t.startswith("[") and "]" in t[:5]:
                ref_p_indices.append(i)
                
        print(f"Found {len(ref_p_indices)} reference paragraphs: {ref_p_indices}")
        
        # Update first 9 references
        for idx in range(9):
            p_i = ref_p_indices[idx]
            p = doc.Paragraphs(p_i)
            rng = doc.Range(p.Range.Start, p.Range.End - 1)
            f_name = rng.Font.Name
            f_size = rng.Font.Size
            rng.Text = revised_refs_9[idx]
            rng.Font.Name = f_name
            rng.Font.Size = f_size
            rng.HighlightColorIndex = 0
            
        # Delete extra references (from index 9 onwards, in reverse order)
        for idx in range(len(ref_p_indices) - 1, 8, -1):
            p_i = ref_p_indices[idx]
            doc.Paragraphs(p_i).Range.Delete()
            print(f"Deleted extra reference paragraph {p_i}")
            
        # Ensure all paragraphs have no yellow highlight
        for i in range(1, doc.Paragraphs.Count + 1):
            doc.Paragraphs(i).Range.HighlightColorIndex = 0
            
        doc.Save()
        doc.Close()
        print("Document saved successfully!")
    finally:
        word.Quit()

if __name__ == '__main__':
    test_doc = r'D:\tj\Graduation Project\开题报告\test_target_copy.doc'
    apply_modifications(test_doc)
