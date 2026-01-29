# AWS CDK 模式和最佳实践

本参考提供 AWS CDK 开发的详细模式、反模式和最佳实践。

## 目录

- [命名规范](#命名规范)
- [构造模式](#构造模式)
- [安全模式](#安全模式)
- [Lambda 集成](#lambda-集成)
- [测试模式](#测试模式)
- [成本优化](#成本优化)
- [反模式](#反模式)

## 命名规范

### 自动资源命名（推荐）

让 CDK 和 CloudFormation 自动生成唯一的资源名称：

**优势**:
- 支持同一区域/账户中的多次部署
- 支持并行环境（dev、staging、prod）
- 防止命名冲突
- 允许 Stack 克隆和测试

**示例**:
```typescript
// ✅ 正确 - 自动命名
const bucket = new s3.Bucket(this, 'DataBucket', {
  // 不指定 bucketName
  encryption: s3.BucketEncryption.S3_MANAGED,
});
```

### 何时需要显式命名

某些场景需要显式名称：
- 被外部系统引用的资源
- 跨部署必须保持一致名称的资源
- 需要稳定名称的跨 Stack 引用

**模式**: 使用逻辑前缀和环境后缀
```typescript
// 仅在绝对必要时
const bucket = new s3.Bucket(this, 'DataBucket', {
  bucketName: `${props.projectName}-data-${props.environment}`,
});
```

## 构造模式

### L3 构造（模式）

优先使用封装最佳实践的高级模式：

```typescript
import * as patterns from 'aws-cdk-lib/aws-apigateway';

new patterns.LambdaRestApi(this, 'MyApi', {
  handler: myFunction,
  // 包含 CloudWatch Logs、IAM 角色和 API Gateway 配置
});
```

### 自定义构造

为重复模式创建可重用构造：

```typescript
export class ApiWithDatabase extends Construct {
  public readonly api: apigateway.RestApi;
  public readonly table: dynamodb.Table;

  constructor(scope: Construct, id: string, props: ApiWithDatabaseProps) {
    super(scope, id);

    this.table = new dynamodb.Table(this, 'Table', {
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
    });

    const handler = new NodejsFunction(this, 'Handler', {
      entry: props.handlerEntry,
      environment: {
        TABLE_NAME: this.table.tableName,
      },
    });

    this.table.grantReadWriteData(handler);

    this.api = new apigateway.LambdaRestApi(this, 'Api', {
      handler,
    });
  }
}
```

## 安全模式

### IAM 最小权限

使用 grant 方法而不是宽泛的策略：

```typescript
// ✅ 正确 - 特定授权
const table = new dynamodb.Table(this, 'Table', { /* ... */ });
const lambda = new lambda.Function(this, 'Function', { /* ... */ });

table.grantReadWriteData(lambda);

// ❌ 错误 - 权限过于宽泛
lambda.addToRolePolicy(new iam.PolicyStatement({
  actions: ['dynamodb:*'],
  resources: ['*'],
}));
```

### 密钥管理

使用 Secrets Manager 管理敏感数据：

```typescript
import * as secretsmanager from 'aws-cdk-lib/aws-secretsmanager';

const secret = new secretsmanager.Secret(this, 'DbPassword', {
  generateSecretString: {
    secretStringTemplate: JSON.stringify({ username: 'admin' }),
    generateStringKey: 'password',
    excludePunctuation: true,
  },
});

// 授予 Lambda 读取权限
secret.grantRead(myFunction);
```

### VPC 配置

遵循 VPC 最佳实践：

```typescript
const vpc = new ec2.Vpc(this, 'Vpc', {
  maxAzs: 2,
  natGateways: 1, // 成本优化: dev 用 1 个，prod 用 2+ 个
  subnetConfiguration: [
    {
      name: 'Public',
      subnetType: ec2.SubnetType.PUBLIC,
      cidrMask: 24,
    },
    {
      name: 'Private',
      subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      cidrMask: 24,
    },
    {
      name: 'Isolated',
      subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
      cidrMask: 24,
    },
  ],
});
```

## Lambda 集成

### NodejsFunction (TypeScript/JavaScript)

```typescript
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

const fn = new NodejsFunction(this, 'Function', {
  entry: 'src/handlers/process.ts',
  handler: 'handler',
  runtime: lambda.Runtime.NODEJS_20_X,
  timeout: Duration.seconds(30),
  memorySize: 512,
  environment: {
    TABLE_NAME: table.tableName,
  },
  bundling: {
    minify: true,
    sourceMap: true,
    externalModules: ['@aws-sdk/*'], // 使用 Lambda 运行时的 AWS SDK
  },
});
```

### PythonFunction

```typescript
import { PythonFunction } from '@aws-cdk/aws-lambda-python-alpha';

const fn = new PythonFunction(this, 'Function', {
  entry: 'src/handlers',
  index: 'process.py',
  handler: 'handler',
  runtime: lambda.Runtime.PYTHON_3_12,
  timeout: Duration.seconds(30),
  memorySize: 512,
});
```

### Lambda Layers

跨函数共享代码：

```typescript
const layer = new lambda.LayerVersion(this, 'CommonLayer', {
  code: lambda.Code.fromAsset('layers/common'),
  compatibleRuntimes: [lambda.Runtime.NODEJS_20_X],
  description: '通用工具',
});

new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  layers: [layer],
});
```

## 测试模式

### 快照测试

```typescript
import { Template } from 'aws-cdk-lib/assertions';

test('Stack 创建预期资源', () => {
  const app = new cdk.App();
  const stack = new MyStack(app, 'TestStack');

  const template = Template.fromStack(stack);
  expect(template.toJSON()).toMatchSnapshot();
});
```

### 细粒度断言

```typescript
test('Lambda 有正确的环境变量', () => {
  const app = new cdk.App();
  const stack = new MyStack(app, 'TestStack');

  const template = Template.fromStack(stack);

  template.hasResourceProperties('AWS::Lambda::Function', {
    Runtime: 'nodejs20.x',
    Timeout: 30,
    Environment: {
      Variables: {
        TABLE_NAME: { Ref: Match.anyValue() },
      },
    },
  });
});
```

### 资源数量验证

```typescript
test('Stack 有正确数量的函数', () => {
  const app = new cdk.App();
  const stack = new MyStack(app, 'TestStack');

  const template = Template.fromStack(stack);
  template.resourceCountIs('AWS::Lambda::Function', 3);
});
```

## 成本优化

### Lambda 适当调整

```typescript
// 开发环境
const devFunction = new NodejsFunction(this, 'DevFunction', {
  memorySize: 256, // 开发环境较低
  timeout: Duration.seconds(30),
});

// 生产环境
const prodFunction = new NodejsFunction(this, 'ProdFunction', {
  memorySize: 1024, // 生产环境更高以获得更好性能
  timeout: Duration.seconds(10),
  reservedConcurrentExecutions: 10, // 防止成本失控
});
```

### DynamoDB 计费模式

```typescript
// 开发/低流量
const devTable = new dynamodb.Table(this, 'DevTable', {
  billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
});

// 生产/可预测负载
const prodTable = new dynamodb.Table(this, 'ProdTable', {
  billingMode: dynamodb.BillingMode.PROVISIONED,
  readCapacity: 5,
  writeCapacity: 5,
  autoScaling: { /* ... */ },
});
```

### S3 生命周期策略

```typescript
const bucket = new s3.Bucket(this, 'DataBucket', {
  lifecycleRules: [
    {
      id: 'MoveToIA',
      transitions: [
        {
          storageClass: s3.StorageClass.INFREQUENT_ACCESS,
          transitionAfter: Duration.days(30),
        },
        {
          storageClass: s3.StorageClass.GLACIER,
          transitionAfter: Duration.days(90),
        },
      ],
    },
    {
      id: 'CleanupOldVersions',
      noncurrentVersionExpiration: Duration.days(30),
    },
  ],
});
```

## 反模式

### ❌ 硬编码值

```typescript
// 错误
new lambda.Function(this, 'Function', {
  functionName: 'my-function', // 阻止多次部署
  code: lambda.Code.fromAsset('lambda'),
  handler: 'index.handler',
  runtime: lambda.Runtime.NODEJS_20_X,
});

// 正确
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  // 让 CDK 生成名称
});
```

### ❌ 权限过于宽泛

```typescript
// 错误
function.addToRolePolicy(new iam.PolicyStatement({
  actions: ['*'],
  resources: ['*'],
}));

// 正确
table.grantReadWriteData(function);
```

### ❌ 手动依赖管理

```typescript
// 错误 - 手动打包
new lambda.Function(this, 'Function', {
  code: lambda.Code.fromAsset('lambda.zip'), // 手动预打包
  // ...
});

// 正确 - 让 CDK 处理
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  // CDK 自动处理打包
});
```

### ❌ 缺少环境变量

```typescript
// 错误
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  // 表名在 Lambda 代码中硬编码
});

// 正确
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  environment: {
    TABLE_NAME: table.tableName,
  },
});
```

### ❌ 忽略 Stack 输出

```typescript
// 错误 - 无法引用资源
new MyStack(app, 'Stack', {});

// 正确 - 导出重要值
class MyStack extends Stack {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    const api = new apigateway.RestApi(this, 'Api', {});

    new CfnOutput(this, 'ApiUrl', {
      value: api.url,
      description: 'API Gateway URL',
      exportName: 'MyApiUrl',
    });
  }
}
```

## 总结

- **始终** 让 CDK 生成资源名称，除非明确需要
- **使用** 高级构造 (L2/L3) 而不是低级构造 (L1)
- **优先使用** grant 方法进行 IAM 权限管理
- **利用** `NodejsFunction` 和 `PythonFunction` 进行自动打包
- **测试** Stack 使用断言和快照
- **优化** 成本基于环境（dev vs prod）
- **验证** 部署前的基础设施
- **记录** 自定义构造和模式
