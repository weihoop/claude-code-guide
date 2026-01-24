# Rube MCP Connector

通过一个服务器连接 Claude 到 500+ 应用（Slack、GitHub、Notion 等），不用给每个应用单独配置授权。

## 功能简介

Rube MCP 是一个统一的 MCP 连接器，让 Claude 能够访问 500+ 应用和服务，只需一次配置。

### 核心特点

- ✅ **统一授权**: 一次配置，访问所有应用
- ✅ **500+ 应用**: Gmail、Slack、GitHub、Notion、Linear等
- ✅ **简化配置**: 不需要为每个应用单独设置 MCP
- ✅ **云端托管**: Composio 提供托管服务

### 适用场景

| 场景 | 说明 |
|------|------|
| **多应用集成** | 需要同时使用多个 SaaS 工具 |
| **自动化工作流** | 跨应用的自动化任务 |
| **数据同步** | 在不同应用间同步数据 |
| **团队协作** | 统一管理团队使用的工具 |

---

## 仓库信息

- **GitHub**: [ComposioHQ/Rube](https://github.com/composiohq/rube)
- **维护者**: [@ComposioHQ](https://github.com/composiohq)
- **服务提供**: [Composio Platform](https://platform.composio.dev/)

### 参考资料

- [MCP Market - Rube](https://mcpmarket.com/server/rube)
- [npm 包](https://www.npmjs.com/package/@composio/rube-mcp)
- [Rube 解决上下文过载问题](https://composio.dev/blog/rube-mcp-solving-context-overload)

---

## 安装方法

### 使用 MCP 协议安装（推荐）

```bash
# 在终端中执行
claude mcp add --transport http rube -s user "https://rube.app/mcp"
```

### 配置步骤

#### 1. 添加 MCP 服务器

```bash
claude mcp add --transport http rube -s user "https://rube.app/mcp"
```

#### 2. 登录 Rube

在 Claude Code 聊天中运行：

```
/mcp
```

从列表中选择 `rube` 并按回车进行登录。

#### 3. 浏览器认证

- 浏览器会自动打开进行身份验证
- 使用 Google 或 GitHub 账号登录
- 认证后返回 Claude Code

#### 4. 验证连接

再次运行 `/mcp` 确认 rube 已连接：

```
/mcp
> rube ✅ Connected
```

#### 5. 连接应用

```
用户: "连接我的 Gmail 账号"

Claude: [使用 Rube 启动 OAuth 流程]
[浏览器打开，授权 Gmail 访问]
[完成后，可以在 Claude 中使用 Gmail]
```

---

## 支持的应用

### 开发工具

| 应用 | 功能示例 |
|------|---------|
| **GitHub** | 创建 Issue、PR、管理仓库 |
| **GitLab** | CI/CD 管理、代码审查 |
| **Linear** | 任务管理、问题追踪 |
| **Jira** | 项目管理、Sprint 规划 |

### 通信工具

| 应用 | 功能示例 |
|------|---------|
| **Slack** | 发送消息、管理频道 |
| **Discord** | 消息、通知、机器人 |
| **Telegram** | 发送消息、管理群组 |

### 办公协作

| 应用 | 功能示例 |
|------|---------|
| **Gmail** | 发送邮件、搜索、标签管理 |
| **Notion** | 创建页面、数据库查询 |
| **Airtable** | 表格操作、数据查询 |
| **Google Drive** | 文件上传、共享 |

### 营销和客户管理

| 应用 | 功能示例 |
|------|---------|
| **HubSpot** | CRM 管理、营销自动化 |
| **Salesforce** | 销售管道、客户数据 |
| **Mailchimp** | 邮件营销、列表管理 |

### 更多应用

查看完整列表：[Composio Apps](https://composio.dev/apps)

---

## 使用示例

### 示例 1：发送 Slack 消息

```
用户: "在 #general 频道发送一条消息：项目已完成"

Claude: [使用 Rube 连接 Slack]
✅ 消息已发送到 #general 频道
```

### 示例 2：创建 GitHub Issue

```
用户: "在 myrepo 创建一个 Issue：修复登录bug"

Claude: [使用 Rube 连接 GitHub]
✅ Issue #123 已创建
标题：修复登录bug
链接：https://github.com/user/myrepo/issues/123
```

### 示例 3：更新 Notion 数据库

```
用户: "在 Notion 的任务数据库中添加一条记录"

Claude: [使用 Rube 连接 Notion]
✅ 记录已添加
页面：[链接]
```

### 示例 4：跨应用工作流

```
用户: "从 Gmail 读取最新邮件，总结后发送到 Slack #team 频道"

Claude:
1. [连接 Gmail] 读取最新邮件
2. [总结邮件内容]
3. [连接 Slack] 发送总结到 #team 频道

✅ 完成！总结已发送到 Slack
```

---

## 进阶使用

### 批量操作

```
用户: "从 Airtable 读取所有待办任务，为每个任务在 Linear 创建 Issue"

Claude: [批量处理]
从 Airtable 读取：15 个任务
创建 Linear Issues：
  ✅ TASK-1
  ✅ TASK-2
  ...
  ✅ TASK-15
完成！
```

### 定时任务

结合 Cron 或其他调度工具：

```bash
# 每天早上 9 点发送昨日 GitHub 活动摘要到 Slack
0 9 * * * claude "总结昨天的 GitHub 活动并发送到 Slack #dev-updates"
```

### 数据同步

```
用户: "将 Notion 中的项目数据同步到 Airtable"

Claude:
1. 从 Notion 读取项目数据
2. 转换数据格式
3. 写入 Airtable

✅ 同步完成：10 个项目
```

---

## 安全和隐私

### OAuth 认证

- ✅ 使用官方 OAuth 流程，不保存密码
- ✅ 可随时撤销访问权限
- ✅ Token 加密存储

### 数据隐私

- ✅ 数据传输加密（HTTPS）
- ✅ 不存储敏感数据
- ⚠️ 数据通过 Composio 服务器中转

### 权限管理

仅请求必要的权限：

```
Gmail: 只读邮件、发送邮件
Slack: 发送消息、读取频道
GitHub: 创建 Issue、管理仓库
```

---

## 常见问题

### Rube 和普通 MCP 的区别

```
普通 MCP:
- 每个应用单独配置
- 需要管理多个 MCP 服务器
- 配置复杂

Rube MCP:
- 统一配置入口
- 一个 MCP 服务器访问所有应用
- 配置简单
```

### 认证失败

**解决方法**:
1. 检查网络连接
2. 清除浏览器缓存
3. 重新运行 `/mcp` 认证
4. 检查 Composio 平台状态

### 应用连接失败

**解决方法**:
1. 确认已授权该应用
2. 检查 OAuth token 是否过期
3. 重新授权应用访问
4. 查看 Composio 控制台的日志

### 速率限制

**问题**: 请求过于频繁被限制

**解决方法**:
- 添加延迟（batch 操作）
- 检查 Composio 的配额
- 升级 Composio 计划（如需要）

---

## 定价

### Composio 平台定价

| 计划 | 价格 | 包含 |
|------|------|------|
| **Free** | $0 | 基础应用访问 |
| **Pro** | $29/月 | 更多请求、优先支持 |
| **Enterprise** | 联系销售 | 自定义配额、SLA |

查看最新定价：[Composio Pricing](https://platform.composio.dev/pricing)

---

## 参考资料

### 官方资源

- [Rube GitHub](https://github.com/composiohq/rube)
- [Composio 平台](https://platform.composio.dev/)
- [Composio 文档](https://docs.composio.dev/)

### MCP 相关

- [MCP Market](https://mcpmarket.com/server/rube)
- [MCP 协议文档](https://modelcontextprotocol.io/)

### 应用集成指南

- [Gmail 集成](https://docs.composio.dev/apps/gmail)
- [Slack 集成](https://docs.composio.dev/apps/slack)
- [GitHub 集成](https://docs.composio.dev/apps/github)

---

**最后更新**: 2026-01-24
**难度**: ⭐⭐ 中等
**推荐指数**: ⭐⭐⭐⭐

[返回 Top 10 列表](README.md) | [返回主页](../README.md)
