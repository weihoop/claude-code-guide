# SPEC 实战案例集

涵盖不同类型项目的完整 SPEC 示例，可直接复用和参考。

---

## 📋 案例目录

1. [CLI 工具：代码检查器](#案例1-cli-工具代码检查器)
2. [RESTful API：博客系统](#案例2-restful-api博客系统)
3. [NPM 包：日期处理库](#案例3-npm-包日期处理库)
4. [数据处理：日志分析工具](#案例4-数据处理日志分析工具)
5. [实时应用：聊天系统](#案例5-实时应用聊天系统)

---

## 案例1: CLI 工具：代码检查器

### 项目信息
- **类型**：命令行工具
- **语言**：Node.js + TypeScript
- **用途**：检查代码中的敏感信息泄露

### SPEC 文档

```markdown
# Code Scanner - 代码安全扫描工具规格说明

## 1. 项目概述

### 1.1 背景
开发者经常不小心将 API 密钥、密码等敏感信息提交到代码仓库。

### 1.2 目标
提供一个快速、准确的命令行工具，扫描代码中的敏感信息。

### 1.3 范围
- ✅ 扫描本地文件和目录
- ✅ 检测常见敏感信息模式
- ✅ 支持自定义规则
- ✅ 生成扫描报告
- ❌ 不包括：远程仓库扫描、实时监控

---

## 2. 功能需求

### 2.1 基础扫描

#### 2.1.1 命令格式
\```bash
code-scan [options] <path>
\```

#### 2.1.2 参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| path | string | ✅ | - | 扫描路径 |
| --config | string | ❌ | .scanrc.json | 配置文件路径 |
| --output | string | ❌ | stdout | 输出文件路径 |
| --format | string | ❌ | text | 输出格式（text/json/html） |
| --severity | string | ❌ | medium | 最低严重级别（low/medium/high） |
| --exclude | string[] | ❌ | [] | 排除的文件模式 |

#### 2.1.3 输出格式

**文本格式**：
\```
Code Scanner v1.0.0

Scanning: /Users/user/project
Files scanned: 156
Issues found: 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 HIGH: API Key Detected
File: src/config.ts:12
Code: const apiKey = "sk_live_abc123..."
Rule: aws-access-key

🟠 MEDIUM: Hardcoded Password
File: src/database.ts:5
Code: password: "admin123"
Rule: generic-password

🔴 HIGH: Private Key
File: .env:3
Code: PRIVATE_KEY=-----BEGIN RSA...
Rule: private-key

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Summary:
  High: 2
  Medium: 1
  Low: 0

Scan completed in 1.23s
\```

**JSON 格式**：
\```json
{
  "version": "1.0.0",
  "scanPath": "/Users/user/project",
  "timestamp": "2025-01-10T10:30:00Z",
  "stats": {
    "filesScanned": 156,
    "issuesFound": 3,
    "duration": 1.23
  },
  "issues": [
    {
      "severity": "high",
      "rule": "aws-access-key",
      "message": "API Key Detected",
      "file": "src/config.ts",
      "line": 12,
      "column": 15,
      "code": "const apiKey = \"sk_live_abc123...\"",
      "match": "sk_live_abc123..."
    }
  ]
}
\```

### 2.2 检测规则

#### 2.2.1 内置规则

| 规则ID | 严重级别 | 模式 | 描述 |
|--------|----------|------|------|
| aws-access-key | HIGH | `AKIA[0-9A-Z]{16}` | AWS Access Key |
| aws-secret-key | HIGH | `[0-9a-zA-Z/+]{40}` | AWS Secret Key |
| github-token | HIGH | `ghp_[0-9a-zA-Z]{36}` | GitHub Personal Access Token |
| stripe-key | HIGH | `sk_live_[0-9a-zA-Z]{24}` | Stripe API Key |
| generic-password | MEDIUM | `password\s*=\s*["'][^"']+["']` | 硬编码密码 |
| private-key | HIGH | `-----BEGIN.*PRIVATE KEY-----` | 私钥 |
| slack-webhook | MEDIUM | `https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}` | Slack Webhook |

#### 2.2.2 自定义规则配置

**文件**: `.scanrc.json`

\```json
{
  "rules": {
    "custom-api-key": {
      "severity": "high",
      "pattern": "API_KEY=[a-f0-9]{32}",
      "message": "Custom API Key detected"
    }
  },
  "exclude": [
    "node_modules/**",
    "dist/**",
    "**/*.test.ts"
  ],
  "allowlist": {
    "files": [".env.example"],
    "patterns": ["EXAMPLE_KEY", "PLACEHOLDER"]
  }
}
\```

### 2.3 性能要求

| 指标 | 要求 |
|------|------|
| 扫描速度 | > 1000 文件/秒 |
| 内存占用 | < 100MB（扫描10000文件） |
| 启动时间 | < 100ms |

---

## 3. 技术实现

### 3.1 技术栈
- Node.js 18+
- TypeScript
- Commander.js（CLI 框架）
- Glob（文件匹配）
- Chalk（终端颜色）

### 3.2 架构设计

\```
CLI 入口
  ↓
参数解析 (Commander)
  ↓
配置加载 (.scanrc.json)
  ↓
文件扫描 (Glob)
  ↓
规则匹配 (正则表达式)
  ↓
结果格式化
  ↓
输出报告
\```

### 3.3 目录结构

\```
code-scanner/
├── src/
│   ├── cli.ts           # CLI 入口
│   ├── scanner.ts       # 扫描引擎
│   ├── rules/
│   │   ├── index.ts
│   │   └── builtin.ts   # 内置规则
│   ├── formatters/
│   │   ├── text.ts
│   │   ├── json.ts
│   │   └── html.ts
│   └── types.ts
├── tests/
├── package.json
└── tsconfig.json
\```

---

## 4. 测试用例

### 4.1 正常流程

\```typescript
test('扫描单个文件', async () => {
  const result = await scan('test/fixtures/api-key.ts');

  expect(result.issues).toHaveLength(1);
  expect(result.issues[0].rule).toBe('aws-access-key');
  expect(result.issues[0].severity).toBe('high');
});

test('扫描目录', async () => {
  const result = await scan('test/fixtures/project/');

  expect(result.stats.filesScanned).toBeGreaterThan(0);
  expect(result.issues.length).toBeGreaterThanOrEqual(0);
});
\```

### 4.2 规则匹配

\```typescript
test('检测 AWS Access Key', () => {
  const code = 'const key = "AKIAIOSFODNN7EXAMPLE";';
  const matches = matchRule(code, 'aws-access-key');

  expect(matches).toHaveLength(1);
  expect(matches[0]).toBe('AKIAIOSFODNN7EXAMPLE');
});

test('检测硬编码密码', () => {
  const code = 'const password = "admin123";';
  const matches = matchRule(code, 'generic-password');

  expect(matches).toHaveLength(1);
});
\```

### 4.3 配置加载

\```typescript
test('加载自定义配置', () => {
  const config = loadConfig('.scanrc.test.json');

  expect(config.rules).toHaveProperty('custom-api-key');
  expect(config.exclude).toContain('node_modules/**');
});
\```

### 4.4 性能测试

\```typescript
test('扫描1000个文件 < 1秒', async () => {
  const start = Date.now();
  await scan('test/fixtures/large-project/');
  const duration = Date.now() - start;

  expect(duration).toBeLessThan(1000);
});
\```

---

## 5. 使用示例

### 5.1 基础使用

\```bash
# 扫描当前目录
code-scan .

# 扫描指定文件
code-scan src/config.ts

# 输出 JSON 格式
code-scan . --format json

# 只显示高危问题
code-scan . --severity high

# 排除目录
code-scan . --exclude "node_modules/**" --exclude "dist/**"
\```

### 5.2 集成到 Git Hook

**文件**: `.git/hooks/pre-commit`

\```bash
#!/bin/bash

echo "Running code scanner..."
code-scan --severity high --format text

if [ $? -ne 0 ]; then
  echo "❌ Code scan failed! Please fix the issues before committing."
  exit 1
fi

echo "✅ Code scan passed!"
\```

### 5.3 集成到 CI/CD

**GitHub Actions**:

\```yaml
name: Security Scan

on: [push, pull_request]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install scanner
        run: npm install -g code-scanner

      - name: Run scan
        run: code-scan . --format json --output scan-results.json

      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: scan-results
          path: scan-results.json
\```

---

## 6. 发布清单

### 6.1 打包

\```bash
npm run build
npm pack
\```

### 6.2 发布到 NPM

\```bash
npm login
npm publish
\```

### 6.3 文档

- [ ] README.md 完整
- [ ] 使用示例清晰
- [ ] API 文档生成
- [ ] CHANGELOG 更新
```

---

## 案例2: RESTful API：博客系统

### 项目信息
- **类型**：Web API
- **技术栈**：Next.js 15 + Prisma + PostgreSQL
- **用途**：博客文章管理 API

### SPEC 文档（简化版）

```markdown
# Blog API 规格说明

## 1. 功能需求

### 1.1 文章管理

#### 1.1.1 创建文章

**端点**: `POST /api/v1/posts`

**请求体**:
\```json
{
  "title": "文章标题",
  "content": "文章内容（Markdown）",
  "excerpt": "摘要（可选）",
  "tags": ["tag1", "tag2"],
  "published": false
}
\```

**验证规则**:
- title: 1-200字符，必填
- content: 1-50000字符，必填
- excerpt: 最多500字符
- tags: 最多10个，每个最多20字符
- published: boolean，默认 false

**响应**（201）:
\```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "title": "文章标题",
    "slug": "wen-zhang-biao-ti",
    "content": "...",
    "excerpt": "...",
    "tags": ["tag1", "tag2"],
    "published": false,
    "views": 0,
    "createdAt": "2025-01-10T10:00:00Z",
    "updatedAt": "2025-01-10T10:00:00Z",
    "author": {
      "id": "uuid",
      "username": "john",
      "avatar": "https://..."
    }
  }
}
\```

**业务规则**:
1. Slug 自动生成（拼音或 ID）
2. 同一作者的 title 必须唯一
3. 未发布的文章只有作者可见
4. Tags 自动创建（如果不存在）

**测试用例**:
\```typescript
test('成功创建文章', async () => {
  const response = await request(app)
    .post('/api/v1/posts')
    .set('Authorization', `Bearer ${token}`)
    .send({
      title: '我的第一篇文章',
      content: '# Hello World\n这是内容...',
      tags: ['技术', 'Node.js']
    });

  expect(response.status).toBe(201);
  expect(response.body.data.slug).toBe('wo-de-di-yi-pian-wen-zhang');
  expect(response.body.data.published).toBe(false);
});

test('拒绝过长标题', async () => {
  const response = await request(app)
    .post('/api/v1/posts')
    .set('Authorization', `Bearer ${token}`)
    .send({
      title: 'a'.repeat(201),
      content: '内容'
    });

  expect(response.status).toBe(400);
  expect(response.body.error.code).toBe('TITLE_TOO_LONG');
});
\```

#### 1.1.2 获取文章列表

**端点**: `GET /api/v1/posts`

**查询参数**:
| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| page | number | 1 | 页码 |
| limit | number | 20 | 每页数量（最大100） |
| tag | string | - | 标签筛选 |
| author | string | - | 作者筛选 |
| search | string | - | 搜索关键词 |
| sort | string | -createdAt | 排序（createdAt/views/title） |

**响应**（200）:
\```json
{
  "success": true,
  "data": {
    "posts": [...],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 100,
      "totalPages": 5
    }
  }
}
\```

---

## 2. 数据模型

\```prisma
model Post {
  id          String   @id @default(uuid())
  title       String   @db.VarChar(200)
  slug        String   @unique
  content     String   @db.Text
  excerpt     String?  @db.VarChar(500)
  published   Boolean  @default(false)
  views       Int      @default(0)
  authorId    String
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
  publishedAt DateTime?

  author      User     @relation(fields: [authorId], references: [id])
  tags        Tag[]    @relation("PostTags")

  @@index([authorId])
  @@index([slug])
  @@index([createdAt])
}

model Tag {
  id        String   @id @default(uuid())
  name      String   @unique @db.VarChar(20)
  slug      String   @unique
  posts     Post[]   @relation("PostTags")
  createdAt DateTime @default(now())
}
\```
```

---

## 案例3: NPM 包：日期处理库

### 项目信息
- **类型**：JavaScript 库
- **用途**：提供轻量级日期处理工具

### SPEC 文档（简化版）

```markdown
# DateUtils - 日期处理库规格说明

## 1. API 设计

### 1.1 format - 格式化日期

\```typescript
function format(date: Date, format: string): string
\```

**参数**:
- `date`: Date 对象
- `format`: 格式字符串
  - `YYYY`: 4位年份
  - `MM`: 2位月份
  - `DD`: 2位日期
  - `HH`: 24小时制小时
  - `mm`: 分钟
  - `ss`: 秒

**示例**:
\```javascript
format(new Date('2025-01-10'), 'YYYY-MM-DD')
// => '2025-01-10'

format(new Date('2025-01-10 15:30:00'), 'YYYY年MM月DD日 HH:mm')
// => '2025年01月10日 15:30'
\```

**边界条件**:
- 无效日期 → 抛出 TypeError
- 空格式字符串 → 返回空字符串
- 不支持的格式符 → 原样返回

**测试用例**:
\```typescript
test('格式化为 ISO 日期', () => {
  const date = new Date('2025-01-10');
  expect(format(date, 'YYYY-MM-DD')).toBe('2025-01-10');
});

test('处理月份补零', () => {
  const date = new Date('2025-01-01');
  expect(format(date, 'MM')).toBe('01');
});

test('拒绝无效日期', () => {
  expect(() => format(new Date('invalid'), 'YYYY-MM-DD'))
    .toThrow(TypeError);
});
\```

### 1.2 addDays - 添加天数

\```typescript
function addDays(date: Date, days: number): Date
\```

**参数**:
- `date`: 基准日期
- `days`: 要添加的天数（可以为负数）

**返回**: 新的 Date 对象（不修改原对象）

**示例**:
\```javascript
addDays(new Date('2025-01-10'), 5)
// => Date('2025-01-15')

addDays(new Date('2025-01-10'), -3)
// => Date('2025-01-07')
\```

### 1.3 isSameDay - 判断同一天

\```typescript
function isSameDay(date1: Date, date2: Date): boolean
\```

**逻辑**: 忽略时间部分，只比较日期

**示例**:
\```javascript
isSameDay(
  new Date('2025-01-10 10:00:00'),
  new Date('2025-01-10 15:30:00')
)
// => true

isSameDay(
  new Date('2025-01-10'),
  new Date('2025-01-11')
)
// => false
\```

---

## 2. 包元数据

\```json
{
  "name": "date-utils",
  "version": "1.0.0",
  "description": "Lightweight date utility library",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "keywords": ["date", "time", "format", "utility"],
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  }
}
\```

---

## 3. 性能要求

| 操作 | 要求 |
|------|------|
| format() | < 1ms per call |
| addDays() | < 0.5ms per call |
| 包体积 | < 5KB (gzipped) |
| Tree-shakable | ✅ |
```

---

## 案例4: 数据处理：日志分析工具

### 项目信息
- **类型**：数据处理脚本
- **语言**：Python
- **用途**：分析 Nginx 日志并生成报告

### SPEC 文档（简化版）

```markdown
# Log Analyzer 规格说明

## 1. 功能需求

### 1.1 日志解析

**输入**: Nginx 访问日志（Combined 格式）

\```
192.168.1.1 - - [10/Jan/2025:10:30:00 +0000] "GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0..."
\```

**解析字段**:
- IP 地址
- 时间戳
- HTTP 方法
- 请求路径
- 状态码
- 响应大小
- User-Agent

### 1.2 统计分析

**指标**:
1. 请求总数
2. 状态码分布（200, 404, 500等）
3. Top 10 最热路径
4. Top 10 最慢请求
5. 每小时请求量趋势
6. 错误率（4xx + 5xx）

**输出格式**:
\```json
{
  "summary": {
    "total_requests": 10000,
    "date_range": {
      "start": "2025-01-10T00:00:00Z",
      "end": "2025-01-10T23:59:59Z"
    },
    "error_rate": 2.5
  },
  "status_codes": {
    "200": 9500,
    "404": 200,
    "500": 50
  },
  "top_paths": [
    { "path": "/api/users", "count": 3000 },
    { "path": "/api/posts", "count": 2500 }
  ]
}
\```

---

## 2. 命令行接口

\```bash
python analyze_logs.py <log_file> [options]
\```

**参数**:
| 参数 | 说明 | 默认值 |
|------|------|--------|
| --start-date | 开始日期 | - |
| --end-date | 结束日期 | - |
| --output | 输出文件 | stdout |
| --format | 输出格式（json/text/html） | text |

---

## 3. 性能要求

- 处理速度: > 100,000 行/秒
- 内存占用: < 500MB（处理1GB日志）
- 支持文件大小: 最大 10GB
```

---

## 案例5: 实时应用：聊天系统

### 项目信息
- **类型**：实时 Web 应用
- **技术栈**：Next.js + Socket.IO + Redis
- **用途**：多人实时聊天

### SPEC 文档（简化版）

```markdown
# Chat System 规格说明

## 1. 核心功能

### 1.1 实时消息

**事件**: `message:send`

**数据结构**:
\```typescript
interface Message {
  id: string;
  roomId: string;
  userId: string;
  content: string;
  type: 'text' | 'image' | 'file';
  timestamp: number;
}
\```

**验证**:
- content: 1-5000字符
- 频率限制: 每秒最多5条消息

**广播**: 同一房间的所有用户

### 1.2 在线状态

**事件**: `user:online`, `user:offline`

**数据结构**:
\```typescript
interface UserStatus {
  userId: string;
  username: string;
  status: 'online' | 'offline' | 'away';
  lastSeen: number;
}
\```

**逻辑**:
- 连接时 → online
- 断开时 → offline
- 5分钟无活动 → away

---

## 2. 数据模型

\```typescript
// Room（聊天室）
interface Room {
  id: string;
  name: string;
  type: 'public' | 'private';
  members: string[];  // User IDs
  createdAt: number;
}

// Message（消息）
interface Message {
  id: string;
  roomId: string;
  userId: string;
  content: string;
  type: 'text' | 'image' | 'file';
  timestamp: number;
  edited: boolean;
  deletedAt?: number;
}

// User（用户）
interface User {
  id: string;
  username: string;
  avatar: string;
  status: 'online' | 'offline' | 'away';
  lastSeen: number;
}
\```

---

## 3. WebSocket API

### 3.1 客户端 → 服务器

| 事件 | 数据 | 说明 |
|------|------|------|
| `room:join` | `{ roomId }` | 加入房间 |
| `room:leave` | `{ roomId }` | 离开房间 |
| `message:send` | `Message` | 发送消息 |
| `typing:start` | `{ roomId }` | 开始输入 |
| `typing:stop` | `{ roomId }` | 停止输入 |

### 3.2 服务器 → 客户端

| 事件 | 数据 | 说明 |
|------|------|------|
| `message:new` | `Message` | 新消息 |
| `user:joined` | `User` | 用户加入 |
| `user:left` | `{ userId }` | 用户离开 |
| `typing:status` | `{ userId, typing }` | 输入状态 |

---

## 4. 性能要求

| 指标 | 要求 |
|------|------|
| 消息延迟 | < 100ms |
| 并发连接 | > 10,000 |
| 房间人数 | 最多 1,000 人/房间 |
| 消息吞吐 | > 10,000 msg/s |
```

---

## 使用建议

### 1. 选择合适的案例

| 项目类型 | 参考案例 |
|---------|---------|
| CLI 工具 | 案例1 - 代码检查器 |
| Web API | 案例2 - 博客系统 |
| NPM 包 | 案例3 - 日期处理库 |
| 数据处理 | 案例4 - 日志分析 |
| 实时应用 | 案例5 - 聊天系统 |

### 2. 复用模板

每个案例都可以作为模板：
1. 复制对应的 SPEC 结构
2. 根据你的需求修改细节
3. 保持测试用例的完整性

### 3. 与 Claude Code 配合

\```bash
# 使用案例作为参考
> 参考 docs/examples/spec-examples.md 中的"CLI 工具"案例
> 帮我创建一个日志分析工具的 SPEC

# Claude 会：
# 1. 读取对应案例
# 2. 理解你的具体需求
# 3. 生成定制化的 SPEC
\```

---

## 下一步

- 查看 [SPEC 范式编程指南](../spec-driven-development.md) 了解如何使用 SPEC
- 查看 [Claude Code 最佳实践](../claude-code-best-practices.md) 了解完整开发流程
- 使用这些案例作为你的项目起点
