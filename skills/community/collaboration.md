# 协作管理 Skills

专注于团队协作、项目管理和 Git 工作流的 Skills。

## 🌟 精选推荐

| Skill | 功能 | 仓库链接 |
|-------|------|---------|
| **git-pushing** | 自动化 Git 操作 | [GitHub](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/git-pushing) |
| **review-implementing** | 评估代码实现计划 | [GitHub](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/review-implementing) |
| **test-fixing** | 检测失败测试并提出修复 | [GitHub](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/test-fixing) |

---

## 📦 完整列表

### Git 工作流

**git-pushing**
- **功能**: 自动化 git 操作和仓库交互
- **用途**: 简化提交、推送、分支管理
- **来源**: engineering-workflow-plugin

**using-git-worktrees**
- **功能**: 创建隔离的 git worktrees
- **特点**:
  - 智能目录选择
  - 安全验证
- **仓库**: [obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/)

### 代码审查

**review-implementing**
- **功能**: 评估代码实现计划并与规格对齐
- **流程**:
  1. 检查实现计划
  2. 对比规格说明
  3. 识别偏差
  4. 提出改进建议

### 测试管理

**test-fixing**
- **功能**: 检测失败的测试并提出补丁或修复
- **流程**:
  1. 运行测试套件
  2. 识别失败测试
  3. 分析失败原因
  4. 生成修复代码

---

## 💡 使用场景

### 场景 1：自动化 Git 工作流

```
任务：提交和推送代码更改

步骤：
1. 使用 git-pushing skill
2. 自动暂存更改
3. 生成提交消息
4. 推送到远程仓库
5. 创建 Pull Request（可选）
```

### 场景 2：代码审查流程

```
任务：审查团队成员的实现

步骤：
1. 查看实现计划
2. 使用 review-implementing skill
3. 对比规格说明
4. 识别问题和改进点
5. 提供反馈建议
```

### 场景 3：测试驱动修复

```
任务：修复失败的测试

步骤：
1. 运行测试套件
2. 使用 test-fixing skill 分析
3. 识别根本原因
4. 生成修复补丁
5. 验证修复效果
```

### 场景 4：并行开发

```
任务：同时开发多个功能

步骤：
1. 使用 using-git-worktrees
2. 为每个功能创建 worktree
3. 隔离开发环境
4. 独立测试和提交
5. 合并回主分支
```

---

## 🔧 最佳实践

### 1. Git 工作流规范

```
提交规范：
- 类型：feat, fix, docs, style, refactor, test, chore
- 格式：<type>: <subject>
- 示例：feat: 添加用户登录功能

分支策略：
- main: 生产环境
- develop: 开发环境
- feature/*: 功能分支
- hotfix/*: 紧急修复
```

### 2. 代码审查清单

```
审查要点：
□ 代码符合规格说明
□ 测试覆盖充分
□ 代码风格一致
□ 性能考虑合理
□ 安全问题检查
□ 文档更新完整
```

### 3. 测试策略

```
测试金字塔：
- 单元测试：70%
- 集成测试：20%
- E2E 测试：10%

失败处理：
1. 快速定位
2. 分析根因
3. 修复验证
4. 防止回归
```

---

## 📖 参考资料

### Skills 仓库

- [git-pushing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/git-pushing)
- [review-implementing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/review-implementing)
- [test-fixing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/test-fixing)
- [using-git-worktrees](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/)

### Git 资源

- [Git 官方文档](https://git-scm.com/doc)
- [Pro Git 书籍](https://git-scm.com/book/zh/v2)
- [Git Worktrees 指南](https://git-scm.com/docs/git-worktree)

### 团队协作

- [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Trunk Based Development](https://trunkbaseddevelopment.com/)
- [Code Review 最佳实践](https://google.github.io/eng-practices/review/)

---

**返回**: [社区导航](README.md) | [主页](../README.md)
