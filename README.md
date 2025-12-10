# Claude Code 中文使用手册

<div align="center">

**完整的 Claude Code 中文学习指南和参考文档**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Latest-blue.svg)](https://claude.com/claude-code)
[![中文文档](https://img.shields.io/badge/语言-中文-red.svg)](README.md)

[快速开始](#快速开始) • [功能特性](#功能特性) • [配置指南](#配置指南) • [官方资源](#官方资源)

</div>

---

## 📖 关于本项目

本项目是一个**非官方**的 Claude Code 中文使用手册，旨在帮助中文用户更好地理解和使用 Claude Code。

### 项目特点

- ✅ **完全中文** - 所有文档均为中文编写
- ✅ **实战导向** - 包含大量实际案例和最佳实践
- ✅ **持续更新** - 跟随 Claude Code 官方版本更新
- ✅ **社区驱动** - 欢迎贡献和反馈

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
- [**快速参考卡**](docs/quick-reference.md) - 一页纸速查核心配置和工作流

#### 资源与参考
- [**官方资源索引**](docs/resources/official-resources.md) - 官方文档、GitHub 仓库、SDK、社区资源

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
