# Skill Lookup

用来发现、检索和安装 Skills，当你想找、安装 Skill 的时候就会自动激活。

## 功能简介

Skill Lookup 类工具帮助你发现和管理 Skills，提供 Skills 市场、搜索、安装和管理功能。

### 核心特点

- ✅ **Skills 发现**: 浏览和搜索可用的 Skills
- ✅ **快速安装**: 一键安装 Skills
- ✅ **版本管理**: 更新和管理已安装的 Skills
- ✅ **推荐系统**: 基于需求推荐合适的 Skills

### 适用场景

| 场景 | 说明 |
|------|------|
| **探索 Skills** | 发现新的 Skills |
| **快速安装** | 简化安装流程 |
| **Skills 管理** | 更新、卸载 Skills |
| **需求匹配** | 根据需求找到合适的 Skills |

---

## 推荐工具

### 1. Vercel Skills Marketplace

官方 Skills 安装工具，由 Vercel 提供。

#### 安装方法

```bash
# 使用 npx 快速安装 Skills
npx skills add <owner/repo>

# 示例
npx skills add anthropics/skills
npx skills add obra/superpowers
```

#### 功能

- ✅ 快速安装：一行命令搞定
- ✅ 自动配置：处理依赖和配置
- ✅ 版本管理：支持更新和回滚

---

### 2. Skill Seekers

自动将文档网站、GitHub 仓库和 PDF 文件转换为 Agent Skills。

#### 仓库信息

- **GitHub**: [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)
- **维护者**: [@yusufkaraaslan](https://github.com/yusufkaraaslan)

#### 安装方法

```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/yusufkaraaslan/Skill_Seekers skill-seekers
```

#### 功能

- ✅ **文档转换**: 将文档网站转换为 Skill
- ✅ **GitHub 仓库**: 从 README 生成 Skill
- ✅ **PDF 转换**: PDF 文件自动转换

#### 使用示例

```
用户: "将这个文档网站转换为 Skill"
[提供 URL]

Claude:
分析文档结构...
提取关键信息...
生成 SKILL.md...
✅ Skill 已创建：doc-website-skill
```

---

### 3. SkillsMP.com

在线 Skills 搜索平台，拥有 25000+ Skills。

#### 特点

- 🔍 **搜索功能**: 按关键词、分类搜索
- 📊 **Skills 统计**: 使用量、评分、更新频率
- 🏷️ **标签系统**: 按功能、场景分类
- ⭐ **社区评价**: 用户评分和评论

#### 使用方式

访问 [SkillsMP.com](https://skillsmp.com/)

---

### 4. Claude Skills 官方文档

官方 Skills 目录和文档。

- **官方 Skills**: [anthropics/skills](https://github.com/anthropics/skills)
- **Skills 指南**: [Claude Skills Overview](https://www.anthropic.com/news/skills)
- **创建指南**: [Creating Custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

---

## 使用方法

### 方式 1：通过 npx 安装（最快）

```bash
# 搜索 Skills（访问 SkillsMP.com）

# 安装 Skills
npx skills add anthropics/skills
npx skills add obra/superpowers
```

### 方式 2：使用 Skill Seekers 转换

```bash
# 安装 Skill Seekers
cd ~/.config/claude-code/skills/
git clone https://github.com/yusufkaraaslan/Skill_Seekers skill-seekers

# 使用 Skill Seekers 转换文档
用户: "使用 skill-seekers 将这个文档转换为 Skill"
```

### 方式 3：手动搜索和安装

```bash
# 1. 在 GitHub 搜索
https://github.com/search?q=claude+skills

# 2. 在 SkillsMP.com 搜索
https://skillsmp.com/

# 3. 手动克隆
cd ~/.config/claude-code/skills/
git clone <skill-repo-url> <skill-name>
```

---

## Skills 发现技巧

### 1. 按需求搜索

#### 开发相关

```
搜索关键词：
- "code review skill"
- "testing skill"
- "mcp builder skill"
```

#### 内容创作

```
搜索关键词：
- "writing skill"
- "content creation skill"
- "social media skill"
```

#### 数据处理

```
搜索关键词：
- "csv skill"
- "data analysis skill"
- "visualization skill"
```

### 2. 浏览精选列表

#### Awesome 列表

- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [awesome-agent-skills](https://github.com/libukai/awesome-agent-skills)

#### 官方推荐

- [Anthropic Skills](https://github.com/anthropics/skills)
- [Claude Code 官方](https://github.com/anthropics/claude-code)

### 3. 关注知名开发者

| 开发者 | GitHub | 代表作品 |
|--------|--------|---------|
| @obra | [obra](https://github.com/obra) | Superpowers |
| @kepano | [kepano](https://github.com/kepano) | Obsidian Skills |
| @JimLiu | [JimLiu](https://github.com/JimLiu) | 宝玉 Skills |

---

## Skills 管理

### 查看已安装的 Skills

```bash
ls -la ~/.config/claude-code/skills/
```

### 更新 Skills

```bash
cd ~/.config/claude-code/skills/<skill-name>
git pull origin main
```

### 卸载 Skills

```bash
rm -rf ~/.config/claude-code/skills/<skill-name>
```

### 检查 Skills 状态

```bash
# 检查 SKILL.md 格式
head ~/.config/claude-code/skills/<skill-name>/SKILL.md

# 验证 YAML frontmatter
grep -A 3 "^---$" ~/.config/claude-code/skills/<skill-name>/SKILL.md | head -5
```

---

## 推荐 Skills 列表

### 官方 Skills

| Skill | 用途 | 安装命令 |
|-------|------|---------|
| docx | Word 文档处理 | `npx skills add anthropics/skills` |
| pdf | PDF 处理 | 同上 |
| pptx | PPT 处理 | 同上 |
| xlsx | Excel 处理 | 同上 |

### 社区热门

| Skill | 用途 | 仓库 |
|-------|------|------|
| Superpowers | 开发工作流 | [obra/superpowers](https://github.com/obra/superpowers) |
| NotebookLM | 知识管理 | [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) |
| Frontend Design | 前端设计 | [anthropics/claude-code](https://github.com/anthropics/claude-code) |

👉 [查看完整 Top 10 列表](README.md)

---

## 最佳实践

### 1. 定期更新 Skills

```bash
# 创建更新脚本
cat > ~/.claude/scripts/update_skills.sh <<'EOF'
#!/bin/bash
cd ~/.config/claude-code/skills/
for skill in */; do
  echo "Updating $skill..."
  cd "$skill"
  git pull origin main
  cd ..
done
EOF

chmod +x ~/.claude/scripts/update_skills.sh

# 定期运行
bash ~/.claude/scripts/update_skills.sh
```

### 2. 备份 Skills 列表

```bash
# 导出已安装的 Skills 列表
ls -1 ~/.config/claude-code/skills/ > ~/.claude/skills-list.txt

# 批量安装（新环境）
while read skill; do
  # 根据 skills-list.txt 重新安装
done < ~/.claude/skills-list.txt
```

### 3. 分类管理

```bash
# 按用途组织 Skills
skills/
├── development/
│   ├── superpowers/
│   └── skill-creator/
├── content/
│   ├── baoyu-skills/
│   └── notebooklm/
└── official/
    ├── pdf/
    └── docx/
```

---

## 常见问题

### 如何找到合适的 Skill？

1. 明确需求（例如：需要处理 CSV 文件）
2. 在 SkillsMP.com 搜索关键词
3. 查看 awesome-claude-skills 推荐
4. 阅读 Skill 的 README 和评价
5. 小范围测试后再正式使用

### Skill 太多怎么办？

**建议**:
- 只安装常用的 Skills
- 定期清理不再使用的 Skills
- 使用分类管理
- 记录每个 Skill 的用途

### Skill 版本冲突

**解决方法**:
- 使用不同的目录名安装多个版本
- 明确指定使用哪个版本
- 优先使用官方维护的版本

---

## 参考资料

### 官方资源

- [Claude Skills 文档](https://code.claude.com/docs/zh-CN/skills)
- [创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

### Skills 平台

- [SkillsMP.com](https://skillsmp.com/) - 25000+ Skills
- [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)
- [Vercel Skills](https://www.npmjs.com/package/skills)

### 精选列表

- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [awesome-agent-skills](https://github.com/libukai/awesome-agent-skills)

### 教程文章

- [CNBlogs：Skills 保姆级教程](https://www.cnblogs.com/javastack/p/19176207)
- [Apifox：Skills 指南](https://apifox.com/apiskills/claude-skills/)

---

**最后更新**: 2026-01-24
**难度**: ⭐ 简单
**推荐指数**: ⭐⭐⭐

[返回 Top 10 列表](README.md) | [返回主页](../README.md)
