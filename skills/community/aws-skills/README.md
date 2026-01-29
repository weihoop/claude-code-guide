# AWS Skills for Claude Code

基于 [zxkane/aws-skills](https://github.com/zxkane/aws-skills) 整合的 AWS 开发技能包，提供成本优化、CDK 开发、监控运维等专业能力。

## 技能列表

| 技能 | 目录 | 用途 |
|------|------|------|
| **AWS 成本运维** | `aws-cost-ops/` | 成本优化、监控、审计、告警配置 |
| **AWS MCP 配置** | `aws-common/` | AWS MCP 服务器配置指南 |
| **AWS CDK 开发** | `aws-cdk/` | CDK 最佳实践、构造模式 |

## 快速开始

### 1. 配置 AWS MCP 服务器

参考 `aws-common/SKILL.md` 配置 MCP 服务器：

**方式 A：完整 AWS MCP（需要 AWS 凭证）**
```json
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-east-1"
      ]
    }
  }
}
```

**方式 B：仅文档 MCP（无需凭证）**
```json
{
  "mcpServers": {
    "awsdocs": {
      "type": "http",
      "url": "https://knowledge-mcp.global.api.aws"
    }
  }
}
```

### 2. 使用技能

配置后重启 Claude Code，即可使用以下功能：

**成本分析**：
```
"显示过去 30 天各服务费用分布"
"估算新加坡区域部署 3 台 t3.medium 的月费用"
"分析 EC2 使用模式，推荐 Savings Plans"
```

**监控运维**：
```
"查询 us-east-1 所有 EC2 的 CPU 使用率"
"找出 CPU 使用率低于 10% 的闲置实例"
"创建 NAT Gateway 流量告警"
```

**CDK 开发**：
```
"创建 Lambda 函数处理 S3 事件的 CDK Stack"
"检查我的 CDK 代码是否符合最佳实践"
```

## 集成的 MCP 服务器

### 成本管理
- **AWS Pricing MCP** - 部署前成本估算
- **AWS Cost Explorer MCP** - 费用分析和报告
- **AWS Billing MCP** - 账单和预算监控

### 监控与可观测性
- **Amazon CloudWatch MCP** - 指标、日志、告警
- **CloudWatch Application Signals MCP** - 应用性能监控
- **AWS Managed Prometheus MCP** - Prometheus 兼容监控

### 安全与审计
- **AWS CloudTrail MCP** - API 活动审计
- **Well-Architected Security Assessment MCP** - 安全评估

### 开发工具
- **AWS CDK MCP** - CDK 构造和模式建议

## 目录结构

```
aws-skills/
├── README.md                    # 本文件
├── aws-cost-ops/                # 成本优化技能
│   ├── SKILL.md                 # 技能定义
│   └── references/              # 参考文档
│       ├── operations-patterns.md
│       └── cloudwatch-alarms.md
├── aws-common/                  # MCP 配置
│   └── SKILL.md
└── aws-cdk/                     # CDK 开发技能
    ├── SKILL.md
    └── references/
        └── cdk-patterns.md
```

## 原项目

- **来源**: https://github.com/zxkane/aws-skills
- **协议**: MIT License
- **整合时间**: 2026-01-29

## 使用场景

### 成本优化
- 部署前估算费用
- 分析月度开支趋势
- 识别闲置资源
- 评估 Savings Plans

### 监控告警
- 设置 CloudWatch 告警
- 查询性能指标
- 排查延迟问题
- 分析错误日志

### 安全审计
- 审计 IAM 变更
- 跟踪 API 活动
- 安全态势评估
- 合规性检查

### CDK 开发
- Lambda 函数最佳实践
- 资源命名规范
- 安全模式实现
- 成本优化配置
