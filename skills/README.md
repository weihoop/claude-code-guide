# Claude Skills 完整指南

> 欢迎来到 Skills 专区！这里提供从入门到高级的完整 Skills 学习路径。

## 📖 什么是 Skills

Skills 是 Claude 的模块化功能扩展系统，让 Claude 具备专业化的工作能力。

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

## 🚀 快速开始

### 三种使用方式

| 平台 | 安装方式 | 适用场景 |
|------|---------|---------|
| **Claude.ai** | 点击技能图标（🧩）添加 | 网页端使用，无需命令行 |
| **Claude Code** | 复制到 `~/.claude/skills/` | 本地开发，自动加载 |
| **Claude API** | 通过 `skills` 参数指定 | 编程集成，批量处理 |

### 快速安装（推荐）

**一键安装 Top 10 精选 Skills**:
```bash
wget https://raw.githubusercontent.com/weihoop/claude-code-guide/main/skills/scripts/install_top10.sh
bash install_top10.sh
```

**手动安装单个 Skill**:
```bash
mkdir -p ~/.claude/skills/
cd ~/.claude/skills/
git clone https://github.com/用户名/skill-仓库 skill-名称
```

👉 [查看详细安装指南](installation-guide.md)

---

## 🌟 Top 10 精选推荐

精心挑选的 10 个实用 Skills，覆盖开发、创作、效率提升等核心场景。

| # | Skill | 功能 | 适用场景 | 详细指南 |
|---|-------|------|---------|---------|
| 1 | **NotebookLM** | AI 对接 NotebookLM，自动上传资料、知识问答 | 研究、学习、知识管理 | [查看](top-10/01-notebooklm.md) |
| 2 | **Obsidian Skills** | Obsidian CEO 出品的完整套件 | Markdown、Canvas、插件开发 | [查看](top-10/02-obsidian.md) |
| 3 | **Planning with Files** | 复刻 Manus 工作流，解决上下文飘移 | 复杂项目规划 | [查看](top-10/03-planning-with-files.md) |
| 4 | **Skill Creator** | 创建符合最佳实践的自定义 Skill | 自定义 Skill 开发 | [查看](top-10/04-skill-creator.md) |
| 5 | **Frontend Design** | 前端设计专用，避免 AI 通用美学 | React + Tailwind 开发 | [查看](top-10/05-frontend-design.md) |
| 6 | **Superpowers** | Obra 开发的工具包，脑暴、规划、执行 | 复杂项目讨论和方案设计 | [查看](top-10/06-superpowers.md) |
| 7 | **Rube MCP** | 连接 500+ 应用（Slack、GitHub、Notion） | 多应用集成 | [查看](top-10/07-rube-mcp.md) |
| 8 | **宝玉 Skills** | 长文配图、自动发帖、发公众号 | 自媒体创作 | [查看](top-10/08-baoyu-skills.md) |
| 9 | **自媒体 Skills** | 选题、写脚本、写文案、数据分析 | 自媒体工作流 | [查看](top-10/09-media-skills.md) |
| 10 | **Skill Lookup** | 发现、检索和安装 Skills | Skills 管理 | [查看](top-10/10-skill-lookup.md) |

📦 **一键安装 Top 10**:
```bash
bash scripts/install_top10.sh
```

👉 [查看 Top 10 完整列表和对比](top-10/)

---

## 🔍 社区 Skills 分类导航

100+ 精选社区 Skills，按使用场景分类。

### 分类概览

| 分类 | Skills 数量 | 典型应用 | 查看详情 |
|------|------------|---------|---------|
| 📄 **文档处理** | 15+ | Word、PDF、Excel、PPT 处理 | [查看](community/document-processing.md) |
| 💻 **开发工具** | 30+ | 代码质量、测试、架构、MCP | [查看](community/development.md) |
| ☁️ **AWS 云平台** | 3 | 成本优化、CDK 开发、监控运维 | [查看](community/aws-skills/) |
| 📊 **数据分析** | 10+ | CSV 分析、数据库、可视化 | [查看](community/data-analysis.md) |
| 💼 **商业营销** | 12+ | 品牌、广告、领英、域名 | [查看](community/business-marketing.md) |
| ✍️ **沟通写作** | 8+ | 内容创作、会议分析、研究 | [查看](community/communication-writing.md) |
| 🎨 **创意媒体** | 10+ | 图片、视频、主题、Canvas | [查看](community/creative-media.md) |
| 🗂️ **生产力工具** | 12+ | 文件整理、简历、发票、持续改进 | [查看](community/productivity.md) |
| 👥 **协作管理** | 6+ | Git 工作流、代码审查、项目管理 | [查看](community/collaboration.md) |
| 🔒 **安全系统** | 8+ | 取证分析、威胁狩猎、元数据提取 | [查看](community/security.md) |

👉 [浏览完整社区分类](community/)

---

## 📦 官方 Skills

Anthropic 官方发布的文档处理套件，质量保证。

| Skill | 功能 | 仓库链接 |
|-------|------|---------|
| **docx** | Word 文档读写、格式化 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/docx) |
| **pdf** | PDF 提取、合并、注释 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| **pptx** | PPT 生成和编辑 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| **xlsx** | Excel 操作、图表生成 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/xlsx) |

👉 [查看官方 Skills 详细说明](official/)

---

## 📚 深度指南

从入门到精通的完整学习路径。

### 入门指南

| 指南 | 内容 | 适合人群 |
|------|------|---------|
| [快速入门](getting-started.md) | 5 分钟上手，安装第一个 Skill | 新手 |
| [统一安装指南](installation-guide.md) | 三种安装方式详解 | 所有用户 |

### 进阶指南

| 指南 | 内容 | 适合人群 |
|------|------|---------|
| [创建自定义 Skills](guides/creating-custom-skills.md) | 完整的 Skill 开发教程 | 开发者 |
| [编程使用 Skills](guides/programming-usage.md) | Python/Node.js SDK 使用 | 开发者 |
| [Skills vs MCP vs Commands](guides/skills-vs-mcp-vs-commands.md) | 三种扩展方式对比和选择 | 架构师 |
| [最佳实践](guides/best-practices.md) | Skill 设计和优化技巧 | 高级用户 |
| [故障排除](guides/troubleshooting.md) | 常见问题解决方案 | 所有用户 |

---

## 🔧 编程使用

通过 API 集成 Skills 到你的应用。

### Python SDK 示例

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    skills=["pdf", "docx"],  # 指定加载的 skills
    messages=[{"role": "user", "content": "分析这个 PDF 文件"}]
)
```

### Node.js SDK 示例

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

const response = await client.messages.create({
  model: "claude-sonnet-4-20250514",
  skills: ["pdf", "docx"],
  messages: [{ role: "user", content: "分析这个 PDF 文件" }],
});
```

👉 [查看完整编程指南](guides/programming-usage.md)

---

## 🛠️ 创建自定义 Skill

### 基础结构

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

👉 [查看完整创建指南](guides/creating-custom-skills.md)

---

## 📖 资源汇总

### 官方资源

| 资源 | 链接 |
|------|------|
| Skills 功能介绍 | [Anthropic News](https://www.anthropic.com/news/skills) |
| Skills 用户指南 | [Support](https://support.claude.com/en/articles/12512180-using-skills-in-claude) |
| 创建自定义 Skills | [Support](https://support.claude.com/en/articles/12512198-creating-custom-skills) |
| Skills API 文档 | [Claude Code Docs](https://code.claude.com/docs/en/skills) |

### 中文教程

| 资源 | 链接 |
|------|------|
| 知乎 - 最佳实践中文版 | [查看](https://zhuanlan.zhihu.com/p/1973059671540663242) |
| 知乎 - Skills 深度解析 | [查看](https://zhuanlan.zhihu.com/p/1966598753134842902) |
| 七牛开发者中心 | [查看](https://developer.qiniu.com/aitokenapi/13171/claude-code-skill-introduce) |
| Claude Code 中文教程 | [查看](https://claudecode.tangshuang.net/tutorial/14.1) |

### GitHub 热门项目

| 项目 | 说明 |
|------|------|
| [anthropics/skills](https://github.com/anthropics/skills) | 官方 skills 仓库 |
| [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 精选 skills 列表（100+） |
| [claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) | Skill 构建工具包 |
| [obra/superpowers](https://github.com/obra/superpowers) | 核心开发 skills |
| [SkillsMP.com](https://skillsmp.com/) | Skills 搜索平台（25000+） |

👉 [查看完整资源列表](resources/)

---

## ❓ 常见问题

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

👉 [查看完整故障排除指南](guides/troubleshooting.md)

---

## 🗺️ 导航

### 本专区导航

| 目录 | 说明 |
|------|------|
| [Top 10 推荐](top-10/) | 10 个精选 Skills 详细安装指南 |
| [官方 Skills](official/) | Anthropic 官方文档处理套件 |
| [社区分类](community/) | 100+ 社区 Skills 分类索引 |
| [深度指南](guides/) | 创建、使用、优化 Skills 的完整教程 |
| [资源汇总](resources/) | 官方文档、中文教程、GitHub 仓库 |
| [安装脚本](scripts/) | 一键安装、验证工具 |

### 快速链接

- [快速入门（5分钟）](getting-started.md)
- [安装指南（详细版）](installation-guide.md)
- [一键安装 Top 10](scripts/install_top10.sh)
- [创建自定义 Skill](guides/creating-custom-skills.md)
- [故障排除](guides/troubleshooting.md)

### 返回主站

- [返回主 README](../README.md)
- [查看快速参考](../skills.md)
- [文档索引](../docs/INDEX.md)

---

## 📊 统计数据

- **Top 10 精选**: 10 个核心推荐 Skills
- **社区分类**: 9 大类，100+ 精选 Skills
- **官方 Skills**: 4 个文档处理套件
- **深度指南**: 5 篇完整教程
- **资源汇总**: 官方文档、中文教程、GitHub 仓库

---

## 🎯 使用建议

### 新手用户（5-10 分钟）
1. 阅读"什么是 Skills"章节，理解基本概念
2. 查看 Top 10 推荐，选择感兴趣的 1-2 个
3. 使用一键安装脚本或手动安装
4. 启动 Claude Code 测试

### 进阶用户（30-60 分钟）
1. 浏览社区分类，发现更多 Skills
2. 阅读"创建自定义 Skills"指南
3. 学习编程使用 Skills
4. 了解 Skills vs MCP vs Commands 的区别

### 高级用户（深入研究）
1. 研究 Skills 最佳实践
2. 创建自己的 Skill 并分享
3. 参与社区贡献
4. 探索 Skills 高级用法和组合

---

**最后更新**: 2026-01-29
**维护者**: [weihoop](https://github.com/weihoop)
**反馈**: [GitHub Issues](https://github.com/weihoop/claude-code-guide/issues)

---

💡 **提示**: 如果你只需要快速参考，可以查看 [skills.md](../skills.md)（简化版）。本专区提供详细的安装指南、社区分类、深度教程等完整内容。
