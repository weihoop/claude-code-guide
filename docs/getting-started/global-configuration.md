# Claude Code 全局配置指南

配置 `~/.claude/` 目录，为所有项目提供统一的设置和自定义命令。

---

## 配置目录结构

```
~/.claude/
├── settings.json          # 全局权限和配置
├── CLAUDE.md             # 全局提示词（可选）
├── commands/             # 用户级自定义命令
│   ├── fix.md
│   ├── push.md
│   ├── deploy.md
│   ├── review.md
│   └── ...
├── .mcp.json             # MCP服务器全局配置（可选）
├── history.jsonl         # 对话历史（自动生成）
├── projects/             # 项目索引（自动��成）
└── session-env/          # 会话环境（自动生成）
```

---

## settings.json 配置

### 文件位置

```bash
~/.claude/settings.json
```

### 基础配置模板

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Glob",
      "Grep",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "WebSearch",
      "WebFetch(domain:docs.anthropic.com)",
      "WebFetch(domain:github.com)"
    ],
    "deny": [
      "Read(.env*)",
      "Read(.secret*)",
      "Read(**/secrets/**)",
      "Write(.env*)",
      "Bash(rm -rf:*)",
      "Bash(sudo:*)",
      "Bash(docker run:*)",
      "Bash(npm publish:*)"
    ],
    "ask": [
      "Bash(git push --force:*)",
      "Bash(npm install:*)",
      "Bash(pip install:*)"
    ]
  }
}
```

### 权限语法说明

#### 1. 文件操作权限

```json
"allow": [
  "Read",                    // 允许读取所有文件
  "Read(/src/**)",          // 只允许读取 src 目录
  "Write",                   // 允许写入新文件
  "Write(/build/**)",       // 只允许在 build 目录写入
  "Edit",                    // 允许编辑文件
  "Edit(**.js)",            // 只允许编辑 .js 文件
  "Glob",                    // 允许使用 glob 搜索
  "Grep"                     // 允许使用 grep 搜索
]
```

#### 2. Shell 命令权限

```json
"allow": [
  "Bash(git:*)",            // 允许所有 git 命令
  "Bash(npm:*)",            // 允许所有 npm 命令
  "Bash(python:*)",         // 允许所有 python 命令
  "Bash(git commit:*)",     // 只允许 git commit
  "Bash(npm run test:*)"    // 只允许 npm run test
],
"deny": [
  "Bash(rm:*)",             // 禁止 rm 命令
  "Bash(sudo:*)",           // 禁止 sudo
  "Bash(chmod:*)",          // 禁止 chmod
  "Bash(curl:*)",           // 禁止 curl（安全考虑）
  "Bash(wget:*)"            // 禁止 wget
]
```

#### 3. 网络访问权限

```json
"allow": [
  "WebSearch",                              // 允许网络搜索
  "WebFetch(domain:api.example.com)",      // 只允许特定域名
  "WebFetch(domain:*.github.com)"          // 允许 GitHub 子域名
],
"deny": [
  "WebFetch(domain:internal.company.com)"  // 禁止内部网络
]
```

#### 4. 通配符规则

- `*` - 匹配任意字符（不包括 `/`）
- `**` - 匹配任意路径
- `*.js` - 所有 .js 文件
- `**/*.test.js` - 所有测试文件

### 权限优先级

```
deny > ask > allow
```

**示例**：
```json
{
  "permissions": {
    "allow": ["Read"],
    "deny": ["Read(.env*)"]
  }
}
```
结果：可以读取所有文件，但 `.env*` 除外。

### 常用配置模板

#### 开发者友好型

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Glob",
      "Grep",
      "Bash(git:*)",
      "Bash(npm:*)",
      "Bash(python:*)",
      "WebSearch"
    ],
    "deny": [
      "Read(.env*)",
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ],
    "ask": [
      "Bash(git push:*)",
      "Bash(npm publish:*)"
    ]
  }
}
```

#### 安全严格型

```json
{
  "permissions": {
    "allow": [
      "Read(/src/**)",
      "Read(/tests/**)",
      "Glob",
      "Grep"
    ],
    "ask": [
      "Edit",
      "Write",
      "Bash(git:*)",
      "Bash(npm:*)"
    ],
    "deny": [
      "Read(.env*)",
      "Read(**/secrets/**)",
      "Bash(rm:*)",
      "Bash(sudo:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "WebFetch"
    ]
  }
}
```

#### 只读模式

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "WebSearch"
    ],
    "deny": [
      "Write",
      "Edit",
      "Bash"
    ]
  }
}
```

---

## CLAUDE.md 全局提示词

### 文件位置

```bash
~/.claude/CLAUDE.md
```

### 用途

为所有项目提供通用的上下文和工作偏好。

### 推荐模板

```markdown
# Claude 开发助手全局配置

## 个人工作偏好

### 编程语言偏好
- **主要语言**: Python, TypeScript, Bash
- **数据处理**: Python（pandas, numpy）
- **Web开发**: Next.js + TypeScript
- **脚本工具**: Bash + Python

### 代码风格
- 使用类型提示（Python Type Hints, TypeScript）
- 遵循 PEP 8（Python）和 ESLint（JavaScript/TypeScript）
- 函数和变量使用描述性命名
- 添加完整的错误处理和日志

### 注释和文档
- 使用中文注释
- 复杂逻辑必须添加说明
- 公共 API 必须有文档注释
- README 保持更新

## 常用命令和工具

### Python
```bash
# 虚拟环境
python -m venv venv
source venv/bin/activate

# 测试
python -m pytest tests/ -v

# 代码检查
python -m mypy src/
black src/
```

### Node.js
```bash
# 测试
npm test
npm run test:watch

# 构建
npm run build
npm run lint
```

### Git
```bash
# 常用命令
git status
git diff
git log --oneline -10
git add -A && git commit -m "message"
```

## 安全策略

### 敏感信息保护
- 不要读取 `.env` 文件
- 不要读取包含 `secret`、`key`、`token` 的文件
- 不要在代码中硬编码密钥
- 使用环境变量管理配置

### 代码提交前检查
- 运行所有测试
- 运行代码检查工具
- 确认没有敏感信息
- 编写清晰的提交信息

### 禁止的操作
- 不执行破坏性命令（rm -rf, sudo, etc.）
- 不修改系统文件
- 不安装未经确认的依赖
- 不直接操作生产数据库

## 最佳实践

### 错误处理
```python
# Python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"操作失败: {e}")
    raise
```

```typescript
// TypeScript
try {
  const result = await riskyOperation();
} catch (error) {
  console.error('操作失败:', error);
  throw error;
}
```

### 日志记录
```python
# Python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("操作成功")
```

```typescript
// TypeScript
console.log('[INFO]', '操作成功');
console.error('[ERROR]', '操作失败', error);
```

### 测试编写
- 每个功能都要有单元测试
- 测试覆盖率目标 >= 80%
- 使用描述性的测试名称
- 测试边界条件和错误情况

## 项目初始化模板

### Python 项目
```bash
mkdir project && cd project
python -m venv venv
source venv/bin/activate
pip install pytest black mypy
echo "pytest\nblack\nmypy" > requirements-dev.txt
```

### Node.js 项目
```bash
mkdir project && cd project
npm init -y
npm install --save-dev typescript @types/node
npm install --save-dev eslint prettier
npx tsc --init
```

## 常用资源

- Python 文档: https://docs.python.org/
- TypeScript 文档: https://www.typescriptlang.org/
- Next.js 文档: https://nextjs.org/docs
- MDN Web Docs: https://developer.mozilla.org/

## 问题排查

### 常见问题清单
1. 检查环境变量是否正确
2. 确认依赖版本兼容
3. 查看错误日志
4. 搜索相关文档和 Stack Overflow

### 调试技巧
- 使用断点调试
- 添加详细日志
- 逐步缩小问题范围
- 编写最小复现代码
```

### 使用建议

1. **保持简洁** - 只添加真正通用的内容
2. **定期更新** - 随着工作习惯的变化调整
3. **避免过于具体** - 项目特定的内容应放在项目级 CLAUDE.md

---

## 自定义命令

### 创建全局命令

所有 `.md` 文件放在 `~/.claude/commands/` 目录。

#### 命令文件格式

```markdown
---
name: command-name
description: 命令描述
aliases: [alias1, alias2]
---

# 命令标题

命令的详细说明和执行步骤。
```

#### 示例：快速提交命令

**文件**：`~/.claude/commands/push.md`

```markdown
---
name: push
description: 快速提交并推送代码
aliases: [p, commit-push]
---

# 快速提交和推送

执行步骤：
1. 运行 `git add -A`
2. 询问提交信息
3. 运行 `git commit`
4. 推送到远程仓库

提交信息格式：
- feat: 新功能
- fix: 修复bug
- docs: 文档更新
- style: 代码格式
```

#### 示例：代码修复命令

**文件**：`~/.claude/commands/fix.md`

```markdown
---
name: fix
description: 自动修复代码问题
aliases: [autofix, lint-fix]
---

# 自动代码修复

执行步骤：
1. 运行 linter 检测问题
2. 自动修复格式问题
3. 显示修复报告
4. 提示无法自动修复的问题

支持的工具：
- ESLint（JavaScript/TypeScript）
- Black（Python）
- Prettier（通用格式化）
```

#### 示例：代码审查命令

**文件**：`~/.claude/commands/review.md`

```markdown
---
name: review
description: 完整的代码审查流程
aliases: [cr, code-review]
---

# 代码审查

审查维度：
1. 代码质量（命名、结构、可读性）
2. 潜在问题（空指针、边界条件、性能）
3. 安全性（SQL注入、XSS、权限）
4. 最佳实践（错误处理、测试覆盖）

输出报告包括：
- 优点
- 问题列表（高/中/低危）
- 改进建议
- 下一步行动
```

### 使用自定义命令

```bash
# 启动 Claude Code
claude

# 使用命令
> /push
> /fix
> /review

# 使用别名
> /p
> /cr
```

---

## MCP 服务器配置

### 文件位置

```bash
~/.claude/.mcp.json
```

### 配置示例

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<your_token>"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_DIRECTORIES": "/Users/username/projects"
      }
    },
    "brave-search": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "<your_api_key>"
      }
    }
  }
}
```

### 常用 MCP 服务器

| 服务器 | 功能 | 包名 |
|--------|------|------|
| GitHub | 仓库管理、PR、Issues | `@modelcontextprotocol/server-github` |
| Filesystem | 文件系统访问 | `@modelcontextprotocol/server-filesystem` |
| Brave Search | 网络搜索 | `@modelcontextprotocol/server-brave-search` |
| Postgres | 数据库查询 | `@modelcontextprotocol/server-postgres` |

### 启用 MCP 服务器

```bash
# 安装服务器包
npm install -g @modelcontextprotocol/server-github

# 配置 .mcp.json

# 重启 Claude Code
claude
```

---

## 配置优先级

当项目和全局都有配置时：

```
项目配置 > 全局配置
```

**示例**：

- `~/.claude/settings.json` - 全局允许 WebSearch
- `.claude/settings.json` - 项目禁止 WebSearch
- **结果**: 在该项目中禁止 WebSearch

---

## 配置管理最佳实践

### 1. 版本控制

```bash
# 备份配置
cp ~/.claude/settings.json ~/.claude/settings.json.backup

# 使用 Git 管理配置
cd ~/.claude
git init
git add settings.json CLAUDE.md commands/
git commit -m "初始配置"
```

### 2. 配置分离

- **全局**: 通用设置、常用命令
- **项目**: 项目特定的配置和命令

### 3. 定期审查

- 每季度检查权限配置
- 删除不再使用的自定义命令
- 更新 CLAUDE.md 中的最佳实践

### 4. 安全检查清单

- [ ] 禁止读取敏感文件
- [ ] 禁止破坏性命令
- [ ] 限制网络访问
- [ ] 重要操作需要确认

---

## 下一步

全局配置完成后，建议：

- [项目配置指南](./project-configuration.md) - 为具体项目创建 CLAUDE.md
- [项目模板](../templates/) - 查看不同类型项目的配置模板
- [基础使用手册](../../basic-guide.md) - 学习基本功能

---

## 参考资源

- [Claude Code 权限系统详解](https://www.petefreitag.com/blog/claude-code-permissions/)
- [settings.json 配置指南](https://www.eesel.ai/blog/settings-json-claude-code)
- [自定义命令文档](https://docs.anthropic.com/claude-code/custom-commands)
- [MCP 服务器文档](https://docs.anthropic.com/claude-code/mcp)
