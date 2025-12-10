---
name: fix
description: 自动修复常见的代码问题
aliases: [autofix, lint-fix, format]
---

# 自动修复流程

智能检测并自动修复常见的代码质量问题、格式问题和 linter 错误。

## 执行步骤

### 1. 检测项目工具

自动识别项目使用的代码质量工具：

**JavaScript/TypeScript**
- ESLint (`eslintrc.js`, `.eslintrc.json`)
- Prettier (`.prettierrc`)
- TSLint (已废弃)

**Python**
- Black (代码格式化)
- isort (导入排序)
- autopep8 (PEP 8 修复)
- pylint

**Go**
- gofmt (标准格式化)
- goimports (导入管理)
- golangci-lint

**其他**
- EditorConfig (`.editorconfig`)
- Stylelint (CSS/SCSS)

### 2. 运行 Linter 检查

首先运行 linter 检测问题：

```bash
# JavaScript/TypeScript
npx eslint . --ext .js,.jsx,.ts,.tsx

# Python
pylint src/
# 或
flake8 src/

# Go
golangci-lint run
```

分析 lint 结果：

```markdown
## Lint 检查报告

发现 15 个问题：
- 🔴 错误：3 个
- 🟡 警告：8 个
- ℹ️ 信息：4 个

### 可自动修复

✅ 12 个问题可以自动修复
⚠️ 3 个问题需要手动处理

### 问题分类

**格式问题** (8个) - 可自动修复
- 缩进不一致
- 缺少分号
- 引号风格不统一
- 行尾空格

**代码质量** (4个) - 可自动修复
- 未使用的变量
- 未使用的导入
- console.log 语句
- 重复的导入

**需要手动修复** (3个)
- 未处理的 Promise
- 缺少错误处理
- 复杂度过高的函数
```

### 3. 自动修复

#### 步骤 1: 运行格式化工具

```bash
# JavaScript/TypeScript - Prettier
npx prettier --write \"**/*.{js,jsx,ts,tsx,json,css,md}\"

# Python - Black
black src/

# Python - isort (导入排序)
isort src/

# Go - gofmt
gofmt -w .

# Go - goimports
goimports -w .
```

#### 步骤 2: 运行 ESLint 自动修复

```bash
# JavaScript/TypeScript
npx eslint . --ext .js,.jsx,.ts,.tsx --fix

# 只修复特定文件
npx eslint src/api.js --fix
```

#### 步骤 3: 运行其他修复工具

```bash
# Python - autopep8
autopep8 --in-place --aggressive --aggressive src/**/*.py

# Stylelint (CSS)
npx stylelint \"**/*.css\" --fix
```

### 4. 验证修复结果

再次运行 linter 确认问题已修复：

```bash
# 重新检查
npm run lint
```

输出修复报告：

```markdown
## 自动修复报告

### 修复概览

✅ 成功修复：12 个问题
⚠️ 需要手动处理：3 个问题

### 修复详情

#### 格式问题 (8个) ✅

1. **缩进统一**
   - 修复文件：15 个
   - 统一使用 2 空格缩进

2. **引号风格**
   - 修复文件：8 个
   - 统一使用单引号

3. **行尾分号**
   - 修复文件：6 个
   - 添加缺失的分号

4. **行尾空格**
   - 修复文件：12 个
   - 移除多余空格

#### 代码质量 (4个) ✅

1. **未使用的导入**
   ```diff
   - import { useState, useEffect, useMemo } from 'react';
   + import { useState, useEffect } from 'react';
   ```
   修复文件：5 个

2. **未使用的变量**
   ```diff
   - const temp = getData();
   - const result = processData();
   + const result = processData();
   ```
   修复文件：3 个

3. **console.log 移除**
   ```diff
   - console.log('Debug:', data);
     return data;
   ```
   修复文件：4 个

4. **重复导入**
   ```diff
   - import { Button } from './Button';
   - import { Input } from './Input';
   - import { Button } from './Button';  // 重复
   + import { Button } from './Button';
   + import { Input } from './Input';
   ```
   修复文件：2 个

#### 需要手动处理 (3个) ⚠️

1. **未处理的 Promise** - `src/api/user.js:45`
   ```javascript
   // 当前代码
   fetchData();  // Promise 未处理

   // 建议修复
   await fetchData();
   // 或
   fetchData().catch(handleError);
   ```

2. **缺少错误处理** - `src/utils/parser.js:78`
   ```javascript
   // 当前代码
   const data = JSON.parse(input);

   // 建议修复
   try {
     const data = JSON.parse(input);
   } catch (error) {
     handleError(error);
   }
   ```

3. **函数复杂度过高** - `src/services/process.js:120`
   ```javascript
   // 复杂度：25 (建议 < 15)
   function processOrder(order) {
     // 150 行复杂逻辑...
   }

   // 建议：拆分为多个小函数
   function processOrder(order) {
     validateOrder(order);
     calculateTotal(order);
     applyDiscounts(order);
     updateInventory(order);
     sendConfirmation(order);
   }
   ```
```

### 5. 提供手动修复建议

对于无法自动修复的问题，提供详细的修复指导：

```markdown
## 手动修复指南

### 问题 1: 未处理的 Promise

**位置**: `src/api/user.js:45`

**问题代码**:
```javascript
function loadUser() {
  fetchUserData();  // ❌ Promise 未处理
  return user;
}
```

**修复方案**:

**方案 A: 使用 async/await**
```javascript
async function loadUser() {
  await fetchUserData();
  return user;
}
```

**方案 B: 使用 .then()**
```javascript
function loadUser() {
  return fetchUserData().then(() => user);
}
```

**方案 C: 添加错误处理**
```javascript
async function loadUser() {
  try {
    await fetchUserData();
    return user;
  } catch (error) {
    console.error('Failed to load user:', error);
    throw error;
  }
}
```

**推荐**: 方案 C（包含错误处理）

---

### 问题 2: 缺少错误处理

**位置**: `src/utils/parser.js:78`

**问题代码**:
```javascript
function parseConfig(input) {
  const config = JSON.parse(input);  // ❌ 可能抛出异常
  return config;
}
```

**修复方案**:

```javascript
function parseConfig(input) {
  try {
    const config = JSON.parse(input);
    return config;
  } catch (error) {
    console.error('Invalid JSON:', error);
    return {};  // 返回默认值
    // 或重新抛出自定义错误
    // throw new ConfigError('Failed to parse config', error);
  }
}
```

---

### 问题 3: 函数复杂度过高

**位置**: `src/services/process.js:120`

**问题**: 函数复杂度 25（建议 < 15）

**重构建议**:

**当前代码结构**:
```javascript
function processOrder(order) {
  // 验证逻辑 (30 行)
  // 计算逻辑 (40 行)
  // 折扣逻辑 (25 行)
  // 库存更新 (20 行)
  // 通知发送 (15 行)
  // 日志记录 (20 行)
}
```

**重构后**:
```javascript
function processOrder(order) {
  validateOrder(order);
  const total = calculateTotal(order);
  const discount = applyDiscounts(order, total);
  updateInventory(order);
  sendConfirmation(order);
  logOrderProcessing(order);
}

function validateOrder(order) {
  // 验证逻辑
}

function calculateTotal(order) {
  // 计算逻辑
  return total;
}

function applyDiscounts(order, total) {
  // 折扣逻辑
  return discount;
}

function updateInventory(order) {
  // 库存更新
}

function sendConfirmation(order) {
  // 通知发送
}

function logOrderProcessing(order) {
  // 日志记录
}
```

**优势**:
- ✅ 每个函数职责单一
- ✅ 易于测试
- ✅ 易于维护
- ✅ 复杂度降低
```

### 6. 运行测试验证

修复后运行测试确保没有引入新问题：

```bash
# 运行测试
npm test

# 运行构建
npm run build
```

### 7. 生成最终报告

```markdown
## 代码修复最终报告

**执行时间**: 2025-11-30 15:30:00
**修复范围**: 全项目

### 修复统计

| 类别 | 检测到 | 自动修复 | 手动修复 | 剩余 |
|------|--------|---------|---------|------|
| 错误 | 3 | 0 | 3 | 0 |
| 警告 | 8 | 8 | 0 | 0 |
| 信息 | 4 | 4 | 0 | 0 |
| **总计** | **15** | **12** | **3** | **0** |

### 修复的文件

总计修改：23 个文件

**JavaScript/TypeScript** (18个)
- src/api/*.js (5个)
- src/components/*.tsx (8个)
- src/utils/*.ts (5个)

**样式文件** (3个)
- src/styles/*.css (3个)

**配置文件** (2个)
- package.json
- tsconfig.json

### 代码质量提升

**修复前**:
- Lint 错误：15 个
- 代码格式：不统一
- 未使用代码：7 处

**修复后**:
- Lint 错误：0 个 ✅
- 代码格式：统一 ✅
- 未使用代码：0 处 ✅

### 下一步行动

- [x] 自动修复完成
- [x] 测试通过
- [ ] 人工审查手动修复建议
- [ ] 应用手动修复
- [ ] 提交代码

### 建议

1. 配置 Git pre-commit hook 自动运行 lint fix
2. 在 CI/CD 中添加代码质量检查
3. 定期运行 /fix 命令保持代码质量
```

## 修复类型

### 1. 格式修复

**自动处理**:
- 缩进统一
- 引号风格
- 分号规则
- 行尾空格
- 换行符

**配置示例** (`.prettierrc`):
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 80
}
```

### 2. Import 优化

**自动处理**:
- 移除未使用的 import
- 排序 import 语句
- 移除重复 import
- 合并 import

**示例**:
```javascript
// 修复前
import { Button } from './Button';
import React from 'react';
import { Input } from './Input';
import { Button } from './Button';  // 重复

// 修复后
import React from 'react';
import { Button } from './Button';
import { Input } from './Input';
```

### 3. 代码清理

**自动处理**:
- 移除未使用的变量
- 移除 console.log
- 移除 debugger
- 移除注释掉的代码

### 4. 类型问题 (TypeScript)

**部分自动**:
- 添加缺失的类型注解
- 修复简单的类型错误
- 移除不必要的类型断言

## 配置项目工具

### 1. 设置 ESLint

```bash
npm install --save-dev eslint
npx eslint --init
```

### 2. 设置 Prettier

```bash
npm install --save-dev prettier
echo {} > .prettierrc.json
```

### 3. 集成 ESLint + Prettier

```bash
npm install --save-dev eslint-config-prettier eslint-plugin-prettier
```

`.eslintrc.json`:
```json
{
  "extends": [
    "eslint:recommended",
    "plugin:prettier/recommended"
  ]
}
```

### 4. 添加 npm 脚本

`package.json`:
```json
{
  "scripts": {
    "lint": "eslint . --ext .js,.jsx,.ts,.tsx",
    "lint:fix": "eslint . --ext .js,.jsx,.ts,.tsx --fix",
    "format": "prettier --write \"**/*.{js,jsx,ts,tsx,json,css,md}\""
  }
}
```

### 5. 配置 Git Hooks

使用 husky 和 lint-staged:

```bash
npm install --save-dev husky lint-staged
npx husky install
```

`package.json`:
```json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,css,md}": ["prettier --write"]
  }
}
```

## 使用场景

### 场景 1: 提交前修复

```bash
/fix
```
在提交代码前运行，确保代码质量。

### 场景 2: PR 审查前

```bash
/fix && /test
```
修复问题并运行测试。

### 场景 3: 合并代码后

```bash
/fix
```
合并代码后统一代码风格。

### 场景 4: 接手遗留项目

```bash
/fix
```
快速提升遗留代码质量。

## 最佳实践

### 1. 定期运行

建议频率：
- 每次提交前
- 合并代码后
- 每周集中修复一次

### 2. 增量修复

对于大项目：
```bash
# 只修复指定目录
npx eslint src/api --fix

# 只修复最近修改的文件
git diff --name-only | xargs npx eslint --fix
```

### 3. 团队规范

- 统一团队的 lint 和 format 配置
- 将配置文件提交到版本控制
- 在 CI/CD 中强制执行

### 4. 自动化

- 设置 Git pre-commit hook
- CI/CD 中添加检查
- IDE 集成自动修复
