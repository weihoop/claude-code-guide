#!/bin/bash
################################################################################
# Skills 验证脚本
#
# 功能: 验证已安装的 Skills 是否正确配置
# 用法: bash verify_skills.sh [--fix]
# 选项:
#   --fix  尝试自动修复发现的问题
################################################################################

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 默认 Skills 目录
SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.config/claude-code/skills}"
FIX_MODE=false

# 解析命令行参数
if [[ "$1" == "--fix" ]]; then
    FIX_MODE=true
fi

# 统计变量
TOTAL_SKILLS=0
VALID_SKILLS=0
INVALID_SKILLS=0
WARNING_SKILLS=0

################################################################################
# 辅助函数
################################################################################

print_header() {
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${PURPLE}  Claude Skills 验证工具${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_section() {
    echo ""
    echo -e "${CYAN}▶ $1${NC}"
    echo -e "${CYAN}───────────────────────────────────────────────────────────${NC}"
}

################################################################################
# 验证函数
################################################################################

# 验证 Skills 目录
check_skills_directory() {
    print_section "检查 Skills 目录"

    if [ ! -d "$SKILLS_DIR" ]; then
        print_error "Skills 目录不存在: $SKILLS_DIR"

        if $FIX_MODE; then
            print_info "正在创建 Skills 目录..."
            mkdir -p "$SKILLS_DIR"
            if [ $? -eq 0 ]; then
                print_success "Skills 目录已创建"
            else
                print_error "创建失败，请检查权限"
                return 1
            fi
        else
            print_info "运行 'verify_skills.sh --fix' 自动创建"
            return 1
        fi
    else
        print_success "Skills 目录存在: $SKILLS_DIR"
    fi

    # 检查目录权限
    if [ ! -r "$SKILLS_DIR" ]; then
        print_error "Skills 目录不可读"
        return 1
    fi

    if [ ! -w "$SKILLS_DIR" ]; then
        print_warning "Skills 目录不可写（可能影响安装新 Skills）"
    fi

    return 0
}

# 验证单个 Skill
validate_skill() {
    local skill_path="$1"
    local skill_name=$(basename "$skill_path")

    echo ""
    echo -e "${BLUE}📦 检查: $skill_name${NC}"

    local has_error=false
    local has_warning=false

    # 1. 检查 SKILL.md 是否存在
    if [ ! -f "$skill_path/SKILL.md" ]; then
        print_error "缺少 SKILL.md 文件"
        has_error=true
    else
        print_success "SKILL.md 存在"

        # 2. 检查 YAML frontmatter
        if ! head -1 "$skill_path/SKILL.md" | grep -q "^---$"; then
            print_error "SKILL.md 缺少 YAML frontmatter（必须以 '---' 开头）"
            has_error=true
        else
            print_success "YAML frontmatter 格式正确"

            # 3. 检查 description 字段
            if ! grep -q "^description:" "$skill_path/SKILL.md"; then
                print_error "SKILL.md 缺少 'description' 字段"
                has_error=true
            else
                print_success "包含 description 字段"
            fi
        fi

        # 4. 检查文件大小（建议 < 100KB）
        local file_size=$(wc -c < "$skill_path/SKILL.md")
        if [ $file_size -gt 102400 ]; then
            print_warning "SKILL.md 文件较大（$(($file_size / 1024))KB），建议 < 100KB"
            has_warning=true
        fi
    fi

    # 5. 检查是否为 Git 仓库
    if [ -d "$skill_path/.git" ]; then
        print_success "Git 仓库（可更新）"

        # 检查远程仓库
        cd "$skill_path"
        if git remote -v &>/dev/null; then
            local remote_url=$(git remote get-url origin 2>/dev/null)
            if [ -n "$remote_url" ]; then
                print_info "远程仓库: $remote_url"
            fi
        fi
    else
        print_warning "非 Git 仓库（无法自动更新）"
        has_warning=true
    fi

    # 6. 检查常见可选文件
    if [ -f "$skill_path/README.md" ]; then
        print_success "包含 README.md"
    else
        print_info "未找到 README.md（可选）"
    fi

    # 统计结果
    if $has_error; then
        INVALID_SKILLS=$((INVALID_SKILLS + 1))
        echo -e "${RED}❌ $skill_name: 验证失败${NC}"
    elif $has_warning; then
        WARNING_SKILLS=$((WARNING_SKILLS + 1))
        echo -e "${YELLOW}⚠️  $skill_name: 有警告${NC}"
    else
        VALID_SKILLS=$((VALID_SKILLS + 1))
        echo -e "${GREEN}✅ $skill_name: 验证通过${NC}"
    fi
}

# 检查所有 Skills
check_all_skills() {
    print_section "扫描已安装的 Skills"

    local skill_count=0

    # 扫描目录
    for skill_path in "$SKILLS_DIR"/*; do
        if [ -d "$skill_path" ]; then
            skill_count=$((skill_count + 1))
            validate_skill "$skill_path"
        fi
    done

    TOTAL_SKILLS=$skill_count

    if [ $skill_count -eq 0 ]; then
        print_warning "未发现任何 Skills"
        print_info "运行以下命令安装 Top 10 推荐 Skills:"
        echo ""
        echo "  bash install_top10.sh"
        echo ""
    fi
}

# 生成总结报告
print_summary() {
    print_section "验证总结"

    echo ""
    echo -e "${PURPLE}统计结果:${NC}"
    echo -e "  总 Skills 数: ${BLUE}$TOTAL_SKILLS${NC}"
    echo -e "  ✅ 验证通过: ${GREEN}$VALID_SKILLS${NC}"
    echo -e "  ⚠️  有警告: ${YELLOW}$WARNING_SKILLS${NC}"
    echo -e "  ❌ 验证失败: ${RED}$INVALID_SKILLS${NC}"
    echo ""

    # 计算健康度
    if [ $TOTAL_SKILLS -gt 0 ]; then
        local health_percent=$(( (VALID_SKILLS * 100) / TOTAL_SKILLS ))

        if [ $health_percent -eq 100 ]; then
            echo -e "${GREEN}🎉 所有 Skills 都配置正确！${NC}"
        elif [ $health_percent -ge 80 ]; then
            echo -e "${GREEN}👍 Skills 配置良好（健康度: ${health_percent}%）${NC}"
        elif [ $health_percent -ge 60 ]; then
            echo -e "${YELLOW}⚠️  部分 Skills 有问题（健康度: ${health_percent}%）${NC}"
        else
            echo -e "${RED}❌ 多个 Skills 配置有误（健康度: ${health_percent}%）${NC}"
        fi
    fi

    echo ""
}

# 提供修复建议
print_recommendations() {
    if [ $INVALID_SKILLS -gt 0 ] || [ $WARNING_SKILLS -gt 0 ]; then
        print_section "修复建议"

        echo ""
        echo "常见问题修复方法:"
        echo ""

        if [ $INVALID_SKILLS -gt 0 ]; then
            echo "1. 缺少 SKILL.md 或格式错误:"
            echo "   - 检查 Skill 是否完整安装"
            echo "   - 重新克隆 Skill 仓库"
            echo "   - 参考官方模板创建 SKILL.md"
            echo ""
        fi

        if [ $WARNING_SKILLS -gt 0 ]; then
            echo "2. 非 Git 仓库警告:"
            echo "   - 建议使用 git clone 安装 Skills"
            echo "   - 这样可以方便地更新 Skills"
            echo ""

            echo "3. 文件过大警告:"
            echo "   - 将详细内容移到 references/ 目录"
            echo "   - SKILL.md 保持简洁（< 100KB）"
            echo ""
        fi

        echo "更多帮助:"
        echo "  - 安装指南: https://github.com/weihoop/claude-code-guide/blob/main/skills/installation-guide.md"
        echo "  - 故障排除: https://github.com/weihoop/claude-code-guide/blob/main/skills/guides/troubleshooting.md"
        echo ""
    fi
}

# 检查 Claude Code 环境
check_claude_environment() {
    print_section "检查 Claude Code 环境"

    # 检查 Claude Code 是否安装
    if command -v claude &> /dev/null; then
        local claude_version=$(claude --version 2>/dev/null)
        print_success "Claude Code 已安装: $claude_version"
    else
        print_warning "未检测到 Claude Code CLI"
        print_info "访问 https://code.claude.com/docs/getting-started 安装"
    fi

    # 检查 Git
    if command -v git &> /dev/null; then
        local git_version=$(git --version | cut -d' ' -f3)
        print_success "Git 已安装: $git_version"
    else
        print_error "未安装 Git（安装 Skills 需要 Git）"
    fi
}

################################################################################
# 主函数
################################################################################

main() {
    print_header

    # 检查环境
    check_claude_environment

    # 检查目录
    if ! check_skills_directory; then
        exit 1
    fi

    # 检查所有 Skills
    check_all_skills

    # 打印总结
    print_summary

    # 打印建议
    print_recommendations

    # 返回状态码
    if [ $INVALID_SKILLS -gt 0 ]; then
        exit 1
    else
        exit 0
    fi
}

# 运行主函数
main
