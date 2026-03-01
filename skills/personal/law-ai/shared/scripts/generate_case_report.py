#!/usr/bin/env python3
"""
中国法院年度案例参考库 — HTML可视化报告生成器

功能：
- 读取案例索引JSON，生成单个自包含HTML文件
- 支持按领域分类浏览、年份筛选、关键词搜索
- 点击展开案例详情、全文路径显示
- 响应式布局，纯前端JS实现

用法：
  python3 generate_case_report.py [--input <索引.json>] [--output <输出.html>]
"""

import argparse
import json
import os
import sys
from datetime import date


def escape_html(text):
    """转义HTML特殊字符"""
    if not text:
        return ""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;"))


def escape_js_string(text):
    """转义JS字符串中的特殊字符"""
    if not text:
        return ""
    return (text
            .replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("'", "\\'")
            .replace("\n", "\\n")
            .replace("\r", "\\r")
            .replace("\t", "\\t"))


def generate_html(index_data, output_path):
    """生成HTML报告"""
    # 提取元数据
    total_cases = index_data.get("_案例总数", 0)
    years = index_data.get("_覆盖年份", [])
    domains = index_data.get("_领域分类", [])
    gen_date = index_data.get("_生成日期", date.today().isoformat())
    cases_by_domain = index_data.get("按领域分类", {})

    # 统计各领域数量和质量
    domain_stats = {}
    quality_stats = {"完整": 0, "部分": 0, "仅全文": 0}
    year_stats = {}
    # 按领域+年份交叉统计（用于对比柱状图）
    domain_year_stats = {}
    for domain, cases in cases_by_domain.items():
        domain_stats[domain] = len(cases)
        for case in cases:
            q = case.get("_提取质量", "未知")
            quality_stats[q] = quality_stats.get(q, 0) + 1
            y = str(case.get("年份", "未知"))
            year_stats[y] = year_stats.get(y, 0) + 1
            if domain not in domain_year_stats:
                domain_year_stats[domain] = {}
            domain_year_stats[domain][y] = domain_year_stats[domain].get(y, 0) + 1

    # 按册号排序领域
    volume_order = {}
    for case_list in cases_by_domain.values():
        if case_list:
            domain = case_list[0].get("领域", "")
            vol = case_list[0].get("册号", 99)
            volume_order[domain] = vol
    sorted_domains = sorted(cases_by_domain.keys(), key=lambda d: volume_order.get(d, 99))

    # 构建案例JSON数据（嵌入HTML）
    all_cases_for_js = []
    for domain in sorted_domains:
        cases = cases_by_domain[domain]
        for case in cases:
            all_cases_for_js.append({
                "id": case.get("id", ""),
                "年份": case.get("年份", ""),
                "册号": case.get("册号", 0),
                "领域": case.get("领域", ""),
                "标题": case.get("标题", ""),
                "当事人": case.get("当事人", ""),
                "裁判书字号": case.get("裁判书字号", ""),
                "案由": case.get("案由", ""),
                "法院": case.get("法院", ""),
                "基本案情摘要": case.get("基本案情摘要", ""),
                "案件焦点": case.get("案件焦点", []),
                "裁判要旨": case.get("裁判要旨", ""),
                "法官后语摘要": case.get("法官后语摘要", ""),
                "涉及法条": case.get("涉及法条", []),
                "页码范围": case.get("页码范围", ""),
                "_提取质量": case.get("_提取质量", ""),
                "PDF来源": case.get("PDF来源", ""),
            })

    cases_json = json.dumps(all_cases_for_js, ensure_ascii=False)

    # 领域统计JSON
    domain_stats_json = json.dumps(
        [{"name": d, "count": domain_stats.get(d, 0)} for d in sorted_domains],
        ensure_ascii=False
    )

    # 领域-年份交叉统计JSON（用于对比柱状图）
    domain_year_stats_json = json.dumps(
        {d: domain_year_stats.get(d, {}) for d in sorted_domains},
        ensure_ascii=False
    )

    # 年份统计JSON
    year_stats_json = json.dumps(year_stats, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>中国法院年度案例参考库</title>
<style>
:root {{
  --primary: #17376A;
  --primary-light: #2E74B5;
  --primary-bg: #EBF1F8;
  --header-bg: #2F5496;
  --text: #333;
  --text-light: #666;
  --border: #D6E4F0;
  --bg: #F5F7FA;
  --white: #fff;
  --red: #C0392B;
  --orange: #E67E22;
  --green: #27AE60;
  --sidebar-w: 240px;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}}

/* 顶部区域 */
.header {{
  background: linear-gradient(135deg, var(--primary) 0%, var(--header-bg) 100%);
  color: var(--white);
  padding: 32px 40px 24px;
  text-align: center;
}}
.header h1 {{
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 8px;
  letter-spacing: 2px;
}}
.header .subtitle {{
  font-size: 15px;
  opacity: 0.85;
}}

/* 统计概览 */
.stats-bar {{
  display: flex;
  justify-content: center;
  gap: 32px;
  margin-top: 20px;
  flex-wrap: wrap;
}}
.stat-item {{
  text-align: center;
}}
.stat-num {{
  font-size: 28px;
  font-weight: 700;
}}
.stat-label {{
  font-size: 13px;
  opacity: 0.8;
  margin-top: 2px;
}}

/* 统计概览区 */
.overview {{
  background: var(--white);
  margin: 20px 24px;
  border-radius: 10px;
  border: 1px solid var(--border);
  padding: 24px;
  display: none;
}}
.overview.show {{ display: block; }}
.overview-toggle {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 16px;
  padding: 6px 16px;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 20px;
  color: var(--white);
  font-size: 13px;
  cursor: pointer;
  transition: background .2s;
}}
.overview-toggle:hover {{ background: rgba(255,255,255,0.25); }}
.overview h3 {{
  font-size: 15px;
  color: var(--primary);
  margin-bottom: 16px;
  font-weight: 600;
}}
.chart-row {{
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
}}
.chart-box {{
  flex: 1;
  min-width: 300px;
}}
.chart-box h4 {{
  font-size: 13px;
  color: var(--text-light);
  margin-bottom: 10px;
  font-weight: 500;
}}
.bar-chart {{
  display: flex;
  flex-direction: column;
  gap: 4px;
}}
.bar-row {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
}}
.bar-label {{
  width: 120px;
  text-align: right;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  flex-shrink: 0;
}}
.bar-track {{
  flex: 1;
  height: 18px;
  background: var(--primary-bg);
  border-radius: 3px;
  overflow: hidden;
  display: flex;
}}
.bar-fill {{
  height: 100%;
  border-radius: 3px;
  transition: width .4s ease;
}}
.bar-fill-2024 {{ background: var(--primary-light); }}
.bar-fill-2025 {{ background: var(--primary); }}
.bar-value {{
  width: 36px;
  text-align: right;
  color: var(--text-light);
  font-family: "SF Mono", monospace;
  flex-shrink: 0;
}}
.chart-legend {{
  display: flex;
  gap: 16px;
  margin-bottom: 8px;
  font-size: 12px;
  color: var(--text-light);
}}
.legend-dot {{
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 2px;
  margin-right: 4px;
  vertical-align: middle;
}}
.year-compare {{
  display: flex;
  gap: 20px;
  margin-top: 16px;
  flex-wrap: wrap;
}}
.year-card {{
  flex: 1;
  min-width: 120px;
  background: var(--primary-bg);
  border-radius: 8px;
  padding: 14px;
  text-align: center;
}}
.year-card .yc-year {{
  font-size: 13px;
  color: var(--text-light);
  margin-bottom: 4px;
}}
.year-card .yc-num {{
  font-size: 24px;
  font-weight: 700;
  color: var(--primary);
}}
.year-card .yc-label {{
  font-size: 11px;
  color: var(--text-light);
  margin-top: 2px;
}}

/* 返回顶部按钮 */
.back-to-top {{
  position: fixed;
  bottom: 32px;
  right: 32px;
  width: 40px;
  height: 40px;
  background: var(--primary);
  color: var(--white);
  border: none;
  border-radius: 50%;
  font-size: 18px;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s, visibility .3s, transform .2s;
  z-index: 200;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.back-to-top.visible {{
  opacity: 1;
  visibility: visible;
}}
.back-to-top:hover {{
  transform: scale(1.1);
  background: var(--primary-light);
}}

/* 工具栏 */
.toolbar {{
  background: var(--white);
  border-bottom: 1px solid var(--border);
  padding: 12px 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}}
.search-box {{
  flex: 1;
  min-width: 200px;
  max-width: 480px;
  position: relative;
}}
.search-box input {{
  width: 100%;
  padding: 8px 12px 8px 36px;
  border: 1px solid var(--border);
  border-radius: 6px;
  font-size: 14px;
  outline: none;
  transition: border-color .2s;
}}
.search-box input:focus {{
  border-color: var(--primary-light);
}}
.search-box::before {{
  content: "\\1F50D";
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 14px;
}}
.filter-select {{
  padding: 8px 12px;
  border: 1px solid var(--border);
  border-radius: 6px;
  font-size: 14px;
  background: var(--white);
  outline: none;
  cursor: pointer;
}}
.result-count {{
  font-size: 13px;
  color: var(--text-light);
  white-space: nowrap;
}}

/* 主体布局 */
.main {{
  display: flex;
  min-height: calc(100vh - 200px);
}}

/* 左侧导航 */
.sidebar {{
  width: var(--sidebar-w);
  background: var(--white);
  border-right: 1px solid var(--border);
  padding: 16px 0;
  overflow-y: auto;
  flex-shrink: 0;
  height: calc(100vh - 140px);
  position: sticky;
  top: 52px;
}}
.sidebar-title {{
  font-size: 13px;
  font-weight: 600;
  color: var(--text-light);
  padding: 0 16px 8px;
  text-transform: uppercase;
  letter-spacing: 1px;
}}
.nav-item {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 16px;
  cursor: pointer;
  font-size: 13px;
  color: var(--text);
  transition: all .15s;
  border-left: 3px solid transparent;
}}
.nav-item:hover {{
  background: var(--primary-bg);
}}
.nav-item.active {{
  background: var(--primary-bg);
  color: var(--primary);
  font-weight: 600;
  border-left-color: var(--primary);
}}
.nav-count {{
  background: var(--primary-bg);
  color: var(--primary-light);
  padding: 1px 8px;
  border-radius: 10px;
  font-size: 11px;
  font-weight: 600;
}}
.nav-item.active .nav-count {{
  background: var(--primary);
  color: var(--white);
}}

/* 案例列表区 */
.content {{
  flex: 1;
  padding: 20px 24px;
  max-width: 960px;
}}

/* 案例卡片 */
.case-card {{
  background: var(--white);
  border-radius: 8px;
  margin-bottom: 12px;
  border: 1px solid var(--border);
  overflow: hidden;
  transition: box-shadow .2s;
}}
.case-card:hover {{
  box-shadow: 0 2px 12px rgba(23,55,106,0.08);
}}
.case-header {{
  padding: 14px 18px;
  cursor: pointer;
  display: flex;
  align-items: flex-start;
  gap: 12px;
}}
.case-header:hover {{
  background: #FAFBFD;
}}
.case-toggle {{
  color: var(--primary-light);
  font-size: 12px;
  margin-top: 3px;
  transition: transform .2s;
  flex-shrink: 0;
}}
.case-card.open .case-toggle {{
  transform: rotate(90deg);
}}
.case-info {{
  flex: 1;
  min-width: 0;
}}
.case-id {{
  font-size: 12px;
  color: var(--primary-light);
  font-weight: 600;
  font-family: "SF Mono", "Fira Code", monospace;
}}
.case-title {{
  font-size: 15px;
  font-weight: 600;
  color: var(--primary);
  margin: 4px 0;
  line-height: 1.4;
}}
.case-meta {{
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  margin-top: 4px;
}}
.case-meta span {{
  font-size: 12px;
  color: var(--text-light);
}}
.case-meta .tag {{
  background: var(--primary-bg);
  color: var(--primary);
  padding: 1px 8px;
  border-radius: 3px;
  font-size: 11px;
  font-weight: 500;
}}
.quality-tag {{
  padding: 1px 8px;
  border-radius: 3px;
  font-size: 11px;
  font-weight: 500;
}}
.quality-complete {{ background: #E8F5E9; color: var(--green); }}
.quality-partial {{ background: #FFF3E0; color: var(--orange); }}
.quality-textonly {{ background: #FFEBEE; color: var(--red); }}

/* 展开详情 */
.case-detail {{
  display: none;
  padding: 0 18px 18px;
  border-top: 1px solid var(--border);
}}
.case-card.open .case-detail {{
  display: block;
}}
.detail-section {{
  margin-top: 14px;
}}
.detail-section h4 {{
  font-size: 13px;
  font-weight: 600;
  color: var(--primary);
  margin-bottom: 6px;
  padding-bottom: 4px;
  border-bottom: 1px solid var(--primary-bg);
}}
.detail-section p, .detail-section li {{
  font-size: 13px;
  color: var(--text);
  line-height: 1.7;
}}
.detail-section ul {{
  padding-left: 18px;
}}
.detail-section li {{
  margin-bottom: 4px;
}}
.law-tags {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}}
.law-tag {{
  background: #EDE7F6;
  color: #5E35B1;
  padding: 2px 10px;
  border-radius: 4px;
  font-size: 12px;
}}
.path-box {{
  background: #F5F5F5;
  border: 1px solid #E0E0E0;
  border-radius: 4px;
  padding: 8px 12px;
  font-family: "SF Mono", "Fira Code", monospace;
  font-size: 12px;
  color: var(--text-light);
  word-break: break-all;
  cursor: pointer;
  position: relative;
}}
.path-box:hover {{
  background: #EEEEEE;
}}
.path-box .copy-hint {{
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 11px;
  color: var(--primary-light);
}}

/* 空状态 */
.empty-state {{
  text-align: center;
  padding: 60px 20px;
  color: var(--text-light);
}}
.empty-state .icon {{
  font-size: 48px;
  margin-bottom: 16px;
}}
.empty-state p {{
  font-size: 15px;
}}

/* 页脚 */
.footer {{
  text-align: center;
  padding: 24px;
  font-size: 12px;
  color: var(--text-light);
  border-top: 1px solid var(--border);
  background: var(--white);
}}

/* 响应式 */
@media (max-width: 768px) {{
  .sidebar {{ display: none; }}
  .header {{ padding: 20px 16px 16px; }}
  .header h1 {{ font-size: 22px; }}
  .stats-bar {{ gap: 16px; }}
  .stat-num {{ font-size: 22px; }}
  .toolbar {{ padding: 10px 12px; }}
  .content {{ padding: 12px; }}
}}

/* 打印样式 */
@media print {{
  .toolbar, .sidebar {{ display: none; }}
  .case-card {{ break-inside: avoid; }}
  .case-detail {{ display: block !important; }}
  .header {{ padding: 16px; }}
}}
</style>
</head>
<body>

<div class="header">
  <h1>中国法院年度案例参考库</h1>
  <p class="subtitle">{total_cases} 个案例 &middot; {len(sorted_domains)} 个领域 &middot; {'-'.join(years)} 年度 &middot; 生成于 {gen_date}</p>
  <div class="stats-bar">
    <div class="stat-item">
      <div class="stat-num">{total_cases}</div>
      <div class="stat-label">案例总数</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">{len(sorted_domains)}</div>
      <div class="stat-label">法律领域</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">{len(years)}</div>
      <div class="stat-label">覆盖年份</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">{quality_stats.get('完整', 0)}</div>
      <div class="stat-label">完整提取</div>
    </div>
  </div>
  <div class="overview-toggle" onclick="toggleOverview()">&#128202; 统计概览</div>
</div>

<div class="overview" id="overviewPanel">
  <h3>数据统计概览</h3>
  <div class="chart-row">
    <div class="chart-box">
      <h4>各领域案例数量分布</h4>
      <div class="chart-legend">
        <span><span class="legend-dot" style="background:var(--primary-light)"></span>2024</span>
        <span><span class="legend-dot" style="background:var(--primary)"></span>2025</span>
      </div>
      <div class="bar-chart" id="domainChart"></div>
    </div>
    <div class="chart-box" style="max-width:280px">
      <h4>年份案例对比</h4>
      <div class="year-compare" id="yearCompare"></div>
      <div style="margin-top:16px">
        <h4>提取质量分布</h4>
        <div id="qualityChart" style="margin-top:8px"></div>
      </div>
    </div>
  </div>
</div>

<div class="toolbar">
  <div class="search-box">
    <input type="text" id="searchInput" placeholder="搜索标题、案由、裁判要旨、法条..." oninput="debouncedFilter()">
  </div>
  <select class="filter-select" id="yearFilter" onchange="filterCases()">
    <option value="">全部年份</option>
    {"".join(f'<option value="{y}">{y}年</option>' for y in sorted(years))}
  </select>
  <select class="filter-select" id="domainFilter" onchange="filterCases(); highlightNav();">
    <option value="">全部领域</option>
    {"".join(f'<option value="{escape_html(d)}">{escape_html(d)}（{domain_stats.get(d, 0)}）</option>' for d in sorted_domains)}
  </select>
  <span class="result-count" id="resultCount">{total_cases} 个案例</span>
</div>

<div class="main">
  <div class="sidebar" id="sidebar">
    <div class="sidebar-title">领域导航</div>
    <div class="nav-item active" data-domain="" onclick="selectDomain(this, '')">
      <span>全部领域</span>
      <span class="nav-count">{total_cases}</span>
    </div>
    {"".join(f'''
    <div class="nav-item" data-domain="{escape_html(d)}" onclick="selectDomain(this, '{escape_js_string(d)}')">
      <span>{escape_html(d)}</span>
      <span class="nav-count">{domain_stats.get(d, 0)}</span>
    </div>''' for d in sorted_domains)}
  </div>
  <div class="content" id="caseList">
    <!-- 案例卡片由JS动态渲染 -->
  </div>
</div>

<div class="footer">
  中国法院年度案例参考库 &middot; 数据来源：国家法官学院《中国法院年度案例》 &middot; 仅供法律研究参考，不构成法律意见
</div>

<button class="back-to-top" id="backToTop" onclick="scrollToTop()" title="返回顶部">&#9650;</button>

<script>
// 案例数据
const ALL_CASES = {cases_json};

// 领域统计
const DOMAIN_STATS = {domain_stats_json};

// 领域-年份交叉统计
const DOMAIN_YEAR_STATS = {domain_year_stats_json};

// 年份统计
const YEAR_STATS = {year_stats_json};

// 当前筛选结果
let filteredCases = ALL_CASES;

// 搜索防抖定时器
let searchTimer = null;

// 渲染案例列表
function renderCases(cases) {{
  const container = document.getElementById('caseList');
  if (!cases.length) {{
    container.innerHTML = '<div class="empty-state"><div class="icon">&#128269;</div><p>未找到匹配的案例</p></div>';
    return;
  }}

  // 分批渲染，避免大量DOM操作卡顿
  const BATCH = 50;
  const total = cases.length;
  let html = '';

  const renderBatch = (start) => {{
    const end = Math.min(start + BATCH, total);
    for (let i = start; i < end; i++) {{
      html += buildCaseCard(cases[i]);
    }}
    if (end < total) {{
      requestAnimationFrame(() => renderBatch(end));
    }} else {{
      container.innerHTML = html;
    }}
  }};

  renderBatch(0);
}}

function buildCaseCard(c) {{
  const qualityClass = c._提取质量 === '完整' ? 'quality-complete' :
                       c._提取质量 === '部分' ? 'quality-partial' : 'quality-textonly';
  const qualityText = c._提取质量 || '未知';

  const focusHtml = (c.案件焦点 && c.案件焦点.length)
    ? '<ul>' + c.案件焦点.map(f => '<li>' + escapeHtml(f) + '</li>').join('') + '</ul>'
    : '<p style="color:#999">无</p>';

  const lawsHtml = (c.涉及法条 && c.涉及法条.length)
    ? '<div class="law-tags">' + c.涉及法条.map(l => '<span class="law-tag">' + escapeHtml(l) + '</span>').join('') + '</div>'
    : '<p style="color:#999">无</p>';

  const year = c.年份 || '';
  const vol = c.册号 ? String(c.册号).padStart(2, '0') : '00';
  const domain = c.领域 || '';
  const seqMatch = c.id ? c.id.match(/(\\d+)$/) : null;
  const seq = seqMatch ? seqMatch[1] : '001';
  const txtPath = '~/.claude/skills/shared/references/案例全文/' + year + '/' + vol + '-' + domain + '/' + seq + '.txt';

  return '<div class="case-card" onclick="toggleCard(this)">' +
    '<div class="case-header">' +
      '<span class="case-toggle">&#9654;</span>' +
      '<div class="case-info">' +
        '<span class="case-id">' + escapeHtml(c.id) + '</span>' +
        '<div class="case-title">' + escapeHtml(c.标题) + '</div>' +
        '<div class="case-meta">' +
          (c.裁判书字号 ? '<span>' + escapeHtml(c.裁判书字号) + '</span>' : '') +
          (c.案由 ? '<span class="tag">' + escapeHtml(c.案由) + '</span>' : '') +
          (c.法院 ? '<span>' + escapeHtml(c.法院) + '</span>' : '') +
          '<span class="quality-tag ' + qualityClass + '">' + qualityText + '</span>' +
        '</div>' +
      '</div>' +
    '</div>' +
    '<div class="case-detail">' +
      (c.当事人 ? '<div class="detail-section"><h4>当事人</h4><p>' + escapeHtml(c.当事人) + '</p></div>' : '') +
      (c.基本案情摘要 ? '<div class="detail-section"><h4>基本案情</h4><p>' + escapeHtml(c.基本案情摘要) + '</p></div>' : '') +
      '<div class="detail-section"><h4>案件焦点</h4>' + focusHtml + '</div>' +
      (c.裁判要旨 ? '<div class="detail-section"><h4>裁判要旨</h4><p>' + escapeHtml(c.裁判要旨) + '</p></div>' : '') +
      (c.法官后语摘要 ? '<div class="detail-section"><h4>法官后语</h4><p>' + escapeHtml(c.法官后语摘要) + '</p></div>' : '') +
      '<div class="detail-section"><h4>涉及法条</h4>' + lawsHtml + '</div>' +
      '<div class="detail-section"><h4>全文路径</h4>' +
        '<div class="path-box" onclick="event.stopPropagation(); copyPath(this)" title="点击复制路径">' +
          escapeHtml(txtPath) +
          '<span class="copy-hint">点击复制</span>' +
        '</div>' +
      '</div>' +
      (c.PDF来源 ? '<div class="detail-section" style="font-size:12px;color:#999">来源: ' + escapeHtml(c.PDF来源) + '，第' + escapeHtml(c.页码范围) + '页</div>' : '') +
    '</div>' +
  '</div>';
}}

function escapeHtml(str) {{
  if (!str) return '';
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}}

// 展开/折叠案例
function toggleCard(el) {{
  el.classList.toggle('open');
}}

// 领域导航点击
function selectDomain(el, domain) {{
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('domainFilter').value = domain;
  filterCases();
}}

function highlightNav() {{
  const domain = document.getElementById('domainFilter').value;
  document.querySelectorAll('.nav-item').forEach(n => {{
    n.classList.toggle('active', n.dataset.domain === domain);
  }});
}}

// 预计算搜索索引（启动时一次性拼接，避免每次搜索重复拼接）
const SEARCH_INDEX = ALL_CASES.map(c => {{
  return [
    c.标题, c.案由, c.裁判要旨, c.当事人, c.裁判书字号,
    c.基本案情摘要, c.法官后语摘要, c.法院,
    ...(c.案件焦点 || []),
    ...(c.涉及法条 || [])
  ].join(' ').toLowerCase();
}});

// 搜索防抖
function debouncedFilter() {{
  clearTimeout(searchTimer);
  searchTimer = setTimeout(filterCases, 200);
}}

// 筛选
function filterCases() {{
  const keyword = document.getElementById('searchInput').value.trim().toLowerCase();
  const year = document.getElementById('yearFilter').value;
  const domain = document.getElementById('domainFilter').value;

  filteredCases = ALL_CASES.filter((c, i) => {{
    if (year && String(c.年份) !== year) return false;
    if (domain && c.领域 !== domain) return false;
    if (keyword) {{
      return SEARCH_INDEX[i].includes(keyword);
    }}
    return true;
  }});

  document.getElementById('resultCount').textContent = filteredCases.length + ' 个案例';
  renderCases(filteredCases);
}}

// 复制路径
function copyPath(el) {{
  const text = el.textContent.replace('点击复制', '').trim();
  navigator.clipboard.writeText(text).then(() => {{
    const hint = el.querySelector('.copy-hint');
    hint.textContent = '已复制!';
    setTimeout(() => {{ hint.textContent = '点击复制'; }}, 1500);
  }}).catch(() => {{
    // 降级方案
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    const hint = el.querySelector('.copy-hint');
    hint.textContent = '已复制!';
    setTimeout(() => {{ hint.textContent = '点击复制'; }}, 1500);
  }});
}}

// 统计概览开关
function toggleOverview() {{
  const panel = document.getElementById('overviewPanel');
  panel.classList.toggle('show');
  if (panel.classList.contains('show') && !panel.dataset.rendered) {{
    renderOverview();
    panel.dataset.rendered = '1';
  }}
}}

// 渲染统计概览图表
function renderOverview() {{
  // 领域分布柱状图（含年份对比）
  const chartEl = document.getElementById('domainChart');
  const maxCount = Math.max(...DOMAIN_STATS.map(d => d.count));
  let chartHtml = '';
  DOMAIN_STATS.forEach(d => {{
    const yearData = DOMAIN_YEAR_STATS[d.name] || {{}};
    const c2024 = yearData['2024'] || 0;
    const c2025 = yearData['2025'] || 0;
    const w2024 = maxCount > 0 ? (c2024 / maxCount * 100) : 0;
    const w2025 = maxCount > 0 ? (c2025 / maxCount * 100) : 0;
    chartHtml += '<div class="bar-row">' +
      '<span class="bar-label" title="' + escapeHtml(d.name) + '">' + escapeHtml(d.name) + '</span>' +
      '<div class="bar-track">' +
        '<div class="bar-fill bar-fill-2024" style="width:' + w2024 + '%" title="2024: ' + c2024 + '"></div>' +
        '<div class="bar-fill bar-fill-2025" style="width:' + w2025 + '%" title="2025: ' + c2025 + '"></div>' +
      '</div>' +
      '<span class="bar-value">' + d.count + '</span>' +
    '</div>';
  }});
  chartEl.innerHTML = chartHtml;

  // 年份对比卡片
  const yearEl = document.getElementById('yearCompare');
  const sortedYears = Object.keys(YEAR_STATS).sort();
  let yearHtml = '';
  sortedYears.forEach(y => {{
    yearHtml += '<div class="year-card">' +
      '<div class="yc-year">' + y + '年</div>' +
      '<div class="yc-num">' + YEAR_STATS[y] + '</div>' +
      '<div class="yc-label">个案例</div>' +
    '</div>';
  }});
  yearEl.innerHTML = yearHtml;

  // 提取质量分布
  const qualityEl = document.getElementById('qualityChart');
  const total = ALL_CASES.length;
  const qCounts = {{}};
  ALL_CASES.forEach(c => {{
    const q = c._提取质量 || '未知';
    qCounts[q] = (qCounts[q] || 0) + 1;
  }});
  const qColors = {{'完整': 'var(--green)', '部分': 'var(--orange)', '仅全文': 'var(--red)'}};
  let qHtml = '<div style="display:flex;height:20px;border-radius:4px;overflow:hidden;margin-bottom:8px">';
  ['完整', '部分', '仅全文'].forEach(q => {{
    const n = qCounts[q] || 0;
    const pct = (n / total * 100).toFixed(1);
    if (n > 0) {{
      qHtml += '<div style="width:' + pct + '%;background:' + (qColors[q]||'#999') + '" title="' + q + ': ' + n + ' (' + pct + '%)"></div>';
    }}
  }});
  qHtml += '</div>';
  ['完整', '部分', '仅全文'].forEach(q => {{
    const n = qCounts[q] || 0;
    const pct = (n / total * 100).toFixed(1);
    qHtml += '<div style="font-size:12px;color:var(--text-light);margin-bottom:2px">' +
      '<span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:' + (qColors[q]||'#999') + ';vertical-align:middle;margin-right:6px"></span>' +
      q + ': ' + n + ' (' + pct + '%)' +
    '</div>';
  }});
  qualityEl.innerHTML = qHtml;
}}

// 返回顶部
function scrollToTop() {{
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}
window.addEventListener('scroll', () => {{
  const btn = document.getElementById('backToTop');
  btn.classList.toggle('visible', window.scrollY > 400);
}});

// 初始渲染
renderCases(ALL_CASES);
</script>
</body>
</html>"""

    # 写入文件
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"HTML报告生成完成: {output_path}")
    print(f"文件大小: {file_size:.2f} MB")
    print(f"案例总数: {total_cases}")
    print(f"领域数量: {len(sorted_domains)}")


def main():
    parser = argparse.ArgumentParser(description='中国法院年度案例参考库HTML报告生成器')
    parser.add_argument('--input',
                        default=os.path.expanduser('~/.claude/skills/shared/references/案例索引.json'),
                        help='案例索引JSON文件路径')
    parser.add_argument('--output',
                        default=os.path.expanduser('~/Library/CloudStorage/OneDrive-个人/桌面/Law-AI-帮助文档/中国法院年度案例参考库.html'),
                        help='输出HTML文件路径')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"错误: 索引文件不存在: {args.input}")
        sys.exit(1)

    print(f"读取索引: {args.input}")
    with open(args.input, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    generate_html(index_data, args.output)


if __name__ == '__main__':
    main()
