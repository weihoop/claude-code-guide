# Claude Code 中文使用手册

<div align="center">

**完整的 Claude Code 中文学习指南和参考文档**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Latest-blue.svg)](https://claude.com/claude-code)
[![中文文档](https://img.shields.io/badge/语言-中文-red.svg)](README.md)

[📖 完整文档索引](docs/INDEX.md) • [🚀 快速开始](#快速开始) • [📚 实战案例](#实战案例) • [🔗 官方资源](#官方资源)

</div>

---

## 📖 关于本项目

本项目是一个**非官方**的 Claude Code 中文使用手册，旨在帮助中文用户更好地理解和使用 Claude Code。

### 项目特点

- ✅ **完全中文** - 所有文档均为中文编写
- ✅ **实战导向** - 包含大量实际案例和最佳实践

---

## 🚀 快速开始

### 🎯 从0到1完整指南

**新手必读！** 完整的安装、配置和项目模板教程。

👉 [**查看完整指南**](docs/getting-started/README.md)

#### 三步快速上手

| 步骤 | 内容 | 文档 | 时间 |
|------|------|------|------|
| 1️⃣ | **安装 Claude Code** | [安装指南](docs/getting-started/installation.md) | 10分钟 |
| 2️⃣ | **配置全局设置** | [全局配置](docs/getting-started/global-configuration.md) | 20分钟 |
| 3️⃣ | **创建项目配置** | [项目模板](docs/templates/) | 15分钟 |

#### 项目配置模板

根据你的项目类型选择合适的模板：

| 项目类型 | 适用场景 | 模板文档 |
|---------|---------|---------|
| 🐍 **Python/Shell** | 运维自动化、脚本工具 | [查看模板](docs/templates/python-shell-project.md) |
| ⚛️ **Next.js** | 全栈 Web 应用、SSR/SSG | [查看模板](docs/templates/nextjs-project.md) |
| 📚 **文档库** | 技术文档、API 文档 | [查看模板](docs/templates/documentation-project.md) |

### 什么是 Claude Code？

Claude Code 是 Anthropic 推出的官方 AI 编程助手 CLI 工具，可以帮助开发者：
- 📝 编写和修改代码
- 🔍 理解和分析代码库
- 🐛 调试和修复问题
- 📚 生成文档和注释
- 🧪 编写测试用例

### 快速安装

```bash
# 使用 npm 安装
npm install -g @anthropic-ai/claude-code

# 验证安装
claude --version

# 启动 Claude Code
claude
```

详细安装步骤请查看：[安装指南](docs/getting-started/installation.md)

### 📦 一键安装配置包（推荐）

**开箱即用的 Claude Code 配置**，包含权限设置和 8 个常用命令。

#### 下载安装

```bash
# 从 GitHub Release 下载最新版本
wget https://github.com/weihoop/claude-code-guide/releases/latest/download/claude-config.tar.gz

# 解压
tar -xzf claude-config.tar.gz
cd claude-config

# 运行安装脚本（自动备份、交互式安装）
bash install.sh
```

#### 配置包包含

| 内容 | 说明 |
|------|------|
| ⚙️ **settings.json** | 两个版本：精简版（新手）/ 完整版（进阶） |
| 📝 **CLAUDE.md** | 全局配置模板（代码规范、Git提交规范等） |
| 🎯 **8个斜杠命令** | /test、/review、/build、/push、/fix、/update、/deploy、/doc |
| 🛠️ **安装脚本** | 自动备份、交互式选择、日志记录 |

#### 手动配置

如果你想自己配置，请查看：
- [全局配置指南](docs/getting-started/global-configuration.md) - 详细的权限配置说明
- [项目模板](docs/templates/) - 不同类型项目的配置模板

---

## 📚 完整文档

### 📖 核心手册

| 文档 | 说明 | 适合人群 |
|------|------|----------|
| [**基础使用手册**](basic-guide.md) | 安装、配置、Mode 切换、文件操作、基本命令 | 新手入门 |
| [**进阶使用手册**](advanced-guide.md) | Skill、MCP、Hooks、自动编程、Agent SDK | 进阶用户 |
| [**最佳实践**](best-practices.md) | Token 优化、安全性、团队协作、性能调优 | 所有用户 |
| [**安全使用手册**](security-guide.md) | 敏感信息保护、权限安全、代码审查、应急响应 | ⭐ 必读 |

### 📂 专题指南

#### 配置与权限
- [**权限配置完整指南**](docs/configuration/permissions.md) - `/permissions` 命令详解
  - 全局配置 vs 项目配置
  - 权限规则语法和最佳实践
  - 5 个实用配置案例
  - 10 个常见问题解答

#### 开发范式与规范
- [**Claude Code 编程最佳实践**](docs/claude-code-best-practices.md) - 完整的开发规范和工作流
  - 项目文件组织（.claude.md、SPEC.md、CHANGELOG.md）
  - 权限配置最佳实践
  - 10个必备自定义命令详解
  - 完整的 CI/CD 配置
  - 测试规范和代码规范
- [**SPEC 范式编程指南**](docs/spec-driven-development.md) - 规格驱动开发完整实践
  - SPEC 优先的开发流程
  - 完整的 SPEC 文档模板和示例
  - 与 Claude Code 深度配合
  - 提升 40%+ 开发效率
- [**快速参考卡**](docs/quick-reference.md) - 一页纸速查核心配置和工作流

#### 性能与优化
- [**上下文管理最佳实践**](docs/best-practices/context-management.md) - 减少 Token 消耗，提升开发效率
  - `/compact` vs `/clear` 完整对比
  - 5 个核心优化方案
  - 推荐工作流和任务管理策略
  - 大文件处理和长会话管理
  - 常见问题解答和快速参考卡片

#### 实战案例
- [**SPEC 实战案例集**](docs/examples/spec-examples.md) - 5种项目类型的完整 SPEC 示例
  - CLI 工具（代码检查器）
  - RESTful API（博客系统）
  - NPM 包（日期处理库）
  - 数据处理（日志分析）
  - 实时应用（聊天系统）
- [**真实项目最佳实践**](docs/examples/real-world-cases.md) - 5个真实项目的完整经验
  - 运维监控平台（5人团队）
  - 电商后台系统（8人团队）
  - 技术博客网站（个人项目）
  - 数据分析工具（Python）
  - 开源 NPM 包（社区项目）

#### 资源与参考
- [**完整文档索引**](docs/INDEX.md) - 按难度、场景、主题分类的完整导航 ⭐
- [**官方资源索引**](docs/resources/official-resources.md) - 官方文档、GitHub 仓库、SDK、社区资源
- [**Claude Skills 使用指南**](skills.md) - Skills 系统完整教程，包含编程使用和创建自定义 Skill
- [**使用限制变化记录（2026年1月）**](docs/claude-code-usage-limits-jan-2026.md) - 了解最新的使用限制和应对策略

### 🎯 快速查阅

#### 基础功能
- [安装和启动](basic-guide.md#安装和启动) - 系统要求、安装步骤
- [基本界面](basic-guide.md#基本界面) - 界面组成、快捷键
- [核心概念](basic-guide.md#核心概念) - 工具、上下文、权限
- [文件操作](basic-guide.md#文件操作) - Read、Edit、Write、查找
- [Mode 切换](basic-guide.md#mode-切换) - Plan Mode vs Build Mode

#### 进阶功能
- [自定义命令](advanced-guide.md#自定义-slash-commands) - 创建项目专属命令
- [Skill 系统](advanced-guide.md#skill-系统) - 创建和使用 Skill
- [MCP 集成](advanced-guide.md#mcp-服务器集成) - 安装配置 MCP 服务器
- [Hooks 配置](advanced-guide.md#hooks-高级配置) - 自定义执行钩子
- [自动编程](advanced-guide.md#自动编程工作流) - 自动化开发流程
- [Agent SDK](advanced-guide.md#agent-sdk-开发) - 开发自定义 Agent

#### 安全使用
- [敏感信息保护](security-guide.md#敏感信息保护) - 环境变量、密钥管理、泄露检测
- [权限配置安全](security-guide.md#权限配置安全) - 安全权限模板、验证脚本
- [代码审查安全](security-guide.md#代码审查安全) - SQL注入、XSS、命令注入检查
- [命令执行安全](security-guide.md#命令执行安全) - 危险命令拦截、审计日志
- [应急响应](security-guide.md#应急响应) - 密钥泄露处理、事件报告

#### 优化与实践
- [Token 优化](best-practices.md#token-使用优化) - 10 个 Token 节省策略
- [提示词技巧](best-practices.md#提示词最佳实践) - 编写高效提示词
- [团队协作](best-practices.md#团队协作规范) - 多人协作配置
- [问题排查](best-practices.md#调试和问题排查) - 常见问题解决
- [编程范式速查](docs/quick-reference.md) - 核心文件、命令、配置速查表

---

## 🎯 核心功能

### 1. 智能代码编写

```bash
# 示例：创建一个 REST API
> 帮我创建一个用户管理的 REST API，包括 CRUD 操作
```

### 2. 代码审查和优化

```bash
# 使用 /review 命令
/review

# 安全审查
/security-review
```

### 3. 项目初始化

```bash
# 初始化项目文档
/init
```

### 4. 权限管理

```bash
# 管理工具访问权限
/permissions
```

---

## 🧩 Skills 技能系统

Skills 是 Claude Code 最强大的扩展机制，让 Claude 自动执行专业化的工作流。

### 什么是 Skills？

| 特性 | 说明 |
|------|------|
| **自动触发** | Claude 根据上下文自动激活相关 skill |
| **渐进式加载** | 按需加载，节省 Token |
| **跨平台** | Claude.ai、Claude Code、API 通用 |

### Skills vs MCP vs Slash Commands

| 特性 | Skills | MCP | Slash Commands |
|------|--------|-----|----------------|
| 触发方式 | 自动 | 手动 | 手动输入 /xxx |
| 关注点 | 流程方法 | 外部访问 | 快捷操作 |
| Token 效率 | 高 | 中 | 低 |

### 安装 Skill

```bash
# 1. 创建 skills 目录
mkdir -p ~/.claude/skills/

# 2. 复制 skill 到目录
cp -r my-skill ~/.claude/skills/

# 3. 启动 Claude Code，自动加载
claude
```

### 热门 Skills 推荐

| Skill | 用途 | 来源 |
|-------|------|------|
| [docx/pdf/pptx](https://github.com/anthropics/skills) | 文档处理 | 官方 |
| [mcp-builder](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/mcp-builder) | 创建 MCP 服务器 | 社区 |
| [skill-creator](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/skill-creator) | 创建新 skill | 社区 |
| [webapp-testing](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/webapp-testing) | Playwright 测试 | 社区 |

👉 **[查看完整 Skills 指南](skills.md)** - 从 0 到 1 学习、编程使用、创建自定义 Skill

---

## ⚙️ 配置指南

### 全局配置文件

位置：`~/.claude/settings.json`

```json
{
  "permissions": {
    "allow": ["Read", "Grep", "Glob"],
    "ask": ["Edit", "Write", "Bash(git commit:*)"],
    "deny": ["Bash(sudo:*)", "Bash(rm:*)", "Read(.env*)"]
  }
}
```

### 项目配置文件

位置：`.claude/settings.json`（团队共享，提交到 git）

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run test:*)",
      "Edit(/src/**)"
    ],
    "deny": [
      "Read(.env*)",
      "Edit(/node_modules/**)"
    ]
  }
}
```

位置：`.claude/settings.local.json`（个人配置，不提交）

```json
{
  "permissions": {
    "allow": ["Read(.env.local)"]
  }
}
```

详细配置说明请参考：[权限配置完整指南](docs/configuration/permissions.md)

---

## 📋 配置案例

### 前端项目

适用于 React/Vue/Angular 等前端项目

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run dev:*)",
      "Bash(npm run test:*)",
      "Edit(/src/**)",
      "Read"
    ],
    "ask": ["Bash(git commit:*)", "Bash(npm install:*)"],
    "deny": ["Bash(rm:*)", "Read(.env*)", "Edit(/node_modules/**)"]
  }
}
```

### Python 项目

适用于数据科学、机器学习项目

```json
{
  "permissions": {
    "allow": [
      "Bash(python:*)",
      "Bash(pip install:*)",
      "Bash(pytest:*)",
      "Edit(/src/**)",
      "Edit(/notebooks/**)"
    ],
    "ask": ["Edit(/data/**)"],
    "deny": ["Read(.env*)", "Edit(/data/raw/**)"]
  }
}
```

### 严格安全项目

适用于生产环境、敏感项目

```json
{
  "permissions": {
    "allow": ["Read(/src/**)", "Read(/tests/**)"],
    "ask": [
      "Edit(/src/**)",
      "Bash(git:*)",
      "Bash(npm:*)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(sudo:*)",
      "Read(.env*)",
      "Read(/secrets/**)",
      "Write"
    ]
  }
}
```

更多案例请参考：[权限配置完整指南 - 配置案例](docs/configuration/permissions.md#配置案例)

---

## 🔗 官方资源

### 官方文档

- 📘 [Claude Code 官方文档](https://code.claude.com/docs/)
- 🔧 [Agent SDK 文档](https://docs.claude.com/en/api/)
- 💬 [Claude 官方网站](https://www.anthropic.com/)

### GitHub 仓库

- 🐙 [Claude Code GitHub](https://github.com/anthropics/claude-code)
- 📦 [Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- 📦 [Node.js SDK](https://github.com/anthropics/anthropic-sdk-nodejs)

### 问题反馈

- 🐛 [报告问题](https://github.com/anthropics/claude-code/issues)
- 💡 [功能建议](https://github.com/anthropics/claude-code/discussions)

完整资源列表：[官方资源索引](docs/resources/official-resources.md)

---

## 🤝 贡献指南

欢迎贡献！您可以：

1. **提交问题** - 发现错误或有疑问
2. **改进文档** - 完善现有文档
3. **添加案例** - 分享您的使用经验
4. **翻译内容** - 帮助翻译官方文档

### 贡献流程

```bash
# 1. Fork 本项目
# 2. 克隆到本地
git clone https://github.com/YOUR_USERNAME/claude-code-guide.git

# 3. 创建分支
git checkout -b feature/your-feature

# 4. 提交更改
git add .
git commit -m "feat: 添加新功能说明"

# 5. 推送到远程
git push origin feature/your-feature

# 6. 创建 Pull Request
```

### 提交规范

```bash
feat: 添加新功能
fix: 修复文档错误
docs: 更新文档
style: 格式调整
refactor: 重构内容
```

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个 Star！**

Made with ❤️ by the Community

</div>
