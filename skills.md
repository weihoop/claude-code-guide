# Claude Skills 使用指南

> 💡 **提示**：本文档提供快速参考。查看完整的 Skills 专区请访问 [skills/](skills/) 目录，包含 Top 10 详细安装指南、社区分类、深度教程等。

Skills 是 Claude 的模块化功能扩展系统，让 Claude 具备专业化的工作能力。

## 目录

- [什么是 Skills](#什么是-skills)
- [Skills vs MCP vs Slash Commands](#skills-vs-mcp-vs-slash-commands)
- [快速开始](#快速开始)
- [编程使用](#编程使用)
- [热门 Skills 推荐](#热门-skills-推荐)
- [创建自定义 Skill](#创建自定义-skill)
- [资源汇总](#资源汇总)

---

## 什么是 Skills

Skills 是可复用的 AI 工作流模块，为 Claude 提供专业领域的知识和工具。

### 核心特点

| 特性 | 说明 |
|------|------|
| **自动触发** | Claude 根据上下文自动激活相关 skill |
| **渐进式加载** | 三层加载机制，按需加载节省 Token |
| **跨平台兼容** | Claude.ai、Claude Code、API 通用 |
| **可执行代码** | 支持脚本执行，处理复杂任务 |

### 渐进式加载机制

```
1. 元数据（name + description）  → 始终在上下文（~100 words）
2. SKILL.md 正文               → 触发时加载（<5k words）
3. 附属资源（scripts/refs/）    → 按需加载（无限制）
```

### 存储位置

```bash
# Claude Code 位置
~/.claude/skills/
# 或
~/.config/claude-code/skills/

# 目录结构
skill-name/
├── SKILL.md          # 必需：skill 说明和指令
├── scripts/          # 可选：可执行脚本
├── references/       # 可选：参考文档
└── assets/           # 可选：模板、图片等资源
```

---

## Skills vs MCP vs Slash Commands

| 特性 | Skills | MCP | Slash Commands |
|------|--------|-----|----------------|
| **触发方式** | 自动/手动 | 手动调用 | 手动输入 `/xxx` |
| **关注点** | 流程和方法 | 外部数据访问 | 快捷操作 |
| **Token 效率** | 高（渐进式） | 中 | 低 |
| **适用场景** | 专业工作流 | API/数据库集成 | 常用命令快捷方式 |

### 组合使用示例

```
MCP 从 GitHub 获取 Issue 数据
  ↓
Skill 分析数据并生成报告（使用特定格式）
  ↓
Slash Command 快速执行 /report
```

---

## 快速开始

### 在 Claude.ai 中使用

1. 点击聊天界面的技能图标（puzzle icon）
2. 从市场添加或上传自定义 skill
3. Claude 自动根据任务激活相关 skill

### 在 Claude Code 中使用

```bash
# 1. 创建 skills 目录
mkdir -p ~/.claude/skills/

# 2. 下载或复制 skill
git clone https://github.com/anthropics/skills.git /tmp/skills
cp -r /tmp/skills/skills/pdf ~/.claude/skills/

# 3. 验证 skill
head ~/.claude/skills/pdf/SKILL.md

# 4. 启动 Claude Code，自动加载
claude
```

### 通过 API 使用

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    skills=["pdf", "docx"],  # 指定加载的 skills
    messages=[{"role": "user", "content": "分析这个 PDF 文件"}]
)
```

---

## 编程使用

### Python SDK 完整示例

```python
import anthropic
import os

# 初始化客户端
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# 基础调用（带 skills）
def analyze_document(file_path: str, skill_name: str = "pdf"):
    """使用指定 skill 分析文档"""
    with open(file_path, "rb") as f:
        content = f.read()

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        skills=[skill_name],
        messages=[{
            "role": "user",
            "content": f"分析这个文档并提取关键信息"
        }]
    )
    return response.content[0].text

# 使用示例
result = analyze_document("report.pdf", "pdf")
print(result)
```

### 自动化工作流示例

```python
# 批量文档处理工作流
import os
from pathlib import Path

def batch_process_docs(input_dir: str, output_dir: str):
    """批量处理文档，自动选择合适的 skill"""

    skill_map = {
        ".pdf": "pdf",
        ".docx": "docx",
        ".xlsx": "xlsx",
        ".pptx": "pptx"
    }

    for file_path in Path(input_dir).iterdir():
        ext = file_path.suffix.lower()
        if ext in skill_map:
            skill = skill_map[ext]
            result = analyze_document(str(file_path), skill)

            # 保存结果
            output_file = Path(output_dir) / f"{file_path.stem}_analysis.md"
            output_file.write_text(result)
            print(f"处理完成: {file_path.name}")

# 执行
batch_process_docs("./documents", "./analysis")
```

---

## 热门 Skills 推荐

### 文档处理

| Skill | 用途 | 链接 |
|-------|------|------|
| **docx** | Word 文档读写、格式化 | [官方](https://github.com/anthropics/skills/tree/main/skills/docx) |
| **pdf** | PDF 提取、合并、注释 | [官方](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| **pptx** | PPT 生成和编辑 | [官方](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| **xlsx** | Excel 操作、图表生成 | [官方](https://github.com/anthropics/skills/tree/main/skills/xlsx) |

### 开发工具

| Skill | 用途 | 链接 |
|-------|------|------|
| **mcp-builder** | 创建 MCP 服务器 | [社区](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/mcp-builder) |
| **skill-creator** | 创建新 skill | [社区](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/skill-creator) |
| **webapp-testing** | Playwright 自动化测试 | [社区](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/webapp-testing) |
| **test-driven-development** | TDD 开发流程 | [社区](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |

### 数据分析

| Skill | 用途 | 链接 |
|-------|------|------|
| **CSV Data Summarizer** | CSV 数据可视化分析 | [社区](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) |
| **D3.js Visualization** | D3 图表生成 | [社区](https://github.com/chrisvoncsefalvay/claude-d3js-skill) |
| **postgres** | PostgreSQL 查询 | [社区](https://github.com/sanjay3290/ai-skills/tree/main/skills/postgres) |

### 创意媒体

| Skill | 用途 | 链接 |
|-------|------|------|
| **canvas-design** | 视觉艺术创作 | [社区](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/canvas-design) |
| **theme-factory** | 主题模板生成 | [社区](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/theme-factory) |
| **video-downloader** | 视频下载 | [社区](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/video-downloader) |

---

## 创建自定义 Skill

### 目录结构

```
my-skill/
├── SKILL.md          # 必需
├── scripts/          # 可选：Python/Bash 脚本
│   └── process.py
├── references/       # 可选：参考文档
│   └── api-docs.md
└── assets/           # 可选：模板、图片
    └── template.html
```

### SKILL.md 模板

```markdown
---
name: my-skill-name
description: 一句话描述这个 skill 的功能和使用场景。
---

# My Skill Name

详细描述 skill 的用途和能力。

## 使用场景

- 场景 1
- 场景 2
- 场景 3

## 指令

[Claude 执行此 skill 的具体步骤和注意事项]

## 示例

**用户**: "示例请求"

**输出**:
[预期输出示例]
```

### 最佳实践

1. **专注单一任务** - 每个 skill 只解决一个具体问题
2. **清晰的触发条件** - description 要明确说明何时使用
3. **渐进式设计** - 核心指令放 SKILL.md，详细参考放 references/
4. **包含示例** - 帮助 Claude 理解预期行为
5. **测试验证** - 在 Claude.ai、Claude Code、API 都测试

---

## 资源汇总

### GitHub 热门项目

| 项目 | 说明 |
|------|------|
| [anthropics/skills](https://github.com/anthropics/skills) | 官方 skills 仓库 |
| [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 精选 skills 列表 |
| [claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) | Skill 构建工具包 |
| [claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor) | Skills + Agents + Commands |
| [obra/superpowers](https://github.com/obra/superpowers) | 核心开发 skills |
| [SkillsMP.com](https://skillsmp.com/) | Skills 搜索平台（25000+） |

### 中文教程

| 资源 | 链接 |
|------|------|
| 知乎 - 最佳实践中文版 | [查看](https://zhuanlan.zhihu.com/p/1973059671540663242) |
| 知乎 - Skills 深度解析 | [查看](https://zhuanlan.zhihu.com/p/1966598753134842902) |
| 七牛开发者中心 | [查看](https://developer.qiniu.com/aitokenapi/13171/claude-code-skill-introduce) |
| Claude Code 中文教程 | [查看](https://claudecode.tangshuang.net/tutorial/14.1) |
| B站视频教程 | [查看](https://www.bilibili.com/video/BV1oZg1ziEy5/) |

### 官方文档

| 资源 | 链接 |
|------|------|
| Skills 功能介绍 | [Anthropic News](https://www.anthropic.com/news/skills) |
| Skills 用户指南 | [Support](https://support.claude.com/en/articles/12512180-using-skills-in-claude) |
| 创建自定义 Skills | [Support](https://support.claude.com/en/articles/12512198-creating-custom-skills) |
| Slash Commands 文档 | [Claude Code Docs](https://code.claude.com/docs/en/slash-commands) |

---

## 常见问题

### Skill 没有自动加载？

```bash
# 检查目录位置
ls ~/.claude/skills/

# 检查 SKILL.md 格式
head -10 ~/.claude/skills/my-skill/SKILL.md
# 必须有 YAML frontmatter（--- name: xxx ---）
```

### 如何调试 Skill？

1. 在 Claude Code 中使用 `/skill my-skill` 手动加载
2. 查看 Claude 的响应是否包含 skill 内容
3. 检查 scripts/ 中的脚本是否有执行权限

### Skills 和 Slash Commands 可以结合使用吗？

可以。创建一个 Slash Command 来触发特定 skill：

```markdown
<!-- .claude/commands/analyze.md -->
使用 pdf skill 分析当前目录的所有 PDF 文件，生成汇总报告。
```

---

**返回**: [README](README.md) | **反馈**: [GitHub Issues](https://github.com/weihoop/claude-code-guide/issues)
