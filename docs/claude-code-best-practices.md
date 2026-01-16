# Claude Code 编程最佳实践与范式

完整的 Claude Code 开发流程、文件组织和配置规范。

---

## 📋 最佳实践总览表

| 实践类型 | 文件/配置 | 优先级 | 用途 | 推荐内容 |
|---------|----------|--------|------|----------|
| **项目配置** | `.claude.md` | ⭐⭐⭐⭐⭐ | 项目上下文、架构说明 | 技术栈、项目结构、常用命令、开发规范 |
| **权限控制** | `.claude/settings.json` | ⭐⭐⭐⭐⭐ | 团队共享权限配置 | 文件操作权限、命令白名单、安全策略 |
| **个人配置** | `.claude/settings.local.json` | ⭐⭐⭐⭐ | 个人权限覆盖 | 本地开发特殊权限（不提交到 Git） |
| **自定义命令** | `.claude/commands/*.md` | ⭐⭐⭐⭐ | 项目专属工作流 | /test, /deploy, /review, /build 等 |
| **规范文档** | `SPEC.md` / `docs/spec/` | ⭐⭐⭐⭐ | 功能规格说明 | API 设计、数据结构、业务逻辑规范 |
| **测试规范** | `tests/` + 测试命令 | ⭐⭐⭐⭐⭐ | 自动化测试 | 单元测试、集成测试、E2E 测试 |
| **变更日志** | `CHANGELOG.md` | ⭐⭐⭐⭐ | 版本变更追踪 | 按语义化版本记录所有变更 |
| **开发文档** | `CONTRIBUTING.md` | ⭐⭐⭐ | 贡献者指南 | 开发流程、提交规范、审查标准 |
| **代码规范** | `.editorconfig` + linter | ⭐⭐⭐⭐ | 代码风格统一 | ESLint/Black/Prettier 配置 |
| **Git 规范** | `.gitignore` + hooks | ⭐⭐⭐⭐⭐ | 版本控制 | 忽略规则、提交钩子、分支策略 |
| **依赖管理** | `package.json` / `requirements.txt` | ⭐⭐⭐⭐⭐ | 依赖声明 | 精确版本锁定、定期更新 |
| **CI/CD 配置** | `.github/workflows/` | ⭐⭐⭐⭐ | 自动化流程 | 测试、构建、部署自动化 |
| **文档生成** | `docs/` | ⭐⭐⭐ | API 和使用文档 | 自动生成 + 手写教程 |
| **环境配置** | `.env.example` | ⭐⭐⭐⭐ | 环境变量模板 | 配置项说明（不含真实值） |
| **MCP 配置** | `.claude/.mcp.json` | ⭐⭐⭐ | 外部工具集成 | GitHub、数据库等服务集成 |
| **Hooks 配置** | `.claude/hooks.json` | ⭐⭐⭐ | 执行钩子 | 工具调用前后的自动化操作 |

---

## 🎯 详细配置指南

### 1. 项目配置文件：`.claude.md`

**位置**：项目根目录（隐藏文件）

**推荐模板**：

```markdown
# 项目名称

## 项目概述
- **类型**：Web应用 / API服务 / CLI工具 / 库
- **技术栈**：Next.js 15, TypeScript, PostgreSQL, Redis
- **用途**：用户管理系统
- **仓库**：https://github.com/org/repo

## 项目结构
\```
src/
├── app/          # Next.js App Router
├── components/   # React 组件
├── lib/          # 工具函数和库
├── hooks/        # 自定义 Hooks
└── types/        # TypeScript 类型定义
\```

## 核心架构

### 数据库设计
- **主库**：PostgreSQL 15（用户数据、事务数据）
- **缓存**：Redis 7（会话、热点数据）
- **ORM**：Prisma 5.x

### API 设计
- **风格**：RESTful API
- **认证**：JWT + httpOnly Cookie
- **版本**：/api/v1/

### 关键设计决策
1. 使用 Server Components 优化性能
2. 采用乐观更新提升用户体验
3. 实现增量静态生成（ISR）

## 常用命令

### 开发
\```bash
npm run dev          # 启动开发服务器（localhost:3000）
npm run dev:debug    # 调试模式启动
npm run db:studio    # Prisma Studio 数据库管理
\```

### 测试
\```bash
npm test             # 运行所有测试
npm run test:watch   # 监听模式
npm run test:e2e     # E2E 测试
npm run test:coverage # 覆盖率报告
\```

### 构建和部署
\```bash
npm run build        # 生产构建
npm run start        # 生产模式启动
npm run lint         # 代码检查
npm run type-check   # TypeScript 类型检查
\```

### 数据库
\```bash
npx prisma migrate dev    # 创建并应用迁移
npx prisma db push        # 推送 schema 到数据库（开发用）
npx prisma generate       # 生成 Prisma Client
npx prisma db seed        # 填充测试数据
\```

## 开发规范

### 代码风格
- **TypeScript**：严格模式，所有函数必须有类型注解
- **命名**：camelCase（变量/函数），PascalCase（组件/类型）
- **组件**：函数组件 + Hooks，避免类组件
- **注释**：中文注释，复杂逻辑必须说明

### 文件组织
- 每个组件一个文件夹（包含组件、样式、测试）
- 工具函数按功能分模块
- 类型定义集中在 `types/` 目录

### Git 提交规范
\```
feat: 添加用户认证功能
fix: 修复登录状态丢失问题
docs: 更新 API 文档
test: 添加用户服务测试
refactor: 重构数据库查询逻辑
\```

### 测试要求
- **单元测试覆盖率** ≥ 80%
- **关键路径必须有 E2E 测试**
- **所有 API 端点必须有集成测试**
- **测试文件**：`*.test.ts` 或 `*.spec.ts`

### 安全规范
- **环境变量**：使用 `.env.local`，不提交敏感信息
- **API 密钥**：通过环境变量注入，不硬编码
- **输入验证**：所有用户输入必须验证和清洗
- **SQL 注入**：使用 Prisma ORM，避免原始 SQL

## 关键文件说明

### 配置文件
- `next.config.js` - Next.js 配置
- `tsconfig.json` - TypeScript 配置
- `prisma/schema.prisma` - 数据库 Schema
- `.env.example` - 环境变量模板

### 文档
- `README.md` - 项目说明
- `SPEC.md` - 功能规格
- `CHANGELOG.md` - 变更日志
- `docs/API.md` - API 文档

## 外部依赖

### 关键依赖
- `next@15.x` - 前端框架
- `@prisma/client@5.x` - 数据库 ORM
- `zod@3.x` - 数据验证
- `jose@5.x` - JWT 处理

### 开发依赖
- `typescript@5.x`
- `@types/node`
- `eslint` + `prettier`
- `jest` + `@testing-library/react`

## 故障排查

### 常见问题
1. **数据库连接失败**：检查 `DATABASE_URL` 环境变量
2. **类型错误**：运行 `npx prisma generate` 重新生成类型
3. **端口占用**：修改 `.env` 中的 `PORT` 变量
4. **构建失败**：清理缓存 `rm -rf .next && npm run build`

### 调试技巧
- 使用 `console.log` 或 VS Code 断点
- 检查 Network 面板（浏览器开发者工具）
- 查看服务器日志输出
- 使用 Prisma Studio 检查数据库

## 团队协作

### 分支策略
- `main` - 生产分支（保护分支）
- `develop` - 开发分支
- `feature/*` - 功能分支
- `fix/*` - 修复分支

### PR 流程
1. 从 `develop` 创建功能分支
2. 完成开发并通过所有测试
3. 提交 PR，填写模板
4. 通过代码审查
5. 合并到 `develop`

### 代码审查要点
- [ ] 代码符合规范
- [ ] 测试覆盖充分
- [ ] 无安全隐患
- [ ] 文档已更新
- [ ] 性能无明显下降
\```

**GitIgnore 配置**：
```gitignore
# 不提交 .claude.md 到版本控制（个人偏好）
# 或者提交以供团队共享（推荐）
```

---

### 2. 权限配置：`.claude/settings.json`

**位置**：`.claude/settings.json`（提交到 Git）

**推荐配置**：

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Edit(/src/**)",
      "Edit(/tests/**)",
      "Edit(/docs/**)",
      "Write(/tests/**)",
      "Glob",
      "Grep",
      "Bash(npm run dev:*)",
      "Bash(npm run test:*)",
      "Bash(npm run build:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "WebSearch"
    ],
    "ask": [
      "Edit(/package.json)",
      "Edit(/tsconfig.json)",
      "Edit(/.env*)",
      "Write(/src/**)",
      "Bash(git push:*)",
      "Bash(npm install:*)",
      "Bash(npx prisma migrate:*)",
      "Bash(npm publish:*)"
    ],
    "deny": [
      "Read(.env)",
      "Read(.env.local)",
      "Read(**/secrets/**)",
      "Edit(/node_modules/**)",
      "Write(/node_modules/**)",
      "Bash(rm -rf:*)",
      "Bash(sudo:*)",
      "Bash(docker rm:*)",
      "Bash(npm publish:*)",
      "Bash(git push --force:*)"
    ]
  }
}
```

**配置说明**：
- **allow**：日常开发常用操作
- **ask**：需要确认的重要操作
- **deny**：禁止的危险操作

---

### 3. 个人配置：`.claude/settings.local.json`

**位置**：`.claude/settings.local.json`（**不提交**到 Git）

**推荐配置**：

```json
{
  "permissions": {
    "allow": [
      "Read(.env.local)",
      "Edit(.env.local)",
      "Bash(docker:*)",
      "Bash(npm run dev:local:*)"
    ]
  }
}
```

**GitIgnore**：
```gitignore
# .gitignore
.claude/settings.local.json
```

---

### 4. 自定义命令：`.claude/commands/`

#### 必备命令列表

| 命令文件 | 命令名 | 用途 | 优先级 |
|---------|--------|------|--------|
| `test.md` | `/test` | 运行测试并分析结果 | ⭐⭐⭐⭐⭐ |
| `build.md` | `/build` | 构建项目并检查错误 | ⭐⭐⭐⭐⭐ |
| `review.md` | `/review` | 代码审查流程 | ⭐⭐⭐⭐⭐ |
| `push.md` | `/push` | 快速提交推送 | ⭐⭐⭐⭐ |
| `deploy.md` | `/deploy` | 部署到指定环境 | ⭐⭐⭐⭐ |
| `fix.md` | `/fix` | 自动修复代码问题 | ⭐⭐⭐⭐ |
| `doc.md` | `/doc` | 更新文档 | ⭐⭐⭐ |
| `update.md` | `/update` | 更新依赖 | ⭐⭐⭐ |
| `spec.md` | `/spec` | 生成功能规格 | ⭐⭐⭐ |
| `changelog.md` | `/changelog` | 生成变更日志 | ⭐⭐⭐ |

#### 示例：`/test` 命令

**文件**：`.claude/commands/test.md`

```markdown
---
name: test
description: 运行测试并智能分析结果
aliases: [t, run-test]
---

# 智能测试执行

## 执行步骤

1. **检测测试框架**
   - 检查 package.json 的 test 脚本
   - 识别 Jest/Vitest/Mocha 等

2. **运行测试**
   \```bash
   npm test
   \```

3. **分析结果**
   - 如果全部通过：显示统计信息
   - 如果有失败：
     - 读取失败的测试文件
     - 读取被测代码
     - 分析失败原因
     - 提供修复建议

4. **生成报告**
   - 测试覆盖率
   - 失败详情
   - 改进建议
```

#### 示例：`/changelog` 命令

**文件**：`.claude/commands/changelog.md`

```markdown
---
name: changelog
description: 生成或更新 CHANGELOG.md
aliases: [log, changes]
---

# 变更日志生成

## 执行步骤

1. **读取 Git 提交历史**
   \```bash
   git log --oneline --since="$(git describe --tags --abbrev=0)"
   # 或从上次发布以来的所有提交
   \```

2. **分析提交信息**
   - 按类型分组：feat, fix, docs, etc.
   - 提取版本号（如果有标签）
   - 识别破坏性变更（BREAKING CHANGE）

3. **生成变更条目**
   按照格式：
   \```markdown
   ## [版本号] - 日期

   ### 新增
   - feat: 添加的功能

   ### 修复
   - fix: 修复的问题

   ### 文档
   - docs: 文档更新

   ### 破坏性变更
   - BREAKING: 不兼容的变更
   \```

4. **更新 CHANGELOG.md**
   - 在文件顶部插入新版本
   - 保持格式一致
   - 添加日期和版本号

5. **询问用户确认**
   - 显示生成的内容
   - 确认是否写入文件
```

---

### 5. 规范文档：`SPEC.md`

**位置**：项目根目录或 `docs/spec/`

**推荐结构**：

```markdown
# 功能规格说明书

## 项目信息
- **项目名称**：用户管理系统
- **版本**：v2.0.0
- **最后更新**：2025-01-10
- **负责人**：@username

---

## 功能需求

### 1. 用户认证

#### 1.1 用户注册
- **功能描述**：允许新用户创建账号
- **输入**：
  - 邮箱（必填，格式验证）
  - 密码（必填，8-32字符，包含大小写字母和数字）
  - 用户名（可选，3-20字符）
- **输出**：
  - 成功：返回用户 ID 和 JWT Token
  - 失败：返回错误码和消息
- **验证规则**：
  - 邮箱唯一性检查
  - 密码强度验证
  - 频率限制：每 IP 每分钟最多 3 次
- **测试用例**：
  - [ ] 正常注册流程
  - [ ] 重复邮箱注册
  - [ ] 弱密码被拒绝
  - [ ] 恶意频繁注册被限制

#### 1.2 用户登录
...

---

## 数据模型

### User 表
\```typescript
interface User {
  id: string;           // UUID
  email: string;        // 唯一索引
  passwordHash: string; // bcrypt 哈希
  username?: string;    // 可选
  role: 'user' | 'admin';
  createdAt: Date;
  updatedAt: Date;
}
\```

### Session 表
\```typescript
interface Session {
  id: string;
  userId: string;      // 外键 -> User.id
  token: string;       // JWT
  expiresAt: Date;
  createdAt: Date;
}
\```

---

## API 设计

### POST /api/v1/auth/register

**请求**：
\```json
{
  "email": "user@example.com",
  "password": "SecurePass123",
  "username": "johndoe"
}
\```

**响应（成功）**：
\```json
{
  "success": true,
  "data": {
    "userId": "uuid-here",
    "token": "jwt-token-here"
  }
}
\```

**响应（失败）**：
\```json
{
  "success": false,
  "error": {
    "code": "EMAIL_EXISTS",
    "message": "该邮箱已被注册"
  }
}
\```

---

## 技术实现

### 认证流程
1. 用户提交注册表单
2. 后端验证输入数据
3. 检查邮箱唯一性
4. 密码加密（bcrypt, cost=10）
5. 创建用户记录
6. 生成 JWT Token（有效期 7 天）
7. 返回用户 ID 和 Token

### 安全措施
- 密码哈希：bcrypt
- JWT 签名：HS256
- Token 存储：httpOnly Cookie
- CSRF 保护：SameSite=Strict
- 速率限制：Redis + sliding window

---

## 测试计划

### 单元测试
- [ ] 密码验证逻辑
- [ ] 邮箱格式验证
- [ ] Token 生成和验证

### 集成测试
- [ ] 注册 API 端到端流程
- [ ] 登录 API 端到端流程
- [ ] 认证中间件

### E2E 测试
- [ ] 用户完整注册登录流程
- [ ] 错误处理和用户反馈

---

## 部署要求

### 环境变量
\```bash
DATABASE_URL=postgresql://...
JWT_SECRET=your-secret-key
REDIS_URL=redis://...
\```

### 性能指标
- 注册请求响应时间：< 500ms
- 登录请求响应时间：< 200ms
- 并发支持：1000 req/s

### 监控
- 注册成功率
- 登录失败率
- API 响应时间
- 数据库查询性能
```

---

### 6. 测试规范

#### 测试目录结构

```
tests/
├── unit/              # 单元测试
│   ├── utils.test.ts
│   └── services.test.ts
├── integration/       # 集成测试
│   ├── api.test.ts
│   └── db.test.ts
├── e2e/              # 端到端测试
│   ├── auth.spec.ts
│   └── user.spec.ts
├── fixtures/         # 测试数据
│   └── users.json
└── setup.ts          # 测试配置
```

#### 测试命令配置

**package.json**：
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:unit": "jest tests/unit",
    "test:integration": "jest tests/integration",
    "test:e2e": "playwright test",
    "test:coverage": "jest --coverage",
    "test:ci": "jest --ci --coverage --maxWorkers=2"
  }
}
```

#### Jest 配置

**jest.config.js**：
```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/tests'],
  testMatch: ['**/*.test.ts', '**/*.spec.ts'],
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/*.spec.ts',
  ],
  coverageThresholds: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
};
```

---

### 7. 变更日志：`CHANGELOG.md`

**位置**：项目根目录

**推荐格式**（遵循 Keep a Changelog）：

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- 用户头像上传功能

### Changed
- 优化数据库查询性能

### Fixed
- 修复登录状态丢失问题

---

## [2.0.0] - 2025-01-10

### Added
- 全新的用户认证系统
- JWT Token 支持
- Redis 会话管理
- 邮箱验证功能

### Changed
- 迁移到 PostgreSQL 15
- 升级 Next.js 到 15.x
- 重构 API 路由结构

### Deprecated
- 旧的 Session Cookie 认证（将在 3.0.0 移除）

### Removed
- 移除不再使用的 MongoDB 依赖

### Fixed
- 修复密码重置链接过期问题
- 修复并发注册导致的邮箱重复

### Security
- 增强密码哈希强度（bcrypt cost 12）
- 添加 CSRF 保护
- 实施速率限制

---

## [1.5.0] - 2024-12-15

### Added
- 用户角色管理
- 管理员后台

### Fixed
- 修复邮件发送失败问题

---

## [1.0.0] - 2024-10-01

### Added
- 初始版本发布
- 基础用户注册登录功能
- RESTful API

[Unreleased]: https://github.com/org/repo/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/org/repo/compare/v1.5.0...v2.0.0
[1.5.0]: https://github.com/org/repo/compare/v1.0.0...v1.5.0
[1.0.0]: https://github.com/org/repo/releases/tag/v1.0.0
```

**自动化生成**：
- 使用 `/changelog` 命令
- 或使用工具：`conventional-changelog`

---

### 8. 贡献指南：`CONTRIBUTING.md`

```markdown
# 贡献指南

感谢你对本项目的关注！

## 开发流程

### 1. Fork 并克隆仓库
\```bash
git clone https://github.com/YOUR_USERNAME/repo.git
cd repo
npm install
\```

### 2. 创建功能分支
\```bash
git checkout -b feature/your-feature-name
\```

### 3. 开发和测试
\```bash
npm run dev        # 启动开发服务器
npm test           # 运行测试
npm run lint       # 代码检查
\```

### 4. 提交代码
遵循提交规范：
\```bash
git commit -m "feat: 添加用户认证功能"
\```

提交类型：
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建/工具变更

### 5. 推送并创建 PR
\```bash
git push origin feature/your-feature-name
\```

## 代码规范

### TypeScript
- 使用严格模式
- 所有函数必须有类型注解
- 避免使用 `any`

### 测试
- 新功能必须有单元测试
- 覆盖率不低于 80%
- 测试文件命名：`*.test.ts`

### 文档
- 更新 README.md（如需要）
- 更新 API 文档
- 添加代码注释

## PR 审查标准

- [ ] 代码符合规范
- [ ] 所有测试通过
- [ ] 测试覆盖率达标
- [ ] 文档已更新
- [ ] 无 lint 错误
- [ ] 提交信息规范

## 获取帮助

- 提 Issue：https://github.com/org/repo/issues
- 讨论区：https://github.com/org/repo/discussions
```

---

### 9. 代码规范配置

#### ESLint 配置

**.eslintrc.json**：
```json
{
  "extends": [
    "next/core-web-vitals",
    "plugin:@typescript-eslint/recommended",
    "prettier"
  ],
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/no-explicit-any": "error",
    "no-console": ["warn", { "allow": ["warn", "error"] }]
  }
}
```

#### Prettier 配置

**.prettierrc**：
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2
}
```

#### EditorConfig

**.editorconfig**：
```ini
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false
```

---

### 10. CI/CD 配置

**`.github/workflows/ci.yml`**：

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x, 20.x]

    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

      - name: Run type check
        run: npm run type-check

      - name: Run tests
        run: npm run test:ci

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info

      - name: Build
        run: npm run build

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run security audit
        run: npm audit --audit-level=moderate
```

---

## 📁 完整项目文件清单

### 必备文件（⭐⭐⭐⭐⭐）

```
项目根目录/
├── .claude.md                      # 项目配置（Claude Code）
├── .claude/
│   ├── settings.json               # 团队权限配置
│   ├── settings.local.json         # 个人权限（不提交）
│   └── commands/                   # 自定义命令
│       ├── test.md
│       ├── build.md
│       ├── review.md
│       ├── push.md
│       └── changelog.md
├── README.md                       # 项目说明
├── CHANGELOG.md                    # 变更日志
├── package.json                    # 依赖管理
├── tsconfig.json                   # TypeScript 配置
├── .gitignore                      # Git 忽略规则
└── .env.example                    # 环境变量模板
```

### 推荐文件（⭐⭐⭐⭐）

```
├── SPEC.md                         # 功能规格
├── CONTRIBUTING.md                 # 贡献指南
├── .eslintrc.json                  # ESLint 配置
├── .prettierrc                     # Prettier 配置
├── .editorconfig                   # 编辑器配置
├── jest.config.js                  # Jest 配置
└── .github/
    └── workflows/
        └── ci.yml                  # CI/CD 配置
```

### 可选文件（⭐⭐⭐）

```
├── docs/                           # 文档目录
│   ├── API.md                      # API 文档
│   ├── ARCHITECTURE.md             # 架构说明
│   └── spec/                       # 详细规格
├── .claude/
│   ├── .mcp.json                   # MCP 配置
│   └── hooks.json                  # Hooks 配置
└── LICENSE                         # 开源协议
```

---

## 🚀 使用 Claude Code 的最佳工作流

### 1. 项目初始化

```bash
# 1. 创建项目
mkdir my-project && cd my-project
npm init -y

# 2. 启动 Claude Code
claude

# 3. 让 Claude 初始化项目
> /init
> 帮我创建一个 Next.js + TypeScript 项目的完整配置

# 4. Claude 会自动创建：
# - .claude.md
# - .claude/settings.json
# - .claude/commands/*.md
# - README.md, SPEC.md, etc.
```

### 2. 开发新功能

```bash
> 我要开发用户认证功能，包括注册和登录

# Claude 会：
1. 读取 SPEC.md 了解需求
2. 设计数据模型和 API
3. 实现代码
4. 编写测试
5. 更新文档
```

### 3. 代码审查

```bash
> /review src/auth/login.ts

# Claude 会：
1. 分析代码质量
2. 检查安全问题
3. 验证测试覆盖
4. 提供改进建议
```

### 4. 测试和构建

```bash
> /test
> /build

# Claude 会：
1. 运行测试
2. 分析失败原因
3. 提供修复建议
4. 生成报告
```

### 5. 发布版本

```bash
> /changelog
> 帮我生成 v2.0.0 的变更日志

# Claude 会：
1. 分析 Git 提交
2. 分类整理变更
3. 更新 CHANGELOG.md
4. 建议版本号
```

### 6. 提交代码

```bash
> /push

# Claude 会：
1. git add -A
2. 生成提交信息
3. git commit
4. git push
```

---

## 💡 最佳实践总结

### ✅ 推荐做法

1. **项目初始化时立即创建 `.claude.md`**
2. **使用自定义命令标准化工作流**
3. **保持 SPEC.md 和代码同步**
4. **每次发布前更新 CHANGELOG.md**
5. **配置严格的权限控制**
6. **编写完整的测试**
7. **提交代码前运行 `/review`**
8. **使用 CI/CD 自动化测试和部署**

### ❌ 避免做法

1. ❌ 不写 `.claude.md`，让 Claude 每次都重新学习项目
2. ❌ 手动重复执行测试/构建命令
3. ❌ 不写 SPEC，需求模糊导致返工
4. ❌ 忘记更新 CHANGELOG
5. ❌ 权限配置过于宽松
6. ❌ 跳过测试直接提交
7. ❌ 敏感信息硬编码到代码中

---

## 🛠 编辑器集成与 LSP

### 何时启用 LSP
- 当仓库体量较大、需要精确引用/定义跳转或希望在 Claude Code 内直接定位符号时，再启用 LSP 能显著提高效率，平常轻量对话可继续沿用 `Glob`/`Grep`。
- 启动前确认项目语言（Python、TS/JS、Go）是否在 `.claude/cclsp.json` 中声明，避免多余 server 依赖。

### 启用配置
1. 启动 Claude 时在外层加入 `ENABLE_LSP_TOOLS=1` 环境变量。
2. 在 `~/.claude/cclsp.json` 中声明 language server：

```json
{
  "servers": [
    {
      "extensions": ["js", "ts", "jsx", "tsx"],
      "command": ["npx", "typescript-language-server", "--stdio"],
      "rootDir": "."
    },
    {
      "extensions": ["py", "pyi"],
      "command": ["uvx", "--from", "python-lsp-server", "pylsp"],
      "rootDir": "."
    },
    {
      "extensions": ["go"],
      "command": ["gopls"],
      "rootDir": "."
    }
  ]
}
```

3. 仅列出当前项目需要的 language server，避免多余拓展。文件名匹配由 `extensions` 控制。

### 推荐语言组合及安装说明
- **TypeScript/JavaScript**：遵循你偏好的 Node 安装方式（建议全局 `npm install -g typescript-language-server typescript`），也可通过 `npx typescript-language-server --stdio` 临时启动；验证：`typescript-language-server --version`。
- **Python**：推荐 `uvx --from python-lsp-server pylsp` 或直接 `pip install python-lsp-server` 后执行 `pylsp`；验证：`uvx --from python-lsp-server pylsp --help`。
- **Go**：安装 `gopls`（`go install golang.org/x/tools/gopls@latest`）并确认 `gopls version` 输出正常；配合 monorepo 时根据模块设置 `rootDir`。

### 在 Claude Code 中使用 LSP
- 描述性提示词，例如：
  - “在 `src/main.ts` 中查找 `renderPage` 的所有引用。”
  - “帮我列出 `handlers/auth.py` 中 `generate_token` 的定义及被哪些文件调用。”
  - “这个 `greet` 函数在哪些 Go 文件里被引用？”
- 输出期望包括路径 + 行号，便于 Claude 直接定位；如果结果未返回，先确认语义对象存在且文件在扫描许可列表内。

### 排错与维护
- **Server 无法启动**：检查 `node`/`python`/`go` 所在路径是否在 `PATH`，`nvm`/`pyenv` 等版本管理器是否正确激活。
- **位置不对**：确认 `rootDir` 指向 monorepo 的实际项目根，或根据不同模块配置多个 server。
- **依赖缺失**：使用 `npm install -g` / `pip install` / `go install` 补全依赖；确认 `type-check`/`build` 命令在本地可运行。
- **不想启用**：可删除 `~/.claude/cclsp.json` 或移除 `ENABLE_LSP_TOOLS=1` 环境变量以还原默认行为。

### 导航提示
- 本节内容会在 `docs/INDEX.md` 中新增“LSP / 编辑器集成”入口，并在 `README.md` 的最佳实践导航处补充指向本节的链接。以便团队更快找到相关配置。

## 📚 参考资源

- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Claude Code 官方文档](https://code.claude.com/docs/)
