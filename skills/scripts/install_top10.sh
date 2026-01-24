#!/bin/bash

# ===============================================
# Claude Skills Top 10 一键安装脚本
#
# 功能：安装 10 个精选的 Claude Skills
# 维护：weihoop/claude-code-guide
# 更新：2026-01-24
# ===============================================

# 设置：遇到错误立即退出
set -e

# ===============================================
# 颜色定义（用于美化输出）
# ===============================================
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ===============================================
# 辅助函数
# ===============================================

# 打印标题
print_header() {
    echo -e "${CYAN}================================================${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}================================================${NC}"
    echo ""
}

# 打印成功消息
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

# 打印警告消息
print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# 打印错误消息
print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# 打印信息消息
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# 打印进度
print_progress() {
    local current=$1
    local total=$2
    local name=$3
    local percentage=$((current * 100 / total))
    echo -e "${PURPLE}[$current/$total] [$percentage%] 📦 $name${NC}"
}

# ===============================================
# 环境检查
# ===============================================

check_environment() {
    print_header "环境检查"

    # 检查 git 是否安装
    if ! command -v git &> /dev/null; then
        print_error "未找到 git 命令，请先安装 git"
        echo ""
        echo "安装方法："
        echo "  macOS:   brew install git"
        echo "  Ubuntu:  sudo apt install git"
        echo "  CentOS:  sudo yum install git"
        exit 1
    fi
    print_success "Git 已安装：$(git --version)"

    # 检查网络连接（尝试访问 GitHub）
    if ! curl -s --head --connect-timeout 5 https://github.com &> /dev/null; then
        print_warning "无法连接到 GitHub，请检查网络连接"
        echo ""
        read -p "是否继续安装？(y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    else
        print_success "网络连接正常"
    fi

    echo ""
}

# ===============================================
# 主安装函数
# ===============================================

install_skills() {
    print_header "开始安装 Top 10 Skills"

    # 创建 skills 目录
    SKILLS_DIR="$HOME/.config/claude-code/skills"
    mkdir -p "$SKILLS_DIR"
    cd "$SKILLS_DIR"

    print_info "Skills 安装目录: $SKILLS_DIR"
    echo ""

    # 总数和计数器
    local total=10
    local current=0
    local installed=0
    local skipped=0
    local failed=0

    # ===============================================
    # 1. NotebookLM
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "NotebookLM - AI 知识问答"
    if [ -d "notebooklm" ]; then
        print_warning "已存在，跳过"
        skipped=$((skipped + 1))
    else
        if git clone --depth 1 https://github.com/PleasePrompto/notebooklm-skill notebooklm 2>/dev/null; then
            print_success "安装完成"
            installed=$((installed + 1))
        else
            print_error "安装失败"
            failed=$((failed + 1))
        fi
    fi
    echo ""

    # ===============================================
    # 2. Obsidian Skills
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "Obsidian Skills - Markdown 和知识管理"
    if [ -d "obsidian" ]; then
        print_warning "已存在，跳过"
        skipped=$((skipped + 1))
    else
        if git clone --depth 1 https://github.com/kepano/obsidian-skills obsidian 2>/dev/null; then
            print_success "安装完成"
            installed=$((installed + 1))
        else
            print_error "安装失败"
            failed=$((failed + 1))
        fi
    fi
    echo ""

    # ===============================================
    # 3. Planning with Files
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "Planning with Files - 项目规划（Manus 工作流）"
    if [ -d "planning-with-files" ]; then
        print_warning "已存在，跳过"
        skipped=$((skipped + 1))
    else
        if git clone --depth 1 https://github.com/OthmanAdi/planning-with-files planning-with-files 2>/dev/null; then
            print_success "安装完成"
            installed=$((installed + 1))
        else
            print_error "安装失败"
            failed=$((failed + 1))
        fi
    fi
    echo ""

    # ===============================================
    # 4. Skill Creator
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "Skill Creator - 创建自定义 Skill"
    if [ -d "skill-creator" ]; then
        print_warning "已存在，跳过"
        skipped=$((skipped + 1))
    else
        print_info "从 awesome-claude-skills 仓库获取..."
        if git clone --depth 1 https://github.com/ComposioHQ/awesome-claude-skills temp_awesome 2>/dev/null; then
            cp -r temp_awesome/skill-creator ./
            rm -rf temp_awesome
            print_success "安装完成"
            installed=$((installed + 1))
        else
            print_error "安装失败"
            failed=$((failed + 1))
        fi
    fi
    echo ""

    # ===============================================
    # 5. Frontend Design
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "Frontend Design - 前端设计（避免 AI 通用美学）"
    if [ -d "frontend-design" ]; then
        print_warning "已存在，跳过"
        skipped=$((skipped + 1))
    else
        if git clone --depth 1 https://github.com/Koomook/claude-frontend-skills frontend-design 2>/dev/null; then
            print_success "安装完成"
            installed=$((installed + 1))
        else
            print_error "安装失败"
            failed=$((failed + 1))
        fi
    fi
    echo ""

    # ===============================================
    # 6. Superpowers
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "Superpowers - 开发工作流增强"
    if [ -d "superpowers" ]; then
        print_warning "已存在，跳过"
        skipped=$((skipped + 1))
    else
        if git clone --depth 1 https://github.com/obra/superpowers 2>/dev/null; then
            print_success "安装完成"
            installed=$((installed + 1))
        else
            print_error "安装失败"
            failed=$((failed + 1))
        fi
    fi
    echo ""

    # ===============================================
    # 7. Rube MCP（跳过，需要单独配置）
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "Rube MCP - 500+ 应用连接器"
    print_info "需要通过 MCP 命令单独安装（见下方说明）"
    skipped=$((skipped + 1))
    echo ""

    # ===============================================
    # 8. 宝玉 Skills
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "宝玉 Skills - 自媒体创作工具包"
    if [ -d "baoyu-skills" ]; then
        print_warning "已存在，跳过"
        skipped=$((skipped + 1))
    else
        if git clone --depth 1 https://github.com/JimLiu/baoyu-skills 2>/dev/null; then
            print_success "安装完成"
            installed=$((installed + 1))
        else
            print_error "安装失败"
            failed=$((failed + 1))
        fi
    fi
    echo ""

    # ===============================================
    # 9. 自媒体 Skills（使用 GuDaStudio）
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "自媒体 Skills - GuDaStudio 工具包"
    if [ -d "gudastudio" ]; then
        print_warning "已存在，跳过"
        skipped=$((skipped + 1))
    else
        if git clone --depth 1 https://github.com/GuDaStudio/skills gudastudio 2>/dev/null; then
            print_success "安装完成"
            installed=$((installed + 1))
        else
            print_error "安装失败"
            failed=$((failed + 1))
        fi
    fi
    echo ""

    # ===============================================
    # 10. Skill Lookup（使用 Skill Seekers）
    # ===============================================
    current=$((current + 1))
    print_progress $current $total "Skill Lookup - Skill 发现和转换工具"
    if [ -d "skill-seekers" ]; then
        print_warning "已存在，跳过"
        skipped=$((skipped + 1))
    else
        if git clone --depth 1 https://github.com/yusufkaraaslan/Skill_Seekers skill-seekers 2>/dev/null; then
            print_success "安装完成"
            installed=$((installed + 1))
        else
            print_error "安装失败"
            failed=$((failed + 1))
        fi
    fi
    echo ""

    # ===============================================
    # 安装总结
    # ===============================================
    print_header "安装总结"

    echo -e "${GREEN}✅ 成功安装: $installed 个${NC}"
    echo -e "${YELLOW}⚠️  跳过（已存在）: $skipped 个${NC}"
    if [ $failed -gt 0 ]; then
        echo -e "${RED}❌ 安装失败: $failed 个${NC}"
    fi
    echo ""

    print_info "已安装的 Skills："
    ls -1 "$SKILLS_DIR" 2>/dev/null | sed 's/^/  - /' || echo "  无"
    echo ""
}

# ===============================================
# 后续操作提示
# ===============================================

show_next_steps() {
    print_header "后续操作"

    echo "⚠️  以下 Skills 需要单独配置："
    echo ""

    echo -e "${CYAN}7️⃣  Rube MCP Connector${NC} (连接 500+ 应用):"
    echo "   ${YELLOW}claude mcp add --transport http rube -s user 'https://rube.app/mcp'${NC}"
    echo ""

    echo -e "${CYAN}6️⃣  Superpowers 插件市场版本${NC} (推荐，自动更新):"
    echo "   在 Claude Code 中执行："
    echo "   ${YELLOW}/plugin marketplace add obra/superpowers-marketplace${NC}"
    echo "   ${YELLOW}/plugin install superpowers@superpowers-marketplace${NC}"
    echo ""

    print_header "验证安装"

    echo "1️⃣  查看已安装的 Skills："
    echo "   ${YELLOW}ls -la ~/.config/claude-code/skills/${NC}"
    echo ""

    echo "2️⃣  验证某个 Skill："
    echo "   ${YELLOW}head ~/.config/claude-code/skills/notebooklm/SKILL.md${NC}"
    echo ""

    echo "3️⃣  启动 Claude Code："
    echo "   ${YELLOW}claude${NC}"
    echo ""

    print_header "参考资源"

    echo "📚 文档："
    echo "  - Top 10 详细指南: https://github.com/weihoop/claude-code-guide/tree/main/skills/top-10"
    echo "  - Skills 主页: https://github.com/weihoop/claude-code-guide/tree/main/skills"
    echo "  - Claude 官方文档: https://code.claude.com/docs/zh-CN/skills"
    echo ""

    echo "🔗 GitHub 仓库："
    echo "  - awesome-claude-skills: https://github.com/ComposioHQ/awesome-claude-skills"
    echo "  - Anthropic 官方: https://github.com/anthropics/skills"
    echo ""
}

# ===============================================
# 主函数
# ===============================================

main() {
    # 打印欢迎信息
    echo ""
    print_header "Claude Skills Top 10 一键安装脚本"
    echo -e "${BLUE}版本: 1.0.0${NC}"
    echo -e "${BLUE}维护: weihoop/claude-code-guide${NC}"
    echo -e "${BLUE}更新: 2026-01-24${NC}"
    echo ""

    # 环境检查
    check_environment

    # 安装 Skills
    install_skills

    # 显示后续操作
    show_next_steps

    # 完成
    print_header "安装完成"
    echo -e "${GREEN}🎉 恭喜！Top 10 Skills 安装完成！${NC}"
    echo -e "${GREEN}现在可以启动 Claude Code 体验这些强大的 Skills 了！${NC}"
    echo ""
}

# ===============================================
# 执行主函数
# ===============================================

main
