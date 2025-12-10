---
name: update
description: 智能更新项目依赖
aliases: [upgrade, dep-update, deps]
---

# 智能依赖更新流程

安全地检查、分析和更新项目依赖，确保兼容性和稳定性。

## 执行步骤

### 1. 检测包管理器

自动识别项目使用的包管理器：

**JavaScript/TypeScript**
- npm (`package-lock.json`)
- yarn (`yarn.lock`)
- pnpm (`pnpm-lock.yaml`)

**Python**
- pip (`requirements.txt`)
- poetry (`poetry.lock`)
- pipenv (`Pipfile.lock`)

**Go**
- go modules (`go.mod`)

**Rust**
- Cargo (`Cargo.lock`)

### 2. 检查过期依赖

运行相应的命令检查过期的依赖：

```bash
# JavaScript/TypeScript
npm outdated
# 或
yarn outdated
# 或
pnpm outdated

# Python
pip list --outdated
# 或
poetry show --outdated

# Go
go list -u -m all

# Rust
cargo outdated
```

### 3. 分析过期依赖

生成详细的过期依赖报告：

```markdown
## 过期依赖分析报告

### 依赖概览

| 包名 | 当前版本 | 最新版本 | 类型 | 风险级别 |
|------|---------|---------|------|---------|
| react | 17.0.2 | 18.2.0 | 主依赖 | 🟡 中 |
| lodash | 4.17.15 | 4.17.21 | 主依赖 | 🔴 高 |
| jest | 27.0.0 | 29.5.0 | 开发依赖 | 🟢 低 |
| webpack | 5.70.0 | 5.88.0 | 开发依赖 | 🟡 中 |

### 详细分析

#### 🔴 高优先级更新

**lodash (4.17.15 → 4.17.21)**
- 原因：包含安全漏洞修复
- 类型：补丁版本
- 兼容性：✅ 向后兼容
- 建议：立即更新

**变更内容**:
- 修复原型污染漏洞 (CVE-2020-8203)
- 修复 ReDoS 漏洞
- 无破坏性变更

#### 🟡 中优先级更新

**react (17.0.2 → 18.2.0)**
- 原因：主版本更新
- 类型：主版本
- 兼容性：⚠️ 可能有破坏性变更
- 建议：测试后更新

**变更内容**:
- 新增并发特性
- 自动批处理
- Suspense 改进
- ⚠️ 需要更新相关生态系统包

**迁移步骤**:
1. 更新 react 和 react-dom
2. 更新 @testing-library/react
3. 检查并更新其他 React 相关包
4. 运行测试确保兼容性

#### 🟢 低优先级更新

**jest (27.0.0 → 29.5.0)**
- 原因：次版本更新
- 类型：次版本
- 兼容性：✅ 向后兼容
- 建议：方便时更新

**变更内容**:
- 性能改进
- 新增快照特性
- Bug 修复
- 无破坏性变更
```

### 4. 询问更新策略

向用户提供以下选项：

**选项 1: 全部更新**
```bash
npm update
```
- 更新所有包到允许的最新版本
- 遵守 package.json 中的版本范围
- 风险：中等

**选项 2: 选择性更新**
询问用户要更新哪些包：
- [ ] lodash (安全更新，推荐)
- [ ] webpack (功能更新)
- [ ] react (主版本，需测试)
- [ ] jest (可选)

**选项 3: 仅安全更新**
```bash
npm audit fix
```
- 只更新有安全漏洞的包
- 最安全的选择

**选项 4: 仅补丁版本**
```bash
npm update --depth 0
```
- 只更新补丁版本（x.x.X）
- 最小风险

### 5. 执行更新

根据用户选择执行相应的更新命令：

#### 全部更新

```bash
# 备份当前依赖
cp package.json package.json.backup
cp package-lock.json package-lock.json.backup

# 更新依赖
npm update

# Python
pip install --upgrade -r requirements.txt
```

#### 选择性更新

```bash
# 更新指定包
npm install lodash@latest
npm install webpack@latest

# Python
pip install --upgrade lodash webpack
```

#### 主版本更新

```bash
# 更新主版本（需要手动）
npm install react@latest react-dom@latest
```

### 6. 安全审计

更新后运行安全审计：

```bash
# JavaScript
npm audit

# Python
pip-audit
# 或
safety check

# Go
go mod verify
```

分析安全报告：

```markdown
## 安全审计报告

### 漏洞概览

- 🔴 严重：0
- 🟠 高危：0
- 🟡 中危：1
- 🟢 低危：2

### 详细信息

#### 中危漏洞

**包名**: lodash
**版本**: 4.17.15
**漏洞**: 原型污染
**CVE**: CVE-2020-8203
**修复版本**: 4.17.21

**影响**:
- 允许攻击者修改对象原型
- 可能导致拒绝服务

**修复**:
```bash
npm install lodash@4.17.21
```

### 审计建议

✅ 已修复所有高危和严重漏洞
⚠️ 建议修复中危漏洞
ℹ️ 低危漏洞可选择性修复
```

### 7. 运行测试

更新后自动运行测试确保兼容性：

```bash
# 运行测试
npm test

# 运行构建
npm run build
```

分析测试结果：

```markdown
## 更新后测试报告

### 测试结果

✅ 所有测试通过（48/48）

### 构建状态

✅ 构建成功

### 兼容性检查

- [ ] 单元测试：通过 ✅
- [ ] 集成测试：通过 ✅
- [ ] E2E 测试：通过 ✅
- [ ] 构建：成功 ✅
- [ ] Linter：通过 ✅

### 结论

所有检查通过，依赖更新成功！
```

### 8. 生成更新报告

```markdown
## 依赖更新报告

**更新时间**: 2025-11-30 15:00:00
**项目**: my-project

### 更新汇总

**更新数量**: 5 个包
**更新类型**:
- 主版本：1
- 次版本：2
- 补丁版本：2

### 更新详情

| 包名 | 旧版本 | 新版本 | 类型 | 状态 |
|------|--------|--------|------|------|
| lodash | 4.17.15 | 4.17.21 | 补丁 | ✅ |
| webpack | 5.70.0 | 5.88.0 | 次版本 | ✅ |
| react | 17.0.2 | 18.2.0 | 主版本 | ✅ |
| jest | 27.0.0 | 29.5.0 | 主版本 | ✅ |
| eslint | 8.20.0 | 8.45.0 | 次版本 | ✅ |

### 变更说明

**lodash 4.17.21**
- 🔒 修复安全漏洞 CVE-2020-8203
- 无破坏性变更

**webpack 5.88.0**
- ⚡ 构建性能提升
- 🐛 Bug 修复
- 新增功能：持久化缓存改进

**react 18.2.0**
- 🎉 新增并发特性
- ⚡ 自动批处理
- ⚠️ API 变更
- 📚 需要更新文档

**jest 29.5.0**
- ⚡ 测试速度提升 30%
- 🎯 新增快照特性
- 🐛 修复已知问题

**eslint 8.45.0**
- 🔍 新增规则
- 🐛 Bug 修复

### 后续任务

- [x] 更新依赖
- [x] 运行测试
- [x] 构建验证
- [ ] 更新文档（React 18 新特性）
- [ ] 团队培训（React 并发特性）
- [ ] 监控生产环境

### 风险评估

**整体风险**: 🟡 中等

**主要风险点**:
- React 18 主版本更新需要团队熟悉新特性
- 建议先在测试环境验证

**缓解措施**:
- 已通过所有测试
- 准备回滚方案（保留备份）
- 增量部署策略
```

## 更新最佳实践

### 1. 定期更新

建议频率：
- 🔴 安全更新：立即
- 🟡 补丁版本：每月
- 🟢 次版本：每季度
- 🔵 主版本：谨慎评估

### 2. 更新前准备

```bash
# 1. 创建分支
git checkout -b deps/update-2025-11-30

# 2. 备份依赖文件
cp package.json package.json.backup
cp package-lock.json package-lock.json.backup

# 3. 确保测试完整
npm test
```

### 3. 渐进式更新

对于主版本更新：

```bash
# 阶段 1: 更新兼容的次要依赖
npm update --depth 0

# 阶段 2: 逐个更新主要依赖
npm install react@18 react-dom@18

# 阶段 3: 更新相关生态
npm install @testing-library/react@latest

# 阶段 4: 测试和验证
npm test && npm run build
```

### 4. 版本锁定策略

```json
{
  "dependencies": {
    "react": "18.2.0",          // 精确版本
    "lodash": "^4.17.21",       // 允许补丁和次版本
    "express": "~4.18.0"        // 只允许补丁版本
  }
}
```

策略建议：
- 核心依赖：精确版本
- 工具库：允许次版本 (^)
- 开发依赖：宽松限制

### 5. 回滚准备

```bash
# 如果更新出现问题，快速回滚
cp package.json.backup package.json
cp package-lock.json.backup package-lock.json
npm install
```

## 常见问题处理

### 1. 依赖冲突

```bash
# 查看依赖树
npm ls package-name

# 解决方案
npm install --legacy-peer-deps
# 或
npm install --force
```

### 2. 版本不兼容

检查 changelog 和 breaking changes：
```bash
# 查看包的变更日志
npm view package-name versions
npm view package-name@version
```

### 3. 更新失败

```bash
# 清理缓存
npm cache clean --force

# 删除并重新安装
rm -rf node_modules package-lock.json
npm install
```

### 4. 安全漏洞无法修复

```bash
# 查看详细信息
npm audit

# 尝试自动修复
npm audit fix

# 强制修复（可能引入破坏性变更）
npm audit fix --force

# 如果无法修复，考虑替代方案
```

## 更新策略矩阵

| 更新类型 | 风险 | 测试要求 | 审批 | 频率 |
|---------|------|---------|------|------|
| 安全补丁 | 低 | 基础测试 | 无需 | 立即 |
| 补丁版本 | 低 | 完整测试 | 无需 | 每月 |
| 次版本 | 中 | 完整测试 + 回归 | 建议 | 每季度 |
| 主版本 | 高 | 全面测试 + 性能 | 必须 | 谨慎 |
| Beta/RC | 极高 | 仅测试环境 | 必须 | 按需 |
