#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
银行卡交易明细文本解析脚本
输入: pdftotext -layout 导出的银行卡明细文本文件
输出: 标准化 JSON 文件（bank_card 类型）

支持格式：工商银行借记卡账户历史明细清单

用法:
    python3 parse_bank_card.py --input /tmp/bank_card.txt --output /tmp/bank_card_data.json
    python3 parse_bank_card.py --input /tmp/bank_card.txt --output /tmp/bank_card_data.json \\
        --card-name "借记卡2306" --card-number "xxx2306" \\
        --holder "李红霞" --branch "安阳内黄新区支行"
"""

import argparse
import json
import re
import sys


# ============================================================
# 常量：工商银行典型关键词
# ============================================================
EXPENSE_KEYWORDS = [
    'ATM取款', '消费', '转账', '还款', '付款', '支出', '汇出', '取款',
    '手续费', '跨行', '代扣', '扣款',
]
INCOME_KEYWORDS = [
    '存款', '收入', '汇入', '工资', '退款', '利息', '转入', '充值',
]


def classify_amount(amount_str, balance_before, balance_after, desc):
    """
    根据余额变化判断交易方向，返回带符号的金额（负=支出，正=收入）。
    若无法从余额判断，则根据关键词判断。
    """
    try:
        amount = float(amount_str.replace(',', ''))
    except (ValueError, AttributeError):
        return None

    # 优先通过余额变化判断
    if balance_before is not None and balance_after is not None:
        diff = balance_after - balance_before
        if abs(abs(diff) - amount) < 0.01:
            return diff  # 带符号：负=支出，正=收入

    # 关键词判断
    for kw in EXPENSE_KEYWORDS:
        if kw in desc:
            return -amount
    for kw in INCOME_KEYWORDS:
        if kw in desc:
            return amount

    # 默认视为支出（保守策略）
    return -amount


def parse_date(s):
    """将常见日期格式统一为 YYYY-MM-DD"""
    s = s.strip()
    # YYYY-MM-DD 或 YYYY/MM/DD 或 YYYYMMDD
    m = re.match(r'(\d{4})[-/](\d{2})[-/](\d{2})', s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.match(r'(\d{4})(\d{2})(\d{2})', s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return s


def parse_money(s):
    """将金额字符串转为 float，去除逗号"""
    try:
        return float(s.replace(',', '').strip())
    except (ValueError, AttributeError):
        return None


def parse_bank_card_layout(filepath):
    """
    解析 pdftotext -layout 导出的工商银行明细文本。
    返回 (transactions, page_totals_raw) 元组。

    工商银行明细典型行格式（空格对齐）：
      日期         金额        余额        类型/说明
      2023-01-15   800.00    12345.67    ATM取款 XXX
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    transactions = []
    page_totals_raw = []  # [(page_label, expense, income), ...]

    # 用于计算余额差的上一行余额
    prev_balance = None

    # 日期行模式：以 YYYY-MM-DD 或 YYYY/MM/DD 开头
    date_pattern = re.compile(
        r'^\s*(\d{4}[-/]\d{2}[-/]\d{2})'  # 日期
        r'\s+([\d,]+\.\d{2})'              # 金额（含逗号）
        r'\s+([\d,]+\.\d{2})'              # 余额
        r'\s+(.+?)\s*$'                    # 类型/说明
    )

    # 分页合计行模式（工行典型）：本页支出合计 / 本页收入合计
    page_expense_pattern = re.compile(r'本页.{0,4}支出.{0,4}[:：]?\s*([\d,]+\.\d{2})')
    page_income_pattern = re.compile(r'本页.{0,4}收入.{0,4}[:：]?\s*([\d,]+\.\d{2})')
    page_label_pattern = re.compile(r'第\s*(\d+)\s*页')

    current_page = 0

    for line_no, line in enumerate(lines):
        raw = line.rstrip('\n')

        # 检测页码，翻页时重置余额链（避免跨页余额差误判）
        plm = page_label_pattern.search(raw)
        if plm:
            current_page = int(plm.group(1))
            prev_balance = None

        # 检测分页合计行
        pem = page_expense_pattern.search(raw)
        pim = page_income_pattern.search(raw)
        if pem or pim:
            # 同一行可能同时含支出和收入（有些银行格式如此）
            exp_val = parse_money(pem.group(1)) if pem else None
            inc_val = parse_money(pim.group(1)) if pim else None
            page_label = f"第{current_page}页" if current_page else f"第{len(page_totals_raw)+1}页"
            page_totals_raw.append((page_label, exp_val, inc_val))
            continue

        # 解析交易行
        m = date_pattern.match(raw)
        if not m:
            # 尝试更宽松的匹配：日期 + 两个金额 + 文字
            loose = re.match(
                r'^\s*(\d{4}[-/]\d{2}[-/]\d{2})'
                r'\s+([\d,]+\.\d{2})'
                r'\s+([\d,]+\.\d{2})'
                r'(.*)',
                raw
            )
            if not loose:
                continue
            date_raw, amount_raw, balance_raw, desc_raw = (
                loose.group(1), loose.group(2), loose.group(3), loose.group(4).strip()
            )
        else:
            date_raw, amount_raw, balance_raw, desc_raw = (
                m.group(1), m.group(2), m.group(3), m.group(4)
            )

        balance_after = parse_money(balance_raw)
        signed_amount = classify_amount(amount_raw, prev_balance, balance_after, desc_raw)
        prev_balance = balance_after

        if signed_amount is None:
            continue

        # 提取交易类型（描述的前几个汉字）和说明
        tx_type = ''
        description = desc_raw.strip()
        type_match = re.match(r'^([\u4e00-\u9fa5A-Za-z]{2,12})\s*(.*)', description)
        if type_match:
            tx_type = type_match.group(1)
            description = type_match.group(2).strip()

        transactions.append({
            'date': parse_date(date_raw),
            'amount': round(signed_amount, 2),
            'type': tx_type,
            'description': description,
        })

    return transactions, page_totals_raw


def consolidate_page_totals(page_totals_raw):
    """
    将分页合计列表整合为 page_totals 结构。
    工行有时支出/收入分两行出现，需要按页合并。
    """
    if not page_totals_raw:
        return None

    # 按页标签合并
    merged = {}
    for label, exp, inc in page_totals_raw:
        if label not in merged:
            merged[label] = {'expense': 0.0, 'income': 0.0}
        if exp is not None:
            merged[label]['expense'] = exp
        if inc is not None:
            merged[label]['income'] = inc

    pages = [
        {'name': k, 'expense': v['expense'], 'income': v['income']}
        for k, v in merged.items()
    ]

    total_expense = sum(p['expense'] for p in pages)
    total_income = sum(p['income'] for p in pages)

    return {
        'expense': round(total_expense, 2),
        'income': round(total_income, 2),
        'pages': pages,
    }


def extract_metadata_from_text(filepath):
    """从文本头部提取持卡人、卡号、支行等元数据"""
    with open(filepath, 'r', encoding='utf-8') as f:
        header_lines = [f.readline() for _ in range(80)]
    header = ''.join(header_lines)

    holder = ''
    card_number = ''
    branch = ''

    # 持卡人
    name_match = re.search(r'(?:户名|持卡人|姓名)[：:\s]+([^\s\d]{2,8})', header)
    if name_match:
        holder = name_match.group(1)

    # 卡号（通常末4位可见，前面打*）
    card_match = re.search(r'(?:卡号|账号)[：:\s]+([*\d\s]{10,25})', header)
    if card_match:
        card_number = card_match.group(1).replace(' ', '').strip()

    # 支行
    branch_match = re.search(r'([\u4e00-\u9fa5]{2,10}(?:支行|分行|储蓄所))', header)
    if branch_match:
        branch = branch_match.group(1)

    return {'holder': holder, 'card_number': card_number, 'branch': branch}


def main():
    parser = argparse.ArgumentParser(
        description='解析银行卡交易明细文本(layout格式)，输出标准 bank_card JSON',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python3 parse_bank_card.py --input bank_card.txt --output bank_card_data.json
  python3 parse_bank_card.py --input bank_card.txt --output bank_card_data.json \\
      --card-name "借记卡2306" --card-number "xxx2306" \\
      --holder "李红霞" --branch "安阳内黄新区支行"
"""
    )
    parser.add_argument('--input', '-i', required=True, help='pdftotext -layout 输出的文本文件路径')
    parser.add_argument('--output', '-o', help='JSON 输出路径（默认: <input>.json）')
    parser.add_argument('--card-name', default='', help='卡片名称，如"借记卡2306"')
    parser.add_argument('--card-number', default='', help='卡号（后四位或完整），如"xxx2306"')
    parser.add_argument('--holder', default='', help='持卡人姓名')
    parser.add_argument('--branch', default='', help='开户支行名称')
    args = parser.parse_args()

    output_path = args.output or args.input.rsplit('.', 1)[0] + '.json'

    print(f"解析文件: {args.input}")

    # 尝试从文本中自动提取元数据
    auto_meta = extract_metadata_from_text(args.input)

    # 命令行参数优先，其次自动提取
    holder = args.holder or auto_meta['holder']
    card_number = args.card_number or auto_meta['card_number']
    branch = args.branch or auto_meta['branch']
    suffix = card_number[-4:] if len(card_number) >= 4 else card_number
    card_name = args.card_name or (f"借记卡{suffix}" if card_number else '银行卡')

    transactions, page_totals_raw = parse_bank_card_layout(args.input)
    page_totals = consolidate_page_totals(page_totals_raw)

    # 推断时间段
    period_start = ''
    period_end = ''
    if transactions:
        dates = sorted(t['date'] for t in transactions)
        period_start = dates[0]
        period_end = dates[-1]

    result = {
        'type': 'bank_card',
        'source': '银行卡账户历史明细清单',
        'card_name': card_name,
        'card_number': card_number,
        'holder': holder,
        'branch': branch,
        'period': {
            'start': period_start,
            'end': period_end,
        },
        'transactions': transactions,
        'page_totals': page_totals,
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # 统计信息
    expense_txs = [t for t in transactions if t['amount'] < 0]
    income_txs = [t for t in transactions if t['amount'] > 0]
    expense_total = sum(abs(t['amount']) for t in expense_txs)
    income_total = sum(t['amount'] for t in income_txs)

    print(f"解析完成: {len(transactions)} 笔交易")
    print(f"  逐笔-支出: {len(expense_txs)} 笔, {expense_total:,.2f} 元")
    print(f"  逐笔-收入: {len(income_txs)} 笔, {income_total:,.2f} 元")
    if page_totals:
        print(f"  银行清单-支出合计: {page_totals['expense']:,.2f} 元")
        print(f"  银行清单-收入合计: {page_totals['income']:,.2f} 元")
        print(f"  分页数量: {len(page_totals['pages'])} 页")
    else:
        print("  未检测到分页合计行（可手工在 JSON 中补充 page_totals 字段）")
    print(f"输出: {output_path}")

    if not transactions:
        print("\n[警告] 未解析到任何交易记录。")
        print("  可能原因:")
        print("  1. PDF 格式与工商银行明细格式不匹配")
        print("  2. pdftotext 未使用 -layout 参数")
        print("  3. PDF 为扫描件（无法提取文本）")
        print("  建议: 手工参考 references/bank_card_template.json 填写数据")
        sys.exit(1)


if __name__ == '__main__':
    main()
