# 美国信用卡账单整理 Skill

一个专门用于整理企业信用卡账单的自动化工具，适用于月度账单整理、费用报销和财务对账。

## 简介

这是一个**个人Skill**，用于自动化处理企业信用卡账单：
- 从账单图片中自动识别表格数据
- 生成规范的Excel汇总表
- 支持PDF文件归类和信息提取（可选功能）

## 核心功能

### ✅ 已实现功能

**Step 1: 图片数据提取**
- 自动识别账单列表图片的表格内容
- 支持多张图片合并到一个Excel
- 自动数据验证和清理
- 生成包含3个工作表的Excel文件
  - 账单汇总：所有账单数据
  - 识别日志：处理日志
  - 使用说明：字段说明和使用指南

### 🚧 设计完成（待启用）

**Step 2: PDF文件归类**
- 智能匹配PDF账单文件
- 标准化文件命名
- 自动归类整理

**Step 3: PDF信息提取**
- 提取发票详细内容
- 补充Excel汇总信息
- 生成完整报表

## 技术架构

### 技术栈
- **Python 3.8+**
- **openpyxl**: Excel文件操作
- **pandas**: 数据处理和合并
- **Claude Code Read工具**: 图片内容识别

### 目录结构
```
~/.claude/skills/us-credit-bill/
├── SKILL.md                    # Skill主文件（Claude指令）
├── README.md                   # 使用文档
├── SPEC.md                     # 功能规格说明
├── CHANGELOG.md                # 版本历史
├── requirements.txt            # Python依赖
├── scripts/                    # 脚本目录
│   ├── step1_extract_images.py    # 图片数据提取
│   ├── utils.py                   # 工具函数
│   └── (step2、step3待实现)
├── assets/                     # 资源目录
└── references/                 # 参考文档
```

## 安装方法

### 1. 安装Skill到本地

```bash
# Skill已安装到
~/.claude/skills/us-credit-bill/
```

### 2. 安装Python依赖

```bash
pip3 install -r ~/.claude/skills/us-credit-bill/requirements.txt
```

依赖项：
- openpyxl>=3.1.2
- pandas>=2.0.0
- Pillow>=10.0.0

## 使用场景

### 场景1: 月度账单整理

**需求**：每月收到信用卡账单图片，需要整理成Excel用于报销

**步骤**：
1. 将账单图片放在命名为`美国信用卡账单-YYYYMM`的目录
2. 使用Claude识别图片内容
3. 自动生成`账单汇总_YYYYMM.xlsx`
4. 提交给财务部门

**优势**：从2小时手工录入降至10分钟

### 场景2: 费用对账

**需求**：核对信用卡账单和实际支出

**步骤**：
1. 生成账单汇总Excel
2. 与财务系统导出数据对比
3. 在备注列标记差异

### 场景3: 财务审计

**需求**：提供完整的账单记录和PDF凭证

**步骤**：
1. Step 1: 生成账单汇总
2. Step 2: 归类PDF文件
3. Step 3: 提取PDF详细信息

## 快速开始

### 基础用法

```bash
# 1. 准备账单图片（jpg/png格式）放在目录中
# 2. 在Claude Code中执行

# Claude会自动：
# - 识别图片内容
# - 生成JSON数据
# - 运行脚本生成Excel
```

### 命令行用法

```bash
# 查看帮助
python3 ~/.claude/skills/us-credit-bill/scripts/step1_extract_images.py --help

# 基础用法
python3 ~/.claude/skills/us-credit-bill/scripts/step1_extract_images.py \
  --image-dir <图片目录> \
  --data extracted_data.json

# 调试模式
python3 ~/.claude/skills/us-credit-bill/scripts/step1_extract_images.py \
  --image-dir <图片目录> \
  --data extracted_data.json \
  --debug
```

## 数据格式

### 输入格式

**图片要求**：
- 格式：.jpg、.jpeg、.png
- 内容：清晰可读的表格
- 字段：Item#、Type、Date、Description、Amount

### 输出格式

**Excel结构**（示例数据）：

| Item# | Type  | Date       | Description                | Amount   | 备注 |
|-------|-------|------------|----------------------------|----------|------|
| 1     | DEBIT | 01/15/2025 | Software License Co.       | $99.00   |      |
| 2     | DEBIT | 01/10/2025 | Cloud Services Provider    | $150.00  |      |
| 3     | DEBIT | 01/05/2025 | Online Service Monthly Fee | $29.99   |      |

**注**: 以上为虚构示例数据，仅用于说明格式。

## 特性亮点

### 智能化处理
- 自动识别表格数据
- 自动数据验证和清理
- 自动去重和排序
- 智能文件命名

### 规范化输出
- 标准的Excel格式
- 清晰的字段说明
- 完整的处理日志
- 详细的使用指南

### 可扩展性
- 模块化设计
- 独立的步骤脚本
- 可选功能随时启用
- 易于维护和扩展

## 性能指标

- **图片识别**: <30秒/张（取决于Claude API）
- **Excel生成**: <5秒
- **支持图片**: 1-20张
- **支持数据**: <500行

## 隐私说明

### 数据处理方式
- ✅ 所有数据本地处理
- ✅ 仅通过Claude API识别图片
- ✅ 不上传到其他服务器
- ✅ 建议定期清理临时文件

### Skill代码安全
- ✅ 不包含任何实际账单数据
- ✅ 示例数据均为虚构
- ✅ 仅用于个人账单整理场景
- ✅ 完全开源，可审查

## 常见问题

### Q: 这是公开的Skill吗？
**A**: 是的，这是一个个人Skill，代码完全公开，不包含任何敏感数据。仅用于账单整理场景。

### Q: 支持哪些账单格式？
**A**: 支持包含表格结构的账单图片，需要包含Item#、Type、Date、Description、Amount等字段。

### Q: 如何保证数据安全？
**A**:
- 所有数据在本地处理
- 仅通过Claude API进行图片识别
- 不上传到任何第三方服务
- 建议处理完成后删除临时文件

### Q: PDF功能什么时候可用？
**A**: Step 2和Step 3已完成设计，当用户下载PDF文件后即可启用。当前优先完成图片识别功能。

## 技术支持

### 查看日志
识别日志记录在Excel的"识别日志"工作表中

### 调试模式
```bash
python3 step1_extract_images.py --image-dir <目录> --debug
```

### 测试工具
```bash
python3 utils.py
```

## 相关文档

- [SKILL.md](~/.claude/skills/us-credit-bill/SKILL.md) - Claude使用指令
- [README.md](~/.claude/skills/us-credit-bill/README.md) - 详细使用文档
- [SPEC.md](~/.claude/skills/us-credit-bill/SPEC.md) - 功能规格说明

## 版本信息

- **当前版本**: v1.0.0
- **发布日期**: 2026-01-24
- **状态**: Step 1可用，Step 2/3设计完成

## 更新日志

### v1.0.0 (2026-01-24)
- 🎉 初始版本发布
- ✨ Step 1: 图片数据提取功能
- 📝 完整的文档和规格说明
- 🔧 工具函数和错误处理

详细更新日志见 [CHANGELOG.md](~/.claude/skills/us-credit-bill/CHANGELOG.md)

## 贡献

这是一个个人工具项目，欢迎提出改进建议。

## 许可证

个人使用工具，代码公开，不包含任何敏感数据。

---

**最后更新**: 2026-01-24
**维护者**: Claude Code 协助创建
**仓库**: claude-code-guide/skills/personal
