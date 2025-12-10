---
name: deploy
description: 自动化部署到指定环境
aliases: [d, publish, release]
---

# 自动化部署流程

安全、可靠地将应用部署到开发、测试或生产环境。

## 执行步骤

### 1. 确定部署环境

询问用户要部署到哪个环境：

**可用环境**:
- 🔵 `dev` - 开发环境
- 🟡 `staging` - 测试/预发布环境
- 🔴 `production` - 生产环境

**示例**:
```
用户: /deploy
Claude: 请选择部署环境：
  1. dev (开发环境)
  2. staging (测试环境)
  3. production (生产环境) ⚠️

用户: production
Claude: ⚠️ 警告：即将部署到生产环境！
       是否确认？(yes/no)
```

### 2. 预检查

在部署前执行安全检查：

#### Git 状态检查

```bash
# 检查当前分支
git branch --show-current

# 检查未提交的改动
git status --porcelain
```

验证规则：

| 环境 | 允许的分支 | 未提交改动 |
|------|-----------|-----------|
| dev | 任意 | ✅ 允许 |
| staging | develop, release/* | ❌ 不允许 |
| production | main, master | ❌ 不允许 |

**检查结果**:

```markdown
## 预检查结果

### Git 状态 ✅

- 当前分支：main
- 未提交改动：无
- 与远程同步：是

### 分支验证 ✅

- 生产环境要求：main 或 master
- 当前分支：main ✅

### 代码状态 ✅

- 工作区：干净
- 暂存区：无文件
- 未跟踪文件：0 个
```

#### 测试检查

```bash
# 运行测试
npm test
```

要求：
- dev: 可选
- staging: 建议
- production: **必须通过**

#### 构建检查

```bash
# 执行构建
npm run build
```

要求：
- 所有环境：**必须成功**

检查结果：

```markdown
## 预检查总结

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Git 状态 | ✅ | 干净的工作区 |
| 分支验证 | ✅ | 在 main 分支 |
| 测试 | ✅ | 48/48 通过 |
| 构建 | ✅ | 成功 |
| Lint | ✅ | 无错误 |

所有检查通过，可以继续部署 ✅
```

### 3. 版本管理

对于 staging 和 production 环境，更新版本号：

```bash
# 自动更新版本
npm version patch  # 补丁版本 (x.x.X)
npm version minor  # 次版本 (x.X.0)
npm version major  # 主版本 (X.0.0)
```

询问用户版本类型：

```
当前版本：1.2.3

选择版本更新类型：
1. patch (1.2.3 → 1.2.4) - Bug 修复
2. minor (1.2.3 → 1.3.0) - 新功能
3. major (1.2.3 → 2.0.0) - 破坏性变更
4. 自定义版本号

用户选择：patch

✅ 版本更新：1.2.3 → 1.2.4
```

### 4. 构建部署包

根据环境构建相应的包：

```bash
# 开发环境
npm run build:dev

# 测试环境
npm run build:staging

# 生产环境
npm run build:prod
```

构建完成后验证：

```markdown
## 构建结果

**环境**: production
**版本**: 1.2.4
**构建时间**: 2025-11-30 16:00:00

### 构建产物

- dist/ (1.2 MB)
  - index.html (3.5 KB)
  - main.js (856 KB, gzip: 312 KB)
  - vendor.js (245 KB, gzip: 89 KB)
  - assets/ (180 KB)

### 优化效果

| 指标 | 值 | 状态 |
|------|-----|------|
| Bundle 大小 | 1.2 MB | ✅ |
| Gzip 后 | 401 KB | ✅ |
| 加载时间估算 | 2.3s (4G) | ✅ |

构建完成 ✅
```

### 5. 执行部署

根据项目配置执行相应的部署命令：

#### 部署方式

**方式 A: npm scripts**
```bash
npm run deploy:dev
npm run deploy:staging
npm run deploy:prod
```

**方式 B: 云服务平台**

**Vercel**:
```bash
vercel --prod
```

**Netlify**:
```bash
netlify deploy --prod
```

**AWS S3**:
```bash
aws s3 sync dist/ s3://my-bucket --delete
aws cloudfront create-invalidation --distribution-id XXX --paths "/*"
```

**Docker**:
```bash
docker build -t myapp:1.2.4 .
docker tag myapp:1.2.4 registry.example.com/myapp:1.2.4
docker push registry.example.com/myapp:1.2.4
kubectl set image deployment/myapp myapp=registry.example.com/myapp:1.2.4
```

**方式 C: CI/CD 触发**
```bash
# 推送标签触发 CI/CD
git tag v1.2.4
git push origin v1.2.4
```

#### 部署进度

实时显示部署状态：

```
🚀 开始部署到 production...

[1/6] 上传构建产物... ✅ (3.2s)
[2/6] 部署到服务器... ✅ (8.5s)
[3/6] 更新配置文件... ✅ (1.2s)
[4/6] 重启服务... ⏳
[5/6] 健康检查...
[6/6] 清理旧版本...
```

### 6. 健康检查

部署完成后验证服务状态：

```bash
# HTTP 健康检查
curl -f https://api.example.com/health

# 检查特定端点
curl https://api.example.com/api/version
```

健康检查结果：

```markdown
## 健康检查结果

### 服务状态 ✅

- 健康检查：通过
- 响应时间：145ms
- HTTP 状态：200 OK

### 版本验证 ✅

- 部署版本：1.2.4
- 当前版本：1.2.4 ✅

### 功能验证 ✅

- [ ] 主页加载：正常 ✅
- [ ] API 响应：正常 ✅
- [ ] 数据库连接：正常 ✅
- [ ] 缓存服务：正常 ✅
- [ ] 静态资源：正常 ✅

### 性能指标

| 指标 | 值 | 状态 |
|------|-----|------|
| 响应时间 | 145ms | ✅ |
| 成功率 | 100% | ✅ |
| CPU 使用 | 12% | ✅ |
| 内存使用 | 256MB/1GB | ✅ |

部署验证通过 ✅
```

### 7. 更新记录

#### Git 标签

为生产部署创建 Git 标签：

```bash
git tag -a v1.2.4 -m "Release version 1.2.4"
git push origin v1.2.4
```

#### 部署日志

```bash
# 记录部署信息
echo "$(date): Deployed v1.2.4 to production" >> deployments.log
```

#### 通知团队

发送部署通知（如果配置了通知工具）：

```markdown
## 部署通知

📦 **新版本部署成功**

**环境**: Production
**版本**: v1.2.4
**时间**: 2025-11-30 16:05:32
**部署者**: @username
**耗时**: 35 秒

**变更内容**:
- 修复用户登录问题
- 优化查询性能
- 更新依赖版本

**验证结果**: 所有检查通过 ✅

**回滚命令** (如需要):
```bash
/deploy production --rollback v1.2.3
```
```

### 8. 生成部署报告

```markdown
## 部署完整报告

**部署编号**: #1234
**执行时间**: 2025-11-30 16:00:00 - 16:05:32
**总耗时**: 5分32秒

### 基本信息

| 项目 | 值 |
|------|-----|
| 环境 | Production |
| 版本 | 1.2.3 → 1.2.4 |
| 分支 | main |
| 提交 | abc1234 |
| 部署者 | username |

### 部署时间线

| 时间 | 阶段 | 耗时 | 状态 |
|------|------|------|------|
| 16:00:00 | 预检查 | 12s | ✅ |
| 16:00:12 | 版本更新 | 3s | ✅ |
| 16:00:15 | 构建 | 48s | ✅ |
| 16:01:03 | 上传 | 15s | ✅ |
| 16:01:18 | 部署 | 120s | ✅ |
| 16:03:18 | 健康检查 | 30s | ✅ |
| 16:03:48 | 验证 | 45s | ✅ |
| 16:04:33 | 清理 | 8s | ✅ |
| 16:04:41 | 通知 | 2s | ✅ |

**总计**: 5分32秒

### 变更内容

**本次部署包含 5 个提交**:

1. `abc1234` - fix: 修复用户登录问题
2. `def5678` - perf: 优化数据库查询性能
3. `ghi9012` - chore: 更新依赖到最新版本
4. `jkl3456` - docs: 更新 API 文档
5. `mno7890` - test: 添加集成测试用例

### 影响范围

**修改的文件**: 23 个
- 源代码：15 个
- 测试文件：5 个
- 配置文件：2 个
- 文档：1 个

**新增功能**: 0 个
**Bug 修复**: 2 个
**性能优化**: 1 个

### 验证结果

**自动化测试**:
- 单元测试：48/48 通过 ✅
- 集成测试：12/12 通过 ✅
- E2E 测试：8/8 通过 ✅

**健康检查**:
- 服务状态：正常 ✅
- API 响应：正常 ✅
- 数据库：正常 ✅
- 缓存：正常 ✅

**性能指标**:
- 响应时间：145ms (优于基线 200ms) ✅
- 错误率：0% ✅
- 可用性：100% ✅

### 回滚准备

**回滚命令**:
```bash
/deploy production --rollback v1.2.3
```

**回滚时间估算**: ~2 分钟

**备份位置**:
- 代码：Git tag v1.2.3
- 数据库：backup_20251130_1600.sql
- 配置：config_v1.2.3.tar.gz

### 监控链接

- 📊 [应用监控](https://monitoring.example.com/app)
- 📈 [性能仪表板](https://metrics.example.com/dashboard)
- 🔍 [日志查询](https://logs.example.com)
- 🚨 [告警中心](https://alerts.example.com)

### 后续任务

- [ ] 监控生产环境 2 小时
- [ ] 检查错误日志
- [ ] 验证新功能
- [ ] 更新 CHANGELOG
- [ ] 通知客户（如适用）

### 部署成功 ✅

生产环境已成功更新到版本 1.2.4
```

## 部署策略

### 1. 蓝绿部署

```
旧版本 (蓝) ─→ 负载均衡器 ←─ 用户
新版本 (绿) ─→ 准备就绪

切换后:
旧版本 (蓝) ─→ 待机
新版本 (绿) ─→ 负载均衡器 ←─ 用户
```

优点：
- 零停机时间
- 快速回滚
- 完整测试

### 2. 金丝雀发布

```
10% 流量 → 新版本 v1.2.4
90% 流量 → 旧版本 v1.2.3

逐步增加:
50% 流量 → 新版本
100% 流量 → 新版本
```

优点：
- 渐进式部署
- 风险可控
- 易于监控

### 3. 滚动更新

```
实例 1: v1.2.3 → v1.2.4 ✅
实例 2: v1.2.3 → v1.2.4 ✅
实例 3: v1.2.3 → v1.2.4 ✅
```

优点：
- 逐步更新
- 始终保持可用
- 资源利用高

## 回滚流程

### 快速回滚

```bash
/deploy production --rollback v1.2.3
```

或手动回滚：

```bash
# Git 回滚
git revert HEAD
git push origin main

# 容器回滚
kubectl rollout undo deployment/myapp

# 云服务回滚
vercel rollback
netlify rollback
```

### 回滚验证

```markdown
## 回滚验证

✅ 已回滚到版本：v1.2.3
✅ 服务状态：正常
✅ 健康检查：通过
✅ 数据完整性：正常
```

## 环境配置示例

### 开发环境 (dev)

```bash
# .env.dev
NODE_ENV=development
API_URL=https://dev-api.example.com
DEBUG=true
LOG_LEVEL=debug
```

### 测试环境 (staging)

```bash
# .env.staging
NODE_ENV=staging
API_URL=https://staging-api.example.com
DEBUG=true
LOG_LEVEL=info
```

### 生产环境 (production)

```bash
# .env.production
NODE_ENV=production
API_URL=https://api.example.com
DEBUG=false
LOG_LEVEL=error
```

## 安全检查清单

在生产部署前确认：

- [ ] 所有测试通过
- [ ] 代码审查完成
- [ ] 安全扫描通过
- [ ] 性能测试通过
- [ ] 文档已更新
- [ ] 数据库迁移就绪
- [ ] 备份已创建
- [ ] 回滚方案已准备
- [ ] 监控已配置
- [ ] 团队已通知

## 最佳实践

### 1. 自动化优先

- 使用 CI/CD 管道
- 自动化测试
- 自动化部署
- 自动化回滚

### 2. 增量部署

- 先部署到 dev
- 再部署到 staging
- 验证后部署到 production

### 3. 监控和告警

- 实时监控关键指标
- 设置告警阈值
- 快速响应异常

### 4. 文档记录

- 记录每次部署
- 更新变更日志
- 维护部署文档

### 5. 团队协作

- 提前通知部署计划
- 部署时沟通状态
- 部署后确认结果
