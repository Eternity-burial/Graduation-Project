# Project Now

## 文件定位

本文件是新会话恢复工作状态的入口。

仅保留当前有效的信息，不记录完整历史流水账。

历史记录保存在 PROJECT_STATUS.md；需要追溯时再按需查阅。

## 当前工作阶段

当前重点：Antigravity 规则、Skills 与学术写作质量控制流程的搭建与维护。

当前暂缓：研究算法路线和具体技术方案的最终选择。

不得将最近讨论的候选路线自动升级为已确定方案。

## 当前有效来源

- AGENTS.md：工作区硬约束与安全规则。
- .agents/rules/academic-entry.md：学术任务接入网关规则。
- docs/PROJECT_FACTS.md：当前有效项目事实（含物理平台构型与 F-001）。
- docs/TERMINOLOGY.md：专业术语纠错与写作偏好（区分 ERROR / PREFERENCE / CONTEXT）。
- docs/contracts/：学术文档章节功能与框架契约（开题报告见 docs/contracts/opening_report_contracts_and_evidence.md，提供结构与功能参考，具体技术路线尚未最终确认）。
- .agents/skills/academic-writing/SKILL.md：通用学术写作与审稿方法（课题无关）。
- PROJECT_STATUS.md：历史台账，仅在需要追溯演进过程时按需查阅。

## 当前任务

学术写作流程架构第二轮质量修复：修复质量门禁五大潜在缺陷（三态退出码、DOCX 原生段落/表格解析、零文件/缺失目标/规则拦截），显式标注章节契约内容状态，同步消除语义冲突，同步 Skill 职责并补充自动化回归测试。

## 已确认的流程原则

- 通用 Skill 不包含具体研究路线与课题特定知识。
- 项目事实（PROJECT_FACTS.md）与术语纠错（TERMINOLOGY.md）分别管理。
- 章节契约集中收纳于 docs/contracts/，不散落在 Skills 内部。
- 章节契约中的具体技术方案仅供参考，不自动升级为确定事实。
- 重大修改先审查计划，经批准后再执行。
- 不以模型自检声明代替真实验证，交付前执行自动化门禁脚本。
- 每次任务应有明确范围及可验收输出。

## 待确认事项

- UC-01：最终研究意义的表述重心（结合 LIAS 实验室近海巡检与生态监测真实场景）。
- UC-02：任务书与开题报告的双向联动修订（任务书作为前期参考底稿，核心任务重心处于动态考量中）。

## 下一次会话交接

最近完成：
- 完成学术写作流程架构第二轮质量修复（scripts/check_academic_quality.py 确定性三态门禁与 OOXML DOCX 支持、docs/contracts/ 章节契约状态显式声明、AGENTS.md/PROJECT_NOW.md/academic-entry.md 消除语义冲突、academic-doc-builder/SKILL.md 职责同步、10 项隔离自动化回归测试套件）。

下一项任务：
- 基于 docs/contracts/opening_report_contracts_and_evidence.md 的章节功能框架与质量门禁，推进开题报告后续环节；契约内的技术路线与任务细分维持 PROVISIONAL 状态，不作为已敲定的研究决定。

允许修改的文件：
- 开题报告草稿与相关配图脚本（如 开题报告/ 目录下草稿）。

不允许修改的文件：
- 模板/ 目录下所有官方空白模板文件；
- 严禁读取或恢复已物理隔离的历史作废草稿；
- 未获授权不得修改通用 Skills 配置。

遗留问题：
- UC-01、UC-02 需在后续章节推进中持续对齐。