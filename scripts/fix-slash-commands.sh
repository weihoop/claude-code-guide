#!/bin/bash

# 批量为斜杠命令添加 disable-model-invocation: true
# 用途：减少上下文膨胀，只在命令被调用时加载内容

COMMANDS_DIR="$HOME/.claude/commands"

echo "开始更新斜杠命令配置..."
echo "命令目录: $COMMANDS_DIR"
echo ""

# 检查目录是否存在
if [ ! -d "$COMMANDS_DIR" ]; then
    echo "❌ 错误: 命令目录不存在: $COMMANDS_DIR"
    exit 1
fi

# 统计变量
total=0
updated=0
skipped=0

# 遍历所有 .md 文件
for file in "$COMMANDS_DIR"/*.md; do
    if [ ! -f "$file" ]; then
        continue
    fi

    filename=$(basename "$file")
    total=$((total + 1))

    # 检查文件是否已包含 disable-model-invocation
    if grep -q "disable-model-invocation:" "$file"; then
        echo "⏭️  跳过: $filename (已包含设置)"
        skipped=$((skipped + 1))
        continue
    fi

    # 检查文件是否有 YAML frontmatter
    if ! head -n 1 "$file" | grep -q "^---$"; then
        echo "⚠️  警告: $filename 缺少 YAML frontmatter，跳过"
        skipped=$((skipped + 1))
        continue
    fi

    # 创建临时文件
    tmpfile="${file}.tmp"

    # 读取文件并在 frontmatter 中添加 disable-model-invocation
    awk '
        BEGIN { in_frontmatter = 0; frontmatter_closed = 0; }
        NR == 1 && /^---$/ {
            print;
            in_frontmatter = 1;
            next;
        }
        in_frontmatter == 1 && /^---$/ {
            print "disable-model-invocation: true";
            print;
            frontmatter_closed = 1;
            in_frontmatter = 0;
            next;
        }
        { print; }
    ' "$file" > "$tmpfile"

    # 替换原文件
    mv "$tmpfile" "$file"

    echo "✅ 已更新: $filename"
    updated=$((updated + 1))
done

echo ""
echo "=============================="
echo "更新完成！"
echo "=============================="
echo "总文件数: $total"
echo "已更新: $updated"
echo "已跳过: $skipped"
echo ""

if [ $updated -gt 0 ]; then
    echo "建议: 重启 Claude Code 以使更改生效"
fi
