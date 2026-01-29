# CloudWatch 告警配置参考

AWS 服务的常用 CloudWatch 告警配置。

## Lambda 函数

### 错误率告警
```typescript
new cloudwatch.Alarm(this, 'LambdaErrorAlarm', {
  metric: lambdaFunction.metricErrors({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 10,
  evaluationPeriods: 1,
  treatMissingData: cloudwatch.TreatMissingData.NOT_BREACHING,
  alarmDescription: 'Lambda 错误数超过阈值',
});
```

### 执行时长告警（接近超时）
```typescript
new cloudwatch.Alarm(this, 'LambdaDurationAlarm', {
  metric: lambdaFunction.metricDuration({
    statistic: 'Maximum',
    period: Duration.minutes(5),
  }),
  threshold: lambdaFunction.timeout.toMilliseconds() * 0.8, // 超时时间的 80%
  evaluationPeriods: 2,
  alarmDescription: 'Lambda 执行时长接近超时',
});
```

### 限流告警
```typescript
new cloudwatch.Alarm(this, 'LambdaThrottleAlarm', {
  metric: lambdaFunction.metricThrottles({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 5,
  evaluationPeriods: 1,
  alarmDescription: 'Lambda 函数被限流',
});
```

## API Gateway

### 5XX 错误率告警
```typescript
new cloudwatch.Alarm(this, 'Api5xxAlarm', {
  metric: api.metricServerError({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 10,
  evaluationPeriods: 1,
  alarmDescription: 'API Gateway 5XX 错误超过阈值',
});
```

### 延迟告警
```typescript
new cloudwatch.Alarm(this, 'ApiLatencyAlarm', {
  metric: api.metricLatency({
    statistic: 'p99',
    period: Duration.minutes(5),
  }),
  threshold: 2000, // 2 秒
  evaluationPeriods: 2,
  alarmDescription: 'API Gateway p99 延迟超过阈值',
});
```

## EC2 实例

### CPU 利用率告警
```typescript
new cloudwatch.Alarm(this, 'EC2CpuAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/EC2',
    metricName: 'CPUUtilization',
    dimensionsMap: {
      InstanceId: instance.instanceId,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 80,
  evaluationPeriods: 3,
  alarmDescription: 'EC2 CPU 利用率过高',
});
```

### 状态检查失败告警
```typescript
new cloudwatch.Alarm(this, 'EC2StatusCheckAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/EC2',
    metricName: 'StatusCheckFailed',
    dimensionsMap: {
      InstanceId: instance.instanceId,
    },
    statistic: 'Maximum',
    period: Duration.minutes(1),
  }),
  threshold: 1,
  evaluationPeriods: 2,
  alarmDescription: 'EC2 状态检查失败',
});
```

## RDS 数据库

### CPU 告警
```typescript
new cloudwatch.Alarm(this, 'RDSCpuAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/RDS',
    metricName: 'CPUUtilization',
    dimensionsMap: {
      DBInstanceIdentifier: dbInstance.instanceIdentifier,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 80,
  evaluationPeriods: 3,
  alarmDescription: 'RDS CPU 利用率过高',
});
```

### 连接数告警
```typescript
new cloudwatch.Alarm(this, 'RDSConnectionAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/RDS',
    metricName: 'DatabaseConnections',
    dimensionsMap: {
      DBInstanceIdentifier: dbInstance.instanceIdentifier,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: maxConnections * 0.8, // 最大连接数的 80%
  evaluationPeriods: 2,
  alarmDescription: 'RDS 连接数接近上限',
});
```

### 可用存储空间告警
```typescript
new cloudwatch.Alarm(this, 'RDSStorageAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/RDS',
    metricName: 'FreeStorageSpace',
    dimensionsMap: {
      DBInstanceIdentifier: dbInstance.instanceIdentifier,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 10 * 1024 * 1024 * 1024, // 10 GB（字节）
  comparisonOperator: cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
  evaluationPeriods: 1,
  alarmDescription: 'RDS 可用存储空间不足',
});
```

## DynamoDB

### 读取限流告警
```typescript
new cloudwatch.Alarm(this, 'DynamoDBReadThrottleAlarm', {
  metric: table.metricUserErrors({
    dimensions: {
      Operation: 'GetItem',
    },
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 5,
  evaluationPeriods: 1,
  alarmDescription: 'DynamoDB 读取操作被限流',
});
```

## ECS 服务

### 任务数量告警
```typescript
new cloudwatch.Alarm(this, 'ECSTaskCountAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'ECS/ContainerInsights',
    metricName: 'RunningTaskCount',
    dimensionsMap: {
      ServiceName: service.serviceName,
      ClusterName: cluster.clusterName,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 1,
  comparisonOperator: cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
  evaluationPeriods: 2,
  alarmDescription: 'ECS 服务没有运行的任务',
});
```

## SQS 队列

### 队列深度告警
```typescript
new cloudwatch.Alarm(this, 'SQSDepthAlarm', {
  metric: queue.metricApproximateNumberOfMessagesVisible({
    statistic: 'Maximum',
    period: Duration.minutes(5),
  }),
  threshold: 1000,
  evaluationPeriods: 2,
  alarmDescription: 'SQS 队列深度超过阈值',
});
```

### 消息年龄告警
```typescript
new cloudwatch.Alarm(this, 'SQSAgeAlarm', {
  metric: queue.metricApproximateAgeOfOldestMessage({
    statistic: 'Maximum',
    period: Duration.minutes(5),
  }),
  threshold: 300, // 5 分钟（秒）
  evaluationPeriods: 1,
  alarmDescription: 'SQS 消息未及时处理',
});
```

## Application Load Balancer

### 目标健康告警
```typescript
new cloudwatch.Alarm(this, 'ALBUnhealthyTargetAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/ApplicationELB',
    metricName: 'UnHealthyHostCount',
    dimensionsMap: {
      LoadBalancer: loadBalancer.loadBalancerFullName,
      TargetGroup: targetGroup.targetGroupFullName,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 1,
  evaluationPeriods: 2,
  alarmDescription: 'ALB 有不健康的目标',
});
```

### HTTP 5XX 告警
```typescript
new cloudwatch.Alarm(this, 'ALB5xxAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/ApplicationELB',
    metricName: 'HTTPCode_Target_5XX_Count',
    dimensionsMap: {
      LoadBalancer: loadBalancer.loadBalancerFullName,
    },
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 10,
  evaluationPeriods: 1,
  alarmDescription: 'ALB 目标 5XX 错误超过阈值',
});
```

## 复合告警

### 服务健康复合告警
```typescript
const errorAlarm = new cloudwatch.Alarm(this, 'ErrorAlarm', { /* ... */ });
const latencyAlarm = new cloudwatch.Alarm(this, 'LatencyAlarm', { /* ... */ });
const throttleAlarm = new cloudwatch.Alarm(this, 'ThrottleAlarm', { /* ... */ });

new cloudwatch.CompositeAlarm(this, 'ServiceHealthAlarm', {
  compositeAlarmName: 'service-health',
  alarmRule: cloudwatch.AlarmRule.anyOf(
    errorAlarm,
    latencyAlarm,
    throttleAlarm
  ),
  alarmDescription: '整体服务健康状态下降',
});
```

## 告警操作

### SNS 主题集成
```typescript
const topic = new sns.Topic(this, 'AlarmTopic', {
  displayName: 'CloudWatch Alarms',
});

// 邮件订阅
topic.addSubscription(new subscriptions.EmailSubscription('ops@example.com'));

// 添加告警操作
alarm.addAlarmAction(new actions.SnsAction(topic));
alarm.addOkAction(new actions.SnsAction(topic));
```

## 告警最佳实践

### 阈值选择

**CPU/内存告警**:
- 警告: 70-80%
- 严重: 80-90%
- 考虑突发模式和正常使用情况

**错误率告警**:
- 基于 SLA 设置阈值（如 99.9% = 0.1% 错误率）
- 考虑正常错误率
- 不同错误类型设置不同阈值

**延迟告警**:
- 面向用户的 API 使用 p99 延迟
- 警告: SLA 目标的 80%
- 严重: SLA 目标的 100%

### 评估周期

**快速变化的指标**（1-2 个周期）:
- 错误计数
- 健康检查失败
- 关键应用错误

**慢速变化的指标**（3-5 个周期）:
- CPU 利用率
- 内存使用
- 磁盘使用

### 缺失数据处理

```typescript
// 间歇性工作负载
alarm.treatMissingData(cloudwatch.TreatMissingData.NOT_BREACHING);

// 持续运行的服务
alarm.treatMissingData(cloudwatch.TreatMissingData.BREACHING);

// 区分数据问题
alarm.treatMissingData(cloudwatch.TreatMissingData.MISSING);
```

### 告警命名规范

```typescript
// 模式: <服务>-<指标>-<严重性>
'lambda-errors-critical'
'api-latency-warning'
'rds-cpu-warning'
'ecs-tasks-critical'
```

### 告警操作最佳实践

1. **按严重性分离主题**:
   - 严重告警 → PagerDuty/值班
   - 警告告警 → Slack/邮件
   - 信息告警 → 指标仪表板

2. **在告警描述中包含上下文**:
   - 服务名称
   - 预期阈值
   - 故障排除手册链接

3. **尽可能自动修复**:
   - Lambda 错误 → 自动重试
   - CPU 过高 → 自动扩展触发
   - 磁盘满 → 自动清理

4. **告警疲劳预防**:
   - 根据实际模式调整阈值
   - 使用复合告警减少噪音
   - 实施适当的评估周期
   - 定期审查和调整告警
