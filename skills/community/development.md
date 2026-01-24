# 开发工具 Skills

30+ 专业开发工具，涵盖代码质量、测试、架构设计、MCP 集成等方面。

## 🌟 精选推荐

| Skill | 功能 | 维护者 | 链接 |
|-------|------|--------|------|
| **MCP Builder** | 创建高质量 MCP 服务器 | awesome-claude-skills | [查看](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/mcp-builder) |
| **Webapp Testing** | Playwright 自动化测试 | awesome-claude-skills | [查看](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/webapp-testing) |
| **Skill Creator** | 创建自定义 Skill | awesome-claude-skills | [查看](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/skill-creator) |
| **test-driven-development** | TDD 开发流程 | obra/superpowers | [查看](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |

---

## 📦 完整列表

### MCP 和集成工具

| Skill | 功能 | 链接 |
|-------|------|------|
| MCP Builder | 创建 MCP 服务器（Python/TypeScript） | [GitHub](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/mcp-builder) |
| Connect | 连接 1000+ 应用（Gmail、Slack、GitHub 等） | [GitHub](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/connect) |

### 测试工具

| Skill | 功能 | 链接 |
|-------|------|------|
| Webapp Testing | Playwright 浏览器自动化测试 | [GitHub](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/webapp-testing) |
| test-driven-development | TDD 开发流程 | [GitHub](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| pypict-claude-skill | PICT 组合测试用例设计 | [GitHub](https://github.com/omkamal/pypict-claude-skill) |

### 代码质量

| Skill | 功能 | 链接 |
|-------|------|------|
| software-architecture | Clean Architecture、SOLID 原则 | [GitHub](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/ddd/skills/software-architecture) |
| prompt-engineering | 提示词工程最佳实践 | [GitHub](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/customaize-agent/skills/prompt-engineering) |
| move-code-quality-skill | Move 语言代码质量检查 | [GitHub](https://github.com/1NickPappas/move-code-quality-skill) |

### 开发流程

| Skill | 功能 | 链接 |
|-------|------|------|
| finishing-a-development-branch | 完成开发分支的工作流 | [GitHub](https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch) |
| using-git-worktrees | Git worktrees 管理 | [GitHub](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/) |
| subagent-driven-development | 子代理驱动开发（SADD） | [GitHub](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/sadd/skills/subagent-driven-development) |

### 前端开发

| Skill | 功能 | 链接 |
|-------|------|------|
| artifacts-builder | 创建复杂 HTML Artifacts（React + Tailwind） | [GitHub](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) |
| D3.js Visualization | D3 数据可视化 | [GitHub](https://github.com/chrisvoncsefalvay/claude-d3js-skill) |

### 移动开发

| Skill | 功能 | 链接 |
|-------|------|------|
| iOS Simulator | iOS Simulator 交互 | [GitHub](https://github.com/conorluddy/ios-simulator-skill) |

### 云服务

| Skill | 功能 | 链接 |
|-------|------|------|
| aws-skills | AWS CDK、Serverless 架构 | [GitHub](https://github.com/zxkane/aws-skills) |

### 调试和监控

| Skill | 功能 | 链接 |
|-------|------|------|
| LangSmith Fetch | LangChain/LangGraph 调试 | [GitHub](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/langsmith-fetch) |
| Claude Code Terminal Title | 终端窗口动态标题 | [GitHub](https://github.com/bluzername/claude-code-terminal-title) |

### 工具类

| Skill | 功能 | 链接 |
|-------|------|------|
| Skill Creator | 创建自定义 Skill | [GitHub](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/skill-creator) |
| Skill Seekers | 文档网站转 Skill | [GitHub](https://github.com/yusufkaraaslan/Skill_Seekers) |
| Changelog Generator | 从 git 提交生成变更日志 | [GitHub](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/changelog-generator) |
| reddit-fetch | Reddit 内容获取 | [GitHub](https://github.com/ykdojo/claude-code-tips/tree/main/skills/reddit-fetch) |

### 安全测试

| Skill | 功能 | 链接 |
|-------|------|------|
| FFUF Web Fuzzing | Web 模糊测试 | [GitHub](https://github.com/jthack/ffuf_claude_skill) |
| Playwright Browser Automation | 浏览器自动化 | [GitHub](https://github.com/lackeyjb/playwright-skill) |

---

## 💡 使用场景

### 场景 1：创建 MCP 服务器

```
用户: "使用 mcp-builder 创建一个 GitHub API 的 MCP 服务器"

Claude:
1. 分析 GitHub API 文档
2. 生成 MCP 服务器骨架
3. 实现核心功能（Issues、PRs、Commits）
4. 添加错误处理和日志
5. 生成测试用例

✅ MCP 服务器已创建：github-mcp
```

### 场景 2：自动化测试

```
用户: "为这个登录页面编写 Playwright 测试"

Claude: [使用 webapp-testing skill]
生成测试用例：
- 正常登录流程
- 错误密码处理
- 表单验证
- 会话管理
```

### 场景 3：TDD 开发

```
用户: "使用 TDD 开发一个用户管理功能"

Claude: [使用 test-driven-development skill]
1. 编写测试用例（红）
2. 实现最小代码（绿）
3. 重构优化（重构）
4. 重复循环
```

### 场景 4：代码架构优化

```
用户: "使用 Clean Architecture 重构这个项目"

Claude: [使用 software-architecture skill]
分析现有架构 → 识别问题 → 提出改进方案 → 逐步重构
```

---

## 🔧 最佳实践

### 1. MCP 服务器开发

```
推荐流程：
1. 使用 mcp-builder skill 生成骨架
2. 实现核心功能
3. 使用 webapp-testing 测试
4. 使用 langsmith-fetch 调试
5. 发布到 MCP Market
```

### 2. 测试策略

```
测试金字塔：
- 单元测试：70%（test-driven-development）
- 集成测试：20%（webapp-testing）
- E2E 测试：10%（Playwright）
```

### 3. 代码质量

```
质量检查清单：
□ 使用 software-architecture 检查架构
□ 使用 prompt-engineering 优化提示词
□ 使用 test-driven-development 保证测试覆盖
□ 使用 changelog-generator 生成变更日志
```

---

## 📖 参考资料

### 官方资源

- [artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder)

### 社区精选

- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [superpowers](https://github.com/obra/superpowers)
- [context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit)

---

**返回**: [社区导航](README.md) | [主页](../README.md)
