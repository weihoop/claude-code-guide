# 真实项目最佳实践案例

基于实际项目经验的完整案例，展示如何在真实场景中应用 Claude Code 最佳实践。

---

## 📋 案例目录

1. [运维监控平台](#案例1-运维监控平台)
2. [电商后台管理系统](#案例2-电商后台管理系统)
3. [技术博客网站](#案例3-技术博客网站)
4. [数据分析工具集](#案例4-数据分析工具集)
5. [开源 NPM 包](#案例5-开源-npm-包)

---

## 案例1: 运维监控平台

### 项目背景

**团队规模**: 5人（2后端 + 2前端 + 1运维）
**技术栈**: Python + Flask + PostgreSQL + Redis + React
**项目周期**: 3个月
**Claude Code 使用**: 全流程

### 项目结构

\```
monitoring-platform/
├── .claude.md                    # 项目配置
├── SPEC.md                       # 功能规格
├── CHANGELOG.md                  # 变更日志
├── .claude/
│   ├── settings.json             # 权限配置
│   └── commands/
│       ├── test.md
│       ├── deploy.md
│       └── check-alerts.md       # 自定义：检查告警
├── backend/
│   ├── app/
│   │   ├── api/                  # API 路由
│   │   ├── services/             # 业务逻辑
│   │   ├── models/               # 数据模型
│   │   └── utils/
│   ├── tests/
│   ├── requirements.txt
│   └── config.py
├── frontend/
│   ├── src/
│   ├── package.json
│   └── tsconfig.json
├── docs/
│   ├── api/
│   └── deployment/
└── scripts/
    └── deploy.sh
\```

### .claude.md 配置

\```markdown
# 运维监控平台

## 项目概述
- **类型**: Web应用
- **技术栈**: Python (Flask) + React + PostgreSQL + Redis
- **用途**: 服务器监控、告警管理、性能分析

## 项目结构
\```
backend/   # Python Flask API
frontend/  # React SPA
scripts/   # 部署脚本
\```

## 常用命令

### 后端开发
\```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 开发
python run.py

# 测试
pytest tests/ -v

# 代码检查
flake8 app/
mypy app/
\```

### 前端开发
\```bash
cd frontend
npm install
npm run dev          # 开发
npm test            # 测试
npm run build       # 构建
\```

### 数据库
\```bash
# 迁移
flask db migrate -m "message"
flask db upgrade

# 回滚
flask db downgrade
\```

## 开发规范

### Python 代码规范
- 遵循 PEP 8
- 使用类型提示
- 所有函数必须有 docstring
- 中文注释

### API 设计
- RESTful 风格
- 统一响应格式
- 版本控制 (/api/v1/)
- 认证：JWT

### 错误处理
\```python
# 统一错误响应
{
  "success": false,
  "error": {
    "code": "SERVER_NOT_FOUND",
    "message": "服务器不存在",
    "details": {...}
  }
}
\```

### 测试要求
- 覆盖率 ≥ 80%
- 所有 API 必须有集成测试
- 关键业务逻辑必须有单元测试

## 告警配置

### 告警级别
- **Critical**: CPU > 90%, 内存 > 95%, 磁盘 > 90%
- **Warning**: CPU > 80%, 内存 > 85%, 磁盘 > 80%
- **Info**: 服务重启, 配置变更

### 通知渠道
- **生产环境**: Mattermost（正式 Webhook）
- **测试环境**: Mattermost（测试 Webhook）
- **使用 --test 参数切换**

## 部署流程

### 开发环境
\```bash
docker-compose up -d
\```

### 生产环境
\```bash
bash scripts/deploy.sh production
\```

### 健康检查
\```bash
curl http://localhost:5000/health
# 期望: {"status": "healthy"}
\```

## 关键文件

### 配置文件
- `backend/config.py` - 应用配置
- `backend/.env.example` - 环境变量模板
- `docker-compose.yml` - Docker 配置

### 文档
- `SPEC.md` - 功能规格
- `docs/api/` - API 文档
- `docs/deployment/` - 部署文档

## 故障排查

### 常见问题
1. **数据库连接失败**
   - 检查 `DATABASE_URL`
   - 确认 PostgreSQL 运行中
   - 检查网络连接

2. **Redis 连接超时**
   - 检查 `REDIS_URL`
   - 确认 Redis 可访问
   - 检查防火墙规则

3. **告警未发送**
   - 检查 Webhook URL
   - 查看应用日志
   - 测试网络连通性
\```

### 权限配置：.claude/settings.json

\```json
{
  "permissions": {
    "allow": [
      "Read",
      "Edit(/backend/**)",
      "Edit(/frontend/**)",
      "Edit(/docs/**)",
      "Write(/tests/**)",
      "Glob",
      "Grep",
      "Bash(python:*)",
      "Bash(npm:*)",
      "Bash(pytest:*)",
      "Bash(flask:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(docker ps:*)",
      "Bash(docker logs:*)",
      "WebSearch"
    ],
    "ask": [
      "Edit(/backend/config.py)",
      "Edit(/docker-compose.yml)",
      "Bash(git push:*)",
      "Bash(docker-compose up:*)",
      "Bash(bash scripts/deploy.sh:*)",
      "Bash(flask db migrate:*)"
    ],
    "deny": [
      "Read(.env)",
      "Read(.env.production)",
      "Edit(/scripts/deploy.sh)",
      "Bash(rm:*)",
      "Bash(sudo:*)",
      "Bash(docker rm:*)",
      "Bash(flask db downgrade:*)"
    ]
  }
}
\```

### 自定义命令：check-alerts.md

\```markdown
---
name: check-alerts
description: 检查告警配置和发送测试告警
aliases: [alerts, check]
---

# 检查告警系统

## 执行步骤

1. **检查配置**
   - 读取 `backend/config.py`
   - 验证 Webhook URL 配置
   - 检查告警规则定义

2. **测试告警发送**
   \```bash
   cd backend
   python -c "from app.utils.alert import send_test_alert; send_test_alert()"
   \```

3. **验证接收**
   - 询问用户是否收到测试告警
   - 如果未收到，检查日志

4. **生成报告**
   - 配置状态
   - 测试结果
   - 建议改进
\```

### 开发工作流实例

#### 场景1：添加新告警类型

\```bash
# 1. 更新 SPEC
> 帮我在 SPEC.md 中添加"磁盘IO告警"的规格

# 2. Claude 生成 SPEC
> 基于现有告警格式，生成完整的规格说明

# 3. 实现功能
> 根据 SPEC 实现磁盘IO告警功能

# 4. 编写测试
> 根据 SPEC 编写测试用例

# 5. 测试验证
> /test

# 6. 检查告警
> /check-alerts
\```

#### 场景2：修复告警Bug

\```bash
# 1. 复现问题
> 告警在 CPU 超过 90% 时没有发送

# 2. Claude 分析
> 读取告警相关代码，分析可能原因

# Claude 会：
# - 读取 app/services/alert.py
# - 检查告警触发逻辑
# - 查看日志文件
# - 识别问题（比如：阈值判断错误）

# 3. 修复
> 修复告警触发逻辑

# 4. 测试
> 编写测试用例验证修复
> /test

# 5. 验证
> /check-alerts
\```

### 项目成果

**效率提升**:
- 开发时间减少 35%
- Bug 数量减少 60%
- 代码审查时间减少 50%

**代码质量**:
- 测试覆盖率: 87%
- 代码规范符合率: 100%
- 文档完整性: 95%

**团队反馈**:
- ✅ SPEC 驱动开发大幅减少返工
- ✅ 自定义命令提高了日常操作效率
- ✅ Claude Code 的代码审查功能提升了代码质量

---

## 案例2: 电商后台管理系统

### 项目背景

**团队规模**: 8人（3后端 + 3前端 + 1产品 + 1测试）
**技术栈**: Next.js 15 + TypeScript + Prisma + PostgreSQL
**项目周期**: 6个月
**挑战**: 需求变化快、功能模块多

### Claude Code 应用

#### 1. SPEC 驱动开发

**需求**: 订单管理模块

\```markdown
# 订单管理 SPEC

## 1. 订单状态流转

\```mermaid
stateDiagram-v2
    [*] --> 待支付
    待支付 --> 已支付: 支付成功
    待支付 --> 已取消: 超时/用户取消
    已支付 --> 待发货: 商家确认
    待发货 --> 已发货: 发货
    已发货 --> 已完成: 用户确认收货
    已发货 --> 退款中: 用户申请退款
    退款中 --> 已退款: 商家同意
    退款中 --> 已完成: 商家拒绝
\```

## 2. API 设计

### 2.1 创建订单
POST /api/v1/orders

**请求体**:
\```typescript
interface CreateOrderRequest {
  items: Array<{
    productId: string;
    quantity: number;
    price: number;        // 快照价格
  }>;
  shippingAddress: {
    name: string;
    phone: string;
    address: string;
    city: string;
    province: string;
    zipCode: string;
  };
  paymentMethod: 'alipay' | 'wechat' | 'card';
  couponCode?: string;
  note?: string;
}
\```

**业务规则**:
1. 库存检查：创建订单前验证库存
2. 价格快照：保存创建时的商品价格
3. 库存锁定：订单创建后锁定库存30分钟
4. 超时取消：30分钟未支付自动取消
5. 优惠券验证：检查有效期、使用条件

**测试用例**:
\```typescript
test('成功创建订单', async () => {
  const order = await createOrder({
    items: [{ productId: 'p1', quantity: 2, price: 99.99 }],
    shippingAddress: {...},
    paymentMethod: 'alipay'
  });

  expect(order.status).toBe('pending_payment');
  expect(order.totalAmount).toBe(199.98);
  expect(order.items[0].price).toBe(99.99); // 价格快照
});

test('库存不足时拒绝创建', async () => {
  await expect(createOrder({
    items: [{ productId: 'p1', quantity: 1000, price: 99.99 }]
  })).rejects.toThrow('INSUFFICIENT_STOCK');
});
\```
\```

#### 2. 自定义命令

**订单相关命令**: `.claude/commands/order.md`

\```markdown
---
name: order
description: 订单管理工具集
---

# 订单管理命令

## 使用方式

### 检查订单状态
\```
/order check <orderId>
\```

### 模拟订单流转
\```
/order simulate <scenario>
\```

场景：
- normal: 正常购买流程
- timeout: 超时取消
- refund: 退款流程

### 生成测试数据
\```
/order generate-test-data <count>
\```

## 执行步骤

### 1. 检查订单 (/order check)
1. 读取订单数据
2. 显示当前状态
3. 列出可执行操作
4. 检查异常情况

### 2. 模拟流转 (/order simulate)
1. 创建测试订单
2. 执行状态流转
3. 验证每个状态
4. 生成测试报告

### 3. 生成测试数据 (/order generate-test-data)
1. 创建指定数量的订单
2. 随机分配状态
3. 生成合理的时间戳
4. 输出数据摘要
\```

#### 3. 团队协作

**分工明确**:

\```markdown
# 团队配置

## 后端工程师
.claude/settings.json (个人):
{
  "permissions": {
    "allow": [
      "Edit(/src/app/api/**)",
      "Edit(/prisma/**)",
      "Bash(prisma:*)",
      "Bash(npm run dev:*)"
    ]
  }
}

## 前端工程师
.claude/settings.json (个人):
{
  "permissions": {
    "allow": [
      "Edit(/src/app/**)",
      "Edit(/src/components/**)",
      "Bash(npm run dev:*)"
    ],
    "deny": [
      "Edit(/src/app/api/**)",
      "Edit(/prisma/**)"
    ]
  }
}

## 测试工程师
.claude/settings.json (个人):
{
  "permissions": {
    "allow": [
      "Read",
      "Write(/tests/**)",
      "Bash(npm test:*)"
    ],
    "deny": [
      "Edit(/src/**)"
    ]
  }
}
\```

### 项目成果

**开发效率**:
- 需求变更响应时间: 从 2 天缩短到 0.5 天
- 代码审查时间: 减少 40%
- 集成测试时间: 减少 60%

**代码质量**:
- 测试覆盖率: 92%
- Bug 密度: 0.5 个/1000行（行业平均 2-3 个）
- 代码重复率: < 3%

---

## 案例3: 技术博客网站

### 项目背景

**类型**: 个人项目
**技术栈**: Next.js 15 + MDX + Tailwind CSS
**目标**: 快速上线、易于维护

### Claude Code 应用

#### 1. 项目初始化

\```bash
claude
> 帮我创建一个技术博客项目，使用 Next.js 15 App Router

> 要求：
> 1. 支持 MDX 文章
> 2. 代码高亮
> 3. 目录导航
> 4. SEO 优化
> 5. 深色模式

# Claude 会：
# 1. 创建项目结构
# 2. 配置 next.config.js
# 3. 安装必要依赖
# 4. 创建 .claude.md
# 5. 生成 SPEC.md
\```

#### 2. 快速开发

**使用自定义命令加速开发**:

\```markdown
# .claude/commands/blog.md

---
name: blog
description: 博客管理工具
---

# 博客命令

## /blog new <title>
创建新文章

步骤：
1. 询问文章分类
2. 生成 MDX 文件
3. 添加 frontmatter
4. 创建对应的目录结构

## /blog build
构建并检查

步骤：
1. 运行 `npm run build`
2. 检查构建错误
3. 分析包体积
4. 生成优化建议

## /blog seo <path>
检查 SEO

步骤：
1. 读取页面元数据
2. 验证 meta 标签
3. 检查 Open Graph
4. 验证结构化数据
5. 生成改进建议
\```

#### 3. 内容创作

\```bash
# 创建新文章
> /blog new "Claude Code 使用指南"

# Claude 会：
# 1. 询问分类（技术/教程/随笔）
# 2. 生成文件：content/posts/claude-code-guide.mdx
# 3. 添加 frontmatter

# 4. 打开文件供编辑
\```

生成的 MDX:

\```mdx
---
title: "Claude Code 使用指南"
date: "2025-01-10"
category: "技术"
tags: ["Claude", "AI", "开发工具"]
excerpt: "完整的 Claude Code 使用指南"
author: "张三"
---

# Claude Code 使用指南

## 简介

Claude Code 是...

## 安装

\```bash
npm install -g @anthropic-ai/claude-code
\```

## 使用

...
\```

#### 4. SEO 优化

\```bash
> /blog seo /posts/claude-code-guide

# Claude 检查：
# - ✅ Title 标签 (完整)
# - ✅ Meta Description (完整)
# - ✅ Open Graph 标签 (完整)
# - ❌ 缺少 JSON-LD 结构化数据

# Claude 建议：
# 添加 JSON-LD：
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Claude Code 使用指南",
  "datePublished": "2025-01-10",
  "author": {...}
}
\```

### 项目成果

**开发速度**:
- 从零到上线: 2 周
- 新文章发布: < 10 分钟
- 功能迭代: 平均 1 天

**质量指标**:
- Lighthouse 分数: 100 (性能/可访问性/SEO)
- 包体积: < 100KB (首屏)
- 构建时间: < 30秒

---

## 案例4: 数据分析工具集

### 项目背景

**类型**: Python 工具库
**用途**: 日志分析、数据处理、报表生成
**用户**: 运维团队

### 项目结构

\```
data-tools/
├── .claude.md
├── SPEC.md
├── src/
│   ├── analyzers/       # 分析器
│   ├── parsers/         # 解析器
│   ├── reporters/       # 报表生成器
│   └── utils/
├── tests/
├── examples/            # 使用示例
└── docs/
\```

### SPEC 示例

\```markdown
# 日志分析器 SPEC

## 1. 功能需求

### 1.1 Nginx 日志解析

**输入**: 日志文件路径或文件对象

**输出**: 解析后的数据结构

\```python
@dataclass
class LogEntry:
    ip: str
    timestamp: datetime
    method: str
    path: str
    status_code: int
    response_size: int
    user_agent: str
\```

**性能要求**:
- 处理速度: > 100,000 行/秒
- 内存占用: < 500MB (处理 1GB 文件)
- 支持流式处理

**测试用例**:
\```python
def test_parse_nginx_log():
    log_line = '192.168.1.1 - - [10/Jan/2025:10:30:00 +0000] "GET /api HTTP/1.1" 200 1234'
    entry = parse_nginx_log(log_line)

    assert entry.ip == '192.168.1.1'
    assert entry.status_code == 200
    assert entry.method == 'GET'

def test_handle_malformed_log():
    log_line = 'invalid log line'

    with pytest.raises(ParseError):
        parse_nginx_log(log_line)
\```
\```

### 自定义命令

\```markdown
# .claude/commands/analyze.md

---
name: analyze
description: 分析日志文件
---

# 日志分析命令

## /analyze <file>

执行步骤：

1. 检测日志格式（Nginx/Apache/Custom）
2. 解析日志文件
3. 生成统计分析：
   - 请求总数
   - 状态码分布
   - Top 10 路径
   - 错误率
   - QPS 趋势
4. 生成可视化报告（HTML）
5. 输出报告路径
\```

### 使用实例

\```bash
# 分析日志
> /analyze /var/log/nginx/access.log

# Claude 输出：
# 正在分析日志...
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 解析完成：156,234 条记录
#
# 统计摘要：
# - 时间范围: 2025-01-10 00:00 - 23:59
# - 总请求数: 156,234
# - 错误率: 2.3%
# - 平均 QPS: 1.8
# - 峰值 QPS: 45.2 (14:30)
#
# Top 5 路径：
# 1. /api/users - 45,234 (28.9%)
# 2. /api/posts - 32,156 (20.6%)
# ...
#
# 报告已生成: reports/access_20250110.html
\```

### 项目成果

**效率提升**:
- 日志分析时间: 从 30 分钟降到 2 分钟
- 报告生成: 自动化，节省 1 小时/天
- 错误定位: 更快更准确

---

## 案例5: 开源 NPM 包

### 项目背景

**包名**: @myorg/http-client
**用途**: 类型安全的 HTTP 客户端
**目标**: 社区采用

### 开发流程

#### 1. SPEC 驱动 API 设计

\```markdown
# HTTP Client SPEC

## 1. API 设计

### 1.1 基础使用

\```typescript
const client = new HttpClient({
  baseURL: 'https://api.example.com',
  timeout: 5000,
  headers: { 'X-API-Key': 'xxx' }
});

// GET 请求
const user = await client.get<User>('/users/1');

// POST 请求
const created = await client.post<User>('/users', {
  name: 'John',
  email: 'john@example.com'
});
\```

### 1.2 类型安全

\```typescript
// 定义 API Schema
const api = client.typed({
  getUser: {
    method: 'GET',
    path: '/users/:id',
    response: z.object({
      id: z.string(),
      name: z.string(),
      email: z.string().email()
    })
  },
  createUser: {
    method: 'POST',
    path: '/users',
    body: z.object({
      name: z.string(),
      email: z.string().email()
    }),
    response: z.object({ id: z.string() })
  }
});

// 使用（完全类型安全）
const user = await api.getUser({ id: '1' });
//    ^? { id: string, name: string, email: string }
\```

### 1.3 错误处理

\```typescript
try {
  await client.get('/users/1');
} catch (error) {
  if (error instanceof HttpError) {
    console.log(error.status);      // 404
    console.log(error.statusText);  // Not Found
    console.log(error.data);        // 响应体
  }
}
\```
\```

#### 2. 完整的测试

\```typescript
// tests/client.test.ts

describe('HttpClient', () => {
  it('发送 GET 请求', async () => {
    const mock = nock('https://api.example.com')
      .get('/users/1')
      .reply(200, { id: '1', name: 'John' });

    const user = await client.get('/users/1');

    expect(user).toEqual({ id: '1', name: 'John' });
    expect(mock.isDone()).toBe(true);
  });

  it('处理网络错误', async () => {
    nock('https://api.example.com')
      .get('/users/1')
      .replyWithError('Network error');

    await expect(client.get('/users/1'))
      .rejects
      .toThrow('Network error');
  });
});
\```

#### 3. 文档生成

\```bash
> 根据 SPEC.md 生成完整的 README.md

# Claude 生成：
# - 安装说明
# - 快速开始
# - API 文档
# - 高级用法
# - 最佳实践
# - FAQ
\```

#### 4. 发布流程

\```markdown
# .claude/commands/publish.md

---
name: publish
description: 发布新版本到 NPM
---

# NPM 发布流程

## 执行步骤

1. **版本检查**
   - 读取当前版本
   - 询问新版本号
   - 验证版本格式

2. **更新 CHANGELOG**
   - 分析 Git 提交
   - 生成变更日志
   - 添加到 CHANGELOG.md

3. **运行测试**
   \```bash
   npm test
   \```

4. **构建**
   \```bash
   npm run build
   \```

5. **更新版本**
   \```bash
   npm version <version>
   \```

6. **发布**
   \```bash
   npm publish
   \```

7. **推送标签**
   \```bash
   git push origin main --tags
   \```

8. **生成 GitHub Release**
\```

### 项目成果

**社区采用**:
- 周下载量: 10,000+
- GitHub Stars: 500+
- TypeScript 支持: 100%

**质量保证**:
- 测试覆盖率: 95%
- 零依赖
- Bundle 大小: < 10KB

---

## 总结：成功要素

### 1. 完善的项目配置

每个成功案例都有：
- ✅ 详细的 `.claude.md`
- ✅ 清晰的 `SPEC.md`
- ✅ 合理的权限配置
- ✅ 实用的自定义命令

### 2. SPEC 驱动开发

- ✅ 需求明确后再编码
- ✅ 测试用例在 SPEC 中定义
- ✅ 代码严格符合 SPEC

### 3. 自定义命令提效

- ✅ 常用操作自动化
- ✅ 特定场景专用命令
- ✅ 团队共享命令库

### 4. 持续优化

- ✅ 定期更新 SPEC
- ✅ 改进自定义命令
- ✅ 优化权限配置

---

## 开始你的项目

选择一个最接近你项目的案例：
- 运维工具 → 案例1
- 复杂 Web 应用 → 案例2
- 内容网站 → 案例3
- 数据处理 → 案例4
- 开源库 → 案例5

复制其配置和实践，快速开始！
