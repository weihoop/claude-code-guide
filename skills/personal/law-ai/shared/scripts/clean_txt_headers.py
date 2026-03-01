#!/usr/bin/env python3
"""
批量清理案例全文txt文件头部残留的目录行和分类标题行。

问题描述：
  约30%的txt文件在元数据头（案例ID/标题/来源/分隔线）之后、
  【案件基本信息】之前，混入了PDF目录中的分类标题行，如：
  - "一、婚姻家庭纠纷"
  - "一、确认劳动关系 3"
  - "(一)离婚纠纷"

用法：
  # 预览模式（只统计，不修改）
  python3 clean_txt_headers.py --dry-run

  # 实际清理
  python3 clean_txt_headers.py

  # 指定目录
  python3 clean_txt_headers.py --dir ~/.claude/skills/shared/references/案例全文
"""

import argparse
import os
import re
import sys


def is_noise_line(stripped):
    """判断一行是否为头部残留的噪声行"""
    if not stripped:
        return False

    # 分类标题行（"一、XX纠纷"或含页码"一、XX纠纷 3"）
    if re.match(r'^[一二三四五六七八九十]+[、．.]\s*\S+', stripped):
        inner = re.sub(r'^[一二三四五六七八九十]+[、．.]\s*', '', stripped)
        inner = re.sub(r'\s+\d+$', '', inner)
        if len(inner) <= 20:
            return True

    # 子分类标题行：(一)XX、（二）XX
    if re.match(r'^[（(][一二三四五六七八九十]+[）)]\s*\S+', stripped):
        inner = re.sub(r'^[（(][一二三四五六七八九十]+[）)]\s*', '', stripped)
        if len(inner) <= 20:
            return True

    # 页眉残留行
    if re.search(r'中国法院\d{4}年度案例', stripped):
        return True

    # 目录行（含省略号）
    if re.search(r'[·.…]{3,}\s*\d+', stripped):
        return True

    return False


def clean_file(filepath, dry_run=False):
    """
    清理单个txt文件头部残留行。

    txt文件格式：
      第1行: 案例ID: YYYY-VV-NNN
      第2行: 标题: XXX
      第3行: 来源: XXX 第X-Y页
      第4行: ============...
      第5行: (空行)
      第6行起: 案例正文（可能有残留行）
      ...
      【案件基本信息】

    返回: (是否有修改, 删除行数, 删除的行内容列表)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 定位分隔线（====）
    separator_match = re.search(r'^={10,}$', content, re.MULTILINE)
    if not separator_match:
        return False, 0, []

    # 定位【案件基本信息】
    info_pos = content.find('【案件基本信息】')
    if info_pos < 0:
        return False, 0, []

    # 提取头部区域（分隔线之后到【案件基本信息】之前）
    header_start = separator_match.end()
    header = content[header_start:info_pos]
    lines = header.split('\n')

    # 清理残留行
    cleaned = []
    removed = []
    for line in lines:
        stripped = line.strip()
        if is_noise_line(stripped):
            removed.append(stripped)
        else:
            cleaned.append(line)

    if not removed:
        return False, 0, []

    # 去掉头部连续空行（保留最多1个空行作为分隔）
    while len(cleaned) > 1 and not cleaned[0].strip() and not cleaned[1].strip():
        cleaned.pop(0)

    # 重组文件内容
    new_content = content[:header_start] + '\n'.join(cleaned) + content[info_pos:]

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return True, len(removed), removed


def main():
    parser = argparse.ArgumentParser(description='批量清理案例txt文件头部残留行')
    parser.add_argument('--dir',
                        default=os.path.expanduser('~/.claude/skills/shared/references/案例全文'),
                        help='案例全文根目录')
    parser.add_argument('--dry-run', action='store_true',
                        help='预览模式，只统计不修改')
    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        print(f"错误: 目录不存在: {args.dir}")
        sys.exit(1)

    mode = "预览模式" if args.dry_run else "清理模式"
    print(f"{'='*60}")
    print(f"案例全文头部残留清理工具 ({mode})")
    print(f"目录: {args.dir}")
    print(f"{'='*60}\n")

    total_files = 0
    modified_files = 0
    total_removed = 0
    stats_by_year = {}

    for root, dirs, files in os.walk(args.dir):
        dirs.sort()
        for filename in sorted(files):
            if not filename.endswith('.txt'):
                continue
            filepath = os.path.join(root, filename)
            total_files += 1

            changed, removed_count, removed_lines = clean_file(filepath, dry_run=args.dry_run)
            if changed:
                modified_files += 1
                total_removed += removed_count
                rel_path = os.path.relpath(filepath, args.dir)
                # 统计年份
                year = rel_path.split(os.sep)[0] if os.sep in rel_path else "unknown"
                stats_by_year[year] = stats_by_year.get(year, 0) + 1

                if args.dry_run:
                    print(f"  待清理: {rel_path}")
                    for line in removed_lines:
                        print(f"    - {line}")
                else:
                    print(f"  已清理: {rel_path} (删除{removed_count}行)")

    print(f"\n{'='*60}")
    print(f"统计:")
    print(f"  扫描文件: {total_files}")
    print(f"  {'待修改' if args.dry_run else '已修改'}: {modified_files}")
    print(f"  删除总行数: {total_removed}")
    if stats_by_year:
        print(f"  按年份分布:")
        for year, count in sorted(stats_by_year.items()):
            print(f"    {year}: {count} 个文件")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
