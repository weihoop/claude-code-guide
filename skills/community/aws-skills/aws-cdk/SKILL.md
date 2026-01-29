---
name: aws-cdk-development
description: AWS CDK 开发专家，用于构建云基础设施。使用场景：创建 CDK Stack、定义 CDK 构造、实现基础设施即代码，或用户提及 CDK、CloudFormation、IaC、cdk synth、cdk deploy，或希望以编程方式定义 AWS 基础设施。
context: fork
skills:
  - aws-mcp-setup
allowed-tools:
  - mcp__cdk__*
  - mcp__aws-mcp__*
  - mcp__awsdocs__*
  - Bash(cdk *)
  - Bash(npm *)
  - Bash(npx *)
  - Bash(aws cloudformation *)
  - Bash(aws sts get-caller-identity)
---

# AWS CDK 开发

本技能提供使用 Cloud Development Kit (CDK) 开发 AWS 基础设施的全面指南，集成 MCP 服务器用于访问最新 AWS 知识和 CDK 工具。

## 集成的 MCP 服务器

### AWS CDK MCP 服务器
**使用场景**: CDK 特定指导和工具
- 获取 CDK 构造建议
- 检索 CDK 最佳实践
- 访问 CDK 模式建议
- 验证 CDK 配置
- 获取 CDK 特定 API 帮助

## 使用场景

- 创建新的 CDK Stack 或构造
- 重构现有 CDK 基础设施
- 在 CDK 中实现 Lambda 函数
- 遵循 AWS CDK 最佳实践
- 部署前验证 CDK Stack 配置
- 验证 AWS 服务能力和区域可用性

## 核心 CDK 原则

### 资源命名

**关键**: 当 CDK 构造中资源名称是可选的时，**不要**显式指定资源名称。

**原因**: CDK 生成的名称支持：
- **可重用模式**: 同一构造/模式可多次部署而不冲突
- **并行部署**: 多个 Stack 可在同一区域同时部署
- **更干净的共享逻辑**: 模式和共享代码可多次初始化而不会命名冲突
- **Stack 隔离**: 每个 Stack 自动获得唯一标识的资源

**模式**: 让 CDK 使用 CloudFormation 的命名机制自动生成唯一名称。

```typescript
// ❌ 错误 - 显式命名阻止可重用性和并行部署
new lambda.Function(this, 'MyFunction', {
  functionName: 'my-lambda',  // 避免这样做
  // ...
});

// ✅ 正确 - 让 CDK 生成唯一名称
new lambda.Function(this, 'MyFunction', {
  // 不指定 functionName - CDK 生成: StackName-MyFunctionXXXXXX
  // ...
});
```

**安全说明**: 对于不同环境（dev、staging、prod），遵循 AWS 安全支柱最佳实践，使用单独的 AWS 账户而不是在单个账户内依赖资源命名。账户级别隔离提供更强的安全边界。

### Lambda 函数开发

根据运行时使用适当的 Lambda 构造：

**TypeScript/JavaScript**: 使用 `@aws-cdk/aws-lambda-nodejs`
```typescript
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

new NodejsFunction(this, 'MyFunction', {
  entry: 'lambda/handler.ts',
  handler: 'handler',
  // 自动处理打包、依赖和转译
});
```

**Python**: 使用 `@aws-cdk/aws-lambda-python`
```typescript
import { PythonFunction } from '@aws-cdk/aws-lambda-python-alpha';

new PythonFunction(this, 'MyFunction', {
  entry: 'lambda',
  index: 'handler.py',
  handler: 'handler',
  // 自动处理依赖和打包
});
```

**优势**:
- 自动打包和依赖管理
- 自动处理转译
- 无需手动打包
- 一致的部署模式

### 部署前验证

使用**多层验证策略**进行全面的 CDK 质量检查：

#### 第 1 层: IDE 实时反馈（推荐）

**TypeScript/JavaScript 项目**:

安装 [cdk-nag](https://github.com/cdklabs/cdk-nag) 用于合成时验证：
```bash
npm install --save-dev cdk-nag
```

添加到 CDK 应用：
```typescript
import { Aspects } from 'aws-cdk-lib';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
Aspects.of(app).add(new AwsSolutionsChecks());
```

#### 第 2 层: 合成时验证（必需）

1. **使用 cdk-nag 合成**: 用全面规则验证 Stack
   ```bash
   cdk synth  # cdk-nag 通过 Aspects 自动运行
   ```

2. **抑制合理的例外**并记录原因：
   ```typescript
   import { NagSuppressions } from 'cdk-nag';

   // 记录为什么需要例外
   NagSuppressions.addResourceSuppressions(resource, [
     {
       id: 'AwsSolutions-L1',
       reason: 'Lambda@Edge 需要特定运行时以兼容 CloudFront'
     }
   ]);
   ```

#### 第 3 层: 提交前安全网

1. **构建**: 确保编译成功
   ```bash
   npm run build  # 或特定语言的构建命令
   ```

2. **测试**: 运行单元和集成测试
   ```bash
   npm test  # 或 pytest, mvn test 等
   ```

3. **验证脚本**: 元级别检查
   ```bash
   ./scripts/validate-stack.sh
   ```

## 工作流指南

### 开发工作流

1. **设计**: 规划基础设施资源和关系
2. **验证 AWS 服务**: 使用 AWS 文档 MCP 确认服务可用性和功能
3. **实现**: 按照最佳实践编写 CDK 构造
4. **验证**: 运行部署前检查
5. **合成**: 生成 CloudFormation 模板
6. **审查**: 检查合成的模板是否正确
7. **部署**: 部署到目标环境
8. **验证**: 确认资源创建正确

### Stack 组织

- 对复杂应用使用嵌套 Stack
- 将关注点分离到逻辑构造边界
- 导出其他 Stack 可能需要的值
- 使用 CDK 上下文进行环境特定配置

### 测试策略

- 对单个构造进行单元测试
- 对 Stack 合成进行集成测试
- 对 CloudFormation 模板进行快照测试
- 验证资源属性和关系

## 有效使用 MCP 服务器

### 何时使用 AWS 文档 MCP

**实现前始终验证**：
- 新的 AWS 服务功能或配置
- 目标区域的服务可用性
- API 参数规范
- 服务限制和配额
- AWS 服务的安全最佳实践

**示例场景**：
- "检查 Lambda 是否支持 Python 3.13 运行时"
- "验证 DynamoDB 在 eu-south-2 是否可用"
- "当前 Lambda 超时限制是多少？"
- "获取最新的 S3 加密选项"

### 何时使用 CDK MCP 服务器

**利用 CDK 特定指导**：
- CDK 构造选择和使用
- CDK API 参数选项
- CDK 最佳实践模式
- 构造属性配置
- CDK 特定优化

**示例场景**：
- "API Gateway REST API 推荐使用什么 CDK 构造？"
- "如何配置 NodejsFunction 打包选项？"
- "CDK Stack 组织的最佳实践"
- "带自动扩展的 DynamoDB CDK 构造"

## 其他资源

详细的 CDK 模式、反模式和架构指南，请参考：

- `references/cdk-patterns.md` - 详细的模式库
