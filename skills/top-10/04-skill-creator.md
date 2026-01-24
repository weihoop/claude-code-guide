# Skill Creator

自己做 Skill 时的首选，可以直接创建符合最佳实践的 Skill，也可以用它来优化现有的 Skill。

## 功能简介

Skill Creator 提供创建高质量 Claude Skills 的指导，包含最佳实践和模板，适用于扩展 Claude 的专业能力。

### 核心特点

- ✅ **最佳实践**: 遵循 Anthropic 官方推荐的 Skill 设计模式
- ✅ **模板驱动**: 提供多种场景的 Skill 模板
- ✅ **质量保证**: 自动检查 Skill 格式和内容
- ✅ **优化建议**: 可以改进现有 Skill

### 适用场景

| 场景 | 说明 |
|------|------|
| **创建新 Skill** | 从零开始创建自定义 Skill |
| **优化现有 Skill** | 改进已有 Skill 的质量 |
| **学习 Skill 开发** | 了解 Skill 最佳实践 |
| **团队规范** | 统一团队的 Skill 开发标准 |

---

## 仓库信息

- **来源**: awesome-claude-skills 仓库
- **路径**: `./skill-creator/`
- **维护者**: ComposioHQ
- **License**: Apache 2.0

---

## 安装方法

### 方式 1：从本仓库安装（推荐）

如果已克隆 awesome-claude-skills 仓库：

```bash
cd ~/.config/claude-code/skills/
cp -r /path/to/awesome-claude-skills/skill-creator ./
```

### 方式 2：直接从 GitHub 安装

```bash
mkdir -p ~/.config/claude-code/skills/
cd ~/.config/claude-code/skills/

# 克隆临时仓库
git clone https://github.com/ComposioHQ/awesome-claude-skills temp

# 复制 skill-creator
cp -r temp/skill-creator ./

# 删除临时仓库
rm -rf temp
```

### 验证安装

```bash
head ~/.config/claude-code/skills/skill-creator/SKILL.md
ls -la ~/.config/claude-code/skills/skill-creator/
```

---

## 配置和使用

### 创建新 Skill

```
用户: "使用 skill-creator 帮我创建一个数据分析的 Skill"

Claude:
好的，我会帮你创建一个数据分析 Skill。

1. 首先，让我了解一些信息：
   - Skill 的主要功能是什么？
   - 预期的使用场景？
   - 需要哪些外部工具或库？

2. 基于你的回答，我会生成：
   - SKILL.md 文件
   - 必要的 scripts/
   - 参考文档 references/
   - 使用示例
```

### 优化现有 Skill

```
用户: "帮我优化这个 Skill"
[提供现有 SKILL.md 内容]

Claude:
我会从以下几个方面优化你的 Skill：

1. **结构优化**:
   - 补充缺失的 YAML frontmatter
   - 改进章节组织

2. **内容优化**:
   - 让描述更清晰
   - 增加使用示例
   - 完善错误处理说明

3. **性能优化**:
   - 减少 Token 使用
   - 优化触发条件
```

---

## Skill 创建最佳实践

### 1. YAML Frontmatter

```yaml
---
name: my-skill
description: 一句话描述这个 skill 的功能和使用场景（<100 words）
---
```

**要点**:
- `name`: 使用小写字母和连字符
- `description`: 清晰描述触发条件和主要功能

### 2. Skill 文档结构

```markdown
# Skill 名称

简短介绍（1-2 句话）

## 使用场景

明确列出 3-5 个使用场景

## 指令

详细的执行步骤和注意事项

## 示例

提供输入和输出示例

## 参考资料

相关文档和资源
```

### 3. 渐进式加载

```
第 1 层：YAML frontmatter（始终加载）
  ↓
第 2 层：SKILL.md 正文（触发时加载）
  ↓
第 3 层：references/ 和 scripts/（按需加载）
```

### 4. 触发条件设计

```markdown
✅ 好的触发条件：
"当用户需要分析 CSV 数据时使用"

❌ 不好的触发条件：
"数据分析工具"（太泛泛）
```

---

## 创建示例

### 示例 1：简单 Skill

创建一个代码审查 Skill：

```markdown
---
name: code-review
description: 对代码进行安全审查，检查常见漏洞（SQL注入、XSS、敏感信息泄露）
---

# Code Review Skill

对代码进行全面的安全审查和最佳实践检查。

## 使用场景

- 提交代码前的安全检查
- Pull Request 代码审查
- 遗留代码安全审计

## 指令

1. 检查以下安全问题：
   - SQL 注入风险
   - XSS 漏洞
   - 敏感信息硬编码
   - 不安全的依赖

2. 检查代码质量：
   - 命名规范
   - 注释完整性
   - 错误处理

3. 生成审查报告

## 示例

**输入**:
```javascript
const query = `SELECT * FROM users WHERE id = ${userId}`;
```

**输出**:
⚠️ 发现 SQL 注入风险
建议使用参数化查询：
```javascript
const query = 'SELECT * FROM users WHERE id = ?';
db.query(query, [userId]);
```
```

### 示例 2：带脚本的 Skill

创建一个数据处理 Skill：

```
skill-name/
├── SKILL.md
├── scripts/
│   └── process_data.py
└── references/
    └── data-formats.md
```

---

## 常见问题

### Skill 没有被触发

**原因**:
- Description 不够具体
- 触发条件不明确

**解决方法**:
1. 优化 description，明确触发场景
2. 在对话中显式提到 Skill 名称

### Skill 加载慢

**原因**:
- SKILL.md 太长
- 没有使用渐进式加载

**解决方法**:
1. 将详细文档放到 references/
2. SKILL.md 保持简洁（<5k words）
3. 使用外部脚本处理复杂逻辑

### 多个 Skill 冲突

**原因**:
- Description 重叠
- 触发条件相似

**解决方法**:
1. 明确每个 Skill 的边界
2. 使用更具体的触发条件
3. 考虑合并相似的 Skills

---

## 高级技巧

### 1. 动态内容加载

```markdown
## 数据格式参考

详见 [数据格式文档](references/data-formats.md)

<!-- Claude 会按需加载这个文件 -->
```

### 2. 条件执行

```markdown
## 指令

1. 检查文件类型：
   - 如果是 .csv: 使用 pandas 处理
   - 如果是 .json: 使用 jq 处理
   - 如果是 .xml: 使用 xmllint 处理
```

### 3. 错误处理

```markdown
## 错误处理

- 文件不存在: 提示用户检查路径
- 格式错误: 提供示例格式
- 权限不足: 提示使用 sudo（如果安全）
```

---

## 参考资料

### 官方文档

- [创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Skills 最佳实践](https://www.anthropic.com/news/skills)

### 社区资源

- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [Skill Creator 仓库](https://github.com/ComposioHQ/awesome-claude-skills/tree/main/skill-creator)

### 相关指南

- [完整创建指南](../guides/creating-custom-skills.md)
- [Skills vs MCP](../guides/skills-vs-mcp-vs-commands.md)

---

**最后更新**: 2026-01-24
**难度**: ⭐⭐⭐ 进阶
**推荐指数**: ⭐⭐⭐⭐⭐

[返回 Top 10 列表](README.md) | [返回主页](../README.md)
