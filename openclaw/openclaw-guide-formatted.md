---
title: OpenClaw 命令行指令指南
slug: openclaw-cli-guide
summary: 从基础控制到高阶维护、故障排查，系统化梳理 OpenClaw 全部命令行指令，帮你快速上手终端操作。
---

Hi，我是 Rex。

玩过 OpenClaw（clawdbot）的朋友都知道，它的强大毋庸置疑，但那繁多的控制台指令常常让人头大，尤其是和我一样代码基础一般的朋友。

过去的一周，我为了优化数据流转以及拥有一个服务器管家，我花了大把时间死磕 OpenClaw 的配置，就是为了让他更好用。说实话，最开始我也在各种文档里迷路，效率极低。不过我有个习惯，遇到繁琐的流程，就把它**系统化、标准化**。

于是，我把这周踩过的坑、验证过的指令，从基础控制到高阶维护、再到故障排查，完完整整地梳理了一遍。现在当我面对黑底白字的终端不知所措的时候，依旧会翻开它，然后找到答案。

## 01 基础控制：一切的起点

很多时候，我们不需要复杂的骚操作，只需要确认"它还活着吗"。这几个指令是我用得比较多的。

### 查看状态

这是最常用的指令，一眼看清全局。

```bash
# 查看完整状态（推荐）
openclaw status

# 查看详细状态（包含深度探测，排查问题必用）
openclaw status --deep

# 查看所有信息（适合截图分享给别人看）
openclaw status --all

# 仅查看健康状态（快速检查）
openclaw health
```

### 服务管理

作为系统的"运维人员"，你得学会管理 Gateway 服务。别等到服务挂了才手忙脚乱。

```bash
# 查看 Gateway 服务状态
openclaw gateway status

# 启动服务
openclaw gateway start

# 停止服务
openclaw gateway stop

# 重启服务（最常用的一招鲜）
openclaw gateway restart

# 安装服务（设置为开机自启）
openclaw gateway install

# 卸载服务
openclaw gateway uninstall
```

### 实时监控日志

排查问题时，盯着日志看是基本功。

```bash
# 查看实时日志（盯着它跑，就像看心电图）
openclaw logs --follow
```

## 02 配置管理：打造个性化 Agent

OpenClaw 的强大在于可配置性。不要只用默认设置，要让它适应你的工作流。

### 查看与修改配置

```bash
# 查看完整配置
openclaw config get

# 查看特定配置项（例如查看 gateway 端口）
openclaw config get gateway.port

# 查看所有 agent 配置
openclaw config get agents

# 进入交互式配置向导（新手强烈推荐！跟着引导走）
openclaw configure

# 单独配置特定部分
openclaw configure --section channels  # 配置渠道
openclaw configure --section models    # 配置模型
openclaw configure --section web       # 配置 Web 端

# 命令行快速设置（老手专用）
openclaw config set gateway.port 18789
openclaw config set agents.main.model "claude-sonnet-4-5"

# 删除某个配置项
openclaw config unset some.config.key
```

### 配置文件位置（必背）

这几个路径一定要记清楚，有时候直接用编辑器改文件比敲命令更快：

| 配置项      | 路径                          |
| -------- | --------------------------- |
| 主配置文件    | `~/.openclaw/openclaw.json` |
| 工作区      | `~/.openclaw/workspace`     |
| Agent 配置 | `~/.openclaw/agents/main/`  |

快速查看配置：

```bash
cat ~/.openclaw/openclaw.json | jq
```

## 03 维护与会话：系统保养

系统运行久了，难免会有积压。这时候需要定期的维护和清理。

### 更新与体检

```bash
# 检查更新
openclaw update

# 更新到最新版本（保持最新总是好的）
npm update openclaw -g

# 查看当前版本
openclaw --version

# 运行全系统诊断（卡顿时的第一反应）
openclaw doctor

# 安全审计
openclaw security audit
openclaw security audit --deep  # 深度审计
```

### 会话管理

看看你的 Agent 都在聊些什么，花了多少钱。

```bash
# 列出所有会话
openclaw sessions

# 查看特定会话的历史记录
openclaw sessions history --sessionKey agent:main:main

# 查看统计（Token 使用量、费用消耗）
openclaw gateway usage-cost
```

### 清理与重置（高能预警）

这几个命令**威力巨大**，执行前请三思，除非你确定要推倒重来。

```bash
# 重置配置（保留 CLI 工具，重置设置）
openclaw reset

# 完全卸载（包括所有数据，慎用！）
openclaw uninstall

# 重新初始化（重装后的第一步）
openclaw setup
openclaw onboard
```

## 04 高阶操作：自动化与集成

这是我最喜欢的部分，也是构建**自动化工作流**的核心。

### 消息与通知

```bash
# 发送 Telegram 消息（测试机器人通不通）
openclaw message send --channel telegram --target @username --message "Hello"

# 发送通知到特定节点（比如手机）
openclaw nodes notify --node phone --title "提醒" --body "该喝水了"

# 查看所有频道状态
openclaw channels

# 登录特定频道（例如 WhatsApp）
openclaw channels login whatsapp
```

### 定时任务（Cron）管理

让 OpenClaw 成为你的 24 小时守夜人。

```bash
# 查看所有 cron 任务列表
openclaw cron list

# 查看 cron 服务状态
openclaw cron status

# 手动触发运行特定任务（测试任务逻辑）
openclaw cron run --jobId <job-id>

# 查看任务执行历史
openclaw cron runs --jobId <job-id>
```

## 05 内存与节点管理

### 内存搜索

OpenClaw 是有记忆的，你可以随时调用它的知识库。

```bash
# 搜索 MEMORY.md 和 memory/*.md
openclaw memory search "关键词"
```

### 节点与设备

管理连接到 OpenClaw 的各种设备节点。

```bash
# 列出所有在线节点
openclaw nodes status

# 查看某个节点的详情
openclaw nodes describe --node <node-id>

# 给指定节点发通知
openclaw nodes notify --node <node-id> --title "标题" --body "内容"
```

## 06 故障排查 SOP

遇到问题不要慌，按照这个 **SOP（标准作业程序）** 走一遍，90% 的问题都能解决。

### 常见问题检查步骤

按顺序依次执行：

1. **检查服务**：`openclaw gateway status`
2. **看日志**：`openclaw logs --follow`
3. **跑诊断**：`openclaw doctor`
4. **查配置**：`openclaw config get`
5. **测连接**：`openclaw gateway probe`

### 重启 Gateway 的三种姿势

| 方式   | 命令                                                  |
| ---- | --------------------------------------------------- |
| 优雅重启 | `openclaw gateway restart`                          |
| 手动重启 | `openclaw gateway stop` 然后 `openclaw gateway start` |
| 暴力重启 | `openclaw gateway --force`                          |

### 安全检查

```bash
# 权限修复
chmod 700 ~/.openclaw

# 检查代理
openclaw config get gateway.trustedProxies
```

***

## 快速参考（Cheat Sheet）

最后，送给大家几个最常用的"救命"指令，背下来准没错：

| 指令                         | 用途                 |
| -------------------------- | ------------------ |
| `openclaw status`          | 只要觉得不对劲，先敲这个       |
| `openclaw logs --follow`   | 想知道 Agent 在想什么，看这个 |
| `openclaw gateway restart` | 重启解千愁              |
| `openclaw configure`       | 不会改配置，用向导          |
| `openclaw doctor`          | 给系统看病              |
| `openclaw update`          | 保持更新               |

***

## 写在最后

在这个信息爆炸的时代，工具是我们的杠杆。但如果工具本身的使用成本过高，杠杆就变成了负担。

整理这份指南，初衷是为了让我自己的操作更丝滑，现在分享出来，也希望通过这种公开的系统化复盘，帮大家省去翻阅枯燥文档的时间。

在这个 AI Agent 爆发的前夜，**掌握工具的底层指令，就是掌握了未来的生产力钥匙**。

如果你觉得这份整理对你有用，欢迎点赞、在看，或者转发给同样在折腾的朋友，有错误和不足也欢迎大家留言讨论。

我是 Rex，致力于用数据和系统构建更高效的人生。下期见。
