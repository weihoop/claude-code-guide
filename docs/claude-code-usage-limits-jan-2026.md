# Claude Code 使用限制变化记录（2026年1月）

> 最后更新：2026-01-13

## 概述

2026年1月，Claude Code 的使用限制经历了两次重要变化，导致许多用户（包括 Max20 套餐用户）感觉可用对话次数明显减少。

## 变化时间线

### 第一波变化：1月1日 - 节日双倍限额到期

- **时间**：2026年1月1日
- **原因**：圣诞节到新年期间，Anthropic 临时**双倍使用限额**作为节日礼物
- **影响**：1月1日恢复正常基准，许多用户感觉可用量下降了 **60%**
- **实际情况**：不是降低了，而是节日加成取消，恢复到正常水平

**用户反馈**：
- 习惯了节日期间的双倍限额后，恢复正常感觉像是被削减
- 一些用户在 Reddit、GitHub、Discord 上表达了困惑

### 第二波变化：1月8日 - Opus 4.5 限制大幅收紧 ⚠️

- **时间**：2026年1月8日（周四）每周限额重置后
- **影响**：Opus 4.5 使用限制**显著降低**，是自2025年11月推出以来**最严格的限制**
- **严重程度**：比之前所有周期都更严格

**用户反馈**：
- 过去3个月从未遇到限额，现在**连续使用2小时就达到限额**
- Max 订阅用户**立即触发使用限制**
- GitHub Issue #17084: "Opus 4.5 usage limits significantly reduced"
- GitHub Issue #16157: "Instantly hitting usage limits with Max subscription"

## 当前使用限制（Max20 套餐）

根据 Anthropic 官方文档，Max20 套餐的当前限制为：

### 基础限制
- **每5小时窗口**：约 220,000 tokens
- **消息数量**：至少 900 条消息/5小时（短对话，使用轻量模型）
- **重置周期**：每 5 小时重置一次

### 额外限制
- **每周限额**：2025年8月起增加（在5小时窗口基础上）
- **共享限制**：claude.ai、Claude Code、Claude Desktop **共用同一限额**

### 影响因素
实际可用的提示数量取决于：
1. **项目复杂度**：项目越复杂，每次对话消耗越多 tokens
2. **代码库大小**：大型代码库上下文消耗更多
3. **模型选择**：
   - Opus 4.5：消耗 tokens 最快
   - Sonnet 4.5：消耗较少
   - Haiku：消耗最少

## Anthropic 官方回应

根据官方声明和调查：

1. **节日加成到期**：承认节日加成到期导致用户感觉限制变严
2. **Token 效率调查**：正在调查某些版本 Claude Code 的 token 使用效率问题
3. **尚未找到 bug**：截至目前未找到确切的 bug，问题仍在持续
4. **不限制讨论**：Anthropic 表示不会尝试限制用户讨论使用限制问题

## 社区反应

### GitHub Issues（高热度）
- [Issue #17084](https://github.com/anthropics/claude-code/issues/17084) - Opus 4.5 限制显著降低
- [Issue #16157](https://github.com/anthropics/claude-code/issues/16157) - Max 订阅立即触发限制
- [Issue #16270](https://github.com/anthropics/claude-code/issues/16270) - 新年后限制 bug

### 媒体报道
- [The Register](https://www.theregister.com/2026/01/05/claude_devs_usage_limits/): "Claude devs complain about surprise usage limits"
- [Techzine Global](https://www.techzine.eu/news/devops/137675/claude-developers-concerned-about-usage-limits/): "Claude developers concerned about usage limits"

### 用户反馈摘要
- 过去几个月从未遇到限额，现在频繁触发
- Max 套餐用户感觉没有获得预期的高额度
- 一些用户报告限额在几小时内就耗尽

## 应对建议

### 1. 优化模型选择
```bash
# 不需要最强推理能力时，使用 Sonnet 4.5
claude --model sonnet

# 简单任务使用 Haiku
claude --model haiku
```

### 2. 管理上下文大小
- 避免加载整个大型代码库到上下文
- 使用 `.claudeignore` 排除不必要的文件
- 定期清理对话历史

### 3. 分散使用时间
- 利用 5 小时重置窗口
- 合理安排复杂任务的执行时间
- 避免在单个窗口内集中使用

### 4. 监控使用情况
```bash
# 检查当前使用情况
claude --usage

# 查看剩余限额
claude --limits
```

### 5. 跨产品使用策略
由于 claude.ai、Claude Code、Claude Desktop 共用限额：
- 简单对话使用 claude.ai
- 编码任务使用 Claude Code
- 避免同时在多个产品上高强度使用

## 历史背景

### 2025年8月
- 引入**每周限额**机制（在5小时窗口基础上）

### 2025年11月
- 发布 Opus 4.5 模型

### 2025年12月25日 - 12月31日
- **节日双倍限额**活动期

### 2026年1月1日
- 节日加成到期，恢复正常限额

### 2026年1月4日
- 用户开始大量反馈使用限制问题
- GitHub Issues 开始激增

### 2026年1月8日
- Opus 4.5 限制进一步收紧
- 成为自推出以来最严格的限制

## 参考资料

### 官方文档
- [About Claude's Max Plan Usage](https://support.claude.com/en/articles/11014257-about-claude-s-max-plan-usage)
- [Using Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
- [Understanding Usage and Length Limits](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits)
- [Extra Usage for Paid Claude Plans](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans)

### 新闻报道
- [The Register: Claude devs complain about surprise usage limits](https://www.theregister.com/2026/01/05/claude_devs_usage_limits/)
- [Techzine Global: Claude developers concerned about usage limits](https://www.techzine.eu/news/devops/137675/claude-developers-concerned-about-usage-limits/)
- [The Agency Journal: Claude AI Latest Updates January 2026](https://www.theagencyjournal.com/claude-ai-january-2026-updates-whats-new-and-what-you-need-to-know/)

### 技术分析
- [Claude Code Token Limits: A Guide for Engineering Leaders](https://www.faros.ai/blog/claude-code-token-limits)
- [Claude Code Rate Limits: Why Unlimited AI Plans are Dying in 2026](https://like2byte.com/claude-code-rate-limits-unlimited-ai-collapse/)
- [Northflank: Claude Code Rate limits, pricing, and alternatives](https://northflank.com/blog/claude-rate-limits-claude-code-pricing-cost)

### 社区讨论
- [GitHub Issue #17084](https://github.com/anthropics/claude-code/issues/17084)
- [GitHub Issue #16157](https://github.com/anthropics/claude-code/issues/16157)
- [GitHub Issue #16270](https://github.com/anthropics/claude-code/issues/16270)
- [GitHub Gist: claude max plan limits](https://gist.github.com/eonist/5ac2fd483cf91a6e6e5ef33cfbd1ee5e)

## 结论

2026年1月的使用限制变化是真实存在的，不是用户的错觉。主要原因包括：

1. **节日加成到期**（1月1日）- 从双倍限额恢复正常
2. **Opus 4.5 限制收紧**（1月8日）- 比以往任何时候都更严格
3. **Token 使用效率**可能存在问题（Anthropic 仍在调查）

对于 Max20 套餐用户，建议：
- 理解这是政策调整，而非个人账户问题
- 优化使用策略（模型选择、上下文管理）
- 关注官方后续更新和可能的调整
- 在 GitHub Issues 上参与讨论，帮助 Anthropic 了解用户需求

---

**文档维护信息**：
- 创建时间：2026-01-13
- 维护者：Claude Code 用户社区
- 更新频率：当 Anthropic 发布新的官方声明或政策变化时更新
