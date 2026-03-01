---
name: legal-bill-evidence
author: zy
description: 分析法律诉讼相关的银行流水和微信支付账单，生成Excel/HTML/PDF格式的证据报告。使用时机：当用户提到"银行流水"、"账单分析"、"消费报告"、"微信交易明细"、"证据整理"时触发此skill。
---

# 法律账单证据分析

对银行卡流水和微信支付明细进行自动化解析，生成可用于法律诉讼的结构化分析报告。

## 适用场景

- 银行卡流水分析（工商银行等 PDF 账单）
- 微信支付交易明细分析
- 法律诉讼证据整理
- 消费记录统计与可视化

## 整体数据流

```
银行卡 PDF                           微信 PDF
   ↓ pdftotext -layout                  ↓ pdftotext -layout
bank_card.txt                        wechat.txt
   ↓ parse_bank_card.py                 ↓ parse_wechat.py
bank_card_data.json                  wechat_data.json
            ↓          ↓
       generate_reports.py
            ↓
  Excel + HTML + PDF 分析报告
```

## 工作流程

### 步骤1：准备数据

**方式A：从 PDF 提取文本**（需安装 `pdftotext`）

```bash
# 安装（macOS）
brew install poppler

# 提取银行卡 PDF
pdftotext -layout 银行卡明细.pdf bank_card.txt

# 提取微信 PDF
pdftotext -layout 微信账单.pdf wechat.txt
```

**方式B：手工填写 JSON**

参考 `references/` 目录中的模板文件手工录入数据：
- `references/bank_card_template.json` —— 银行卡数据格式
- `references/wechat_template.json` —— 微信数据格式

### 步骤2：解析数据

> 以下命令中 `SKILL_DIR` 指 skill 安装目录，通常为 `~/.claude/skills/legal-bill-evidence`。

**解析银行卡文本：**

```bash
SKILL_DIR=~/.claude/skills/legal-bill-evidence

python3 "$SKILL_DIR/scripts/parse_bank_card.py" \
  --input bank_card.txt \
  --output bank_card_data.json \
  --card-name "借记卡2306" \
  --card-number "xxx2306" \
  --holder "李红霞" \
  --branch "安阳内黄新区支行"
```

**解析微信支付文本：**

```bash
python3 "$SKILL_DIR/scripts/parse_wechat.py" \
  --input wechat.txt \
  --output wechat_data.json
```

### 步骤3：生成报告

```bash
# 生成单份报告（Excel + HTML + PDF）
python3 "$SKILL_DIR/scripts/generate_reports.py" \
  --data bank_card_data.json \
  --output-dir ./分析报告/

# 指定报告名称
python3 "$SKILL_DIR/scripts/generate_reports.py" \
  --data wechat_data.json \
  --output-dir ./分析报告/ \
  --name "证据报告-微信支付"

# 只生成 Excel（不生成 PDF）
python3 "$SKILL_DIR/scripts/generate_reports.py" \
  --data bank_card_data.json \
  --output-dir ./分析报告/ \
  --formats excel,html
```

### 步骤4：查看输出

输出目录下会生成：

| 文件 | 说明 |
|------|------|
| `报告名称.xlsx` | Excel 表格（交易明细 + 汇总统计） |
| `报告名称.html` | HTML 报告（可在浏览器查看） |
| `报告名称.pdf` | PDF 报告（可直接打印，用于诉讼） |

## 脚本说明

### parse_bank_card.py

解析 `pdftotext -layout` 导出的银行卡交易文本，输出标准 bank_card JSON。

```
用法: python3 parse_bank_card.py --input <txt文件> --output <json文件>
                                  [--card-name "借记卡2306"]
                                  [--card-number "xxx2306"]
                                  [--holder "姓名"]
                                  [--branch "支行名称"]
```

### parse_wechat.py

解析微信支付账单 PDF 文本，输出标准 wechat JSON。

```
用法: python3 parse_wechat.py --input <txt文件> --output <json文件>
```

### generate_reports.py

读取 JSON 数据文件，生成 Excel + HTML + PDF 三种格式报告。支持 bank_card 和 wechat 两种数据类型。

```
用法: python3 generate_reports.py --data <json文件> --output-dir <输出目录>
                                   [--name "报告名称"]
                                   [--formats excel,html,pdf]
```

## JSON 数据格式说明

### bank_card 格式

```json
{
  "type": "bank_card",
  "source": "银行卡账户历史明细清单",
  "card_name": "借记卡2306",
  "card_number": "xxx2306",
  "holder": "李红霞",
  "branch": "安阳内黄新区支行",
  "period": { "start": "2023-01-01", "end": "2023-12-31" },
  "transactions": [
    { "date": "2023-03-15", "amount": -800.00, "type": "ATM取款", "description": "说明" }
  ],
  "page_totals": {
    "expense": 23157.89,
    "income": 32.45,
    "pages": [
      { "name": "第1页", "expense": 5000.00, "income": 0.00 }
    ]
  }
}
```

**注意**：`transactions[].amount` 为负值表示支出，正值表示收入。

### wechat 格式

```json
{
  "type": "wechat",
  "source": "微信支付交易明细证明",
  "holder": "张三",
  "account": "wxid_xxx",
  "period": { "start": "2023-01-01", "end": "2023-12-31" },
  "transactions": [
    {
      "date": "2023-03-15",
      "time": "14:30:00",
      "type": "商户消费",
      "direction": "支出",
      "payment": "零钱",
      "amount": 98.00,
      "counterparty": "超市名称"
    }
  ]
}
```

## 依赖安装

```bash
# 安装 Python 依赖
pip3 install openpyxl

# PDF 转文本工具
brew install poppler     # macOS

# PDF 生成工具（可选，用于生成 PDF 报告）
brew install wkhtmltopdf
# 或安装 Google Chrome（会自动使用 headless 模式）
```

## 常见问题

### Q：银行卡 PDF 解析结果交易数量很少？

A：不同银行的 PDF 格式差异大，`parse_bank_card.py` 的正则基于工商银行格式设计。如果解析效果差，建议：
1. 用手工方式填写 JSON（参考模板）
2. 或让 Claude 读取 `bank_card.txt` 帮助提取数据

### Q：PDF 转文本后格式乱？

A：确保使用 `-layout` 参数保留列对齐：`pdftotext -layout 文件.pdf 输出.txt`

### Q：生成 PDF 报告失败？

A：PDF 生成依赖 `wkhtmltopdf` 或 Chrome，若两者都未安装，只会生成 Excel 和 HTML。可用 `--formats excel,html` 跳过 PDF 生成。

### Q：如何处理多张银行卡？

A：分别解析每张卡，生成独立报告：
```bash
python3 generate_reports.py --data card2306_data.json --output-dir ./报告/ --name "报告-卡2306"
python3 generate_reports.py --data card5432_data.json --output-dir ./报告/ --name "报告-卡5432"
```
