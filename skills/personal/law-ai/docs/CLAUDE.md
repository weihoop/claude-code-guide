# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

本项目包含一个 Python 脚本 `generate_help_doc.py`，用于生成《法律AI技能使用手册》Word 文档（`法律AI技能使用手册.docx`）。该手册是 Claude Code 法律 AI 技能包（Skills）的用户使用指南。

## 运行命令

```bash
# 生成手册文档（输出到同目录下 法律AI技能使用手册.docx）
python3 generate_help_doc.py
```

## 依赖

- Python 3
- `python-docx`（安装：`pip install python-docx`）

## 代码架构

`generate_help_doc.py` 是一个单文件脚本，结构如下：

- **排版工具函数**（第 25-173 行）：`set_font`、`set_page`、`h1/h2/h3`、`body`、`tip_box`、`bullet`、`code_block`、`two_col_table`、`skill_card` 等，封装了 python-docx 的字体设置、页面布局、标题样式、表格生成等操作
- **`generate()` 主函数**（第 205 行起）：按章节顺序生成 Word 文档内容，包含封面、6个章节和附录
- 字体规范：标题用"黑体"，正文用"仿宋_GB2312"，代码块用"Courier New"
- 颜色体系：主色 `#17376A`（深蓝），辅色 `#2E74B5`（蓝），表头 `#2F5496`

## 修改注意事项

- 修改手册内容后需重新运行 `python3 generate_help_doc.py` 生成 docx
- 所有文书格式遵循中国法院标准：A4 页面、页边距 2.54cm、仿宋_GB2312 小四正文
- 表格使用交替行底色（`#EBF1F8` / `#FFFFFF`）提升可读性

---

## 法律 AI 技能包全景（~/.claude/skills/）

共 11 个技能包 + 1 个共享资源目录。每个技能包统一结构：`SKILL.md`（技能说明）+ `scripts/`（Python 脚本）+ `references/`（模板/参考数据）。

### 技能总览

| # | 技能名 | 目录名 | 触发词 | 输出 | 脚本 |
|---|--------|--------|--------|------|------|
| 1 | 赔偿计算器 | compensation-calc | 赔偿计算/工伤赔偿/经济补偿金/交通赔偿/离婚财产分割 | Excel | calc_compensation.py |
| 2 | 合同审查 | contract-review | 合同审查/审合同/合同风险/条款审查 | Word | generate_review.py |
| 3 | 诉讼文书起草 | legal-doc-draft | 起诉状/答辩状/上诉状/仲裁申请书/强制执行 | Word | generate_doc.py |
| 4 | 证据整理 | evidence-organize | 证据目录/质证意见/整理证据/证据清单 | Word | generate_evidence.py |
| 5 | 案情梳理 | case-summary | 案情梳理/法律意见/案件分析/法律意见书 | Word | generate_opinion.py |
| 6 | 企业合规审查 | compliance-check | 合规审查/合规风险/企业合规/劳动合规 | Word | generate_compliance.py |
| 7 | 法律内容生产 | legal-content | 普法文章/公众号/客户告知书/进展说明/法律问答 | Word/文本 | generate_content.py |
| 8 | 庭审代理意见书 | court-opinion | 代理意见/庭审意见/代理词/辩护词 | Word | generate_court_opinion.py |
| 9 | 图片转Excel | image-to-excel | 转Excel/提取表格/图片转表格 | Excel | csv_to_excel.py |
| 10 | 图片转Word | image-to-word | 转Word/生成Word/图片转文档 | Word | create_word.py |
| 11 | 账单证据分析 | legal-bill-evidence | 银行流水/账单分析/微信交易明细 | Excel/HTML/PDF | parse_bank_card.py + parse_wechat.py + generate_reports.py |

### 共享资源（shared/）

| 文件 | 用途 |
|------|------|
| `shared/references/法条库.json` | 25条高频法条原文白名单，5个法律类 skill 共用 |
| `shared/references/案例索引.json` | 总索引 14MB，合并 1,739 个案例（2024+2025），覆盖 23 个法律领域 |
| `shared/references/案例索引-2025.json` | 2025年索引 4.2MB，1,358 个案例（23册） |
| `shared/references/案例索引-2024.json` | 2024年索引 2.6MB，381 个案例（23册） |
| `shared/references/案例全文/` | 1,739 个 txt 全文文件，按 `{年份}/{册号}-{领域}/{序号}.txt` 组织 |
| `shared/scripts/build_case_index.py` | PDF 案例提取工具（依赖 pdfplumber）：提取→反向OCR检测→分割→结构化解析→生成索引 |
| `shared/scripts/generate_case_report.py` | HTML 可视化报告生成工具：读取索引JSON，生成自包含HTML（搜索/筛选/详情展开） |

---

### 各技能详情

#### 1. compensation-calc（赔偿计算器）

- **4种计算类型**：`--type labor`（劳动经济补偿金）、`--type injury`（工伤）、`--type traffic`（交通事故）、`--type divorce`（离婚财产分割）
- **核心参数文件**：`references/标准参数.json`——包含全国/各省平均工资、人均可支配收入等，**需每年手动更新**
- **运行方式**：`python3 scripts/calc_compensation.py --type <类型> --monthly-salary <月工资> --years <工龄> [其他参数] --output <输出.xlsx>`
- **输出**：Sheet1 分项明细+法律依据，Sheet2 汇总合计，Sheet3 法条声明
- **数据年份**：当前为 2023 年数据（national_avg_salary=97388，urban_avg_annual=49283）
- **注意**：修改标准参数.json 后需同步检查 calc_compensation.py 中的 DEFAULT_PARAMS 字典

#### 2. contract-review（合同审查）

- **输入**：合同全文 + 审查立场（甲方/乙方/中立）+ 合同类型
- **输出结构**：封面 → 总体评价 → 风险清单表（高红/中橙/低黄） → 缺失条款 → 综合建议
- **参考文件**：`references/审查要点.md`（8种合同类型核查要点）、`references/contract_review_template.json`
- **运行**：`python3 scripts/generate_review.py --input <JSON> --output <.docx>`

#### 3. legal-doc-draft（诉讼文书起草）

- **5种文书**：`qisu`（起诉状）、`daben`（答辩状）、`susong`（上诉状）、`zhongcai`（仲裁申请书）、`zhixing`（执行申请书）
- **模板目录**：`templates/`下有 5 个对应的 JSON 模板文件
- **格式标准**：标题黑体二号居中、正文仿宋_GB2312小四、A4 页边距 2.54cm
- **运行**：`python3 scripts/generate_doc.py --type <类型> --input <JSON> --output <.docx>`

#### 4. evidence-organize（证据整理）

- **输出两张表**：表1 己方证据目录（序号/名称/证明目的/来源/页码）、表2 对方证据质证意见（三性：真实性/合法性/关联性 + 综合意见）
- **运行**：`python3 scripts/generate_evidence.py --input <JSON> --output <.docx>`

#### 5. case-summary（案情梳理与法律意见书）

- **输出结构**：委托方信息 → 事实概述 → 法律关系分析 → 争议焦点 → 法律规定 → 法律意见 → 证据建议 → 风险提示 → 律师声明
- **可选案例参考**：读取 `shared/references/案例索引.json` 检索相似判例
- **运行**：`python3 scripts/generate_opinion.py --input <JSON> --output <.docx>`

#### 6. compliance-check（企业合规审查）

- **4个审查领域**：`labor`（劳动用工）、`data`（数据安全）、`contract`（合同管理）、`general`（综合）
- **参考文件**：`references/compliance_checklist.json`（各领域核查清单）、`references/compliance_template.json`
- **风险分级**：高（违法违规，需立即整改）→ 中（制度漏洞，3个月内完善）→ 低（流程不规范，逐步优化）
- **运行**：`python3 scripts/generate_compliance.py --area <领域> --input <JSON> --output <.docx>`

#### 7. legal-content（法律内容生产）

- **4种内容类型**：`article`（普法文章，纯文本）、`notice`（客户告知书，Word）、`guide`（进展说明函，Word）、`faq`（法律问答，Word）
- **参考模板**：`references/notice_template.json`、`references/guide_template.json`、`references/faq_template.json`
- **运行**：`python3 scripts/generate_content.py --type <类型> --input <JSON> --output <.docx>`

#### 8. court-opinion（庭审代理意见书）

- **文书类型**：民事代理意见书、刑事辩护意见书、劳动仲裁代理意见书（通过 JSON 中"文书类型"字段区分）
- **输出结构**：标题 → 代理人信息表 → 事实意见（己方陈述+反驳对方）→ 证据意见 → 法律适用分析 → 请求事项 → 落款
- **运行**：`python3 scripts/generate_court_opinion.py --input <JSON> --output <.docx>`

#### 9. image-to-excel（图片转Excel）

- **流程**：Read 读取图片 → Claude 多模态识别表格结构 → 生成 CSV → `scripts/csv_to_excel.py` 转换为带格式 Excel
- **依赖**：`openpyxl`
- **Excel 样式**：标题行蓝色背景(#4472C4)白色加粗字体，列宽自适应

#### 10. image-to-word（图片转Word）

- **流程**：Read 读取图片 → Claude 识别内容结构 → 整理为 JSON → `scripts/create_word.py` 生成 Word
- **JSON 支持 3 种 section type**：`table`（表格）、`text`（段落）、`list`（列表），每种可指定 heading 和 header_color
- **依赖**：`python-docx`

#### 11. legal-bill-evidence（账单证据分析）

- **数据流**：银行卡/微信 PDF → `pdftotext -layout` → txt → `parse_bank_card.py`/`parse_wechat.py` → JSON → `generate_reports.py` → Excel+HTML+PDF
- **外部依赖**：`poppler`（pdftotext）、`openpyxl`、`wkhtmltopdf` 或 Chrome（PDF 生成可选）
- **支持格式参数**：`--formats excel,html,pdf`（可选择性生成）
- **参考模板**：`references/bank_card_template.json`、`references/wechat_template.json`

---

### 跨 Skill 共享机制

#### 法条引用规则（5个法律类 skill 共用）

以下 5 个 skill 的 SKILL.md 中包含相同的"法条引用规则"章节：case-summary、court-opinion、contract-review、compliance-check、legal-doc-draft

- **法条库优先**：引用法条时优先从 `shared/references/法条库.json` 精确匹配，标注 `[库中已核实]`
- **三级确定性标注**：`VERIFIED`（直接引用）/ `UNCERTAIN`（标注 `[待核实]`）/ `OBSOLETE`（禁止引用废止法）
- **废止法律黑名单**：婚姻法→民法典婚姻家庭编、合同法→民法典合同编、侵权责任法→民法典侵权责任编、物权法→民法典物权编、继承法→民法典继承编、担保法→民法典相关编章
- **条文号上限**：劳动合同法止于第98条、民法典止于第1260条，禁止超出
- **JSON 输出要求**：每条法条必须携带 `_来源`（LIBRARY/AI_GENERATED）和 `_确定性` 字段

#### 案例参考系统（5个法律类 skill 可选使用）

**数据规模**：1,739 个案例，覆盖 23 个法律领域，总索引 14MB

| 年份 | 案例数 | 说明 |
|------|--------|------|
| 2025版 | 1,358 个 | 23册全部提取，99.8% 完整质量 |
| 2024版 | 381 个 | 23册全部提取（含3册反向OCR翻转处理） |

**文件结构**：
```
~/.claude/skills/shared/
├── scripts/
│   ├── build_case_index.py              ← PDF提取工具（反向OCR检测+模糊标签匹配+结构化解析）
│   └── generate_case_report.py          ← HTML可视化报告生成工具
├── references/
│   ├── 法条库.json                      ← 25条高频法条白名单
│   ├── 案例索引.json                    ← 总索引 14MB（Claude 可直接读取）
│   ├── 案例索引-2025.json              ← 2025年索引 4.2MB
│   ├── 案例索引-2024.json              ← 2024年索引 2.2MB
│   └── 案例全文/                       ← 1,739 个 txt 全文文件
│       ├── 2025/ (23个领域目录)
│       └── 2024/ (23个领域目录)
```

**使用方式**：Claude 在使用 5 个法律技能时，自动读取 `案例索引.json`，按领域/案由/关键词检索相似案例；如需详情，读取 `案例全文/{年份}/{册号}-{领域}/{序号}.txt`

**引用格式**：`[参考案例：{案例标题}，{裁判书字号}]`

---

### 新增/优化 Skill 的统一规范

新建或修改 skill 时应遵循以下约定：

1. **目录结构**：`~/.claude/skills/<skill-name>/SKILL.md` + `scripts/` + `references/`（可选 `templates/`）
2. **SKILL.md 头部**：必须包含 YAML front matter（name、author、description）
3. **触发词**：在 SKILL.md 中以"## 触发词"章节明确列出
4. **工作流**：分为 AI 分析阶段（Claude 输出 JSON）和脚本生成阶段（Python 生成 Word/Excel）
5. **法律类 skill**：必须包含"法条引用规则"章节（复制自现有 skill 的标准模板），引用 `shared/references/法条库.json`
6. **Python 脚本依赖**：Word 类用 `python-docx`，Excel 类用 `openpyxl`
7. **文书格式标准**：标题黑体二号居中、正文仿宋_GB2312小四、A4 页面页边距 2.54cm
8. **手册同步**：新增 skill 后需在 `generate_help_doc.py` 中补充对应章节并重新生成手册
