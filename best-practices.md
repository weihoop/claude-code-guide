# Claude Code 最佳实践

> 本文档提供 Claude Code 使用的最佳实践，包括 Token 优化、安全性、团队协作等

---

## 📋 目录

- [Token 使用优化](#token-使用优化)
- [提示词最佳实践](#提示词最佳实践)
- [项目组织结构](#项目组织结构)
- [安全性最佳实践](#安全性最佳实践)
- [团队协作规范](#团队协作规范)
- [性能优化技巧](#性能优化技巧)
- [调试和问题排查](#调试和问题排查)
- [常见陷阱和解决方案](#常见陷阱和解决方案)

---

## 💎 Token 使用优化

### 为什么要优化 Token？

- ⚠️ **成本控制**: Token 使用量直接影响 API 费用
- ⚡ **性能提升**: 减少 Token 可加快响应速度
- 📊 **上下文限制**: 避免超出模型上下文窗口

### Token 消耗来源

| 来源 | 占比 | 优化方式 |
|------|------|----------|
| 对话历史 | 30-40% | 定期清除、分段对话 |
| 文件内容 | 40-50% | 精确读取、避免大文件 |
| 系统提示词 | 10-15% | 优化配置 |
| 工具调用结果 | 5-10% | 过滤输出 |

### 优化策略

#### 1. 及时清除对话历史

```bash
# 完成一个任务后清除历史
/clear

# 或在对话中明确说明
> 前面的内容可以忘记了，现在开始新任务
```

**最佳实践**:
```
✅ 每完成一个独立任务就 /clear
✅ 切换项目或功能模块时清除
❌ 不要在一个会话中处理多个不相关任务
```

#### 2. 精确文件读取

**不好的做法** ❌:
```
> 帮我看看这个项目的所有文件
```

**好的做法** ✅:
```
> 只读取 src/api/user.js 文件
> 读取 src/api/user.js 的第 50-100 行
```

**使用 Grep 代替 Read**:
```
# 不好：读取整个文件找函数
> 读取 utils.js 找到 formatDate 函数

# 好：直接搜索
> 在 utils.js 中搜索 formatDate 函数的定义
```

#### 3. 使用更小的模型

```bash
# 简单任务：使用 Haiku (速度快、便宜)
/model haiku

# 示例：代码格式化、简单修复、文档生成
```

**模型选择指南**:

| 模型 | Token 成本 | 适用场景 | 速度 |
|------|-----------|----------|------|
| **Haiku** | $ | 代码格式化、简单修复、文档生成 | 最快 |
| **Sonnet** | $$ | 功能开发、代码审查、重构 | 中等 |
| **Opus** | $$$ | 复杂架构设计、难题调试 | 较慢 |

#### 4. 分解大任务

**不好的做法** ❌:
```
> 重构整个项目，优化性能，添加测试，更新文档
```

**好的做法** ✅:
```
# 任务 1
> 帮我重构 UserService 类

# 完成后 /clear

# 任务 2
> 为 UserService 编写单元测试

# 完成后 /clear

# 任务 3
> 更新 UserService 的文档
```

#### 5. 使用 Task 工具

对于独立的子任务，使用 Task 工具启动新的 Agent：

```
> 使用 Task 工具分析项目架构（这个子任务的上下文不会累积到主对话）
```

#### 6. 避免重复读取

Claude 会记住已读取的文件：

```
# 第一次读取
> 读取 api.js 文件

# 之后直接引用，不要再读
> 在 api.js 中添加错误处理（不需要再说"先读取文件"）
```

#### 7. 限制搜索范围

```
# 不好：全项目搜索
> 搜索所有文件中的 TODO

# 好：限制范围
> 只在 src/components 目录下搜索 TODO
```

#### 8. 使用配置文件减少重复说明

**不好的做法** ❌:
每次都说明项目结构和规范

**好的做法** ✅:
创建 `.claude.md`:

```markdown
# 项目说明

- 使用 React + TypeScript
- 测试框架：Jest
- 代码风格：Prettier + ESLint
- 所有组件放在 src/components/
- 测试文件命名：*.test.ts
```

Claude 会自动读取这个文件，不需要重复说明。

#### 9. 批量操作合并

**不好的做法** ❌:
```
> 修改 file1.js
> 修改 file2.js
> 修改 file3.js
```

**好的做法** ✅:
```
> 在以下文件中统一添加错误处理：
  - file1.js
  - file2.js
  - file3.js
```

#### 10. 使用 Glob 代替逐个列举

**不好的做法** ❌:
```
> 读取 src/utils/date.js
> 读取 src/utils/string.js
> 读取 src/utils/number.js
```

**好的做法** ✅:
```
> 读取 src/utils/*.js 所有工具函数
```

### Token 使用监控

```bash
# 查看当前对话的 token 使用
/context

# 显示类似：
# Current context:
# - Messages: 15
# - Tokens: ~8,500
# - Files read: 5
```

### Token 优化检查清单

使用前检查：

- [ ] 这个任务需要所有对话历史吗？→ 否则 `/clear`
- [ ] 需要读取整个文件吗？→ 否则指定行号或用 Grep
- [ ] 可以用更小的模型吗？→ 简单任务用 Haiku
- [ ] 可以分解成多个独立任务吗？→ 分段处理
- [ ] 有重复的操作可以合并吗？→ 批量处理

---

## 💬 提示词最佳实践

### 清晰明确的指令

**优秀提示词特征**:
- ✅ **具体**: 明确指出要修改什么、如何修改
- ✅ **完整**: 包含所有必要信息
- ✅ **结构化**: 分点列出要求
- ✅ **有上下文**: 说明技术栈和约束

**示例对比**:

❌ **不好的提示词**:
```
> 改一下登录功能
```

✅ **好的提示词**:
```
> 修改 src/auth/login.js 中的登录功能：
> 1. 添加邮箱格式验证
> 2. 密码至少 8 位，包含数字和字母
> 3. 登录失败 3 次后锁定账户 15 分钟
> 4. 使用 bcrypt 加密密码
> 5. 添加相应的单元测试
```

### 提供示例

当需要特定格式或风格时，提供示例：

```
> 为 User 类添加 toJSON 方法，参考 Product 类的实现方式
```

或：

```
> 生成 API 文档，格式如下：
>
> ## GET /api/users
>
> **描述**: 获取用户列表
>
> **参数**:
> - page: 页码（可选，默认 1）
> - limit: 每页数量（可选，默认 10）
>
> **响应**:
> ```json
> {
>   "users": [...],
>   "total": 100
> }
> ```
```

### 分步骤说明

对于复杂任务：

```
> 重构用户认证模块，按以下步骤：
>
> 第一步：分析现有代码结构
> 第二步：设计新的模块划分
> 第三步：等我确认后再实施
```

### 明确约束条件

```
> 添加数据导出功能，要求：
> - 支持 CSV 和 JSON 格式
> - 不要使用额外的依赖包
> - 导出文件大小不超过 10MB
> - 添加进度提示
```

### 指定技术栈

```
✅ 使用 React Hooks 和 TypeScript 创建一个用户表单组件
✅ 用 Express.js 和 PostgreSQL 实现 RESTful API
✅ 使用 Jest 和 React Testing Library 编写测试
```

---

## 📁 项目组织结构

### 推荐的项目结构

```
project/
├── .claude/
│   ├── settings.json           # 项目配置
│   ├── settings.local.json     # 个人配置（不提交）
│   ├── .claude.md              # 项目说明
│   ├── commands/               # 自定义命令
│   │   ├── deploy.md
│   │   └── test.md
│   ├── skills/                 # 自定义 Skill
│   │   └── code-reviewer/
│   └── hooks/                  # Hook 脚本
│       ├── format-code.sh
│       └── security-check.js
├── src/
├── tests/
├── docs/
├── .gitignore                  # 确保忽略 settings.local.json
└── README.md
```

### .claude.md 最佳实践

创建项目说明文件，减少重复解释：

```markdown
# 项目：电商管理系统

## 技术栈
- 前端：React 18 + TypeScript + Vite
- 后端：Node.js + Express + PostgreSQL
- 测试：Jest + React Testing Library

## 代码规范
- 使用 Prettier 格式化（配置见 .prettierrc）
- ESLint 检查（配置见 .eslintrc.js）
- 提交前必须通过 lint 和 test

## 项目结构
- `/src/components` - React 组件
- `/src/api` - API 调用
- `/src/utils` - 工具函数
- `/src/types` - TypeScript 类型定义

## 注意事项
- 所有 API 调用必须有错误处理
- 组件必须有 PropTypes 或 TypeScript 类型
- 新功能必须包含单元测试
- 敏感配置使用环境变量（.env）

## 常用命令
```bash
npm run dev       # 开发服务器
npm run test      # 运行测试
npm run lint      # 代码检查
npm run build     # 生产构建
```
```

### .gitignore 配置

确保不提交敏感配置：

```gitignore
# Claude Code 本地配置
.claude/settings.local.json
.claude.md.local

# 环境变量
.env
.env.local
.env.*.local

# 日志
.claude/logs/
```

---

## 🔒 安全性最佳实践

### 1. 保护敏感信息

**配置权限拒绝访问**:

```json
{
  "permissions": {
    "deny": [
      "Read(.env*)",
      "Read(**/.env*)",
      "Read(**/secrets/**)",
      "Read(**/*credential*)",
      "Read(**/*password*)",
      "Read(**/*key*)",
      "Read(**/*token*)",
      "Edit(.env*)",
      "Edit(**/secrets/**)"
    ]
  }
}
```

### 2. 危险命令控制

```json
{
  "permissions": {
    "deny": [
      "Bash(sudo:*)",
      "Bash(rm:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(chmod:*)",
      "Bash(chown:*)"
    ],
    "ask": [
      "Bash(git push:*)",
      "Bash(npm publish:*)",
      "Bash(docker:*)"
    ]
  }
}
```

### 3. 使用环境变量

**不好的做法** ❌:

```javascript
// config.js
const API_KEY = 'sk-1234567890abcdef';  // ❌ 硬编码
```

**好的做法** ✅:

```javascript
// config.js
const API_KEY = process.env.API_KEY;  // ✅ 使用环境变量

// .env (不提交到 git)
API_KEY=sk-1234567890abcdef
```

### 4. Code Review Hook

创建安全检查 Hook：

```javascript
// .claude/hooks/security-check.js
const SENSITIVE_PATTERNS = [
  /password\s*=\s*["'][^"']+["']/i,
  /api[_-]?key\s*=\s*["'][^"']+["']/i,
  /secret\s*=\s*["'][^"']+["']/i,
  /token\s*=\s*["'][^"']+["']/i
];

const content = process.env.TOOL_ARGS_content || '';

for (const pattern of SENSITIVE_PATTERNS) {
  if (pattern.test(content)) {
    console.error('🚨 检测到硬编码的敏感信息！请使用环境变量。');
    process.exit(1);
  }
}

process.exit(0);
```

配置：

```json
{
  "hooks": {
    "tool-call-hook": {
      "command": "node",
      "args": [".claude/hooks/security-check.js"]
    }
  }
}
```

### 5. 代码审查清单

提示 Claude 进行安全审查：

```
> 审查 src/auth.js 的安全性，重点检查：
> 1. SQL 注入风险
> 2. XSS 漏洞
> 3. 认证绕过
> 4. 敏感信息泄露
> 5. CSRF 保护
```

---

## 👥 团队协作规范

### 1. 统一配置管理

**团队共享配置** (`.claude/settings.json`):

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run test:*)",
      "Bash(npm run lint:*)",
      "Edit(/src/**)",
      "Edit(/tests/**)"
    ],
    "ask": [
      "Bash(git push:*)",
      "Bash(npm publish:*)"
    ],
    "deny": [
      "Bash(rm:*)",
      "Edit(/node_modules/**)",
      "Edit(/package-lock.json)"
    ]
  },
  "hooks": {
    "pre-commit-hook": {
      "command": "bash",
      "args": ["-c", "npm run lint && npm run test"]
    }
  }
}
```

**个人配置** (`.claude/settings.local.json`，不提交):

```json
{
  "model": "haiku",  // 个人偏好使用更快的模型
  "permissions": {
    "allow": ["Bash(docker:*)"]  // 个人开发环境允许 Docker
  }
}
```

### 2. 代码规范一致性

**创建团队 Skill** (`.claude/skills/team-standards/prompt.md`):

```markdown
# 团队代码规范

## 代码风格
- 使用 Prettier 格式化
- 遵循 Airbnb JavaScript Style Guide
- 变量命名使用 camelCase
- 常量使用 UPPER_SNAKE_CASE

## 提交规范
- 提交信息格式：`类型: 简短描述`
- 类型：feat, fix, docs, style, refactor, test, chore

## 测试要求
- 新功能必须包含单元测试
- 测试覆盖率不低于 80%
- 使用 Jest + React Testing Library

## 文档要求
- 所有公共 API 必须有 JSDoc 注释
- 复杂逻辑必须有行内注释
- README 必须包含使用示例
```

### 3. PR 流程规范

**自定义 PR 命令** (`.claude/commands/pr.md`):

```markdown
---
name: pr
description: 创建 Pull Request
---

# 创建 Pull Request

执行以下步骤：

1. **检查改动**
   ```bash
   git status
   git diff
   ```

2. **运行测试**
   ```bash
   npm run test
   npm run lint
   ```

3. **创建提交**
   - 按照团队规范编写提交信息
   - 格式：`类型: 简短描述`

4. **推送分支**
   ```bash
   git push origin feature/xxx
   ```

5. **生成 PR 描述**
   包含：
   - 改动说明
   - 测试情况
   - 截图（如有 UI 改动）
   - 相关 Issue 链接

6. **创建 PR**
   使用 gh CLI 或手动创建
```

使用：

```bash
/pr
```

### 4. 文档同步

**自动更新文档** (`.claude/commands/update-docs.md`):

```markdown
---
name: update-docs
description: 更新项目文档
---

# 更新文档

检查并更新以下文档：

1. **README.md**
   - 功能列表是否最新
   - 安装步骤是否正确
   - 使用示例是否有效

2. **CHANGELOG.md**
   - 添加本次更新内容
   - 格式：`## [版本] - 日期`

3. **API 文档**
   - 检查 API 接口文档
   - 更新参数说明
   - 添加示例代码

4. **.claude.md**
   - 更新技术栈信息
   - 更新项目结构
   - 更新开发规范
```

---

## ⚡ 性能优化技巧

### 1. 选择合适的工具

| 任务 | 推荐工具 | 原因 |
|------|---------|------|
| 查找文件 | `Glob` | 比 `Read` 每个文件快 |
| 搜索代码 | `Grep` | 比 `Read` + 分析快 |
| 简单修改 | `Edit` | 比 `Read` + `Write` 快 |
| 命令执行 | `Bash` | 直接执行，无需额外解析 |

### 2. 缓存常用信息

创建项目缓存文件：

```markdown
<!-- .claude/cache.md -->

# 项目缓存信息

## 常用路径
- 组件：`src/components/`
- API：`src/api/`
- 测试：`tests/`

## 常用命令
- 测试：`npm test`
- 构建：`npm run build`
- 开发：`npm run dev`

## 关键文件
- 配置：`config/app.config.js`
- 路由：`src/routes.js`
- 状态管理：`src/store/index.js`
```

### 3. 并行处理

当任务可以并行时，一次性提出：

```
> 同时执行以下任务：
> 1. 读取 src/api.js
> 2. 读取 src/auth.js
> 3. 运行测试
```

Claude 会并行处理这些工具调用。

---

## 🐛 调试和问题排查

### 1. 查看详细日志

```bash
# 启用详细日志
claude --verbose

# 查看日志文件
tail -f ~/.claude/logs/claude-code.log
```

### 2. 检查权限配置

```bash
# 查看当前权限
/permissions

# 查看被拒绝的操作
grep "denied" ~/.claude/logs/claude-code.log
```

### 3. 验证配置文件

```bash
# 检查 JSON 语法
cat ~/.claude/settings.json | jq .

# 如果报错，说明 JSON 格式有问题
```

### 4. 隔离问题

```bash
# 使用最小配置启动
claude --no-config

# 或创建测试配置
cp ~/.claude/settings.json ~/.claude/settings.json.bak
echo '{}' > ~/.claude/settings.json
claude
```

### 5. 常见问题排查

| 问题 | 排查步骤 |
|------|---------|
| 工具调用失败 | 检查权限配置 → 查看日志 → 验证工具参数 |
| Token 消耗快 | 检查对话历史 → 检查已读文件 → 使用 `/context` |
| 响应慢 | 切换到更小模型 → 减少上下文 → 检查网络 |
| 读取文件失败 | 检查文件路径 → 检查权限 → 检查文件是否存在 |

---

## ⚠️ 常见陷阱和解决方案

### 陷阱 1: 过度依赖历史上下文

**问题**:
```
对话历史太长，导致 token 消耗快、响应慢
```

**解决方案**:
```bash
# 养成定期清除的习惯
完成任务后 → /clear

# 或明确告知
> 前面的内容可以忘记，现在开始新任务
```

### 陷阱 2: 读取不必要的大文件

**问题**:
```
> 分析这个项目

Claude 读取了所有文件，包括 node_modules、dist 等
```

**解决方案**:
```
# 1. 配置权限
{
  "permissions": {
    "deny": [
      "Read(/node_modules/**)",
      "Read(/dist/**)",
      "Read(/build/**)"
    ]
  }
}

# 2. 明确指定范围
> 只分析 src/ 目录下的代码
```

### 陷阱 3: 没有验证就执行

**问题**:
```
Claude 直接修改了重要文件，结果不符合预期
```

**解决方案**:
```
# 1. 配置权限需要确认
{
  "permissions": {
    "ask": ["Edit", "Write", "Bash"]
  }
}

# 2. 要求先展示
> 先别修改，展示给我看看你打算怎么改
```

### 陷阱 4: 混用不同语言/框架的知识

**问题**:
```
Claude 用了 Vue 的语法修改 React 项目
```

**解决方案**:
```
# 在 .claude.md 中明确说明
## 技术栈
- 前端：React 18 + TypeScript（不使用 Vue）
```

### 陷阱 5: 忽略错误

**问题**:
```
命令执行失败，但继续后续操作
```

**解决方案**:
```
# 明确要求错误处理
> 执行测试，如果失败，停止并报告错误
```

### 陷阱 6: 没有备份就重构

**问题**:
```
大规模重构后发现问题，无法回退
```

**解决方案**:
```
# 1. 使用 git
> 先创建一个 git 分支再开始重构

# 2. 分步骤
> 先重构一个模块，测试通过后再继续
```

---

## 📊 效果对比

### Token 使用对比

| 场景 | 不优化 | 优化后 | 节省 |
|------|--------|--------|------|
| 代码审查 | 15K tokens | 5K tokens | 67% |
| 功能开发 | 30K tokens | 12K tokens | 60% |
| Bug 修复 | 8K tokens | 3K tokens | 63% |
| 文档生成 | 12K tokens | 4K tokens | 67% |

### 性能对比

| 场景 | 不优化 | 优化后 |
|------|--------|--------|
| 响应时间 | 15-20s | 5-8s |
| 文件读取 | 读取整个文件 | 只读取相关部分 |
| 模型使用 | 始终用 Sonnet | 简单任务用 Haiku |

---

## ✅ 最佳实践检查清单

### 每日使用检查

- [ ] 完成任务后是否 `/clear`
- [ ] 是否使用了合适的模型
- [ ] 是否只读取必要的文件
- [ ] 是否明确了技术栈和要求
- [ ] 是否验证了重要修改

### 项目配置检查

- [ ] 是否创建了 `.claude.md`
- [ ] 是否配置了合理的权限
- [ ] 是否设置了安全性检查
- [ ] 是否忽略了敏感配置文件
- [ ] 是否创建了团队规范 Skill

### 团队协作检查

- [ ] 团队配置是否提交到 git
- [ ] 个人配置是否添加到 .gitignore
- [ ] 是否统一了代码规范
- [ ] 是否建立了 PR 流程
- [ ] 是否定期同步文档

---

## 📚 相关资源

- [基础使用手册](basic-guide.md) - 基础功能入门
- [进阶使用手册](advanced-guide.md) - Skill、MCP、Hooks 等
- [权限配置指南](docs/configuration/permissions.md) - 权限详解
- [官方资源](docs/resources/official-resources.md) - 官方文档

---

**最后更新**: 2025-11-27
**文档版本**: 1.0
**适用于**: Claude Code 所有版本
