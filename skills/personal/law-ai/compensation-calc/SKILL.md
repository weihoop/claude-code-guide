---
name: compensation-calc
author: zy
description: 劳动/工伤/交通/离婚赔偿计算器，自动生成分项明细 Excel，含法律依据
---

# compensation-calc — 赔偿计算器

## 触发词
赔偿计算、工伤赔偿、经济补偿金、劳动赔偿、交通赔偿、离婚财产分割

## 功能说明
根据案件类型自动计算各项赔偿/补偿金额，生成 Excel 表格（Sheet1 分项明细+法律依据，Sheet2 汇总合计）。

## 使用方式

### 劳动争议经济补偿金
```bash
python3 ~/.claude/skills/compensation-calc/scripts/calc_compensation.py \
  --type labor \
  --monthly-salary 8000 \
  --years 3.5 \
  --reason illegal \
  --output 劳动赔偿.xlsx
```

### 工伤赔偿
```bash
python3 ~/.claude/skills/compensation-calc/scripts/calc_compensation.py \
  --type injury \
  --monthly-salary 6000 \
  --years 5 \
  --disability-level 8 \
  --output 工伤赔偿.xlsx
```

### 交通事故赔偿
```bash
python3 ~/.claude/skills/compensation-calc/scripts/calc_compensation.py \
  --type traffic \
  --urban \
  --disability-level 10 \
  --lost-work-days 30 \
  --nursing-days 15 \
  --hospital-days 10 \
  --medical-fee 25000 \
  --output 交通赔偿.xlsx
```

### 离婚财产分割
```bash
python3 ~/.claude/skills/compensation-calc/scripts/calc_compensation.py \
  --type divorce \
  --assets-json ~/.claude/skills/compensation-calc/references/标准参数.json \
  --output 财产分割.xlsx
```

## 参数说明

| 参数 | 说明 |
|------|------|
| `--type` | 计算类型：labor/injury/traffic/divorce |
| `--monthly-salary` | 月工资（元） |
| `--years` | 工龄（年，支持小数） |
| `--reason` | 解除原因：illegal（违法）/ legal（合法）/ mutual（协商） |
| `--disability-level` | 伤残等级（1-10级） |
| `--urban` | 城镇标准（不加则用农村标准） |
| `--lost-work-days` | 误工天数 |
| `--nursing-days` | 护理天数 |
| `--hospital-days` | 住院天数 |
| `--medical-fee` | 医疗费用（元） |
| `--assets-json` | 共同财产清单 JSON 文件路径 |
| `--output` | 输出 Excel 文件路径 |

## 参考文件
- `references/标准参数.json`：当年标准参数（全国/各省平均工资，需用户每年更新）

## 法律依据
- 劳动合同法第 46、47 条（经济补偿金）
- 工伤保险条例第 35-37 条（工伤赔偿）
- 《最高人民法院关于审理人身损害赔偿案件适用法律若干问题的解释》（2022年修正版，法释〔2022〕14号；原2020年第二次修正版，非2003年旧版）（交通事故）
- 婚姻家庭编司法解释（离婚财产）
