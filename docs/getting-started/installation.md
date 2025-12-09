# Claude Code 安装指南

完整的 Claude Code 安装和初始化配置指南。

---

## 系统要求

### 支持的操作系统

| 操作系统 | 最低版本 | 推荐版本 |
|---------|---------|---------|
| macOS | 10.15 (Catalina) | 最新版本 |
| Linux | Ubuntu 20.04+ / Debian 10+ | Ubuntu 22.04+ |
| Windows | Windows 10 | Windows 11 |

### 必要依赖

- **Node.js**: >= 18.0.0（推荐使用 LTS 版本）
- **Git**: >= 2.0（用于版本控制功能）
- **终端**: Bash 或 Zsh（Windows 使用 PowerShell 或 Git Bash）

### 验证依赖

```bash
# 检查 Node.js 版本
node --version
# 应输出: v18.x.x 或更高

# 检查 npm 版本
npm --version
# 应输出: 9.x.x 或更高

# 检查 Git
git --version
# 应输出: git version 2.x.x
```

---

## 安装方法

### 方法 1: 使用 npm 安装（推荐）

```bash
# 全局安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 验证安装
claude --version
```

**优势**：
- ✅ 跨平台支持
- ✅ 自动处理依赖
- ✅ 便于更新

### 方法 2: 使用 Homebrew（仅 macOS）

```bash
# 安装 Node.js（如果尚未安装）
brew install node

# 使用 npm 安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 验证安装
claude --version
```

### 方法 3: 手动下载二进制文件

访问 [Claude Code 官网](https://claude.com/claude-code) 下载适合你操作系统的二进制文件。

**步骤**：
1. 下载对应平台的安装包
2. 解压到指定目录
3. 将可执行文件路径添加到 PATH
4. 验证安装：`claude --version`

---

## 首次启动和认证

### 1. 启动 Claude Code

```bash
# 在任意目录启动
claude
```

### 2. OAuth 认证

首次运行时会自动启动浏览器进行 OAuth 认证：

```
欢迎使用 Claude Code!

请在浏览器中完成登录...
正在打开: https://console.anthropic.com/auth/...

等待认证完成...
```

### 3. 验证认证状态

```bash
# 成功认证后会显示
✓ 认证成功
✓ 已连接到 Claude API

# 可以开始使用 Claude Code
>
```

### 账户要求

- ✅ 需要有 Claude Pro 或 Claude Team 订阅
- ✅ 在 [console.anthropic.com](https://console.anthropic.com) 设置有效的计费账户
- ✅ API 访问权限已启用

---

## Shell 配置

### Bash 配置（可选）

Claude Code 自动支持 Bash，无需额外配置。如需自定义：

```bash
# 编辑 ~/.bashrc
vim ~/.bashrc

# 添加别名（可选）
alias c='claude'
alias cc='claude'

# 保存后重新加载
source ~/.bashrc
```

### Zsh 配置（可选）

Claude Code 自动支持 Zsh，如需自定义：

```bash
# 编辑 ~/.zshrc
vim ~/.zshrc

# 添加别名（可选）
alias c='claude'
alias cc='claude'

# 保存后重新加载
source ~/.zshrc
```

### 自动补全（可选）

```bash
# 生成自动补全脚本
claude --generate-completion bash > ~/.claude-completion.bash
# 或
claude --generate-completion zsh > ~/.claude-completion.zsh

# 在 ~/.bashrc 或 ~/.zshrc 中添加
source ~/.claude-completion.bash
# 或
source ~/.claude-completion.zsh
```

---

## 验证安装

### 基本验证

```bash
# 1. 检查版本
claude --version
# 应输出: Claude Code v1.x.x

# 2. 查看帮助
claude --help
# 应显示帮助信息和可用命令

# 3. 测试运行
claude
# 应成功启动交互式会话
```

### 功能验证

在 Claude Code 交互会话中：

```bash
# 启动 Claude
claude

# 测试基本命令
> /help
# 应显示可用命令列表

> 你好
# 应收到 Claude 的回复

> 退出
# 退出会话
```

---

## 更新 Claude Code

### 使用 npm 更新

```bash
# 更新到最新版本
npm update -g @anthropic-ai/claude-code

# 或完全重新安装
npm uninstall -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code
```

### 检查更新

```bash
# 查看当前版本
claude --version

# 查看最新可用版本
npm view @anthropic-ai/claude-code version
```

---

## 卸载 Claude Code

### 使用 npm 卸载

```bash
# 卸载全局包
npm uninstall -g @anthropic-ai/claude-code

# 清理配置文件（可选）
rm -rf ~/.claude
```

### 清理认证信息

```bash
# 删除认证令牌
claude --logout

# 或手动删除配置目录
rm -rf ~/.claude
```

---

## 常见问题

### Q1: npm 安装失败

**问题**：`Error: EACCES: permission denied`

**解决方案**：

```bash
# 方法 1: 使用 sudo（不推荐）
sudo npm install -g @anthropic-ai/claude-code

# 方法 2: 配置 npm 全局路径（推荐）
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'

# 添加到 PATH（~/.bashrc 或 ~/.zshrc）
export PATH=~/.npm-global/bin:$PATH

# 重新加载配置
source ~/.bashrc  # 或 source ~/.zshrc

# 重新安装
npm install -g @anthropic-ai/claude-code
```

### Q2: 认证失败

**问题**：无法完成 OAuth 认证

**解决方案**：

1. 检查网络连接
2. 确认浏览器未被阻止
3. 清除认证缓存：`rm -rf ~/.claude/auth`
4. 重新启动：`claude`
5. 检查账户状态：访问 [console.anthropic.com](https://console.anthropic.com)

### Q3: 命令未找到

**问题**：`command not found: claude`

**解决方案**：

```bash
# 检查安装位置
npm list -g @anthropic-ai/claude-code

# 检查 PATH 配置
echo $PATH

# 查找 Claude 可执行文件
which claude

# 如果找不到，手动添加到 PATH
export PATH="$(npm bin -g):$PATH"
```

### Q4: Node.js 版本过低

**问题**：`Error: Requires Node.js >= 18.0.0`

**解决方案**：

```bash
# 使用 nvm 安装最新 LTS 版本
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install --lts
nvm use --lts

# 验证版本
node --version

# 重新安装 Claude Code
npm install -g @anthropic-ai/claude-code
```

### Q5: Windows 安装问题

**问题**：Windows 环境下安装或运行失败

**解决方案**：

1. **使用 PowerShell（管理员模式）**：
   ```powershell
   npm install -g @anthropic-ai/claude-code
   ```

2. **使用 Git Bash**：
   - 下载安装 [Git for Windows](https://git-scm.com/download/win)
   - 在 Git Bash 中运行安装命令

3. **配置执行策略**：
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```

---

## 下一步

安装完成后，建议继续阅读：

- [全局配置指南](./global-configuration.md) - 配置 ~/.claude/ 目录
- [项目配置指南](./project-configuration.md) - 创建项目级 CLAUDE.md
- [基础使用手册](../../basic-guide.md) - 学习基本功能
- [进阶使用手册](../../advanced-guide.md) - 探索高级功能

---

## 参考资源

- [Claude Code 官方文档](https://code.claude.com/docs/)
- [Node.js 官方下载](https://nodejs.org/)
- [Git 官方下载](https://git-scm.com/)
- [问题反馈](https://github.com/anthropics/claude-code/issues)
