# Superpowers

Obra 开发的强大工具包，包含 /brainstorm、/write-plan、/execute-plan 等命令，在做复杂项目时帮你讨论方案、脑暴、分析问题生成靠谱的方案。

## 功能简介

Superpowers 是由 @obra 开发的综合性开发工具包，提供从头脑风暴到执行计划的完整工作流支持。

### 核心特点

- ✅ **交互式设计**: 通过提问帮你优化方案
- ✅ **计划生成**: 自动创建详细的实现计划
- ✅ **批量执行**: 一次性执行多个计划步骤
- ✅ **社区活跃**: 持续更新，社区支持强

### 主要命令

| 命令 | 功能 | 适用场景 |
|------|------|---------|
| `/brainstorm` | 交互式设计优化 | 方案讨论、头脑风暴 |
| `/write-plan` | 创建实现计划 | 项目规划、任务分解 |
| `/execute-plan` | 批量执行计划 | 自动化执行、快速开发 |

---

## 仓库信息

### 主仓库

- **GitHub**: [obra/superpowers](https://github.com/obra/superpowers)
- **维护者**: [@obra](https://github.com/obra)
- **License**: 开源

### 相关仓库

| 仓库 | 说明 |
|------|------|
| [superpowers-lab](https://github.com/obra/superpowers-lab) | 实验性技能 |
| [superpowers-skills](https://github.com/obra/superpowers-skills) | 社区编辑技能 |
| [superpowers-marketplace](https://github.com/obra/superpowers-marketplace) | 精选插件市场 |

### 参考博客

- [Superpowers: How I'm using coding agents](https://blog.fsck.com/2025/10/09/superpowers/)

---

## 安装方法

### 方式 1：通过插件市场安装（推荐）

```bash
# 在 Claude Code 中执行
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

**优点**:
- 官方支持，稳定性好
- 自动更新
- 包含精选 Skills

### 方式 2：手动安装

```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/obra/superpowers
```

### 验证安装

```bash
# 检查安装
ls -la ~/.config/claude-code/skills/superpowers/

# 查看可用命令
# 在 Claude Code 中输入 /superpowers: 查看所有命令
```

---

## 核心功能

### 1. Brainstorm - 头脑风暴

交互式设计优化，通过提问帮你完善方案。

```
用户: /superpowers:brainstorm

Claude:
让我们通过几个问题来优化你的设计方案：

1. 这个功能的核心目标是什么？
2. 用户最常见的使用场景是？
3. 有哪些技术约束？
4. 性能要求是什么？

[根据你的回答，逐步优化方案]
```

**适用场景**:
- 新功能设计
- 架构选型
- 问题诊断
- 方案对比

### 2. Write Plan - 编写计划

基于讨论结果，生成详细的实现计划。

```
用户: /superpowers:write-plan

Claude:
基于我们的讨论，这是实现计划：

## 实现计划：用户登录功能

### Phase 1：数据库设计
- [ ] 创建 users 表
- [ ] 添加索引：email, username

### Phase 2：API 实现
- [ ] POST /api/login
- [ ] POST /api/register
- [ ] POST /api/logout

### Phase 3：前端集成
- [ ] 登录表单组件
- [ ] 错误处理
- [ ] Token 管理

### Phase 4：测试
- [ ] 单元测试
- [ ] 集成测试
- [ ] E2E 测试
```

### 3. Execute Plan - 执行计划

批量执行计划中的步骤。

```
用户: /superpowers:execute-plan

Claude:
开始执行计划...

[Task 1/10] 创建 users 表
✅ 完成

[Task 2/10] 添加索引
✅ 完成

[Task 3/10] 实现 POST /api/login
✅ 完成

...
```

---

## 使用示例

### 示例 1：新功能开发完整流程

```
步骤 1: 头脑风暴
用户: /superpowers:brainstorm
[讨论功能需求、技术方案]

步骤 2: 生成计划
用户: /superpowers:write-plan
[生成详细的实现计划]

步骤 3: 执行计划
用户: /superpowers:execute-plan
[自动化执行所有步骤]

步骤 4: 验证结果
[运行测试，确认功能正常]
```

### 示例 2：问题诊断

```
用户: "系统性能下降，帮我分析原因"
用户: /superpowers:brainstorm

Claude:
让我们通过几个问题定位问题：

1. 性能下降从什么时候开始？
2. 哪些操作变慢了？
3. 数据库查询耗时如何？
4. 内存和 CPU 使用情况？

[根据回答，逐步诊断]
```

### 示例 3：架构选型

```
用户: "选择数据库：PostgreSQL vs MongoDB"
用户: /superpowers:brainstorm

Claude:
让我们分析一下：

1. 数据结构：
   - 关系型数据？→ PostgreSQL
   - 文档型数据？→ MongoDB

2. 查询需求：
   - 复杂 JOIN？→ PostgreSQL
   - 灵活查询？→ MongoDB

3. 扩展性：
   - 垂直扩展？→ PostgreSQL
   - 水平扩展？→ MongoDB

[生成对比表和推荐方案]
```

---

## 进阶使用

### 组合使用多个 Skills

```
Superpowers（工作流管理）
  + Planning with Files（持久化规划）
  + Skill Creator（创建自定义 Skills）
  ↓
完整的项目开发工作流
```

### 自定义 Brainstorm 问题

可以创建自定义的头脑风暴模板：

```markdown
# 性能优化头脑风暴模板

1. 当前性能指标？
2. 性能目标？
3. 瓶颈在哪里？
4. 已尝试的优化？
5. 资源约束？
```

### 计划模板

创建可复用的计划模板：

```markdown
# API 开发计划模板

## Phase 1: 设计
- [ ] 定义 API 接口
- [ ] 设计数据模型
- [ ] 编写 API 文档

## Phase 2: 实现
- [ ] 实现路由
- [ ] 实现业务逻辑
- [ ] 错误处理

## Phase 3: 测试
- [ ] 单元测试
- [ ] 集成测试
- [ ] 性能测试
```

---

## 最佳实践

### 1. 充分利用 Brainstorm

```
不要直接要求实现，先 brainstorm：
❌ "帮我实现用户登录"
✅ "/superpowers:brainstorm 用户登录功能"
```

### 2. 分阶段执行计划

```
对于大型项目：
1. 先执行 Phase 1
2. 测试验证
3. 再执行 Phase 2
...
```

### 3. 保存计划文件

```
将生成的计划保存为文件：
- 便于版本控制
- 团队协作
- 进度追踪
```

---

## 常见问题

### Brainstorm 提问太多

**解决方法**:
- 提前准备好关键信息
- 明确告诉 Claude 你已知的部分
- 使用 "快速模式"（如果可用）

### Execute Plan 执行失败

**原因**:
- 计划步骤有依赖关系
- 环境配置问题

**解决方法**:
1. 检查依赖是否满足
2. 逐步执行，而非批量执行
3. 查看错误日志

### 与其他 Skills 冲突

**解决方法**:
- 明确指定使用哪个 Skill
- 检查 Skill 的触发条件
- 考虑禁用冲突的 Skills

---

## 参考资料

### 官方资源

- [Superpowers 主仓库](https://github.com/obra/superpowers)
- [Superpowers 博客](https://blog.fsck.com/2025/10/09/superpowers/)
- [插件市场](https://github.com/obra/superpowers-marketplace)

### 社区资源

- [Superpowers Lab](https://github.com/obra/superpowers-lab)
- [社区 Skills](https://github.com/obra/superpowers-skills)

### 相关 Skills

- [Planning with Files](03-planning-with-files.md)
- [Skill Creator](04-skill-creator.md)

---

**最后更新**: 2026-01-24
**难度**: ⭐⭐⭐ 进阶
**推荐指数**: ⭐⭐⭐⭐⭐

[返回 Top 10 列表](README.md) | [返回主页](../README.md)
