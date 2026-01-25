# Skills 快速入门指南

5 分钟上手 Claude Skills，从零到第一个 Skill。

---

## 🎯 学习目标

完成本指南后，你将能够：
- ✅ 理解 Skills 是什么
- ✅ 在 Claude.ai 使用第一个 Skill
- ✅ 在 Claude Code 安装和使用 Skills
- ✅ 知道如何寻找更多 Skills

---

## 📚 什么是 Skills

Skills 是 Claude 的**能力扩展包**，类似浏览器的插件或手机的 App。

### 一句话理解

> Skills = 给 Claude 安装"专业技能包"，让它能做更多事情

### 举例说明

| 没有 Skills | 使用 NotebookLM Skill |
|------------|----------------------|
| "我需要整理这些笔记" | "帮我把这些笔记上传到 NotebookLM" |
| Claude: 我可以帮你总结... | Claude: ✅ 已上传 5 个文档到 NotebookLM |

---

## 🚀 第一个 Skill（Claude.ai 网页版）

### 步骤 1：访问 Claude.ai

1. 打开 [claude.ai](https://claude.ai/)
2. 登录你的账号
3. 创建新对话

### 步骤 2：添加 Skill

1. 点击输入框上方的 **"+ Skills"** 按钮
2. 在 Skills 列表中搜索 `"NotebookLM"`
3. 点击 **"Add"** 添加到当前对话

### 步骤 3：使用 Skill

```
发送消息：
"帮我创建一个 NotebookLM 笔记本，主题是 Python 学习"

Claude 会：
1. 调用 NotebookLM Skill
2. 创建笔记本
3. 返回笔记本链接
```

### 效果

✅ 你的第一个 Skill 已经在工作了！

---

## 💻 第一个 Skill（Claude Code CLI）

### 前提条件

- ✅ 已安装 Claude Code CLI
- ✅ 已登录账号（`claude auth login`）

### 步骤 1：创建 Skills 目录

```bash
mkdir -p ~/.config/claude-code/skills
cd ~/.config/claude-code/skills
```

### 步骤 2：安装第一个 Skill

**推荐：NotebookLM**（知识管理）

```bash
git clone https://github.com/PleasePrompto/notebooklm-skill.git notebooklm
```

**验证安装**：
```bash
head ~/.config/claude-code/skills/notebooklm/SKILL.md
```

应该看到类似输出：
```yaml
---
description: >
  上传文档到 NotebookLM，自动进行知识问答和摘要。
---

# NotebookLM Skill
...
```

### 步骤 3：使用 Skill

启动 Claude Code：
```bash
claude
```

发送消息：
```
帮我上传这个 PDF 到 NotebookLM
```

Claude Code 会自动调用 notebooklm Skill 完成任务。

---

## 🌟 安装更多 Skills

### 方法 1：一键安装 Top 10（推荐）

安装我们精选的 10 个最实用 Skills：

```bash
wget https://raw.githubusercontent.com/weihoop/claude-code-guide/main/skills/scripts/install_top10.sh
bash install_top10.sh
```

包含的 Skills：
- NotebookLM - 知识管理
- Obsidian - 笔记系统
- Planning with Files - 项目规划
- Skill Creator - 创建自定义 Skills
- Frontend Design - 前端设计
- Superpowers - 开发工具集
- Rube MCP - 500+ 应用集成
- Baoyu Skills - 自媒体工具
- Media Skills - 社交媒体管理
- Skill Lookup - Skills 搜索

### 方法 2：使用 npx（推荐）

```bash
# 快速安装官方 Skills
npx skills add anthropics/skills

# 安装特定 Skill
npx skills add obra/superpowers
```

### 方法 3：手动安装

```bash
cd ~/.config/claude-code/skills/
git clone <skill-repo-url> <skill-name>
```

---

## 🔍 寻找更多 Skills

### 在线平台

| 平台 | 特点 | 链接 |
|------|------|------|
| **SkillsMP** | 25000+ Skills 搜索 | [skillsmp.com](https://skillsmp.com/) |
| **GitHub** | 源码和详细说明 | [搜索 "claude skills"](https://github.com/search?q=claude+skills) |
| **本指南** | 中文精选分类 | [查看分类](community/) |

### 按场景选择

| 场景 | 推荐 Skills | 详细指南 |
|------|-----------|---------|
| 📝 笔记和知识管理 | NotebookLM, Obsidian | [查看](top-10/01-notebooklm.md) |
| 💻 软件开发 | Superpowers, Skill Creator | [查看](top-10/06-superpowers.md) |
| 🎨 前端设计 | Frontend Design | [查看](top-10/05-frontend-design.md) |
| 📊 数据分析 | CSV Analyzer, D3.js Skill | [查看](community/data-analysis.md) |
| 📱 自媒体创作 | Baoyu Skills, Media Skills | [查看](top-10/08-baoyu-skills.md) |

---

## 🛠️ Skills 使用技巧

### 1. 查看已安装的 Skills

```bash
ls -la ~/.config/claude-code/skills/
```

### 2. 查看 Skill 详细信息

```bash
cat ~/.config/claude-code/skills/<skill-name>/SKILL.md
```

### 3. 更新 Skill

```bash
cd ~/.config/claude-code/skills/<skill-name>
git pull
```

### 4. 删除 Skill

```bash
rm -rf ~/.config/claude-code/skills/<skill-name>
```

---

## ⚠️ 常见问题

### Q: Skill 没有生效？

**A**: 检查以下几点：
```bash
# 1. 验证 SKILL.md 存在
ls ~/.config/claude-code/skills/*/SKILL.md

# 2. 检查 SKILL.md 格式
head ~/.config/claude-code/skills/<skill-name>/SKILL.md

# 3. 重启 Claude Code
exit
claude
```

### Q: 如何卸载 Skill？

**A**: 直接删除目录即可：
```bash
rm -rf ~/.config/claude-code/skills/<skill-name>
```

### Q: Skill 和 MCP 有什么区别？

**A**:
- **Skills**: 能力扩展，给 Claude 添加新功能
- **MCP**: 数据连接，让 Claude 访问外部数据源

详细对比：[Skills vs MCP vs Commands](guides/skills-vs-mcp-vs-commands.md)

### Q: 可以同时使用多个 Skills 吗？

**A**: 可以！Claude 会自动选择合适的 Skill 组合使用。

---

## 📖 下一步学习

### 初学者路径

1. ✅ **你在这里** - 快速入门
2. 📦 [Top 10 推荐](top-10/) - 安装最实用的 Skills
3. 🔍 [社区分类](community/) - 探索更多 Skills
4. 📚 [最佳实践](guides/best-practices.md) - 高效使用 Skills

### 进阶路径

1. 🛠️ [创建自定义 Skills](guides/creating-custom-skills.md) - 制作自己的 Skill
2. 💻 [编程使用 Skills](guides/programming-usage.md) - Python/Node.js 集成
3. ⚡ [性能优化](guides/best-practices.md#性能优化) - 让 Skills 运行更快
4. 🔧 [故障排除](guides/troubleshooting.md) - 解决常见问题

---

## 📚 延伸阅读

| 资源 | 说明 | 链接 |
|------|------|------|
| 官方文档 | Anthropic 官方 Skills 文档 | [查看](resources/official-docs.md) |
| 中文教程 | 知乎、B站、CSDN 教程 | [查看](resources/chinese-tutorials.md) |
| GitHub 仓库 | 精选 Skills 仓库列表 | [查看](resources/github-repos.md) |
| 市场平台 | Skills 发现和搜索平台 | [查看](resources/marketplace.md) |

---

## 🎉 恭喜

你已经掌握了 Skills 的基础使用！

**接下来试试**：
- 🌟 安装 [Top 10 推荐 Skills](top-10/)
- 🔍 在 [SkillsMP](https://skillsmp.com/) 搜索你需要的 Skill
- 🛠️ 尝试[创建自己的 Skill](guides/creating-custom-skills.md)

---

**返回**: [Skills 主页](README.md)

**最后更新**: 2026-01-25
