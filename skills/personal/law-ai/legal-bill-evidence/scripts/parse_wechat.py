#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信支付交易明细文本解析脚本
输入: pdftotext -layout 导出的文本文件
输出: 标准化 JSON 文件

用法:
    python3 parse_wechat.py --input /tmp/wechat_layout.txt --output /tmp/wechat_data.json
"""

import argparse
import json
import re
import sys


def parse_wechat_layout(filepath):
    """解析 layout 模式的微信支付文本，返回交易记录列表"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    transactions = []

    # 匹配交易行: 交易单号(20+位数字) + 日期(YYYY-MM-DD) + 后续内容
    tx_pattern = re.compile(
        r'^(\d{20,})'           # 交易单号
        r'(\d{4}-\d{2}-\d{2})'  # 日期
        r'\s+'
        r'(.+?)'               # 后续内容(类型+收支+支付方式+金额+对方)
        r'\s*$'
    )

    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')

        m = tx_pattern.match(line)
        if not m:
            i += 1
            continue

        date = m.group(2)
        rest = m.group(3)

        # 使用多空格分隔字段
        parts = re.split(r'\s{2,}', rest.strip())

        tx_type = ''
        direction = ''
        payment = ''
        amount = 0.0
        counterparty = ''

        # 解析各字段
        for j, p in enumerate(parts):
            p = p.strip()
            if p in ('支出', '收入', '其他'):
                tx_type = parts[j - 1].strip() if j > 0 else ''
                direction = p
                if j + 1 < len(parts):
                    next_p = parts[j + 1].strip()
                    if next_p in ('零钱', '/') or '银行' in next_p or '蓄卡' in next_p:
                        payment = next_p
                        if j + 2 < len(parts):
                            try:
                                amount = float(parts[j + 2].strip())
                                if j + 3 < len(parts):
                                    counterparty = parts[j + 3].strip()
                            except ValueError:
                                pass
                    else:
                        try:
                            amount = float(next_p)
                            if j + 2 < len(parts):
                                counterparty = parts[j + 2].strip()
                        except ValueError:
                            pass
                break

        # 回退: 从整行找金额
        if amount == 0.0:
            amounts_found = re.findall(r'\b(\d+\.\d{2})\b', rest)
            for af in amounts_found:
                val = float(af)
                if 0.01 <= val < 1000000:
                    amount = val
                    break

        # 回退: 从整行找方向
        if not direction:
            if '支出' in rest:
                direction = '支出'
            elif '收入' in rest:
                direction = '收入'
            elif '其他' in rest:
                direction = '其他'

        # 回退: 从整行找交易类型
        if not tx_type:
            if '商户消费' in rest:
                tx_type = '商户消费'
            elif '转账' in rest:
                tx_type = '转账'
            elif '扫二维码' in rest:
                tx_type = '扫二维码付款'
            elif '红包' in rest:
                tx_type = '微信红包'
            elif '退款' in rest:
                tx_type = '退款'
            elif '提现' in rest:
                tx_type = '零钱提现'

        # 回退: 从整行找支付方式
        if not payment:
            if '零钱' in rest and '提现' not in rest:
                payment = '零钱'
            elif '/' in rest:
                payment = '/'
            # 银行卡号匹配(通用)
            card_match = re.search(r'储蓄卡\((\d{4})\)', rest)
            if card_match:
                payment = f'工商银行储蓄卡({card_match.group(1)})'
            elif not payment:
                for suffix in re.findall(r'(\d{4})', rest):
                    if len(suffix) == 4 and suffix not in date:
                        nearby = rest[rest.find(suffix) - 10:rest.find(suffix) + 5] if rest.find(suffix) >= 10 else rest[:rest.find(suffix) + 5]
                        if '银行' in nearby or '蓄卡' in nearby:
                            payment = f'工商银行储蓄卡({suffix})'
                            break

        # 获取时间(在下一行)
        time_str = ''
        if i + 1 < len(lines):
            next_line = lines[i + 1].rstrip('\n')
            time_match = re.search(r'(\d{2}:\d{2}:\d{2})', next_line)
            if time_match:
                time_str = time_match.group(1)

        # 清理交易对方 - 去除商户单号(长数字/字母串)
        if counterparty:
            counterparty = re.sub(r'\s*\d{15,}.*$', '', counterparty).strip()
            counterparty = re.sub(r'\s*[A-Za-z0-9_\-]{15,}.*$', '', counterparty).strip()
            counterparty = counterparty.rstrip('，,')

        # 修复截断的交易类型
        type_fixes = {
            '扫二维码付': '扫二维码付款',
            '微信红包-退': '微信红包-退款',
            '京东商城平': '京东商城平台商户-退款',
            '深圳市汇顺': '退款',
        }
        if tx_type in type_fixes:
            tx_type = type_fixes[tx_type]

        # 修复截断的支付方式 - 检查当前行和后续3行
        if payment in ('工商银行储', '工商银行储蓄卡') or (not payment and '工商银行储' in line):
            nearby_text = line
            for offset in range(1, 4):
                if i + offset < len(lines):
                    nearby_text += ' ' + lines[i + offset]
            card_match = re.search(r'(\d{4})\)', nearby_text)
            if card_match:
                payment = f'工商银行储蓄卡({card_match.group(1)})'
            else:
                payment = '工商银行储蓄卡'

        if direction and amount > 0:
            transactions.append({
                'date': date,
                'time': time_str,
                'type': tx_type,
                'direction': direction,
                'payment': payment,
                'amount': amount,
                'counterparty': counterparty,
            })

        i += 1

    return transactions


def extract_metadata(filepath):
    """从文本头部提取账户和时间段信息"""
    with open(filepath, 'r', encoding='utf-8') as f:
        header_lines = [f.readline() for _ in range(50)]
    header_text = ''.join(header_lines)

    # 提取微信号
    account = ''
    acc_match = re.search(r'微信号[：:]\s*(\S+)', header_text)
    if acc_match:
        account = acc_match.group(1)

    # 提取姓名
    holder = ''
    name_match = re.search(r'姓名[：:]\s*(\S+)', header_text)
    if name_match:
        holder = name_match.group(1)

    # 提取时间段
    period_start = ''
    period_end = ''
    period_match = re.search(r'(\d{4}-\d{2}-\d{2})\s*[至到~-]\s*(\d{4}-\d{2}-\d{2})', header_text)
    if period_match:
        period_start = period_match.group(1)
        period_end = period_match.group(2)

    return {
        'account': account,
        'holder': holder,
        'period_start': period_start,
        'period_end': period_end,
    }


def main():
    parser = argparse.ArgumentParser(description='解析微信支付交易明细(layout格式)，输出标准JSON')
    parser.add_argument('--input', '-i', required=True, help='pdftotext -layout 输出的文本文件路径')
    parser.add_argument('--output', '-o', help='JSON 输出路径(默认: <input>.json)')
    args = parser.parse_args()

    output_path = args.output or args.input.rsplit('.', 1)[0] + '.json'

    print(f"解析文件: {args.input}")
    transactions = parse_wechat_layout(args.input)
    metadata = extract_metadata(args.input)

    # 如果头部没提取到时间段，从交易数据推断
    if not metadata['period_start'] and transactions:
        dates = sorted(t['date'] for t in transactions)
        metadata['period_start'] = dates[0]
        metadata['period_end'] = dates[-1]

    result = {
        'source': '微信支付交易明细证明',
        'type': 'wechat',
        'holder': metadata['holder'],
        'account': metadata['account'],
        'period': {
            'start': metadata['period_start'],
            'end': metadata['period_end'],
        },
        'transactions': transactions,
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # 统计信息
    expense_txs = [t for t in transactions if t['direction'] == '支出']
    income_txs = [t for t in transactions if t['direction'] == '收入']
    other_txs = [t for t in transactions if t['direction'] == '其他']
    expense_total = sum(t['amount'] for t in expense_txs)
    income_total = sum(t['amount'] for t in income_txs)

    print(f"解析完成: {len(transactions)} 笔交易")
    print(f"  支出: {len(expense_txs)} 笔, {expense_total:,.2f} 元")
    print(f"  收入: {len(income_txs)} 笔, {income_total:,.2f} 元")
    print(f"  其他: {len(other_txs)} 笔")
    print(f"输出: {output_path}")


if __name__ == '__main__':
    main()
