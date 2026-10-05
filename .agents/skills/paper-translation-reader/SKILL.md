---
name: paper-translation-reader
description: >-
  Use this skill whenever the user asks to read, analyze, or translate English
  research papers (PDFs) in the 资料/ directory, generate full Chinese translation
  Markdown files, extract paper figures, or update the interactive bilingual
  literature reader web app (资料/index.html and 资料/js/data_paper*.js).
---

# 外文文献精读、中文全译与双语阅读器构建技能 (Paper Translation & Bilingual Reader Skill)

本技能规范了 `资料/` 目录下核心外文文献的精读解析、100% 完整中文全译 Markdown 生成，以及“毕业设计文献研读平台”（[index.html](file:///d:/tj/Graduation%20Project/资料/index.html)）的数据文件构建流程。

---

## 一、 外文文献全译五大铁律

1. **100% 完整全译（严禁漏段、严禁缩写）**：
   - 翻译外文论文时，必须从摘要、引言、数学建模、控制律设计、实验设置、结果讨论到结论**逐段逐句完整翻译**。
   - **严禁**因为篇幅长而擅自使用“（此处省略实验细节）”、“（公式推导略）”或将多句合并概括成一句话。
2. **数学公式 100% KaTeX 精确还原**：
   - 原文中的所有行内公式（`$...$`）与独立编号公式（`$$...$$`）必须完整还原，矢量/矩阵加粗符号（`\boldsymbol{...}` 或 `\mathbf{...}`）、上下标及正体算子保持严谨规范。
3. **零遗漏推导证明与公式校验门禁（Formula & Proof Zero-Loss Invariant）**：
   - 论文中的所有理论定理（Theorems）、引理（Lemmas）、注记（Remarks）、推导步骤（Proofs）以及中间公式展开必须 100% 完整呈现；
   - 交付前**必须执行自动化公式比对门禁**：编写 Python 脚本提取原文中所有公式编号集合（$1 \sim N$），比对译文中 `\tag{}` 编号集合，确保差集为 0；
   - 双语对照版页数必须与原文字量相匹配（通常为原文页数的 1.2 ~ 1.5 倍），严禁出现页数严重缩水或摘要概括化。
4. **专业术语强制统一**：
   - 翻译前必须查阅并遵守本技能目录下的标准术语表：[references/terminology.md](./references/terminology.md)，确保文献译稿中的专业词汇与开题报告、毕业论文正文完全一致。
5. **原图提取与图文对应**：
   - 使用 PyMuPDF (`fitz`) 从原版 PDF 中提取高清实验图与架构框图，统一存放于 `资料/images/paperX_figY_*.png` 或各专业目录，并在全译 Markdown 与双语阅读器对应章节中准确嵌入图片与中英双语图注。

---

## 二、 产出物标准与双轨排版技术流水线 (Dual-Track Pipeline)

每精读翻译一篇新文献（如 `资料/` 各子目录下的核心论文），标准产出为完整的**双语对照出版级文档集**：

### 1. 核心产出物三件套与目录归集规范
1. **统一 Markdown 源码归档（严禁散落在分类目录）**：
   - **存放路径**：所有文献生成的 Markdown 源码一律且仅存放在 **`资料/md/`** 单一归档文件夹中；
   - **双语对照 Markdown**：`资料/md/<编号>_<标题>_双语对照.md`，采用 `<div class="bilingual-box">` 容器（内部嵌套 `<div class="en-text"><strong>[EN]</strong> ...</div>` 与 `<div class="zh-text"><strong>[中文]</strong> ...</div>`）；
   - **中文全译精读 Markdown**：`资料/md/<编号>_<标题>_中文全译精读.md`，纯净学术中文单语版，公式、图表与定理完全一致。
2. **主题分类目录纯净 PDF 产出（用户查阅主视图）**：
   - **存放路径**：各主题分类子目录（`01_海洋航行器机理建模与理论基础/` 等）下**仅保留纯净权威的 PDF 文档与必要图表**，严禁散落存放任何 Markdown 文件；
   - **高保真矢量 PDF**：
     - `资料/<分类>/<编号>_<标题>_双语对照.pdf`：中英双语卡片并排，公式原生渲染，带有防分页撕裂保护；
     - `资料/<分类>/<编号>_<标题>_中文版.pdf`：中文紧凑精排单语版。

### 2. 双轨制排版技术流水线 (Dual-Track Pipeline)

针对不同技术历史时期的 PDF 源码特性，严格执行以下双轨分工，杜绝排版灾难：

- **Track A：现代原生双栏数字论文（如 IEEE/Elsevier 2015 之后的论文，如 Li 2025）**：
  - **适用特征**：现代排版软件生成，文本层未打散，坐标系标准；
  - **处理工具**：采用 `pdf2zh` 原位双栏替换引擎，自动化保留原文矢量图排版与双语分栏对照。
- **Track B：早期历史经典文献（如 1990 年代及更早的 TeX/DVI 论文，如 Fossen 1995）**：
  - **技术陷阱警示**：`dvipsk` 编译导致文字层被编码为 0.17 pt 微米级字体、单词按音节打散为独立文字块、负 Y 轴坐标颠倒，`pdf2zh` 会导致严重的错乱或排版灾难；
  - **处理管线**：
    1. **空间重构文本**：使用 PyMuPDF 获取单词坐标并按行高容差（y 轴容差 3 pt）排序，拼接恢复连贯文本；
    2. **逐段 1:1 双语卡片重构**：编写 Markdown，包含全部定理、证明、注记和所有公式编号（`\tag{1} ~ \tag{N}`）；
    3. **出版级 CSS 与分页防护**：强制为 `.bilingual-box`、`.theorem-box`、`.proof-box`、`table`、公式块注入 `page-break-inside: avoid;`，为各级标题注入 `page-break-after: avoid;`；
    4. **Headless Edge 矢量打印**：通过 Pandoc + MathJax 生成单文件 HTML，调用 `msedge --headless --print-to-pdf --virtual-time-budget=12000` 渲染高保真矢量 PDF。

### 3. 双语精读网页阅读器数据 (`资料/js/data_paper<X>.js`)
当需要将文献挂载到 Web 双语阅读平台（[index.html](file:///d:/tj/Graduation%20Project/资料/index.html)）时，构建对应数据文件：

#### `data_paper<X>.js` 标准 Schema：
```javascript
window.BISHE_DATA = window.BISHE_DATA || {};
window.BISHE_DATA['paperX'] = {
  "id": "paperX",
  "title": "English Paper Title",
  "chineseTitle": "中文准确译名",
  "authors": "Author 1, Author 2, ...",
  "journal": "IEEE ... (Year)",
  "venue": "研究机构中英文名称",
  "video": "https://...", // 可选
  "code": "https://...",  // 可选
  "overview": "200~300字论文核心导读：概括研究背景、核心方法突破、实验平台与关键定量实验指标对比。",
  "sections": [
    {
      "id": "sec-abstract",
      "sectionNumber": "摘要", // 或 "I", "II-A" 等
      "title": "ABSTRACT",
      "chineseTitle": "论文摘要 (Abstract)",
      "figure": { // 可选：若本节包含核心配图
        "image": "images/paperX_fig1_xxx.png",
        "alt": "Figure 1",
        "caption": "图 1：中英对照图注说明"
      },
      "paragraphs": [
        {
          "pIndex": 1,
          "logicRole": "本段在全文中的学术逻辑角色（如：传统模型控制局限性剖析）",
          "mainIdea": "一句话提炼本段核心主旨",
          "sentences": [
            {
              "sIndex": 1,
              "id": "P1-S1",
              "text": "Original English sentence with $math$ preserved.",
              "translation": "对应的中文精准翻译，保留 $math$ 公式。",
              "vocab": [
                {
                  "word": "dynamic inversion",
                  "ipa": "/daɪˈnæmɪk ɪnˈvɜːʃn/",
                  "meaning": "动态逆控制",
                  "level": "blue", // "blue": 专业术语, "red": 重点核心词, "green": 进阶学术词
                  "zh": "动态逆"   // 【关键】必须为 translation 字符串中完全匹配的中文子串，以激活双向联动高亮！
                }
              ]
            }
          ]
        }
      ]
    }
  ]
};
```

---

## 三、 双语阅读器词汇高亮与同步更新规范

1. **双向词汇高亮匹配规则（极其重要）**：
   - [reader_app.js](file:///d:/tj/Graduation%20Project/资料/js/reader_app.js#L131-L196) 中的 `renderAnnotatedChinese` 通过精确查找 `v.zh` 在 `s.translation` 中的子串位置来生成 `<span class="vocab-word trans-vocab-word ...">` 标签。
   - 因此，每个 `vocab` 词条的 `"zh"` 字段**必须是该句中文 `translation` 中原封不动出现的精确子串**！
   - 优先从 [master_vocab_cache.json](file:///d:/tj/Graduation%20Project/资料/master_vocab_cache.json) 中检索复用已有的音标（`ipa`）和释义（`meaning`），新增专业词汇同步补充。
2. **新增论文后的前端三处同步更新**：
   - 在 `资料/js/` 下生成 `data_paper<X>.js`；
   - 在 [index.html](file:///d:/tj/Graduation%20Project/资料/index.html#L38-L61) 的 `#paperNavList` 侧边栏中添加对应的 `.paper-nav-item` 卡片，并在底部添加 `<script src="js/data_paper<X>.js"></script>` 引用；
   - 检查并更新 [reader_app.js](file:///d:/tj/Graduation%20Project/资料/js/reader_app.js#L333-L338) 中的 `getPaperPdfLink(paperId)` 函数，确保其返回 `资料/` 目录下真实的 PDF 文件名（如 `01-en-...pdf` ~ `05-en-...pdf`）。

---

## 四、 文献深度综述与引文真伪核验协议（Deep Research & Citation Verification）
*(吸收自 `HKUSTDial/Supervisor-Skills/deep-research` 与 `ARS-Codex`)*

在为毕业论文“国内外研究现状”检索补充新文献或整理对比综述时，严格执行以下**两步核验与 MECE 综合法则**：

1. **引文两步真伪核验（零容忍编造引文）**：
   - **Step 1 存在性核验**：通过检索核实完整论文标题、第一作者姓氏、发表年份与期刊/会议名称；凡检索无果、仅靠模型记忆拼凑的条目一律定级为 `UNVERIFIABLE`，**严禁写入论文或 `.bib` 题录库**。
   - **Step 2 论点匹配度核验**：仅凭题目与摘要（L2/L3 证据）只能引用其研究方向与宏观结论，严禁凭空捏造其内部实验数值；只有本地 `资料/` 中已核实全文（L1 证据）的文献，方可引用其具体公式、参数与定量对比数据。
2. **MECE 分类综述框架（不堆砌流水账）**：
   - 严禁按“作者 A 做了 X；作者 B 做了 Y；作者 C 做了 Z”的机械罗列式写文献综述。
   - 必须围绕本课题主线按 **MECE（相互独立、完全穷尽）流派分类法** 组织（例如：① 水下航行器六自由度机理建模与参数辨识方法；② 非线性与基于模型的鲁棒运动控制方法；③ 过驱动水下机器人冗余推力分配与饱和处理；④ 基于开源飞控架构的水下控制系统实现），并在每类末尾自然引出**现有研究与本实验室八推进器平台需求之间的切入点（Gap）**。

