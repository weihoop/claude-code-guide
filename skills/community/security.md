# 安全系统 Skills

专注于安全分析、取证调查和威胁检测的 Skills。

## 🌟 精选推荐

| Skill | 功能 | 仓库链接 |
|-------|------|---------|
| **computer-forensics** | 数字取证分析和调查技术 | [GitHub](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/computer-forensics) |
| **threat-hunting-with-sigma-rules** | 使用 Sigma 规则进行威胁狩猎 | [GitHub](https://github.com/jthack/threat-hunting-with-sigma-rules-skill) |
| **metadata-extraction** | 提取和分析文件元数据 | [GitHub](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/metadata-extraction) |
| **file-deletion** | 安全文件删除和数据清理 | [GitHub](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/file-deletion) |

---

## 📦 完整列表

### 数字取证

**computer-forensics**
- **功能**: 数字取证分析和调查技术
- **用途**:
  - 证据收集
  - 数据恢复
  - 事件分析
  - 法庭支持

**file-deletion**
- **功能**: 安全文件删除和数据清理方法
- **特点**:
  - 多次覆写
  - 验证删除
  - 符合标准
- **用途**: 敏感数据销毁

**metadata-extraction**
- **功能**: 提取和分析文件元数据用于取证目的
- **信息**: 创建时间、修改时间、作者、GPS 位置等

### 威胁检测

**threat-hunting-with-sigma-rules**
- **功能**: 使用 Sigma 检测规则进行威胁狩猎和分析安全事件
- **特点**:
  - 标准化规则
  - 跨平台检测
  - 威胁情报集成
- **维护者**: @jthack

### Web 安全

**FFUF Web Fuzzing**
- **功能**: 集成 ffuf web fuzzer 进行模糊测试
- **用途**:
  - 发现漏洞
  - 目录枚举
  - 参数测试
- **仓库**: [jthack/ffuf_claude_skill](https://github.com/jthack/ffuf_claude_skill)

---

## 💡 使用场景

### 场景 1：安全事件响应

```
任务：调查可疑的安全事件

步骤：
1. 使用 computer-forensics 收集证据
2. 使用 metadata-extraction 分析文件
3. 使用 threat-hunting-with-sigma-rules 检测威胁
4. 编写调查报告
5. 提出修复建议
```

### 场景 2：数据清理

```
任务：安全删除敏感文件

步骤：
1. 识别需要删除的文件
2. 使用 metadata-extraction 记录信息
3. 使用 file-deletion 安全删除
4. 验证删除完整性
5. 记录删除日志
```

### 场景 3：威胁狩猎

```
任务：主动搜索潜在威胁

步骤：
1. 定义 Sigma 检测规则
2. 使用 threat-hunting-with-sigma-rules
3. 分析日志和事件
4. 识别异常模式
5. 调查可疑活动
```

### 场景 4：Web 应用安全测试

```
任务：测试 Web 应用安全性

步骤：
1. 使用 FFUF 进行目录枚举
2. 测试常见漏洞
3. 分析响应模式
4. 识别安全问题
5. 生成测试报告
```

---

## 🔧 最佳实践

### 1. 取证调查原则

```
证据处理规范：
□ 保持证据完整性
□ 记录操作链
□ 使用写保护设备
□ 创建镜像副本
□ 详细记录过程
```

### 2. 数据清理标准

```
删除级别：
- Level 1：简单删除（回收站）
- Level 2：覆写一次
- Level 3：多次覆写（3-7 次）
- Level 4：物理销毁（高敏感数据）
```

### 3. Sigma 规则编写

```yaml
title: 可疑的 PowerShell 下载
status: experimental
description: 检测通过 PowerShell 下载文件的行为
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    CommandLine|contains:
      - 'Invoke-WebRequest'
      - 'wget'
      - 'curl'
  condition: selection
fields:
  - CommandLine
  - User
falsepositives:
  - 合法的软件更新
level: medium
```

### 4. Web 模糊测试

```bash
# FFUF 基本用法
ffuf -w wordlist.txt -u https://example.com/FUZZ

# 目录枚举
ffuf -w dirs.txt -u https://example.com/FUZZ -mc 200,301,302

# 参数测试
ffuf -w params.txt -u https://example.com/api?FUZZ=test
```

---

## ⚠️ 重要提示

### 合法性和授权

- ⚠️ 仅在授权的环境中使用
- ⚠️ 遵守法律法规
- ⚠️ 获得书面许可
- ⚠️ 记录所有操作

### 伦理准则

- ✅ 保护用户隐私
- ✅ 负责任的披露
- ✅ 尊重数据所有权
- ✅ 遵守行业标准

---

## 📖 参考资料

### Skills 仓库

- [computer-forensics](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/computer-forensics)
- [file-deletion](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/file-deletion)
- [metadata-extraction](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/metadata-extraction)
- [threat-hunting-with-sigma-rules](https://github.com/jthack/threat-hunting-with-sigma-rules-skill)
- [FFUF Web Fuzzing](https://github.com/jthack/ffuf_claude_skill)

### 安全资源

- [Sigma Rules](https://github.com/SigmaHQ/sigma)
- [NIST 取证指南](https://www.nist.gov/digital-forensics)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [FFUF 文档](https://github.com/ffuf/ffuf)

### 认证和培训

- [SANS Digital Forensics](https://www.sans.org/cyber-security-courses/advanced-incident-response-threat-hunting-training/)
- [CEH (Certified Ethical Hacker)](https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/)
- [OSCP (Offensive Security)](https://www.offensive-security.com/pwk-oscp/)

---

**返回**: [社区导航](README.md) | [主页](../README.md)
