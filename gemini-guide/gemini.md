
Gemini CLI 目前**没有内置的代码仓库记忆功能**，但可以通过以下几种方式来实现类似效果：

## 1. **使用上下文文件 (推荐)**

### 创建项目上下文文件
```bash
# 创建项目描述文件
cat > .gemini-context.md << 'EOF'
# 项目上下文

## 项目结构
```
my-project/
├── src/
│   ├── components/
│   ├── utils/
│   └── main.js
├── package.json
└── README.md
```

## 技术栈
- Node.js + Express
- React + TypeScript
- PostgreSQL
- Docker

## 关键文件说明
- `src/main.js`: 应用入口
- `src/components/`: React组件
- `package.json`: 依赖管理
EOF

# 每次询问时包含上下文
gemini "请基于以下项目上下文回答问题：

$(cat .gemini-context.md)

问题：如何优化这个React组件？"
```

## 2. **使用脚本自动收集代码信息**

```bash
#!/bin/bash
# save as: gemini-with-context.sh

PROJECT_ROOT=$(pwd)
CONTEXT_FILE="/tmp/gemini-context-$(basename $PROJECT_ROOT).txt"

# 生成项目上下文
generate_context() {
    echo "=== 项目信息 ===" > $CONTEXT_FILE
    echo "项目路径: $PROJECT_ROOT" >> $CONTEXT_FILE
    echo "最后更新: $(date)" >> $CONTEXT_FILE
    echo "" >> $CONTEXT_FILE

    echo "=== 项目结构 ===" >> $CONTEXT_FILE
    tree -L 3 -I 'node_modules|.git|dist|build' >> $CONTEXT_FILE 2>/dev/null || ls -la >> $CONTEXT_FILE
    echo "" >> $CONTEXT_FILE

    echo "=== package.json ===" >> $CONTEXT_FILE
    if [ -f "package.json" ]; then
        cat package.json >> $CONTEXT_FILE
    fi
    echo "" >> $CONTEXT_FILE

    echo "=== README.md ===" >> $CONTEXT_FILE
    if [ -f "README.md" ]; then
        head -50 README.md >> $CONTEXT_FILE
    fi
    echo "" >> $CONTEXT_FILE
}

# 使用方式
if [ "$1" = "--update-context" ]; then
    generate_context
    echo "上下文已更新: $CONTEXT_FILE"
elif [ -z "$1" ]; then
    echo "用法: $0 '你的问题' 或 $0 --update-context"
else
    # 如果上下文文件不存在或过期，自动生成
    if [ ! -f "$CONTEXT_FILE" ] || [ $(find "$CONTEXT_FILE" -mmin +60 2>/dev/null | wc -l) -eq 1 ]; then
        generate_context
    fi

    # 发送带上下文的问题
    gemini "基于以下项目上下文：

$(cat $CONTEXT_FILE)

问题：$1"
fi
```

使用方式：
```bash
chmod +x gemini-with-context.sh

# 更新项目上下文
./gemini-with-context.sh --update-context

# 询问问题（自动包含上下文）
./gemini-with-context.sh "这个项目如何添加用户认证功能？"
```

## 3. **使用环境变量存储常用信息**

```bash
# 在 ~/.bashrc 或 ~/.zshrc 中添加
export CURRENT_PROJECT_CONTEXT="
项目：我的React应用
技术栈：React+TypeScript+Node.js
数据库：PostgreSQL
部署：Docker+Nginx
"

# 创建别名
alias gask='gemini "项目上下文：$CURRENT_PROJECT_CONTEXT\n\n问题："'

# 使用
gask "如何优化数据库查询性能？"
```

## 4. **使用配置文件管理多个项目**

```bash
# ~/.gemini-projects.json
{
  "my-react-app": {
    "path": "/home/user/projects/my-react-app",
    "tech_stack": ["React", "TypeScript", "Node.js"],
    "description": "电商前端应用",
    "key_files": ["src/App.tsx", "package.json", "README.md"]
  },
  "api-server": {
    "path": "/home/user/projects/api-server",
    "tech_stack": ["Node.js", "Express", "PostgreSQL"],
    "description": "RESTful API服务器",
    "key_files": ["server.js", "routes/", "models/"]
  }
}
```

```bash
#!/bin/bash
# gemini-project.sh

PROJECTS_FILE="$HOME/.gemini-projects.json"

if [ "$1" = "list" ]; then
    jq -r 'keys[]' $PROJECTS_FILE
elif [ "$1" = "set" ]; then
    export CURRENT_PROJECT="$2"
    echo "当前项目设置为: $2"
elif [ -n "$CURRENT_PROJECT" ]; then
    PROJECT_INFO=$(jq -r ".\"$CURRENT_PROJECT\"" $PROJECTS_FILE)
    gemini "当前项目信息：$PROJECT_INFO\n\n问题：$1"
else
    echo "请先设置项目: gemini-project.sh set <project-name>"
fi
```

## 5. **VS Code 集成方案**

如果你使用VS Code，可以创建工作区设置：

```json
// .vscode/settings.json
{
  "gemini.projectContext": {
    "name": "My React App",
    "description": "电商前端应用",
    "techStack": ["React", "TypeScript", "Vite"],
    "keyFiles": [
      "src/App.tsx",
      "src/components/",
      "package.json"
    ],
    "conventions": [
      "使用函数式组件",
      "TypeScript严格模式",
      "ESLint + Prettier"
    ]
  }
}
```

## 6. **最佳实践建议**

### 创建项目模板
```bash
# 为每个项目创建 .gemini 目录
mkdir .gemini

# 项目概述
cat > .gemini/overview.md << 'EOF'
# 项目概述
- 项目名称：
- 技术栈：
- 主要功能：
- 架构模式：
EOF

# 代码规范
cat > .gemini/conventions.md << 'EOF'
# 代码规范
- 命名约定：
- 文件结构：
- 编码标准：
EOF

# 常见问题
cat > .gemini/faq.md << 'EOF'
# 常见问题
Q: 如何启动开发服务器？
A: npm run dev

Q: 如何运行测试？
A: npm test
EOF
```

### 快速查询脚本
```bash
#!/bin/bash
# gask (gemini ask with context)

CONTEXT_DIR=".gemini"

if [ -d "$CONTEXT_DIR" ]; then
    FULL_CONTEXT=""
    for file in $CONTEXT_DIR/*.md; do
        if [ -f "$file" ]; then
            FULL_CONTEXT="$FULL_CONTEXT\n\n$(cat $file)"
        fi
    done

    gemini "项目上下文：$FULL_CONTEXT\n\n问题：$1"
else
    gemini "$1"
fi
```

虽然Gemini CLI没有内置记忆功能，但通过这些方法可以有效地为每个项目维护上下文信息，让AI更好地理解你的代码仓库！
