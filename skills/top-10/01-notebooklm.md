# NotebookLM Skill

AI 对接 NotebookLM，自动上传资料、知识问答、生成 PPT、脑图都能搞定。

## 功能简介

NotebookLM Skill 让 Claude Code 能够直接与 NotebookLM 交互，通过浏览器自动化技术实现零幻觉的知识问答系统。

### 核心特点

- ✅ **浏览器自动化**: 通过 Chrome DevTools Protocol 与 NotebookLM 交互
- ✅ **持久化认证**: 登录一次，长期使用
- ✅ **零幻觉**: 答案完全基于上传的文档，不会编造信息
- ⚠️ **本地限制**: 只能在本地 Claude Code 使用，不支持 Web UI

### 适用场景

| 场景 | 说明 |
|------|------|
| **学术研究** | 上传论文、文献，快速提取关键信息 |
| **知识管理** | 整理笔记、文档，构建个人知识库 |
| **项目调研** | 上传行业报告，快速获取洞察 |
| **学习辅导** | 上传教材、课件，回答学习问题 |

---

## 仓库信息

- **GitHub**: [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill)
- **维护者**: [@PleasePrompto](https://github.com/PleasePrompto)
- **License**: 开源
- **官方文档**: [MCP Servers - NotebookLM](https://mcpservers.org/claude-skills/pleaseprompto/notebooklm-skill)

---

## 安装方法

### 快速安装（推荐）

```bash
# 创建 skills 目录（如果不存在）
mkdir -p ~/.config/claude-code/skills/

# 进入目录
cd ~/.config/claude-code/skills/

# 克隆仓库
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm
```

### 验证安装

```bash
# 检查 SKILL.md 是否存在
head ~/.config/claude-code/skills/notebooklm/SKILL.md

# 应该看到类似以下内容：
# ---
# name: notebooklm
# description: Integration with NotebookLM for document-based Q&A
# ---
```

---

## 配置和使用

### 首次配置

1. **启动 Claude Code**:
   ```bash
   claude
   ```

2. **登录 NotebookLM**:
   - Skill 会自动打开 Chrome 浏览器
   - 在浏览器中登录你的 Google 账号
   - 登录成功后，认证信息会持久化保存

3. **上传文档**:
   - 在 NotebookLM 中创建新的笔记本
   - 上传你的文档（PDF、文本、网页等）

### 基础使用

在 Claude Code 中，直接提问关于文档的问题：

```
用户: "根据我上传的文档，总结一下主要观点"
Claude: [使用 notebooklm skill 查询并返回答案]
```

### 使用示例

#### 示例 1：学术论文分析

```
上传文档: research-paper.pdf

问题: "这篇论文的核心贡献是什么？"
回答: [基于论文内容的精确回答，不会编造]

问题: "论文中提到的实验方法有哪些？"
回答: [提取论文中的实验部分]
```

#### 示例 2：项目文档问答

```
上传文档: project-spec.md, api-docs.md

问题: "如何调用用户登录 API？"
回答: [基于 api-docs.md 的准确步骤]
```

---

## 进阶使用

### 多文档管理

NotebookLM 支持多个笔记本，每个笔记本可以包含不同的文档集合：

```
笔记本 1: 学术研究（论文、文献）
笔记本 2: 工作项目（需求文档、技术文档）
笔记本 3: 个人学习（书籍摘要、笔记）
```

在 Claude Code 中，可以指定使用哪个笔记本：

```
"使用学术研究笔记本，找出关于 XX 主题的相关信息"
```

### 集成其他工具

NotebookLM Skill 可以与其他 Skills 配合使用：

```
NotebookLM（知识检索） + Obsidian（笔记整理） + PDF Skill（文档生成）
  ↓
完整的知识管理工作流
```

### 高级配置

如果需要自定义浏览器路径或其他设置，编辑 Skill 配置：

```bash
cd ~/.config/claude-code/skills/notebooklm
# 查看和编辑配置文件（如果存在）
```

---

## 注意事项

### 使用限制

- ⚠️ **仅限本地**: 不支持在 Claude.ai 网页版使用
- ⚠️ **需要浏览器**: 依赖 Chrome/Chromium 浏览器
- ⚠️ **网络要求**: 需要稳定的网络连接访问 NotebookLM

### 隐私和安全

- ✅ **数据隐私**: 文档上传到 Google NotebookLM，不经过第三方
- ✅ **认证安全**: 使用 Google 官方认证，本地保存 token
- ⚠️ **敏感文档**: 避免上传机密文档到云端服务

### 最佳实践

1. **文档组织**: 按主题创建不同的笔记本，便于管理
2. **定期清理**: 删除不再需要的文档，节省存储空间
3. **备份重要文档**: NotebookLM 是云服务，建议保留本地备份
4. **精确提问**: 问题越具体，答案越准确

---

## 故障排除

### 浏览器无法启动

**问题**: Skill 无法打开 Chrome 浏览器

**解决方法**:
```bash
# 检查 Chrome 是否安装
which google-chrome
which chromium-browser

# 如果未安装，安装 Chrome
# macOS:
brew install --cask google-chrome

# Linux:
sudo apt install chromium-browser
```

### 认证失败

**问题**: 无法登录 Google 账号

**解决方法**:
1. 清除浏览器缓存和 Cookie
2. 手动在浏览器中登录 NotebookLM
3. 重启 Claude Code

### Skill 不响应

**问题**: Claude 没有激活 NotebookLM Skill

**解决方法**:
1. 确认 SKILL.md 格式正确
2. 重启 Claude Code
3. 手动激活 Skill：`/skill notebooklm`

---

## 参考资料

### 官方资源

- [NotebookLM 官网](https://notebooklm.google.com/)
- [Skill 仓库](https://github.com/PleasePrompto/notebooklm-skill)
- [MCP Servers 页面](https://mcpservers.org/claude-skills/pleaseprompto/notebooklm-skill)

### 教程文章

- [如何使用 NotebookLM 进行知识管理](https://blog.google/technology/ai/notebooklm-guide/)
- [Claude Skills + NotebookLM 实战](https://community.anthropic.com/)

### 相关 Skills

- [Obsidian Skills](02-obsidian.md) - 本地知识管理
- [Planning with Files](03-planning-with-files.md) - 项目规划和笔记

---

**最后更新**: 2026-01-24
**难度**: ⭐ 简单
**推荐指数**: ⭐⭐⭐⭐

[返回 Top 10 列表](README.md) | [返回主页](../README.md)
