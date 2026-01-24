# Planning with Files

复刻 Manus 的 Skill，使用持久化文件作为"外部记忆"，有效解决上下文飘移问题。

## 功能简介

Planning with Files 是基于价值 20 亿美元的 Manus 工作流模式，通过持久化 Markdown 文件来管理任务规划和进度跟踪。

### 核心特点

- ✅ **外部记忆**: 使用 Markdown 文件作为持久化存储
- ✅ **解决上下文限制**: 避免 AI 对话中的上下文丢失
- ✅ **任务规划**: 通过 `task_plan.md` 进行任务管理
- ✅ **进度跟踪**: 通过 `notes.md` 记录工作笔记

### 适用场景

| 场景 | 说明 |
|------|------|
| **复杂项目** | 多步骤、长周期的项目开发 |
| **团队协作** | 多人参与的项目，需要清晰的任务分工 |
| **长期维护** | 需要持续跟踪进度的项目 |
| **上下文管理** | 避免 AI 对话中的信息丢失 |

---

## 仓库信息

- **GitHub**: [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)
- **维护者**: [@OthmanAdi](https://github.com/OthmanAdi)
- **License**: 开源
- **背景**: 基于 Manus（价值 20 亿美元）的工作流模式

### 参考资料

- [Quickstart Guide](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)
- [Skillplugs 页面](https://skillplugs.com/skills/OthmanAdi/planning-with-files)

---

## 安装方法

### 快速安装

```bash
# 创建 skills 目录
mkdir -p ~/.config/claude-code/skills/

# 进入目录
cd ~/.config/claude-code/skills/

# 克隆仓库
git clone https://github.com/OthmanAdi/planning-with-files planning-with-files
```

### 验证安装

```bash
# 检查 SKILL.md
head ~/.config/claude-code/skills/planning-with-files/SKILL.md

# 查看文件结构
ls -la ~/.config/claude-code/skills/planning-with-files/
```

---

## 核心理念

### Manus 工作流

Manus 是一个价值 20 亿美元的 AI 助手项目，其核心理念是：

```
传统 AI 对话的问题:
  对话上下文有限 → 长期项目信息丢失
  没有持久化存储 → 每次从头开始
  缺乏结构化管理 → 任务混乱

Manus 解决方案:
  使用文件作为"外部记忆"
  持久化任务规划和笔记
  结构化的工作流程
```

### Planning with Files 的实现

通过两个核心文件实现：

1. **task_plan.md**: 任务规划和待办事项
2. **notes.md**: 工作笔记和进度记录

---

## 配置和使用

### 初始化项目

在项目根目录创建规划文件：

```bash
# 创建规划文件
touch task_plan.md notes.md

# 或使用 Skill 自动创建
```

### task_plan.md 结构

```markdown
# 项目规划：[项目名称]

## 当前状态
- **阶段**: 需求分析
- **进度**: 30%
- **下一步**: 完成 API 设计

## 任务列表

### 待办任务
- [ ] 完成用户需求文档
- [ ] 设计 API 接口
- [ ] 搭建开发环境

### 进行中
- [x] 项目初始化
- [ ] 数据库设计（50%）

### 已完成
- [x] 项目立项
- [x] 技术选型

## 里程碑

- [ ] MVP 版本（2026-02-15）
- [ ] Beta 测试（2026-03-01）
- [ ] 正式发布（2026-03-15）

## 资源和依赖

- **团队成员**: Alice（后端）, Bob（前端）
- **技术栈**: Node.js, React, PostgreSQL
- **外部依赖**: 支付 API, 邮件服务
```

### notes.md 结构

```markdown
# 工作笔记：[项目名称]

## 2026-01-24

### 完成的工作
- 完成项目初始化
- 搭建 Git 仓库
- 创建基础目录结构

### 遇到的问题
- 依赖包版本冲突
  - 解决方案：使用 npm-force-resolutions

### 下次工作
- 开始数据库设计
- 准备 API 文档模板

## 2026-01-23

### 完成的工作
- 完成技术选型
- ...
```

---

## 使用示例

### 示例 1：项目启动

```
用户: "帮我启动一个新的 Web 项目，使用 planning-with-files"

Claude:
1. 创建 task_plan.md 和 notes.md
2. 初始化任务列表
3. 记录项目背景和目标

已创建规划文件，可以开始项目开发了。
```

### 示例 2：任务更新

```
用户: "更新任务进度：数据库设计已完成"

Claude:
已更新 task_plan.md：
- [x] 数据库设计（100%，移至已完成）

已更新 notes.md：
添加了今日工作记录。
```

### 示例 3：进度查询

```
用户: "项目目前进度如何？"

Claude:
根据 task_plan.md：
- 当前阶段：开发阶段
- 整体进度：45%
- 待办任务：5 个
- 进行中任务：2 个
- 已完成任务：8 个
- 下一个里程碑：MVP 版本（2026-02-15）
```

---

## 进阶使用

### 多项目管理

为每个项目创建独立的规划文件：

```
project-a/
  ├── task_plan.md
  └── notes.md

project-b/
  ├── task_plan.md
  └── notes.md
```

### 集成其他工具

与其他 Skills 配合使用：

```
Planning with Files（任务管理）
  + Obsidian Skills（知识管理）
  + Superpowers（工作流增强）
  ↓
完整的项目管理系统
```

### 自定义模板

创建自己的规划模板：

```bash
# 创建模板目录
mkdir -p ~/.claude/templates/

# 创建自定义模板
cat > ~/.claude/templates/task_plan_template.md <<'EOF'
# 项目规划：{{project_name}}

## 项目信息
- **负责人**: {{owner}}
- **开始日期**: {{start_date}}
- **预计完成**: {{end_date}}

## 当前状态
...
EOF
```

---

## 最佳实践

### 1. 定期更新

```
建议更新频率：
- task_plan.md: 每完成一个任务就更新
- notes.md: 每天记录工作笔记
- 定期回顾：每周回顾一次进度
```

### 2. 清晰的任务描述

```markdown
❌ 不好的任务描述：
- [ ] 做后端

✅ 好的任务描述：
- [ ] 实现用户登录 API（包含注册、登录、登出）
```

### 3. 使用标签和优先级

```markdown
- [ ] [P0] 修复生产环境的严重 bug #bug #urgent
- [ ] [P1] 实现用户反馈功能 #feature
- [ ] [P2] 优化数据库查询性能 #optimization
```

### 4. 记录决策过程

在 notes.md 中记录重要决策：

```markdown
### 技术决策：使用 PostgreSQL 而非 MongoDB

**原因**:
1. 需要强一致性事务
2. 数据关系复杂
3. 团队更熟悉 SQL

**权衡**:
- 优点：数据完整性好，查询灵活
- 缺点：横向扩展相对困难
```

---

## 故障排除

### 文件未生效

**问题**: Claude 没有使用规划文件

**解决方法**:
1. 确保文件名正确：`task_plan.md`, `notes.md`
2. 文件放在项目根目录
3. 重启 Claude Code

### 格式混乱

**问题**: 规划文件格式不一致

**解决方法**:
1. 使用统一的模板
2. 定期整理和格式化
3. 使用 Markdown lint 工具检查

### 信息过载

**问题**: notes.md 变得太长难以管理

**解决方法**:
1. 定期归档：将旧笔记移到 `notes-archive/`
2. 按月份分割：`notes-2026-01.md`, `notes-2026-02.md`
3. 只保留最近的关键信息

---

## 参考资料

### 官方资源

- [Planning with Files 仓库](https://github.com/OthmanAdi/planning-with-files)
- [Quickstart Guide](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)
- [Skillplugs 页面](https://skillplugs.com/skills/OthmanAdi/planning-with-files)

### Manus 相关

- [Manus 官方博客](https://www.manus.ai/blog)
- [Manus 工作流介绍](https://www.manus.ai/workflow)

### 相关 Skills

- [Superpowers](06-superpowers.md) - 包含类似的规划功能
- [Obsidian Skills](02-obsidian.md) - 知识管理和笔记

### 项目管理最佳实践

- [Getting Things Done (GTD)](https://gettingthingsdone.com/)
- [Agile 项目管理](https://www.agilealliance.org/)
- [PARA 方法](https://fortelabs.co/blog/para/)

---

**最后更新**: 2026-01-24
**难度**: ⭐⭐ 中等
**推荐指数**: ⭐⭐⭐⭐

[返回 Top 10 列表](README.md) | [返回主页](../README.md)
