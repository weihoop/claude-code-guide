# Skills 最佳实践指南

设计高质量 Skills 的原则、模式和技巧集合。

## 📚 目录

- [设计原则](#设计原则)
- [性能优化](#性能优化)
- [Token 使用优化](#token-使用优化)
- [调试技巧](#调试技巧)
- [团队协作](#团队协作)
- [版本管理](#版本管理)
- [安全考虑](#安全考虑)

---

## 🎯 设计原则

### 1. 单一职责原则（SRP）

**原则**: 每个 Skill 只做一件事，做好一件事。

```
❌ 不好的设计：
name: data-tool
description: 处理 CSV、JSON、XML、数据库查询、生成报告...

✅ 好的设计：
name: csv-analyzer
description: 分析 CSV 文件并生成统计报告

name: json-validator
description: 验证 JSON 格式并修复常见错误

name: sql-query-builder
description: 辅助构建安全的 SQL 查询
```

**好处**:
- 更容易维护
- 更清晰的触发条件
- 更好的复用性

### 2. 清晰的触发条件

**原则**: Description 要明确说明何时使用这个 Skill。

```yaml
❌ 不好：
description: 数据分析工具

✅ 好：
description: 分析 CSV 数据并生成可视化报告，适用于销售数据、用户行为等场景
```

**技巧**:
- 包含具体的使用场景
- 提及支持的数据类型
- 说明输出格式

### 3. 渐进式设计

**原则**: 核心信息在 SKILL.md，详细内容在 references/。

```
SKILL.md (简洁，<5k words)
├── name + description (必需)
├── 核心流程说明
└── 基础示例

references/ (详细，无限制)
├── api-reference.md (API 文档)
├── advanced-usage.md (高级用法)
└── troubleshooting.md (问题排查)
```

### 4. 示例驱动

**原则**: 通过丰富的示例帮助 Claude 理解预期行为。

```markdown
## 示例

### 示例 1: 基础用法（必需）
[最常见的使用场景]

### 示例 2: 边界情况
[处理特殊输入]

### 示例 3: 错误处理
[如何处理和报告错误]

### 示例 4: 高级功能
[展示进阶用法]
```

---

## ⚡ 性能优化

### 1. 控制 SKILL.md 大小

**目标**: < 5k words（约 7.5k tokens）

```bash
# 检查文件大小
wc -w SKILL.md

# 如果超过 5k words
# 1. 提取详细文档到 references/
# 2. 简化示例
# 3. 移除冗余内容
```

**优化示例**:

**优化前** (8k words):
```markdown
## 详细说明

[500 行的详细 API 文档]
[100 个示例]
[完整的错误代码列表]
```

**优化后** (2k words):
```markdown
## 核心说明

[简要流程说明]
[3-5 个代表性示例]

详细文档：
- [API 参考](references/api-reference.md)
- [完整示例](references/examples.md)
- [错误代码](references/error-codes.md)
```

### 2. 延迟加载策略

```markdown
## 基础功能

[核心功能说明]

## 高级功能

需要高级功能？请查看 [高级用法指南](references/advanced.md)

## 故障排除

遇到问题？参考 [故障排除指南](references/troubleshooting.md)
```

**效果**: Claude 只在需要时才加载详细内容。

### 3. 脚本优化

```python
# ❌ 不好：在 SKILL.md 中内嵌大量代码
# SKILL.md 包含 500 行 Python 代码

# ✅ 好：脚本独立存放
# SKILL.md
## 数据处理

使用 scripts/process_data.py 处理数据。

参数说明：
- input_file: 输入文件路径
- output_format: 输出格式（csv/json/xlsx）

# scripts/process_data.py
[完整的处理逻辑]
```

---

## 💾 Token 使用优化

### 1. Description 优化

```yaml
# 目标：< 100 words

❌ 冗长（150 words）：
description: |
  这是一个非常强大和全面的数据分析工具，它可以帮助你...
  [大量冗余描述]

✅ 精炼（50 words）：
description: 分析 CSV 数据并生成可视化报告，支持销售、用户行为、财务等场景，自动识别数据类型，提供趋势分析和优化建议。
```

### 2. 避免重复内容

```markdown
❌ 不好：
## 使用场景
- 场景 1：分析销售数据
- 场景 2：分析用户数据
- 场景 3：分析财务数据

## 示例
### 示例 1：分析销售数据
### 示例 2：分析用户数据
### 示例 3：分析财务数据

✅ 好：
## 使用场景
- 业务数据分析（销售、用户、财务等）
- 数据质量检查
- 趋势预测

## 示例
### 通用分析流程
[一个涵盖核心功能的示例]

### 特定场景
更多示例见 [examples/](references/examples.md)
```

### 3. 精简指令

```markdown
❌ 冗长：
## 步骤 1: 数据接收
首先，你需要接收用户提供的数据文件。这个文件可能是 CSV 格式...
[200 字描述]

✅ 精炼：
## 步骤 1: 数据接收
- 接收 CSV/Excel 文件
- 验证格式（必需列：日期、金额）
- 识别编码（UTF-8/GBK）
```

---

## 🐛 调试技巧

### 1. 验证 Skill 加载

```bash
# 方法 1：检查文件格式
head -20 ~/.claude/skills/my-skill/SKILL.md

# 应该看到 YAML frontmatter：
# ---
# name: my-skill
# description: ...
# ---

# 方法 2：在 Claude Code 中测试
claude
> 使用 my-skill 处理数据
```

### 2. 调试触发条件

```markdown
## 测试触发

创建测试提示词：

测试 1（应该触发）:
"分析这个 CSV 文件的销售数据"

测试 2（不应该触发）:
"帮我写一个 Python 脚本"

测试 3（边界情况）:
"分析 Excel 文件"
```

### 3. 日志和反馈

```markdown
## 指令

### 步骤 1: 初始化
- 确认收到数据文件
- 输出：`✅ 已接收文件：{filename}`

### 步骤 2: 分析
- 执行数据分析
- 输出进度：`📊 分析中...`

### 步骤 3: 生成报告
- 创建报告
- 输出：`✅ 报告已生成`
```

**好处**: 用户和开发者都能看到执行进度。

### 4. 错误诊断

```markdown
## 常见问题诊断

### Skill 未加载
检查：
1. YAML frontmatter 格式是否正确
2. 文件名是否为 SKILL.md（全大写）
3. 文件是否在 ~/.claude/skills/ 目录

### Skill 未触发
检查：
1. Description 是否够具体
2. 测试提示词是否匹配使用场景
3. 是否有其他 Skill 冲突

### 输出不符合预期
检查：
1. 示例是否清晰
2. 指令是否详细
3. 是否有歧义描述
```

---

## 👥 团队协作

### 1. Skill 命名规范

```
团队规范：
- 使用小写字母和连字符
- 包含功能描述：<domain>-<action>
- 避免通用名称

示例：
✅ data-csv-analyzer
✅ code-security-reviewer
✅ api-doc-generator

❌ tool
❌ helper
❌ utils
```

### 2. 文档规范

```markdown
# 每个 Skill 必需的文件：

my-skill/
├── SKILL.md               # Skill 定义（必需）
├── README.md              # 使用说明（推荐）
├── CHANGELOG.md           # 版本历史（推荐）
└── references/
    └── team-guidelines.md # 团队使用指南（可选）
```

### 3. 代码审查清单

```markdown
## Skill Review Checklist

### 必需检查
- [ ] YAML frontmatter 格式正确
- [ ] Description < 100 words
- [ ] 包含至少 3 个示例
- [ ] SKILL.md < 5k words
- [ ] 测试通过（Claude Code + API）

### 推荐检查
- [ ] 有 README.md
- [ ] 有版本号
- [ ] 错误处理完善
- [ ] 文档链接有效

### 团队规范
- [ ] 命名符合规范
- [ ] 遵循设计原则
- [ ] Token 使用合理
```

---

## 📦 版本管理

### 1. 语义化版本

```yaml
---
name: my-skill
description: ...
version: 1.2.3
---

# 版本号规则：
# 1.2.3
# │ │ └─ 补丁版本（Bug 修复）
# │ └─── 次版本（新功能，向后兼容）
# └───── 主版本（破坏性变更）
```

### 2. CHANGELOG.md

```markdown
# Changelog

## [1.2.0] - 2026-01-24

### Added
- 支持 JSON 格式输出
- 新增批量处理模式

### Changed
- 优化数据分析算法
- 改进错误消息

### Fixed
- 修复空数据文件崩溃问题

### Deprecated
- `old_function()` 将在 v2.0.0 移除

## [1.1.0] - 2026-01-10
...
```

### 3. 破坏性变更

```markdown
## 处理破坏性变更

### v2.0.0 升级指南

#### 变更 1：参数重命名
```
旧版本（v1.x）:
"使用 my-skill 处理文件，格式：csv"

新版本（v2.x）:
"使用 my-skill 处理文件，输出格式：csv"
```

#### 变更 2：输出格式
[详细说明]

#### 迁移步骤
1. 备份现有配置
2. 更新提示词
3. 测试验证
```

---

## 🔒 安全考虑

### 1. 敏感信息保护

```markdown
❌ 不要在 Skill 中硬编码：
- API 密钥
- 数据库密码
- 私人信息

✅ 使用环境变量：
## 配置

需要设置以下环境变量：
- `API_KEY`: 你的 API 密钥
- `DB_PASSWORD`: 数据库密码

参考 [安全配置指南](references/security.md)
```

### 2. 输入验证

```markdown
## 数据验证

### 步骤 1: 验证输入
检查：
- 文件格式是否正确
- 文件大小是否在限制内（< 100MB）
- 数据格式是否符合预期

### 步骤 2: 清理数据
- 移除特殊字符
- 转义 SQL 特殊字符
- 验证数据范围
```

### 3. 权限控制

```markdown
## 权限说明

此 Skill 需要以下权限：
- ✅ 读取用户提供的文件
- ✅ 创建临时文件
- ❌ 不会访问系统文件
- ❌ 不会连接外部网络
```

---

## 📊 质量指标

### Skill 质量评分

```
质量评分表（满分 100）：

设计（30 分）
- [ ] 单一职责（10 分）
- [ ] 清晰的触发条件（10 分）
- [ ] 良好的示例（10 分）

性能（25 分）
- [ ] SKILL.md < 5k words（10 分）
- [ ] 渐进式加载（10 分）
- [ ] Token 使用优化（5 分）

文档（25 分）
- [ ] 完整的说明（10 分）
- [ ] 详细的示例（10 分）
- [ ] 有 README.md（5 分）

测试（20 分）
- [ ] 基础功能测试（10 分）
- [ ] 边界情况测试（5 分）
- [ ] 跨平台测试（5 分）

A 级：90-100 分
B 级：80-89 分
C 级：70-79 分
需改进：< 70 分
```

---

## 📚 延伸阅读

- [创建自定义 Skills](creating-custom-skills.md)
- [编程使用 Skills](programming-usage.md)
- [故障排除指南](troubleshooting.md)
- [Skills vs MCP vs Commands](skills-vs-mcp-vs-commands.md)

---

**返回**: [指南目录](README.md) | [主页](../README.md)

**最后更新**: 2026-01-24
