# 毕业设计项目全局规则 (AGENTS.md)

## 1. 课题基本信息与核心定位

- **课题名称**：《基于PX4的水下航行器模型控制方法研究》
  - **任务书关联全称**：《基于PX4的水下航行器动力学建模、系统辨识、运动控制与推力分配研究》
- **学院与专业**：机械工程与机器人学院 · 机械设计制造及其自动化（本科毕业论文）
- **研究对象**：实验室已有的**八推进器便携式/微小型水下航行器（SwiftROV / Compact ROV）**实验平台（双耐压舱紧凑构型，绝非开架式；空间对称与矢量倾斜布置的 8 推进器过驱动冗余构型）。
- **核心研究任务定位（动态考量与联动论证中）**：
  - 围绕水下复杂环境下的动力学建模、运动控制与控制分配等主干任务，结合 PX4/SITL 闭环仿真与水池实验进行系统验证；
  - 各任务模块的边界、权重与表述重心处于深入考量与动态论证中，保持学术开放性，绝不僵化锁死。

---

## 2. 学术表述基调与红线（导师审阅核心规范）

1. **构型定性铁律（严禁再写“开架式”）**：
   - 实验室机器人为双圆柱耐压舱、碳纤维夹板紧凑集成的便携式水下航行器（SwiftROV），**严禁出现“开架式 (Open-frame)”**表述。
2. **立项逻辑与研究意义铁律（严禁大作业/做项目思维）**：
   - 毕业论文的研究意义必须立足于**“该类装备在特定恶劣场景下面临的客观物理矛盾与行业共性瓶颈”**（如深水非线性流扰、水下姿态失稳等）。
   - 实验室已有样机（SwiftROV）仅作为后文方案验证的**物理实验载体**，**严禁在背景与意义中将“为实验室已有平台提供控制系统/基座”作为立项原因或核心研究意义**。
3. **保持方案开放性与比选空间**：
   - 保持研究方案与技术路线的学术开放性与合理比选余地，严禁在前期过早写死排他性的狭窄算法，严禁在全局规则中僵化限定具体数学形式或技术实现细节。
4. **文体与通用规范**：
   - 毕业设计类型统一规范为：**毕业论文**（非“毕业设计”）；学术表述保持客观严谨，专业术语遵循国家标准与学术界公认规范。
5. **旧版开题报告全量作废与物理隔离铁律（严禁沿袭旧版）**：
   - 2026/09/30 之前撰写的旧版开题报告草稿与代码因存在严重的“大作业思维、缺乏外部恶劣场景物理驱动、提前剧透算法与公式”等问题，已被导师批评并全量推倒重来；
   - 旧版所有相关 Markdown 草稿（`开题报告_全文草稿.md` 等）、生成脚本（`build_opening_report_doc.py`）及历史 `.docx` 文件已全量物理移出至仓库外部 `D:\tj\Graduation_Project_旧版开题作废备份_20260930\`；
   - **严禁任何 Agent 读取、恢复、全局搜索或沿用旧版开题报告中的任何段落与表述！**
   - 开题报告的章节功能与组织框架参考 [docs/contracts/opening_report_contracts_and_evidence.md](file:///d:/tj/Graduation%20Project/docs/contracts/opening_report_contracts_and_evidence.md) 章节契约规范，直接向学校官方空白模板 [模板/2毕业设计(论文)开题报告.docx](file:///d:/tj/Graduation%20Project/模板/2毕业设计(论文)开题报告.docx) 从零撰写；契约中涉及的具体算法与技术方案仅供参考，尚未最终锁定，不得将未决假设作为既定研究决定。
6. **任务书定位铁律（仅作前期参考，绝非死板基准）**：
   - 任务书文件（[基于PX4的水下航行器模型控制方法研究.docx](file:///d:/tj/Graduation%20Project/开题报告/基于PX4的水下航行器模型控制方法研究.docx)）目前仅作为前期参考工作底稿，**绝非不可更改的死板基准**；
   - 毕业论文的核心研究任务、模块边界与重心仍处于重新审视与深入考量中；
   - 后续随着核心物理矛盾与科学价值的确定，任务书与开题报告保持双向联动修订，**严禁将任务书历史文字作为限制开题论述或技术推演的僵化约束**！

---

## 3. 工作区目录结构与工程环境约定

- `模板/`：存放学校官方下发的原始空白 `.doc` / `.docx` 模板文件（**只读基准，严禁直接覆盖修改**）。
- `参考/`：往届优秀任务书与相关参考文档（只读参考）。
- `选题/`：课题筛选记录及 [PX4与ArduSub对比分析.md](file:///d:/tj/Graduation%20Project/选题/PX4与ArduSub对比分析.md) 深度调研报告。
- `开题报告/`：仅存放前期参考任务书工作底稿（[基于PX4的水下航行器模型控制方法研究.docx](file:///d:/tj/Graduation%20Project/开题报告/基于PX4的水下航行器模型控制方法研究.docx)，仅作参考，可随时联动修改）、配图素材（`figures/`）、参考文献源文件（`references.bib`/`references.ris`）以及当前正在基于官方模板从零全新撰写的开题报告。旧版全量草稿、历史版本及生成脚本已全量移出至项目外 `D:\tj\Graduation_Project_旧版开题作废备份_20260930`，严禁任何 Agent 读取！
- `资料/`：按课题主干清晰划分为 4 大主题专题库（`01_海洋航行器机理建模与理论基础/`、`02_水动力参数辨识与数据驱动建模/`、`03_先进运动控制与动态补偿/`、`04_控制分配与水下传感实验/`）及 Markdown 源码归档库 `md/`；
  - **主题分类纯净 PDF 铁律**：4 大主题目录下仅存放纯净权威的 PDF 文档（英文原版、中文全译版、中英双语对照版 PDF）及必要图表，**严禁散落存放任何 Markdown 文档**；
  - **Markdown 统一归档铁律**：所有文献生成的中文全译、精读导读、双语对照等 Markdown 源码一律且仅存放在 `资料/md/` 统一收纳管理；
  - 双语文献 Web 精读阅读器及翻译资产已独立归档至远程私有仓库 [Eternity-burial/rov-paper-reader](https://github.com/Eternity-burial/rov-paper-reader)。
- `PX4_INDI_Research/`：前期 PX4 架构调研、INDI 嵌入式 C++ 原型代码与 Python 离线仿真实验。

### Windows / PowerShell 与 Python 执行铁律
1. **终端 UTF-8 编码保护**：在 PowerShell 中执行含中文路径或输出的命令时，开头务必加上 `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8;`；在所有 Python 脚本头部必须声明 `# -*- coding: utf-8 -*-` 并调用 `sys.stdout.reconfigure(encoding="utf-8")`。
2. **Word 进程锁检查**：在运行任何 `python-docx` 写入或 `win32com`（`Word.Application`）自动化脚本前，若遇到文件占用或 COM 异常，需先检查是否存在残留锁死进程（如 `~$*.doc` 临时文件或后台 `WINWORD.EXE`），并在 `try...finally` 块中确保 `word.Quit()` 被可靠调用。
3. **文档格式铁律（DOCX 优先与归档准则）**：除用户明确要求外，所有毕设学术文档（任务书、开题报告、中期检查、毕业论文等）**默认且仅生成 `.docx` 格式**，不再自动调用 Word COM 接口将 `.docx` 另存为 `.doc`。旧的 `.doc` 文件统一归档至 `开题报告/归档/历史DOC版本/`；当前轮次的修改对比版 `.docx` 保留在工作区根目录供审阅，之后每次迭代产生新对比版前，上一轮旧对比版打上时间戳快照移入 `开题报告/归档/历次修改对比版/` 并在台账中记录。

---

## 4. Git 版本控制与数据安全红线（防覆盖、防丢失）

项目已建立完整的 Git 本地版本控制仓库，Agent 与开发者必须严格执行以下版本纪律：

1. **写前检查与防盲改铁律（Safety First）**：
   - 在运行任何全量生成或改写 Word 文档（`.doc`/`.docx`）、Python 脚本或 C++ 代码前，必须先在终端执行 `git status --short` 检查当前工作区是否有未暂存的用户手工编辑；
   - 若检测到目标文件存在用户修改，**严禁静默覆盖**，必须先提示用户或将其单独另存为快照（如 `*_用户修改备份.*`）；
   - 所有自动化写操作必须保留 `.bak` 备份机制。
2. **里程碑及时提交（Commit Early & Often）**：
   - 每当完成一节论文撰写、通过一次重要仿真验证、排版完一个官方表格或完成重要重构后，必须主动执行有意义的 `git commit`（推荐使用 Conventional Commits 格式，如 `feat:`, `fix:`, `docs:`, `style:`）；
   - 禁止长时间积累大量未提交改动。
3. **环境与编码配置守则**：
   - 仓库根目录严格维护 [.gitignore](file:///d:/tj/Graduation%20Project/.gitignore)，禁止将 Office 临时锁死文件（`~$*`、`*.wbk`、`*.asd`）、Python 编译缓存（`__pycache__/`）及 >50MB 的非关键压缩包提交入库；
   - 保持 `git config core.quotepath false`，确保 Windows 终端下所有中文路径清晰可读；
   - 保持 `git config core.autocrlf false`，防止多平台换行符意外变动引发大面积无意义 diff。

---

## 5. 项目全流程运行与协同总规范（含跨对话记忆与科研质量门禁）

为确保毕业论文高质高效推进，日常开发与写作遵循以下统一闭环：

1. **跨对话持久化记忆（Planning with Files 铁律）**：
   - 根目录维护双轨台账：[PROJECT_NOW.md](file:///d:/tj/Graduation%20Project/PROJECT_NOW.md)（当前工作状态与极速恢复入口）与 [PROJECT_STATUS.md](file:///d:/tj/Graduation%20Project/PROJECT_STATUS.md)（历史里程碑与演进总控台账）；
   - **新窗口必读**：开启新对话推进学术任务时，严格遵循 [.agents/rules/academic-entry.md](file:///d:/tj/Graduation%20Project/.agents/rules/academic-entry.md)，优先查阅 `PROJECT_NOW.md` 恢复当前上下文；需要追溯历史演进或重大里程碑时按需查阅 `PROJECT_STATUS.md`；
   - **状态同步更新**：每完成一项任务，优先在 `PROJECT_NOW.md` 记录交接；达成重大阶段里程碑时同步更新 `PROJECT_STATUS.md`。
2. **学术文档两阶段推导推进规范（先定边界，再定细节）**：
   - 撰写学术章节时，必须遵守以下四步递进工作法，严禁在未理清边界时盲目堆砌具体内容：
     1. **文献与证据先行**：必须先检索中英文权威文献，以扎实的物理与工程证据驱动论述，不凭空捏造；
     2. **对比优秀范文**：深入剖析本组已获导师认可的标杆开题（如郑祺耀优秀开题范式），吸收其段落结构与论证范式；
     3. **先界定元规则（性质边界）**：明确该部分“是写什么性质的内容，坚决不是写什么（准入与禁区）”；
     4. **再推导具体细节**：在元规则框架锁定后，再深入讨论并确认具体场景、具体方法与具体参数。
3. **学术严谨性、去 AI 腔与证据门控**：
   - 始终对标 [学长毕设全过程资料深度解析与演进避坑指南.md](file:///d:/tj/Graduation%20Project/参考/学长毕设全过程资料深度解析与演进避坑指南.md) 与专属写作技能 [.agents/skills/academic-writing/SKILL.md](file:///d:/tj/Graduation%20Project/.agents/skills/academic-writing/SKILL.md)，保持学术语言克制、禁用破折号连接分句与浮夸词汇，严守 L0~L4 证据门控纪律（严禁编造实验数据与未核实引文）；
4. **公式与图表规范**：
   - 所有 Word 公式必须通过 [omml_converter.py](file:///d:/tj/Graduation%20Project/.agents/skills/academic-doc-builder/scripts/omml_converter.py) 输出原生 OMML，严禁使用图片；
   - 仿真曲线采用颜色+线型双重编码（300 DPI），可编辑矢量框图通过 [drawio-skill](file:///d:/tj/Graduation%20Project/.agents/skills/drawio-skill/SKILL.md) / [drawio-reconstruction](file:///d:/tj/Graduation%20Project/.agents/skills/drawio-reconstruction/SKILL.md) 构建为 `.drawio` 文件，框架图设计遵循 [paper-framework-figure-studio-pro](file:///d:/tj/Graduation%20Project/.agents/skills/paper-framework-figure-studio-pro/SKILL.md)；
5. **参考文献规范**：严格遵守 GB/T 7714-2015 顺序编码制，正文首次引用递增，同步维护 `references.bib` 与 `references.ris`。
6. **文献双语化与研读规范**：外文文献全译与双语对照严格执行 [paper-translation-reader](file:///d:/tj/Graduation%20Project/.agents/skills/paper-translation-reader/SKILL.md) 五大铁律与双轨制流水线；严禁省略任何定理证明、子公式与推导步骤，交付前必须执行自动化公式比对门禁，确保差集为 0；**所有文献 Markdown 源码必须统一收纳于 `资料/md/`，各主题分类目录下仅保留纯净权威的 PDF 文档**。
