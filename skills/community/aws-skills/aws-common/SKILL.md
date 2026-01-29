---
name: aws-mcp-setup
description: 配置 AWS MCP 服务器，用于查询最新 AWS 文档、API 和最佳实践
---

# AWS MCP 服务器配置指南

## 概述

本指南帮助你配置 AWS MCP 工具。提供两种选项：

| 选项 | 要求 | 能力 |
|------|------|------|
| **完整 AWS MCP** | Python 3.10+, uvx, AWS 凭证 | 执行 AWS API + 文档搜索 |
| **文档 MCP** | 无 | 仅文档搜索 |

## 步骤 1: 检查现有配置

### 方法 A: 检查可用工具（推荐）

在 Claude Code 中运行 `/mcp` 命令查看已激活的 MCP 服务器。

查找以下工具名模式：
- `mcp__aws-mcp__*` 或 `mcp__aws__*` → 完整 AWS MCP 已配置
- `mcp__*awsdocs*__aws___*` → 文档 MCP 已配置

### 方法 B: 检查配置文件

MCP 配置使用层级优先级（本地 → 项目 → 用户 → 企业）：

| 范围 | 文件位置 | 用途 |
|------|----------|------|
| 本地 | `.claude.json` (项目内) | 个人/实验 |
| 项目 | `.mcp.json` (项目根目录) | 团队共享 |
| 用户 | `~/.claude.json` | 跨项目个人配置 |
| 企业 | 系统管理目录 | 组织范围 |

```bash
# 检查项目配置
cat .mcp.json 2>/dev/null | grep -E '"(aws-mcp|aws|awsdocs)"'

# 检查用户配置
cat ~/.claude.json 2>/dev/null | grep -E '"(aws-mcp|aws|awsdocs)"'

# 或使用 Claude CLI
claude mcp list
```

## 步骤 2: 选择配置方式

### 自动检测

```bash
# 检查 uvx（需要 Python 3.10+）
which uvx || echo "uvx 不可用"

# 检查 AWS 凭证
aws sts get-caller-identity || echo "AWS 凭证未配置"
```

### 选项 A: 完整 AWS MCP（推荐）

**使用条件**: uvx 可用 且 AWS 凭证有效

**前置条件**:
- Python 3.10+ 和 `uv` 包管理器
- AWS 凭证已配置（profile、环境变量或 IAM Role）

**所需 IAM 权限**:
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "aws-mcp:InvokeMCP",
      "aws-mcp:CallReadOnlyTool",
      "aws-mcp:CallReadWriteTool"
    ],
    "Resource": "*"
  }]
}
```

**配置（添加到 MCP 设置）**:
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

**凭证配置选项**:

1. **AWS Profile**（推荐用于开发）:
   ```json
   "args": [
     "mcp-proxy-for-aws@latest",
     "https://aws-mcp.us-east-1.api.aws/mcp",
     "--profile", "my-profile",
     "--metadata", "AWS_REGION=us-east-1"
   ]
   ```

2. **环境变量**:
   ```json
   "env": {
     "AWS_ACCESS_KEY_ID": "...",
     "AWS_SECRET_ACCESS_KEY": "...",
     "AWS_REGION": "us-east-1"
   }
   ```

3. **IAM Role**（EC2/ECS/Lambda）: 无需额外配置，使用实例凭证

**参考文档**: https://github.com/aws/mcp-proxy-for-aws

### 选项 B: 文档 MCP（无需认证）

**使用条件**:
- 无 Python/uvx 环境
- 无 AWS 凭证
- 仅需要文档搜索（不执行 API）

**配置**:
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

## 步骤 3: 验证

配置后重启 Claude Code，验证工具是否可用：

**完整 AWS MCP**:
- 查找工具: `mcp__aws-mcp__aws___search_documentation`, `mcp__aws-mcp__aws___call_aws`

**文档 MCP**:
- 查找工具: `mcp__awsdocs__aws___search_documentation`, `mcp__awsdocs__aws___read_documentation`

## 故障排除

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `uvx: command not found` | uv 未安装 | 安装 `pip install uv` 或使用选项 B |
| `AccessDenied` 错误 | 缺少 IAM 权限 | 添加 aws-mcp:* 权限到 IAM 策略 |
| `InvalidSignatureException` | 凭证问题 | 检查 `aws sts get-caller-identity` |
| 工具未出现 | MCP 未启动 | 配置更改后重启 Claude Code |

## 常用 MCP 工具

配置完成后可使用的工具：

| 工具 | 功能 |
|------|------|
| `aws___search_documentation` | 搜索 AWS 文档 |
| `aws___read_documentation` | 读取特定文档页面 |
| `aws___get_regional_availability` | 检查服务区域可用性 |
| `aws___call_aws` | 执行 AWS API 调用（仅完整版） |
