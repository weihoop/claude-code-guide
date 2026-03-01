#!/usr/bin/env python3
"""
中国法院年度案例索引构建工具

功能：
- 从PDF中提取案例文本
- 按标签分割为独立案例
- 解析案例结构化字段
- 生成JSON索引文件
- 保存案例全文为txt文件

用法：
  # 处理某年度PDF
  python3 build_case_index.py --input-dir <PDF目录> --year <年份> --output <输出索引.json>

  # 合并多个索引
  python3 build_case_index.py --merge --inputs <索引1.json> <索引2.json> --output <总索引.json>
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

import pdfplumber


# ============================================================
# 册号-领域映射
# ============================================================
VOLUME_MAP = {
    1: "婚姻家庭与继承纠纷",
    2: "物权纠纷",
    3: "土地纠纷",
    4: "房屋买卖合同纠纷",
    5: "合同纠纷",
    6: "买卖合同纠纷",
    7: "借款担保纠纷",
    8: "民间借贷纠纷",
    9: "侵权赔偿纠纷",
    10: "道路交通纠纷",
    11: "提供劳务者受害责任纠纷",
    12: "人格权纠纷",
    13: "劳动纠纷（含社会保险纠纷）",
    14: "公司纠纷",
    15: "保险纠纷",
    16: "金融纠纷",
    17: "知识产权纠纷",
    18: "行政纠纷",
    19: "刑事案例一",
    20: "刑事案例二",
    21: "刑事案例三",
    22: "刑事案例四",
    23: "执行案例",
}


def extract_volume_number(filename):
    """从PDF文件名中提取册号（1-23）"""
    # 2025版: "中国法院2025年度案例13-劳动纠纷（含社会保险纠纷）.pdf"
    m = re.search(r'案例(\d+)', filename)
    if m:
        num = int(m.group(1))
        if 1 <= num <= 23:
            return num
    # 2024版: "13劳动纠纷（含社会保险纠纷）(OCR).pdf"
    m = re.match(r'^(\d{1,2})(?=\D)', filename)
    if m:
        num = int(m.group(1))
        if 1 <= num <= 23:
            return num
    return None


def clean_page_text(text):
    """清理页面文本中的页眉、页码等干扰内容，合并连续空行"""
    lines = text.split('\n')
    cleaned = []
    prev_blank = False
    for line in lines:
        stripped = line.strip()
        # 跳过页眉行（如 "中国法院2025年度案例 ·劳动纠纷(含社会保险纠纷)"）
        if re.match(r'^中国法院\d{4}年度案例', stripped):
            continue
        # 跳过页码行（纯数字，1-4位）
        if re.match(r'^\d{1,4}$', stripped):
            continue
        # 合并连续空行（保留最多1个）
        if not stripped:
            if prev_blank:
                continue
            prev_blank = True
        else:
            prev_blank = False
        cleaned.append(line)
    return '\n'.join(cleaned)


def _detect_reversed_text(pages_sample):
    """
    检测文本是否为反向OCR文本。
    检查前几页文本中中文标点的出现位置，如果多数标点出现在行首而非行尾，
    则判定为反向文本。
    """
    line_start_punct = 0
    line_end_punct = 0
    cn_puncts = set('。，、；：！？）》】"\'')
    for _, text in pages_sample:
        for line in text.split('\n'):
            stripped = line.strip()
            if len(stripped) < 2:
                continue
            if stripped[0] in cn_puncts:
                line_start_punct += 1
            if stripped[-1] in cn_puncts:
                line_end_punct += 1
    # 如果行首标点数远多于行尾，判定为反向
    total = line_start_punct + line_end_punct
    if total >= 5 and line_start_punct > line_end_punct * 2:
        return True
    return False


def _reverse_text(text):
    """翻转反向OCR文本的每一行"""
    lines = text.split('\n')
    return '\n'.join(line[::-1] for line in lines)


def extract_pdf_text(pdf_path):
    """提取PDF全文文本，返回 [(page_num, text), ...]"""
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages):
            try:
                text = page.extract_text()
                if text:
                    text = clean_page_text(text)
                    pages.append((i + 1, text))
            except Exception as e:
                print(f"  警告: 第{i+1}页提取失败: {e}")
            if (i + 1) % 50 == 0:
                print(f"  已提取 {i+1}/{total} 页...")

    # 检测并修复反向OCR文本
    if pages:
        sample = pages[:min(10, len(pages))]
        if _detect_reversed_text(sample):
            print(f"  检测到反向OCR文本，正在翻转...")
            pages = [(num, _reverse_text(text)) for num, text in pages]

    return pages


def _find_title_start(full_text, info_tag_pos):
    """
    从【案件基本信息】标签位置向前回溯，找到案例标题的起始位置。

    PDF中案例结构为：
      编写人：XXX法院 XXX          ← 上一个案例的结尾
      [子分类标题行，如 "一、确认劳动关系"]  ← 可选，要包含以便后续过滤
      描述性标题（如 "以用工事实与用工合意二要素认定劳动关系"）
      ——冯某诉某餐饮公司劳动合同案
      【案件基本信息】
    """
    # 向前搜索最多800个字符
    lookback_size = 800
    lookback_start = max(0, info_tag_pos - lookback_size)
    lookback = full_text[lookback_start:info_tag_pos]

    # 策略1：找"编写人：XXX"行，标题从其后开始
    editor_match = re.search(r'编写人[：:][^\n]+\n', lookback)
    if editor_match:
        return lookback_start + editor_match.end()

    # 策略2：找最后一个目录行（含省略号），标题在其后
    toc_matches = list(re.finditer(r'[·.…]{3,}\s*\d+\s*\n', lookback))
    if toc_matches:
        return lookback_start + toc_matches[-1].end()

    # 策略3：找"——"当事人行，向前再找标题行
    party_match = re.search(r'\n([—\-]{2}[^\n]+)\n[^\n]*【案件基本信息】', lookback + '【案件基本信息】')
    if party_match:
        # 从当事人行再向前找标题行（非空非数字行）
        pre_party = lookback[:party_match.start()]
        # 取最后几行作为标题候选
        lines = pre_party.rstrip().split('\n')
        # 向前跳过空行，找到标题行
        title_start = party_match.start()
        for i in range(len(lines) - 1, -1, -1):
            stripped = lines[i].strip()
            if not stripped:
                break
            if re.match(r'^\d{1,4}$', stripped):
                # 纯数字行可能是编号也可能是页码，包含进来
                title_start = lookback_start + len('\n'.join(lines[:i])) + 1
                break
            title_start = lookback_start + len('\n'.join(lines[:i])) + 1
        return title_start

    # 策略4：回退到【案件基本信息】前200字符，找最近的空行
    short_lookback = full_text[max(0, info_tag_pos - 200):info_tag_pos]
    # 找到连续两个换行的位置
    double_nl = short_lookback.rfind('\n\n')
    if double_nl >= 0:
        return max(0, info_tag_pos - 200) + double_nl + 2

    # 兜底：直接从【案件基本信息】开始
    return info_tag_pos


def find_case_boundaries(full_text):
    """
    在全文中定位案例边界。

    案例以【案件基本信息】标签开头，在其之前通常有编号和标题行。
    返回 [(case_start_pos, case_end_pos), ...]
    """
    # 严格匹配
    pattern = re.compile(r'【案件基本信息】')
    matches = list(pattern.finditer(full_text))

    # 如果严格匹配无结果，退化为模糊匹配（处理OCR识别偏差）
    if not matches:
        fuzzy_pattern = re.compile(r'[【\[].{0,2}案件基本信息[】\]]')
        matches = list(fuzzy_pattern.finditer(full_text))
        if matches:
            print(f"  使用模糊标签匹配，找到 {len(matches)} 个案例标签")

    if not matches:
        return []

    # 先计算每个案例的标题起始位置
    title_starts = []
    for match in matches:
        title_start = _find_title_start(full_text, match.start())
        title_starts.append(title_start)

    boundaries = []
    for idx in range(len(matches)):
        case_start = title_starts[idx]

        # 案例结束：下一个案例标题的开始，或文本末尾
        if idx + 1 < len(title_starts):
            case_end = title_starts[idx + 1]
        else:
            case_end = len(full_text)

        boundaries.append((case_start, case_end))

    return boundaries


def compute_page_range(case_text_start, case_text_end, page_offsets):
    """根据文本位置计算对应的PDF页码范围"""
    start_page = 1
    end_page = 1
    for page_num, offset_start, offset_end in page_offsets:
        if offset_start <= case_text_start < offset_end:
            start_page = page_num
        if offset_start <= case_text_end <= offset_end:
            end_page = page_num
        if offset_start < case_text_end:
            end_page = page_num
    return start_page, end_page


def _clean_section_text(text):
    """清理段落文本中的脚注标记、页眉残留、编写人行等"""
    # 去除脚注标记
    text = re.sub(r'[①②③④⑤⑥⑦⑧⑨⑩]', '', text)
    # 去除页眉行残留
    text = re.sub(r'中国法院\d{4}年度案例\s*[·•]\s*\S+', '', text)
    # 去除子分类标题残留（如 "一、确认劳动关系 3"）
    text = re.sub(r'\n[一二三四五六七八九十]+[、．.]\s*\S+\s*\d*\s*\n', '\n', text)
    # 去除脚注内容行（以小字体开头，通常在行首）
    text = re.sub(r'\n本书【[^】]+】[^\n]+\n', '\n', text)
    # 去除编写人行
    text = re.sub(r'\n编写人[：:][^\n]+\n', '\n', text)
    # 去除多余连续空行
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def _clean_case_text_header(case_text):
    """
    清理案例全文头部（【案件基本信息】之前）的残留目录行和分类标题行。

    残留类型：
    - 分类标题行：如 "一、婚姻家庭纠纷"、"一、确认劳动关系 3"
    - 子分类标题行：如 "(一)离婚纠纷"
    - 目录行：含省略号和页码的行
    - 页眉行：如 "14 中国法院2025年度案例·合同纠纷"
    """
    # 定位【案件基本信息】
    info_pos = case_text.find('【案件基本信息】')
    if info_pos < 0:
        return case_text

    header = case_text[:info_pos]
    body = case_text[info_pos:]

    lines = header.split('\n')
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # 跳过空行不做判断，直接保留
        if not stripped:
            cleaned.append(line)
            continue
        # 分类标题行（"一、XX纠纷"或"一、XX纠纷 3"，可能含多字标题）
        if re.match(r'^[一二三四五六七八九十]+[、．.]\s*\S+.*$', stripped):
            # 排除真正的案例标题（通常较长且不以中文数字序号开头后接短词）
            # 分类标题特征：中文序号 + 短标题（通常<20字）+ 可选页码
            inner = re.sub(r'^[一二三四五六七八九十]+[、．.]\s*', '', stripped)
            inner = re.sub(r'\s+\d+$', '', inner)  # 去掉尾部页码
            if len(inner) <= 20:
                continue
        # 子分类标题行：(一)XX、（二）XX
        if re.match(r'^[（(][一二三四五六七八九十]+[）)]\s*\S+', stripped):
            inner = re.sub(r'^[（(][一二三四五六七八九十]+[）)]\s*', '', stripped)
            if len(inner) <= 20:
                continue
        # 页眉残留行（如 "14 中国法院2025年度案例·合同纠纷"）
        if re.search(r'中国法院\d{4}年度案例', stripped):
            continue
        # 目录行（含省略号）
        if re.search(r'[·.…]{3,}\s*\d+', stripped):
            continue
        cleaned.append(line)

    # 去掉头部连续空行
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)

    return '\n'.join(cleaned) + body


def parse_case(case_text, volume_num, year, case_index_in_volume):
    """解析单个案例文本，提取结构化字段"""
    result = {
        "_提取质量": "完整"
    }

    # 提取各段落
    sections = {}
    section_labels = ['案件基本信息', '基本案情', '案件焦点', '法院裁判要旨', '法官后语']

    for i, label in enumerate(section_labels):
        pattern = re.compile(r'【' + label + r'】[①②③④⑤⑥⑦⑧⑨⑩]?\s*\n?')
        match = pattern.search(case_text)
        if match:
            section_start = match.end()
            # 查找下一个段落标签
            next_start = len(case_text)
            for next_label in section_labels[i+1:]:
                next_pattern = re.compile(r'【' + next_label + r'】')
                next_match = next_pattern.search(case_text, section_start)
                if next_match:
                    next_start = next_match.start()
                    break
            sections[label] = case_text[section_start:next_start].strip()

    # 判断提取质量
    if not sections.get('案件基本信息'):
        result["_提取质量"] = "仅全文"
    elif not sections.get('法院裁判要旨'):
        result["_提取质量"] = "部分"

    # 解析案件基本信息
    info = sections.get('案件基本信息', '')

    # 裁判书字号
    case_number_match = re.search(r'[（(]\s*\d{4}\s*[）)]\s*[\w\u4e00-\u9fff]+\d+号', info)
    if not case_number_match:
        # 更宽松的匹配
        case_number_match = re.search(r'[（(]\d{4}[）)].*?号', info)
    result['裁判书字号'] = case_number_match.group(0).strip() if case_number_match else ""

    # 案由
    case_cause_match = re.search(r'案\s*由[：:]\s*(.+?)(?:\n|$)', info)
    result['案由'] = case_cause_match.group(1).strip() if case_cause_match else ""

    # 当事人
    parties = []
    # 原告
    plaintiff_match = re.search(r'原告[^：:]*[：:]\s*(.+?)(?:\n|$)', info)
    if plaintiff_match:
        parties.append("原告：" + plaintiff_match.group(1).strip())
    # 被告
    defendant_match = re.search(r'被告[^：:]*[：:]\s*(.+?)(?:\n|$)', info)
    if defendant_match:
        parties.append("被告：" + defendant_match.group(1).strip())
    # 第三人
    third_party_match = re.search(r'第三人[^：:]*[：:]\s*(.+?)(?:\n|$)', info)
    if third_party_match:
        parties.append("第三人：" + third_party_match.group(1).strip())
    # 刑事案例: 公诉机关/被告人
    prosecutor_match = re.search(r'公诉机关[：:]\s*(.+?)(?:\n|$)', info)
    if prosecutor_match:
        parties.append("公诉机关：" + prosecutor_match.group(1).strip())
    accused_match = re.search(r'被告人[^：:]*[：:]\s*(.+?)(?:\n|$)', info)
    if accused_match:
        parties.append("被告人：" + accused_match.group(1).strip())
    # 申请人/被申请人 (执行案例)
    applicant_match = re.search(r'申请(?:执行)?人[^：:]*[：:]\s*(.+?)(?:\n|$)', info)
    if applicant_match:
        parties.append("申请人：" + applicant_match.group(1).strip())
    respondent_match = re.search(r'被(?:执行)?申请人[^：:]*[：:]\s*(.+?)(?:\n|$)', info)
    if respondent_match:
        parties.append("被申请人：" + respondent_match.group(1).strip())

    result['当事人'] = "；".join(parties) if parties else ""

    # 法院 - 从裁判书字号前后文提取
    court_match = re.search(r'([\u4e00-\u9fff]+(?:人民)?法院)', info)
    result['法院'] = court_match.group(1).strip() if court_match else ""

    # 提取标题 - 在【案件基本信息】之前的文本
    pre_info = case_text[:case_text.find('【案件基本信息】')] if '【案件基本信息】' in case_text else ""
    # 标题和当事人行通常在【案件基本信息】前的最后几行
    # 格式：
    #   子分类标题行（如 "一、确认劳动关系 11" 或 "一、确认劳动关系"）  ← 要过滤
    #   描述性标题（如 "以用工事实与用工合意二要素认定劳动关系"）        ← 要保留
    #   当事人行（如 "——冯某诉某餐饮公司劳动合同案" 或 "— — 冯某诉..."） ← 要保留
    title_lines = [l.strip() for l in pre_info.strip().split('\n') if l.strip()]

    # 过滤干扰行
    def is_noise_line(line):
        # 纯数字行（页码）
        if re.match(r'^\d+$', line):
            return True
        # 页眉行
        if '中国法院' in line:
            return True
        # 目录行
        if '目 录' in line:
            return True
        # 子分类标题行（如 "一、确认劳动关系 11" 或 "一、确认劳动关系"）
        if re.match(r'^[一二三四五六七八九十]+[、．.]\s*\S+(?:\s+\d+)?$', line):
            return True
        # (一)类标题行
        if re.match(r'^[（(][一二三四五六七八九十]+[）)]', line):
            return True
        # 编写人行（前一个案例的结尾）
        if re.match(r'^编写人[：:]', line):
            return True
        # 目录内容行（含虚线和页码，如 "62. 劳动者和用人单位... 314"）
        if re.search(r'\.{3,}', line) or re.search(r'…{2,}', line):
            return True
        # 太短的行（小于2个字符）
        if len(line) <= 1:
            return True
        return False

    filtered = [l for l in title_lines if not is_noise_line(l)]

    # 从过滤后的行中提取标题和当事人
    title_parts = []
    party_line = ""
    for line in filtered:
        if line.startswith('——') or line.startswith('— —') or line.startswith('--'):
            party_line = re.sub(r'^[—\-\s]+', '', line).strip()
        elif re.match(r'^.{0,10}诉.+案$', line):
            # 当事人行没有"——"前缀的情况（如"某科技公司诉宋某劳动争议案"）
            party_line = line.strip()
        else:
            title_parts.append(line)

    # 清理标题中的脚注标记
    title = "".join(title_parts) if title_parts else f"案例{case_index_in_volume}"
    title = re.sub(r'[①②③④⑤⑥⑦⑧⑨⑩]+', '', title).strip()
    result['标题'] = title

    # 从当事人行提取简短当事人描述
    if party_line and not result['当事人']:
        result['当事人'] = party_line

    # 基本案情摘要 (前200字)
    basic_facts = sections.get('基本案情', '')
    # 清理脚注标记和页眉残留
    basic_facts_clean = _clean_section_text(basic_facts)
    result['基本案情摘要'] = basic_facts_clean[:200].strip() + ("..." if len(basic_facts_clean) > 200 else "")

    # 案件焦点
    focus = sections.get('案件焦点', '')
    focus_clean = re.sub(r'[①②③④⑤⑥⑦⑧⑨⑩]', '', focus).strip()
    # 分割多个焦点
    focus_items = re.split(r'\d+[.、．]\s*', focus_clean)
    focus_items = [f.strip() for f in focus_items if f.strip()]
    if not focus_items and focus_clean:
        focus_items = [focus_clean]
    result['案件焦点'] = focus_items

    # 裁判要旨（索引中只存摘要，全文在txt文件中）
    ruling = sections.get('法院裁判要旨', '')
    ruling_clean = _clean_section_text(ruling)
    result['裁判要旨'] = ruling_clean[:300].strip() + ("..." if len(ruling_clean) > 300 else "")

    # 法官后语摘要 (前150字)
    judge_note = sections.get('法官后语', '')
    judge_note_clean = _clean_section_text(judge_note)
    result['法官后语摘要'] = judge_note_clean[:150].strip() + ("..." if len(judge_note_clean) > 150 else "")

    # 涉及法条 - 先将文本中的换行符去除再匹配
    laws = set()
    law_pattern = re.compile(r'《[^》]+》(?:第[\d一二三四五六七八九十百千零]+条(?:之[一二三四五六七八九十])?(?:第[\d一二三四五六七八九十百千零]+款)?(?:第[\d一二三四五六七八九十百千零]+项)?(?:[、，,]第[\d一二三四五六七八九十百千零]+条(?:之[一二三四五六七八九十])?(?:第[\d一二三四五六七八九十百千零]+款)?(?:第[\d一二三四五六七八九十百千零]+项)?)*)')
    for section_text in [ruling, judge_note, basic_facts]:
        # 去掉换行符以避免法条名被拆分
        text_no_newline = section_text.replace('\n', '')
        for m in law_pattern.finditer(text_no_newline):
            laws.add(m.group(0))
    result['涉及法条'] = sorted(list(laws))

    return result, sections


def process_single_pdf(pdf_path, year, volume_num, fulltext_dir):
    """处理单个PDF文件，返回案例列表"""
    filename = os.path.basename(pdf_path)
    domain = VOLUME_MAP.get(volume_num, f"未知领域{volume_num}")
    print(f"\n处理: {filename}")
    print(f"  册号: {volume_num}, 领域: {domain}")

    # 提取所有页面文本
    pages = extract_pdf_text(pdf_path)
    print(f"  提取了 {len(pages)} 页文本")

    if not pages:
        print(f"  警告: 未提取到任何文本！")
        return []

    # 构建全文和页码偏移映射（使用 list + join 避免 O(n²) 拼接）
    text_parts = []
    page_offsets = []  # [(page_num, start_offset, end_offset), ...]
    current_offset = 0
    for page_num, text in pages:
        part = text + "\n\n"
        text_parts.append(part)
        page_offsets.append((page_num, current_offset, current_offset + len(part)))
        current_offset += len(part)
    full_text = "".join(text_parts)

    # 查找案例边界
    boundaries = find_case_boundaries(full_text)
    print(f"  找到 {len(boundaries)} 个案例")

    if not boundaries:
        print(f"  警告: 未找到任何案例边界！将全文作为单个案例保存。")
        # 退化：保存全文
        case_dir = os.path.join(fulltext_dir, str(year), f"{volume_num:02d}-{domain}")
        os.makedirs(case_dir, exist_ok=True)
        with open(os.path.join(case_dir, "全文.txt"), 'w', encoding='utf-8') as f:
            f.write(full_text)
        return []

    cases = []
    for idx, (start, end) in enumerate(boundaries):
        case_text = full_text[start:end].strip()
        case_index = idx + 1

        # 计算页码范围
        start_page, end_page = compute_page_range(start, end, page_offsets)

        # 解析案例
        parsed, sections = parse_case(case_text, volume_num, year, case_index)

        # 构建案例ID
        case_id = f"{year}-{volume_num:02d}-{case_index:03d}"

        case_entry = {
            "id": case_id,
            "年份": str(year),
            "册号": volume_num,
            "领域": domain,
            "案例序号": case_index,
            "标题": parsed['标题'],
            "当事人": parsed['当事人'],
            "裁判书字号": parsed['裁判书字号'],
            "案由": parsed['案由'],
            "法院": parsed['法院'],
            "基本案情摘要": parsed['基本案情摘要'],
            "案件焦点": parsed['案件焦点'],
            "裁判要旨": parsed['裁判要旨'],
            "法官后语摘要": parsed['法官后语摘要'],
            "涉及法条": parsed['涉及法条'],
            "PDF来源": filename,
            "页码范围": f"{start_page}-{end_page}",
            "_提取质量": parsed['_提取质量'],
        }
        cases.append(case_entry)

        # 保存全文txt
        case_dir = os.path.join(fulltext_dir, str(year), f"{volume_num:02d}-{domain}")
        os.makedirs(case_dir, exist_ok=True)
        txt_path = os.path.join(case_dir, f"{case_index:03d}.txt")
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(f"案例ID: {case_id}\n")
            f.write(f"标题: {parsed['标题']}\n")
            f.write(f"来源: {filename} 第{start_page}-{end_page}页\n")
            f.write(f"{'='*60}\n\n")
            f.write(_clean_case_text_header(case_text))

    # 统计提取质量
    quality_stats = {}
    for c in cases:
        q = c['_提取质量']
        quality_stats[q] = quality_stats.get(q, 0) + 1
    print(f"  提取质量: {quality_stats}")

    return cases


def process_directory(input_dir, year, output_path, fulltext_dir):
    """处理一个目录下的所有PDF"""
    input_path = Path(input_dir)
    pdf_files = sorted(input_path.glob("*.pdf"))

    if not pdf_files:
        print(f"错误: 在 {input_dir} 中未找到PDF文件")
        sys.exit(1)

    print(f"找到 {len(pdf_files)} 个PDF文件")

    all_cases = []
    domain_cases = {}

    for pdf_file in pdf_files:
        volume_num = extract_volume_number(pdf_file.name)
        if volume_num is None:
            print(f"  跳过: {pdf_file.name} (无法识别册号)")
            continue

        cases = process_single_pdf(str(pdf_file), year, volume_num, fulltext_dir)
        all_cases.extend(cases)

        # 按领域分组
        domain = VOLUME_MAP.get(volume_num, f"未知领域{volume_num}")
        if domain not in domain_cases:
            domain_cases[domain] = []
        domain_cases[domain].extend(cases)

    # 构建索引
    index = {
        "_说明": f"中国法院{year}年度案例索引，供法律AI Skills参考使用",
        "_版本": "v1.0",
        "_案例总数": len(all_cases),
        "_覆盖年份": [str(year)],
        "_领域分类": sorted(domain_cases.keys()),
        "_生成日期": date.today().isoformat(),
        "_使用方式": "Claude分析案件时，按领域或关键词在本文件中检索相似案例，参考裁判要旨和法官后语",
        "按领域分类": domain_cases,
    }

    # 写入JSON
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n{'='*60}")
    print(f"索引生成完成: {output_path}")
    print(f"案例总数: {len(all_cases)}")
    print(f"覆盖领域: {len(domain_cases)} 个")
    print(f"文件大小: {file_size:.2f} MB")
    print(f"{'='*60}")

    return index


def merge_indexes(input_files, output_path):
    """合并多个年份的索引文件"""
    merged_cases_by_domain = {}
    merged_cases_by_year = {}
    all_years = set()
    all_domains = set()
    total_cases = 0

    for input_file in input_files:
        print(f"读取索引: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            index = json.load(f)

        year_list = index.get('_覆盖年份', [])
        total_cases += index.get('_案例总数', 0)
        all_years.update(year_list)

        for domain, cases in index.get('按领域分类', {}).items():
            all_domains.add(domain)
            if domain not in merged_cases_by_domain:
                merged_cases_by_domain[domain] = []
            merged_cases_by_domain[domain].extend(cases)

            # 按年份分类
            for case in cases:
                case_year = case.get('年份', year_list[0] if year_list else 'unknown')
                if case_year not in merged_cases_by_year:
                    merged_cases_by_year[case_year] = {}
                if domain not in merged_cases_by_year[case_year]:
                    merged_cases_by_year[case_year][domain] = []
                merged_cases_by_year[case_year][domain].append(case)

    merged_index = {
        "_说明": "中国法院年度案例索引，供法律AI Skills参考使用",
        "_版本": "v1.0",
        "_案例总数": total_cases,
        "_覆盖年份": sorted(list(all_years)),
        "_领域分类": sorted(list(all_domains)),
        "_生成日期": date.today().isoformat(),
        "_使用方式": "Claude分析案件时，按领域或关键词在本文件中检索相似案例，参考裁判要旨和法官后语",
        "按领域分类": merged_cases_by_domain,
        "按年份分类": merged_cases_by_year,
    }

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged_index, f, ensure_ascii=False, indent=2)

    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n{'='*60}")
    print(f"合并索引生成完成: {output_path}")
    print(f"案例总数: {total_cases}")
    print(f"覆盖年份: {sorted(list(all_years))}")
    print(f"覆盖领域: {len(all_domains)} 个")
    print(f"文件大小: {file_size:.2f} MB")
    print(f"{'='*60}")


def main():
    parser = argparse.ArgumentParser(description='中国法院年度案例索引构建工具')
    parser.add_argument('--input-dir', help='PDF文件所在目录')
    parser.add_argument('--year', type=int, help='案例年份（如2024、2025）')
    parser.add_argument('--output', required=True, help='输出索引JSON文件路径')
    parser.add_argument('--fulltext-dir',
                        default=os.path.expanduser('~/.claude/skills/shared/references/案例全文'),
                        help='全文存储目录')
    parser.add_argument('--merge', action='store_true', help='合并模式')
    parser.add_argument('--inputs', nargs='+', help='合并模式下的输入索引文件列表')

    args = parser.parse_args()

    if args.merge:
        if not args.inputs:
            print("错误: 合并模式需要 --inputs 参数指定输入文件")
            sys.exit(1)
        merge_indexes(args.inputs, args.output)
    else:
        if not args.input_dir or not args.year:
            print("错误: 需要 --input-dir 和 --year 参数")
            sys.exit(1)
        process_directory(args.input_dir, args.year, args.output, args.fulltext_dir)


if __name__ == '__main__':
    main()
