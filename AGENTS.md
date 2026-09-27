# 毕业设计项目全局规则 (AGENTS.md)

## 1. 课题基本信息与核心定位

- **课题名称**：《基于PX4的水下航行器模型控制方法研究》
  - **任务书关联全称**：《基于PX4的水下航行器动力学建模、系统辨识、运动控制与推力分配研究》
- **学院与专业**：机械工程与机器人学院 · 机械设计制造及其自动化（本科毕业论文）
- **研究对象**：实验室已有的**八推进器开架式水下航行器（Open-frame UUV/ROV）**实验平台（空间对称与矢量倾斜布置的过驱动冗余构型）。
- **核心研究链路（四阶段闭环）**：
  1. **平台梳理与六自由度建模**：依托已有八推进器平台，建立六自由度（6-DOF）运动学与动力学模型（刚体惯性、附加质量、科氏力与向心力、水动力阻尼、重浮力恢复作用）及必要的单推进器模型；
  2. **系统辨识与模型验证**：明确系统辨识输入输出关系，结合已有平台参数资料及相关数据开展关键未知水动力参数辨识，通过代表性动态响应进行模型基本验证并分析模型误差与适用范围；
  3. **运动控制与八推进器控制分配**：以经验证的航行器模型为基础，结合模型特性补偿与实时状态反馈设计闭环运动控制方法（姿态、深度、航向等），输出期望广义力与力矩；建立 $6 \times 8$ 八推进器控制分配矩阵，考虑推进器基本推力输出范围约束，将期望广义力/力矩分配为各推进器推力指令；
  4. **PX4/SITL 闭环仿真与系统验证**：基于 PX4 软件架构与 uORB 消息机制，在 SITL 环境中完成航行器模型、运动控制与八推进器控制分配模块的闭环集成，开展典型运动工况与适量外部扰动工况下的仿真验证与性能评价（跟踪误差、动态响应、控制分配误差）。

---

## 2. 学术表述基调与红线（导师审阅规范）

1. **稳健务实、留有方法比选余地**：
   - 在任务书、开题报告、中期及论文纲领性表述中，必须坚持**“机理建模与数据辨识相结合、模型信息与状态反馈相结合”**的稳健工程表述。
   - 运动控制统一表述为**“基于航行器模型和状态反馈的闭环运动控制”**，在后续具体章节和实验中可根据模型验证结果灵活展开模型前馈补偿、反馈线性化（FBL）、增量非线性动态逆（INDI）与经典 PID 的横向对比，**严禁在纲领性条款中把算法过早写死为单一窄门算法**。
2. **合理界定约束与工作量边界**：
   - 控制分配部分统一表述为**“考虑推进器基本推力输出范围，分析控制分配误差及推进器输出情况”**，避免在任务书/开题考核指标中包揽过多高难度硬件约束（如不要随意承诺复杂的电机推力变化率动态约束、硬件故障重构或真实水池极限特技试验）。
3. **术语统一规范**：
   - 毕业设计类型统一为：**毕业论文**（非“毕业设计”）。
   - 核心术语统一：六自由度（6-DOF）、北东地惯性坐标系（NED）、附体坐标系（Body-fixed Frame / FRD）、附加质量（Added Mass）、水动力阻尼（Hydrodynamic Damping）、恢复力与力矩（Restoring Forces and Moments）、广义控制力与力矩（Generalized Control Forces and Moments）、控制分配（Control Allocation）、软件在环仿真（SITL）。

---

## 3. 全局数学符号与坐标系规范（Fossen 6-DOF + PX4 标准）

所有学术文档（Markdown / Word）、Python 仿真脚本与 PX4 C++ 源码注释必须严格遵循以下符号与坐标系约定：

- **坐标系定义**：
  - **惯性系 $\{n\}$**：北-东-地（North-East-Down, **NED**）坐标系。
  - **附体系 $\{b\}$**：前-右-下（Forward-Right-Down, **FRD**）附体坐标系（与 PX4 机体坐标系严格一致）。
- **核心数学符号与代码变量映射**：
  - 广义位置与欧拉角姿态矢量：$\boldsymbol{\eta} = [x, y, z, \phi, \theta, \psi]^T \in \mathbb{R}^6$ （代码变量：`eta`）
  - 附体系线速度与角速度矢量：$\boldsymbol{\nu} = [u, v, w, p, q, r]^T \in \mathbb{R}^6$，对应纵荡（Surge $u$）、横荡（Sway $v$）、垂荡（Heave $w$）、横滚角速度（Roll rate $p$）、俯仰角速度（Pitch rate $q$）、偏航角速度（Yaw rate $r$）（代码变量：`nu`）
  - 运动学坐标转换矩阵：$\dot{\boldsymbol{\eta}} = \boldsymbol{J}(\boldsymbol{\eta})\boldsymbol{\nu}$ （代码变量：`J_eta`）
  - 动力学标准方程：
    $$\boldsymbol{M}\dot{\boldsymbol{\nu}} + \boldsymbol{C}(\boldsymbol{\nu})\boldsymbol{\nu} + \boldsymbol{D}(\boldsymbol{\nu})\boldsymbol{\nu} + \boldsymbol{g}(\boldsymbol{\eta}) = \boldsymbol{\tau} + \boldsymbol{\tau}_d$$
    - $\boldsymbol{M} = \boldsymbol{M}_{RB} + \boldsymbol{M}_A \in \mathbb{R}^{6 \times 6}$：刚体惯性矩阵与附加质量矩阵之和（代码变量：`M_total`, `M_RB`, `M_A`）
    - $\boldsymbol{C}(\boldsymbol{\nu}) = \boldsymbol{C}_{RB}(\boldsymbol{\nu}) + \boldsymbol{C}_A(\boldsymbol{\nu}) \in \mathbb{R}^{6 \times 6}$：科氏力与向心力矩阵（代码变量：`C_nu`）
    - $\boldsymbol{D}(\boldsymbol{\nu}) = \boldsymbol{D}_{\text{lin}} + \boldsymbol{D}_{\text{quad}}(\boldsymbol{\nu}) \in \mathbb{R}^{6 \times 6}$：线性与二次非线性水动力阻尼矩阵（代码变量：`D_nu`, `D_lin`, `D_quad`）
    - $\boldsymbol{g}(\boldsymbol{\eta}) \in \mathbb{R}^6$：重力与浮力恢复力/力矩矢量（代码变量：`g_eta`）
    - $\boldsymbol{\tau} \in \mathbb{R}^6$：实际作用于机体的广义推力与力矩矢量（代码变量：`tau`）
    - $\boldsymbol{\tau}_d \in \mathbb{R}^6$：外部水流等未知扰动力与力矩矢量（代码变量：`tau_d`）
  - 运动控制与八推进器控制分配：
    - 参考状态与误差：$\boldsymbol{\eta}_r, \boldsymbol{\nu}_r$，位置/姿态误差 $\boldsymbol{e}_{\eta} = \boldsymbol{\eta}_r - \boldsymbol{\eta}$，速度误差 $\boldsymbol{e}_{\nu} = \boldsymbol{\nu}_r - \boldsymbol{\nu}$（代码变量：`eta_ref`, `nu_ref`, `e_eta`, `e_nu`）
    - 期望广义控制力/力矩：$\boldsymbol{\tau}_c = [F_x, F_y, F_z, M_x, M_y, M_z]^T \in \mathbb{R}^6$（代码变量：`tau_c`）
    - 八推进器控制分配矩阵：$\boldsymbol{B} \in \mathbb{R}^{6 \times 8}$，由各推进器安装位置 $\boldsymbol{r}_i$ 与推力方向单位矢量 $\boldsymbol{d}_i$ 构造（代码变量：`B_alloc`）
    - 推进器推力指令矢量：$\boldsymbol{T} = [T_1, T_2, \dots, T_8]^T \in \mathbb{R}^8$，满足推力范围约束 $\boldsymbol{T}_{\min} \le \boldsymbol{T} \le \boldsymbol{T}_{\max}$（代码变量：`T_cmd`, `T_min`, `T_max`）
    - 控制分配残差矢量：$\boldsymbol{e}_{\tau} = \boldsymbol{\tau}_c - \boldsymbol{B}\boldsymbol{T} \in \mathbb{R}^6$（代码变量：`e_tau`）

---

## 4. 工作区目录结构与工程环境约定

- `模板/`：存放学校官方下发的原始空白 `.doc` / `.docx` 模板文件（**只读基准，严禁直接覆盖修改**）。
- `参考/`：往届优秀任务书与相关参考文档（只读参考）。
- `选题/`：课题筛选记录及 [PX4与ArduSub对比分析.md](file:///d:/tj/Graduation%20Project/选题/PX4与ArduSub对比分析.md) 深度调研报告。
- `开题报告/`：任务书定稿、开题报告全文草稿（[开题报告_全文草稿.md](file:///d:/tj/Graduation%20Project/开题报告/开题报告_全文草稿.md)）、高清架构图生成脚本（[generate_report_figures.py](file:///d:/tj/Graduation%20Project/开题报告/generate_report_figures.py)）及 Word 自动化生成脚本（[build_opening_report_doc.py](file:///d:/tj/Graduation%20Project/开题报告/build_opening_report_doc.py)）。
- `资料/`：核心英文文献 PDF（`01`~`05`）、中文全译 Markdown 及双语文献精读平台（[index.html](file:///d:/tj/Graduation%20Project/资料/index.html)、`js/data_paper*.js`、`master_vocab_cache.json`）。
- `PX4_INDI_Research/`：前期 PX4 架构调研、INDI 嵌入式 C++ 原型代码与 Python 离线仿真实验。

### Windows / PowerShell 与 Python 执行铁律
1. **终端 UTF-8 编码保护**：在 PowerShell 中执行含中文路径或输出的命令时，开头务必加上 `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8;`；在所有 Python 脚本头部必须声明 `# -*- coding: utf-8 -*-` 并调用 `sys.stdout.reconfigure(encoding="utf-8")`。
2. **Word 进程锁检查**：在运行任何 `python-docx` 写入或 `win32com`（`Word.Application`）自动化脚本前，若遇到文件占用或 COM 异常，需先检查是否存在残留锁死进程（如 `~$*.doc` 临时文件或后台 `WINWORD.EXE`），并在 `try...finally` 块中确保 `word.Quit()` 被可靠调用。

---

## 5. Git 版本控制与数据安全红线（防覆盖、防丢失）

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

## 6. 项目全流程运行与协同总规范

为确保毕业论文高质高效推进，日常开发与写作遵循以下统一闭环：

1. **学术严谨性**：始终对标 [学长毕设全过程资料深度解析与演进避坑指南.md](file:///d:/tj/Graduation%20Project/参考/学长毕设全过程资料深度解析与演进避坑指南.md)，保持学术语言克制，留有算法比选余地；
2. **公式规范**：所有 Word 公式必须通过 [omml_converter.py](file:///d:/tj/Graduation%20Project/.agents/skills/academic-doc-builder/scripts/omml_converter.py) 输出原生 OMML，严禁使用图片；
3. **参考文献规范**：严格遵守 GB/T 7714-2015 顺序编码制，正文首次引用递增，同步维护 `references.bib` 与 `references.ris`。

