#!/bin/bash

# ============================================================================
# Claude Code 官方 Skills 安装脚本
# ============================================================================
# 功能：一键安装 Anthropic 官方 Skills（docx、pdf、pptx、xlsx）
# 版本：1.0.0
# 更新：2026-01-26
# ============================================================================

set -e  # 遇到错误立即退出

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Skills 安装目录
SKILLS_DIR="${HOME}/.claude/skills"

# 官方 Skills 仓库
OFFICIAL_REPO="https://github.com/anthropics/skills.git"

# 需要安装的官方 Skills
OFFICIAL_SKILLS=("docx" "pdf" "pptx" "xlsx")

# ============================================================================
# 辅助函数
# ============================================================================

print_header() {
    echo -e "${BLUE}======================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}======================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# ============================================================================
# 主要功能
# ============================================================================

# 检查 Git 是否安装
check_git() {
    if ! command -v git &> /dev/null; then
        print_error "Git 未安装。请先安装 Git。"
        exit 1
    fi
    print_success "Git 已安装"
}

# 创建 Skills 目录
create_skills_dir() {
    if [ ! -d "$SKILLS_DIR" ]; then
        print_info "创建 Skills 目录: $SKILLS_DIR"
        mkdir -p "$SKILLS_DIR"
    fi
    print_success "Skills 目录已就绪"
}

# 克隆官方仓库到临时目录
clone_official_repo() {
    local temp_dir="/tmp/claude-official-skills-$$"

    print_info "克隆官方 Skills 仓库..."
    if git clone --depth 1 "$OFFICIAL_REPO" "$temp_dir" &> /dev/null; then
        print_success "官方仓库克隆成功"
        echo "$temp_dir"
    else
        print_error "克隆官方仓库失败"
        exit 1
    fi
}

# 安装单个官方 Skill
install_skill() {
    local skill_name=$1
    local temp_dir=$2
    local source_path="${temp_dir}/skills/${skill_name}"
    local target_path="${SKILLS_DIR}/${skill_name}"

    # 检查源路径是否存在
    if [ ! -d "$source_path" ]; then
        print_warning "Skill '${skill_name}' 在官方仓库中不存在"
        return 1
    fi

    # 检查目标路径
    if [ -d "$target_path" ]; then
        print_warning "Skill '${skill_name}' 已存在，跳过安装"
        return 0
    fi

    # 复制 Skill
    print_info "安装 ${skill_name}..."
    if cp -r "$source_path" "$target_path"; then
        print_success "Skill '${skill_name}' 安装成功"
        return 0
    else
        print_error "Skill '${skill_name}' 安装失败"
        return 1
    fi
}

# 验证安装
verify_installation() {
    local skill_name=$1
    local skill_path="${SKILLS_DIR}/${skill_name}"

    if [ -f "${skill_path}/SKILL.md" ]; then
        print_success "${skill_name} - 验证通过"
        return 0
    else
        print_error "${skill_name} - 验证失败"
        return 1
    fi
}

# 清理临时文件
cleanup() {
    local temp_dir=$1
    if [ -d "$temp_dir" ]; then
        rm -rf "$temp_dir"
        print_info "清理临时文件"
    fi
}

# ============================================================================
# 主程序
# ============================================================================

main() {
    print_header "Claude Code 官方 Skills 安装程序"

    echo ""
    print_info "将要安装的官方 Skills："
    for skill in "${OFFICIAL_SKILLS[@]}"; do
        echo "  - $skill"
    done
    echo ""

    # 检查 Git
    check_git

    # 创建 Skills 目录
    create_skills_dir

    # 克隆官方仓库
    temp_dir=$(clone_official_repo)

    # 安装 Skills
    echo ""
    print_header "开始安装 Skills"

    local success_count=0
    local total_count=${#OFFICIAL_SKILLS[@]}

    for skill in "${OFFICIAL_SKILLS[@]}"; do
        if install_skill "$skill" "$temp_dir"; then
            ((success_count++))
        fi
    done

    # 清理临时文件
    cleanup "$temp_dir"

    # 验证安装
    echo ""
    print_header "验证安装"

    for skill in "${OFFICIAL_SKILLS[@]}"; do
        if [ -d "${SKILLS_DIR}/${skill}" ]; then
            verify_installation "$skill"
        fi
    done

    # 显示安装总结
    echo ""
    print_header "安装总结"

    echo -e "${GREEN}成功安装 ${success_count}/${total_count} 个官方 Skills${NC}"
    echo ""

    if [ $success_count -eq $total_count ]; then
        print_success "所有官方 Skills 安装完成！"
        echo ""
        print_info "Skills 安装位置: ${SKILLS_DIR}"
        print_info "重启 Claude Code 以使用新安装的 Skills"
    else
        print_warning "部分 Skills 安装失败，请检查错误信息"
    fi

    echo ""
}

# 运行主程序
main

exit 0
