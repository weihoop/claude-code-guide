# 官方 Skills

Anthropic 官方发布的文档处理 Skills，质量保证，适用于所有平台。

## 📦 官方 Skills 列表

| Skill | 功能 | 适用场景 | 文档 |
|-------|------|---------|------|
| **docx** | Word 文档处理 | 创建、编辑、分析 Word 文档 | [查看详情](docx-pdf-pptx-xlsx.md#docx) |
| **pdf** | PDF 处理 | 提取、合并、注释 PDF | [查看详情](docx-pdf-pptx-xlsx.md#pdf) |
| **pptx** | PPT 处理 | 生成、编辑幻灯片 | [查看详情](docx-pdf-pptx-xlsx.md#pptx) |
| **xlsx** | Excel 处理 | 电子表格操作、图表生成 | [查看详情](docx-pdf-pptx-xlsx.md#xlsx) |

---

## 🚀 快速安装

### 方式 1：使用 npx（推荐）

```bash
npx skills add anthropics/skills
```

### 方式 2：手动安装

```bash
cd ~/.claude/skills/

# 克隆官方仓库
git clone https://github.com/anthropics/skills

# 复制需要的 Skills 到 skills 目录
cp -r skills/skills/docx ./
cp -r skills/skills/pdf ./
cp -r skills/skills/pptx ./
cp -r skills/skills/xlsx ./

# 清理
rm -rf skills
```

### 方式 3：从本指南安装

```bash
# 如果已克隆本仓库
cd ~/.claude/skills/
git clone https://github.com/anthropics/skills temp
cp -r temp/skills/* ./
rm -rf temp
```

---

## 💡 使用示例

### 单个 Skill 使用

```
用户: "分析这个 PDF 文件的内容"
Claude: [使用 pdf skill]

用户: "创建一个包含销售数据的 Excel 图表"
Claude: [使用 xlsx skill]

用户: "将这个 Word 文档转换为 PPT"
Claude: [使用 docx + pptx skills]
```

### 编程使用

**Python**:
```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    skills=["pdf", "docx"],  # 加载多个 Skills
    messages=[{"role": "user", "content": "分析这些文档"}]
)

print(response.content[0].text)
```

**Node.js**:
```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const response = await client.messages.create({
  model: "claude-sonnet-4-20250514",
  skills: ["pdf", "docx"],
  messages: [{ role: "user", content: "分析这些文档" }],
});

console.log(response.content[0].text);
```

---

## 🌟 特点和优势

### 官方支持

- ✅ Anthropic 官方维护
- ✅ 持续更新和优化
- ✅ 完整的文档和示例
- ✅ 稳定可靠

### 跨平台兼容

- ✅ Claude.ai 网页版
- ✅ Claude Code CLI
- ✅ Claude API
- ✅ 所有 Claude 模型

### 高质量实现

- ✅ 专业的文档处理
- ✅ 完善的错误处理
- ✅ 性能优化
- ✅ 遵循最佳实践

---

## 📚 详细文档

查看每个 Skill 的详细说明：

- [📄 文档处理套件完整说明](docx-pdf-pptx-xlsx.md)

---

## 🔗 相关资源

### 官方资源

- [GitHub 仓库](https://github.com/anthropics/skills)
- [Skills 功能介绍](https://www.anthropic.com/news/skills)
- [使用指南](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

### 社区资源

- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [Skills 最佳实践](../guides/best-practices.md)
- [创建自定义 Skills](../guides/creating-custom-skills.md)

---

## 💬 常见问题

### 官方 Skills 和社区 Skills 的区别？

| 特性 | 官方 Skills | 社区 Skills |
|------|------------|------------|
| 维护者 | Anthropic 官方 | 社区开发者 |
| 质量保证 | ✅ 官方测试 | ⚠️ 参差不齐 |
| 更新频率 | 定期更新 | 取决于维护者 |
| 兼容性 | ✅ 所有平台 | ⚠️ 可能有限制 |
| 文档 | ✅ 完整详细 | ⚠️ 可能不完整 |

### 如何更新官方 Skills？

```bash
cd ~/.claude/skills/

# 备份现有配置（如果有自定义）
cp -r docx docx.backup

# 更新
git clone https://github.com/anthropics/skills temp
cp -r temp/skills/docx ./
rm -rf temp

# 测试
claude
```

### 官方 Skills 收费吗？

官方 Skills 本身是免费的，但使用 Claude API 需要按 API 调用付费。

---

**返回**: [主页](../README.md) | [社区 Skills](../community/)
