# AWS 成本与运维模式

成本优化、监控和运维卓越的全面模式和最佳实践。

## 目录

- [成本优化模式](#成本优化模式)
- [监控模式](#监控模式)
- [可观测性模式](#可观测性模式)
- [安全与审计模式](#安全与审计模式)
- [故障排除工作流](#故障排除工作流)

## 成本优化模式

### 模式 1: 部署前成本估算

**何时使用**: 部署任何新基础设施之前

**MCP 服务器**: AWS Pricing MCP

**步骤**:
1. 列出所有待部署资源
2. 查询每种资源类型的定价
3. 根据预期使用量计算月成本
4. 比较不同区域的定价
5. 在架构文档中记录成本估算

**示例**:
```
资源: Lambda 函数
- 调用次数: 1,000,000/月
- 执行时长: 3 秒平均
- 内存: 512 MB
- 区域: us-east-1
预估成本: $X/月
```

### 模式 2: 月度成本审查

**何时使用**: 每月第一周

**MCP 服务器**: Cost Explorer MCP, Billing MCP

**步骤**:
1. 审查总支出与预算对比
2. 按服务分析成本（前 5 个服务）
3. 识别成本异常（>20% 增长）
4. 按环境审查成本（dev/staging/prod）
5. 检查成本分配标签覆盖率
6. 生成成本优化建议

**关键指标**:
- 月环比成本变化
- 每个环境的成本
- 每个应用/项目的成本
- 未标记资源的成本

### 模式 3: 资源适当调整

**何时使用**: 季度或利用率告警触发时

**MCP 服务器**: CloudWatch MCP, Cost Explorer MCP

**步骤**:
1. 查询 CloudWatch 获取资源利用率指标
2. 识别过度配置的资源（< 40% 利用率）
3. 识别配置不足的资源（> 80% 利用率）
4. 计算适当调整后的潜在节省
5. 规划和执行调整变更
6. 监控变更后的性能

**常见适当调整场景**:
- CPU 利用率低的 EC2 实例
- 容量过剩的 RDS 实例
- 读写使用率低的 DynamoDB 表
- 内存分配过多的 Lambda 函数

### 模式 4: 未使用资源清理

**何时使用**: 每月或成本异常触发时

**MCP 服务器**: Cost Explorer MCP, CloudTrail MCP

**步骤**:
1. 识别使用量为零的资源
2. 查询 CloudTrail 获取最后访问时间
3. 标记资源以供删除审查
4. 通知资源所有者
5. 删除确认未使用的资源
6. 跟踪成本节省

**常见未使用资源**:
- 未附加的 EBS 卷
- 旧的 EBS 快照
- 空闲的负载均衡器
- 未使用的弹性 IP
- 旧的 AMI 和快照
- 长期停机的 EC2 实例

## 监控模式

### 模式 1: 关键服务监控

**何时使用**: 所有生产服务

**MCP 服务器**: CloudWatch MCP

**监控指标**:
- **可用性**: 服务运行时间、健康检查
- **性能**: 延迟、响应时间
- **错误**: 错误率、失败请求
- **饱和度**: CPU、内存、磁盘、网络利用率

**告警阈值**（根据 SLA 调整）:
- 错误率: > 1% 连续 2 个周期
- 延迟: p99 > 1 秒持续 5 分钟
- CPU: > 80% 持续 10 分钟
- 内存: > 85% 持续 5 分钟

### 模式 2: Lambda 函数监控

**MCP 服务器**: CloudWatch MCP

**关键指标**:
```
- Invocations（调用次数）
- Errors（错误数、错误率）
- Duration（平均时长、p99）
- Throttles（限流次数）
- ConcurrentExecutions（最大并发）
- IteratorAge（流处理延迟）
```

**推荐告警**:
- 错误率 > 1%
- 执行时长 > 超时时间的 80%
- 限流次数 > 0
- 并发执行 > 保留并发的 80%

### 模式 3: API Gateway 监控

**MCP 服务器**: CloudWatch MCP

**关键指标**:
```
- Count（请求总数）
- 4XXError, 5XXError
- Latency（p50, p95, p99）
- IntegrationLatency
- CacheHitCount, CacheMissCount
```

**推荐告警**:
- 5XX 错误率 > 0.5%
- 4XX 错误率 > 5%
- 延迟 p99 > 2 秒
- 集成延迟激增

### 模式 4: 数据库监控

**MCP 服务器**: CloudWatch MCP

**RDS 指标**:
```
- CPUUtilization
- DatabaseConnections
- FreeableMemory
- ReadLatency, WriteLatency
- ReadIOPS, WriteIOPS
- FreeStorageSpace
```

**DynamoDB 指标**:
```
- ConsumedReadCapacityUnits
- ConsumedWriteCapacityUnits
- UserErrors
- SystemErrors
- ThrottledRequests
```

**推荐告警**:
- RDS CPU > 80% 持续 10 分钟
- RDS 连接数 > 最大值的 80%
- RDS 可用存储 < 10 GB
- DynamoDB 限流请求 > 0
- DynamoDB 用户错误激增

## 可观测性模式

### 模式 1: 分布式追踪设置

**MCP 服务器**: CloudWatch Application Signals MCP

**组件**:
1. **服务地图**: 可视化服务依赖
2. **追踪**: 跨服务跟踪请求
3. **指标**: 监控每个服务的延迟和错误
4. **SLO**: 定义和跟踪服务级别目标

**实施**:
- 在 Lambda 函数上启用 X-Ray 追踪
- 在应用代码中添加 X-Ray SDK
- 配置采样规则
- 创建服务透镜仪表板

### 模式 2: 日志聚合和分析

**MCP 服务器**: CloudWatch MCP

**日志策略**:
1. **集中日志**: 将所有应用日志发送到 CloudWatch Logs
2. **结构化日志**: 使用 JSON 格式进行结构化日志记录
3. **日志洞察**: 使用 CloudWatch Logs Insights 进行查询
4. **保留期**: 设置适当的保留期

**示例 Log Insights 查询**:
```
# 查找最近一小时的错误
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 100

# 按类型统计错误
stats count() by error_type
| sort count desc

# 计算 p99 延迟
stats percentile(duration, 99) by service_name
```

## 安全与审计模式

### 模式 1: API 活动审计

**MCP 服务器**: CloudTrail MCP

**定期审计查询**:
```
# 查找所有 IAM 变更
eventName: CreateUser, DeleteUser, AttachUserPolicy 等
时间: 最近 24 小时

# 跟踪 S3 存储桶删除
eventName: DeleteBucket
时间: 最近 7 天

# 查找失败的登录尝试
eventName: ConsoleLogin
errorCode: Failure

# 监控特权操作
userIdentity.arn: *admin* OR *root*
```

**审计计划**:
- 每日: 审查特权用户操作
- 每周: 审计 IAM 变更和安全组修改
- 每月: 全面安全审查

### 模式 2: 安全态势评估

**MCP 服务器**: Well-Architected Security Assessment MCP

**评估领域**:
1. **身份和访问管理**: 最小权限、MFA、RBAC
2. **检测控制**: CloudTrail、GuardDuty、Config
3. **基础设施保护**: VPC 安全组、网络 ACL、WAF
4. **数据保护**: 静态加密、传输加密、KMS
5. **事件响应**: 响应手册、自动化响应

**评估频率**:
- 季度: 完整 Well-Architected 审查
- 每月: 高优先级发现审查
- 每周: 关键安全发现

## 故障排除工作流

### 工作流 1: Lambda 高错误率

**MCP 服务器**: CloudWatch MCP, Application Signals MCP

**步骤**:
1. 查询 CloudWatch 获取 Lambda 错误指标
2. 检查 CloudWatch Logs 中的错误日志
3. 识别错误模式（超时、内存、权限）
4. 检查 Lambda 配置（内存、超时、权限）
5. 审查最近的代码部署
6. 检查下游服务健康
7. 实施修复并监控

### 工作流 2: 延迟增加

**MCP 服务器**: CloudWatch MCP, Application Signals MCP

**步骤**:
1. 在 CloudWatch 指标中识别延迟激增
2. 检查服务地图中的慢依赖
3. 查询分布式追踪获取慢请求
4. 检查数据库查询性能
5. 审查 API Gateway 集成延迟
6. 检查 Lambda 冷启动
7. 识别瓶颈并优化

### 工作流 3: 成本激增调查

**MCP 服务器**: Cost Explorer MCP, CloudWatch MCP, CloudTrail MCP

**步骤**:
1. 使用 Cost Explorer 识别导致激增的服务
2. 检查 CloudWatch 指标获取使用量增加
3. 审查 CloudTrail 获取最近的资源创建
4. 识别根本原因（配置错误、失控进程、攻击）
5. 实施成本控制（预算、告警、服务配额）
6. 清理不必要的资源

### 工作流 4: 安全事件响应

**MCP 服务器**: CloudTrail MCP, GuardDuty (via CloudWatch), Well-Architected Assessment MCP

**步骤**:
1. 在 GuardDuty 或 CloudWatch 中识别安全事件
2. 查询 CloudTrail 获取相关 API 活动
3. 确定范围和影响
4. 隔离受影响的资源
5. 撤销受损凭证
6. 实施修复
7. 进行事后审查
8. 更新安全控制

## 总结

- **成本优化**: 使用 Pricing、Cost Explorer 和 Billing MCP 进行主动成本管理
- **监控**: 为所有关键服务设置全面的 CloudWatch 告警
- **可观测性**: 实施分布式追踪和结构化日志记录
- **安全**: 定期进行 CloudTrail 审计和 Well-Architected 评估
- **主动性**: 不要等待事件发生 - 持续监控和优化
