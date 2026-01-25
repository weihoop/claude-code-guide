# Skills 安装指南

完整的 Skills 安装方法和平台支持说明。

---

## 📋 目录

- [平台支持](#平台支持)
- [安装方法](#安装方法)
- [配置 Skills 目录](#配置-skills-目录)
- [验证安装](#验证安装)
- [常见问题](#常见问题)

---

## 🖥️ 平台支持

### Claude.ai（网页版）

**支持情况**: ✅ 完全支持

**特点**:
- 无需手动安装，从 Skills 市场直接添加
- 自动更新，无需维护
- 跨设备同步
- 限制：仅支持官方认证的 Skills

**使用场景**: 日常使用、快速尝试、团队协作

---

### Claude Code（CLI）

**支持情况**: ✅ 完全支持

**特点**:
- 支持所有开源 Skills
- 可自定义和修改
- 本地管理，完全控制
- 支持私有 Skills

**使用场景**: 开发者、高级用户、企业内部

**系统要求**:
- macOS 10.15+ 或 Linux
- Git（用于克隆 Skills）
- Claude Code CLI >= 1.0

---

### Claude API（编程集成）

**支持情况**: ✅ 通过 SDK 支持

**特点**:
- Python/TypeScript SDK
- 完全编程控制
- 适合自动化和批量处理
- 需要 API key

**使用场景**: API 集成、自动化脚本、企业应用

---

## 📦 安装方法

### 方法 1：一键安装脚本（推荐）

**适用平台**: Claude Code CLI

**安装 Top 10 推荐 Skills**:

```bash
# 下载安装脚本
wget https://raw.githubusercontent.com/weihoop/claude-code-guide/main/skills/scripts/install_top10.sh

# 执行安装
bash install_top10.sh

# 清理脚本（可选）
rm install_top10.sh
```

**脚本功能**:
- ✅ 自动创建 Skills 目录
- ✅ 检查 Git 和网络环境
- ✅ 并发安装 10 个 Skills
- ✅ 显示进度和结果
- ✅ 验证安装成功

**安装的 Skills**:
1. NotebookLM - 知识管理
2. Obsidian - 笔记系统
3. Planning with Files - 项目规划
4. Skill Creator - 创建自定义 Skills
5. Frontend Design - 前端设计
6. Superpowers - 开发工具集
7. Rube MCP - 500+ 应用集成
8. Baoyu Skills - 自媒体工具
9. Media Skills - 社交媒体管理
10. Skill Lookup - Skills 搜索

---

### 方法 2：npx 快速安装（推荐）

**适用平台**: Claude Code CLI

**前提条件**: 已安装 Node.js >= 14

**安装官方 Skills**:
```bash
npx skills add anthropics/skills
```

**安装社区 Skills**:
```bash
# Superpowers 开发工具
npx skills add obra/superpowers

# Baoyu 自媒体工具
npx skills add JimLiu/baoyu-skills

# 支持 GitHub 仓库格式：owner/repo
npx skills add <github-owner>/<repo-name>
```

**优势**:
- ⚡ 快速安装
- 🔄 自动配置
- 📦 依赖管理
- ✅ 版本控制

---

### 方法 3：手动 Git 克隆（灵活）

**适用平台**: Claude Code CLI

**步骤**:

#### 1. 创建 Skills 目录
```bash
mkdir -p ~/.config/claude-code/skills
cd ~/.config/claude-code/skills
```

#### 2. 克隆 Skill 仓库
```bash
# 通用格式
git clone <skill-repo-url> <skill-name>

# 示例：安装 NotebookLM
git clone https://github.com/PleasePrompto/notebooklm-skill.git notebooklm
```

#### 3. 验证安装
```bash
head ~/.config/claude-code/skills/notebooklm/SKILL.md
```

**优势**:
- 🔧 完全控制
- 🔍 可以审查代码
- 📝 可以修改和定制
- 🔄 手动控制更新

---

### 方法 4：Claude.ai 市场（简单）

**适用平台**: Claude.ai 网页版

**步骤**:

1. 登录 [Claude.ai](https://claude.ai/)
2. 创建新对话或打开现有对话
3. 点击输入框上方的 **"+ Skills"**
4. 搜索或浏览 Skills 列表
5. 点击 **"Add"** 添加到对话
6. 开始使用 Skill

**优势**:
- 🚀 最简单，零配置
- 🔄 自动更新
- 📱 跨设备同步
- 🔐 官方审核的 Skills

**限制**:
- ⚠️ 仅支持官方认证的 Skills
- ⚠️ 无法修改 Skill 行为
- ⚠️ 需要网络连接

---

### 方法 5：API 编程安装（高级）

**适用平台**: Python/TypeScript 应用

**Python 示例**:
```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    skills=["notebooklm", "obsidian"],  # 指定要使用的 Skills
    messages=[{
        "role": "user",
        "content": "帮我整理这些笔记"
    }]
)

print(response.content[0].text)
```

**TypeScript 示例**:
```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

const response = await client.messages.create({
  model: 'claude-sonnet-4-20250514',
  skills: ['notebooklm', 'obsidian'],
  messages: [{
    role: 'user',
    content: '帮我整理这些笔记'
  }]
});

console.log(response.content[0].text);
```

**详细教程**: [编程使用 Skills](guides/programming-usage.md)

---

## 🗂️ 配置 Skills 目录

### 默认目录位置

| 平台 | 目录路径 |
|------|---------|
| **macOS** | `~/.config/claude-code/skills/` |
| **Linux** | `~/.config/claude-code/skills/` |
| **Windows** | `%APPDATA%\claude-code\skills\` |

### 手动创建目录

```bash
# macOS / Linux
mkdir -p ~/.config/claude-code/skills

# Windows (PowerShell)
New-Item -Path "$env:APPDATA\claude-code\skills" -ItemType Directory -Force
```

### 自定义目录（高级）

**设置环境变量**:
```bash
# 临时设置
export CLAUDE_SKILLS_DIR=/path/to/your/skills

# 永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export CLAUDE_SKILLS_DIR=/path/to/your/skills' >> ~/.bashrc
source ~/.bashrc
```

---

## ✅ 验证安装

### 方法 1：列出已安装的 Skills

```bash
ls -la ~/.config/claude-code/skills/
```

**预期输出**:
```
drwxr-xr-x  notebooklm/
drwxr-xr-x  obsidian/
drwxr-xr-x  superpowers/
...
```

### 方法 2：检查 SKILL.md

```bash
# 查看 Skill 描述
head ~/.config/claude-code/skills/notebooklm/SKILL.md

# 检查所有 Skills 的 SKILL.md 是否存在
find ~/.config/claude-code/skills/ -name "SKILL.md"
```

**预期输出**:
```yaml
---
description: >
  上传文档到 NotebookLM，自动进行知识问答和摘要。
---

# NotebookLM Skill
...
```

### 方法 3：使用验证脚本

```bash
bash ~/.config/claude-code-guide/skills/scripts/verify_skills.sh
```

**输出示例**:
```
✅ Skills 目录存在: /Users/xxx/.config/claude-code/skills
✅ 发现 10 个 Skills
✅ 所有 Skills 都有有效的 SKILL.md
```

### 方法 4：在 Claude Code 中测试

```bash
# 启动 Claude Code
claude

# 发送测试消息
> 列出我已安装的 Skills

# Claude 会返回已安装的 Skills 列表
```

---

## ⚙️ 高级配置

### 并发安装多个 Skills

**Bash 并发脚本**:
```bash
#!/bin/bash
SKILLS_DIR="$HOME/.config/claude-code/skills"
mkdir -p "$SKILLS_DIR"

# Skills 列表
declare -a SKILLS=(
    "https://github.com/PleasePrompto/notebooklm-skill.git notebooklm"
    "https://github.com/kepano/obsidian-skills.git obsidian"
    "https://github.com/obra/superpowers.git superpowers"
)

# 并发克隆
for skill in "${SKILLS[@]}"; do
    read -r url name <<< "$skill"
    git clone "$url" "$SKILLS_DIR/$name" &
done

# 等待所有任务完成
wait
echo "✅ 所有 Skills 安装完成"
```

### 批量更新 Skills

```bash
#!/bin/bash
SKILLS_DIR="$HOME/.config/claude-code/skills"

# 遍历所有 Skills 目录
for skill_dir in "$SKILLS_DIR"/*; do
    if [ -d "$skill_dir/.git" ]; then
        echo "更新: $(basename "$skill_dir")"
        cd "$skill_dir" && git pull
    fi
done
```

### 从配置文件安装

**创建 `skills.txt`**:
```
PleasePrompto/notebooklm-skill notebooklm
kepano/obsidian-skills obsidian
obra/superpowers superpowers
```

**批量安装脚本**:
```bash
#!/bin/bash
SKILLS_DIR="$HOME/.config/claude-code/skills"
mkdir -p "$SKILLS_DIR"

while read -r repo name; do
    url="https://github.com/$repo.git"
    echo "安装: $name from $repo"
    git clone "$url" "$SKILLS_DIR/$name"
done < skills.txt
```

---

## 🔄 更新和维护

### 更新单个 Skill

```bash
cd ~/.config/claude-code/skills/<skill-name>
git pull
```

### 更新所有 Skills（推荐脚本）

```bash
# 创建更新脚本
cat > ~/.config/claude-code/update_skills.sh << 'EOF'
#!/bin/bash
SKILLS_DIR="$HOME/.config/claude-code/skills"

echo "🔄 开始更新所有 Skills..."
for skill in "$SKILLS_DIR"/*; do
    if [ -d "$skill/.git" ]; then
        name=$(basename "$skill")
        echo "更新: $name"
        cd "$skill" && git pull
    fi
done
echo "✅ 所有 Skills 更新完成"
EOF

# 添加执行权限
chmod +x ~/.config/claude-code/update_skills.sh

# 运行更新
~/.config/claude-code/update_skills.sh
```

### 删除 Skill

```bash
# 删除单个 Skill
rm -rf ~/.config/claude-code/skills/<skill-name>

# 清空所有 Skills
rm -rf ~/.config/claude-code/skills/*
```

---

## ⚠️ 常见问题

### Q1: 安装后 Skill 不生效？

**排查步骤**:
```bash
# 1. 检查目录结构
ls -la ~/.config/claude-code/skills/<skill-name>/

# 2. 验证 SKILL.md 存在且有效
head ~/.config/claude-code/skills/<skill-name>/SKILL.md

# 3. 检查 YAML frontmatter 格式
cat ~/.config/claude-code/skills/<skill-name>/SKILL.md | head -10

# 4. 重启 Claude Code
exit
claude
```

### Q2: Git clone 失败？

**可能原因**:
- 网络问题：使用代理或切换网络
- Git 未安装：`brew install git` (macOS) 或 `sudo apt install git` (Linux)
- 仓库不存在：检查 URL 是否正确
- 权限问题：使用 HTTPS 而非 SSH URL

**解决方法**:
```bash
# 检查 Git 版本
git --version

# 使用 HTTPS URL
git clone https://github.com/owner/repo.git

# 配置代理（如果需要）
git config --global http.proxy http://proxy.example.com:8080
```

### Q3: Skills 目录在哪里？

**查找方法**:
```bash
# 方法 1：检查环境变量
echo $CLAUDE_SKILLS_DIR

# 方法 2：默认位置
ls -la ~/.config/claude-code/skills/

# 方法 3：搜索 SKILL.md 文件
find ~ -name "SKILL.md" 2>/dev/null
```

### Q4: 如何备份 Skills？

**备份方法**:
```bash
# 备份整个 Skills 目录
tar -czvf skills-backup-$(date +%Y%m%d).tar.gz ~/.config/claude-code/skills/

# 恢复备份
tar -xzvf skills-backup-20260125.tar.gz -C ~/
```

### Q5: 可以安装私有 Skills 吗？

**可以！步骤**:
```bash
# 1. 克隆私有仓库（需要认证）
cd ~/.config/claude-code/skills/
git clone git@github.com:your-org/private-skill.git

# 2. 或使用 Personal Access Token
git clone https://YOUR_TOKEN@github.com/your-org/private-skill.git
```

### Q6: npx skills 命令找不到？

**解决方法**:
```bash
# 1. 检查 Node.js 版本
node --version  # 需要 >= 14

# 2. 更新 npm
npm install -g npm@latest

# 3. 清除 npx 缓存
npx clear-npx-cache

# 4. 使用完整路径
$(npm bin -g)/npx skills add <skill>
```

---

## 📊 安装方法对比

| 特性 | 一键脚本 | npx | 手动 Git | Claude.ai | API |
|------|---------|-----|---------|----------|-----|
| **易用性** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **灵活性** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **速度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Skills 数量** | 10 个 | 无限 | 无限 | 有限 | 无限 |
| **需要 Node.js** | ❌ | ✅ | ❌ | ❌ | ✅ |
| **需要 Git** | ✅ | ✅ | ✅ | ❌ | ❌ |
| **支持私有 Skill** | ✅ | ✅ | ✅ | ❌ | ✅ |
| **自动更新** | ❌ | ❌ | ❌ | ✅ | ❌ |
| **适合场景** | 新手快速开始 | 日常使用 | 高级用户 | 临时使用 | 编程集成 |

---

## 📚 延伸阅读

- [快速入门](getting-started.md) - 5 分钟上手 Skills
- [Top 10 推荐](top-10/) - 最实用的 Skills
- [编程使用](guides/programming-usage.md) - Python/Node.js 集成
- [故障排除](guides/troubleshooting.md) - 解决常见问题

---

**返回**: [Skills 主页](README.md)

**最后更新**: 2026-01-25
