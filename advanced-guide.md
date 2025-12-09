# Claude Code 进阶使用手册

> 本手册适合熟悉基础功能的用户，涵盖 Skill、MCP、Hooks、自动编程等高级特性

---

## 📋 目录

- [Skill 系统](#skill-系统)
- [MCP 服务器集成](#mcp-服务器集成)
- [Hooks 高级配置](#hooks-高级配置)
- [自定义 Slash Commands](#自定义-slash-commands)
- [自动编程工作流](#自动编程工作流)
- [Agent SDK 开发](#agent-sdk-开发)
- [多项目管理](#多项目管理)
- [企业级配置](#企业级配置)
- [性能优化](#性能优化)

---

## 🎯 Skill 系统

### Skill 是什么？

Skill 是 Claude Code 的**可复用能力模块**，类似于插件系统，可以扩展 Claude 的功能。

### Skill 结构

```bash
.claude/
└── skills/
    └── my-skill/
        ├── skill.json       # Skill 配置
        ├── prompt.md        # Skill 提示词
        └── tools/           # 自定义工具（可选）
```

### 创建 Skill

#### 1. 创建 Skill 目录

```bash
mkdir -p .claude/skills/code-reviewer
cd .claude/skills/code-reviewer
```

#### 2. 创建 `skill.json`

```json
{
  "name": "code-reviewer",
  "version": "1.0.0",
  "description": "自动代码审查工具",
  "author": "Your Name",
  "entrypoint": "prompt.md",
  "tools": ["Read", "Grep", "Glob"],
  "triggers": {
    "keywords": ["审查", "review", "检查代码"],
    "autoActivate": false
  }
}
```

**配置说明**:
- `entrypoint`: Skill 入口提示词文件
- `tools`: 允许使用的工具列表
- `triggers.keywords`: 触发关键词
- `triggers.autoActivate`: 是否自动激活

#### 3. 创建 `prompt.md`

```markdown
# Code Reviewer Skill

你是一个专业的代码审查专家。当用户请求代码审查时，你需要：

## 审查内容

1. **代码质量**
   - 变量命名是否清晰
   - 函数是否单一职责
   - 代码复用性

2. **潜在问题**
   - 安全漏洞（XSS, SQL注入等）
   - 性能问题
   - 边界条件处理

3. **最佳实践**
   - 是否符合项目规范
   - 错误处理是否完善
   - 注释是否充分

## 输出格式

以 Markdown 格式输出：

```markdown
## 代码审查报告

### ✅ 优点
- 列出代码的优点

### ⚠️ 问题
- 列出发现的问题

### 💡 建议
- 提供改进建议

### 🔒 安全性
- 安全相关的发现
```

## 使用示例

```
用户: 帮我审查 src/api.js
你: [执行上述审查流程]
```
```

### 使用 Skill

#### 方法 1: 使用 Skill 命令

```bash
# 在 Claude Code 中
/skill code-reviewer
```

#### 方法 2: 通过关键词触发

```
> 帮我审查一下这个文件的代码
```

如果 Skill 配置了 `keywords: ["审查"]`，会自动激活。

#### 方法 3: 在代码中调用

```
> 使用 code-reviewer skill 审查 src/utils.js
```

### 高级 Skill 示例

#### Skill: 自动化测试生成器

**skill.json**:
```json
{
  "name": "test-generator",
  "version": "1.0.0",
  "description": "自动生成单元测试",
  "tools": ["Read", "Write", "Bash"],
  "config": {
    "testFramework": "jest",
    "coverageTarget": 80
  }
}
```

**prompt.md**:
```markdown
# Test Generator Skill

根据源代码自动生成单元测试。

## 工作流程

1. 读取源文件
2. 识别可测试函数
3. 生成测试用例
4. 创建测试文件
5. 运行测试验证

## 测试框架

使用配置中的 testFramework: {{config.testFramework}}

## 覆盖率目标

目标覆盖率: {{config.coverageTarget}}%
```

### Skill 管理

```bash
# 列出所有 Skill
/skills list

# 启用 Skill
/skill enable code-reviewer

# 禁用 Skill
/skill disable code-reviewer

# 查看 Skill 信息
/skill info code-reviewer
```

---

## 🔌 MCP 服务器集成

### MCP 是什么？

**MCP (Model Context Protocol)** 是一个标准协议，允许 Claude Code 连接外部服务和数据源。

### MCP 架构

```
Claude Code
    ↓ (MCP Protocol)
MCP Server
    ↓
External Service (数据库、API、工具等)
```

### 安装 MCP 服务器

#### 1. 使用官方 MCP 服务器

**安装 Filesystem MCP**:

```bash
npm install -g @anthropic-ai/mcp-server-filesystem
```

**配置** (`~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "mcp-server-filesystem",
      "args": ["/path/to/allowed/directory"],
      "env": {}
    }
  }
}
```

#### 2. 常用官方 MCP 服务器

| MCP 服务器 | 功能 | 安装命令 |
|-----------|------|---------|
| `mcp-server-filesystem` | 文件系统访问 | `npm i -g @anthropic-ai/mcp-server-filesystem` |
| `mcp-server-git` | Git 操作 | `npm i -g @anthropic-ai/mcp-server-git` |
| `mcp-server-github` | GitHub API | `npm i -g @anthropic-ai/mcp-server-github` |
| `mcp-server-postgres` | PostgreSQL | `npm i -g @anthropic-ai/mcp-server-postgres` |
| `mcp-server-sqlite` | SQLite | `npm i -g @anthropic-ai/mcp-server-sqlite` |

### 配置 MCP 服务器

**完整配置示例** (`~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "mcp-server-filesystem",
      "args": ["/Users/you/projects"],
      "env": {}
    },
    "github": {
      "command": "mcp-server-github",
      "args": [],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    },
    "postgres": {
      "command": "mcp-server-postgres",
      "args": [],
      "env": {
        "POSTGRES_URL": "postgresql://user:pass@localhost:5432/db"
      }
    }
  }
}
```

### 使用 MCP 服务器

#### 示例 1: 查询数据库

```
> 查询 PostgreSQL 中 users 表的所有数据
```

Claude 会通过 `mcp-server-postgres` 执行查询。

#### 示例 2: GitHub 操作

```
> 创建一个 GitHub Issue，标题是 "修复登录 bug"
```

Claude 会通过 `mcp-server-github` 调用 API。

#### 示例 3: 文件系统操作

```
> 在 /projects 目录下创建新项目结构
```

Claude 会通过 `mcp-server-filesystem` 操作文件。

### 自定义 MCP 服务器

#### 1. 创建 MCP 服务器项目

```bash
mkdir my-mcp-server
cd my-mcp-server
npm init -y
npm install @anthropic-ai/mcp-sdk
```

#### 2. 实现服务器 (`index.js`)

```javascript
import { Server } from '@anthropic-ai/mcp-sdk/server/index.js';
import { StdioServerTransport } from '@anthropic-ai/mcp-sdk/server/stdio.js';

// 创建服务器
const server = new Server({
  name: 'my-custom-server',
  version: '1.0.0'
});

// 注册工具
server.tool(
  'fetch_weather',
  {
    description: '获取城市天气',
    parameters: {
      city: { type: 'string', description: '城市名称' }
    }
  },
  async ({ city }) => {
    // 调用天气 API
    const weather = await fetchWeatherAPI(city);
    return { temperature: weather.temp, condition: weather.condition };
  }
);

// 启动服务器
const transport = new StdioServerTransport();
await server.connect(transport);
```

#### 3. 配置使用

```json
{
  "mcpServers": {
    "weather": {
      "command": "node",
      "args": ["/path/to/my-mcp-server/index.js"]
    }
  }
}
```

#### 4. 使用自定义 MCP

```
> 查询北京的天气
```

### MCP 权限控制

```json
{
  "permissions": {
    "mcpServers": {
      "github": {
        "allow": ["issues:read", "issues:write"],
        "deny": ["repo:delete"]
      },
      "postgres": {
        "ask": ["query", "insert", "update"],
        "deny": ["drop", "truncate"]
      }
    }
  }
}
```

---

## 🪝 Hooks 高级配置

### Hooks 是什么？

Hooks 允许在 Claude Code 执行特定操作前后运行自定义命令。

### Hooks 类型

| Hook | 触发时机 | 用途 |
|------|---------|------|
| `user-prompt-submit-hook` | 用户提交消息前 | 预处理输入、验证 |
| `tool-call-hook` | 工具调用前 | 拦截、修改工具调用 |
| `tool-result-hook` | 工具执行后 | 后处理结果 |
| `pre-commit-hook` | Git 提交前 | 代码检查、格式化 |

### 配置 Hooks

**位置**: `~/.claude/settings.json` 或 `.claude/settings.json`

```json
{
  "hooks": {
    "user-prompt-submit-hook": {
      "command": "bash",
      "args": ["-c", "echo '检查输入...' && exit 0"]
    },
    "tool-call-hook": {
      "command": "node",
      "args": ["./hooks/validate-tool.js"]
    },
    "pre-commit-hook": {
      "command": "bash",
      "args": ["-c", "npm run lint && npm test"]
    }
  }
}
```

### Hook 示例

#### 1. 代码格式化 Hook

**创建 hook 脚本** (`hooks/format-code.sh`):

```bash
#!/bin/bash

# 在编辑文件前自动格式化
if [[ "$TOOL_NAME" == "Edit" ]]; then
  FILE_PATH="$TOOL_ARGS_file_path"

  # 格式化 JavaScript
  if [[ "$FILE_PATH" == *.js ]]; then
    npx prettier --write "$FILE_PATH"
  fi

  # 格式化 Python
  if [[ "$FILE_PATH" == *.py ]]; then
    black "$FILE_PATH"
  fi
fi

exit 0
```

**配置**:

```json
{
  "hooks": {
    "tool-call-hook": {
      "command": "bash",
      "args": ["./hooks/format-code.sh"]
    }
  }
}
```

#### 2. 安全检查 Hook

```javascript
// hooks/security-check.js
const SENSITIVE_PATTERNS = [
  /password\s*=/i,
  /api[_-]?key\s*=/i,
  /secret\s*=/i
];

const toolArgs = JSON.parse(process.env.TOOL_ARGS || '{}');

if (process.env.TOOL_NAME === 'Write' || process.env.TOOL_NAME === 'Edit') {
  const content = toolArgs.content || toolArgs.new_string || '';

  for (const pattern of SENSITIVE_PATTERNS) {
    if (pattern.test(content)) {
      console.error('⚠️ 检测到敏感信息，请使用环境变量！');
      process.exit(1); // 阻止操作
    }
  }
}

process.exit(0); // 允许操作
```

**配置**:

```json
{
  "hooks": {
    "tool-call-hook": {
      "command": "node",
      "args": ["./hooks/security-check.js"]
    }
  }
}
```

#### 3. 提交前测试 Hook

```json
{
  "hooks": {
    "pre-commit-hook": {
      "command": "bash",
      "args": ["-c", "npm run test && npm run lint"]
    }
  }
}
```

### Hook 环境变量

Hook 脚本可访问的环境变量：

| 变量 | 说明 | 示例 |
|------|------|------|
| `TOOL_NAME` | 工具名称 | `Edit`, `Write`, `Bash` |
| `TOOL_ARGS` | 工具参数 (JSON) | `{"file_path": "..."}` |
| `CLAUDE_CODE_VERSION` | Claude Code 版本 | `1.0.0` |
| `WORKING_DIR` | 工作目录 | `/path/to/project` |

---

## 📜 自定义 Slash Commands

### 创建自定义命令

#### 1. 创建命令目录

```bash
mkdir -p .claude/commands
```

#### 2. 创建命令文件

**`.claude/commands/review.md`**:

```markdown
---
name: review
description: 执行完整的代码审查流程
aliases: [code-review, cr]
---

# 代码审查流程

请执行以下步骤：

1. **读取文件**
   - 如果用户指定了文件，读取该文件
   - 否则，询问要审查哪个文件

2. **执行审查**
   - 检查代码质量
   - 识别潜在问题
   - 验证安全性

3. **生成报告**
   以 Markdown 格式输出审查报告

4. **运行测试**
   如果有测试文件，运行相关测试
```

#### 3. 使用自定义命令

```bash
# 使用命令名
/review

# 使用别名
/cr

# 带参数
/review src/api.js
```

### 高级命令示例

#### 命令: 自动化部署

**`.claude/commands/deploy.md`**:

```markdown
---
name: deploy
description: 自动化部署流程
args:
  - name: environment
    description: 部署环境
    required: true
    choices: [dev, staging, production]
---

# 自动化部署到 {{args.environment}}

1. **预检查**
   - 确认当前分支是 main/master
   - 检查是否有未提交的改动
   - 运行测试确保通过

2. **构建**
   ```bash
   npm run build
   ```

3. **部署**
   ```bash
   # 根据环境执行不同部署命令
   {% if args.environment == "production" %}
   npm run deploy:prod
   {% else %}
   npm run deploy:{{args.environment}}
   {% endif %}
   ```

4. **验证**
   - 检查部署状态
   - 运行健康检查

5. **通知**
   - 记录部署日志
   - 发送通知
```

**使用**:

```bash
/deploy production
```

---

## 🤖 自动编程工作流

### 什么是自动编程？

让 Claude Code 自主完成从需求到部署的完整开发流程。

### 自动编程流程

```
需求分析 → 设计方案 → 编写代码 → 测试 → 文档 → 部署
```

### 配置自动编程

#### 1. 创建工作流配置

**`.claude/workflows/feature-development.json`**:

```json
{
  "name": "feature-development",
  "description": "完整的功能开发流程",
  "steps": [
    {
      "name": "analyze",
      "description": "分析需求",
      "autoExecute": false,
      "prompt": "分析用户需求，生成技术方案"
    },
    {
      "name": "design",
      "description": "设计架构",
      "autoExecute": false,
      "prompt": "设计代码架构和模块划分"
    },
    {
      "name": "implement",
      "description": "实现代码",
      "autoExecute": true,
      "prompt": "根据设计实现代码"
    },
    {
      "name": "test",
      "description": "编写测试",
      "autoExecute": true,
      "prompt": "编写单元测试和集成测试"
    },
    {
      "name": "document",
      "description": "生成文档",
      "autoExecute": true,
      "prompt": "更新相关文档和注释"
    }
  ]
}
```

#### 2. 使用工作流

```
> 使用 feature-development 工作流开发用户认证功能
```

Claude 会：
1. ✅ 分析需求（等待确认）
2. ✅ 设计方案（等待确认）
3. 🤖 自动实现代码
4. 🤖 自动编写测试
5. 🤖 自动生成文档

### 自动编程最佳实践

#### 1. 明确需求

```
✅ 实现一个 RESTful API，包含用户 CRUD 操作：
   - GET /api/users - 获取用户列表
   - POST /api/users - 创建用户
   - PUT /api/users/:id - 更新用户
   - DELETE /api/users/:id - 删除用户
   使用 Express.js 和 PostgreSQL

❌ 做一个用户管理功能
```

#### 2. 分阶段确认

```
> 先规划一下实现方案，不要直接写代码

（Claude 生成方案）

> 方案看起来不错，开始实施吧
```

#### 3. 设置检查点

```json
{
  "workflows": {
    "checkpoints": {
      "afterImplement": "运行测试确保代码正确",
      "beforeDeploy": "人工审查代码"
    }
  }
}
```

---

## 🔧 Agent SDK 开发

### Agent SDK 简介

Agent SDK 允许你开发自定义的 Claude Code Agent。

### 创建自定义 Agent

#### 1. 安装 SDK

```bash
npm install @anthropic-ai/claude-code-agent-sdk
```

#### 2. 创建 Agent

```javascript
// my-agent.js
import { Agent } from '@anthropic-ai/claude-code-agent-sdk';

class MyCustomAgent extends Agent {
  constructor() {
    super({
      name: 'my-custom-agent',
      description: '我的自定义 Agent',
      version: '1.0.0'
    });
  }

  // 定义 Agent 能力
  async capabilities() {
    return {
      tools: ['Read', 'Write', 'Bash'],
      skills: ['code-analysis', 'refactoring']
    };
  }

  // 处理用户输入
  async handleInput(userMessage) {
    // 分析用户意图
    const intent = await this.analyzeIntent(userMessage);

    // 执行相应操作
    switch (intent.type) {
      case 'code-review':
        return await this.performCodeReview(intent.file);
      case 'refactor':
        return await this.refactorCode(intent.file);
      default:
        return await this.defaultHandler(userMessage);
    }
  }

  // 代码审查
  async performCodeReview(filePath) {
    const content = await this.tools.read(filePath);
    const issues = await this.analyzeCode(content);
    return this.formatReviewReport(issues);
  }
}

// 启动 Agent
const agent = new MyCustomAgent();
agent.start();
```

#### 3. 注册 Agent

**`.claude/settings.json`**:

```json
{
  "agents": {
    "my-custom-agent": {
      "command": "node",
      "args": ["./my-agent.js"],
      "autoActivate": false
    }
  }
}
```

#### 4. 使用 Agent

```
> 使用 my-custom-agent 审查代码
```

---

## 📂 多项目管理

### 项目配置继承

```
~/.claude/settings.json          (全局配置)
    ↓
project1/.claude/settings.json   (项目配置)
    ↓
project1/.claude/settings.local.json  (本地配置)
```

### 多项目配置示例

**全局配置** (`~/.claude/settings.json`):

```json
{
  "model": "claude-sonnet-4-5",
  "permissions": {
    "allow": ["Read", "Grep", "Glob"],
    "ask": ["Edit", "Write"],
    "deny": ["Bash(sudo:*)", "Bash(rm:*)"]
  }
}
```

**前端项目配置** (`frontend/.claude/settings.json`):

```json
{
  "extends": "~/.claude/settings.json",
  "permissions": {
    "allow": [
      "Bash(npm run dev:*)",
      "Bash(npm run test:*)",
      "Edit(/src/**)"
    ],
    "deny": ["Edit(/node_modules/**)"]
  }
}
```

**后端项目配置** (`backend/.claude/settings.json`):

```json
{
  "extends": "~/.claude/settings.json",
  "permissions": {
    "allow": [
      "Bash(python:*)",
      "Bash(pytest:*)",
      "Edit(/app/**)"
    ],
    "deny": ["Read(.env*)", "Edit(/migrations/**)"]
  }
}
```

### 项目切换

```bash
# 方法 1: 重新启动
cd ~/projects/frontend
claude

# 方法 2: 在运行中切换
> /cd ~/projects/backend
```

---

## 🏢 企业级配置

### 统一策略管理

**位置**:
- Linux/Mac: `/etc/claude-code/settings.json`
- Windows: `C:\ProgramData\ClaudeCode\settings.json`

**企业配置示例**:

```json
{
  "permissions": {
    "deny": [
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(ssh:*)",
      "Read(**/*credential*)",
      "Read(**/*secret*)",
      "WebFetch(*.internal.company.com/*)"
    ]
  },
  "mcpServers": {
    "company-gitlab": {
      "command": "mcp-server-gitlab",
      "env": {
        "GITLAB_URL": "https://gitlab.company.com"
      }
    }
  },
  "hooks": {
    "tool-call-hook": {
      "command": "/opt/company/claude-security-check.sh"
    }
  }
}
```

### 团队配置模板

```bash
# 创建团队模板
mkdir -p ~/claude-templates/react-team

cat > ~/claude-templates/react-team/settings.json << 'EOF'
{
  "permissions": {
    "allow": [
      "Bash(npm run dev:*)",
      "Bash(npm run test:*)",
      "Edit(/src/**)"
    ]
  },
  "hooks": {
    "pre-commit-hook": {
      "command": "bash",
      "args": ["-c", "npm run lint && npm test"]
    }
  }
}
EOF

# 新项目使用模板
cp -r ~/claude-templates/react-team/.claude new-project/
```

---

## ⚡ 性能优化

### 1. 使用合适的模型

#### 基础模型选择

```bash
# 简单任务使用 Haiku (快速、便宜)
/model haiku

# 复杂任务使用 Sonnet (平衡)
/model sonnet

# 最复杂任务使用 Opus (强大、慢)
/model opus
```

#### 高级模型策略

##### 策略 1: Opus Plan Mode（推荐）

**适用场景**：大型功能开发、复杂重构

```bash
/model opusplan
```

**工作流程**：
1. 规划阶段 → Opus（强大推理）
2. 执行阶段 → Sonnet（高效实现）
3. 自动切换，无需手动干预

**实际案例**：

```
用户: 重构整个用户认证模块

【自动使用 Opus 进行规划】
Claude: 我来分析现有架构...
- 当前实现：Session + Cookie
- 建议：迁移到 JWT
- 需要修改：auth.js, middleware/, routes/

【切换到 Sonnet 执行】
Claude: 开始实施重构...
- 创建 JWT 工具函数
- 更新中间件
- 迁移路由处理
```

**优势**：
- ✅ 节省 40-60% Token 消耗
- ✅ 保持高质量设计
- ✅ 加快执行速度

##### 策略 2: 动态模型切换

**适用场景**：长期会话，多种任务混合

```bash
# 1. 复杂分析阶段
/model opus
> 分析这个性能问题的根本原因

# 2. 切换到实现阶段
/model sonnet
> 按照上面的分析，开始优化代码

# 3. 简单验证
/model haiku
> 检查代码格式是否正确
```

##### 策略 3: 任务分层策略

**不同任务类型的模型选择**：

| 任务类型 | 推荐模型 | Token 消耗 | 质量 | 速度 |
|---------|---------|-----------|------|------|
| 🏗️ 架构设计 | Opus | 💰💰💰 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 🔍 问题诊断 | Opus | 💰💰💰 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 🛠️ 功能开发 | Sonnet | 💰💰 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 🔧 Bug 修复 | Sonnet | 💰💰 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 🎨 代码格式化 | Haiku | 💰 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 📖 快速查询 | Haiku | 💰 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 📝 文档生成 | Sonnet | 💰💰 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

#### 模型切换最佳实践

##### 1. 按阶段切换

```
阶段 1: 理解和规划（Opus）
> /model opus
> 分析整个系统的认证流程，找出安全漏洞

阶段 2: 实现（Sonnet）
> /model sonnet
> 根据上面的分析，修复这些安全问题

阶段 3: 测试和验证（Haiku）
> /model haiku
> 运行测试，检查代码风格
```

##### 2. 按复杂度切换

**简单任务链**：
```bash
/model haiku
> 格式化代码
> 添加注释
> 运行 linter
```

**复杂任务链**：
```bash
/model opus
> 设计分布式锁方案
> 评估不同实现的优劣

/model sonnet
> 实现 Redis 分布式锁
```

##### 3. Token 预算管理

**场景 1: Token 充足**
```bash
# 全程使用 Opus 保证质量
/model opus
```

**场景 2: Token 有限**
```bash
# 使用 Opus Plan Mode
/model opusplan

# 或手动切换
/model opus      # 只在关键决策时使用
/model sonnet    # 大部分时间使用
```

**场景 3: Token 紧张**
```bash
# 优先使用 Sonnet 和 Haiku
/model sonnet    # 主力模型
/model haiku     # 简单任务
```

#### 模型性能对比

##### 响应时间

| 模型 | 简单查询 | 代码生成 | 复杂分析 |
|------|---------|---------|---------|
| Opus | ~3-5s | ~8-15s | ~15-30s |
| Sonnet | ~1-2s | ~3-6s | ~6-12s |
| Haiku | ~0.5-1s | ~1-3s | ~3-6s |

##### Token 效率

```
相同任务的 Token 消耗对比（估算）：

简单 Bug 修复：
- Opus:   ~2000 tokens
- Sonnet: ~1500 tokens
- Haiku:  ~1000 tokens

复杂架构设计：
- Opus:   ~8000 tokens  ✅ 最佳选择
- Sonnet: ~6000 tokens  ⚠️ 可能遗漏细节
- Haiku:  ~4000 tokens  ❌ 不推荐
```

### 2. 优化上下文

```bash
# 清除历史释放 token
/clear

# 只读取必要的文件
> 只看 src/api.js 的第 10-50 行
```

### 3. 使用 Agent 分解任务

对于复杂任务，启动子 Agent：

```
> 使用 Task 工具分析这个大项目的架构
```

### 4. 智能上下文管理

#### 选择性读取

```
❌ 低效：
> 读取整个项目所有文件

✅ 高效：
> 搜索包含 "auth" 的文件
> 只读取 auth.js 和 middleware/auth.js
```

#### 分段处理

```
大型重构任务拆分：

第 1 步：
> 分析 src/auth/ 目录的结构

第 2 步（清除上下文）：
/clear
> 重构 auth.js 文件

第 3 步（清除上下文）：
/clear
> 更新相关测试
```

### 5. 组合优化策略

#### 最优策略组合

```
1. 启动：选择合适的模型
   /model opusplan

2. 规划：让 Claude 先分析
   > 先别写代码，分析一下如何实现

3. 执行：分步骤进行
   > 好的，先实现第一步

4. 清理：完成后释放上下文
   /clear

5. 验证：使用轻量模型
   /model haiku
   > 运行测试，检查格式
```

---

## 📚 相关资源

- [基础使用手册](basic-guide.md) - 基础功能入门
- [最佳实践](best-practices.md) - Token 优化、安全性等
- [权限配置指南](docs/configuration/permissions.md) - 权限详解
- [官方资源](docs/resources/official-resources.md) - 官方文档链接

---

**最后更新**: 2025-11-27
**文档版本**: 1.0
**适用于**: Claude Code 所有版本
