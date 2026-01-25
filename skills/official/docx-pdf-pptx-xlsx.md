# 文档处理套件详细说明

Anthropic 官方的 4 个文档处理 Skills 完整指南。

## 📄 docx - Word 文档处理

### 功能概述

创建、编辑、分析 Word 文档，支持修订追踪、评论、格式化。

### 核心功能

- ✅ 创建新的 Word 文档
- ✅ 编辑现有文档内容
- ✅ 读取和分析文档
- ✅ 修订追踪和评论
- ✅ 格式化（字体、段落、样式）
- ✅ 插入表格、图片、图表
- ✅ 文档模板支持

### 使用示例

```
用户: "创建一个产品需求文档"

Claude: [使用 docx skill]
已创建产品需求文档（PRD.docx）：

# 产品需求文档

## 1. 概述
[产品概述内容]

## 2. 功能需求
### 2.1 核心功能
- 功能 1
- 功能 2

## 3. 非功能需求
[性能、安全、可用性要求]

文档已保存，包含：
- 标题样式
- 目录
- 页眉页脚
- 版本信息
```

### 技术细节

- **格式支持**: .docx（Office 2007+）
- **依赖**: python-docx 库
- **输出**: 标准 Office Open XML 格式

### GitHub

[anthropics/skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx)

---

## 📑 pdf - PDF 处理

### 功能概述

提取文本、表格、元数据，合并和注释 PDF 文件。

### 核心功能

- ✅ 提取 PDF 文本内容
- ✅ 提取表格数据
- ✅ 读取元数据（作者、创建日期等）
- ✅ 合并多个 PDF
- ✅ 添加注释和书签
- ✅ 分割 PDF 页面
- ✅ PDF 转换（转图片、文本）

### 使用示例

```
用户: "分析这个合同 PDF，提取关键条款"

Claude: [使用 pdf skill]
已分析合同文件（contract.pdf）：

📋 文档信息
- 页数：25 页
- 作者：Legal Department
- 创建日期：2024-12-01

🔍 关键条款
1. 合同期限：2年（2025-01-01 至 2026-12-31）
2. 付款方式：月度结算
3. 违约责任：第15页，第3条
4. 终止条款：第22页，第7条

⚠️ 风险提示
- 自动续约条款（第5页）
- 排他性协议（第8页）
```

### 技术细节

- **格式支持**: PDF 1.0-1.7, PDF/A
- **依赖**: PyPDF2, pdfplumber
- **OCR**: 支持（需额外配置）

### GitHub

[anthropics/skills/pdf](https://github.com/anthropics/skills/tree/main/skills/pdf)

---

## 📊 pptx - PowerPoint 处理

### 功能概述

读取、生成、调整幻灯片、布局、模板。

### 核心功能

- ✅ 创建新的 PPT 演示
- ✅ 编辑现有幻灯片
- ✅ 读取和分析 PPT
- ✅ 应用模板和主题
- ✅ 插入图表、图片、表格
- ✅ 动画和过渡效果
- ✅ 演讲者备注

### 使用示例

```
用户: "根据这些数据创建一个季度业绩报告 PPT"

Claude: [使用 pptx skill]
已创建 Q4 业绩报告（Q4_Report.pptx）：

幻灯片 1: 封面
- 标题：2024 Q4 业绩报告
- 副标题：销售部门
- 日期：2026-01-24

幻灯片 2: 业绩概览
- 总销售额：$1.2M（+15% YoY）
- 新客户：234（+20%）
- 柱状图：月度销售趋势

幻灯片 3: 产品分析
- 饼图：产品占比
- 表格：TOP 5 产品

幻灯片 4: 下季度计划
- 5 个关键目标
- 时间线图表

演示文稿包含：
- 4 张幻灯片
- 3 个图表
- 统一的配色方案
- 演讲者备注
```

### 技术细节

- **格式支持**: .pptx（Office 2007+）
- **依赖**: python-pptx 库
- **模板**: 支持自定义母版

### GitHub

[anthropics/skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx)

---

## 📈 xlsx - Excel 处理

### 功能概述

电子表格操作：公式、图表、数据转换。

### 核心功能

- ✅ 创建和编辑 Excel 文件
- ✅ 读取和分析数据
- ✅ 公式计算（SUM、AVERAGE、VLOOKUP等）
- ✅ 生成图表（柱状图、折线图、饼图）
- ✅ 数据透视表
- ✅ 条件格式
- ✅ 多工作表管理

### 使用示例

```
用户: "分析这个销售数据 Excel，生成月度报告"

Claude: [使用 xlsx skill]
已分析销售数据（sales.xlsx）：

📊 数据概览
- 工作表：3 个（Sales, Products, Customers）
- 记录数：1,234 行
- 时间范围：2024-01 到 2024-12

📈 月度分析
| 月份 | 销售额 | 增长率 | 订单数 |
|------|--------|--------|--------|
| 01月 | $95K   | -      | 234    |
| 02月 | $102K  | +7.4%  | 256    |
| ...  | ...    | ...    | ...    |
| 12月 | $150K  | +12.5% | 378    |

🎯 关键发现
- 年度总销售：$1.23M
- 平均月增长：8.5%
- 最佳月份：12月（$150K）
- 客单价：$513

已生成报告文件（monthly_report.xlsx）：
- 工作表 1：原始数据
- 工作表 2：月度汇总
- 工作表 3：图表分析
  - 折线图：销售趋势
  - 柱状图：月度对比
  - 饼图：产品占比
```

### 技术细节

- **格式支持**: .xlsx（Excel 2007+）, .xls（Excel 97-2003）
- **依赖**: openpyxl, xlrd
- **公式**: 支持 Excel 标准公式

### GitHub

[anthropics/skills/xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx)

---

## 🔄 组合使用

### 场景 1：报告生成工作流

```
Excel 数据分析（xlsx）
  ↓
生成 Word 报告（docx）
  ↓
创建 PPT 演示（pptx）
  ↓
导出 PDF 分发（pdf）
```

**示例**:
```
用户: "根据 sales.xlsx 生成完整的季度报告（Word + PPT + PDF）"

Claude:
1. [xlsx] 分析销售数据
2. [docx] 生成详细 Word 报告
3. [pptx] 创建管理层 PPT
4. [pdf] 导出分发版 PDF

✅ 已生成：
- Q4_Report_Detailed.docx（15 页详细报告）
- Q4_Report_Executive.pptx（8 张幻灯片）
- Q4_Report_Final.pdf（分发版）
```

### 场景 2：文档转换

```
用户: "将这个 Word 合同转换为 PDF，并提取关键条款"

Claude:
1. [docx] 读取 Word 合同
2. [pdf] 转换为 PDF 格式
3. [pdf] 提取关键条款
4. [xlsx] 生成条款对比表

✅ 完成转换和分析
```

---

## 📦 批量操作

### Python 批量处理示例

```python
import anthropic
from pathlib import Path

client = anthropic.Anthropic()

# 批量处理文档目录
docs_dir = Path("./documents")
for doc in docs_dir.glob("*.pdf"):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        skills=["pdf"],
        messages=[{
            "role": "user",
            "content": f"分析文档：{doc.name}"
        }]
    )

    # 保存分析结果
    output = Path("./analysis") / f"{doc.stem}_analysis.txt"
    output.write_text(response.content[0].text)
    print(f"✅ 完成：{doc.name}")
```

---

## ⚠️ 使用限制

### 文件大小

- **docx**: < 50MB
- **pdf**: < 100MB
- **pptx**: < 50MB
- **xlsx**: < 50MB（或 100,000 行）

### 格式兼容性

| Skill | 推荐格式 | 兼容格式 | 不支持 |
|-------|---------|---------|--------|
| docx | .docx | .doc（有限） | .rtf, .odt |
| pdf | PDF 1.7 | PDF 1.0-1.7 | 加密 PDF* |
| pptx | .pptx | .ppt（有限） | .key |
| xlsx | .xlsx | .xls | .ods, .csv** |

*加密 PDF 需要先解密
**CSV 建议使用专门的 CSV Skills

---

## 📚 延伸阅读

- [官方文档](https://github.com/anthropics/skills)
- [编程使用 Skills](../guides/programming-usage.md)
- [最佳实践](../guides/best-practices.md)

---

**返回**: [官方 Skills](README.md) | [主页](../README.md)
