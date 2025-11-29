# Gemini CLI 中文使用指南

> Google Gemini CLI 完整使用教程和最佳实践集合

## 📚 文档目录

### 核心文档

1. **[Gemini CLI 编程最佳实践](./gemini-cli-best-practices.md)** ⭐️ 推荐
   - 完整的安装配置指南
   - GEMINI.md 配置最佳实践
   - 项目上下文管理策略
   - MCP 服务器集成教程
   - 实用脚本和工具集合
   - 10+ 个实战示例

2. **[Gemini CLI 架构与流程图](./ARCHITECTURE.md)** 🎨 可视化
   - 整体架构图（Mermaid）
   - 工作流程序列图
   - GEMINI.md 加载机制
   - MCP 集成架构
   - 开发工作流程图
   - 性能优化流程

3. **[Gemini CLI 项目记忆管理](./gemini.md)**
   - 代码仓库上下文管理方法
   - 自动化上下文生成脚本
   - 多项目管理方案
   - Shell 别名配置技巧

4. **[文档索引导航](./DOCS_INDEX.md)** 📖 快速查找
   - 完整学习路径
   - 按主题分类导航
   - 快速参考指南

5. **[Gemini 订阅计划详细对比](./PRICING.md)** 💰 定价指南
   - 免费版 vs 付费版完整对比
   - API 定价和成本优化
   - 企业版方案说明
   - 选择建议和常见问题

## 🚀 快速开始

### 1. 安装 Gemini CLI

```bash
# 使用 npm 全局安装
npm install -g @google/gemini-cli

# 或使用 npx（无需安装）
npx @google/gemini-cli
```

### 2. 首次运行

```bash
# 启动 Gemini CLI
gemini

# 选择认证方式（推荐使用 Google 账号）
```

### 3. 初始化项目配置

```bash
# 在项目根目录运行
cd /path/to/your/project
gemini

# 在 CLI 中执行
/init

# 这会生成 GEMINI.md 配置文件
```

## 💡 核心功能

### 免费额度

- ✅ 每分钟 60 次请求
- ✅ 每天 1000 次请求
- ✅ 100 万 token 上下文窗口（Gemini 2.5 Pro）

### 内置工具

- 🔍 Google 搜索集成
- 📁 文件操作（读取、写入、编辑）
- 💻 Shell 命令执行
- 🌐 网页内容抓取
- 🔌 MCP 服务器支持

## 📖 主要章节

### GEMINI.md 配置

创建项目级配置文件，让 Gemini 了解你的项目：

```markdown
# 项目配置

## 技术栈
- React 18 + TypeScript
- Node.js + Express
- PostgreSQL

## 编码规范
- 使用函数式组件
- TypeScript 严格模式
- ESLint + Prettier
```

详见：[GEMINI.md 配置最佳实践](./gemini-cli-best-practices.md#geminimd-配置最佳实践)

### 项目上下文管理

虽然 Gemini CLI 没有内置记忆功能，但可以通过以下方式实现：

1. **GEMINI.md 配置文件**（推荐）
2. **自动上下文生成脚本**
3. **Shell 别名快速查询**
4. **多项目配置管理**

详见：[项目上下文管理](./gemini.md)

### MCP 服务器集成

扩展 Gemini CLI 功能：

- **GitHub MCP**: 直接操作 GitHub 仓库
- **Docker MCP**: 容器管理和操作
- **FastMCP**: 使用 Python 构建自定义 MCP 服务器
- **自定义 MCP**: 集成数据库、API、自定义脚本

详见：[MCP 服务器集成](./gemini-cli-best-practices.md#mcp-服务器集成)

## 🛠️ 实用工具

### 自动提交脚本

```bash
#!/bin/bash
# 自动生成 Git 提交信息
gemini "根据 git diff 生成提交信息" | git commit -F -
```

### 代码审查助手

```bash
#!/bin/bash
# 自动审查代码质量
gemini "审查 $1 的代码质量和安全性" > review.md
```

### 文档生成器

```bash
#!/bin/bash
# 自动生成 API 文档
gemini "为 $1 生成 API 文档" > docs.md
```

更多脚本详见：[实用脚本与工具](./gemini-cli-best-practices.md#实用脚本与工具)

## 🎯 最佳实践要点

1. **充分利用 GEMINI.md** - 为每个项目创建详细配置
2. **分解复杂任务** - 将大任务拆分为小步骤
3. **先计划后执行** - 让 Gemini 先生成计划再实施
4. **增量提交代码** - 每完成一步就提交
5. **使用 MCP 扩展** - 集成外部工具和服务
6. **优化提示词** - 提供明确的上下文和要求

## 💰 Gemini 订阅计划对比（2025年）

### 免费版 vs 付费版

| 特性 | 免费版 | AI Pro<br/>$19.99/月 | AI Ultra<br/>$249.99/月 | API 付费层 |
|------|--------|---------------------|------------------------|-----------|
| **日请求限制** | 15-50 次 | ~100 次 | 更高 | 按用量计费 |
| **上下文窗口** | 32K tokens | 1M tokens | 1M+ tokens | 视模型而定 |
| **存储空间** | 15GB | 2TB | 2TB+ | - |
| **视频上传** | 5 分钟 | 1 小时 | 更长 | - |
| **NotebookLM** | 3 概览/天 | 20 概览/天 | - | - |
| **数据隐私** | ❌ | ✅ | ✅ | ✅ |
| **高级模型** | 基础 | 完整 | 最先进 | 完整 |

### Google AI Pro ($19.99/月) 适合

- ✅ 每天需要 50-100 次请求
- ✅ 处理长文档（1M tokens = 1500 页文本）
- ✅ 需要数据隐私保护
- ✅ 使用 NotebookLM Pro、Deep Research 等高级功能
- ✅ 需要 2TB 云存储空间

### API 付费层定价

**按百万 token 计费**（输入/输出）:

- **Flash-Lite**: $0.10 / $0.40
- **2.5 Flash**: $0.30 / $2.50
- **2.5 Pro**: $1.25 / $10.00
- **3 Pro Preview**: $2.00 / $12.00

**成本优化**:
- Batch API: 50% 折扣
- Context Caching: 节省最多 90%
- 付费层数据不会用于改进产品

### 企业版方案

- **Gemini for Google Workspace**: 需联系销售获取报价
- **Gemini Code Assist**: 标准版/企业版，新客户首月 50 个免费许可证
- **Google AI Ultra for Business**: 企业级方案

### 选择建议

💡 **继续免费版**: 轻度使用（< 15次/天），不介意数据用于产品改进
💡 **升级 AI Pro**: 中度使用，需要长上下文和数据隐私
💡 **选择 API 层**: 应用集成，按需付费，完全隐私保护
💡 **企业方案**: 团队协作，企业级安全和合规需求

📘 **详细对比**: 查看 **[完整定价文档](./PRICING.md)** 了解更多细节

官方价格页面：
- [Google One AI Premium](https://one.google.com/about/ai-premium/)
- [Gemini API 定价](https://ai.google.dev/gemini-api/docs/pricing)

## 📚 学习资源

### 官方资源

- [Gemini CLI 官方文档](https://geminicli.com/docs/)
- [GitHub 仓库](https://github.com/google-gemini/gemini-cli)
- [Google Codelabs 实践教程](https://codelabs.developers.google.com/gemini-cli-hands-on)
- [FastMCP 集成指南](https://developers.googleblog.com/en/gemini-cli-fastmcp-simplifying-mcp-server-development/)

### 社区资源

- [Gemini CLI Cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet)
- [Gemini CLI 最佳实践（英文）](https://dev.to/proflead/gemini-cli-best-practices-10-pro-tips-youre-not-using-272b)
- [Addy Osmani 的技巧集合](https://addyo.substack.com/p/gemini-cli-tips-and-tricks)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来完善这份指南！

### 贡献方式

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: 添加某个特性'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🔗 相关项目

- [Claude Code 中文使用手册](https://github.com/anthropics/claude-code)
- [MCP 服务器集合](https://github.com/modelcontextprotocol/servers)

## 📮 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 [GitHub Issue](../../issues)
- 发送邮件至项目维护者

---

**最后更新**: 2025-01-29
**文档版本**: v1.0.0

⭐️ 如果这份指南对你有帮助，请给个 Star！
