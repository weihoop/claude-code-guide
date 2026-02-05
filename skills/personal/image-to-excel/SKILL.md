---
name: image-to-excel
author: qingyang
description: 识别图片中的表格数据并转换为Excel文件。支持各类表格截图、账号密码表、财务数据等。使用时机：当用户提供图片并要求"转Excel"、"提取表格"、"图片转表格"、"识别表格数据"时触发此skill。
---

# 图片转Excel

将图片中的表格数据识别并转换为格式化的Excel文件。

## 适用场景

- 表格截图转Excel
- 账号密码表整理
- 财务数据提取
- 任何包含表格结构的图片

## 工作流程

### 步骤1：读取并识别图片

使用 Read 工具读取图片文件，Claude 会自动识别图片中的表格结构和数据。

```
Read 工具读取图片 → Claude 多模态识别 → 提取表格数据
```

### 步骤2：解析表格结构

识别图片后，分析表格结构：
- 确定列数和列名
- 识别每行数据
- 处理合并单元格或特殊格式

### 步骤3：生成Excel文件

使用 `scripts/csv_to_excel.py` 脚本将数据转换为带格式的Excel文件。

**方式一：先生成CSV再转Excel（推荐）**

```bash
# 1. 将识别的数据写入CSV文件
# 2. 运行转换脚本
python3 /Users/qingyang/.claude/skills/image-to-excel/scripts/csv_to_excel.py <csv文件路径> [输出xlsx路径]
```

**方式二：直接用Python生成Excel**

对于简单表格，可直接使用Python代码生成：

```python
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill

wb = Workbook()
ws = wb.active
ws.title = '数据表'

# 写入数据并设置样式
# ... 具体实现见脚本
```

## Excel格式规范

生成的Excel文件包含以下格式：

| 元素 | 样式 |
|------|------|
| 标题行 | 加粗、白色字体、蓝色背景(#4472C4) |
| 数据行 | 默认字体、居左对齐 |
| 列宽 | 自动调整，最小10字符 |
| 边框 | 细线边框（可选） |

## 输出文件命名

- 默认：与输入图片同名，扩展名改为 `.xlsx`
- 示例：`账号密码.jpg` → `账号密码.xlsx`

## 安全提示

处理敏感数据（如账号密码）时：
1. 转换完成后提醒用户删除原始图片
2. Excel文件建议加密保存
3. 不要将敏感文件上传到云端

## 常见问题处理

### 图片模糊或倾斜
- 尽量使用清晰的截图
- 轻微倾斜可以识别，严重倾斜可能影响准确性

### 表格边框不清晰
- 根据数据对齐和间距推断列边界
- 必要时询问用户确认列的划分

### 多个表格在同一图片
- 依次识别每个表格
- 可输出到同一Excel的不同工作表
