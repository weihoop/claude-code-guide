# 法律 AI 技能包

Claude Code 法律行业专用技能包，包含 11 个技能 + 1 个共享资源目录，覆盖法律文书起草、合同审查、赔偿计算、证据整理、合规审查等核心法律工作场景。

## 技能总览

| # | 技能名 | 目录 | 触发词 | 输出 |
|---|--------|------|--------|------|
| 1 | 赔偿计算器 | `compensation-calc` | 赔偿计算/工伤赔偿/经济补偿金 | Excel |
| 2 | 合同审查 | `contract-review` | 合同审查/审合同/合同风险 | Word |
| 3 | 诉讼文书起草 | `legal-doc-draft` | 起诉状/答辩状/上诉状/仲裁/执行 | Word |
| 4 | 证据整理 | `evidence-organize` | 证据目录/质证意见/证据清单 | Word |
| 5 | 案情梳理 | `case-summary` | 案情梳理/法律意见/案件分析 | Word |
| 6 | 企业合规审查 | `compliance-check` | 合规审查/合规风险/企业合规 | Word |
| 7 | 法律内容生产 | `legal-content` | 普法文章/客户告知书/进展说明 | Word/文本 |
| 8 | 庭审代理意见书 | `court-opinion` | 代理意见/庭审意见/代理词 | Word |
| 9 | 图片转Excel | `image-to-excel` | 转Excel/提取表格/图片转表格 | Excel |
| 10 | 图片转Word | `image-to-word` | 转Word/生成Word/图片转文档 | Word |
| 11 | 账单证据分析 | `legal-bill-evidence` | 银行流水/账单分析/微信交易 | Excel/HTML/PDF |

## 目录结构

```
law-ai/
├── README.md                    # 本文件
├── .gitignore                   # 排除大文件
├── docs/                        # 帮助文档
│   ├── CLAUDE.md                # 技能包完整架构说明
│   ├── CHANGELOG.md             # 变更日志
│   ├── TODO.md                  # 待办事项
│   ├── generate_help_doc.py     # Word手册生成脚本
│   └── 法律AI技能使用手册.docx    # 用户手册
├── compensation-calc/           # 赔偿计算器
├── contract-review/             # 合同审查
├── legal-doc-draft/             # 诉讼文书起草
├── evidence-organize/           # 证据整理
├── case-summary/                # 案情梳理
├── compliance-check/            # 企业合规审查
├── legal-content/               # 法律内容生产
├── court-opinion/               # 庭审代理意见书
├── image-to-excel/              # 图片转Excel
├── image-to-word/               # 图片转Word
├── legal-bill-evidence/         # 账单证据分析
└── shared/                      # 共享资源
    ├── references/
    │   ├── 法条库.json            # 25条高频法条白名单
    │   ├── 案例索引.json          # [不入库] 总索引 14MB
    │   ├── 案例索引-2024.json     # [不入库] 2024年索引
    │   ├── 案例索引-2025.json     # [不入库] 2025年索引
    │   └── 案例全文/              # [不入库] 1,739个txt全文
    └── scripts/
        ├── build_case_index.py    # PDF案例提取工具
        ├── clean_txt_headers.py   # 全文头部清理
        └── generate_case_report.py # HTML报告生成
```

## 安装方式

### 1. 拷贝技能到 Claude Code skills 目录

```bash
# 拷贝所有技能目录到 ~/.claude/skills/
cp -r compensation-calc ~/.claude/skills/
cp -r contract-review ~/.claude/skills/
cp -r legal-doc-draft ~/.claude/skills/
cp -r evidence-organize ~/.claude/skills/
cp -r case-summary ~/.claude/skills/
cp -r compliance-check ~/.claude/skills/
cp -r legal-content ~/.claude/skills/
cp -r court-opinion ~/.claude/skills/
cp -r image-to-excel ~/.claude/skills/
cp -r image-to-word ~/.claude/skills/
cp -r legal-bill-evidence ~/.claude/skills/
cp -r shared ~/.claude/skills/
```

### 2. 安装 Python 依赖

```bash
pip install python-docx openpyxl
# 账单证据分析额外需要 poppler（pdftotext）
# macOS: brew install poppler
# Linux: apt install poppler-utils
```

### 3. 案例参考库（可选）

案例数据文件（约 54MB）未纳入 Git 版本控制，需要单独获取：

- `案例索引.json` — 总索引 14MB，1,739个案例
- `案例索引-2024.json` — 2024年索引 3MB，381个案例
- `案例索引-2025.json` — 2025年索引 5MB，1,358个案例
- `案例全文/` — 1,739个txt全文文件，32MB

**生成方式**：使用 `shared/scripts/build_case_index.py` 从《中国法院年度案例》PDF 中提取：

```bash
cd ~/.claude/skills/shared/scripts
python3 build_case_index.py --input /path/to/案例PDF目录 --output ../references/
```

## 跨技能共享机制

### 法条引用规则

5个法律类技能（case-summary、court-opinion、contract-review、compliance-check、legal-doc-draft）共享：

- **法条库优先**：引用法条时优先从 `shared/references/法条库.json` 精确匹配
- **三级确定性标注**：`VERIFIED` / `UNCERTAIN`（标注 `[待核实]`）/ `OBSOLETE`（禁止引用）
- **废止法律黑名单**：婚姻法→民法典婚姻家庭编、合同法→民法典合同编等

### 案例参考系统

- 1,739个案例，覆盖 23 个法律领域
- Claude 自动读取案例索引，按领域/案由/关键词检索相似案例
- 引用格式：`[参考案例：{案例标题}，{裁判书字号}]`

## 文书格式标准

所有输出文书遵循中国法院标准：
- 标题：黑体二号居中
- 正文：仿宋_GB2312 小四
- 页面：A4，页边距 2.54cm
- 配色：主色 `#17376A`（深蓝），辅色 `#2E74B5`

## 详细文档

- 完整架构说明：[docs/CLAUDE.md](docs/CLAUDE.md)
- 变更日志：[docs/CHANGELOG.md](docs/CHANGELOG.md)
- 待办事项：[docs/TODO.md](docs/TODO.md)
- 用户手册：[docs/法律AI技能使用手册.docx](docs/法律AI技能使用手册.docx)
