---
name: test
description: 运行测试并智能分析结果
aliases: [t, run-test, unittest]
---

# 智能测试执行流程

自动运行项目测试，分析失败原因，并提供修复建议。

## 执行步骤

### 1. 检测测试框架

自动识别项目使用的测试框架：

**JavaScript/TypeScript**
- Jest (`package.json` 中有 `jest` 依赖)
- Mocha (`mocha` 依赖)
- Vitest (`vitest` 依赖)
- Cypress (E2E 测试)

**Python**
- pytest (`requirements.txt` 或 `pyproject.toml` 中)
- unittest (Python 内置)
- nose2

**Go**
- go test (标准测试)

**其他**
- 检查 `package.json` 的 `scripts.test`
- 检查 `Makefile` 的 test 目标

### 2. 运行测试

根据检测到的框架执行相应的测试命令：

```bash
# JavaScript
npm test
# 或
npm run test

# Python
pytest
# 或
python -m pytest

# Go
go test ./...
```

#### 可选参数

- `--coverage` - 生成覆盖率报告
- `--watch` - 监听模式（持续测试）
- `--verbose` - 详细输出
- 指定文件 - 只运行特定测试

### 3. 分析测试结果

#### 成功情况

输出测试统计：
```
✅ 测试全部通过！

统计信息：
- 总测试数：48
- 通过：48
- 失败：0
- 跳过：0
- 耗时：2.3s

覆盖率：
- 语句覆盖：85%
- 分支覆盖：78%
- 函数覆盖：92%
- 行覆盖：85%
```

#### 失败情况

详细分析每个失败的测试：

```
❌ 发现 3 个测试失败

【失败 1】用户登录测试
文件：tests/auth.test.js:45
错误：AssertionError: expected 200 to equal 401

分析：
- 测试期望未授权用户返回 401 状态码
- 实际返回了 200（成功）
- 可能原因：权限验证逻辑缺失

修复建议：
检查 src/api/auth.js:67 的权限验证逻辑
```

### 4. 定位问题代码

对于失败的测试：

1. **读取测试文件**
   ```javascript
   // tests/auth.test.js:45
   it('should return 401 for unauthorized user', async () => {
     const response = await request.get('/api/profile');
     expect(response.status).toBe(401);  // 失败在这里
   });
   ```

2. **读取被测代码**
   ```javascript
   // src/api/auth.js:67
   app.get('/api/profile', (req, res) => {
     // 缺少权限检查！
     res.json({ profile: getProfile() });
   });
   ```

3. **分析问题**
   - 缺少认证中间件
   - 未验证用户登录状态
   - 直接返回了数据

### 5. 提供修复建议

```markdown
## 修复建议

### 问题：缺少权限验证

**位置**: `src/api/auth.js:67`

**当前代码**:
```javascript
app.get('/api/profile', (req, res) => {
  res.json({ profile: getProfile() });
});
```

**修复后**:
```javascript
app.get('/api/profile', requireAuth, (req, res) => {
  res.json({ profile: getProfile(req.user.id) });
});
```

**说明**:
- 添加 `requireAuth` 中间件验证用户身份
- 未登录用户将收到 401 状态码
- 使用经过验证的用户 ID 获取个人资料
```

### 6. 重新运行测试

修复后，提示用户重新运行测试验证修复：
```bash
npm test -- auth.test.js
```

### 7. 生成测试报告

```markdown
## 测试执行报告

**执行时间**: 2025-11-30 14:30:00
**项目**: my-project
**分支**: feature/user-auth

### 测试概览

| 指标 | 数值 |
|------|------|
| 总测试数 | 48 |
| ✅ 通过 | 45 |
| ❌ 失败 | 3 |
| ⏭️ 跳过 | 0 |
| ⏱️ 耗时 | 2.3s |

### 失败详情

1. **用户登录测试** - `tests/auth.test.js:45`
   - 错误：权限验证缺失
   - 已提供修复建议

2. **数据验证测试** - `tests/validation.test.js:23`
   - 错误：边界值处理不当
   - 已提供修复建议

3. **API 响应格式测试** - `tests/api.test.js:67`
   - 错误：返回格式不一致
   - 已提供修复建议

### 覆盖率报告

| 类型 | 覆盖率 | 状态 |
|------|--------|------|
| 语句 | 85% | ✅ 良好 |
| 分支 | 78% | ⚠️ 需改进 |
| 函数 | 92% | ✅ 优秀 |
| 行 | 85% | ✅ 良好 |

### 建议

1. 优先修复失败的测试
2. 提高分支覆盖率至 80% 以上
3. 为新增功能添加测试用例
4. 考虑添加集成测试
```

## 测试场景

### 1. 快速测试（默认）

```
/test
```
运行所有测试，提供基本报告。

### 2. 测试特定文件

```
/test auth.test.js
```
只运行指定的测试文件。

### 3. 带覆盖率

```
/test --coverage
```
运行测试并生成覆盖率报告。

### 4. 监听模式

```
/test --watch
```
持续监听文件变化并自动运行测试。

### 5. 详细模式

```
/test --verbose
```
显示详细的测试输出。

## 测试最佳实践

### 1. 测试命名

```javascript
// ✅ 好的命名
describe('UserService', () => {
  describe('login', () => {
    it('should return token for valid credentials', () => {});
    it('should return 401 for invalid password', () => {});
    it('should return 404 for non-existent user', () => {});
  });
});

// ❌ 不好的命名
describe('test', () => {
  it('test1', () => {});
  it('test2', () => {});
});
```

### 2. 测试覆盖

**必须测试**:
- 正常流程（Happy Path）
- 错误处理
- 边界条件
- 异常情况

**示例**:
```javascript
describe('divide', () => {
  it('should divide two positive numbers', () => {
    expect(divide(10, 2)).toBe(5);
  });

  it('should handle division by zero', () => {
    expect(() => divide(10, 0)).toThrow('Division by zero');
  });

  it('should handle negative numbers', () => {
    expect(divide(-10, 2)).toBe(-5);
  });

  it('should handle floating point', () => {
    expect(divide(10, 3)).toBeCloseTo(3.33, 2);
  });
});
```

### 3. 测试隔离

每个测试应该独立，不依赖其他测试：

```javascript
// ✅ 好的实践
beforeEach(() => {
  // 每个测试前重置状态
  database.clear();
  user = createTestUser();
});

// ❌ 不好的实践
let userId;
it('should create user', () => {
  userId = createUser();  // 下一个测试依赖这个
});
it('should get user', () => {
  getUser(userId);  // 依赖上一个测试
});
```

### 4. 测试数据

使用工厂函数或 fixtures：

```javascript
// 测试数据工厂
function createTestUser(overrides = {}) {
  return {
    id: 1,
    name: 'Test User',
    email: 'test@example.com',
    ...overrides
  };
}

// 使用
it('should validate email', () => {
  const user = createTestUser({ email: 'invalid' });
  expect(validateUser(user)).toBe(false);
});
```

## 常见测试框架命令

### Jest

```bash
# 运行所有测试
npm test

# 运行特定文件
npm test -- auth.test.js

# 监听模式
npm test -- --watch

# 覆盖率
npm test -- --coverage

# 更新快照
npm test -- -u
```

### Pytest

```bash
# 运行所有测试
pytest

# 运行特定文件
pytest tests/test_auth.py

# 详细输出
pytest -v

# 覆盖率
pytest --cov=src

# 只运行失败的测试
pytest --lf
```

### Go Test

```bash
# 运行所有测试
go test ./...

# 详细输出
go test -v

# 覆盖率
go test -cover

# 运行特定测试
go test -run TestAuth
```

## 错误分析模式

### 1. 断言失败

```
AssertionError: expected 200 to equal 401

原因：
- 预期状态码不匹配
- 可能是权限验证缺失
- 或者测试用例错误
```

### 2. 超时错误

```
Timeout: async operation did not complete

原因：
- 异步操作未正确等待
- 死锁或无限循环
- 网络请求超时
```

### 3. 模拟错误

```
TypeError: mock.verify is not a function

原因：
- Mock 对象未正确设置
- 使用了不存在的方法
- Mock 库版本不兼容
```

## 自动修复建议

对于常见的测试失败模式，提供自动修复建议：

1. **权限验证缺失** → 添加认证中间件
2. **空值错误** → 添加空值检查
3. **类型错误** → 添加类型验证
4. **异步错误** → 正确使用 async/await
5. **Mock 错误** → 修复 Mock 配置
