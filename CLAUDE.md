# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 **Claude Code 中文使用手册** 文档库项目，为中文用户提供完整的 Claude Code 学习资料和参考文档。

### 项目特点
- **纯文档项目**：主要由 Markdown 文档组成，无需构建或编译
- **中文内容**：所有文档均为中文编写，面向中文开发者
- **教程导向**：从入门到进阶，包含大量实践案例和模板
- **社区驱动**：欢迎贡献和反馈

### 技术栈
- Markdown 文档
- Git 版本控制
- 无构建工具（纯文档）

## 项目结构

```
claude-code-guide/
├── README.md                    # 项目主页和索引
├── basic-guide.md              # 基础使用手册
├── advanced-guide.md           # 进阶使用手册
├── best-practices.md           # 最佳实践
├── security-guide.md           # 安全使用手册
├── docs/                       # 详细文档目录
│   ├── getting-started/        # 入门指南
│   │   ├── README.md          # 从0到1完整指南
│   │   ├── installation.md    # 安装教程
│   │   └── global-configuration.md  # 全局配置
│   ├── templates/              # 项目配置模板
│   │   ├── python-shell-project.md  # Python/Shell 模板
│   │   ├── nextjs-project.md        # Next.js 模板
│   │   └── documentation-project.md # 文档项目模板
│   ├── configuration/          # 配置专题
│   │   └── permissions.md      # 权限配置详解
│   └── resources/              # 资源索引
│       └── official-resources.md    # 官方资源
├── gemini-guide/              # Gemini CLI 对比文档
└── .claude/                   # Claude Code 配置
    ├── commands/              # 自定义命令
    │   ├── test.md
    │   ├── build.md
    │   ├── review.md
    │   ├── push.md
    │   ├── fix.md
    │   ├── deploy.md
    │   ├── update.md
    │   └── doc.md
    └── settings.local.json    # 本地权限配置
```

## 核心文档说明

### 主要手册（根目录）
- **README.md**：项目主索引，快速导航到所有文档
- **basic-guide.md**：基础功能教程（安装、Mode切换、文件操作）
- **advanced-guide.md**：高级功能（Skill、MCP、Hooks、Agent SDK）
- **best-practices.md**：Token优化、安全性、团队协作
- **security-guide.md**：敏感信息保护、权限安全、代码审查

### 专题文档（docs/）
- **getting-started/**：完整的从0到1教程，适合新手
- **templates/**：各种项目类型的CLAUDE.md模板和配置示例
- **configuration/**：深入的配置指南
- **resources/**：官方资源和社区资源索引

## 常用命令

### 文档相关
```bash
# 查看所有文档（使用 tree 或 find）
find . -name "*.md" -type f

# 搜索特定内容
grep -r "关键词" *.md docs/

# 查看 Git 状态
git status

# 查看最近提交
git log --oneline -5
```

### Git 提交规范
```bash
# 提交格式：<类型>: <描述>
git commit -m "docs: 更新安装指南"
git commit -m "fix: 修复文档链接错误"
git commit -m "feat: 添加新的配置模板"
```

提交类型：
- `docs`: 文档更新
- `feat`: 新增内容
- `fix`: 修复错误
- `style`: 格式调整
- `refactor`: 重构内容
- `chore`: 其他维护（如更新配置、整理目录）

**提交信息约束：**
- 使用中文，祈使语气，简洁明了
- 不使用 emoji
- **禁止添加 Claude 署名**（不得包含 `Co-Authored-By: Claude` 或 `🤖 Generated with Claude Code`）
- 原子性提交：每个提交只做一件事

### 快速推送（一行命令）
```bash
# 添加、提交、推送一步完成
git add -A && git status && git commit -m "提交信息" && git push origin main
```

## 自定义命令说明

项目已配置 8 个自定义命令（`.claude/commands/`）：

- **/test** - 智能测试执行（主要用于代码项目示例）
- **/build** - 构建检查（主要用于示例说明）
- **/review** - 代码审查流程
- **/push** - 一键提交推送代码
- **/fix** - 自动修复常见问题
- **/deploy** - 自动化部署指南
- **/update** - 依赖更新指南
- **/doc** - 智能文档更新

## 文档编写规范

### Markdown 格式
- 使用标准 GitHub Flavored Markdown
- 代码块标注语言类型（如 ```bash、```json）
- 使用表格组织对比信息
- 使用清晰的标题层级（h1-h4）

### 中文规范
- 使用简体中文
- 专业术语保持英文（如 Claude Code、MCP、Token）
- 中英文之间无需空格（GitHub渲染已优化）
- 使用全角标点符号

### 文档结构
每个主要文档应包含：
1. **标题和简介** - 说明文档目的
2. **目录导航** - 快速跳转（长文档）
3. **核心内容** - 详细说明
4. **代码示例** - 实际可用的例子
5. **常见问题** - FAQ 部分
6. **相关链接** - 关联文档

### 案例格式
使用一致的示例格式：
```markdown
**适用场景**：XXX

**配置示例**：
\```json
{...}
\```

**使用方法**：
\```bash
command
\```
```

## 核心工作原则

### 1. 先想后写（Think Before Acting）

不要假设，把取舍摆出来。动手之前明确说出假设；存在多种理解时列出来；有更简单结构就说出来；搞不清楚就停下来问。

### 2. 能简则简（Simplicity First）

用最少的篇幅解决问题。不加未要求的内容；不为一次性说明搭抽象结构；不预加"未来扩展"内容。自检：读者会觉得冗余吗？如果会，精简。

### 3. 精准修改（Surgical Changes）

只动该动的地方。修改文档时不顺手改旁边的段落/格式/链接；保持原有风格；发现不相关错误提一句，不擅自修改。检验：每处改动都能追溯到用户请求。

### 4. 目标驱动执行（Goal-Driven Execution）

明确完成标准，执行后验证。多步骤任务列出简要计划（步骤 → 验证检查项），完成后逐条确认不遗漏。

## 文档维护流程

### 添加新文档
1. 确定文档分类（入门/模板/配置/资源）
2. 在对应目录创建 Markdown 文件
3. 更新 README.md 的索引链接
4. 确保文档间的交叉引用正确
5. 提交时使用 `docs: 添加XXX文档`

### 更新现有文档
1. 修改文档内容
2. 检查相关链接是否需要更新
3. 更新文档中的日期/版本信息（如有）
4. 提交时使用 `docs: 更新XXX内容`

### 修复文档错误
1. 修正错别字、格式问题、代码错误
2. 提交时使用 `fix: 修复XXX文档中的YYY问题`

## 权限配置建议

### 推荐权限（.claude/settings.json）
```json
{
  "permissions": {
    "allow": [
      "Read",
      "Edit(/README.md)",
      "Edit(/*.md)",
      "Edit(/docs/**/*.md)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(find:*)",
      "Bash(grep:*)"
    ],
    "ask": [
      "Edit(/docs/**)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Write"
    ],
    "deny": [
      "Bash(rm:*)",
      "Bash(sudo:*)",
      "Edit(.claude/settings.json)"
    ]
  }
}
```

## 内容审查要点

### 添加新内容时检查
- ✅ 内容准确性（是否与官方文档一致）
- ✅ 中文表达（是否清晰易懂）
- ✅ 代码示例（是否可执行且正确）
- ✅ 链接有效性（内部链接和外部链接）
- ✅ 格式一致性（与现有文档风格统一）

### 不要
- ❌ 不要创建空文档或待办文档
- ❌ 不要添加未验证的配置示例
- ❌ 不要包含过时的信息
- ❌ 不要使用非标准的 Markdown 语法
- ❌ 不要添加与 Claude Code 无关的内容

## 禁止提交清单

不要将以下内容提交到本仓库：

```
~/.claude/          # 全局个人配置
.vscode/            # 编辑器个人设置
.idea/
*.swp *.swo
.env .env.local     # 环境变量
```

注意：项目级 `.claude.md` **应该**提交（团队共享上下文），全局 `~/.claude/CLAUDE.md` **不应**提交。

## 文档规划规范（SPEC-Lite）

较大改动（新增一级目录、重构结构、批量修改多个文件）时，动手前说明：
- **改动范围**：影响哪些文件/目录
- **改动理由**：为什么要这样调整
- **改动步骤**：分几步完成，每步验证什么

小改动（修改单个文档、修复链接等）不强制。

## 工作流程

### 典型场景：更新文档内容

1. **接收用户请求**
   ```
   用户：更新安装指南，添加 Windows 安装说明
   ```

2. **读取现有文档**
   ```bash
   # 使用 Read 工具读取
   Read docs/getting-started/installation.md
   ```

3. **编辑文档**
   ```bash
   # 使用 Edit 工具修改
   Edit docs/getting-started/installation.md
   ```

4. **检查相关文档**
   ```bash
   # 检查是否需要更新其他关联文档
   Read docs/getting-started/README.md
   ```

5. **提交更改**
   ```bash
   git add docs/getting-started/installation.md
   git commit -m "docs: 添加 Windows 安装说明"
   git push origin main
   ```

### 典型场景：添加新模板

1. **创建模板文件**
   ```bash
   Write docs/templates/new-template.md
   ```

2. **更新索引**
   ```bash
   Edit README.md  # 添加新模板链接
   Edit docs/templates/README.md  # 更新模板列表
   ```

3. **提交**
   ```bash
   git add -A
   git commit -m "feat: 添加XXX项目模板"
   git push origin main
   ```

## 特殊注意事项

### 链接维护
- 使用相对路径而非绝对路径
- 定期检查链接有效性
- 更新文件位置时同步更新所有引用

### 版本信息
- 文档中提到的 Claude Code 版本应保持更新
- 标注"最后更新日期"（如需要）
- 跟踪官方文档变更

### 社区贡献
- 欢迎 Pull Request
- 审查贡献内容的准确性和质量
- 保持友好和专业的交流

## Git 分支策略

- **main**：主分支，稳定内容
- **feature/xxx**：新功能或大型更新
- **fix/xxx**：修复错误

小改动可直接提交到 main，大改动使用分支。

## 相关资源

### 官方文档
- [Claude Code 官方文档](https://code.claude.com/docs/)
- [Claude API 文档](https://docs.claude.com/)

### 本项目链接
- [主 README](README.md)
- [从0到1指南](docs/getting-started/README.md)
- [项目模板](docs/templates/)
