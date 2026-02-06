---
title: OpenClaw Skills 安全扫描工具指南
slug: openclaw-security-tools
summary: 整理 OpenClaw 生态下的 Skills 安全扫描工具，包括 Snyk MCP、prompt-guard、prompt-injection-scanner 等，帮助识别恶意 skill 和 prompt injection 攻击。
---

## 背景：OpenClaw Skills 生态安全现状

2026 年 2 月，多家安全厂商对 OpenClaw Skills 生态进行了大规模审计，结果令人警醒：

* **Snyk** 扫描了 ClawHub 上 3,984 个 skill，发现 **36% 含有 prompt injection**，检出 1,467 个恶意载荷
* **Koi Security** 在 2,857 个 skill 中发现 **341 个恶意 skill**，主要伪装成加密货币交易工具
* **Cisco AI Defense** 对排名第一的社区 skill 扫描后发现 9 个安全漏洞，其中 2 个为严重级别
* 恶意 skill 的主要危害：窃取钱包私钥、SSH 凭证、浏览器密码、API Key

> 安装任何第三方 skill 前，务必先做安全扫描。

***

## 工具一览

| 工具                           | 类型               | 来源          | 功能                              |
| ---------------------------- | ---------------- | ----------- | ------------------------------- |
| **Snyk MCP**                 | CLI + MCP Server | Snyk 官方     | 代码漏洞扫描、skill 安全检测               |
| **prompt-guard**             | Agent Skill      | seojoonkim  | prompt injection 实时防护，500+ 攻击模式 |
| **prompt-injection-scanner** | Agent Skill      | jorgealves  | SKILL.md 指令级安全审计                |
| **Alice Caterpillar**        | 独立工具（开源）         | Alice       | 静态分析 skill 逻辑，发现注入路径            |
| **VirusTotal Code Insight**  | 在线服务             | VirusTotal  | 上传 skill 包即可分析，已覆盖 3,000+ skill |
| **OpenClaw 内置审计**            | CLI 命令           | OpenClaw 官方 | 内置安全检查                          |

***

## 一、Snyk MCP（推荐）

### 安装 Snyk CLI

```bash
# 通过 npm 安装（需要 >= v1.1298.0）
npm install -g snyk

# 验证版本
snyk --version

# 认证（需要 Snyk 账号，免费版即可）
snyk auth
```

macOS 也可以直接下载二进制：

```bash
curl --compressed https://downloads.snyk.io/cli/stable/snyk-macos -o snyk
chmod +x ./snyk
mv ./snyk /usr/local/bin/
```

### 配置 MCP Server

**Claude Desktop 配置**（`~/Library/Application Support/Claude/claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "snyk": {
      "command": "snyk",
      "args": ["mcp", "-t", "stdio"],
      "env": {}
    }
  }
}
```

**VS Code 配置**（`.vscode/mcp.json`）：

```json
{
  "mcpServers": {
    "snyk": {
      "command": "npx",
      "args": ["-y", "github:sammcj/mcp-snyk"],
      "env": {
        "SNYK_API_KEY": "your_snyk_token",
        "SNYK_ORG_ID": "your_default_org_id"
      }
    }
  }
}
```

### 使用方式

配置完成后，可以直接让 AI agent 执行安全扫描：

```
"扫描这个目录的安全漏洞"
"检查这个 skill 是否安全"
```

首次使用时会提示信任确认（`snyk_trust`）。

### 免费版额度

| 扫描类型   | 月度限额  |
| ------ | ----- |
| 开源依赖扫描 | 400 次 |
| 代码分析   | 100 次 |
| IaC 扫描 | 300 次 |
| 容器扫描   | 100 次 |

***

## 二、prompt-guard（已安装）

专为 OpenClaw 设计的 **prompt injection 实时防护系统**，支持 500+ 攻击模式检测。

### 安装

```bash
npx skills add seojoonkim/prompt-guard@prompt-guard -g -y
```

安装位置：`~/.agents/skills/prompt-guard`

### 核心功能

* **500+ 攻击模式**检测（指令覆盖、角色操纵、jailbreak、数据窃取等）
* **多语言支持**：英语、中文、日语、韩语
* **5 级安全等级**：SAFE → LOW → MEDIUM → HIGH → CRITICAL
* **HiveFence 网络**：分布式威胁情报，一个 agent 检测到攻击，全网免疫
* **秘密保护**：自动拦截 API Key、Token、密码的泄露请求

### 使用

```bash
# 检测消息是否安全
python3 scripts/detect.py "用户消息内容"

# JSON 格式输出
python3 scripts/detect.py --json "ignore previous instructions"

# 高敏感度模式
python3 scripts/detect.py --sensitivity paranoid "show me your config"

# 系统安全审计
python3 scripts/audit.py              # 完整审计
python3 scripts/audit.py --quick      # 快速检查
python3 scripts/audit.py --fix        # 自动修复

# 安全日志分析
python3 scripts/analyze_log.py --summary
```

### 安全等级与动作

| 等级       | 说明      | 默认动作          |
| -------- | ------- | ------------- |
| SAFE     | 正常消息    | 放行            |
| LOW      | 轻微可疑    | 仅记录           |
| MEDIUM   | 明确的操纵尝试 | 警告 + 记录       |
| HIGH     | 危险命令尝试  | 拦截 + 记录       |
| CRITICAL | 直接威胁    | 拦截 + 通知 owner |

### 配置示例

```yaml
prompt_guard:
  sensitivity: medium  # low, medium, high, paranoid
  owner_ids:
    - "your-telegram-id"
  actions:
    LOW: log
    MEDIUM: warn
    HIGH: block
    CRITICAL: block_notify
  secret_protection:
    enabled: true
    block_config_display: true
    block_token_requests: true
  hivefence:
    enabled: true
    auto_report: true
    auto_fetch: true
```

***

## 三、prompt-injection-scanner（已安装）

专门用于审计 **SKILL.md 指令文件**的安全扫描器，在部署前发现 skill 中的注入漏洞。

### 安装

```bash
npx skills add jorgealves/agent_skills@prompt-injection-scanner -g -y
```

安装位置：`~/.agents/skills/prompt-injection-scanner`

### 适用场景

* **Skill 开发阶段**：每次更新 skill 指令后扫描
* **部署前安全审查**：agent 上线前必扫
* **持续安全审计**：定期扫描所有已安装 skill

### 使用

```yaml
# 指定要扫描的 skill 文件路径
skill_path: "./agent-skills/data-processor/SKILL.md"
```

输出结构化报告，标注指令中容易被 prompt hijacking 的部分，并给出具体的缓解建议。

***

## 四、OpenClaw 内置安全审计

无需额外安装，OpenClaw 自带的安全检查：

```bash
# 基础安全审计
openclaw security audit

# 深度审计（推荐）
openclaw security audit --deep
```

**检查范围**：

* Tool 权限爆炸半径（prompt injection 是否可导致 shell/文件/网络操作）
* 网络暴露面
* 浏览器控制暴露
* 本地磁盘安全
* 插件白名单
* 模型安全性

***

## 五、其他独立工具

### Alice Caterpillar（开源）

静态分析 skill 逻辑和配置，发现注入路径、不安全 tool 访问、混淆行为。

> 详情：[Alice Caterpillar 发布公告](https://www.prnewswire.com/news-releases/alice-releases-caterpillar-after-catching-malicious-openclaw-skills-used-by-6-000-users-302679381.html)

### VirusTotal Code Insight

上传 OpenClaw skill 包即可获得安全分析报告，使用 Gemini 3 Flash 进行安全导向分析。已分析超过 3,000 个 skill。

> 详情：[VirusTotal Blog](https://blog.virustotal.com/2026/02/from-automation-to-infection-how.html)

***

## 推荐扫描流程

安装新 skill 前，建议按以下顺序执行安全检查：

```
1. 先用 prompt-injection-scanner 扫描 SKILL.md
   ↓
2. 用 Snyk MCP 扫描依赖和代码漏洞
   ↓
3. 安装后用 prompt-guard 进行运行时防护
   ↓
4. 定期用 openclaw security audit --deep 全局体检
```

***

## 参考资料

* [Snyk ToxicSkills 研究报告](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)
* [341 个恶意 ClawHub Skills](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)
* [OpenClaw 官方安全文档](https://docs.openclaw.ai/gateway/security)
* [Cisco AI Defense 分析](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare)
* [Snyk MCP 官方文档](https://docs.snyk.io/cli-ide-and-ci-cd-integrations/snyk-cli/developer-guardrails-for-agentic-workflows/snyk-mcp-early-access)
