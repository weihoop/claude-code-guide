# Claude Code 安全使用手册

> 本手册提供使用 Claude Code 时的安全最佳实践，保护代码、数据和系统安全

---

## 📋 目录

- [安全概述](#安全概述)
- [敏感信息保护](#敏感信息保护)
- [权限配置安全](#权限配置安全)
- [代码审查安全](#代码审查安全)
- [命令执行安全](#命令执行安全)
- [文件访问控制](#文件访问控制)
- [网络安全](#网络安全)
- [团队协作安全](#团队协作安全)
- [企业环境安全](#企业环境安全)
- [安全检查清单](#安全检查清单)
- [应急响应](#应急响应)

---

## 🔒 安全概述

### 为什么需要安全配置？

Claude Code 具有强大的代码操作能力，如果配置不当可能导致：

| 风险类型 | 潜在影响 | 严重程度 |
|---------|---------|---------|
| 敏感信息泄露 | API 密钥、密码暴露 | 🔴 高危 |
| 误删除文件 | 重要文件丢失 | 🔴 高危 |
| 未授权访问 | 系统文件被修改 | 🟠 中危 |
| 恶意代码注入 | 安全漏洞引入 | 🔴 高危 |
| 配置错误 | 生产环境受损 | 🟠 中危 |

### 安全三原则

1. **最小权限原则** - 只授予必需的最小权限
2. **纵深防御** - 多层安全措施，互为补充
3. **持续审计** - 定期检查和更新安全配置

---

## 🔐 敏感信息保护

### 1. 禁止访问敏感文件

**配置权限拒绝访问**：

```json
{
  "permissions": {
    "deny": [
      "Read(.env*)",
      "Read(**/.env*)",
      "Read(**/secrets/**)",
      "Read(**/*credential*)",
      "Read(**/*password*)",
      "Read(**/*secret*)",
      "Read(**/*key*)",
      "Read(**/*token*)",
      "Read(**/*.pem)",
      "Read(**/*.key)",
      "Read(**/*.p12)",
      "Read(**/*.pfx)",
      "Edit(.env*)",
      "Edit(**/.env*)",
      "Edit(**/secrets/**)",
      "Write(.env*)",
      "Write(**/secrets/**)"
    ]
  }
}
```

### 2. 环境变量文件保护

**正确的做法** ✅：

```bash
# .env 文件（不提交到 git）
API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:pass@localhost/db
JWT_SECRET=your_jwt_secret
```

```javascript
// config.js - 使用环境变量
const config = {
  apiKey: process.env.API_KEY,
  dbUrl: process.env.DATABASE_URL,
  jwtSecret: process.env.JWT_SECRET
};
```

**错误的做法** ❌：

```javascript
// config.js - 硬编码（危险！）
const config = {
  apiKey: 'sk-1234567890abcdef',  // ❌ 不要这样做
  dbUrl: 'postgresql://user:password@localhost/db',  // ❌ 暴露密码
  jwtSecret: 'my-secret-key'  // ❌ 明文密钥
};
```

### 3. Git 忽略敏感文件

**.gitignore 配置**：

```gitignore
# 环境变量文件
.env
.env.local
.env.development
.env.test
.env.production
.env.*.local

# 密钥文件
*.pem
*.key
*.p12
*.pfx
secrets/
credentials/

# 配置文件
config/credentials.yml
config/master.key
config/secrets.yml

# 数据库文件
*.db
*.sqlite
*.sqlite3

# 日志文件可能包含敏感信息
logs/
*.log

# 备份文件
*.bak
*.backup
*.old

# IDE 配置可能包含路径
.vscode/
.idea/
```

### 4. 敏感信息检测 Hook

创建自动检测脚本：

```javascript
// .claude/hooks/detect-secrets.js
const fs = require('fs');

// 敏感信息模式
const SENSITIVE_PATTERNS = [
  {
    pattern: /password\s*=\s*["'][^"']{3,}["']/gi,
    message: '检测到硬编码密码'
  },
  {
    pattern: /api[_-]?key\s*=\s*["'][^"']{10,}["']/gi,
    message: '检测到硬编码 API Key'
  },
  {
    pattern: /secret\s*=\s*["'][^"']{8,}["']/gi,
    message: '检测到硬编码 Secret'
  },
  {
    pattern: /token\s*=\s*["'][^"']{20,}["']/gi,
    message: '检测到硬编码 Token'
  },
  {
    pattern: /(sk|pk)_live_[a-zA-Z0-9]{24,}/g,
    message: '检测到 Stripe 生产密钥'
  },
  {
    pattern: /ghp_[a-zA-Z0-9]{36}/g,
    message: '检测到 GitHub Personal Access Token'
  },
  {
    pattern: /AKIA[0-9A-Z]{16}/g,
    message: '检测到 AWS Access Key'
  }
];

// 获取工具参数
const toolName = process.env.TOOL_NAME;
const toolArgs = JSON.parse(process.env.TOOL_ARGS || '{}');

if (toolName === 'Write' || toolName === 'Edit') {
  const content = toolArgs.content || toolArgs.new_string || '';
  const filePath = toolArgs.file_path;

  // 检查是否是配置文件（跳过检查）
  if (filePath && filePath.match(/\.(env|example)$/)) {
    process.exit(0);  // .env.example 允许示例值
  }

  // 检测敏感信息
  for (const { pattern, message } of SENSITIVE_PATTERNS) {
    if (pattern.test(content)) {
      console.error(`🚨 安全警告: ${message}`);
      console.error(`文件: ${filePath}`);
      console.error(`\n建议:`);
      console.error(`1. 使用环境变量代替硬编码`);
      console.error(`2. 将敏感值存储在 .env 文件中`);
      console.error(`3. 确保 .env 文件已添加到 .gitignore`);
      process.exit(1);  // 阻止操作
    }
  }
}

process.exit(0);  // 允许操作
```

**配置 Hook**：

```json
{
  "hooks": {
    "tool-call-hook": {
      "command": "node",
      "args": [".claude/hooks/detect-secrets.js"]
    }
  }
}
```

### 4.1 远程命令防火 Hook（sshpass / ssh）

**场景**：在自动接受模式（`acceptEdits`）下，`sshpass -p 密码 ssh host "..."` 这类命令会无提示执行。一旦远程命令里藏了 `rm -rf`、`mkfs`、关机等破坏性操作，后果不可逆。

**为什么不用 `deny` 权限规则**：Claude Code 的 Bash 权限匹配以**前缀匹配**为主，`Bash(sshpass *rm -rf*)` 这种"中段通配 + 关键词"对藏在远程引号字符串里的命令**不保证命中**。可靠做法是用 **PreToolUse hook**——在命令执行前对**命令全文**跑正则，命中即拦（`exit 2`）。

> 关键点：现代 hook 从 **stdin 读 JSON**（不是老文档里的 `process.env.TOOL_ARGS`），字段为 `tool_name` / `tool_input.command`；`exit 2` 表示阻断并把 stderr 反馈给 Claude，`exit 0` 放行。

脚本 `~/.claude/hooks/sshpass-firewall.py`（完整版见 `config-templates/hooks/`）：

```python
#!/usr/bin/env python3
"""sshpass 防火 hook：拦截通过 sshpass 远程执行的破坏性命令。"""
import json, re, sys

DANGER_PATTERNS = [
    r"rm\s+-[rf]{1,2}\b",   r"\bmkfs\b",     r"\bdd\s+(if|of)=",
    r"\bshutdown\b",        r"\breboot\b",   r"\bpoweroff\b",
    r"\bhalt\b",            r">\s*/dev/sd[a-z]",
]

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)                       # 解析失败放行，避免误伤
    if data.get("tool_name") != "Bash":
        sys.exit(0)
    cmd = data.get("tool_input", {}).get("command", "")
    if "sshpass" not in cmd:
        sys.exit(0)
    for pat in DANGER_PATTERNS:
        if re.search(pat, cmd, re.IGNORECASE):
            print(f"[sshpass 防火] 已拦截破坏性命令（匹配 /{pat}/）。"
                  f"如确需执行请手动在终端运行。", file=sys.stderr)
            sys.exit(2)                   # exit 2 = 阻断
    sys.exit(0)

if __name__ == "__main__":
    main()
```

**配置（全局 `~/.claude/settings.json`）**：用 `if` 条件让 hook 只对 sshpass 命令触发，不拖累其他命令：

```json
{
  "permissions": {
    "defaultMode": "acceptEdits",
    "allow": ["Bash(sshpass:*)"]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command",
            "command": "python3 ~/.claude/hooks/sshpass-firewall.py",
            "if": "Bash(sshpass *)" }
        ]
      }
    ]
  }
}
```

**要点**：
- hook 在 `~/.claude/` 下，**不进 git、不随仓库同步**——换机器要重新部署（这正是把它沉淀进本指南的原因）。
- 该思路通用：把 `sshpass` 换成任何高危命令前缀、调整 `DANGER_PATTERNS` 即可复用。
- `defaultMode: acceptEdits` 减少手动确认，但它**只自动接受已 allow 的命令和文件编辑**，不放行未知危险命令；hook 是第二道兜底。

### 5. 密钥轮换策略

**定期轮换密钥**：

```bash
# 生成新密钥
NEW_API_KEY=$(openssl rand -hex 32)

# 更新环境变量
echo "API_KEY=$NEW_API_KEY" > .env

# 撤销旧密钥（在服务提供商后台）
```

**密钥轮换检查清单**：

- [ ] 生成新密钥
- [ ] 更新所有环境的配置
- [ ] 验证新密钥工作正常
- [ ] 撤销旧密钥
- [ ] 更新文档
- [ ] 通知团队成员

---

## 🛡️ 权限配置安全

### 安全权限模板

#### 开发环境（个人电脑）

```json
{
  "permissions": {
    "allow": [
      "Read(/src/**)",
      "Read(/tests/**)",
      "Read(/docs/**)",
      "Grep",
      "Glob",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(npm run test:*)",
      "Bash(npm run lint:*)",
      "Bash(npm run dev:*)"
    ],
    "ask": [
      "Edit(/src/**)",
      "Edit(/tests/**)",
      "Write",
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(npm install:*)",
      "Bash(docker:*)"
    ],
    "deny": [
      "Bash(sudo:*)",
      "Bash(rm:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(nc:*)",
      "Bash(ssh:*)",
      "Read(.env*)",
      "Read(**/secrets/**)",
      "Edit(.env*)",
      "Edit(/node_modules/**)",
      "Edit(/package-lock.json)"
    ]
  }
}
```

#### 生产环境（严格限制）

```json
{
  "permissions": {
    "allow": [
      "Read(/src/**)",
      "Read(/tests/**)",
      "Grep",
      "Glob"
    ],
    "ask": [
      "Edit(/src/**)",
      "Edit(/tests/**)",
      "Bash(git status:*)",
      "Bash(git diff:*)"
    ],
    "deny": [
      "Bash(sudo:*)",
      "Bash(rm:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(ssh:*)",
      "Bash(scp:*)",
      "Bash(nc:*)",
      "Bash(telnet:*)",
      "Bash(git push:*)",
      "Bash(npm publish:*)",
      "Bash(docker:*)",
      "Read(.env*)",
      "Read(**/secrets/**)",
      "Read(**/config/production.*)",
      "Read(**/credentials/**)",
      "Edit(.env*)",
      "Edit(**/config/production.*)",
      "Edit(/node_modules/**)",
      "Write",
      "WebFetch"
    ]
  }
}
```

### 权限配置验证

**验证脚本**：

```bash
#!/bin/bash
# verify-permissions.sh

echo "🔍 验证 Claude Code 权限配置..."

CONFIG_FILE=".claude/settings.json"

if [ ! -f "$CONFIG_FILE" ]; then
  echo "❌ 未找到配置文件: $CONFIG_FILE"
  exit 1
fi

# 检查是否拒绝了危险命令
DANGEROUS_CMDS=("sudo" "rm" "curl" "wget" "ssh")
for cmd in "${DANGEROUS_CMDS[@]}"; do
  if ! grep -q "\"Bash($cmd:" "$CONFIG_FILE"; then
    echo "⚠️  建议禁止: Bash($cmd:*)"
  fi
done

# 检查是否保护了敏感文件
if ! grep -q "\"Read(.env" "$CONFIG_FILE"; then
  echo "⚠️  建议禁止读取: .env 文件"
fi

# 检查是否禁止网络访问（生产环境）
if [ "$ENV" = "production" ]; then
  if ! grep -q "\"WebFetch\"" "$CONFIG_FILE"; then
    echo "⚠️  生产环境建议禁止: WebFetch"
  fi
fi

echo "✅ 权限配置验证完成"
```

---

## 🔍 代码审查安全

### 1. 自动安全审查 Skill

创建安全审查 Skill：

```markdown
<!-- .claude/skills/security-audit/prompt.md -->

# 代码安全审查 Skill

对代码进行全面的安全审查，识别常见安全漏洞。

## 检查项目

### 1. 注入攻击
- SQL 注入
- XSS (跨站脚本)
- 命令注入
- LDAP 注入
- XML 注入

### 2. 认证和授权
- 弱密码策略
- 会话管理漏洞
- 未授权访问
- 权限提升

### 3. 敏感数据
- 硬编码凭据
- 明文存储密码
- 日志中的敏感信息
- 不安全的加密

### 4. 配置安全
- 默认配置
- 调试模式启用
- 错误信息泄露
- CORS 配置错误

### 5. 依赖安全
- 已知漏洞的依赖
- 过时的库版本
- 不受信任的来源

## 输出格式

```markdown
## 🔒 安全审查报告

### 🔴 高危问题
- [文件:行号] 问题描述
  - 风险: 具体风险说明
  - 建议: 修复建议

### 🟠 中危问题
- ...

### 🟡 低危问题
- ...

### ✅ 安全建议
- ...
```
```

### 2. 常见安全漏洞检查

#### SQL 注入检查

**不安全的代码** ❌：

```javascript
// 直接拼接 SQL（危险！）
const userId = req.params.id;
const sql = `SELECT * FROM users WHERE id = ${userId}`;
db.query(sql);
```

**安全的代码** ✅：

```javascript
// 使用参数化查询
const userId = req.params.id;
const sql = 'SELECT * FROM users WHERE id = ?';
db.query(sql, [userId]);
```

#### XSS 防护检查

**不安全的代码** ❌：

```javascript
// 直接插入用户输入（危险！）
element.innerHTML = userInput;
```

**安全的代码** ✅：

```javascript
// 转义用户输入
element.textContent = userInput;
// 或使用安全的库
element.innerHTML = DOMPurify.sanitize(userInput);
```

#### 命令注入检查

**不安全的代码** ❌：

```javascript
// 直接拼接命令（危险！）
const filename = req.query.file;
exec(`cat ${filename}`);
```

**安全的代码** ✅：

```javascript
// 验证输入并使用安全的 API
const filename = path.basename(req.query.file);
fs.readFile(filename, 'utf8', callback);
```

---

## ⚡ 命令执行安全

### 1. 禁止危险命令

```json
{
  "permissions": {
    "deny": [
      "Bash(sudo:*)",
      "Bash(su:*)",
      "Bash(rm:*)",
      "Bash(rmdir:*)",
      "Bash(dd:*)",
      "Bash(mkfs:*)",
      "Bash(fdisk:*)",
      "Bash(chmod 777:*)",
      "Bash(chown:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(nc:*)",
      "Bash(ncat:*)",
      "Bash(telnet:*)",
      "Bash(ssh:*)",
      "Bash(scp:*)",
      "Bash(rsync:*)",
      "Bash(> /dev:*)",
      "Bash(kill -9:*)"
    ]
  }
}
```

### 2. 命令白名单

**只允许安全的命令**：

```json
{
  "permissions": {
    "allow": [
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(npm run test:*)",
      "Bash(npm run lint:*)",
      "Bash(npm run build:*)",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(grep:*)",
      "Bash(find:*)"
    ],
    "deny": ["Bash"]  // 默认拒绝所有其他命令
  }
}
```

### 3. 命令审计日志

```javascript
// .claude/hooks/audit-commands.js
const fs = require('fs');
const path = require('path');

const toolName = process.env.TOOL_NAME;
const toolArgs = JSON.parse(process.env.TOOL_ARGS || '{}');

if (toolName === 'Bash') {
  const command = toolArgs.command;
  const timestamp = new Date().toISOString();
  const logEntry = `${timestamp} | Bash | ${command}\n`;

  // 记录到审计日志
  const logFile = path.join(process.env.HOME, '.claude/audit.log');
  fs.appendFileSync(logFile, logEntry);

  // 检查是否是可疑命令
  const SUSPICIOUS_PATTERNS = [
    /sudo/i,
    /rm\s+-rf/i,
    /curl.*\|\s*bash/i,
    /wget.*\|\s*sh/i,
    /nc.*-e/i
  ];

  for (const pattern of SUSPICIOUS_PATTERNS) {
    if (pattern.test(command)) {
      console.error(`🚨 可疑命令: ${command}`);
      console.error(`已记录到审计日志: ${logFile}`);
      process.exit(1);
    }
  }
}

process.exit(0);
```

---

## 📂 文件访问控制

### 1. 目录访问限制

```json
{
  "permissions": {
    "allow": [
      "Read(/home/user/projects/**)",
      "Edit(/home/user/projects/*/src/**)"
    ],
    "deny": [
      "Read(/etc/**)",
      "Read(/root/**)",
      "Read(/home/user/.ssh/**)",
      "Read(/home/user/.aws/**)",
      "Read(/home/user/.config/**)",
      "Edit(/etc/**)",
      "Edit(/root/**)",
      "Write(/etc/**)",
      "Write(/root/**)"
    ]
  }
}
```

### 2. 文件类型限制

```json
{
  "permissions": {
    "deny": [
      "Read(**/*.pem)",
      "Read(**/*.key)",
      "Read(**/*.p12)",
      "Read(**/*.pfx)",
      "Read(**/*.cer)",
      "Read(**/*.crt)",
      "Read(**/*.der)",
      "Read(**/*.ppk)",
      "Edit(**/*.pem)",
      "Edit(**/*.key)"
    ]
  }
}
```

### 3. 文件完整性检查

```bash
#!/bin/bash
# check-file-integrity.sh

# 计算关键文件的哈希值
CRITICAL_FILES=(
  "package.json"
  "package-lock.json"
  ".env.example"
  "docker-compose.yml"
)

HASH_FILE=".file-hashes.txt"

for file in "${CRITICAL_FILES[@]}"; do
  if [ -f "$file" ]; then
    sha256sum "$file" >> "$HASH_FILE.new"
  fi
done

if [ -f "$HASH_FILE" ]; then
  if ! diff "$HASH_FILE" "$HASH_FILE.new" > /dev/null; then
    echo "⚠️  检测到关键文件被修改:"
    diff "$HASH_FILE" "$HASH_FILE.new"
  fi
fi

mv "$HASH_FILE.new" "$HASH_FILE"
```

---

## 🌐 网络安全

### 1. 限制网络访问

```json
{
  "permissions": {
    "deny": [
      "WebFetch",
      "WebSearch",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(nc:*)",
      "Bash(telnet:*)"
    ]
  }
}
```

### 2. 白名单域名（如需要网络访问）

```json
{
  "permissions": {
    "allow": [
      "WebFetch(https://api.github.com/*)",
      "WebFetch(https://registry.npmjs.org/*)"
    ],
    "deny": [
      "WebFetch"  // 拒绝其他所有域名
    ]
  }
}
```

### 3. MCP 服务器安全

```json
{
  "mcpServers": {
    "github": {
      "command": "mcp-server-github",
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"  // 使用环境变量
      }
    }
  },
  "permissions": {
    "mcpServers": {
      "github": {
        "allow": ["issues:read", "repo:read"],
        "deny": ["repo:delete", "admin:*"]
      }
    }
  }
}
```

---

## 👥 团队协作安全

### 1. 团队配置模板

```json
{
  "permissions": {
    "allow": [
      "Read(/src/**)",
      "Read(/tests/**)",
      "Grep",
      "Glob"
    ],
    "ask": [
      "Edit(/src/**)",
      "Edit(/tests/**)",
      "Bash(git:*)",
      "Bash(npm:*)"
    ],
    "deny": [
      "Bash(sudo:*)",
      "Bash(rm:*)",
      "Read(.env*)",
      "Edit(.env*)",
      "Write"
    ]
  },
  "hooks": {
    "tool-call-hook": {
      "command": "node",
      "args": [".claude/hooks/team-security-check.js"]
    }
  }
}
```

### 2. 代码审查流程

**PR 前检查**：

```bash
# .claude/commands/pre-pr.md
---
name: pre-pr
description: PR 前安全检查
---

# PR 前安全检查

1. **扫描敏感信息**
   ```bash
   git diff main | grep -E "(password|api[_-]?key|secret|token)" || true
   ```

2. **运行安全测试**
   ```bash
   npm audit
   npm run test:security
   ```

3. **检查依赖漏洞**
   ```bash
   npm audit --audit-level=moderate
   ```

4. **代码质量检查**
   ```bash
   npm run lint
   npm run test
   ```

5. **生成变更摘要**
   - 列出修改的文件
   - 说明变更原因
   - 标注潜在风险
```

### 3. 访问日志

```javascript
// .claude/hooks/access-log.js
const fs = require('fs');
const os = require('os');

const toolName = process.env.TOOL_NAME;
const toolArgs = JSON.parse(process.env.TOOL_ARGS || '{}');
const timestamp = new Date().toISOString();
const user = os.userInfo().username;

const logEntry = {
  timestamp,
  user,
  tool: toolName,
  args: toolArgs
};

const logFile = '.claude/access.log';
fs.appendFileSync(logFile, JSON.stringify(logEntry) + '\n');

process.exit(0);
```

---

## 🏢 企业环境安全

### 1. 企业策略模板

**位置**: `/etc/claude-code/settings.json` (Linux/Mac)

```json
{
  "permissions": {
    "deny": [
      "Bash(sudo:*)",
      "Bash(rm:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(ssh:*)",
      "Bash(scp:*)",
      "Bash(docker:*)",
      "Read(.env*)",
      "Read(**/secrets/**)",
      "Read(**/*credential*)",
      "Read(**/*password*)",
      "Read(/etc/**)",
      "Read(/root/**)",
      "Edit(.env*)",
      "Edit(/etc/**)",
      "WebFetch",
      "WebSearch"
    ]
  },
  "hooks": {
    "tool-call-hook": {
      "command": "/opt/company/claude-security-audit.sh"
    }
  },
  "mcpServers": {
    "company-gitlab": {
      "command": "/opt/company/mcp-gitlab",
      "env": {
        "GITLAB_URL": "https://gitlab.company.internal"
      }
    }
  }
}
```

### 2. 网络隔离

**仅允许内网访问**：

```json
{
  "permissions": {
    "allow": [
      "WebFetch(https://*.company.internal/*)",
      "WebFetch(https://gitlab.company.internal/*)"
    ],
    "deny": [
      "WebFetch(http://*)",
      "WebFetch(https://*)",
      "Bash(curl:*)",
      "Bash(wget:*)"
    ]
  }
}
```

### 3. 合规审计

```bash
#!/bin/bash
# compliance-audit.sh

echo "🔍 合规性审计..."

# 检查敏感命令使用
grep -E "(sudo|rm|curl|wget)" .claude/audit.log > suspicious-commands.txt

# 检查文件访问
grep -E "Read.*\.env|Read.*secret" .claude/audit.log > sensitive-access.txt

# 生成报告
cat > compliance-report.txt << EOF
# Claude Code 合规性审计报告

日期: $(date)

## 可疑命令
$(cat suspicious-commands.txt | wc -l) 条

## 敏感文件访问
$(cat sensitive-access.txt | wc -l) 条

详细日志见:
- suspicious-commands.txt
- sensitive-access.txt
EOF

echo "✅ 审计完成: compliance-report.txt"
```

---

## ✅ 安全检查清单

### 日常使用检查

- [ ] 已配置权限拒绝访问 `.env` 文件
- [ ] 已配置权限拒绝危险命令（`sudo`, `rm` 等）
- [ ] 已启用敏感信息检测 Hook
- [ ] 已添加 `.env` 到 `.gitignore`
- [ ] 使用环境变量而非硬编码

### 项目初始化检查

- [ ] 创建 `.claude/settings.json` 配置权限
- [ ] 配置 `.gitignore` 忽略敏感文件
- [ ] 设置安全检查 Hooks
- [ ] 创建 `.env.example` 示例文件
- [ ] 文档说明安全配置要求

### 代码提交前检查

- [ ] 运行 `git diff` 检查是否包含敏感信息
- [ ] 执行 `npm audit` 检查依赖漏洞
- [ ] 运行安全测试用例
- [ ] 代码审查安全问题
- [ ] 检查提交历史是否泄露密钥

### 团队协作检查

- [ ] 团队成员都配置了相同的安全策略
- [ ] PR 流程包含安全审查步骤
- [ ] 定期审计访问日志
- [ ] 密钥定期轮换
- [ ] 安全培训和意识提升

### 企业环境检查

- [ ] 部署企业级策略配置
- [ ] 启用网络隔离
- [ ] 配置审计日志
- [ ] 定期合规性检查
- [ ] 应急响应预案

---

## 🚨 应急响应

### 1. 密钥泄露处理

如果不小心提交了密钥到 git：

```bash
# 1. 立即撤销泄露的密钥
# 在服务提供商后台撤销旧密钥

# 2. 生成新密钥
NEW_KEY=$(openssl rand -hex 32)

# 3. 更新配置
echo "API_KEY=$NEW_KEY" > .env

# 4. 从 git 历史中删除（慎用！）
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# 5. 强制推送（警告：破坏性操作）
git push origin --force --all

# 6. 通知团队成员重新克隆仓库
```

### 2. 可疑活动检测

检查审计日志：

```bash
# 查看最近的文件访问
tail -100 .claude/audit.log | grep "Read"

# 查找敏感文件访问
grep -E "\.env|secret|credential" .claude/audit.log

# 查找危险命令
grep -E "sudo|rm|curl|wget" .claude/audit.log
```

### 3. 回滚操作

```bash
# 查看最近的提交
git log --oneline -10

# 回滚到安全的提交
git reset --hard <commit-hash>

# 或创建反向提交
git revert <commit-hash>
```

### 4. 事件报告模板

```markdown
# 安全事件报告

## 基本信息
- 事件时间: YYYY-MM-DD HH:MM:SS
- 发现人: 姓名
- 影响范围: [低/中/高]

## 事件描述
简要描述发生了什么

## 影响评估
- 受影响的系统/服务
- 泄露的数据/密钥
- 潜在风险

## 应对措施
- [ ] 已撤销受影响的凭据
- [ ] 已生成新凭据
- [ ] 已更新配置
- [ ] 已通知相关人员
- [ ] 已修复漏洞

## 预防措施
- 添加了哪些检查
- 更新了哪些配置
- 加强了哪些培训

## 总结和建议
经验教训和改进建议
```

---

## 📚 安全资源

### 推荐工具

| 工具 | 功能 | 链接 |
|------|------|------|
| **git-secrets** | 防止提交密钥到 git | https://github.com/awslabs/git-secrets |
| **TruffleHog** | 扫描 git 历史中的密钥 | https://github.com/trufflesecurity/trufflehog |
| **npm audit** | 检查 npm 依赖漏洞 | `npm audit` |
| **Snyk** | 依赖漏洞扫描 | https://snyk.io/ |
| **OWASP ZAP** | Web 应用安全测试 | https://www.zaproxy.org/ |

### 安全标准

- **OWASP Top 10**: https://owasp.org/www-project-top-ten/
- **CWE Top 25**: https://cwe.mitre.org/top25/
- **SANS Top 25**: https://www.sans.org/top25-software-errors/

### 学习资源

- [OWASP 安全编码实践](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Node.js 安全最佳实践](https://nodejs.org/en/docs/guides/security/)
- [GitHub 密钥扫描](https://docs.github.com/en/code-security/secret-scanning)

---

## 🔗 相关文档

- [基础使用手册](basic-guide.md) - 基础功能入门
- [进阶使用手册](advanced-guide.md) - 高级特性
- [最佳实践](best-practices.md) - 优化和技巧
- [权限配置指南](docs/configuration/permissions.md) - 权限详解

---

**最后更新**: 2025-11-27
**文档版本**: 1.0
**适用于**: Claude Code 所有版本

---

<div align="center">

**🔒 安全第一，预防为主**

</div>
