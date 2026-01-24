# Obsidian Skills

Obsidian CEO 出品的 Skill 套件，功能全面，覆盖 Markdown、Canvas、插件开发等。

## 功能简介

Obsidian Skills 是由 Obsidian 创始人 Kepano 开发的官方 Skill 套件，为 Claude 提供了完整的 Obsidian 工作流支持。

### 核心特点

- ✅ **官方出品**: Obsidian 创始人维护，质量保证
- ✅ **功能全面**: 覆盖 Markdown、Canvas、插件开发
- ✅ **生态丰富**: 多个相关技能包，满足不同需求
- ✅ **持续更新**: 活跃的社区支持和定期更新

### 适用场景

| 场景 | 说明 |
|------|------|
| **知识管理** | 使用 Obsidian 构建第二大脑 |
| **笔记整理** | Markdown 文档编写和组织 |
| **可视化思维** | Canvas 画布创作和脑图绘制 |
| **插件开发** | 为 Obsidian 开发自定义插件 |

---

## 仓库信息

### 主仓库

- **GitHub**: [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)
- **维护者**: [@kepano](https://github.com/kepano) (Obsidian CEO)
- **License**: MIT

### 相关技能包

| 技能包 | 仓库 | 功能 |
|--------|------|------|
| **Obsidian Visual Skills** | [axtonliu/axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills) | 可视化技能包 |
| **Obsidian Plugin开发** | [gapmiss/obsidian-plugin-skill](https://github.com/gapmiss/obsidian-plugin-skill) | 插件开发 |
| **Obsidian PKM套件** | [ballred/obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm) | 完整 PKM 系统 |

---

## 安装方法

### 1. 主 Skill 安装（推荐）

```bash
# 创建 skills 目录
mkdir -p ~/.config/claude-code/skills/

# 进入目录
cd ~/.config/claude-code/skills/

# 克隆主仓库
git clone https://github.com/kepano/obsidian-skills obsidian
```

### 2. 可视化技能包（可选）

适用于需要生成 Obsidian 风格 Markdown、Canvas、DataView 的场景。

```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/axtonliu/axton-obsidian-visual-skills obsidian-visual
```

**功能**:
- 直接写出 Obsidian 风格的 Markdown
- 生成 DataView 插件的过滤器和公式
- 生成 Canvas 无限画布

### 3. 插件开发 Skill（可选）

适用于 Obsidian 插件开发者。

```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/gapmiss/obsidian-plugin-skill obsidian-plugin
```

### 4. PKM 完整套件（可选）

包含完整的个人知识管理（PKM）工作流。

```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/ballred/obsidian-claude-pkm obsidian-pkm
```

### 验证安装

```bash
# 检查主 Skill
head ~/.config/claude-code/skills/obsidian/SKILL.md

# 列出所有 Obsidian 相关 Skills
ls -d ~/.config/claude-code/skills/obsidian*
```

---

## 配置和使用

### 基础使用 - Markdown 编写

```
用户: "帮我创建一个项目笔记，使用 Obsidian 格式"

Claude: [生成符合 Obsidian 规范的 Markdown]
# 项目笔记

#project #active

## 概述
...

## 任务
- [ ] 任务 1
- [ ] 任务 2

## 相关笔记
[[相关笔记1]]
[[相关笔记2]]
```

### 进阶使用 - Canvas 画布

使用可视化技能包生成 Canvas：

```
用户: "创建一个项目规划的 Canvas 画布"

Claude: [生成 .canvas 文件]
{
  "nodes": [
    {"id": "1", "type": "text", "text": "项目目标", "x": 0, "y": 0},
    {"id": "2", "type": "text", "text": "任务1", "x": 200, "y": 100}
  ],
  "edges": [
    {"fromNode": "1", "toNode": "2"}
  ]
}
```

### DataView 查询

使用可视化技能包生成 DataView 查询：

```
用户: "创建一个查询所有活跃项目的 DataView"

Claude:
\```dataview
TABLE
  status,
  deadline,
  tags
FROM #project
WHERE status = "active"
SORT deadline ASC
\```
```

---

## 插件开发

### 使用插件开发 Skill

安装 `obsidian-plugin` Skill 后，可以直接创建插件：

```
用户: "帮我创建一个 Obsidian 插件，功能是自动生成每日笔记的摘要"

Claude: [按照 Obsidian API 规范生成插件代码]
```

### 插件结构

```typescript
// main.ts
import { Plugin } from 'obsidian';

export default class MyPlugin extends Plugin {
    async onload() {
        // 插件加载时的逻辑
    }

    async onunload() {
        // 插件卸载时的清理
    }
}
```

---

## PKM 工作流

### 使用 PKM 套件

安装 `obsidian-pkm` Skill 后，获得完整的知识管理工作流：

1. **笔记捕获**: 快速创建各类笔记
2. **标签管理**: 自动化标签系统
3. **链接建立**: 智能推荐相关笔记
4. **定期回顾**: 生成回顾清单

### 示例工作流

```
1. 阅读文章 → 创建笔记
2. 提取关键概念 → 创建卡片笔记
3. 建立链接 → 连接相关概念
4. 定期回顾 → 巩固知识
```

---

## 最佳实践

### 1. Skill 组合使用

```
obsidian（主 Skill）
  + obsidian-visual（可视化）
  + obsidian-pkm（工作流）
  ↓
完整的 Obsidian 生态
```

### 2. 文件命名规范

```
Obsidian 推荐的文件命名：
- 使用有意义的标题
- 避免特殊字符
- 使用日期前缀（可选）：YYYY-MM-DD-标题
```

### 3. 标签系统

```markdown
建议的标签层级：
#project/active
#project/archived
#note/fleeting
#note/permanent
```

### 4. 双向链接

```markdown
充分利用双向链接：
[[概念A]] 和 [[概念B]] 之间有关联

可以使用别名：
[[概念A|更友好的名称]]
```

---

## 进阶配置

### 自定义模板

创建自定义笔记模板：

```bash
# 在 Obsidian vault 中创建模板目录
mkdir -p ~/ObsidianVault/templates/

# 创建模板文件
cat > ~/ObsidianVault/templates/project.md <<'EOF'
# {{title}}

#project #new

## 概述

## 目标
- [ ]

## 任务
- [ ]

## 资源
[[]]

## 笔记
EOF
```

在 Claude Code 中使用：
```
"使用 project 模板创建新项目笔记"
```

---

## 常见问题

### Obsidian 格式不正确

**问题**: 生成的 Markdown 不符合 Obsidian 规范

**解决方法**:
1. 确保已安装主 Skill
2. 明确指定使用 "Obsidian 格式"
3. 检查双向链接语法：`[[笔记名]]`

### Canvas 无法显示

**问题**: 生成的 Canvas 文件在 Obsidian 中无法正常显示

**解决方法**:
1. 确保安装了 `obsidian-visual` Skill
2. 检查 JSON 格式是否正确
3. 使用 Obsidian 最新版本

### DataView 查询失败

**问题**: DataView 查询语法错误

**解决方法**:
1. 确保 Obsidian 中已安装 DataView 插件
2. 参考 [DataView 文档](https://blacksmithgu.github.io/obsidian-dataview/)
3. 逐步调试查询语句

---

## 参考资料

### 官方资源

- [Obsidian 官网](https://obsidian.md/)
- [Obsidian 文档](https://help.obsidian.md/)
- [Obsidian API 文档](https://docs.obsidian.md/)
- [Obsidian 论坛](https://forum.obsidian.md/)

### Skill 相关

- [主 Skill 仓库](https://github.com/kepano/obsidian-skills)
- [Visual Skills 仓库](https://github.com/axtonliu/axton-obsidian-visual-skills)
- [Plugin Skill 仓库](https://github.com/gapmiss/obsidian-plugin-skill)
- [PKM 套件仓库](https://github.com/ballred/obsidian-claude-pkm)

### 教程文章

- [Obsidian 入门指南](https://obsidian.rocks/getting-started-with-obsidian/)
- [Building a Second Brain with Obsidian](https://www.buildingasecondbrain.com/)
- [Obsidian PKM 最佳实践](https://medium.com/obsidian-observer)

---

**最后更新**: 2026-01-24
**难度**: ⭐⭐ 中等
**推荐指数**: ⭐⭐⭐⭐⭐

[返回 Top 10 列表](README.md) | [返回主页](../README.md)
