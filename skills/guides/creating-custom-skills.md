# 创建自定义 Skills 完整指南

从零开始创建高质量的 Claude Skills，掌握最佳实践和设计模式。

## 📚 目录

- [快速开始](#快速开始)
- [目录结构](#目录结构)
- [SKILL.md 详解](#skillmd-详解)
- [渐进式加载设计](#渐进式加载设计)
- [完整示例](#完整示例)
- [最佳实践](#最佳实践)
- [测试和发布](#测试和发布)
- [常见错误](#常见错误)

---

## 🚀 快速开始

### 5 分钟创建第一个 Skill

```bash
# 1. 创建目录
mkdir -p ~/.claude/skills/my-first-skill
cd ~/.claude/skills/my-first-skill

# 2. 创建 SKILL.md
cat > SKILL.md <<'EOF'
---
name: my-first-skill
description: 一个简单的示例 Skill，演示基本结构和功能。
---

# My First Skill

这是我的第一个 Claude Skill！

## 使用场景

- 学习 Skill 基础结构
- 理解 YAML frontmatter
- 测试 Skill 加载机制

## 指令

当用户请求使用这个 skill 时：
1. 向用户问好
2. 说明这是一个示例 Skill
3. 建议用户创建自己的 Skill

## 示例

**用户**: "使用 my-first-skill"

**输出**:
你好！这是一个示例 Skill。你可以基于这个模板创建自己的 Skill。
EOF

# 3. 测试
claude
```

恭喜！你已经创建了第一个 Skill！

---

## 📁 目录结构

### 基础结构（必需）

```
my-skill/
└── SKILL.md          # 唯一必需的文件
```

### 标准结构（推荐）

```
my-skill/
├── SKILL.md          # Skill 定义和核心指令
├── scripts/          # 可执行脚本
│   ├── process.py
│   └── utils.sh
├── references/       # 参考文档和详细资料
│   ├── api-docs.md
│   └── examples.md
└── assets/           # 模板、图片、配置
    ├── template.html
    └── config.yaml
```

### 完整结构（高级）

```
my-advanced-skill/
├── SKILL.md                    # Skill 定义
├── README.md                   # 使用说明（可选）
├── scripts/                    # 脚本目录
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── tests/
│       └── test_main.py
├── references/                 # 参考资料
│   ├── architecture.md
│   ├── api-reference.md
│   └── troubleshooting.md
├── assets/                     # 资源文件
│   ├── templates/
│   │   └── output.html
│   └── configs/
│       └── default.yaml
└── examples/                   # 使用示例
    ├── basic.md
    └── advanced.md
```

---

## 📝 SKILL.md 详解

### YAML Frontmatter

**必需字段**:

```yaml
---
name: skill-name           # 小写字母和连字符
description: 简短描述（<100 words）  # 触发条件和主要功能
---
```

**可选字段**:

```yaml
---
name: advanced-skill
description: 高级 Skill 示例，展示所有可选字段。
version: 1.0.0            # 版本号
author: Your Name         # 作者
tags: [data, analysis]    # 标签（用于分类）
requires: [python, pandas] # 依赖项
---
```

### 关键要素

#### 1. 清晰的标题和介绍

```markdown
# Skill 名称

[1-2 句话概括 Skill 的核心功能和价值]

## 功能特点

- 特点 1：具体说明
- 特点 2：具体说明
- 特点 3：具体说明
```

#### 2. 使用场景（重要！）

```markdown
## 使用场景

明确列出 3-5 个具体场景，帮助 Claude 理解何时应该激活这个 Skill。

- **场景 1**: CSV 数据分析和可视化
- **场景 2**: 批量数据处理和转换
- **场景 3**: 数据质量检查和报告生成
```

#### 3. 详细指令

```markdown
## 指令

### 步骤 1: 数据准备
- 接收用户提供的 CSV 文件
- 验证文件格式和数据完整性
- 识别数据类型（数值、文本、日期等）

### 步骤 2: 数据分析
- 计算基础统计信息（均值、中位数、标准差）
- 识别缺失值和异常值
- 分析数据分布

### 步骤 3: 生成报告
- 创建可视化图表
- 总结关键发现
- 提出数据质量改进建议

### 错误处理
- 文件格式错误：提示用户检查文件格式
- 数据缺失：报告缺失比例并继续分析
- 内存不足：建议采样或分批处理
```

#### 4. 示例（必需）

```markdown
## 示例

### 示例 1: 基础使用

**用户输入**:
```
分析这个销售数据 CSV 文件
[上传 sales.csv]
```

**预期输出**:
```
📊 数据摘要
- 记录数：1,234 行
- 时间范围：2024-01 到 2024-12
- 字段：日期、产品、销售额、数量

📈 统计分析
- 总销售额：$1,234,567
- 平均订单：$1,000
- 最畅销产品：产品 A（45% 占比）

[生成可视化图表]
```

### 示例 2: 高级功能

**用户输入**:
```
对比两个季度的销售数据，找出趋势变化
```

**预期输出**:
```
📊 季度对比分析
Q1 vs Q2:
- 销售额增长：+15%
- 订单量增长：+20%
- 客单价下降：-4%

🔍 趋势发现
- 新客户增加显著
- 复购率略有下降
- 促销活动效果明显

💡 建议
1. 加强客户留存策略
2. 优化产品定价
3. 持续促销投入
```
```

---

## 🔄 渐进式加载设计

### 三层加载机制

```
第 1 层：YAML Frontmatter（始终加载）
  ↓ 约 100 words，始终在 Claude 的上下文中
  ↓ 包含：name + description

第 2 层：SKILL.md 正文（触发时加载）
  ↓ < 5k words，仅在 Skill 被触发时加载
  ↓ 包含：核心指令、基础示例

第 3 层：References 和 Scripts（按需加载）
  ↓ 无限制，仅在需要时引用
  ↓ 包含：详细文档、复杂脚本
```

### 设计示例

**SKILL.md**（第 2 层，简洁版）:
```markdown
---
name: data-analyzer
description: 分析 CSV 数据并生成可视化报告，适用于销售、用户行为等数据分析场景。
---

# Data Analyzer

快速分析 CSV 数据并生成洞察报告。

## 核心功能

1. 自动数据分析
2. 生成可视化图表
3. 提供优化建议

详细文档请参考：[完整 API 文档](references/api-docs.md)
```

**references/api-docs.md**（第 3 层，详细版）:
```markdown
# Data Analyzer 完整 API 文档

## 支持的数据格式

- CSV（逗号分隔）
- TSV（制表符分隔）
- 自定义分隔符

## 高级参数

### 数据清洗选项
- `remove_duplicates`: 删除重复行
- `fill_missing`: 填充缺失值策略
- `outlier_detection`: 异常值检测阈值

### 可视化选项
- `chart_types`: 图表类型列表
- `color_scheme`: 颜色方案
- `export_format`: 导出格式（PNG/SVG/PDF）

## 完整示例

[50+ 行的详细示例代码]
```

---

## 💡 完整示例

### 示例：代码审查 Skill

```markdown
---
name: code-review
description: 对代码进行全面的安全审查和质量检查，检测 SQL 注入、XSS、敏感信息等问题。
version: 1.0.0
author: Your Name
tags: [security, code-quality]
---

# Code Review Skill

专业的代码安全审查和质量检查工具。

## 功能特点

- ✅ 安全漏洞检测（SQL 注入、XSS、CSRF）
- ✅ 代码质量分析（命名规范、复杂度）
- ✅ 最佳实践检查
- ✅ 自动生成审查报告

## 使用场景

- **提交前检查**: 开发者提交代码前的自检
- **Pull Request 审查**: 代码审查员的辅助工具
- **安全审计**: 定期安全扫描和审计
- **遗留代码**: 老代码的安全评估

## 指令

### 步骤 1: 代码接收和解析
1. 接收用户提供的代码（文件或片段）
2. 识别编程语言（JavaScript、Python、Java 等）
3. 解析代码结构（函数、类、变量）

### 步骤 2: 安全扫描
检查以下安全问题：

**高危**:
- SQL 注入风险
- XSS 漏洞
- 命令注入
- 路径遍历

**中危**:
- 硬编码密钥
- 不安全的随机数
- 弱加密算法

**低危**:
- 敏感信息日志
- 注释中的凭证

### 步骤 3: 代码质量检查
- 命名规范（变量、函数、类）
- 函数复杂度（圈复杂度 < 10）
- 代码重复度
- 注释完整性
- 错误处理

### 步骤 4: 生成报告
```
📋 代码审查报告

文件：auth.js
语言：JavaScript
行数：150

🔴 高危问题（1 个）
- 第 42 行：SQL 注入风险
  const query = `SELECT * FROM users WHERE id = ${userId}`;

  建议修复：
  const query = 'SELECT * FROM users WHERE id = ?';
  db.query(query, [userId]);

🟠 中危问题（2 个）
...

🟢 建议（5 个）
...

总体评分：B+（85/100）
```

### 错误处理
- 无法识别的语言：提示支持的语言列表
- 文件过大（>10MB）：建议分批审查
- 解析失败：提供部分结果并说明原因

## 示例

### 示例 1: JavaScript 安全审查

**用户输入**:
```javascript
function login(username, password) {
  const query = `SELECT * FROM users WHERE username='${username}' AND password='${password}'`;
  return db.execute(query);
}
```

**输出**:
```
🔴 发现严重安全问题！

问题：SQL 注入漏洞
位置：第 2 行
风险等级：高危

详细说明：
直接拼接用户输入到 SQL 查询中，攻击者可以通过构造特殊输入来执行任意 SQL 命令。

示例攻击：
username: admin' OR '1'='1
password: anything

修复建议：
```javascript
function login(username, password) {
  const query = 'SELECT * FROM users WHERE username=? AND password=?';
  return db.execute(query, [username, password]);
}
```

参考资料：
- [OWASP SQL Injection](references/owasp-sql-injection.md)
```

### 示例 2: Python 代码质量

**用户输入**:
```python
def calculate(a,b,c,d,e):
    if a>0:
        if b>0:
            if c>0:
                return a+b+c+d+e
    return 0
```

**输出**:
```
🟡 代码质量问题

1. 命名问题（中）
   - 参数名不够描述性：a, b, c, d, e
   - 建议：使用有意义的变量名

2. 复杂度问题（低）
   - 嵌套深度：3 层
   - 建议：简化逻辑或提取函数

3. 代码风格（低）
   - 缺少空格：a,b,c,d,e
   - 建议：遵循 PEP 8 规范

改进后的代码：
```python
def calculate_total(value1, value2, value3, value4, value5):
    """计算五个值的总和，仅当前三个值为正数时。"""
    if value1 > 0 and value2 > 0 and value3 > 0:
        return sum([value1, value2, value3, value4, value5])
    return 0
```
```

## 支持的语言

- JavaScript / TypeScript
- Python
- Java
- Go
- PHP
- Ruby
- C / C++

## 参考资料

详细的漏洞说明和修复方案请参考：
- [SQL 注入防护](references/sql-injection.md)
- [XSS 防护指南](references/xss-prevention.md)
- [代码质量标准](references/code-quality.md)
```

---

## ✅ 最佳实践

### 1. Skill 设计原则

```
单一职责原则（SRP）
  ↓
每个 Skill 只做一件事，做好一件事

示例：
❌ 不好：universal-tool（什么都做）
✅ 好：csv-analyzer（专注 CSV 分析）
```

### 2. Description 编写技巧

```markdown
✅ 好的 description：
"分析 CSV 数据并生成可视化报告，适用于销售数据、用户行为等场景。"

❌ 不好的 description：
"数据分析工具"（太泛泛，不明确触发条件）
```

### 3. Token 优化

```
SKILL.md 大小建议：
- 理想：< 2k words（约 3k tokens）
- 可接受：2k-5k words（约 3k-7.5k tokens）
- 避免：> 5k words（影响性能）

优化策略：
1. 核心指令放 SKILL.md
2. 详细文档放 references/
3. 大型数据放 assets/
```

### 4. 示例质量

```markdown
高质量示例包含：
✅ 真实的用户输入
✅ 完整的预期输出
✅ 边界情况处理
✅ 错误示例（展示如何处理错误）

示例结构：
**用户**: [具体输入]
**输出**: [详细输出，包含格式]
**说明**: [可选，解释关键点]
```

### 5. 版本控制

```
使用语义化版本：
- 1.0.0: 初始稳定版本
- 1.1.0: 新增功能（向后兼容）
- 1.1.1: Bug 修复
- 2.0.0: 破坏性变更

在 SKILL.md 中记录版本：
---
name: my-skill
description: ...
version: 1.2.0
changelog: references/CHANGELOG.md
---
```

---

## 🧪 测试和发布

### 测试清单

```bash
□ 本地测试
  - Claude Code 中加载成功
  - Skill 被正确触发
  - 输出符合预期

□ 跨平台测试
  - Claude.ai 网页版
  - Claude Code CLI
  - Claude API

□ 边界测试
  - 空输入
  - 超大输入
  - 错误格式

□ 性能测试
  - 加载时间 < 2 秒
  - Token 使用合理
  - 不影响其他 Skills
```

### 发布步骤

```bash
# 1. 创建 GitHub 仓库
gh repo create my-skill --public

# 2. 添加 README.md
cat > README.md <<'EOF'
# My Skill

[Skill 描述和安装说明]

## 安装

```bash
cd ~/.claude/skills/
git clone https://github.com/username/my-skill
```

## 使用

[使用示例]
EOF

# 3. 提交代码
git add .
git commit -m "feat: initial release v1.0.0"
git tag v1.0.0
git push origin main --tags

# 4. 发布到社区
# 提交 PR 到 awesome-claude-skills
```

---

## ⚠️ 常见错误

### 错误 1: YAML 格式错误

```yaml
❌ 错误：
---
name my-skill  # 缺少冒号
description: ...
---

✅ 正确：
---
name: my-skill
description: ...
---
```

### 错误 2: Description 太长

```yaml
❌ 错误（150+ words）：
description: 这是一个非常强大的工具，它可以做很多事情...（太长）

✅ 正确（<100 words）：
description: 分析 CSV 数据并生成可视化报告，适用于销售和用户行为分析。
```

### 错误 3: 缺少示例

```markdown
❌ 错误：
## 指令
1. 步骤 1
2. 步骤 2
[没有示例]

✅ 正确：
## 指令
1. 步骤 1
2. 步骤 2

## 示例
[具体的输入输出示例]
```

### 错误 4: 文件结构混乱

```
❌ 错误：
my-skill/
├── skill.md         # 文件名错误，应该是 SKILL.md
├── test.py          # 应该在 scripts/ 目录
└── readme.txt       # 应该在根目录为 README.md

✅ 正确：
my-skill/
├── SKILL.md
├── README.md
└── scripts/
    └── test.py
```

---

## 📚 延伸阅读

- [编程使用 Skills](programming-usage.md)
- [Skills 最佳实践](best-practices.md)
- [故障排除指南](troubleshooting.md)
- [Skills vs MCP vs Commands](skills-vs-mcp-vs-commands.md)

---

**返回**: [指南目录](README.md) | [主页](../README.md)

**最后更新**: 2026-01-24
