# 多 Skill 串联工作流

一个任务需要依次调用多个 Skill 时，默认每个工具调用都会弹出确认提示。本文介绍三种方案消除确认、实现全自动串联。

---

## 问题场景

以律师工作为例，处理一个劳动争议案件需要依次调用：

```
case-summary → compensation-calc → evidence-organize → legal-doc-draft → court-opinion
```

每个 Skill 内部会调用 `Write`、`Bash` 等工具，每次都弹确认，严重打断流程。

---

## 方案一：启动时跳过所有确认（推荐日常使用）

```bash
claude --dangerously-skip-permissions
```

**效果**：当前 session 内所有工具调用不弹确认，Skill 串联全自动跑完。

**适用场景**：你清楚要执行什么任务、信任当前工作目录下的所有操作。

**注意**：只影响当前 session，下次启动恢复正常。

---

## 方案二：项目目录级别放开权限

在你的工作目录下创建 `.claude/settings.json`，只对该目录生效：

```bash
mkdir -p .claude
```

```json
{
  "permissions": {
    "allow": ["*"]
  }
}
```

**效果**：在这个目录下启动 Claude Code，所有操作自动允许，其他目录不受影响。

**适用场景**：固定在某个目录处理任务（如专门的案件工作目录），想永久免确认。

---

## 方案三：全局 settings 精确放开常用操作

编辑 `~/.claude/settings.json`，把 Skill 常用的操作从 `ask` 移到 `allow`：

```json
{
  "permissions": {
    "allow": [
      "Write",
      "Edit",
      "Bash(mkdir:*)",
      "Bash(cp:*)",
      "Bash(mv:*)",
      "Bash(python3:*)"
    ]
  }
}
```

**适用场景**：想在所有项目里减少确认，但不想完全放开权限。

---

## 方案对比

| 方案 | 范围 | 持久性 | 安全性 | 适合场景 |
|------|------|--------|--------|---------|
| `--dangerously-skip-permissions` | 当前 session | 临时 | 中 | 临时任务、已知流程 |
| 项目级 `settings.json` | 单个目录 | 永久 | 高 | 固定工作目录 |
| 全局 `allow` 精确放开 | 所有项目 | 永久 | 高 | 常用无副作用操作 |

---

## 推荐组合

**日常工作**：在案件工作目录建项目级 `settings.json`（方案二），一次配置永久生效。

**临时任务**：启动时加 `--dangerously-skip-permissions`（方案一），不改任何配置。

**不确定操作保留确认**：数据库写入、服务重启、`kill` 进程等高风险操作不要加入 allow，保留人工确认作为最后防线。
