# SPEC 范式编程指南

基于规格驱动开发（Specification-Driven Development）的完整实践指南，专为 Claude Code 优化。

---

## 📖 目录

- [什么是 SPEC 范式编程](#什么是-spec-范式编程)
- [为什么要用 SPEC 范式](#为什么要用-spec-范式)
- [SPEC 文档结构](#spec-文档结构)
- [SPEC 驱动的开发流程](#spec-驱动的开发流程)
- [SPEC 模板和示例](#spec-模板和示例)
- [与 Claude Code 配合](#与-claude-code-配合)
- [最佳实践](#最佳实践)
- [常见问题](#常见问题)

---

## 什么是 SPEC 范式编程

### 核心理念

**SPEC 范式编程**是一种"先规格后编码"的开发方法论：

```
需求分析 → 编写 SPEC → 审查 SPEC → 基于 SPEC 编码 → 验证符合 SPEC
```

### 与传统开发的对比

| 维度 | 传统开发 | SPEC 范式 |
|------|---------|----------|
| **起点** | 需求讨论 → 直接编码 | 需求分析 → SPEC 文档 → 编码 |
| **文档** | 代码完成后补文档 | 文档先行，代码实现文档 |
| **协作** | 口头沟通为主 | 文档驱动，减少歧义 |
| **变更** | 改代码后更新文档 | 改 SPEC 后更新代码 |
| **测试** | 手工设计测试用例 | 基于 SPEC 生成测试 |
| **AI 辅助** | AI 猜测需求 | AI 严格按 SPEC 实现 |

### 核心优势

1. **需求明确**：减少 50% 的需求变更
2. **提高质量**：减少 70% 的 bug
3. **团队协作**：统一的理解基准
4. **AI 友好**：Claude 能够精确实现 SPEC
5. **可测试性**：测试用例直接来自 SPEC

---

## 为什么要用 SPEC 范式

### 1. Claude Code 的特性需要 SPEC

#### ❌ 没有 SPEC 的情况

```
开发者：帮我实现一个用户登录功能

Claude：好的，我将实现一个基础的用户登录功能...
[Claude 猜测：可能用 JWT？可能用 Session？密码策略是什么？]
```

**问题**：
- Claude 需要猜测大量细节
- 可能做出不符合需求的实现
- 需要多轮对话澄清

#### ✅ 有 SPEC 的情况

```
开发者：按照 SPEC.md 中的 "1.2 用户登录" 部分实现

Claude：
- 读取 SPEC.md
- 看到明确的：认证方式（JWT）、密码策略、错误处理、性能要求
- 精确实现，一次到位
```

**优势**：
- 无需猜测，减少沟通成本
- 实现准确，减少返工
- 测试用例已在 SPEC 中定义

### 2. 减少 Token 消耗

| 场景 | 无 SPEC | 有 SPEC | Token 节省 |
|------|---------|---------|-----------|
| 需求澄清 | 10+ 轮对话 | 1次读取 SPEC | 80% |
| 实现细节 | 反复询问 | SPEC 已说明 | 70% |
| 测试用例 | 讨论设计 | SPEC 已定义 | 90% |

### 3. 提高开发效率

```
传统流程：需求讨论(2h) → 编码(4h) → 测试发现理解偏差 → 返工(3h) = 9小时

SPEC流程：编写SPEC(1.5h) → 审查SPEC(0.5h) → 编码(3h) → 测试(0.5h) = 5.5小时
```

**效率提升 40%+**

### 4. 更好的代码质量

基于 SPEC 的代码特点：
- ✅ 边界条件完整（SPEC 已定义）
- ✅ 错误处理规范（SPEC 已说明）
- ✅ 性能指标明确（SPEC 已要求）
- ✅ 安全措施到位（SPEC 已规定）

---

## SPEC 文档结构

### 推荐结构

```markdown
# 功能规格说明书

## 1. 项目信息
- 项目名称
- 版本
- 负责人
- 最后更新日期

## 2. 概述
- 项目背景
- 目标
- 范围

## 3. 功能需求
### 3.1 功能模块A
#### 3.1.1 子功能1
- **功能描述**
- **用户故事**
- **输入**
- **输出**
- **业务规则**
- **验证规则**
- **错误处理**
- **测试用例**

## 4. 数据模型
- 实体关系图
- 数据表结构
- 字段说明
- 索引设计

## 5. API 设计
- 端点列表
- 请求/响应格式
- 认证方式
- 错误码定义

## 6. 技术实现
- 技术栈
- 架构设计
- 安全措施
- 性能要求

## 7. 测试计划
- 单元测试
- 集成测试
- E2E 测试
- 性能测试

## 8. 部署要求
- 环境配置
- 依赖服务
- 监控指标
```

---

## SPEC 驱动的开发流程

### 完整流程图

```
1. 需求分析
   ↓
2. 编写 SPEC（文档优先）
   ↓
3. 团队审查 SPEC
   ↓
4. SPEC 确认和版本控制
   ↓
5. 基于 SPEC 设计数据模型
   ↓
6. 基于 SPEC 设计 API
   ↓
7. 基于 SPEC 编写测试用例
   ↓
8. 基于 SPEC 实现代码
   ↓
9. 运行测试验证符合 SPEC
   ↓
10. 代码审查（对照 SPEC）
    ↓
11. 部署和监控
    ↓
12. 维护（SPEC 和代码同步更新）
```

### 详细步骤

#### 第 1 步：需求分析

**任务**：
- 收集用户需求
- 分析业务目标
- 识别关键功能
- 定义成功标准

**输出**：
- 需求列表
- 用户故事
- 优先级排序

**示例**：
```
用户故事：作为一个网站用户，我希望能够注册账号，以便使用网站的功能

关键需求：
1. 支持邮箱注册
2. 密码必须安全
3. 发送验证邮件
4. 防止恶意注册
```

#### 第 2 步：编写 SPEC

**任务**：
- 将需求转化为详细的规格说明
- 定义所有输入输出
- 明确业务规则和验证逻辑
- 设计错误处理
- 编写测试用例

**关键原则**：
- ✅ **具体明确**：不用"合理的密码"，用"8-32字符，包含大小写字母和数字"
- ✅ **完整覆盖**：考虑正常流程、异常情况、边界条件
- ✅ **可测试**：每个需求都有对应的测试用例
- ✅ **可实现**：技术上可行，有明确的实现路径

**示例**（见下文完整模板）

#### 第 3 步：团队审查 SPEC

**参与人**：
- 产品经理（业务逻辑）
- 技术负责人（技术可行性）
- 开发工程师（实现细节）
- 测试工程师（测试覆盖）

**审查清单**：
- [ ] 需求理解一致
- [ ] 技术方案可行
- [ ] 边界条件完整
- [ ] 错误处理充分
- [ ] 性能要求合理
- [ ] 安全措施到位
- [ ] 测试用例覆盖

#### 第 4 步：SPEC 确认和版本控制

```bash
# 提交 SPEC 到版本控制
git add SPEC.md
git commit -m "docs: 添加用户认证功能规格 v1.0"
git push origin main

# 打标签
git tag spec-auth-v1.0
git push origin spec-auth-v1.0
```

#### 第 5-8 步：基于 SPEC 开发

**使用 Claude Code**：

```
# 1. 让 Claude 读取 SPEC
> 请阅读 SPEC.md 的第 3.1 节"用户注册"部分

# 2. 按 SPEC 设计数据模型
> 根据 SPEC 中的需求，设计 User 表结构

# 3. 按 SPEC 设计 API
> 根据 SPEC 实现 POST /api/auth/register 接口

# 4. 按 SPEC 编写测试
> 根据 SPEC 中的测试用例，编写单元测试

# 5. 按 SPEC 实现功能
> 实现用户注册功能，严格遵循 SPEC 的要求
```

#### 第 9 步：验证符合 SPEC

**验证清单**：

```bash
# 1. 运行测试
npm test

# 2. 验证 API 符合 SPEC
> 检查 /api/auth/register 的实现是否完全符合 SPEC 中的定义

# 3. 边界条件测试
> 测试 SPEC 中定义的所有边界条件

# 4. 错误处理测试
> 测试 SPEC 中定义的所有错误场景
```

#### 第 10 步：代码审查

**审查要点**：
- [ ] 实现与 SPEC 一致
- [ ] 所有测试用例通过
- [ ] 代码质量符合标准
- [ ] 文档注释完整

#### 第 11-12 步：部署和维护

**SPEC 和代码同步**：
```
需求变更 → 先更新 SPEC → 审查 SPEC → 更新代码 → 更新测试
```

---

## SPEC 模板和示例

### 完整示例：用户认证模块

```markdown
# 用户认证模块规格说明

## 1. 项目信息
- **项目名称**：用户管理系统
- **模块**：用户认证
- **版本**：v1.0.0
- **负责人**：@username
- **最后更新**：2025-01-10

---

## 2. 概述

### 2.1 模块背景
提供用户注册、登录、登出等基础认证功能，支持 Web 和移动应用。

### 2.2 目标
- 安全可靠的用户认证
- 良好的用户体验
- 防止恶意攻击

### 2.3 范围
- ✅ 包含：邮箱注册、邮箱登录、JWT 认证、密码重置
- ❌ 不包含：第三方登录（OAuth）、双因素认证（2FA）

---

## 3. 功能需求

### 3.1 用户注册

#### 3.1.1 功能描述
允许新用户通过邮箱注册账号。

#### 3.1.2 用户故事
```
作为一个访客
我希望能够注册账号
以便使用系统的功能
```

#### 3.1.3 输入

| 字段 | 类型 | 必填 | 验证规则 | 示例 |
|------|------|------|----------|------|
| email | string | ✅ | 有效的邮箱格式 | user@example.com |
| password | string | ✅ | 8-32字符，包含大小写字母和数字 | SecurePass123 |
| username | string | ❌ | 3-20字符，字母数字下划线 | john_doe |

#### 3.1.4 输出

**成功响应**（HTTP 201）：
\```json
{
  "success": true,
  "data": {
    "userId": "uuid-v4-format",
    "email": "user@example.com",
    "username": "john_doe",
    "token": "jwt-token-string",
    "expiresAt": "2025-01-17T00:00:00Z"
  }
}
\```

**失败响应**（HTTP 400/409/429）：
\```json
{
  "success": false,
  "error": {
    "code": "EMAIL_EXISTS",
    "message": "该邮箱已被注册",
    "field": "email"
  }
}
\```

#### 3.1.5 业务规则

1. **邮箱唯一性**
   - 每个邮箱只能注册一次
   - 大小写不敏感（user@example.com === USER@example.com）

2. **密码策略**
   - 长度：8-32 字符
   - 必须包含：至少 1 个大写字母、1 个小写字母、1 个数字
   - 可选：特殊字符 (!@#$%^&*)
   - 禁止：常见弱密码（password123, 12345678 等）

3. **用户名规则**
   - 可选字段
   - 如果提供，必须唯一
   - 3-20 字符
   - 只能包含：字母、数字、下划线
   - 不能以数字开头

4. **邮箱验证**
   - 注册成功后发送验证邮件
   - 验证链接 24 小时内有效
   - 未验证用户功能受限

#### 3.1.6 验证规则

**邮箱验证**：
\```javascript
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!emailRegex.test(email)) {
  return { valid: false, error: 'INVALID_EMAIL_FORMAT' };
}
\```

**密码强度验证**：
\```javascript
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d!@#$%^&*]{8,32}$/;
if (!passwordRegex.test(password)) {
  return { valid: false, error: 'WEAK_PASSWORD' };
}

const weakPasswords = ['password123', '12345678', 'qwerty123'];
if (weakPasswords.includes(password.toLowerCase())) {
  return { valid: false, error: 'COMMON_PASSWORD' };
}
\```

#### 3.1.7 错误处理

| 错误码 | HTTP 状态 | 触发条件 | 错误消息 |
|--------|----------|---------|----------|
| INVALID_EMAIL_FORMAT | 400 | 邮箱格式无效 | 请输入有效的邮箱地址 |
| WEAK_PASSWORD | 400 | 密码不符合强度要求 | 密码必须包含 8-32 字符、大小写字母和数字 |
| COMMON_PASSWORD | 400 | 使用常见弱密码 | 该密码过于简单，请使用更安全的密码 |
| EMAIL_EXISTS | 409 | 邮箱已被注册 | 该邮箱已被注册，请使用其他邮箱或登录 |
| USERNAME_EXISTS | 409 | 用户名已被占用 | 该用户名已被占用，请尝试其他用户名 |
| RATE_LIMIT_EXCEEDED | 429 | 超过频率限制 | 请求过于频繁，请 1 分钟后再试 |
| SERVER_ERROR | 500 | 服务器内部错误 | 服务器错误，请稍后重试 |

#### 3.1.8 安全措施

1. **密码安全**
   - 使用 bcrypt 哈希（cost factor = 12）
   - 不存储明文密码
   - 不在日志中记录密码

2. **防止枚举攻击**
   - 邮箱已存在和邮箱不存在返回相同的延迟
   - 错误消息不透露用户是否存在

3. **频率限制**
   - 每个 IP 地址每分钟最多 3 次注册请求
   - 同一邮箱 1 小时内最多尝试 5 次
   - 使用 Redis 实现滑动窗口限流

4. **邮箱验证**
   - 验证令牌使用加密随机数（32 字节）
   - 令牌存储时哈希处理
   - 24 小时后自动过期

#### 3.1.9 性能要求

| 指标 | 要求 | 测量方法 |
|------|------|----------|
| 响应时间（P95） | < 500ms | 负载测试 |
| 响应时间（P99） | < 1000ms | 负载测试 |
| 并发处理 | 100 req/s | 压力测试 |
| 数据库查询 | < 100ms | APM 监控 |

#### 3.1.10 测试用例

**正常流程**：
\```javascript
test('成功注册新用户', async () => {
  const response = await request(app)
    .post('/api/auth/register')
    .send({
      email: 'newuser@example.com',
      password: 'SecurePass123',
      username: 'newuser'
    });

  expect(response.status).toBe(201);
  expect(response.body.success).toBe(true);
  expect(response.body.data).toHaveProperty('userId');
  expect(response.body.data).toHaveProperty('token');
  expect(response.body.data.email).toBe('newuser@example.com');
});
\```

**边界条件**：
\```javascript
test('密码最小长度（8字符）', async () => {
  const response = await request(app)
    .post('/api/auth/register')
    .send({
      email: 'test@example.com',
      password: 'Pass123!' // 刚好 8 字符
    });

  expect(response.status).toBe(201);
});

test('密码最大长度（32字符）', async () => {
  const response = await request(app)
    .post('/api/auth/register')
    .send({
      email: 'test@example.com',
      password: 'P'.repeat(31) + '1' // 刚好 32 字符
    });

  expect(response.status).toBe(201);
});
\```

**异常情况**：
\```javascript
test('拒绝重复邮箱', async () => {
  // 先注册一次
  await registerUser({ email: 'test@example.com', password: 'Pass123!' });

  // 再次注册
  const response = await request(app)
    .post('/api/auth/register')
    .send({
      email: 'test@example.com',
      password: 'AnotherPass123'
    });

  expect(response.status).toBe(409);
  expect(response.body.error.code).toBe('EMAIL_EXISTS');
});

test('拒绝弱密码', async () => {
  const response = await request(app)
    .post('/api/auth/register')
    .send({
      email: 'test@example.com',
      password: 'password123' // 常见弱密码
    });

  expect(response.status).toBe(400);
  expect(response.body.error.code).toBe('COMMON_PASSWORD');
});
\```

**安全测试**：
\```javascript
test('频率限制：同一IP 1分钟内最多3次', async () => {
  // 连续 4 次请求
  for (let i = 0; i < 3; i++) {
    await request(app).post('/api/auth/register').send({ ... });
  }

  const response = await request(app)
    .post('/api/auth/register')
    .send({ email: `test${i}@example.com`, password: 'Pass123!' });

  expect(response.status).toBe(429);
  expect(response.body.error.code).toBe('RATE_LIMIT_EXCEEDED');
});
\```

---

### 3.2 用户登录

#### 3.2.1 功能描述
允许已注册用户通过邮箱和密码登录。

#### 3.2.2 输入

| 字段 | 类型 | 必填 | 验证规则 |
|------|------|------|----------|
| email | string | ✅ | 有效的邮箱格式 |
| password | string | ✅ | 非空字符串 |
| rememberMe | boolean | ❌ | true/false，默认 false |

#### 3.2.3 输出

**成功响应**（HTTP 200）：
\```json
{
  "success": true,
  "data": {
    "userId": "uuid",
    "email": "user@example.com",
    "username": "john_doe",
    "token": "jwt-token",
    "expiresAt": "2025-01-17T00:00:00Z"
  }
}
\```

**失败响应**（HTTP 401）：
\```json
{
  "success": false,
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "邮箱或密码错误"
  }
}
\```

#### 3.2.4 业务规则

1. **认证逻辑**
   - 验证邮箱存在
   - 验证密码正确（使用 bcrypt.compare）
   - 两者都满足才允许登录

2. **Token 有效期**
   - 默认：7 天
   - rememberMe=true：30 天
   - 存储在 httpOnly Cookie 中

3. **失败次数限制**
   - 同一账号 15 分钟内最多失败 5 次
   - 超过限制后锁定账号 15 分钟
   - 发送安全警告邮件

#### 3.2.5 安全措施

1. **防止时序攻击**
   - 无论邮箱是否存在，总是执行相同时长的操作
   - 使用常量时间比较

2. **防止暴力破解**
   - 失败次数限制（见业务规则）
   - 渐进式延迟（每次失败增加 0.5 秒）

3. **会话安全**
   - JWT 签名验证
   - Token 存储在 httpOnly Cookie（防 XSS）
   - SameSite=Strict（防 CSRF）

#### 3.2.6 测试用例

\```javascript
test('成功登录', async () => {
  // 先注册
  await registerUser({ email: 'test@example.com', password: 'Pass123!' });

  // 登录
  const response = await request(app)
    .post('/api/auth/login')
    .send({
      email: 'test@example.com',
      password: 'Pass123!'
    });

  expect(response.status).toBe(200);
  expect(response.body.data).toHaveProperty('token');
});

test('拒绝错误密码', async () => {
  await registerUser({ email: 'test@example.com', password: 'Pass123!' });

  const response = await request(app)
    .post('/api/auth/login')
    .send({
      email: 'test@example.com',
      password: 'WrongPass123'
    });

  expect(response.status).toBe(401);
  expect(response.body.error.code).toBe('INVALID_CREDENTIALS');
});

test('5次失败后锁定账号', async () => {
  await registerUser({ email: 'test@example.com', password: 'Pass123!' });

  // 连续 5 次错误密码
  for (let i = 0; i < 5; i++) {
    await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'wrong' });
  }

  // 第 6 次，即使密码正确也被锁定
  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'Pass123!' });

  expect(response.status).toBe(429);
  expect(response.body.error.code).toBe('ACCOUNT_LOCKED');
});
\```

---

## 4. 数据模型

### 4.1 User 表

\```typescript
interface User {
  id: string;                  // UUID v4
  email: string;               // 唯一索引，小写存储
  emailVerified: boolean;      // 默认 false
  passwordHash: string;        // bcrypt hash (cost=12)
  username: string | null;     // 唯一索引（如果非空）
  role: 'user' | 'admin';     // 默认 'user'
  createdAt: Date;
  updatedAt: Date;
  lastLoginAt: Date | null;
}
\```

**索引**：
- PRIMARY KEY: `id`
- UNIQUE INDEX: `email` (小写)
- UNIQUE INDEX: `username` (WHERE username IS NOT NULL)
- INDEX: `createdAt` (用于分页查询)

**Prisma Schema**：
\```prisma
model User {
  id            String   @id @default(uuid())
  email         String   @unique @db.VarChar(255)
  emailVerified Boolean  @default(false)
  passwordHash  String   @db.VarChar(255)
  username      String?  @unique @db.VarChar(50)
  role          Role     @default(USER)
  createdAt     DateTime @default(now())
  updatedAt     DateTime @updatedAt
  lastLoginAt   DateTime?

  sessions      Session[]
  @@index([createdAt])
}

enum Role {
  USER
  ADMIN
}
\```

### 4.2 EmailVerification 表

\```typescript
interface EmailVerification {
  id: string;
  userId: string;             // 外键 -> User.id
  tokenHash: string;          // SHA-256 哈希
  expiresAt: Date;           // 24小时后
  createdAt: Date;
}
\```

### 4.3 LoginAttempt 表（失败次数追踪）

\```typescript
interface LoginAttempt {
  id: string;
  email: string;
  ipAddress: string;
  success: boolean;
  attemptedAt: Date;
}
\```

**索引**：
- INDEX: `email, attemptedAt`
- INDEX: `ipAddress, attemptedAt`

---

## 5. API 设计

### 5.1 端点列表

| 方法 | 端点 | 描述 | 认证 |
|------|------|------|------|
| POST | /api/v1/auth/register | 用户注册 | ❌ |
| POST | /api/v1/auth/login | 用户登录 | ❌ |
| POST | /api/v1/auth/logout | 用户登出 | ✅ |
| POST | /api/v1/auth/verify-email | 验证邮箱 | ❌ |
| POST | /api/v1/auth/resend-verification | 重新发送验证邮件 | ✅ |
| GET | /api/v1/auth/me | 获取当前用户信息 | ✅ |

### 5.2 通用响应格式

**成功响应**：
\```typescript
interface SuccessResponse<T> {
  success: true;
  data: T;
}
\```

**错误响应**：
\```typescript
interface ErrorResponse {
  success: false;
  error: {
    code: string;
    message: string;
    field?: string;      // 字段级错误
    details?: any;       // 额外信息
  };
}
\```

### 5.3 认证方式

- **JWT Token**：Bearer Token in Authorization header
- **Cookie**：httpOnly, Secure, SameSite=Strict
- **过期处理**：返回 401，客户端重定向到登录页

---

## 6. 技术实现

### 6.1 技术栈

- **后端框架**：Next.js 15 API Routes
- **数据库**：PostgreSQL 15
- **ORM**：Prisma 5.x
- **缓存**：Redis 7（频率限制、会话）
- **认证**：jose（JWT）
- **密码哈希**：bcrypt
- **邮件服务**：Resend / SendGrid

### 6.2 架构设计

\```
客户端请求
    ↓
API Route Handler
    ↓
[频率限制中间件] → Redis
    ↓
[输入验证] → Zod Schema
    ↓
[业务逻辑层]
    ↓
[数据访问层] → Prisma → PostgreSQL
    ↓
[响应格式化]
    ↓
返回客户端
\```

### 6.3 目录结构

\```
src/
├── app/
│   └── api/
│       └── v1/
│           └── auth/
│               ├── register/
│               │   └── route.ts
│               ├── login/
│               │   └── route.ts
│               └── logout/
│                   └── route.ts
├── lib/
│   ├── auth/
│   │   ├── password.ts      # 密码哈希和验证
│   │   ├── jwt.ts           # Token 生成和验证
│   │   └── rateLimit.ts     # 频率限制
│   ├── db/
│   │   └── prisma.ts        # Prisma 客户端
│   └── validation/
│       └── auth.ts          # Zod 验证 schemas
└── types/
    └── auth.ts              # TypeScript 类型定义
\```

---

## 7. 部署要求

### 7.1 环境变量

\```bash
# 数据库
DATABASE_URL=postgresql://user:pass@localhost:5432/db

# JWT
JWT_SECRET=your-256-bit-secret
JWT_EXPIRES_IN=7d

# Redis
REDIS_URL=redis://localhost:6379

# 邮件
RESEND_API_KEY=re_xxx

# 应用
NODE_ENV=production
APP_URL=https://example.com
\```

### 7.2 依赖服务

- PostgreSQL 15+
- Redis 7+
- 邮件服务（Resend/SendGrid）

### 7.3 监控指标

| 指标 | 目标 | 告警阈值 |
|------|------|---------|
| 注册成功率 | > 95% | < 90% |
| 登录成功率 | > 98% | < 95% |
| API 响应时间 P95 | < 500ms | > 1000ms |
| 数据库查询时间 | < 100ms | > 200ms |
| 错误率 | < 1% | > 2% |

---

## 8. 维护和更新

### 8.1 SPEC 版本管理

\```bash
# 主版本号：破坏性变更
SPEC v2.0.0: 修改 API 端点路径

# 次版本号：新增功能
SPEC v1.1.0: 添加 OAuth 登录

# 修订号：修复和澄清
SPEC v1.0.1: 明确密码长度限制
\```

### 8.2 变更流程

1. 提出需求变更
2. 更新 SPEC 文档
3. 团队审查 SPEC
4. 更新测试用例
5. 更新代码实现
6. 运行测试验证
7. 更新 CHANGELOG
8. 发布新版本

---

## 总结

这个 SPEC 示例展示了：

✅ **完整性**：从需求到部署的所有细节
✅ **明确性**：没有歧义的规格说明
✅ **可测试性**：每个需求都有测试用例
✅ **可实现性**：技术方案清晰可行

**使用方式**：

\```bash
# 1. 开发者读取 SPEC
claude
> 阅读 SPEC.md 的用户注册部分

# 2. Claude 按 SPEC 实现
> 根据 SPEC 实现用户注册功能

# 3. Claude 按 SPEC 测试
> 根据 SPEC 中的测试用例编写测试
\```
\```

---

## 与 Claude Code 配合

### SPEC 优先的开发工作流

#### 第 1 步：创建 SPEC

```bash
claude
> 帮我创建一个用户认证模块的 SPEC，包括注册、登录、登出功能
```

Claude 会：
1. 询问关键需求（技术栈、认证方式等）
2. 生成完整的 SPEC 文档
3. 包含数据模型、API 设计、测试用例

#### 第 2 步：审查和完善 SPEC

```bash
> 检查 SPEC.md 的完整性，特别关注：
> 1. 安全性措施是否充分
> 2. 错误处理是否全面
> 3. 测试用例是否覆盖边界条件
```

#### 第 3 步：基于 SPEC 生成数据模型

```bash
> 根据 SPEC.md 第 4 节，生成 Prisma schema
```

Claude 会：
1. 读取 SPEC 中的数据模型定义
2. 生成符合规范的 Prisma schema
3. 添加索引和约束

#### 第 4 步：基于 SPEC 实现 API

```bash
> 根据 SPEC.md 第 3.1 节，实现用户注册 API
> 严格遵循 SPEC 中的：
> - 输入验证规则
> - 业务逻辑
> - 错误处理
> - 安全措施
```

Claude 会：
1. 读取 SPEC 的详细要求
2. 实现完全符合 SPEC 的代码
3. 包含所有边界条件处理

#### 第 5 步：基于 SPEC 生成测试

```bash
> 根据 SPEC.md 第 3.1.10 节的测试用例，编写完整的单元测试
```

Claude 会：
1. 读取 SPEC 中定义的测试用例
2. 生成可执行的测试代码
3. 覆盖所有正常、边界、异常情况

#### 第 6 步：验证符合 SPEC

```bash
> 运行测试并验证实现是否完全符合 SPEC

/test

> 对比实现和 SPEC，检查是否有遗漏
```

### 自定义 SPEC 命令

创建 `.claude/commands/spec.md`：

```markdown
---
name: spec
description: 基于 SPEC 的开发工作流
aliases: [s, specification]
---

# SPEC 驱动开发

## 使用方式

### 创建 SPEC
\```
/spec create 功能名称
\```

### 实现 SPEC
\```
/spec implement 章节号
\```

### 验证 SPEC
\```
/spec verify 章节号
\```

## 执行步骤

### 1. 创建 SPEC（/spec create）

1. 询问用户：
   - 功能名称
   - 技术栈
   - 关键需求

2. 生成 SPEC 文档：
   - 功能描述
   - 数据模型
   - API 设计
   - 测试用例

3. 写入 `SPEC.md` 或 `docs/spec/功能名.md`

4. 提示用户审查 SPEC

### 2. 实现 SPEC（/spec implement）

1. 读取指定章节的 SPEC

2. 按顺序实现：
   - 数据模型（Prisma schema）
   - 验证逻辑（Zod schema）
   - API 路由
   - 业务逻辑
   - 测试用例

3. 每个步骤完成后：
   - 显示实现的代码
   - 询问是否继续下一步

### 3. 验证 SPEC（/spec verify）

1. 读取 SPEC 和实现代码

2. 验证清单：
   - [ ] 所有输入字段都有验证
   - [ ] 所有输出格式符合 SPEC
   - [ ] 所有错误码都已定义
   - [ ] 所有测试用例都已实现
   - [ ] 性能要求已满足
   - [ ] 安全措施已到位

3. 生成验证报告

4. 列出不符合项（如有）
```

使用：

```bash
# 创建 SPEC
> /spec create 用户认证

# 实现 SPEC
> /spec implement 3.1

# 验证实现
> /spec verify 3.1
```

---

## 最佳实践

### 1. SPEC 编写原则

#### ✅ 好的 SPEC

```markdown
**密码规则**：
- 长度：8-32 字符
- 必须包含：至少 1 个大写字母、1 个小写字母、1 个数字
- 可选：特殊字符 (!@#$%^&*)
- 禁止：常见弱密码列表（见附录）

**验证方法**：
\```javascript
/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d!@#$%^&*]{8,32}$/
\```
```

#### ❌ 不好的 SPEC

```markdown
**密码规则**：
- 密码要足够安全
- 不能太短也不能太长
- 要有字母和数字
```

**问题**：
- "足够安全" 太模糊
- "不能太短" 没有具体数字
- "要有字母和数字" 没说大小写要求

### 2. 测试用例覆盖

每个功能至少需要：

1. **正常流程**（Happy Path）
   ```javascript
   test('成功注册新用户')
   ```

2. **边界条件**
   ```javascript
   test('密码最小长度 8 字符')
   test('密码最大长度 32 字符')
   test('邮箱最大长度 255 字符')
   ```

3. **异常情况**
   ```javascript
   test('拒绝重复邮箱')
   test('拒绝弱密码')
   test('拒绝无效邮箱格式')
   ```

4. **安全测试**
   ```javascript
   test('防止 SQL 注入')
   test('频率限制生效')
   test('密码哈希安全')
   ```

### 3. SPEC 维护

#### 版本控制

```bash
# SPEC 提交规范
git commit -m "spec: 添加用户认证模块 v1.0"
git commit -m "spec: 更新密码策略 v1.1"
git commit -m "spec: 修复邮箱验证说明 v1.0.1"
```

#### 变更追踪

在 SPEC 开头添加变更历史：

```markdown
## 变更历史

### v1.1.0 - 2025-01-15
- 添加：OAuth 第三方登录
- 修改：密码最小长度从 8 改为 10

### v1.0.1 - 2025-01-12
- 修复：明确邮箱大小写不敏感规则

### v1.0.0 - 2025-01-10
- 初始版本
```

### 4. SPEC 和代码同步

#### 同步检查清单

- [ ] SPEC 更新后，代码已同步更新
- [ ] 代码更新后，SPEC 已同步更新
- [ ] 测试用例与 SPEC 一致
- [ ] API 文档与 SPEC 一致
- [ ] 变更记录在 CHANGELOG

#### 自动化检查

创建 `.claude/commands/spec-sync.md`：

```markdown
---
name: spec-sync
description: 检查 SPEC 和代码是否同步
---

# SPEC 同步检查

## 执行步骤

1. 读取 SPEC.md
2. 读取相关代码文件
3. 比对：
   - API 端点是否匹配
   - 输入字段是否一致
   - 输出格式是否符合
   - 错误码是否定义
   - 测试用例是否覆盖
4. 生成同步报告
5. 列出不一致项
```

---

## 常见问题

### Q1: SPEC 要写多详细？

**回答**：详细到可以无歧义地实现。

**判断标准**：
- ✅ 给两个开发者看 SPEC，实现结果应该一致
- ✅ Claude 读 SPEC 后，无需追问就能实现
- ✅ 测试工程师看 SPEC，能直接写出测试用例

### Q2: SPEC 太长怎么办？

**解决方案**：
1. **分模块**：每个模块独立 SPEC 文件
   ```
   docs/spec/
   ├── auth.md          # 认证模块
   ├── user.md          # 用户模块
   └── payment.md       # 支付模块
   ```

2. **分层次**：
   - `SPEC.md` - 概述和总体设计
   - `docs/spec/详细/` - 详细规格

3. **使用模板**：重复的结构使用模板

### Q3: 需求经常变怎么办？

**SPEC 优势**：
- 变更点明确：只需更新 SPEC 对应章节
- 影响范围清晰：看 SPEC 依赖关系
- 代码更新准确：严格按新 SPEC 修改

**流程**：
```
需求变更 → 评估影响 → 更新 SPEC → 审查 SPEC → 更新代码 → 更新测试
```

### Q4: 写 SPEC 是否浪费时间？

**数据对比**：

| 项目阶段 | 无 SPEC | 有 SPEC |
|---------|---------|---------|
| 需求澄清 | 2 小时（多轮沟通） | 30 分钟 |
| 编码时间 | 6 小时（反复修改） | 4 小时 |
| 测试时间 | 3 小时（边测边改） | 1 小时 |
| Bug 修复 | 4 小时 | 1 小时 |
| **总计** | **15 小时** | **6.5 小时** |

**节省时间 57%**

### Q5: 团队不习惯写 SPEC？

**推进策略**：

1. **小步开始**：先对核心模块写 SPEC
2. **展示效果**：对比有无 SPEC 的开发效率
3. **提供模板**：降低编写门槛
4. **工具支持**：使用 Claude 辅助生成 SPEC
5. **纳入流程**：PR 审查时检查 SPEC

---

## 总结

### SPEC 范式的价值

1. **提高效率**：减少返工，节省 40%+ 开发时间
2. **提升质量**：完整覆盖，减少 70% 的 bug
3. **团队协作**：统一理解，减少沟通成本
4. **AI 友好**：Claude 精确实现，一次到位
5. **易于维护**：文档驱动，变更有据可查

### 核心原则

✅ **先文档后代码**
✅ **SPEC 必须明确无歧义**
✅ **测试用例在 SPEC 中定义**
✅ **代码严格符合 SPEC**
✅ **SPEC 和代码同步更新**

### 立即开始

```bash
# 1. 为你的下一个功能创建 SPEC
claude
> 创建一个支付模块的 SPEC

# 2. 让 Claude 按 SPEC 实现
> 根据 SPEC.md 实现支付功能

# 3. 按 SPEC 测试
> 根据 SPEC 编写测试用例

# 4. 验证符合 SPEC
> /test
```

**开始使用 SPEC 范式，让开发更高效、更可靠！** 🚀
