# Claude Code 完整指南：LSP、CLAUDE.md 与最佳实践

> **版本说明**: 本指南基于 Claude Code 2.0.74+（2025年12月发布），涵盖 LSP 语义智能、CLAUDE.md 配置体系、MCP 服务器集成等核心特性。

## 目录

1. [版本更新说明](#1-版本更新说明)
2. [全局 CLAUDE.md 配置](#2-全局-claudemd-配置)
3. [项目脚手架规范](#3-项目脚手架规范)
4. [MCP 服务器集成](#4-mcp-服务器集成)
5. [Context7 实时文档](#5-context7-实时文档)
6. [技能（Skills）系统](#6-技能skills系统)
7. [上下文管理最佳实践](#7-上下文管理最佳实践)
8. [Hooks 确定性执行](#8-hooks-确定性执行)
9. [LSP 语义代码智能](#9-lsp-语义代码智能)
10. [快速参考表](#10-快速参考表)
11. [参考资源](#11-参考资源)

---

## 1. 版本更新说明

### 2.0.74 版本核心更新（2025年12月）

#### 🚀 LSP 语义智能支持
- **性能提升**: 900倍速度提升（代码理解从45秒降至50毫秒）
- **支持语言**: 11种主流语言（Python, TypeScript, Go, Rust, Java, C/C++, C#, PHP, Kotlin, Ruby, HTML/CSS）
- **智能特性**:
  - 精确的符号跳转和定义查找
  - 类型推断和智能补全
  - 实时语法检查和错误诊断
  - 代码重构建议

#### 📝 CLAUDE.md 配置增强
- **多层级配置**: 企业级 → 全局用户 → 项目 → 项目本地
- **外部导入**: 支持从远程加载配置，带审批对话框
- **安全守门人**: 内置多层防御策略

#### 🔌 MCP 服务器生态
- **官方市场**: claude-plugins-official 自动可用
- **社区扩展**: 25+ 推荐服务器涵盖开发全流程
- **智能权衡**: 明确何时不应使用 MCP

#### ⚡ 性能与上下文优化
- **混合主题衰减**: 避免39%性能下降
- **上下文分层**: 智能管理200K token预算
- **确定性执行**: Hooks 提供可预测的工作流

---

## 2. 全局 CLAUDE.md 配置

### 2.1 安全守门人规则

**核心原则**: CLAUDE.md 作为项目的安全守门人，防止敏感数据泄露。

#### 三大黄金规则

```markdown
## 安全守门人规则

### 🔴 规则1: 永不发布敏感数据
- 禁止在公共仓库提交 API 密钥、密码、Token
- 禁止在代码注释中包含真实凭证
- 禁止在日志中输出敏感信息

### 🔴 规则2: 永不提交 .env 文件
- 所有环境变量使用 .env.example 作为模板
- .env 文件必须在 .gitignore 中
- 使用密钥管理服务（如 1Password, AWS Secrets Manager）

### 🔴 规则3: 多层防御策略
- Pre-commit hooks 自动扫描敏感数据
- CI/CD 流水线二次检查
- 定期审计代码仓库历史
```

### 2.2 Memory Hierarchy（配置加载顺序）

Claude Code 按以下优先级加载 CLAUDE.md 配置：

```
优先级（低到高）:
┌─────────────────────────────────────┐
│ 1. 企业级配置 (Enterprise)          │  ← 公司全局策略
│    /etc/claude/CLAUDE.md            │
├─────────────────────────────────────┤
│ 2. 全局用户配置 (Global User)       │  ← 个人偏好设置
│    ~/.claude/CLAUDE.md              │
├─────────────────────────────────────┤
│ 3. 项目配置 (Project)               │  ← 项目特定规范
│    /project/CLAUDE.md               │
├─────────────────────────────────────┤
│ 4. 项目本地配置 (Project Local)     │  ← 本地覆盖（不提交）
│    /project/.claude/CLAUDE.md       │
└─────────────────────────────────────┘
```

**配置合并策略**:
- 高优先级配置覆盖低优先级同名配置
- 不同配置项会合并（非完全替换）
- 使用 `/context` 命令查看当前生效配置

### 2.3 全局 CLAUDE.md 最佳实践

**位置**: `~/.claude/CLAUDE.md`

**推荐内容**:

```markdown
# 我的 Claude Code 全局配置

## 编码风格偏好
- **注释语言**: 中文
- **代码风格**: PEP 8 (Python), Airbnb (JavaScript)
- **禁止使用**: emoji（除非明确要求）

## 安全规范
- 永不提交敏感数据
- 使用环境变量管理配置
- Pre-commit hooks 强制执行

## Git 提交规范
- **格式**: `<类型>: <描述>`
- **类型**: feat, fix, docs, style, refactor, perf, test, chore
- **语言**: 中文
- **禁止**: 不使用 emoji 和 Claude 署名

## 自动化工具
- **代码扫描**: ~/cobra-code/github/code-scanner/
- **提交脚本**: ~/.claude/scripts/auto_commit_enhanced.sh
- **语法检查**: python3 ~/.claude/scripts/check_syntax_multi.py

## 开发环境
- **Python**: 3.8+ with virtualenv
- **Node.js**: 18+ with pnpm
- **Shell**: Bash 5+

## 调试限制
- 本地不支持生产数据库连接
- 使用虚拟环境进行语法验证
- 优先使用 `--help` 和 `-m py_compile` 检查
```

---

## 3. 项目脚手架规范

### 3.1 标准项目结构

```
my-project/
├── CLAUDE.md                # 项目配置（提交到git）
├── SPEC.md                  # 功能规格说明
├── CHANGELOG.md             # 版本变更日志
├── README.md                # 项目概览
├── .gitignore               # Git 忽略规则
├── .editorconfig            # 编辑器配置
├── .claude/                 # 本地配置（不提交）
│   └── CLAUDE.md            # 项目本地覆盖配置
├── docs/                    # 文档目录
│   ├── INDEX.md
│   └── architecture.md
├── src/                     # 源代码
├── tests/                   # 测试用例
├── scripts/                 # 辅助脚本
└── config/                  # 配置文件
    ├── config.yaml.example
    └── .env.example
```

### 3.2 项目 CLAUDE.md 模板

```markdown
# 项目名称

## 项目信息
- **类型**: Web应用 / API服务 / 命令行工具
- **技术栈**: Python 3.8+, Flask, PostgreSQL
- **部署环境**: AWS ECS, Docker

## 架构说明
### 核心模块
- `src/api/`: REST API 接口
- `src/models/`: 数据模型
- `src/services/`: 业务逻辑
- `src/utils/`: 工具函数

### 数据库设计
- **表结构**: 参考 `docs/database-schema.md`
- **迁移工具**: Alembic

## 开发规范
### 代码风格
- Python: PEP 8, Black 格式化
- 注释: 中文注释，docstring 使用 Google 风格

### 测试要求
- 单元测试覆盖率 >= 80%
- 使用 pytest 框架
- Mock 外部依赖

### 环境配置
\```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行测试
pytest tests/
\```

## 安全要求
- API Key 使用环境变量
- 数据库密码使用 AWS Secrets Manager
- 敏感文件不提交: `.env`, `credentials.json`

## 部署流程
1. 运行测试: `pytest`
2. 构建镜像: `docker build -t app:latest .`
3. 推送到ECR: `docker push ...`
4. 更新ECS服务: `aws ecs update-service ...`
```

### 3.3 使用 `/init` 命令初始化项目

```bash
# 在项目根目录执行
/init

# 自动创建:
# - CLAUDE.md（项目配置）
# - .gitignore（标准忽略规则）
# - docs/ 目录结构
# - 文档维护脚本
```

---

## 4. MCP 服务器集成

### 4.1 什么是 MCP 服务器

MCP（Model Context Protocol）服务器是扩展 Claude Code 能力的插件系统，提供：
- **外部工具集成**: 数据库、API、浏览器
- **实时数据访问**: GitHub, Slack, Linear
- **专用功能**: RAG 检索、云服务管理

### 4.2 何时不应使用 MCP

⚠️ **MCP 权衡（Trade-offs）**：

| 场景 | 推荐方式 | 原因 |
|------|---------|------|
| 简单文件操作 | 内置 Read/Write 工具 | MCP 增加不必要的复杂性 |
| 本地代码搜索 | 内置 Grep/Glob 工具 | 性能更快，无需额外配置 |
| 一次性任务 | Bash 工具 | 无需持久化连接 |
| 高频小请求 | 直接 API 调用 | 减少 MCP 通信开销 |

**适合使用 MCP 的场景**:
- 需要持久化连接（数据库、实时API）
- 复杂的外部系统交互（云服务管理）
- 需要状态管理的操作（浏览器自动化）

### 4.3 推荐 MCP 服务器列表

#### 核心开发工具

| 服务器 | 功能 | 推荐场景 |
|--------|------|---------|
| **Context7** | 实时文档和库搜索 | 学习新框架、查询API |
| **GitHub** | 仓库管理、PR、Issue | 代码审查、项目管理 |
| **FileSystem** | 文件系统操作 | 大规模文件处理 |
| **Sequential-thinking** | 逐步推理增强 | 复杂问题调试 |

#### 数据库集成

| 服务器 | 支持数据库 | 功能 |
|--------|-----------|------|
| **MongoDB** | MongoDB | 查询、聚合、索引管理 |
| **PostgreSQL** | PostgreSQL | SQL 查询、Schema 管理 |
| **DBHub** | 多数据库统一接口 | 跨数据库查询 |

#### 文件与 RAG 检索

| 服务器 | 功能 | 推荐场景 |
|--------|------|---------|
| **Docling** | 文档解析（PDF, DOCX） | 文档内容提取 |
| **Qdrant** | 向量数据库 | 语义搜索、RAG |
| **Chroma** | 向量数据库 | 本地 RAG 应用 |

#### 浏览器与测试

| 服务器 | 功能 | 推荐场景 |
|--------|------|---------|
| **Playwright** | 浏览器自动化 | E2E 测试、爬虫 |
| **Browser MCP** | 浏览器控制 | 网页交互、截图 |
| **Brave Search** | 网络搜索 | 实时信息查询 |

#### 云服务管理

| 服务器 | 平台 | 功能 |
|--------|------|------|
| **AWS** | Amazon Web Services | EC2, S3, Lambda 管理 |
| **Cloudflare** | Cloudflare | DNS, Workers, R2 |
| **Hostinger** | Hostinger | 虚拟主机管理 |
| **Kubectl** | Kubernetes | 集群管理、Pod 操作 |

#### 协作工具

| 服务器 | 功能 | 推荐场景 |
|--------|------|---------|
| **Slack** | 消息发送、频道管理 | 团队通知、Bot |
| **Linear** | Issue 跟踪、项目管理 | 敏捷开发 |
| **Figma** | 设计文件访问 | 设计协作 |

### 4.4 MCP 配置示例

**位置**: `~/.claude/settings.json`

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upura/context7-mcp"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost:5432/db"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@executeautomation/playwright-mcp-server"]
    }
  }
}
```

**环境变量管理**:

```bash
# ~/.bashrc 或 ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"
export OPENAI_API_KEY="sk-xxxxxxxxxxxx"
```

---

## 5. Context7 实时文档

### 5.1 什么是 Context7

Context7 是一个 MCP 服务器，提供：
- **实时文档搜索**: 最新的官方文档和库说明
- **代码示例**: 实际可用的代码片段
- **API 参考**: 准确的函数签名和参数说明

### 5.2 支持的文档库

- **前端框架**: React, Vue, Angular, Svelte
- **后端框架**: Django, Flask, FastAPI, Express
- **数据库**: PostgreSQL, MongoDB, Redis
- **工具库**: Lodash, Axios, Pandas, NumPy
- **云服务**: AWS SDK, Azure SDK, GCP SDK

### 5.3 使用示例

```bash
# Claude Code 会自动调用 Context7 MCP
User: "如何使用 FastAPI 创建 WebSocket 端点?"

Claude: [调用 Context7 查询 FastAPI WebSocket 文档]
根据最新的 FastAPI 文档,创建 WebSocket 端点的方法:

\```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message: {data}")
\```

[来源: FastAPI 官方文档 - WebSocket]
```

### 5.4 配置 Context7

```bash
# 安装
npx -y @upura/context7-mcp

# 在 settings.json 中配置
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upura/context7-mcp"]
    }
  }
}
```

---

## 6. 技能（Skills）系统

### 6.1 什么是 Skills

Skills（技能）是 Claude Code 的预定义工作流，通过斜杠命令调用：
- `/commit` - 智能代码提交
- `/review-pr` - 代码审查
- `/pdf` - PDF 处理
- `/expense` - 报销凭证整理
- `/frontend-design` - 前端界面设计

### 6.2 自定义 Skills

**位置**: `~/.claude/skills/` 或项目 `.claude/skills/`

**示例: 创建代码扫描 Skill**

文件: `~/.claude/skills/code-scan.md`

```markdown
---
name: code-scan
description: 运行代码安全扫描并生成报告
---

# 代码扫描技能

## 功能
使用 code-scanner 工具扫描项目代码,检测:
- 硬编码密钥
- SQL 注入风险
- XSS 漏洞
- 代码质量问题

## 执行流程

1. 检查 code-scanner 是否安装
\```bash
if [ ! -d ~/cobra-code/github/code-scanner ]; then
    echo "错误: code-scanner 未安装"
    exit 1
fi
\```

2. 运行扫描
\```bash
cd ~/cobra-code/github/code-scanner
python3 scanner.py --target {{project_path}} --output report
\```

3. 分析报告
- 解析扫描结果
- 按风险级别分类
- 生成修复建议

4. 输出结果
\```markdown
# 代码扫描报告

## 高危问题 (🔴)
- [文件:行号] 问题描述

## 中危问题 (🟠)
- [文件:行号] 问题描述

## 建议
- 修复建议1
- 修复建议2
\```

## 参数
- `--target`: 扫描目标路径（默认: 当前目录）
- `--severity`: 最低风险级别（high/medium/low）
```

**使用**:
```bash
# 调用自定义 Skill
/code-scan
/code-scan --target /path/to/project --severity high
```

### 6.3 Skills 开发最佳实践

1. **清晰的描述**: 明确 Skill 的用途和适用场景
2. **参数化**: 使用 `{{variable}}` 支持动态输入
3. **错误处理**: 检查依赖和前置条件
4. **输出格式**: 使用结构化输出（Markdown 表格、列表）
5. **文档完善**: 包含使用示例和参数说明

---

## 7. 上下文管理最佳实践

### 7.1 上下文衰减问题

**研究发现**: 混合主题导致 **39% 性能下降**

```
纯主题对话:
"帮我优化这个 SQL 查询" → "添加索引" → "测试性能"
✅ 上下文连贯,性能高

混合主题对话:
"优化 SQL" → "顺便改下前端样式" → "再看看 API" → "回到 SQL"
❌ 上下文切换频繁,性能下降 39%
```

### 7.2 上下文管理策略

#### 策略1: 主题分离

```bash
# ✅ 好的方式
Session 1: 专注于数据库优化
Session 2: 专注于前端重构
Session 3: 专注于 API 开发

# ❌ 不好的方式
Session 1: 数据库 + 前端 + API 混合讨论
```

#### 策略2: 使用 `/clear` 重置上下文

```bash
# 完成一个主题后清理
/clear

# 开始新主题
"现在帮我处理前端问题..."
```

#### 策略3: 分层上下文规划

```
┌─────────────────────────────────────────┐
│ 全局上下文 (~/.claude/CLAUDE.md)        │  ← 始终加载
│ - 编码风格                              │
│ - 安全规范                              │
│ - Git 规范                              │
├─────────────────────────────────────────┤
│ 项目上下文 (project/CLAUDE.md)          │  ← 项目级加载
│ - 架构说明                              │
│ - 技术栈                                │
│ - 部署流程                              │
├─────────────────────────────────────────┤
│ 任务上下文 (当前会话)                   │  ← 动态加载
│ - 具体需求                              │
│ - 相关代码                              │
│ - 错误信息                              │
└─────────────────────────────────────────┘
```

### 7.3 Token 预算管理

Claude Code 支持 **200K token** 上下文窗口:

| 内容类型 | 平均 Token | 建议比例 |
|---------|-----------|---------|
| CLAUDE.md 配置 | 2-5K | 2.5% |
| 项目文档 | 5-10K | 5% |
| 代码文件 | 10-30K | 15% |
| 对话历史 | 50-100K | 50% |
| 工具输出 | 20-50K | 25% |
| 缓冲区 | 5-10K | 2.5% |

**优化建议**:
- 使用 `Read` 工具的 `offset` 和 `limit` 参数读取大文件的部分内容
- 使用 `Grep` 精确搜索而非读取整个文件
- 定期使用 `/clear` 清理不再需要的上下文
- 将长文档分割成多个小文件

---

## 8. Hooks 确定性执行

### 8.1 什么是 Hooks

Hooks 是在特定事件触发时自动执行的 Shell 脚本:
- **user-prompt-submit-hook**: 用户提交请求前执行
- **tool-call-hook**: 工具调用前执行
- **session-start-hook**: 会话开始时执行

### 8.2 配置 Hooks

**位置**: `~/.claude/settings.json`

```json
{
  "hooks": {
    "user-prompt-submit-hook": {
      "command": "bash",
      "args": ["-c", "~/.claude/hooks/before-prompt.sh"]
    },
    "tool-call-hook": {
      "command": "bash",
      "args": ["-c", "~/.claude/hooks/before-tool.sh \"${tool}\" \"${args}\""]
    }
  }
}
```

### 8.3 Hook 脚本示例

#### 示例1: 提交前检查

文件: `~/.claude/hooks/before-prompt.sh`

```bash
#!/bin/bash
# 用户提交请求前的安全检查

# 检查是否在敏感目录
CURRENT_DIR=$(pwd)
SENSITIVE_DIRS=("/etc" "/var" "/root")

for dir in "${SENSITIVE_DIRS[@]}"; do
    if [[ "$CURRENT_DIR" == "$dir"* ]]; then
        echo "⚠️  警告: 当前在敏感目录 $dir"
        echo "建议切换到安全目录后再操作"
        exit 1
    fi
done

# 检查是否有未提交的敏感文件
if git rev-parse --git-dir > /dev/null 2>&1; then
    STAGED_FILES=$(git diff --cached --name-only)
    if echo "$STAGED_FILES" | grep -qE '\.(env|key|pem|p12)$'; then
        echo "🔴 错误: 检测到敏感文件即将提交"
        echo "$STAGED_FILES" | grep -E '\.(env|key|pem|p12)$'
        exit 1
    fi
fi

exit 0
```

#### 示例2: 工具调用拦截

文件: `~/.claude/hooks/before-tool.sh`

```bash
#!/bin/bash
# 工具调用前的权限检查

TOOL=$1
ARGS=$2

# 拦截危险的 Bash 命令
if [ "$TOOL" == "Bash" ]; then
    # 检查是否包含危险命令
    DANGEROUS_CMDS=("rm -rf" "dd if=" "mkfs" "> /dev")

    for cmd in "${DANGEROUS_CMDS[@]}"; do
        if echo "$ARGS" | grep -q "$cmd"; then
            echo "🔴 拦截: 检测到危险命令 '$cmd'"
            echo "如需执行,请手动运行"
            exit 1
        fi
    done
fi

# 记录所有工具调用（审计日志）
echo "[$(date)] Tool: $TOOL, Args: $ARGS" >> ~/.claude/logs/tool-audit.log

exit 0
```

### 8.4 Hooks 最佳实践

1. **快速执行**: Hook 应在 100ms 内完成,避免阻塞工作流
2. **明确错误**: 使用清晰的错误消息说明拦截原因
3. **日志记录**: 记录关键操作用于审计
4. **幂等性**: Hook 可能被多次调用,确保幂等
5. **错误处理**: Hook 失败不应导致 Claude Code 崩溃

---

## 9. LSP 语义代码智能

### 9.1 什么是 LSP

LSP（Language Server Protocol）是一个标准协议,提供:
- **符号定义跳转**: 快速定位函数、类的定义位置
- **类型推断**: 理解变量和返回值类型
- **智能补全**: 基于上下文的代码建议
- **实时诊断**: 语法错误和类型错误检测
- **代码重构**: 重命名、提取函数等

### 9.2 性能提升

**对比测试（大型项目代码理解）**:

| 方式 | 时间 | 准确度 |
|------|------|--------|
| 无 LSP（纯文本分析） | 45 秒 | 75% |
| 启用 LSP | 50 毫秒 | 98% |

**速度提升**: **900倍** 🚀

### 9.3 启用 LSP

#### 步骤1: 设置环境变量

```bash
# 临时启用
ENABLE_LSP_TOOL=1 claude

# 永久启用（推荐）
echo 'export ENABLE_LSP_TOOL=1' >> ~/.zshrc
source ~/.zshrc
```

#### 步骤2: 验证 LSP 可用

```bash
claude
# 在 Claude Code 中输入
/lsp status

# 输出示例:
# LSP Status:
# - Python: ✅ pyright (v1.1.339)
# - TypeScript: ✅ typescript-language-server (v4.3.3)
# - Go: ✅ gopls (v0.14.2)
```

### 9.4 支持的语言和 LSP 服务器

| 语言 | LSP 服务器 | 安装方式 |
|------|-----------|---------|
| **Python** | pyright | `npm install -g pyright` |
| **TypeScript/JavaScript** | typescript-language-server | `npm install -g typescript-language-server` |
| **Go** | gopls | `go install golang.org/x/tools/gopls@latest` |
| **Rust** | rust-analyzer | `rustup component add rust-analyzer` |
| **Java** | jdtls | 自动下载 |
| **C/C++** | clangd | `brew install llvm` / `apt install clangd` |
| **C#** | omnisharp | 自动下载 |
| **PHP** | intelephense | `npm install -g intelephense` |
| **Kotlin** | kotlin-language-server | 自动下载 |
| **Ruby** | solargraph | `gem install solargraph` |
| **HTML/CSS** | vscode-html/css-languageserver | `npm install -g vscode-langservers-extracted` |

### 9.5 LSP 配置示例

**位置**: `~/.claude/lsp-config.json`

```json
{
  "python": {
    "server": "pyright",
    "settings": {
      "python.analysis.typeCheckingMode": "strict",
      "python.analysis.autoImportCompletions": true,
      "python.analysis.diagnosticMode": "workspace"
    }
  },
  "typescript": {
    "server": "typescript-language-server",
    "settings": {
      "typescript.suggest.autoImports": true,
      "typescript.preferences.importModuleSpecifier": "relative"
    }
  },
  "go": {
    "server": "gopls",
    "settings": {
      "gopls.analyses": {
        "unusedparams": true,
        "shadow": true
      }
    }
  }
}
```

### 9.6 LSP 使用示例

#### 示例1: 快速定位函数定义

```python
# 用户: "这个 calculate_total 函数在哪里定义的?"
# Claude 使用 LSP 快速跳转

def process_order(order):
    total = calculate_total(order.items)  # ← LSP 识别此处调用
    # ...

# LSP 输出:
# calculate_total 定义在: src/utils/pricing.py:45
```

#### 示例2: 类型错误检测

```python
# LSP 实时检测类型错误

def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers("10", "20")  # ← LSP 诊断: 类型错误
# 期望: int, 实际: str
```

#### 示例3: 智能重构

```python
# 用户: "将这个 user_name 变量重命名为 username"
# Claude 使用 LSP 安全重命名

# 重命名前:
user_name = "Alice"
print(f"Hello, {user_name}")

# LSP 自动更新所有引用 (23 处)
username = "Alice"
print(f"Hello, {username}")
```

### 9.7 LSP 最佳实践

1. **项目初始化**: 在项目根目录启动 Claude Code，确保 LSP 正确加载项目配置
2. **依赖安装**: 确保项目依赖已安装（LSP 需要解析 import）
3. **配置文件**: 使用项目的配置文件（`tsconfig.json`, `pyproject.toml`）
4. **大型项目**: LSP 首次启动可能需要几秒钟索引项目
5. **错误排查**: 使用 `/lsp status` 检查 LSP 服务器状态

---

## 10. 快速参考表

### 10.1 常用命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `/init` | 初始化项目配置 | `/init` |
| `/context` | 查看当前上下文 | `/context` |
| `/clear` | 清除对话历史 | `/clear` |
| `/commit` | 智能 Git 提交 | `/commit` |
| `/review-pr` | 代码审查 | `/review-pr 123` |
| `/lsp status` | LSP 状态检查 | `/lsp status` |
| `/help` | 帮助文档 | `/help` |

### 10.2 文件路径快速参考

| 配置项 | 路径 |
|--------|------|
| 全局配置 | `~/.claude/CLAUDE.md` |
| 全局设置 | `~/.claude/settings.json` |
| 自定义 Skills | `~/.claude/skills/` |
| Hooks 脚本 | `~/.claude/hooks/` |
| 项目配置 | `<project>/CLAUDE.md` |
| 项目本地配置 | `<project>/.claude/CLAUDE.md` |
| LSP 配置 | `~/.claude/lsp-config.json` |

### 10.3 环境变量

```bash
# LSP 支持
export ENABLE_LSP_TOOL=1

# 常用 Token
export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"
export OPENAI_API_KEY="sk-xxxxxxxxxxxx"
export ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxx"
```

### 10.4 Git 提交类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: 添加用户登录功能` |
| `fix` | Bug修复 | `fix: 修复空指针异常` |
| `docs` | 文档更新 | `docs: 更新安装说明` |
| `style` | 代码格式 | `style: 调整代码缩进` |
| `refactor` | 重构 | `refactor: 优化数据库查询逻辑` |
| `perf` | 性能优化 | `perf: 减少API响应时间` |
| `test` | 测试 | `test: 添加单元测试用例` |
| `chore` | 其他修改 | `chore: 更新依赖版本` |

---

## 11. 参考资源

### 11.1 官方文档

- [Claude Code 官方文档](https://docs.anthropic.com/claude-code)
- [MCP 协议规范](https://modelcontextprotocol.io)
- [LSP 协议规范](https://microsoft.github.io/language-server-protocol/)

### 11.2 社区资源

- [GitHub: claude-code-lsps](https://github.com/Piebald-AI/claude-code-lsps) - LSP 插件市场
- [GitHub: cclsp](https://github.com/ktnyt/cclsp) - Claude Code LSP 增强
- [ClaudeLog](https://claudelog.com/) - 文档、教程和最佳实践

### 11.3 教程文章

- [Claude Code LSP 完整安装指南](https://www.aifreeapi.com/en/posts/claude-code-lsp)
- [Claude Code 2.0 最佳实践](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
- [LSP 插件对比测试](https://medium.com/@joe.njenga/i-tested-all-available-claude-code-lsp-plugins-dont-waste-time-read-this-first-6896e992a540)

### 11.4 工具推荐

| 工具 | 用途 | 链接 |
|------|------|------|
| **Code Scanner** | 安全扫描 | 本地工具 `~/cobra-code/github/code-scanner/` |
| **Pre-commit** | Git hooks 管理 | https://pre-commit.com/ |
| **Black** | Python 格式化 | https://github.com/psf/black |
| **ESLint** | JavaScript 检查 | https://eslint.org/ |
| **Prettier** | 代码格式化 | https://prettier.io/ |

### 11.5 社区贡献者

本指南整合了社区的宝贵反馈:
- **u/BlueVajra** - 命令/技能合并建议
- **u/stratofax** - 点文件同步方案
- **u/antoniocs** - MCP 权衡分析
- **u/GeckoLogic** - LSP 集成指南
- **weihoop** - 中文本地化和配置模板

### 11.6 项目文档索引

本项目的其他相关文档：
- [Claude Code 最佳实践](./claude-code-best-practices.md)
- [Skills 技能系统指南](./claude-code-skills-guide.md)
- [配置包说明](../config-templates/README.md)
- [文档索引](./INDEX.md)

---

## 附录: 常见问题

### Q1: LSP 服务器启动失败怎么办?

```bash
# 检查 LSP 状态
/lsp status

# 手动安装 LSP 服务器
npm install -g pyright typescript-language-server

# 验证安装
which pyright
pyright --version
```

### Q2: MCP 服务器连接超时?

1. 检查网络连接
2. 验证 Token 是否有效
3. 查看 MCP 服务器日志: `~/.claude/logs/mcp-server.log`
4. 尝试重启 Claude Code

### Q3: CLAUDE.md 配置不生效?

```bash
# 查看当前生效配置
/context

# 检查配置加载顺序
# 记住: 项目本地 > 项目 > 全局用户 > 企业级

# 清除缓存重新加载
/clear
/context
```

### Q4: 如何优化 Token 使用?

1. 使用 `Read` 的 `offset`/`limit` 读取大文件片段
2. 用 `Grep` 精确搜索而非全文读取
3. 定期使用 `/clear` 清理上下文
4. 避免混合多个主题讨论

### Q5: Hook 脚本执行权限问题?

```bash
# 添加执行权限
chmod +x ~/.claude/hooks/*.sh

# 验证脚本可执行
bash ~/.claude/hooks/before-prompt.sh
echo $?  # 应输出 0
```

---

**文档版本**: v1.0
**最后更新**: 2026-01-16
**维护者**: weihoop

如有问题或建议，请在项目 Issues 中反馈: https://github.com/weihoop/claude-code-guide/issues
