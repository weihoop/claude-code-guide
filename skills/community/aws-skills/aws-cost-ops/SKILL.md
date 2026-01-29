---
name: aws-cost-operations
description: AWS 成本优化、监控和运维最佳实践，集成多个 MCP 服务器用于账单分析、成本估算、可观测性和安全评估
skills:
  - aws-mcp-setup
allowed-tools:
  - mcp__pricing__*
  - mcp__costexp__*
  - mcp__cw__*
  - mcp__aws-mcp__*
  - mcp__awsdocs__*
  - Bash(aws ce *)
  - Bash(aws cloudwatch *)
  - Bash(aws logs *)
  - Bash(aws budgets *)
  - Bash(aws cloudtrail *)
  - Bash(aws sts get-caller-identity)
---

# AWS 成本与运维

本技能提供 AWS 成本优化、监控、可观测性和运维卓越的全面指南，集成多个 MCP 服务器。

## 集成的 MCP 服务器

### 成本管理服务器

#### 1. AWS Pricing MCP
**用途**: 部署前成本估算和优化
- 部署资源前估算成本
- 比较不同区域的定价
- 计算总拥有成本 (TCO)
- 评估不同服务选项的成本效益

#### 2. AWS Cost Explorer MCP
**用途**: 详细成本分析和报告
- 分析历史支出模式
- 创建自定义成本报告
- 识别成本异常和趋势
- 预测未来成本
- 生成成本优化建议

#### 3. AWS Billing MCP
**用途**: 实时账单和成本管理
- 查看当前 AWS 支出和趋势
- 分析各服务账单明细
- 跟踪预算使用情况
- 监控成本分配标签

### 监控与可观测性服务器

#### 4. Amazon CloudWatch MCP
**用途**: 指标、告警和日志分析
- 查询 CloudWatch 指标和日志
- 创建和管理告警
- 分析应用性能指标
- 排查运维问题

#### 5. CloudWatch Application Signals MCP
**用途**: 应用监控和性能洞察
- 监控应用健康和性能
- 分析服务级别目标 (SLO)
- 跟踪应用依赖
- 识别性能瓶颈

#### 6. AWS Managed Prometheus MCP
**用途**: Prometheus 兼容监控
- 查询 Prometheus 指标
- 监控容器化应用
- 分析 Kubernetes 工作负载指标

### 审计与安全服务器

#### 7. AWS CloudTrail MCP
**用途**: AWS API 活动和审计分析
- 分析 AWS API 调用和用户活动
- 跟踪资源变更
- 调查安全事件
- 审计合规要求

#### 8. Well-Architected Security Assessment MCP
**用途**: 安全态势评估
- 根据 AWS 最佳实践评估安全态势
- 识别安全漏洞
- 获取安全改进建议

## 使用场景

- 优化 AWS 成本和减少支出
- 部署前估算成本
- 监控应用和基础设施性能
- 设置可观测性和告警
- 分析支出模式和趋势
- 调查运维问题
- 审计 AWS 活动和变更
- 评估安全态势

## 成本优化最佳实践

### 部署前成本估算

**始终在部署前估算成本**：
1. 使用 **AWS Pricing MCP** 估算资源成本
2. 比较不同区域的定价
3. 评估替代服务选项
4. 计算预期月成本
5. 规划扩展和增长

**示例工作流**：
```
"估算在 us-east-1 运行 Lambda 函数的月成本：
- 调用次数: 100万/月
- 内存: 512MB
- 执行时长: 3秒"
```

### 成本分析和优化

**定期成本审查**：
1. 使用 **Cost Explorer MCP** 分析支出趋势
2. 识别成本异常和意外费用
3. 按服务、区域和环境审查成本
4. 比较实际与预算成本
5. 生成成本优化建议

**成本优化策略**：
- 对过度配置的资源进行适当调整
- 使用合适的存储类别（S3、EBS）
- 为动态工作负载实施自动扩展
- 利用 Savings Plans 和预留实例
- 删除未使用的资源和快照
- 有效使用成本分配标签

### 预算监控

**跟踪预算支出**：
1. 使用 **Billing MCP** 监控预算
2. 设置预算超限告警
3. 定期审查预算使用情况
4. 根据趋势调整预算
5. 实施成本控制和治理

## 监控和可观测性最佳实践

### CloudWatch 指标和告警

**实施全面监控**：
1. 使用 **CloudWatch MCP** 查询指标和日志
2. 为关键指标设置告警：
   - CPU 和内存利用率
   - 错误率和延迟
   - 队列深度和处理时间
   - API Gateway 限流
   - Lambda 错误和超时
3. 创建 CloudWatch 仪表板进行可视化
4. 使用日志洞察进行故障排除

**示例告警场景**：
- Lambda 错误率 > 1%
- EC2 CPU 利用率 > 80%
- API Gateway 4xx/5xx 错误激增
- DynamoDB 限流请求
- ECS 任务失败

## 审计和安全最佳实践

### CloudTrail 活动分析

**审计 AWS 活动**：
1. 使用 **CloudTrail MCP** 分析 API 活动
2. 跟踪谁对资源进行了更改
3. 调查安全事件
4. 监控可疑活动模式
5. 审计策略合规性

**常见审计场景**：
- "谁删除了这个 S3 存储桶？"
- "显示最近 24 小时内所有 IAM 角色变更"
- "列出失败的登录尝试"
- "查找特定用户的所有操作"
- "跟踪安全组的修改"

### 安全评估

**定期安全审查**：
1. 使用 **Well-Architected Security Assessment MCP**
2. 根据最佳实践评估安全态势
3. 识别安全漏洞
4. 实施推荐的安全改进
5. 记录安全合规性

## 其他资源

详细的运维模式和最佳实践，请参考：

- `references/operations-patterns.md` - 成本优化、监控、可观测性模式
- `references/cloudwatch-alarms.md` - CloudWatch 告警配置参考
