# Claude Code 完整文档索引

按难度和场景分类的完整文档导航，快速找到你需要的内容。

---

## 📊 按难度分类

### 🌱 入门级（新手必读）

适合第一次接触 Claude Code 的用户。

| 文档 | 内容概述 | 预计时间 |
|------|---------|---------|
| [**从0到1完整指南**](getting-started/README.md) | 安装、配置、第一个项目 | 45分钟 |
| ├─ [安装指南](getting-started/installation.md) | 系统要求、安装步骤、OAuth 认证 | 10分钟 |
| ├─ [全局配置](getting-started/global-configuration.md) | settings.json、CLAUDE.md、自定义命令 | 20分钟 |
| └─ [项目模板](templates/) | Python/Next.js/文档项目模板 | 15分钟 |
| [**基础使用手册**](../basic-guide.md) | Mode 切换、文件操作、基本命令 | 1小时 |
| [**快速参考卡**](quick-reference.md) | 核心文件、命令、配置速查 ⚡ | 5分钟 |

**学习路径**：
```
安装指南 → 全局配置 → 选择项目模板 → 基础使用手册 → 开始开发
```

---

### 🚀 进阶级（有经验用户）

适合已经掌握基础，想要提升效率的用户。

| 文档 | 内容概述 | 适用场景 |
|------|---------|----------|
| [**Claude Code 完整指南（v2.0+）**](claude-code-v3-complete-guide.md) | LSP、CLAUDE.md、MCP、Skills、Context7 完整体系 | 系统学习 ⭐ |
| [**进阶使用手册**](../advanced-guide.md) | Skill、MCP、Hooks、Agent SDK | 深度定制 |
| [**自定义命令详解**](../advanced-guide.md#自定义-slash-commands) | 创建项目专属命令 | 工作流自动化 |
| [**权限配置完整指南**](configuration/permissions.md) | 细粒度权限控制、10+ 配置案例 | 团队协作 |
| [**Claude Code 编程最佳实践**](claude-code-best-practices.md) | 15种核心实践、10个必备命令 | 规范开发 |
| [**LSP / 编辑器集成**](claude-code-best-practices.md#编辑器集成与-lsp) | LSP 启动、常用 server 与 Claude 提示范式 | 提高调试与引用定位效率 |
| [**最佳实践手册**](../best-practices.md) | Token 优化、提示词技巧、团队协作 | 效率提升 |

**学习路径**：
```
进阶手册 → 自定义命令 → 权限配置 → 编程最佳实践 → 团队协作
```

---

### 🎓 专家级（深度使用）

适合追求极致效率和代码质量的用户。

| 文档 | 内容概述 | 价值 |
|------|---------|------|
| [**SPEC 范式编程指南**](spec-driven-development.md) | 规格驱动开发完整实践 | 效率提升 40%+ |
| [**SPEC 实战案例**](examples/spec-examples.md) | 5种项目类型的完整 SPEC 示例 | 可直接复用 |
| [**真实项目案例**](examples/real-world-cases.md) | 5个真实项目的完整实践 | 经验总结 |
| [**安全使用手册**](../security-guide.md) | 敏感信息保护、权限安全、应急响应 | 必读 ⭐ |
| [**Agent SDK 开发**](../advanced-guide.md#agent-sdk-开发) | 开发自定义 Agent | 高度定制 |

**学习路径**：
```
SPEC 范式 → 实战案例 → 真实项目 → 安全手册 → Agent 开发
```

---

## 🎯 按场景分类

### 💻 Web 应用开发

| 场景 | 推荐文档 | 核心内容 |
|------|---------|----------|
| **全栈应用** | [Next.js 模板](templates/nextjs-project.md) | 项目结构、API 设计、前后端规范 |
| **RESTful API** | [博客 API 案例](examples/spec-examples.md#案例2-restful-api博客系统) | API 设计、数据模型、测试用例 |
| **实时应用** | [聊天系统案例](examples/spec-examples.md#案例5-实时应用聊天系统) | WebSocket、消息队列、性能优化 |
| **后台管理** | [电商后台案例](examples/real-world-cases.md#案例2-电商后台管理系统) | 权限管理、订单流程、团队协作 |

**配置建议**：
```json
{
  "permissions": {
    "allow": [
      "Edit(/src/**)",
      "Bash(npm run dev:*)",
      "Bash(npm test:*)"
    ],
    "deny": ["Read(.env*)"]
  }
}
```

---

### 🖥️ CLI 工具开发

| 场景 | 推荐文档 | 核心内容 |
|------|---------|----------|
| **代码扫描** | [CLI 工具案例](examples/spec-examples.md#案例1-cli-工具代码检查器) | 参数解析、规则引擎、报告生成 |
| **数据处理** | [日志分析案例](examples/spec-examples.md#案例4-数据处理日志分析工具) | 大文件处理、性能优化、流式处理 |
| **运维工具** | [监控平台案例](examples/real-world-cases.md#案例1-运维监控平台) | 告警系统、部署脚本、健康检查 |

**配置建议**：
```json
{
  "permissions": {
    "allow": [
      "Edit(/src/**)",
      "Bash(node:*)",
      "Bash(npm test:*)"
    ]
  }
}
```

---

### 📦 库/包开发

| 场景 | 推荐文档 | 核心内容 |
|------|---------|----------|
| **NPM 包** | [日期处理库案例](examples/spec-examples.md#案例3-npm-包日期处理库) | API 设计、类型定义、Tree-shaking |
| **开源项目** | [HTTP Client 案例](examples/real-world-cases.md#案例5-开源-npm-包) | 类型安全、文档生成、发布流程 |

**配置建议**：
```json
{
  "permissions": {
    "allow": [
      "Edit(/src/**)",
      "Edit(/tests/**)",
      "Bash(npm run build:*)",
      "Bash(npm test:*)"
    ],
    "ask": ["Bash(npm publish:*)"]
  }
}
```

---

### 📄 文档/内容项目

| 场景 | 推荐文档 | 核心内容 |
|------|---------|----------|
| **技术博客** | [博客网站案例](examples/real-world-cases.md#案例3-技术博客网站) | MDX 配置、SEO 优化、内容管理 |
| **文档库** | [文档项目模板](templates/documentation-project.md) | VitePress/Docusaurus 配置 |
| **API 文档** | [SPEC 范式指南](spec-driven-development.md) | 文档生成、示例编写 |

**配置建议**：
```json
{
  "permissions": {
    "allow": [
      "Read",
      "Edit(/docs/**)",
      "Edit(/content/**)",
      "Bash(npm run dev:*)"
    ]
  }
}
```

---

### 🔧 运维/DevOps

| 场景 | 推荐文档 | 核心内容 |
|------|---------|----------|
| **监控平台** | [监控平台案例](examples/real-world-cases.md#案例1-运维监控平台) | 告警系统、Webhook、部署流程 |
| **Python 运维** | [Python/Shell 模板](templates/python-shell-project.md) | 脚本规范、错误处理、日志记录 |
| **数据分析** | [数据工具案例](examples/real-world-cases.md#案例4-数据分析工具集) | 日志解析、报表生成、性能优化 |

**配置建议**：
```json
{
  "permissions": {
    "allow": [
      "Edit(/scripts/**)",
      "Bash(python:*)",
      "Bash(docker ps:*)",
      "Bash(docker logs:*)"
    ],
    "ask": [
      "Bash(docker-compose up:*)",
      "Bash(bash scripts/deploy.sh:*)"
    ],
    "deny": [
      "Bash(rm:*)",
      "Bash(sudo:*)"
    ]
  }
}
```

---

## 🎨 按主题分类

### 📝 项目配置

| 主题 | 文档链接 | 说明 |
|------|---------|------|
| **完整配置指南** | [Claude Code 完整指南](claude-code-v3-complete-guide.md) | LSP、CLAUDE.md、MCP、Hooks 全覆盖 ⭐ |
| **.claude.md** | [编程最佳实践](claude-code-best-practices.md#项目配置文件claudemd) | 项目上下文配置 |
| **权限配置** | [权限配置指南](configuration/permissions.md) | settings.json 详解 |
| **自定义命令** | [全局配置](getting-started/global-configuration.md#自定义命令) | commands/*.md 创建 |
| **MCP 集成** | [进阶手册](../advanced-guide.md#mcp-服务器集成) | 外部工具集成 |
| **Hooks** | [进阶手册](../advanced-guide.md#hooks-高级配置) | 自动化钩子 |

---

### 📐 开发规范

| 主题 | 文档链接 | 价值 |
|------|---------|------|
| **SPEC 范式** | [SPEC 编程指南](spec-driven-development.md) | 提升效率 40%+ |
| **Git 规范** | [编程最佳实践](claude-code-best-practices.md#git-提交规范) | 提交格式、分支策略 |
| **测试规范** | [编程最佳实践](claude-code-best-practices.md#测试规范) | 测试结构、覆盖率 |
| **代码规范** | [编程最佳实践](claude-code-best-practices.md#代码规范配置) | ESLint、Prettier |
| **文档规范** | [编程最佳实践](claude-code-best-practices.md#文档维护流程) | README、CHANGELOG |

---

### 🔐 安全使用

| 主题 | 文档链接 | 重要性 |
|------|---------|--------|
| **敏感信息保护** | [安全手册](../security-guide.md#敏感信息保护) | ⭐⭐⭐⭐⭐ |
| **权限安全** | [安全手册](../security-guide.md#权限配置安全) | ⭐⭐⭐⭐⭐ |
| **代码审查** | [安全手册](../security-guide.md#代码审查安全) | ⭐⭐⭐⭐ |
| **命令执行** | [安全手册](../security-guide.md#命令执行安全) | ⭐⭐⭐⭐ |
| **应急响应** | [安全手册](../security-guide.md#应急响应) | ⭐⭐⭐ |

---

### ⚡ 效率提升

| 主题 | 文档链接 | 提升幅度 |
|------|---------|----------|
| **Token 优化** | [最佳实践](../best-practices.md#token-使用优化) | 节省 50%+ |
| **提示词技巧** | [最佳实践](../best-practices.md#提示词最佳实践) | 提升准确度 |
| **自定义命令** | [编程最佳实践](claude-code-best-practices.md#自定义命令) | 节省时间 60%+ |
| **SPEC 驱动** | [SPEC 编程指南](spec-driven-development.md) | 效率提升 40%+ |
| **快速参考** | [快速参考卡](quick-reference.md) | 快速查阅 |

---

### 👥 团队协作

| 主题 | 文档链接 | 适用场景 |
|------|---------|----------|
| **权限分工** | [权限配置](configuration/permissions.md) | 多人协作 |
| **团队规范** | [最佳实践](../best-practices.md#团队协作规范) | 统一标准 |
| **代码审查** | [进阶手册](../advanced-guide.md) | 质量保证 |
| **真实案例** | [真实项目案例](examples/real-world-cases.md#案例2-电商后台管理系统) | 8人团队实践 |

---

## 🔍 快速查找

### 我想...

| 需求 | 推荐文档 | 章节 |
|------|---------|------|
| **快速上手** | [从0到1指南](getting-started/README.md) | 完整流程 |
| **创建项目** | [项目模板](templates/) | 选择模板 |
| **提高效率** | [SPEC 编程指南](spec-driven-development.md) | 全文 |
| **优化 Token** | [最佳实践](../best-practices.md) | Token 优化 |
| **自动化工作流** | [自定义命令](getting-started/global-configuration.md#自定义命令) | 命令创建 |
| **团队协作** | [权限配置](configuration/permissions.md) | 团队配置 |
| **学习案例** | [真实项目案例](examples/real-world-cases.md) | 全部案例 |
| **参考 SPEC** | [SPEC 案例集](examples/spec-examples.md) | 选择类型 |
| **保证安全** | [安全手册](../security-guide.md) | 全文必读 |
| **解决问题** | [最佳实践](../best-practices.md) | 问题排查 |

---

## 📚 完整文档列表

### 核心手册

1. [基础使用手册](../basic-guide.md) - 新手入门
2. [进阶使用手册](../advanced-guide.md) - 进阶用户
3. [最佳实践](../best-practices.md) - 所有用户
4. [安全使用手册](../security-guide.md) - ⭐ 必读

### 专题指南

#### 入门教程
- [从0到1完整指南](getting-started/README.md)
- [安装指南](getting-started/installation.md)
- [全局配置](getting-started/global-configuration.md)

#### 项目模板
- [Python/Shell 项目模板](templates/python-shell-project.md)
- [Next.js 项目模板](templates/nextjs-project.md)
- [文档项目模板](templates/documentation-project.md)

#### 配置与权限
- [权限配置完整指南](configuration/permissions.md)

#### 开发范式
- [Claude Code 完整指南（v2.0+）](claude-code-v3-complete-guide.md) - LSP、CLAUDE.md、MCP 完整体系
- [Claude Code 编程最佳实践](claude-code-best-practices.md)
- [SPEC 范式编程指南](spec-driven-development.md)
- [快速参考卡](quick-reference.md)

#### 实战案例
- [SPEC 实战案例集](examples/spec-examples.md)
- [真实项目最佳实践](examples/real-world-cases.md)

#### 资源与参考
- [官方资源索引](resources/official-resources.md)
- [Claude Code 使用限制变化记录（2026年1月）](claude-code-usage-limits-jan-2026.md)

---

## 🎓 推荐学习路径

### 路径1: 新手快速上手

```
第1天: 安装指南 (10分钟)
      ↓
      全局配置 (20分钟)
      ↓
      选择项目模板 (15分钟)
      ↓
      基础使用手册 (1小时)

第2天: 快速参考卡 (收藏)
      ↓
      创建第一个项目
      ↓
      实践基本操作

第3天: 进阶使用手册
      ↓
      自定义命令
      ↓
      优化工作流
```

**预计时间**: 3天掌握基础

---

### 路径2: 进阶效率提升

```
前置: 已掌握基础使用

第1周: SPEC 范式编程指南
      ↓
      SPEC 实战案例
      ↓
      实践 SPEC 驱动开发

第2周: 编程最佳实践
      ↓
      自定义命令深化
      ↓
      权限配置优化

第3周: 真实项目案例学习
      ↓
      应用到实际项目
      ↓
      团队推广
```

**预计效果**: 效率提升 40%+

---

### 路径3: 团队协作落地

```
准备阶段 (1周):
  - 团队培训 (基础手册)
  - 统一配置 (权限配置)
  - 规范制定 (最佳实践)

落地阶段 (2周):
  - 试点项目 (选择1个项目)
  - SPEC 驱动 (编写 SPEC)
  - 自定义命令 (共享命令库)

推广阶段 (1个月):
  - 全面推广
  - 持续优化
  - 经验总结
```

**预计效果**: 团队效率提升 30%+

---

## 💡 使用建议

### 1. 收藏快速参考

将 [快速参考卡](quick-reference.md) 加入书签，随时查阅。

### 2. 按需学习

不必一次性阅读所有文档，根据实际需求选择：
- 新手 → 入门级文档
- 提效 → 进阶级 + SPEC 范式
- 团队 → 权限配置 + 真实案例

### 3. 实践优先

边学边做，每学一个概念立即实践：
```bash
claude
> 按照 XXX 文档的指引，帮我实现 YYY 功能
```

### 4. 案例参考

遇到类似场景，直接参考案例：
- 开发 CLI → [CLI 工具案例](examples/spec-examples.md#案例1-cli-工具代码检查器)
- 开发 API → [博客 API 案例](examples/spec-examples.md#案例2-restful-api博客系统)

### 5. 持续优化

定期回顾文档，优化配置和工作流。

---

## 🆘 获取帮助

### 文档内查找

1. 使用浏览器搜索功能（Ctrl+F / Cmd+F）
2. 查看本索引的分类导航
3. 参考"我想..."快速查找表

### 官方资源

- [Claude Code 官方文档](https://code.claude.com/docs/)
- [GitHub Issues](https://github.com/anthropics/claude-code/issues)
- [官方资源索引](resources/official-resources.md)

### 社区支持

- 提交 Issue 到本项目
- 参与讨论和贡献

---

<div align="center">

**📖 开始你的 Claude Code 学习之旅！**

[返回主页](../README.md) • [从0到1指南](getting-started/README.md) • [快速参考](quick-reference.md)

</div>
