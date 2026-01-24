# 数据分析 Skills

专注于数据处理、分析和可视化的 Skills，涵盖 CSV、数据库、图表等。

## 🌟 精选推荐

| Skill | 功能 | 维护者 | 链接 |
|-------|------|--------|------|
| **CSV Data Summarizer** | 自动分析 CSV 并生成可视化 | @coffeefuelbump | [GitHub](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) |
| **D3.js Visualization** | D3 图表和交互式可视化 | @chrisvoncsefalvay | [GitHub](https://github.com/chrisvoncsefalvay/claude-d3js-skill) |
| **postgres** | PostgreSQL 安全只读查询 | @sanjay3290 | [GitHub](https://github.com/sanjay3290/ai-skills/tree/main/skills/postgres) |

---

## 📦 完整列表

### CSV 处理

**CSV Data Summarizer**
- **功能**: 自动分析 CSV 文件，无需用户提示即可生成综合洞察和可视化
- **特点**:
  - 自动数据分析
  - 智能可视化
  - 统计摘要
  - 趋势识别

**安装**:
```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill csv-summarizer
```

**使用示例**:
```
用户: "分析这个销售数据 CSV"
[上传 sales.csv]

Claude: [使用 csv-summarizer skill]
📊 数据摘要：
- 记录数：1,234 行
- 时间范围：2024-01 到 2024-12
- 总销售额：$1,234,567

📈 趋势分析：
- 销售额持续增长（+15%/月）
- 最佳月份：12月（$150,000）
- 主要产品：产品 A（45% 占比）

[生成可视化图表]
```

### 数据库工具

**postgres**
- **功能**: 对 PostgreSQL 数据库执行安全的只读 SQL 查询
- **特点**:
  - 多连接支持
  - 深度防御安全
  - 只读权限
  - 查询优化

**安装**:
```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/sanjay3290/ai-skills
cp -r ai-skills/skills/postgres ./
rm -rf ai-skills
```

**使用示例**:
```
用户: "查询用户表中活跃用户数"

Claude: [使用 postgres skill]
SELECT COUNT(*) FROM users WHERE status = 'active';

结果：1,234 个活跃用户
```

### 可视化工具

**D3.js Visualization**
- **功能**: 使用 D3.js 生成图表和交互式数据可视化
- **特点**:
  - 多种图表类型
  - 交互式设计
  - 响应式布局
  - 自定义样式

**安装**:
```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/chrisvoncsefalvay/claude-d3js-skill d3-viz
```

**使用示例**:
```
用户: "创建一个销售趋势的折线图"

Claude: [使用 d3-viz skill]
[生成 D3.js 代码]
- 折线图
- 交互式提示
- 时间轴缩放
- 数据筛选器
```

### 问题诊断

**root-cause-tracing**
- **功能**: 错误深度追溯，找到原始触发点
- **仓库**: [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/root-cause-tracing)

**安装**:
```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/obra/superpowers
# root-cause-tracing 在 superpowers/skills/ 目录下
```

---

## 💡 使用场景

### 场景 1：CSV 数据快速分析

```
任务：分析电商平台的订单数据

步骤：
1. 上传 orders.csv
2. 使用 csv-summarizer 自动分析
3. 查看生成的统计和可视化
4. 导出分析报告
```

### 场景 2：数据库查询和分析

```
任务：分析用户行为数据

步骤：
1. 使用 postgres skill 连接数据库
2. 查询用户活跃度数据
3. 使用 d3-viz 生成可视化
4. 识别趋势和模式
```

### 场景 3：错误根因分析

```
任务：诊断生产环境错误

步骤：
1. 收集错误日志
2. 使用 root-cause-tracing 追溯
3. 识别原始触发点
4. 提出修复方案
```

---

## 🔧 最佳实践

### 1. 数据准备

```
CSV 数据质量检查：
□ 编码格式正确（UTF-8）
□ 列名清晰明确
□ 数据类型一致
□ 无缺失关键字段
```

### 2. 查询优化

```
PostgreSQL 查询技巧：
- 使用索引字段查询
- 限制返回行数
- 避免 SELECT *
- 使用 EXPLAIN 分析
```

### 3. 可视化选择

```
图表类型选择：
- 趋势数据：折线图
- 分类对比：柱状图
- 占比分析：饼图
- 关系分析：散点图
```

---

## 📖 参考资料

### Skills 仓库

- [CSV Data Summarizer](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill)
- [D3.js Visualization](https://github.com/chrisvoncsefalvay/claude-d3js-skill)
- [postgres](https://github.com/sanjay3290/ai-skills/tree/main/skills/postgres)
- [root-cause-tracing](https://github.com/obra/superpowers/tree/main/skills/root-cause-tracing)

### 工具文档

- [D3.js 官方文档](https://d3js.org/)
- [PostgreSQL 文档](https://www.postgresql.org/docs/)
- [Pandas 数据分析](https://pandas.pydata.org/)

---

**返回**: [社区导航](README.md) | [主页](../README.md)
