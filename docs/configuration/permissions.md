# Claude Code 权限配置完整指南

> 本指南详细介绍如何使用 `/permissions` 命令和配置文件管理 Claude Code 的工具访问权限

---

## 📋 目录

- [基本概念](#基本概念)
- [快速开始](#快速开始)
- [全局配置](#全局配置)
- [项目配置](#项目配置)
- [权限优先级](#权限优先级)
- [配置案例](#配置案例)
- [常见问题](#常见问题)

---

## 基本概念

### `/permissions` 命令

在 Claude Code 中输入：

```bash
/permissions
```

这个命令会打开一个**交互式用户界面**，让你能够：
- ✓ 查看所有当前生效的权限规则
- ✓ 查看每条规则来自哪个配置文件
- ✓ 更新和管理工具访问控制
- ✓ 为特定工具和 MCP 连接设置权限

### 权限规则的三种类型

| 规则类型 | 说明 | 优先级 | 使用场景 |
|---------|------|--------|----------|
| **Allow** (允许) | 无需确认直接授予工具访问权限 | 低 | 常用的安全操作，如读取代码文件 |
| **Ask** (询问) | 执行前需要用户确认 | 中 | 重要操作，如 git commit、npm publish |
| **Deny** (拒绝) | 完全阻止工具访问 | 高 | 危险操作或敏感文件，如 rm、.env |

**关键原则**：
- **Deny** 规则会覆盖 **Ask** 和 **Allow** 规则
- **Ask** 规则会覆盖 **Allow** 规则
- 更具体的规则优先于通用规则

---

## 快速开始

### 方法 1: 使用交互式界面（推荐新手）

```bash
# 1. 打开权限管理界面
/permissions

# 2. 在界面中操作：
#    - 查看现有规则
#    - 点击"添加规则"
#    - 选择规则类型（Allow/Ask/Deny）
#    - 输入工具名称和条件
#    - 选择保存位置（全局/项目）
```

### 方法 2: 直接编辑配置文件（推荐有经验用户）

```bash
# 编辑全局配置（对所有项目生效）
nano ~/.claude/settings.json

# 或编辑项目配置（仅对当前项目生效）
nano .claude/settings.json
```

修改后自动生效，**无需重启**。

---

## 全局配置

### 配置文件位置

```
~/.claude/settings.json
```

这个文件对您计算机上的**所有项目**生效。

### 基本配置格式

```json
{
  "permissions": {
    "allow": [
      "工具名(条件)",
      "工具名(条件)"
    ],
    "ask": [
      "工具名(条件)"
    ],
    "deny": [
      "工具名(条件)"
    ]
  }
}
```

### 规则语法详解

#### 1. 工具级别规则

```json
{
  "permissions": {
    "allow": [
      "Read",           // 允许所有 Read 操作
      "Edit",           // 允许所有 Edit 操作
      "Bash"            // 允许所有 Bash 命令（不推荐！）
    ]
  }
}
```

#### 2. Bash 命令规则（前缀匹配）

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run test:*)",    // 允许所有以 "npm run test" 开头的命令
      "Bash(git status:*)",      // 允许 git status
      "Bash(ls:*)"               // 允许所有 ls 命令
    ],
    "ask": [
      "Bash(git push:*)",        // 执行前需确认
      "Bash(npm publish:*)"      // 执行前需确认
    ],
    "deny": [
      "Bash(sudo:*)",            // 完全禁止 sudo
      "Bash(rm:*)",              // 完全禁止 rm 命令
      "Bash(curl:*)",            // 完全禁止 curl
      "Bash(wget:*)"             // 完全禁止 wget
    ]
  }
}
```

**注意**：
- 规则使用**前缀匹配**，不是正则表达式
- `Bash(npm run test:*)` 会匹配所有以 `npm run test` 开头的命令
- `:*` 是固定语法，不要省略

#### 3. 文件路径规则（gitignore 语法）

```json
{
  "permissions": {
    "allow": [
      "Read(/src/**)",           // 允许读取 src 目录下所有文件
      "Edit(/src/**/*.js)",      // 允许编辑所有 JS 文件
      "Read(~/.zshrc)"           // 允许读取特定文件
    ],
    "deny": [
      "Read(.env*)",             // 禁止读取所有 .env 文件
      "Read(./.env*)",           // 同上
      "Read(/secrets/**)",       // 禁止读取 secrets 目录
      "Edit(/etc/**)"            // 禁止编辑系统配置
    ]
  }
}
```

**通配符规则**：
- `*` - 匹配单层目录中的任意字符
- `**` - 匹配任意层级目录
- `.env*` - 匹配 .env、.env.local、.env.production 等

### 全局配置示例（推荐）

```json
{
  "permissions": {
    "allow": [
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(grep:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(npm run test:*)",
      "Bash(npm run lint:*)",
      "Read",
      "Edit(/src/**)",
      "Edit(/docs/**)",
      "WebFetch",
      "Grep",
      "Glob"
    ],
    "ask": [
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(npm install:*)",
      "Bash(npm publish:*)",
      "Bash(docker:*)",
      "Write"
    ],
    "deny": [
      "Bash(sudo:*)",
      "Bash(rm:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Read(.env*)",
      "Read(secrets/**)",
      "Edit(.env*)"
    ]
  }
}
```

---

## 项目配置

### 两种项目配置文件

#### 1. `.claude/settings.json` (团队共享配置)

**特点**：
- ✓ 提交到代码仓库
- ✓ 对整个团队生效
- ✓ 在 git 版本控制中追踪
- ✓ 定义项目级别的安全策略

**示例**：
```json
{
  "permissions": {
    "allow": [
      "Bash(npm run test:*)",
      "Bash(npm run build:*)",
      "Bash(npm run dev:*)",
      "Edit(/src/**)",
      "Edit(/tests/**)"
    ],
    "ask": [
      "Bash(npm publish:*)",
      "Bash(git push:*)"
    ],
    "deny": [
      "Bash(rm:*)",
      "Read(.env*)",
      "Edit(/config/production.json)"
    ]
  }
}
```

#### 2. `.claude/settings.local.json` (个人本地配置)

**特点**：
- ✓ 不提交到仓库（应添加到 `.gitignore`）
- ✓ 仅对您的本地环境生效
- ✓ 用于个人覆盖或敏感配置
- ✓ 优先级高于 `.claude/settings.json`

**示例**：
```json
{
  "permissions": {
    "allow": [
      "Read(.env.local)",         // 允许读取个人本地环境变量
      "Bash(docker compose:*)"    // 个人开发环境允许 docker
    ],
    "deny": [
      "Bash(git push:*)"          // 个人禁止直接 push（使用 PR 流程）
    ]
  }
}
```

**`.gitignore` 配置**：
```gitignore
# Claude Code 本地配置（不提交）
.claude/settings.local.json
```

### 项目配置示例

#### 示例 1: 前端项目

**`.claude/settings.json`**：
```json
{
  "permissions": {
    "allow": [
      "Bash(npm run dev:*)",
      "Bash(npm run test:*)",
      "Bash(npm run lint:*)",
      "Bash(npm run build:*)",
      "Edit(/src/**)",
      "Edit(/public/**)",
      "Read"
    ],
    "ask": [
      "Bash(npm install:*)",
      "Bash(git commit:*)",
      "Write"
    ],
    "deny": [
      "Bash(rm:*)",
      "Read(.env*)",
      "Edit(/node_modules/**)"
    ]
  }
}
```

#### 示例 2: Python 数据科学项目

**`.claude/settings.json`**：
```json
{
  "permissions": {
    "allow": [
      "Bash(python:*)",
      "Bash(pip install:*)",
      "Bash(jupyter:*)",
      "Edit(/notebooks/**)",
      "Edit(/src/**)",
      "Read(/data/**)"
    ],
    "ask": [
      "Bash(rm:*)",
      "Edit(/data/**)"
    ],
    "deny": [
      "Read(/data/credentials/**)",
      "Edit(/data/raw/**)"
    ]
  }
}
```

#### 示例 3: 严格安全项目

**`.claude/settings.json`**：
```json
{
  "permissions": {
    "allow": [
      "Read(/src/**)",
      "Read(/tests/**)",
      "Read(/docs/**)"
    ],
    "ask": [
      "Edit(/src/**)",
      "Edit(/tests/**)",
      "Bash(npm:*)",
      "Bash(git:*)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(sudo:*)",
      "Read(.env*)",
      "Read(/secrets/**)",
      "Read(/config/production.*)",
      "Edit(.env*)",
      "Write"
    ]
  }
}
```

---

## 权限优先级

权限配置按以下顺序应用，**上面的优先级更高**：

```
1. 企业托管策略 (最高优先级，无法覆盖)
   ├─ Linux/Mac: /etc/claude-code/settings.json
   └─ Windows: C:\ProgramData\ClaudeCode\settings.json

2. 命令行参数
   └─ claude --system-prompt "..."

3. 项目本地配置 (个人覆盖)
   └─ .claude/settings.local.json

4. 项目共享配置 (团队规则)
   └─ .claude/settings.json

5. 全局用户配置 (默认规则)
   └─ ~/.claude/settings.json
```

### 优先级示例

假设有以下配置：

**全局配置** (`~/.claude/settings.json`)：
```json
{
  "permissions": {
    "allow": ["Bash(rm:*)"]
  }
}
```

**项目配置** (`.claude/settings.json`)：
```json
{
  "permissions": {
    "deny": ["Bash(rm:*)"]
  }
}
```

**结果**：`Bash(rm:*)` 被**拒绝**，因为项目配置优先级更高。

---

## 配置案例

### 案例 1: 开发环境（宽松）

**适用场景**：个人学习、快速原型开发

```json
{
  "permissions": {
    "allow": [
      "Bash(npm:*)",
      "Bash(git:*)",
      "Bash(python:*)",
      "Bash(docker:*)",
      "Read",
      "Edit",
      "Write",
      "WebFetch"
    ],
    "ask": [
      "Bash(sudo:*)"
    ],
    "deny": [
      "Bash(rm -rf /:*)"
    ]
  }
}
```

### 案例 2: 生产环境（严格）

**适用场景**：生产代码、敏感项目

```json
{
  "permissions": {
    "allow": [
      "Read(/src/**)",
      "Read(/tests/**)",
      "Bash(git status:*)",
      "Bash(git diff:*)"
    ],
    "ask": [
      "Edit(/src/**)",
      "Edit(/tests/**)",
      "Bash(git commit:*)",
      "Bash(npm:*)"
    ],
    "deny": [
      "Bash(rm:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(sudo:*)",
      "Read(.env*)",
      "Read(/secrets/**)",
      "Read(/config/production.*)",
      "Edit(.env*)",
      "Edit(/config/**)",
      "Write"
    ]
  }
}
```

### 案例 3: 数据安全优先

**适用场景**：处理敏感数据、金融/医疗项目

```json
{
  "permissions": {
    "allow": [
      "Read(/src/**)",
      "Read(/docs/**)"
    ],
    "ask": [
      "Edit(/src/**)",
      "Bash(git:*)",
      "Bash(npm:*)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(nc:*)",
      "Bash(telnet:*)",
      "Bash(ssh:*)",
      "Bash(scp:*)",
      "Read(.env*)",
      "Read(/data/**)",
      "Read(/secrets/**)",
      "Read(**/*credential*)",
      "Read(**/*password*)",
      "Read(**/*key*)",
      "Edit(.env*)",
      "Edit(/data/**)",
      "WebFetch",
      "Write"
    ]
  }
}
```

### 案例 4: 前端开发（平衡）

**适用场景**：React/Vue/Angular 项目

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run dev:*)",
      "Bash(npm run test:*)",
      "Bash(npm run lint:*)",
      "Bash(npm run build:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Read",
      "Edit(/src/**)",
      "Edit(/public/**)",
      "Edit(/tests/**)",
      "Grep",
      "Glob",
      "WebFetch"
    ],
    "ask": [
      "Bash(npm install:*)",
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Write"
    ],
    "deny": [
      "Bash(sudo:*)",
      "Bash(rm:*)",
      "Read(.env*)",
      "Edit(.env*)",
      "Edit(/node_modules/**)",
      "Edit(/package-lock.json)"
    ]
  }
}
```

### 案例 5: Python/AI 项目

**适用场景**：机器学习、数据分析

```json
{
  "permissions": {
    "allow": [
      "Bash(python:*)",
      "Bash(pip install:*)",
      "Bash(jupyter:*)",
      "Bash(pytest:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Read",
      "Edit(/src/**)",
      "Edit(/notebooks/**)",
      "Edit(/tests/**)",
      "Grep",
      "Glob"
    ],
    "ask": [
      "Bash(git commit:*)",
      "Edit(/data/**)",
      "Write"
    ],
    "deny": [
      "Bash(sudo:*)",
      "Bash(rm:*)",
      "Read(.env*)",
      "Read(/data/credentials/**)",
      "Edit(.env*)",
      "Edit(/data/raw/**)"
    ]
  }
}
```

---

## 常见问题

### Q1: 配置文件修改后需要重启吗？

**A**: 不需要。配置文件修改后会**自动生效**，无需重启 Claude Code。

---

### Q2: 如何查看当前生效的规则？

**A**: 运行 `/permissions` 命令，会显示所有规则及其来源。

---

### Q3: 项目配置和全局配置冲突怎么办？

**A**: 项目配置优先级更高。具体优先级请参考 [权限优先级](#权限优先级) 部分。

---

### Q4: 如何禁止读取所有 .env 文件？

**A**: 使用通配符：

```json
{
  "permissions": {
    "deny": [
      "Read(.env*)",
      "Read(**/.env*)",
      "Edit(.env*)",
      "Edit(**/.env*)"
    ]
  }
}
```

---

### Q5: 如何允许特定目录下的所有操作？

**A**: 使用 `**` 通配符：

```json
{
  "permissions": {
    "allow": [
      "Read(/src/**)",
      "Edit(/src/**)",
      "Write(/src/**)"
    ]
  }
}
```

---

### Q6: Bash 规则的 `:*` 是什么意思？

**A**: `:*` 表示**前缀匹配**。例如：
- `Bash(npm run test:*)` 匹配所有以 `npm run test` 开头的命令
- `Bash(git:*)` 匹配所有以 `git` 开头的命令
- 这不是正则表达式，而是固定的语法格式

---

### Q7: 如何临时覆盖规则？

**A**: 使用 `.claude/settings.local.json`（优先级最高的用户配置）：

```json
{
  "permissions": {
    "allow": [
      "Bash(sudo apt install:*)"
    ]
  }
}
```

这个配置不会提交到 git，仅影响您的本地环境。

---

### Q8: 企业环境如何统一管理？

**A**: 系统管理员可以在以下位置放置全局策略文件：
- Linux/Mac: `/etc/claude-code/settings.json`
- Windows: `C:\ProgramData\ClaudeCode\settings.json`

这些策略**优先级最高**，用户无法覆盖。

---

### Q9: 如何调试权限问题？

**方法 1**: 使用 `/permissions` 查看所有规则

**方法 2**: 查看 Claude Code 日志：
```bash
# Linux/Mac
tail -f ~/.claude/logs/claude-code.log

# Windows
Get-Content "$env:USERPROFILE\.claude\logs\claude-code.log" -Tail 50 -Wait
```

**方法 3**: 临时添加 Allow 规则测试：
```json
{
  "permissions": {
    "allow": ["Bash(你要测试的命令:*)"]
  }
}
```

---

### Q10: 如何分享配置给团队？

**步骤**：

1. 创建 `.claude/settings.json`
2. 提交到 git 仓库
3. 团队成员拉取代码后自动生效

**示例**：
```bash
# 创建配置
mkdir -p .claude
cat > .claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": ["Bash(npm run test:*)"],
    "deny": ["Bash(rm:*)"]
  }
}
EOF

# 提交到 git
git add .claude/settings.json
git commit -m "feat: 添加 Claude Code 权限配置"
git push
```

---

## 最佳实践

### ✓ DO (推荐做法)

1. **使用最小权限原则**
   ```json
   {
     "permissions": {
       "allow": ["Read(/src/**)"],  // 只允许必要的操作
       "ask": ["Edit(/src/**)"],     // 重要操作需确认
       "deny": ["Bash(rm:*)"]        // 危险操作完全禁止
     }
   }
   ```

2. **分离敏感配置**
   - 团队规则 → `.claude/settings.json`（提交到 git）
   - 个人规则 → `.claude/settings.local.json`（不提交）

3. **使用具体的路径**
   ```json
   {
     "permissions": {
       "deny": [
         "Read(.env*)",
         "Read(/secrets/**)",
         "Read(/config/production.json)"
       ]
     }
   }
   ```

4. **分层管理**
   - 全局配置：通用安全规则
   - 项目配置：项目特定规则
   - 本地配置：个人偏好

### ✗ DON'T (避免做法)

1. **过度宽松的全局配置**
   ```json
   {
     "permissions": {
       "allow": ["Bash"]  // ❌ 允许所有 Bash 命令（危险！）
     }
   }
   ```

2. **在项目配置中包含个人敏感信息**
   ```json
   // ❌ 不要在 .claude/settings.json 中写个人配置
   {
     "permissions": {
       "allow": ["Read(/home/myname/.ssh/*)"]
     }
   }
   ```

3. **忽略 Deny 规则**
   ```json
   {
     "permissions": {
       "allow": ["Bash(rm:*)"]  // ❌ 危险！应该用 ask 或 deny
     }
   }
   ```

---

## 快速参考卡片

### 常用命令

| 命令 | 说明 |
|------|------|
| `/permissions` | 打开权限管理界面 |
| `nano ~/.claude/settings.json` | 编辑全局配置 |
| `nano .claude/settings.json` | 编辑项目配置 |
| `cat ~/.claude/settings.json` | 查看全局配置 |

### 配置文件位置

| 类型 | 路径 | 优先级 | 是否提交 git |
|------|------|--------|-------------|
| 全局 | `~/.claude/settings.json` | 低 | ❌ |
| 项目共享 | `.claude/settings.json` | 中 | ✓ |
| 项目本地 | `.claude/settings.local.json` | 高 | ❌ |
| 企业策略 | `/etc/claude-code/settings.json` | 最高 | ❌ |

### 规则语法速查

| 规则 | 示例 | 说明 |
|------|------|------|
| 工具级别 | `"Read"` | 允许/拒绝所有该工具操作 |
| Bash 前缀 | `"Bash(npm run test:*)"` | 匹配以该命令开头的所有命令 |
| 文件路径 | `"Read(/src/**)"` | gitignore 风格通配符 |
| 环境文件 | `"Read(.env*)"` | 匹配所有 .env 开头的文件 |

---

## 附录

### A. 完整配置模板

```json
{
  "permissions": {
    "allow": [
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(grep:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(npm run test:*)",
      "Bash(npm run lint:*)",
      "Bash(npm run dev:*)",
      "Read",
      "Grep",
      "Glob",
      "WebFetch"
    ],
    "ask": [
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(npm install:*)",
      "Bash(docker:*)",
      "Edit",
      "Write"
    ],
    "deny": [
      "Bash(sudo:*)",
      "Bash(rm:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Read(.env*)",
      "Read(**/.env*)",
      "Read(/secrets/**)",
      "Edit(.env*)",
      "Edit(**/.env*)"
    ]
  }
}
```

### B. 工具列表

常见的 Claude Code 工具：
- `Bash` - 执行 shell 命令
- `Read` - 读取文件
- `Edit` - 编辑文件
- `Write` - 创建新文件
- `Grep` - 搜索代码
- `Glob` - 查找文件
- `WebFetch` - 获取网页内容
- `Task` - 启动子代理

### C. 相关文档

- [官方资源索引](../resources/official-resources.md)
- [返回主文档](../../README.md)

---

**最后更新**: 2025-11-27
**文档版本**: 1.0
**适用于**: Claude Code (所有版本)
