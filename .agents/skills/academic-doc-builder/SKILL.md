---
name: academic-doc-builder
description: >-
  Use this skill whenever the user asks to draft, edit, format, or generate
  graduation project academic documents (Task Book 任务书, Opening Report 开题报告,
  Midterm Report 中期检查, Thesis 毕业论文), manipulate Word (.doc/.docx) files,
  manage citations/references with EndNote or Zotero (.bib/.ris), render native
  Word OMML math formulas, generate diff-highlighted review versions, or plot
  300 DPI technical figures for reports.
---

# 毕设学术文档撰写、原生公式与参考文献自动化技能 (Academic Document Builder)

本技能定义了《基于PX4的水下航行器模型控制方法研究》毕业论文全周期学术文档（任务书、开题报告、中期检查、毕业论文）的文风准则、学校官方模板原生 XML 样式映射规范、Word 原生 OMML 数学公式渲染规范、GB/T 7714-2015 参考文献自动重排与 Zotero/EndNote（`.bib`/`.ris`）协同规范，以及 Word 自动化操作安全红线。

---

## 一、 导师审阅文风与学术表述准则

在起草或修改任何毕设材料时，必须严格遵守以下表述口径（详见根目录 [AGENTS.md](file:///d:/tj/Graduation%20Project/AGENTS.md)）：

1. **研究链路闭环口径**：
   - 始终围绕**“已有八推进器水下航行器平台 $\rightarrow$ 六自由度动力学与推进器建模 $\rightarrow$ 系统辨识与模型验证 $\rightarrow$ 基于模型与状态反馈的运动控制 $\rightarrow$ 八推进器控制分配 $\rightarrow$ PX4/SITL 闭环仿真验证”**展开。
2. **稳健弹性、不把路走窄**：
   - 强调“依托已有平台参数资料和相关数据开展系统辨识与模型验证，分析模型误差及适用范围”。
   - 运动控制部分表述为“结合航行器模型特性补偿与实时状态反馈构建闭环运动控制系统，计算期望广义力和力矩，实现姿态、深度和航向等基本运动状态的闭环控制”，为后续具体算法比选（如模型前馈 + PID、反馈线性化 FBL、增量非线性动态逆 INDI 等）留出充分空间。
   - 控制分配部分表述为“根据八推进器安装位置、推力方向及力臂关系建立控制分配矩阵，考虑推进器基本推力输出范围，分析控制分配误差及各推进器输出情况”，不随意承诺难以验证的复杂硬件约束（如推力变化率动态约束等）。
3. **行文规范、去 AI 腔与证据门控（Supervisor-Skills 融合规范）**：
   - 杜绝口语化、空洞套话与大模型浮夸词（如“卓越、颠覆性、完美解决、赋能”，以及破折号 `——` 连接分句），数学符号与 [AGENTS.md](file:///d:/tj/Graduation%20Project/AGENTS.md) 中的 Fossen 6-DOF 符号体系 100% 保持一致。
   - **撰写或润色任何正文段落与设计配图前，必须阅读并执行**：[supervisor_writing_and_figure_guide.md](./references/supervisor_writing_and_figure_guide.md)（包含 L0~L4 证据门控防幻觉纪律、中英文去 AI 腔禁用词表、审稿人逻辑自查清单及双重编码科研作图规范）。

---

## 二、 标准执行工作流（Git 前置检查 + Markdown 草稿 + 题录库 + 双格式导出 + Git 快照）

切勿在未对齐内容前直接盲改二进制 Word 文件，必须严格按以下七步闭环推进：

1. **第零步：Git 状态前置检查（防覆盖、防丢失铁律）**
   - 在运行任何构建或修改脚本前，必须先在终端执行 `git status --short`，检查目标 Word 文档或脚本是否有未暂存的用户手工编辑；
   - 若检测到用户改动，**严禁静默覆盖**，必须先提示用户或将其单独另存为快照备份（如 `*_用户标注备份.*`）；写操作必须保留 `.bak` 备份机制。
2. **第一步：Markdown 草稿对齐**
   - 先在对应的 Markdown 草稿文件（如 [开题报告_全文草稿.md](file:///d:/tj/Graduation%20Project/开题报告/开题报告_全文草稿.md)）中完成文本、公式、表格与技术路线图的编写或修订。
3. **第二步：参考文献顺序校验与 `.bib` / `.ris` 题录库同步**
   - 按 GB/T 7714-2015 顺序编码制，严格依据文献在正文中**首次出现的先后顺序**编号 `[1] ~ [N]`，同步更新 [references.bib](file:///d:/tj/Graduation%20Project/开题报告/references.bib) 与 [references.ris](file:///d:/tj/Graduation%20Project/开题报告/references.ris)，支持一键导入本地 **Zotero**（`C:\Program Files\Zotero\zotero.exe`）或 **EndNote**。
4. **第三步：300 DPI 高清配图与可编辑 `.drawio` 架构图生成（如需更新配图）**
   - 使用 Python（Pillow / Matplotlib）脚本（参考 [generate_report_figures.py](file:///d:/tj/Graduation%20Project/开题报告/generate_report_figures.py)）生成 300 DPI 出版级白底高清 PNG 配图，严禁使用低分辨率截图；
   - 若需将论文参考图、控制框图或系统架构图重建为**可编辑的 `.drawio` 矢量源文件**，联动激活工作区技能 [drawio-reconstruction](file:///d:/tj/Graduation%20Project/.agents/skills/drawio-reconstruction/SKILL.md)。
5. **第四步：基于官方模板生成/更新 `.docx`（默认仅生成 `.docx`，原生 OMML 公式注入）**
   - 运行 Python 脚本（参考 [build_opening_report_doc.py](file:///d:/tj/Graduation%20Project/开题报告/build_opening_report_doc.py)），挂载官方模板原生样式、通过 [omml_converter.py](file:///d:/tj/Graduation%20Project/.agents/skills/academic-doc-builder/scripts/omml_converter.py) 写入原生 OMML 数学公式与上标交叉引用，产出规范 `.docx` 文档。
   - **格式铁律（DOCX 优先）**：除用户明确要求外，所有毕设学术文档默认且仅生成 `.docx` 格式，不再自动调用 Word COM 另存为 `.doc`，以消除后台锁死、加快构建并防止排版降级。仅在用户明确要求或传入 `--doc` 时按需导出 `.doc`。
6. **第五步：生成修改对比版（当用户需要向导师展示修改痕迹时）**
   - 自动生成带有逐段差异高亮的对比文档并存放于 `归档/修改对比版/`（如 `归档/修改对比版/*-新旧版本修改对比版_逐段差异高亮.docx`），而**正式提交版必须确保全篇清除所有高亮（`HighlightColorIndex = 0`）**。
7. **第六步：Git 里程碑版本提交与 `PROJECT_STATUS.md` 同步**
   - 文档与脚本自检验证通过后，同步更新根目录 [PROJECT_STATUS.md](file:///d:/tj/Graduation%20Project/PROJECT_STATUS.md) 台账，并在终端执行 `git add` 与清晰规范的 Git Commit（如 `git commit -m "docs: 更新开题报告..."`），固化阶段成果。

---

## 三、 学校官方模板原生 XML 样式映射与分阶段排版参数规范

> [!IMPORTANT]
> **分阶段隔离原则**：同济大学本科毕设的**《任务书 / 开题报告》（小四号正文、1.5倍行距）**与**《毕业论文最终正稿》（五号正文、固定值18磅行距，见 `D:\tj\模板\带学院.doc`）**采用两套不同的字号与行距体系，严禁混用，且严禁套用研究生学位论文（20磅行距）参数。

### 3.1 《任务书》与《开题报告》官方模板排版参数表
经拆解官方模板 [1毕业设计(论文)任务书.docx](file:///d:/tj/Graduation%20Project/模板/1毕业设计(论文)任务书.docx) 与 [2毕业设计(论文)开题报告.docx](file:///d:/tj/Graduation%20Project/模板/2毕业设计(论文)开题报告.docx) 的 `styles.xml` 与 `document.xml`，所有通过 `python-docx` 生成的任务书/开题报告必须严格执行以下参数（**核心铁律：① 封面填写格必须保持 `vAlign="bottom"` 靠底贴线对齐，严禁设为垂直居中；② 仅一/二级标题保留段前段后 0.5 行间距，正文段落与参考文献严禁添加段前段后间距！**）：

| 样式类别 | 挂载模板样式名 (`styleId`) | 中文字体 (`w:eastAsia`) | 西文/数字字体 (`w:ascii`/`w:hAnsi`) | 字号 (`Pt`) | 对齐与缩进 | 行距与段间距 (`w:spacing`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **封面信息表格 (`Table 0`)** | `Normal` (`a`) | 宋体 | Times New Roman | **四号 (`14.0 pt` / `sz=28`)** | **单元格垂直靠底对齐 (`vAlign="bottom"`)**，段落水平居中，无缩进 | **单倍行距 (`12.0 pt`)，段前 0 磅，段后 0 磅（严禁覆写 `<w:spacing>` 或设为 `center`）** |
| **一级标题 (`h1`)** | `Normal` (`a`) | 黑体 | Times New Roman | 四号 (`14.0 pt` / `sz=28`) | 两端对齐，首行缩进 2 字符 (`w:firstLine="560"`) | 1.5 倍行距 (`w:line="360"`), **段前 0.5 行 (`beforeLines="50"`), 段后 0.5 行 (`afterLines="50"`)** |
| **二级标题 (`h2`)** | `条` (`a6`) | 黑体 | Times New Roman | 小四 (`12.0 pt` / `sz=24`) | **顶格无缩进** (`firstLine="0"`), 序号与题名空一格（如 `1． 课题来源...`） | 1.5 倍行距 (`w:line="360"`), **段前 0.5 行 (`beforeLines="50"`), 段后 0.5 行 (`afterLines="50"`)** |
| **三级标题 (`h3`)** | `正文格式` (`a7`) | 黑体 | Times New Roman | 小四 (`12.0 pt` / `sz=24`) | 两端对齐，首行缩进 2 字符 (`w:firstLine="480"`) | 1.5 倍行距 (`w:line="360"`), **段前 0 行，段后 0 行** |
| **正文段落 (`body`)** | `正文格式` (`a7`) | 宋体 | Times New Roman | 小四 (`12.0 pt` / `sz=24`) | 两端对齐，首行缩进 2 字符 (`w:firstLine="480"` / `firstLineChars="200"`) | 1.5 倍行距 (`w:line="360"`), **段前 0 行，段后 0 行（严禁加段间距）** |
| **独立公式 (`formula`)** | `正文格式` (`a7`) | Cambria Math | Cambria Math | 小四 (`12.0 pt` / `sz=24`) | 居中对齐，无缩进，右侧制表位右对齐公式编号 `（1）` | 1.5 倍行距 (`w:line="360"`), 段前 0 行，段后 0 行 |
| **图题 / 表题 (`caption`)** | `Normal` (`a`) | 宋体（加粗） | Times New Roman | 五号 (`10.5 pt` / `sz=21`) | 居中对齐，无缩进 | 1.5 倍行距，图前 0.5 行，图题后 0.5 行 |
| **正文数据表格内容** | `Normal` (`a`) | 表头黑体 / 内容宋体 | Times New Roman | 五号 (`10.5 pt`) 或 `9.5 pt` | 垂直居中；表头/序号居中，长文本居左；首行开启 `<w:tblHeader/>` | 1.2 倍行距，段前 2pt，段后 2pt |
| **参考文献 (`ref`)** | `参考文献` (`a9`) | 宋体 | Times New Roman | 小四 (`12.0 pt` / `sz=24`) | 两端对齐，**悬挂缩进 `0.74 cm`** (`w:left="420" w:hanging="420"`) | 1.5 倍行距 (`w:line="360"`), **段前 0 行，段后 0 行（严禁加段间距）** |

---

### 3.2 本科《毕业论文（最终正稿）》专属排版参数表（源自 `D:\tj\模板\带学院.doc` 47 条官方批注）
当进入毕业论文最终正稿撰写阶段时，严格切换至以下同济大学本科毕业论文正稿标准（与 22 级学长答辩终稿 `毕业论文_V5.docx` 完全一致）：

| 论文结构要素 | 字体要求（中 / 英） | 字号 (`Pt`) | 对齐、缩进与分页要求 | 行距与段间距 |
| :--- | :--- | :--- | :--- | :--- |
| **中/英文论文题目（摘要页上方）** | 中文黑体加粗 / 英文 Times New Roman 加粗 | 小二号 (`18.0 pt`) | 居中，上下各空一行，英文题目页另起一页 | 固定值 18 磅，段前 0.5 行，段后 0.5 行 |
| **中文摘要与英文 ABSTRACT 标题** | 中文黑体（`摘 要` 中间空一格）/ 英文 Times New Roman | 四号 (`14.0 pt`) | 居中 | 固定值 18 磅，段前 0.5 行，段后 0.5 行 |
| **中/英文摘要正文与关键词** | 中文宋体 / 英文 Times New Roman | 五号 (`10.5 pt`) | 首行缩进 2 字符；摘要约 300 字；与关键词之间空一行；`关键词：` / `Key words：` 加粗，3～5 个词逗号分隔，末尾无标点 | 固定值 18 磅，段前 0 行，段后 0 行 |
| **目录（`目 录`）** | 标题黑体四号 / 内容宋体五号（英文 Times New Roman） | 四号 / 五号 | 换页，上下各空一行，`目 录` 中间空 1 格居中 | 标题 18 磅（段前段后 0.5 行）；目录项单倍行距 |
| **一级标题（各章标题，如 `1  引 言`）** | 黑体 / Times New Roman | 四号 (`14.0 pt`) | **每章另起一页**，上下各空一行；居中（章末位数字后不加点，空两格写章名） | 固定值 18 磅 (`w:line="360" exact`)，段前 0.5 行，段后 0.5 行 |
| **二级标题（如 `1.1 ...`）** | 黑体 / Times New Roman | 五号 (`10.5 pt`) | **顶格书写**，序号与题名之间空 1 格 | 固定值 18 磅，段前 0.5 行，段后 0.5 行 |
| **三级标题（如 `1.1.1 ...`）** | 黑体 / Times New Roman | 五号 (`10.5 pt`) | **首行缩进 2 个汉字符**书写序号，序号与题名之间空 1 格 | 固定值 18 磅，段前 0.5 行，段后 0.5 行 |
| **三级以下占行标题（`A. ...` / `a. ...`）** | 黑体 / Times New Roman | 五号 (`10.5 pt`) | 首行缩进 2 个汉字符，序号与题名之间空 1 格 | 固定值 18 磅，段前 0 行，段后 0 行 |
| **论文正文段落、谢辞正文** | 宋体 / Times New Roman | 五号 (`10.5 pt`) | 两端对齐，首行左缩进 2 个汉字符 | **固定值 18 磅**，段前 0 行，段后 0 行 |
| **独立公式** | 原生 OMML (`Cambria Math` / Times New Roman) | 五号 (`10.5 pt`) | 公式居中，按章编号如 `（2.1）` 右对齐，公式与编号间不加虚线 | **1.5 倍行距**，段前 0 行，段后 0 行 |
| **表题、续表注与表内文字** | 宋体 / Times New Roman | **小五号 (`9.0 pt`)** | 三线表两端与页面对齐，上下与正文各空一行；表题（如 `表4.4 草酸...`）居中置于表上方；跨页省略原表题、重写表头并在右上方注 `续表X.X`（右空 2 格） | 固定值 18 磅，段前 0 行，段后 0 行 |
| **插图、图中文字与图题** | 宋体 / Times New Roman | **小五号 (`9.0 pt`)** | 图居中，上下与正文各空一行；图题（如 `图4.1 ...`）居中置于图下方 | 图中文字 1 倍行距；图题固定值 18 磅，段前段后 0 行 |
| **参考文献列表** | 宋体 / Times New Roman | 五号 (`10.5 pt`) | 标题按一级标题（换页、上下空一行、四号黑体居中、中间不空格）；条目序号加方括号 `[1]` | 固定值 18 磅，段前 0 行，段后 0 行 |

---

### 3.3 跨阶段通用书写、量与单位、公式图表及国标规范（`GB/T 7714` / `15834` / `15835`）
以下 7 条规范在《任务书》、《开题报告》、《中期报告》与《毕业论文正稿》中**完全无冲突且全程强制执行**：

1. **物理量斜体与复合单位单斜杠铁律（`带学院.doc` Shape 19, 29）**：
   - 计算式及正文中涉及的物理量标量一律为**斜体**（pH 例外），矢量与矩阵为**粗斜体**；国际单位符号（如 $\text{m}, \text{s}, \text{N}, \text{rad}, \text{Hz}$）、化学元素符号、数学算子与记号（$\text{d}, \sin, \min, \max, \text{RB}$）无例外一律为**正体**，数值与单位间留适当间隙。
   - **严禁双斜杠 `/`**：物理量及表格列头单位后**不允许出现两次“/”**（如严禁写 `m/s/s`），第二次出现的“/”必须用**负幂次（如 $\text{m}\cdot\text{s}^{-2}$、$\text{mol}\cdot\text{L}^{-1}$）**或括号表示。
2. **公式连续编号与不重编规则（Shape 19）**：
   - 公式序号必须连续，不得重复或跳缺；**重复引用的公式直接写“由式（X）可知”，不得另编新序号**；公式与右对齐序号之间**严禁加虚线引导符**；公式下方参数释义以“式中，”或“式（X.X）中，”领起，各分项用分号“；”隔开。
3. **图表先见文后见图与自明性规则（Shape 21~25 & 指南 3.4）**：
   - 必须**先见相应引导文字（如“如图 1 所示”、“见表 1”），后见图/表**，切忌图、表与文字表述简单重复；
   - 表序与表题置于**表上方居中**，图序与图题置于**图下方居中**，序号与题名间空 1 格，**题名末尾不加任何标点**；所有数据表格首行必须写入 `<w:tblHeader/>` 以支持跨页自动重复表头。
4. **层次标题排比性与段内序号层次（Shape 20, 26, 27 & 指南 3.2）**：
   - 同级标题尽量保持词组结构排比；章节序号末位数字后不加点号；
   - 段落号采用 `（1）…`、`（2）…` 或 `1）…`、`2）…`；段内分项采用 `①…；②…；③…。`。
5. **参考文献完整刊名与卷期省略规则（Shape 39, 40 & `GB/T 7714—2015`）**：
   - 所有引用的中外文期刊**必须写出完整刊名**；期刊若只有期没有卷，可省略卷号（如 `2000(2): 5-8`）；若只有卷没有（或不分）期，可省略期号（如 `2013, 60: 81-94`）。
6. **关键词标点规则（Shape 07, 12）**：
   - 关键词 3～5 个，中文用全角逗号分隔，英文用半角逗号加一空格分隔，**最后一个关键词后面不加任何标点符号**。
7. **数字与标点国标细节（`GB/T 15834-2011` & `GB/T 15835-2011`）**：
   - 同篇文档内的数值/周次范围连接符保持统一（如统一使用 `~` 或 `～`）；概数连用（如“三四个”）中间不加顿号；并列引号或书名号之间不加顿号。

---

## 四、 Word 原生数学公式（OMML）渲染规范与转换工具

**严禁使用图片（PNG/JPG）或粗糙的纯文本 Unicode 拼接（如 `η̇`、`M̂`、`ℝ⁶`）代替数学公式。** 毕业论文全流程必须使用 OpenXML Math（`xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"`）构造原生公式对象：

1. **自动化转换引擎（推荐）**：
   - 使用本项目内置封装的转换脚本：[`omml_converter.py`](./scripts/omml_converter.py)
   - 转换链路：标准 LaTeX 语法 $\rightarrow$ MathML (`latex2mathml`) $\rightarrow$ OMML (`MML2OMML.XSL` 位于 `C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL`) $\rightarrow$ python-docx 原生公式节点。
   - 使用示例：
     ```python
     from omml_converter import append_omml_formula
     # 独行居中公式
     append_omml_formula(paragraph, r"\dot{\boldsymbol{\eta}} = \boldsymbol{J}(\boldsymbol{\eta})\boldsymbol{\nu}", is_display=True)
     # 行内公式
     append_omml_formula(paragraph, r"\boldsymbol{\tau}_c \in \mathbb{R}^6", is_display=False)
     ```
2. **独立公式行（Displayed Equations）**：
   - 使用 `<m:oMathPara><m:oMath>...</m:oMath></m:oMathPara>` 嵌入公式段落，并在行末标注标准右对齐或居中公式编号 `（1）`、`（2）`。
3. **行内数学符号（Inline Math）**：
   - 正文中的矢量、矩阵、上下标与集合表达式（如 $\boldsymbol{\eta} = [x, y, z, \phi, \theta, \psi]^T$、$\boldsymbol{M} = \boldsymbol{M}_{RB} + \boldsymbol{M}_A$、$\boldsymbol{\tau}_c \in \mathbb{R}^6$、$6 \times 8$、$\boldsymbol{T}_{\min} \le \boldsymbol{T} \le \boldsymbol{T}_{\max}$、$\boldsymbol{e}_{\tau} = \boldsymbol{\tau}_c - \boldsymbol{B}\boldsymbol{T}$）均使用内联 `<m:oMath>` 节点嵌入段落 `<w:p>`。
4. **OMML 数学字体与字形规范**：
   - 公式字体统一绑定 `Cambria Math`，字号小四（`w:sz w:val="24"`）；
   - 矩阵与矢量（如 $\boldsymbol{\eta}, \boldsymbol{\nu}, \boldsymbol{J}, \boldsymbol{M}, \boldsymbol{C}, \boldsymbol{D}, \boldsymbol{g}, \boldsymbol{\tau}, \boldsymbol{B}, \boldsymbol{T}, \boldsymbol{e}, \boldsymbol{\theta}, \boldsymbol{r}, \boldsymbol{d}$）设置 `<m:sty m:val="bi"/>`（粗斜体 Bold-Italic）；
   - 标量变量（如 $x, y, z, \phi, \theta, \psi, u, v, w, p, q, r, i$）设置 `<m:sty m:val="i"/>`（斜体 Italic）；
   - 算子、括号、数字与描述性下标（如 $\text{RB}, \text{min}, \text{max}, \text{model}, \text{fb}, [, ], (, ), +, -, =, \le, \times$）设置 `<m:sty m:val="p"/>`（正体 Plain Roman）；
   - 导数点号（如 $\dot{\boldsymbol{\eta}}, \dot{\boldsymbol{\nu}}$）与估计帽号（如 $\hat{\boldsymbol{M}}, \hat{\boldsymbol{C}}, \hat{\boldsymbol{D}}, \hat{\boldsymbol{g}}$）使用 `<m:acc>` 顶标结构渲染。
5. **学长全过程经验对照基准**：
   - 撰写报告、大论文或答辩 PPT 时，必须参考 [学长毕设全过程资料深度解析与演进避坑指南.md](file:///d:/tj/Graduation%20Project/参考/学长毕设全过程资料深度解析与演进避坑指南.md)（解析了学长论文 V5 中 186 个原生 OMML 公式及开题 V1~V5 的演进避坑点）。

---

## 五、 参考文献管理与 Word 交叉引用上标规范（Zotero / EndNote 双轨协同）

1. **顺序编码自动校验**：
   - 构建脚本在生成文档时，自动扫描正文中所有引用角标 `[n]` 或 `[n, m]`，校验其首次出现顺序是否严格为 `1, 2, ..., N` 递增，杜绝跳号或乱序。
2. **Word 原生书签与上标跳转**：
   - 在“三、毕业论文的主要参考文献”部分，为每一条文献 `[i]` 写入原生 Word 书签 `<w:bookmarkStart w:id="..." w:name="_Ref_Paper_i"/>...<w:bookmarkEnd w:id="..."/>`。
   - 在正文中解析 `[1]`、`[1, 8]` 等引用标记，自动将其转换为带 `<w:vertAlign w:val="superscript"/>`（**上标**）且带内部书签锚点（`w:anchor="_Ref_Paper_i"`）的跳转节点（当作为句子名词成分如“文献[1]”时可保持平齐，句末或作者后引用一律设为上标 $^{[1]}$）。
3. **双格式题录库维护**：
   - 每次新增或调整参考文献时，必须同步维护同目录下的 `references.bib`（BibTeX）与 `references.ris`（EndNote / Zotero 通用 RIS 格式）。

---

## 六、 Word 自动化操作四大安全红线（防崩表、防乱码）

1. **严禁抛弃学校模板从零 `docx.Document()` 裸建文档**：
   - 必须以 `模板/` 目录下的学校官方模板（如 [1毕业设计(论文)任务书.docx](file:///d:/tj/Graduation%20Project/模板/1毕业设计(论文)任务书.docx)、[2毕业设计(论文)开题报告.docx](file:///d:/tj/Graduation%20Project/模板/2毕业设计(论文)开题报告.docx)）或已定稿文档为基底打开，定位到目标锚点段落（如审核意见表前）使用 `insert_paragraph_before` 或 `addprevious` 插入内容，确保封面、页眉页脚、装订线和教务审核表 100% 原样保留。
2. **修改前自动备份（`.bak`）与进程锁检查**：
   - 对已有的 `.doc` / `.docx` 执行原地修改前，先检查是否有残留 `WINWORD.EXE` 锁死目标文件，并在 `try...finally` 中确保 `word.Quit()` 被可靠调用。
3. **`win32com` 修改单元格/段落文本时必须执行 `Range.End - 1` 切片保护**：
   - 在 Word COM 中，表格单元格末尾包含特殊结束符 `\r\x07`，普通段落末尾包含 `\r`。直接对 `cell.Range.Text` 赋值会覆盖单元格结束符导致整张表格结构损坏！务必使用 `doc.Range(cell.Range.Start, cell.Range.End - 1)`。
4. **中西文字体必须同时绑定 XML 属性**：
   - 必须使用 `set_run_font()` 同时设置 `w:ascii`、`w:hAnsi`、`w:cs` 为 `"Times New Roman"`，并设置 `w:eastAsia` 为 `"宋体"` 或 `"黑体"`。

---

## 七、 验证与自检清单（Validation Steps）

每次生成或修改完 Word 文档后，Agent 必须执行以下验证步骤才算完成任务：
1. 运行读取校验脚本，检查生成的 `.docx` 和 `.doc` 文件是否存在且字节数正常。
2. 用脚本遍历检查生成的文档段落与表格，确认：
   - 正文与参考文献段落的 `beforeLines` 和 `afterLines` 均为 `None` / `0`（仅标题保留段前段后 0.5 行）；
   - 正文中的文献引用编号 `[1] ~ [N]` 顺序严格递增、全部已设为上标（`superscript`）且与文末参考文献一一对应；
   - 公式已渲染为原生 `<m:oMath>` / `<m:oMathPara>` 节点；
   - 课题名称、学院、姓名、学号、进度表 12 个阶段时间节点与最新任务书完全一致；
   - 正式版文档所有段落的 `HighlightColorIndex == 0`（无残留高亮）。
