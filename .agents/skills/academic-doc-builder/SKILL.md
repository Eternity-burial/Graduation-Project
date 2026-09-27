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
3. **行文规范**：
   - 杜绝口语化与空洞套话，段落逻辑严密，数学符号与 [AGENTS.md](file:///d:/tj/Graduation%20Project/AGENTS.md) 中的 Fossen 6-DOF 符号体系 100% 保持一致。

---

## 二、 标准执行工作流（Markdown 草稿 + 题录库 + 双格式导出）

切勿在未对齐内容前直接盲改二进制 Word 文件，必须按以下五步推进：

1. **第一步：Markdown 草稿对齐**
   - 先在对应的 Markdown 草稿文件（如 [开题报告_全文草稿.md](file:///d:/tj/Graduation%20Project/开题报告/开题报告_全文草稿.md)）中完成文本、公式、表格与技术路线图的编写或修订。
2. **第二步：参考文献顺序校验与 `.bib` / `.ris` 题录库同步**
   - 按 GB/T 7714-2015 顺序编码制，严格依据文献在正文中**首次出现的先后顺序**编号 `[1] ~ [N]`，同步更新 [references.bib](file:///d:/tj/Graduation%20Project/开题报告/references.bib) 与 [references.ris](file:///d:/tj/Graduation%20Project/开题报告/references.ris)，支持一键导入本地 **Zotero**（`C:\Program Files\Zotero\zotero.exe`）或 **EndNote**。
3. **第三步：300 DPI 高清配图生成（如需更新配图）**
   - 使用 Python（Pillow / Matplotlib）脚本（参考 [generate_report_figures.py](file:///d:/tj/Graduation%20Project/开题报告/generate_report_figures.py)）生成 300 DPI 出版级白底高清 PNG 配图，严禁使用低分辨率截图。
4. **第四步：基于官方模板生成/更新 `.docx` 并同步转换 `.doc`**
   - 运行 Python 脚本（参考 [build_opening_report_doc.py](file:///d:/tj/Graduation%20Project/开题报告/build_opening_report_doc.py)），挂载官方模板原生样式、写入 OMML 数学公式与上标交叉引用，同时产出 `.docx` 与二进制 `.doc`（`FileFormat=0`）。
5. **第五步：生成修改对比版（当用户需要向导师展示修改痕迹时）**
   - 自动生成一份带有逐段差异高亮的对比文档（如 `*-新旧版本修改对比版_逐段差异高亮.doc` / `.docx`），而**正式提交版必须确保全篇清除所有高亮（`HighlightColorIndex = 0`）**。

---

## 三、 学校官方模板原生 XML 样式映射与排版参数规范

经拆解官方模板 [2毕业设计(论文)开题报告.docx](file:///d:/tj/Graduation%20Project/模板/2毕业设计(论文)开题报告.docx) 的 `styles.xml` 与 `document.xml`，所有通过 `python-docx` 生成的文档必须直接挂载模板内置样式并严格执行以下段落参数（**核心铁律：仅标题保留段前段后 0.5 行间距，正文段落与参考文献严禁添加段前段后间距！**）：

| 样式类别 | 挂载模板样式名 (`styleId`) | 中文字体 (`w:eastAsia`) | 西文/数字字体 (`w:ascii`/`w:hAnsi`) | 字号 (`Pt`) | 对齐与缩进 | 行距与段间距 (`w:spacing`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **一级标题 (`h1`)** | `Normal` (`a`) | 黑体 | Times New Roman | 四号 (`14.0 pt` / `sz=28`) | 两端对齐，首行缩进 2 字符 (`w:firstLine="560"`) | 1.5 倍行距 (`w:line="360"`), **段前 0.5 行 (`beforeLines="50"`), 段后 0.5 行 (`afterLines="50"`)** |
| **二级标题 (`h2`)** | `条` (`a6`) | 黑体 | Times New Roman | 小四 (`12.0 pt` / `sz=24`) | **顶格无缩进** (`firstLine="0"`), 序号与题名空一格（如 `1． 课题来源...`） | 1.5 倍行距 (`w:line="360"`), **段前 0.5 行 (`beforeLines="50"`), 段后 0.5 行 (`afterLines="50"`)** |
| **三级标题 (`h3`)** | `正文格式` (`a7`) | 黑体 | Times New Roman | 小四 (`12.0 pt` / `sz=24`) | 两端对齐，首行缩进 2 字符 (`w:firstLine="480"`) | 1.5 倍行距 (`w:line="360"`), **段前 0 行，段后 0 行** |
| **正文段落 (`body`)** | `正文格式` (`a7`) | 宋体 | Times New Roman | 小四 (`12.0 pt` / `sz=24`) | 两端对齐，首行缩进 2 字符 (`w:firstLine="480"` / `firstLineChars="200"`) | 1.5 倍行距 (`w:line="360"`), **段前 0 行，段后 0 行（严禁加段间距）** |
| **独立公式 (`formula`)** | `正文格式` (`a7`) | Cambria Math | Cambria Math | 小四 (`12.0 pt` / `sz=24`) | 居中对齐，无缩进，右侧制表位右对齐公式编号 `(1)` | 1.5 倍行距 (`w:line="360"`), 段前 0 行，段后 0 行 |
| **图题 / 表题 (`caption`)** | `Normal` (`a`) | 宋体（加粗） | Times New Roman | 五号 (`10.5 pt` / `sz=21`) | 居中对齐，无缩进 | 1.5 倍行距，图前 0.5 行，图题后 0.5 行 |
| **表格内容** | `Normal` (`a`) | 表头黑体 / 内容宋体 | Times New Roman | 五号 (`10.5 pt` / `sz=21`) | 垂直居中；表头/序号居中，长文本居左 | 1.25 倍行距，段前 2pt，段后 2pt |
| **参考文献 (`ref`)** | `参考文献` (`a9`) | 宋体 | Times New Roman | 小四 (`12.0 pt` / `sz=24`) | 两端对齐，**悬挂缩进 `0.74 cm`** (`w:left="420" w:hanging="420"`) | 1.5 倍行距 (`w:line="360"`), **段前 0 行，段后 0 行（严禁加段间距）** |

---

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
