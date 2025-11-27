# Claude Code 官方资源索引

> 本文档汇总了 Claude Code 和相关工具的所有官方资源链接

---

## 📚 目录

- [官方文档](#官方文档)
- [GitHub 仓库](#github-仓库)
- [SDK 和 API](#sdk-和-api)
- [技术架构](#技术架构)
- [社区资源](#社区资源)
- [问题反馈](#问题反馈)

---

## 📘 官方文档

### Claude Code 文档

| 资源 | 链接 | 说明 |
|------|------|------|
| 官方主文档 | https://code.claude.com/docs/ | Claude Code 完整文档入口 |
| 文档地图 | https://code.claude.com/docs/en/claude_code_docs_map.md | 文档结构导航 |
| 中文文档 | https://code.claude.com/docs/zh/ | 中文版文档（如可用） |

### Agent SDK 文档

| 资源 | 链接 | 说明 |
|------|------|------|
| SDK 主文档 | https://docs.claude.com/en/api/ | Agent SDK 完整文档 |
| SDK 文档地图 | https://docs.claude.com/en/api/agent_sdk_docs_map.md | SDK 文档结构 |

### Anthropic 官方网站

| 资源 | 链接 | 说明 |
|------|------|------|
| 主网站 | https://www.anthropic.com/ | Anthropic 公司官网 |
| Claude 产品页 | https://claude.com/ | Claude 产品介绍 |
| Claude Code 页面 | https://claude.com/claude-code | Claude Code 产品页面 |
| 研究与资源 | https://www.anthropic.com/research | 官方研究和博客 |
| API 文档 | https://docs.anthropic.com/ | Anthropic API 完整文档 |
| 模型信息 | https://docs.anthropic.com/en/docs/models | Claude 模型规格和能力 |

---

## 🐙 GitHub 仓库

### 官方仓库

| 仓库 | 链接 | 说明 |
|------|------|------|
| Anthropic GitHub | https://github.com/anthropics/ | Anthropic 官方组织 |
| Claude Code | https://github.com/anthropics/claude-code | Claude Code 主仓库 |
| Python SDK | https://github.com/anthropics/anthropic-sdk-python | Python 官方 SDK |
| Node.js SDK | https://github.com/anthropics/anthropic-sdk-nodejs | Node.js 官方 SDK |
| TypeScript SDK | https://github.com/anthropics/anthropic-sdk-typescript | TypeScript 官方 SDK |

### 示例和模板

| 仓库 | 链接 | 说明 |
|------|------|------|
| Cookbook | https://github.com/anthropics/anthropic-cookbook | 官方示例代码集合 |
| Quickstart | https://github.com/anthropics/anthropic-quickstarts | 快速入门项目模板 |

---

## 🔧 SDK 和 API

### API 文档

| 资源 | 链接 | 说明 |
|------|------|------|
| API 参考 | https://docs.anthropic.com/en/api/ | 完整 API 参考文档 |
| API 密钥管理 | https://console.anthropic.com/ | Anthropic Console |
| 使用限制 | https://docs.anthropic.com/en/api/rate-limits | API 速率限制说明 |
| 定价信息 | https://www.anthropic.com/pricing | API 定价详情 |

### SDK 安装

#### Python SDK

```bash
# 安装
pip install anthropic

# 文档
# https://github.com/anthropics/anthropic-sdk-python
```

#### Node.js SDK

```bash
# 安装
npm install @anthropic-ai/sdk

# 文档
# https://github.com/anthropics/anthropic-sdk-nodejs
```

#### TypeScript SDK

```bash
# 安装
npm install @anthropic-ai/sdk-typescript

# 文档
# https://github.com/anthropics/anthropic-sdk-typescript
```

---

## 🏗️ 技术架构

### Claude Code 核心组件

| 组件 | 说明 |
|------|------|
| **SDK Core** | SDK 核心框架 |
| **Tools API** | 工具调用接口系统 |
| **Model Integration** | 模型集成层 |
| **Agent Loop** | Agent 循环执行引擎 |
| **Context Management** | 上下文管理系统 |

### 可用工具

| 工具 | 说明 |
|------|------|
| `Bash` | Bash 命令执行 |
| `Read` | 文件读取 |
| `Edit` | 文件编辑 |
| `Write` | 文件创建 |
| `Grep` | 代码搜索 |
| `Glob` | 文件查找 |
| `WebFetch` | 网页获取 |
| `WebSearch` | 网络搜索 |
| `Task` | 子任务代理 |

### 主要功能模块

| 功能 | 说明 |
|------|------|
| **Plan 模式** | 任务规划和设计 |
| **Build 模式** | 代码编写和修改 |
| **REPL** | 实时交互环境 |
| **Terminal 集成** | 终端命令集成 |
| **Hooks 系统** | 自定义钩子 |
| **Slash Commands** | 自定义斜杠命令 |
| **MCP 集成** | Model Context Protocol |
| **权限管理** | 工具访问控制 |

---

## 🌐 社区资源

### 官方社区

| 平台 | 链接 | 说明 |
|------|------|------|
| Discord | https://discord.gg/anthropic | 官方 Discord 社区 |
| Twitter/X | https://twitter.com/AnthropicAI | Anthropic 官方推特 |
| LinkedIn | https://www.linkedin.com/company/anthropic | Anthropic 领英页面 |

### 学习资源

| 资源 | 链接 | 说明 |
|------|------|------|
| 官方博客 | https://www.anthropic.com/news | Anthropic 官方博客 |
| 研究论文 | https://www.anthropic.com/research | 技术研究论文 |
| YouTube | https://www.youtube.com/@AnthropicAI | 官方视频教程 |

---

## 🐛 问题反馈

### 报告问题

| 类型 | 渠道 | 链接 |
|------|------|------|
| Bug 报告 | GitHub Issues | https://github.com/anthropics/claude-code/issues |
| 功能建议 | GitHub Discussions | https://github.com/anthropics/claude-code/discussions |
| 安全问题 | 安全邮箱 | security@anthropic.com |
| 一般咨询 | 支持邮箱 | support@anthropic.com |

### 提交规范

#### Bug 报告模板

```markdown
**问题描述**
简要描述遇到的问题

**复现步骤**
1. 执行命令 '...'
2. 看到错误 '...'
3. ...

**预期行为**
描述应该出现的正确行为

**环境信息**
- OS: [例如 macOS 14.0]
- Claude Code 版本: [例如 1.0.0]
- Python/Node 版本: [如适用]

**日志信息**
粘贴相关错误日志
```

#### 功能建议模板

```markdown
**功能描述**
简要描述建议的功能

**使用场景**
描述该功能的使用场景和价值

**可能的实现方式**
如果有想法，描述可能的实现方式

**替代方案**
是否有其他替代方案
```

---

## 📖 文档章节结构

基于官方文档的典型组织结构：

### 快速开始 (Getting Started)

- 安装指南 (Installation)
- 基础设置 (Setup)
- 首个项目 (Your First Project)
- 快速入门教程 (Quick Start Tutorial)

### 核心功能 (Core Features)

- **Plan 模式** (Planning Mode)
  - 任务规划
  - 实现设计
  - 架构决策

- **Build 模式** (Building Mode)
  - 代码生成
  - 代码修改
  - 重构优化

- **Terminal 集成** (Terminal Integration)
  - 命令执行
  - 脚本运行
  - 环境管理

- **Interactive 特性** (Interactive Features)
  - 对话交互
  - 确认机制
  - 实时反馈

### 自定义功能 (Customization)

- **Slash Commands** (斜杠命令)
  - 创建自定义命令
  - 命令参数
  - 命令组织

- **Hooks** (钩子)
  - 执行前钩子
  - 执行后钩子
  - 工具钩子

- **Agent Architecture** (Agent 架构)
  - 自定义 Agent
  - Agent 通信
  - Agent 生命周期

### MCP 集成 (MCP Integration)

- Model Context Protocol 简介
- MCP Server 安装
- MCP Server 配置
- 自定义 MCP Server

### 配置 (Configuration)

- **settings.json** 配置选项
- 环境变量设置
- 项目级配置
- 全局配置
- [权限配置详解](../configuration/permissions.md)

---

## 🔍 快速查询

### 常用链接速查

```bash
# 官方文档
https://code.claude.com/docs/

# GitHub 仓库
https://github.com/anthropics/claude-code

# API 文档
https://docs.anthropic.com/

# 问题反馈
https://github.com/anthropics/claude-code/issues

# Discord 社区
https://discord.gg/anthropic

# Console 控制台
https://console.anthropic.com/
```

### 内置命令参考

| 命令 | 说明 |
|------|------|
| `/help` | 查看所有可用命令 |
| `/permissions` | 管理工具权限 |
| `/context` | 查看当前上下文 |
| `/model` | 查看模型信息 |
| `/init` | 初始化项目文档 |
| `/review` | 代码审查 |
| `/security-review` | 安全审查 |

---

## 📝 相关文档

- [返回主文档](../../README.md)
- [权限配置指南](../configuration/permissions.md)

---

## 📅 更新日志

| 日期 | 版本 | 更新内容 |
|------|------|----------|
| 2025-11-27 | 1.0 | 初始版本，汇总官方资源 |

---

## 🤝 贡献

如果您发现：
- 链接失效或错误
- 缺少重要资源
- 需要更新的信息

欢迎：
1. 提交 Issue
2. 创建 Pull Request
3. 在社区中反馈

---

**最后更新**: 2025-11-27
**维护者**: Claude Code 中文社区
**文档版本**: 1.0
