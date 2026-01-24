# Skills vs MCP vs Commands 对比指南

全面对比 Claude 的三种扩展方式，帮助你选择最合适的工具。

## 📊 核心对比

| 特性 | Skills | MCP | Slash Commands |
|------|--------|-----|----------------|
| **定位** | 工作流和方法论 | 外部数据访问 | 快捷操作 |
| **触发方式** | 自动/手动 | 手动调用 | 手动输入 `/xxx` |
| **Token 效率** | 高（渐进式加载） | 中 | 低（始终加载） |
| **开发难度** | 简单（Markdown） | 中（需要服务器） | 简单（Markdown） |
| **执行能力** | 可选脚本 | ✅ 完整程序 | ❌ 仅提示词 |
| **数据访问** | 本地文件 | ✅ API/数据库/工具 | 本地文件 |
| **跨平台** | ✅ 全平台 | ✅ 全平台 | ⚠️ 仅 Claude Code |
| **维护成本** | 低 | 中-高 | 低 |

---

## 🧩 Skills - 工作流和方法论

### 适用场景

✅ **最适合**：
- 定义工作流程和方法论
- 提供专业领域知识
- 规范化操作步骤
- 代码审查、文档编写等流程

❌ **不适合**：
- 需要实时外部数据
- 复杂的API 交互
- 需要状态管理

### 示例

**代码审查 Skill**:
```markdown
---
name: code-review
description: 对代码进行安全审查和质量检查
---

# Code Review Skill

## 检查清单

1. 安全漏洞检测
2. 代码质量分析
3. 最佳实践检查

## 审查流程

步骤 1: 接收代码...
步骤 2: 安全扫描...
步骤 3: 生成报告...
```

**优势**:
- 📝 简单的 Markdown 文件
- 🚀 自动加载和触发
- 💾 Token 效率高

---

## 🔌 MCP - 外部数据和工具访问

### 适用场景

✅ **最适合**：
- 访问外部 API（GitHub、Slack、数据库）
- 实时数据获取
- 复杂的工具集成
- 需要状态管理的操作

❌ **不适合**：
- 简单的提示词优化
- 纯流程指导
- 不需要外部数据的场景

### 示例

**GitHub MCP 服务器**:
```python
# github_mcp_server.py
from mcp.server import Server
import github

server = Server("github-mcp")

@server.tool()
async def create_issue(repo: str, title: str, body: str):
    """在 GitHub 仓库创建 Issue"""
    gh = github.Github(token=os.getenv("GITHUB_TOKEN"))
    repository = gh.get_repo(repo)
    issue = repository.create_issue(title=title, body=body)
    return {"url": issue.html_url, "number": issue.number}

@server.tool()
async def list_prs(repo: str, state: str = "open"):
    """列出 Pull Requests"""
    gh = github.Github(token=os.getenv("GITHUB_TOKEN"))
    repository = gh.get_repo(repo)
    prs = repository.get_pulls(state=state)
    return [{"number": pr.number, "title": pr.title} for pr in prs]
```

**优势**:
- ✅ 完整的程序执行能力
- 🌐 访问外部数据源
- 🔧 复杂工具集成

**劣势**:
- 🔨 需要编写和维护服务器
- 💰 额外的运行成本
- 🔧 配置相对复杂

---

## ⚡ Slash Commands - 快捷操作

### 适用场景

✅ **最适合**：
- 常用操作的快捷方式
- 项目特定的提示词
- 快速模板生成
- 简化重复任务

❌ **不适合**：
- 复杂逻辑
- 需要外部数据
- 跨项目共享

### 示例

**代码审查命令**:
```markdown
<!-- .claude/commands/review.md -->
请对当前更改的代码进行全面审查：

1. 检查安全漏洞（SQL注入、XSS等）
2. 验证代码质量（命名、复杂度）
3. 确认测试覆盖
4. 检查文档完整性

使用以下格式输出审查报告：
[审查报告模板]
```

**优势**:
- 🚀 快速创建和使用
- 📁 项目级别定制
- 🎯 精确控制提示词

**劣势**:
- ⚠️ 仅 Claude Code 支持
- 📊 Token 效率较低（始终加载）
- 🔄 不能自动触发

---

## 🎯 选择决策树

```
需要访问外部API/数据库吗？
├─ 是 → 使用 MCP
└─ 否 ↓

需要定义标准化流程吗？
├─ 是 ↓
│   └─ 需要跨项目共享吗？
│       ├─ 是 → 使用 Skills
│       └─ 否 → 使用 Slash Commands
└─ 否 ↓

只是快捷操作吗？
├─ 是 → 使用 Slash Commands
└─ 否 → 根据具体需求选择
```

---

## 🔄 组合使用案例

### 案例 1：代码审查工作流

```
Skill（定义审查流程）
  ↓
MCP（从 GitHub 获取 PR 数据）
  ↓
Slash Command（快速触发审查）

具体实现：
1. code-review Skill 定义审查标准
2. GitHub MCP 获取 PR 代码和历史
3. /review 命令快速触发完整流程
```

**代码示例**:

**Skill** (`code-review/SKILL.md`):
```markdown
---
name: code-review
description: 专业代码审查，检查安全性和质量
---

# Code Review Skill

## 审查标准

### 安全检查
- SQL 注入
- XSS 漏洞
- 敏感信息泄露

### 质量检查
- 命名规范
- 代码复杂度
- 测试覆盖
```

**MCP** (提供数据访问):
```bash
# 配置 GitHub MCP
claude mcp add github --transport stdio
```

**Slash Command** (`.claude/commands/review.md`):
```markdown
使用 code-review skill 和 GitHub MCP 审查当前 PR：

1. 从 GitHub 获取 PR 详情
2. 按照 code-review 标准审查
3. 生成详细报告
```

**使用**:
```bash
# 在 Claude Code 中
/review
```

### 案例 2：数据分析管道

```
Slash Command（触发分析）
  ↓
MCP（从数据库获取数据）
  ↓
Skill（执行分析流程）
  ↓
Skill（生成可视化报告）

具体实现：
1. /analyze 触发分析流程
2. PostgreSQL MCP 获取数据
3. data-analysis Skill 执行分析
4. report-generator Skill 生成报告
```

### 案例 3：文档自动化

```
Skill（文档标准和模板）
  ↓
MCP（从 Notion 获取内容）
  ↓
Slash Command（快速生成文档）

具体实现：
1. technical-writing Skill 定义文档规范
2. Notion MCP 获取项目信息
3. /doc 命令快速生成技术文档
```

---

## 📋 实战对比

### 同一功能的三种实现

**需求**: 生成项目 changelog

#### 方式 1：使用 Skill

```markdown
---
name: changelog-generator
description: 从 git 提交历史生成用户友好的 changelog
---

# Changelog Generator

## 流程

1. 分析 git commit 历史
2. 分类提交（feat/fix/docs）
3. 转换为用户友好的描述
4. 按版本组织
5. 生成 Markdown 格式

## 输出格式

# Changelog

## v1.2.0 - 2026-01-24

### ✨ 新功能
- 添加用户登录功能

### 🐛 Bug 修复
- 修复数据保存问题
```

**适合**：标准化的 changelog 生成流程，不需要外部数据

#### 方式 2：使用 MCP

```python
# changelog_mcp.py
@server.tool()
async def generate_changelog(repo_path: str, from_tag: str, to_tag: str):
    """从 git 仓库生成 changelog"""
    import git

    repo = git.Repo(repo_path)
    commits = list(repo.iter_commits(f"{from_tag}..{to_tag}"))

    changelog = {
        "features": [],
        "fixes": [],
        "docs": []
    }

    for commit in commits:
        if commit.message.startswith("feat:"):
            changelog["features"].append(commit.message)
        elif commit.message.startswith("fix:"):
            changelog["fixes"].append(commit.message)
        # ...

    return changelog
```

**适合**：需要直接访问 git 仓库，复杂的提交分析

#### 方式 3：使用 Slash Command

```markdown
<!-- .claude/commands/changelog.md -->
生成当前项目的 changelog：

1. 运行：git log --oneline v1.1.0..HEAD
2. 分析提交信息
3. 按类型分类
4. 生成 Markdown 格式的 changelog

格式要求：
- 使用 emoji（✨ 新功能，🐛 修复）
- 按重要性排序
- 包含 PR 链接
```

**适合**：快速触发，利用现有 git 命令

---

## 💡 最佳实践

### 1. 优先级建议

```
1. 简单场景：Slash Commands
   - 快速创建
   - 项目特定
   - 经常使用的提示词

2. 标准流程：Skills
   - 可复用的工作流
   - 跨项目共享
   - 不需要外部数据

3. 复杂集成：MCP
   - 需要外部 API
   - 复杂工具集成
   - 状态管理
```

### 2. 组合使用原则

```
Layer 1: Slash Commands（入口层）
  - 提供便捷的入口
  - 组合多个 Skills 和 MCP

Layer 2: Skills（流程层）
  - 定义标准化流程
  - 提供专业知识

Layer 3: MCP（数据层）
  - 提供外部数据访问
  - 执行实际操作
```

### 3. 避免过度工程

```
❌ 不要为简单任务创建 MCP
好的：
  - Slash Command：/format-json
差的：
  - MCP Server：json-formatter-mcp

✅ 不要为复杂集成只用 Slash Commands
差的：
  - 在 Slash Command 中硬编码 API 调用
好的：
  - 创建 MCP 服务器处理 API 交互
```

---

## 📚 延伸阅读

- [创建自定义 Skills](creating-custom-skills.md)
- [MCP 服务器开发](../../mcp-guide.md)
- [Slash Commands 最佳实践](../../slash-commands.md)

---

**返回**: [指南目录](README.md) | [主页](../README.md)

**最后更新**: 2026-01-24
