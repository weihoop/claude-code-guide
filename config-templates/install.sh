#!/bin/bash

#==============================================================================
# Claude Code 配置安装脚本
# 用途: 自动安装 Claude Code 配置到 ~/.claude/
# 版本: 1.0.0
#==============================================================================

set -e  # 遇到错误立即退出

# 配置变量
CLAUDE_DIR="$HOME/.claude"
BACKUP_TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_DIR="$CLAUDE_DIR/backup-$BACKUP_TIMESTAMP"
LOG_FILE="$CLAUDE_DIR/install.log"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

#==============================================================================
# 日志函数
#==============================================================================

log_to_file() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

info() {
    echo -e "${BLUE}[INFO]${NC} $1"
    log_to_file "INFO: $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
    log_to_file "SUCCESS: $1"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
    log_to_file "WARNING: $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    log_to_file "ERROR: $1"
    exit 1
}

print_header() {
    echo ""
    echo "======================================================================"
    echo -e "  ${CYAN}Claude Code 配置安装脚本 v1.0.0${NC}"
    echo "======================================================================"
    echo ""
}

print_usage_info() {
    echo -e "${CYAN}📋 本脚本将执行以下操作:${NC}"
    echo ""
    echo "  1️⃣  检查现有配置文件"
    echo "  2️⃣  自动备份现有配置（如果存在）"
    echo "  3️⃣  让你选择配置版本（精简版/完整版）"
    echo "  4️⃣  安装新配置到 ~/.claude/"
    echo "  5️⃣  记录安装日志到 ~/.claude/install.log"
    echo ""
    echo -e "${YELLOW}⚠️  文件覆盖说明:${NC}"
    echo ""
    echo -e "  ${RED}会被覆盖的文件:${NC}"
    echo "    • settings.json      - 权限配置文件"
    echo "    • commands/*.md      - 8个标准斜杠命令"
    echo ""
    echo -e "  ${GREEN}不会被覆盖的文件:${NC}"
    echo "    • CLAUDE.md          - 如果已存在，保持不变"
    echo "    • 自定义命令         - 不同文件名的命令会保留"
    echo ""
    echo -e "${CYAN}🛡️  备份机制:${NC}"
    echo ""
    echo "    所有现有配置会自动备份到:"
    echo "    ~/.claude/backup-YYYYMMDD-HHMMSS/"
    echo ""
    echo "    恢复命令:"
    echo "    cp -r ~/.claude/backup-YYYYMMDD-HHMMSS/* ~/.claude/"
    echo ""
    echo -e "${CYAN}📝 安装日志:${NC}"
    echo ""
    echo "    所有操作记录到: ~/.claude/install.log"
    echo ""
    echo "======================================================================"
    echo ""

    read -p "按 Enter 继续，或按 Ctrl+C 取消安装..."
    echo ""
}

#==============================================================================
# 环境检查
#==============================================================================

check_environment() {
    info "检查安装环境..."

    # 创建 .claude 目录（如果不存在）
    if [ ! -d "$CLAUDE_DIR" ]; then
        mkdir -p "$CLAUDE_DIR"
        info "创建配置目录: $CLAUDE_DIR"
    fi

    # 检查必需文件
    local missing_files=()

    if [ ! -f "$SCRIPT_DIR/settings.simple.json" ]; then
        missing_files+=("settings.simple.json")
    fi

    if [ ! -f "$SCRIPT_DIR/settings.full.json" ]; then
        missing_files+=("settings.full.json")
    fi

    if [ ! -d "$SCRIPT_DIR/commands" ]; then
        missing_files+=("commands/")
    fi

    if [ ${#missing_files[@]} -gt 0 ]; then
        error "缺少必需文件: ${missing_files[*]}"
    fi

    success "环境检查通过"
}

#==============================================================================
# 备份现有配置
#==============================================================================

backup_existing_config() {
    info "检查现有配置..."

    local files_to_backup=(
        "settings.json"
        "CLAUDE.md"
        "commands"
    )

    local need_backup=false
    local backup_list=()

    # 检查哪些文件需要备份
    for item in "${files_to_backup[@]}"; do
        if [ -e "$CLAUDE_DIR/$item" ]; then
            need_backup=true
            backup_list+=("$item")
        fi
    done

    if [ "$need_backup" = true ]; then
        echo ""
        echo -e "${YELLOW}检测到现有配置文件:${NC}"
        for item in "${backup_list[@]}"; do
            echo "  - $item"
        done
        echo ""
        echo -e "${CYAN}这些文件将被备份到:${NC}"
        echo "  $BACKUP_DIR"
        echo ""
        read -p "是否继续安装？(y/n): " confirm

        if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
            info "安装已取消"
            exit 0
        fi

        # 创建备份目录
        mkdir -p "$BACKUP_DIR"
        info "创建备份目录: $BACKUP_DIR"

        # 备份文件
        for item in "${backup_list[@]}"; do
            if [ -e "$CLAUDE_DIR/$item" ]; then
                cp -r "$CLAUDE_DIR/$item" "$BACKUP_DIR/"
                info "已备份: $item"
                log_to_file "BACKUP: $item -> $BACKUP_DIR/$item"
            fi
        done

        success "配置备份完成"

        # 记录备份清单到日志
        echo "" >> "$LOG_FILE"
        echo "=== 备份清单 ===" >> "$LOG_FILE"
        echo "备份时间: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
        echo "备份目录: $BACKUP_DIR" >> "$LOG_FILE"
        echo "备份文件:" >> "$LOG_FILE"
        for item in "${backup_list[@]}"; do
            echo "  - $item" >> "$LOG_FILE"
        done
        echo "===============" >> "$LOG_FILE"
        echo "" >> "$LOG_FILE"

    else
        info "未检测到现有配置，跳过备份"
    fi
}

#==============================================================================
# 选择配置版本
#==============================================================================

select_settings_version() {
    echo ""
    echo "======================================================================"
    echo -e "${CYAN}请选择配置版本:${NC}"
    echo "======================================================================"
    echo ""
    echo "  1) 精简版 (settings.simple.json) - 推荐新手"
    echo "     - 11 条 allow 规则"
    echo "     - 基础文件操作 + Git + 网络搜索"
    echo "     - 简单易用，安全性高"
    echo ""
    echo "  2) 完整版 (settings.full.json) - 进阶用户"
    echo "     - 111 条 allow 规则"
    echo "     - 57 条 deny 规则（禁止危险操作）"
    echo "     - 62 条 ask 规则（敏感操作需确认）"
    echo "     - 功能全面，精细控制"
    echo ""
    echo "  3) 取消安装"
    echo ""

    while true; do
        read -p "请输入选择 [1/2/3]: " choice
        case $choice in
            1)
                SELECTED_SETTINGS="settings.simple.json"
                SETTINGS_VERSION="精简版"
                break
                ;;
            2)
                SELECTED_SETTINGS="settings.full.json"
                SETTINGS_VERSION="完整版"
                break
                ;;
            3)
                info "安装已取消"
                exit 0
                ;;
            *)
                echo -e "${RED}无效选择，请输入 1、2 或 3${NC}"
                ;;
        esac
    done

    info "已选择: $SETTINGS_VERSION"
    log_to_file "SELECTED: $SETTINGS_VERSION ($SELECTED_SETTINGS)"
}

#==============================================================================
# 安装配置文件
#==============================================================================

install_settings() {
    info "安装 settings.json ($SETTINGS_VERSION)..."

    cp "$SCRIPT_DIR/$SELECTED_SETTINGS" "$CLAUDE_DIR/settings.json"
    chmod 644 "$CLAUDE_DIR/settings.json"

    success "settings.json 安装完成"
    log_to_file "INSTALL: settings.json ($SELECTED_SETTINGS)"
}

install_commands() {
    info "安装斜杠命令..."

    # 创建 commands 目录
    mkdir -p "$CLAUDE_DIR/commands"

    # 复制所有命令文件
    local cmd_count=0
    for cmd_file in "$SCRIPT_DIR/commands/"*.md; do
        if [ -f "$cmd_file" ]; then
            cp "$cmd_file" "$CLAUDE_DIR/commands/"
            chmod 600 "$CLAUDE_DIR/commands/$(basename "$cmd_file")"
            cmd_count=$((cmd_count + 1))
            log_to_file "INSTALL: commands/$(basename "$cmd_file")"
        fi
    done

    success "已安装 $cmd_count 个斜杠命令"
}

install_claude_md() {
    info "检查 CLAUDE.md..."

    # 如果用户已有 CLAUDE.md，不覆盖
    if [ -f "$CLAUDE_DIR/CLAUDE.md" ]; then
        warning "CLAUDE.md 已存在，跳过安装（已在备份中保存）"
        log_to_file "SKIP: CLAUDE.md (already exists)"
    else
        echo ""
        read -p "是否安装 CLAUDE.md 模板？(y/n): " install_template

        if [ "$install_template" = "y" ] || [ "$install_template" = "Y" ]; then
            cp "$SCRIPT_DIR/CLAUDE.template.md" "$CLAUDE_DIR/CLAUDE.md"
            chmod 644 "$CLAUDE_DIR/CLAUDE.md"
            success "CLAUDE.md 模板安装完成"
            log_to_file "INSTALL: CLAUDE.md (from template)"
            info "你可以编辑 $CLAUDE_DIR/CLAUDE.md 自定义配置"
        else
            info "跳过 CLAUDE.md 安装"
            log_to_file "SKIP: CLAUDE.md (user choice)"
        fi
    fi
}

#==============================================================================
# 显示安装结果
#==============================================================================

show_installation_summary() {
    echo ""
    echo "======================================================================"
    success "Claude Code 配置安装完成！"
    echo "======================================================================"
    echo ""

    echo -e "${CYAN}安装信息:${NC}"
    echo "  配置版本: $SETTINGS_VERSION"
    echo "  安装目录: $CLAUDE_DIR"
    echo ""

    echo -e "${CYAN}已安装的文件:${NC}"
    echo "  ✓ settings.json - 权限配置文件 ($SETTINGS_VERSION)"

    if [ -d "$CLAUDE_DIR/commands" ]; then
        local cmd_count=$(ls -1 "$CLAUDE_DIR/commands/"*.md 2>/dev/null | wc -l | tr -d ' ')
        echo "  ✓ commands/ - 自定义命令目录 ($cmd_count 个命令)"
    fi

    if [ -f "$CLAUDE_DIR/CLAUDE.md" ]; then
        echo "  ✓ CLAUDE.md - 全局配置文件"
    fi

    if [ -d "$BACKUP_DIR" ]; then
        echo ""
        echo -e "${CYAN}备份信息:${NC}"
        echo "  备份目录: $BACKUP_DIR"
        echo "  恢复命令: cp -r $BACKUP_DIR/* $CLAUDE_DIR/"
    fi

    echo ""
    echo -e "${CYAN}日志文件:${NC}"
    echo "  $LOG_FILE"
    echo ""

    echo -e "${CYAN}可用的斜杠命令:${NC}"
    echo "  /test    - 运行测试并智能分析结果"
    echo "  /review  - 完整的代码审查流程"
    echo "  /build   - 构建项目并检查错误和警告"
    echo "  /push    - 一键提交并推送代码到远程仓库"
    echo "  /fix     - 自动修复常见的代码问题"
    echo "  /update  - 智能更新项目依赖"
    echo "  /deploy  - 自动化部署到指定环境"
    echo "  /doc     - 智能更新项目文档"
    echo ""

    echo -e "${CYAN}下一步:${NC}"
    echo "  1. 重启 Claude Code (如果正在运行)"
    echo "     $ exit  # 退出当前会话"
    echo "     $ claude  # 重新启动"
    echo ""
    echo "  2. 在任意项目中使用 Claude Code"
    echo "     $ cd your-project"
    echo "     $ claude"
    echo ""
    echo "  3. 尝试使用斜杠命令"
    echo "     > /test"
    echo "     > /review"
    echo ""
    echo "  4. 自定义配置 (可选)"
    echo "     $ vim $CLAUDE_DIR/settings.json"
    echo "     $ vim $CLAUDE_DIR/CLAUDE.md"
    echo ""

    echo "======================================================================"
    echo ""

    # 记录安装摘要到日志
    echo "" >> "$LOG_FILE"
    echo "=== 安装摘要 ===" >> "$LOG_FILE"
    echo "安装时间: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
    echo "配置版本: $SETTINGS_VERSION ($SELECTED_SETTINGS)" >> "$LOG_FILE"
    echo "安装目录: $CLAUDE_DIR" >> "$LOG_FILE"
    if [ -d "$BACKUP_DIR" ]; then
        echo "备份目录: $BACKUP_DIR" >> "$LOG_FILE"
    fi
    echo "安装状态: SUCCESS" >> "$LOG_FILE"
    echo "================" >> "$LOG_FILE"
}

#==============================================================================
# 错误处理
#==============================================================================

handle_error() {
    echo ""
    error "安装过程中发生错误，请查看日志: $LOG_FILE"
    log_to_file "INSTALL FAILED: An error occurred during installation"
    exit 1
}

trap handle_error ERR

#==============================================================================
# 主流程
#==============================================================================

main() {
    # 初始化日志
    echo "" >> "$LOG_FILE"
    echo "================================================" >> "$LOG_FILE"
    echo "安装开始: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
    echo "================================================" >> "$LOG_FILE"

    print_header
    print_usage_info

    # 执行安装步骤
    check_environment
    backup_existing_config
    select_settings_version

    echo ""
    info "开始安装配置文件..."
    echo ""

    install_settings
    install_commands
    install_claude_md

    # 显示安装结果
    show_installation_summary

    success "安装完成！祝使用愉快！ 🎉"
}

# 执行主函数
main
