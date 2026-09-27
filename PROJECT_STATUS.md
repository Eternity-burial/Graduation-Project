# 毕业论文全周期进度、决策与跨会话记忆总控台账 (`PROJECT_STATUS.md`)

> **使用规范（Planning with Files 跨窗口持久化记忆机制）**：
> 1. **新对话必读**：每当开启新的对话窗口推进毕设任务时，Agent 必须首先读取本文件，快速恢复上下文，无需用户重复交代背景；
> 2. **里程碑必更**：每当完成一节文档修订、一次参数辨识/控制仿真实验、或达成新的技术决策时，Agent 必须在执行 `git commit` 前同步更新本文件。

---

## 一、 课题核心基准信息

- **毕业论文题目**：《基于PX4的水下航行器模型控制方法研究》
  - **任务书关联全称**：《基于PX4的水下航行器动力学建模、系统辨识、运动控制与推力分配研究》
- **研究对象**：实验室已有**八推进器开架式水下航行器（Open-frame UUV/ROV）**实验平台（水平面 4 台矢量倾斜布置 + 垂直面 4 台垂向对称布置，6-DOF 全驱动冗余构型）。
- **核心表述红线**：坚持**“机理建模与数据辨识相结合、航行器模型特性补偿与实时状态反馈相结合、考虑推进器基本推力输出范围的 $6 \times 8$ 控制分配”**，在纲领性文件中保持算法开放性与工程稳健性。

---

## 二、 四阶段里程碑总进度（Roadmap & Checklist）

### 阶段 0：选题论证、任务书与开题报告（当前阶段：开题报告已完成深度优化）
- [x] PX4 与 ArduSub 水下控制架构深度对比调研（[PX4与ArduSub对比分析.md](file:///d:/tj/Graduation%20Project/选题/PX4与ArduSub对比分析.md)）
- [x] 任务书定稿与导师审阅口径对齐（[1毕业设计（论文）任务书.doc](file:///d:/tj/Graduation%20Project/开题报告/1毕业设计（论文）任务书.doc)）
- [x] 找回并保护用户手工标注版开题报告（[用户标注版_开题报告_已恢复.doc](file:///d:/tj/Graduation%20Project/开题报告/用户标注版_开题报告_已恢复.doc)）
- [x] 建立 Git 版本控制体系、全局规则 [AGENTS.md](file:///d:/tj/Graduation%20Project/AGENTS.md) 及 4 大专业 Skill
- [x] 完成开题报告三阶段全面深度优化（3 张 300 DPI 原理/技术路线/PX4 架构图及可编辑 `.drawio`、表 1 方案对比分析表、毕业论文拟定六章大纲、5 项研究方法与式(3) $6 \times 8$ 推力分配方程、全文去 AI 腔润色、20 篇 GB/T 7714 顺序编码文献 `[1]~[20]`），同步生成正式纯净版（[开题报告-基于PX4的水下航行器模型控制方法研究.docx](file:///d:/tj/Graduation%20Project/开题报告/开题报告-基于PX4的水下航行器模型控制方法研究.docx) / `.doc`）与差异高亮对比版（[开题报告-新旧版本修改对比版_逐段差异高亮.docx](file:///d:/tj/Graduation%20Project/开题报告/开题报告-新旧版本修改对比版_逐段差异高亮.docx) / `.doc`）
- [ ] **待办**：准备开题答辩 PPT 汇报材料

### 阶段 1：外文文献精读与六自由度建模（进行中）
- [x] 精读并完成前 3 篇核心英文文献中文全译与双语精读平台（[资料/index.html](file:///d:/tj/Graduation%20Project/资料/index.html) `paper1` ~ `paper3`）
- [ ] **待办**：完成 `04-en-*.pdf` 与 `05-en-*.pdf` 的 100% 中文全译及双语阅读器数据接入（`data_paper4.js`, `data_paper5.js`）
- [ ] **待办**：梳理实验室八推进器 ROV 平台物理几何参数（质量、主尺度、重心/浮心、8 推进器坐标 $\boldsymbol{r}_i$ 与方向矢量 $\boldsymbol{d}_i$），建立参数化 Fossen 6-DOF 仿真模型

### 阶段 2：系统辨识与模型验证（待启动）
- [ ] **待办**：明确激励输入与状态响应输出关系，构建水动力参数（附加质量 $\boldsymbol{M}_A$、线性与二次阻尼 $\boldsymbol{D}$、恢复力矩参数）最小二乘/回归辨识脚本
- [ ] **待办**：使用 Autoresearch 迭代闭环完成代表性动态响应下的模型拟合验证与残差分析

### 阶段 3：运动控制设计与八推进器控制分配（前期原型已建，待扩展为 6-DOF 全模型）
- [x] 单通道/姿态角速率级 INDI vs. PID 离线仿真与 C++ 原型验证（[PX4_INDI_Research/](file:///d:/tj/Graduation%20Project/PX4_INDI_Research)）
- [ ] **待办**：构建统一的 6-DOF“基于航行器模型补偿 + 状态反馈”闭环控制器框架（支持纯 PID、模型前馈补偿 FBL、增量动态逆 INDI 等对比）
- [ ] **待办**：构建 $6 \times 8$ 八推进器控制分配器（伪逆基准 + 考虑推力基本范围约束 $[\boldsymbol{T}_{\min}, \boldsymbol{T}_{\max}]$ 的有界分配），量化分析分配误差 $\boldsymbol{e}_{\tau}$ 与推力输出饱和情况

### 阶段 4：PX4/SITL 闭环集成与毕业论文撰写（待启动）
- [ ] **待办**：在 PX4 SITL 环境中集成八推进器分配矩阵与水下 6-DOF 运动控制模块，通过 uORB 消息闭环验证典型工况与外部扰动工况
- [ ] **待办**：撰写毕业论文各章节正文（使用 [`omml_converter.py`](file:///d:/tj/Graduation%20Project/.agents/skills/academic-doc-builder/scripts/omml_converter.py) 注入原生 Word OMML 公式）

---

## 三、 关键设计决策与避坑发现台账（Key Findings & Decisions）

1. **学长全过程资料核心启示**（详见 [学长毕设全过程资料深度解析与演进避坑指南.md](file:///d:/tj/Graduation%20Project/参考/学长毕设全过程资料深度解析与演进避坑指南.md)）：
   - 开题报告 V1 $\rightarrow$ V5 的最大教训是早期“算法口号贴太多、约束包揽太满”；必须采用平实严谨的工程语言；
   - 毕业论文全部数学公式必须采用 Word 原生 `<m:oMath>`（OMML），严禁嵌入公式截图。
2. **Word 自动化排版核心发现**：
   - 学校官方模板正文字体为小四号宋体 + Times New Roman，1.5 倍行距，**仅一/二级标题有段前段后 0.5 行间距，正文与参考文献严禁设置段前段后间距**。
3. **工作区四大技能（`.agents/skills/`）分工**：
   - [`academic-doc-builder`](file:///d:/tj/Graduation%20Project/.agents/skills/academic-doc-builder/SKILL.md)：负责文档撰写、原生 OMML 公式转换、GB/T 7714 参考文献及去 AI 腔润色（内嵌 `Supervisor-Skills` 证据门控与润色规范）；
   - [`rov-modeling-control-px4`](file:///d:/tj/Graduation%20Project/.agents/skills/rov-modeling-control-px4/SKILL.md)：负责 6-DOF 建模、系统辨识、运动控制、$6 \times 8$ 推力分配及 `Autoresearch` 定量指标迭代实验闭环；
   - [`paper-translation-reader`](file:///d:/tj/Graduation%20Project/.agents/skills/paper-translation-reader/SKILL.md)：负责外文文献 100% 全译、双语网页阅读器更新及引文两步真伪核验；
   - [`drawio-reconstruction`](file:///d:/tj/Graduation%20Project/.agents/skills/drawio-reconstruction/SKILL.md)：负责将参考架构图、控制框图一键重建为可编辑的 `.drawio` 矢量源文件。

---

## 四、 跨会话交接日志（Session Handoff Log）

- **2026-09-27**：
  - 完成 Git 仓库初始化与用户标注版开题报告恢复（[用户标注版_开题报告_已恢复.doc](file:///d:/tj/Graduation%20Project/开题报告/用户标注版_开题报告_已恢复.doc)）；
  - 完成 `LaTeX -> MathML -> OMML` 原生 Word 公式引擎 [`omml_converter.py`](file:///d:/tj/Graduation%20Project/.agents/skills/academic-doc-builder/scripts/omml_converter.py) 开发与测试；
  - 完成 `HKUSTDial/Supervisor-Skills`、`codex-autoresearch`、`planning-with-files` 精华吸收与本土化配置，落地本总控台账 `PROJECT_STATUS.md`；
  - 通过 `/grill-me` 达成开题报告四维度优化共识并落地执行：新增图 1（坐标系与八推进器空间布置图）与表 1（控制与推力分配方案对比表），升级图 2（技术路线图）与图 3（PX4/SITL 架构框图）并导出 `.drawio`，补充毕业论文六章大纲、5 项研究方法与式(3) $6 \times 8$ 控制分配方程，完成去 AI 腔润色与 20 篇文献顺序编码更新，同步输出正式纯净版与差异高亮对比版 `.docx`/`.doc`。
