# 文档处理 Skills

专注于文档创建、编辑、转换和分析的 Skills，覆盖 Word、PDF、Excel、PPT、EPUB 等格式。

## 📦 官方 Skills

Anthropic 官方发布，质量保证。

| Skill | 功能 | 仓库链接 |
|-------|------|---------|
| **docx** | 创建、编辑、分析 Word 文档，支持修订追踪、评论、格式化 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/docx) |
| **pdf** | 提取文本、表格、元数据，合并和注释 PDF | [GitHub](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| **pptx** | 读取、生成、调整幻灯片、布局、模板 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| **xlsx** | 电子表格操作：公式、图表、数据转换 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/xlsx) |

### 安装方法

```bash
# 方式 1：使用 npx（推荐）
npx skills add anthropics/skills

# 方式 2：手动克隆
cd ~/.config/claude-code/skills/
git clone https://github.com/anthropics/skills
# 然后将需要的 skill 复制到 skills 目录
```

### 使用示例

```
用户: "分析这个 PDF 文件的内容"
Claude: [使用 pdf skill 提取文本和结构]

用户: "创建一个包含销售数据的 Excel 图表"
Claude: [使用 xlsx skill 生成图表]

用户: "将这个 Word 文档转换为 PPT"
Claude: [使用 docx + pptx skills]
```

---

## 🌟 社区精选

### Markdown to EPUB Converter

将 Markdown 文档和聊天摘要转换为专业的 EPUB 电子书文件。

- **维护者**: [@smerchek](https://github.com/smerchek)
- **仓库**: [smerchek/claude-epub-skill](https://github.com/smerchek/claude-epub-skill)

**功能**:
- Markdown 转 EPUB
- 聊天摘要转电子书
- 专业排版
- 自定义样式

**安装**:
```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/smerchek/claude-epub-skill epub-converter
```

**使用示例**:
```
用户: "将这个 Markdown 文件转换为 EPUB"
[提供 example.md]

Claude:
✅ 已转换为 EPUB
文件：example.epub
章节：5 个
图片：3 张
```

---

## 📚 使用场景

### 场景 1：批量文档处理

```
任务：将 100 个 Word 文档转换为 PDF

步骤：
1. 使用 docx skill 读取 Word 文档
2. 提取关键信息
3. 使用 pdf skill 生成 PDF
4. 批量处理所有文档
```

### 场景 2：报告生成

```
任务：从 Excel 数据生成 PPT 报告

步骤：
1. 使用 xlsx skill 读取数据
2. 分析数据，生成图表
3. 使用 pptx skill 创建幻灯片
4. 插入图表和分析结论
```

### 场景 3：文档分析

```
任务：分析合同文档中的关键条款

步骤：
1. 使用 pdf/docx skill 读取合同
2. 提取关键条款
3. 标记风险点
4. 生成摘要报告
```

### 场景 4：电子书制作

```
任务：将博客文章合集制作为 EPUB 电子书

步骤：
1. 整理 Markdown 格式的文章
2. 使用 epub-converter skill
3. 自定义封面和样式
4. 生成 EPUB 文件
```

---

## 🔧 最佳实践

### 1. 批量处理

使用循环处理多个文档：

```python
import anthropic

client = anthropic.Anthropic()

for doc in documents:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        skills=["pdf"],
        messages=[{
            "role": "user",
            "content": f"分析文档：{doc}"
        }]
    )
```

### 2. 格式转换

保持格式一致性：

```
Word → PDF: 保留样式和格式
Excel → PPT: 保持图表样式
Markdown → EPUB: 自定义排版
```

### 3. 质量检查

转换后验证：
- 检查文本完整性
- 验证图片质量
- 测试超链接
- 确认格式正确

---

## ❓ 常见问题

### PDF 提取失败

**原因**: PDF 是扫描件或加密

**解决方法**:
1. 使用 OCR 工具先识别文字
2. 解密 PDF 后再处理
3. 尝试使用其他 PDF 工具

### Excel 公式错误

**原因**: 公式格式不兼容

**解决方法**:
1. 使用标准 Excel 公式
2. 避免自定义函数
3. 检查单元格引用

### EPUB 格式问题

**原因**: Markdown 格式不标准

**解决方法**:
1. 使用标准 Markdown 语法
2. 检查图片路径
3. 验证 Markdown 文件

---

## 📖 参考资料

### 官方文档

- [docx Skill](https://github.com/anthropics/skills/tree/main/skills/docx)
- [pdf Skill](https://github.com/anthropics/skills/tree/main/skills/pdf)
- [pptx Skill](https://github.com/anthropics/skills/tree/main/skills/pptx)
- [xlsx Skill](https://github.com/anthropics/skills/tree/main/skills/xlsx)

### 社区资源

- [Markdown to EPUB](https://github.com/smerchek/claude-epub-skill)

### 相关工具

- [python-docx](https://python-docx.readthedocs.io/) - Python Word 处理库
- [PyPDF2](https://pypdf2.readthedocs.io/) - Python PDF 处理库
- [python-pptx](https://python-pptx.readthedocs.io/) - Python PPT 处理库
- [openpyxl](https://openpyxl.readthedocs.io/) - Python Excel 处理库

---

**返回**: [社区导航](README.md) | [主页](../README.md)
