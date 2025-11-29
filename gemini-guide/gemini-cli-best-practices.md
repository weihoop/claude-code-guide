# Gemini CLI 编程最佳实践指南

> 基于 Gemini 2.5 Pro 和最新的 CLI 功能整理（2025年1月）

## 目录

1. [快速开始](#快速开始)
2. [安装与配置](#安装与配置)
3. [核心功能与使用](#核心功能与使用)
4. [GEMINI.md 配置最佳实践](#geminimd-配置最佳实践)
5. [项目上下文管理](#项目上下文管理)
6. [高效提示词技巧](#高效提示词技巧)
7. [工作流程最佳实践](#工作流程最佳实践)
8. [MCP 服务器集成](#mcp-服务器集成)
9. [命令行参数与配置](#命令行参数与配置)
10. [性能优化技巧](#性能优化技巧)
11. [常见问题与解决方案](#常见问题与解决方案)
12. [实用脚本与工具](#实用脚本与工具)

---

## 快速开始

### 什么是 Gemini CLI？

Gemini CLI 是一个**开源 AI 代理**，将 Google Gemini 的强大功能直接带入终端，专为开发者设计。

### 核心优势

- ✅ **免费额度充足**: 每分钟 60 次请求，每天 1000 次请求
- ✅ **超大上下文**: Gemini 2.5 Pro 提供 100 万 token 上下文窗口
- ✅ **内置工具**: Google 搜索、文件操作、Shell 命令、Web 抓取
- ✅ **MCP 支持**: 通过 Model Context Protocol 扩展自定义功能
- ✅ **终端优先**: 为命令行开发者优化的交互体验

---

## 安装与配置

### 前置要求

```bash
# 检查 Node.js 版本（需要 18 或更高）
node --version
```

### 安装方式

#### 方式 1: 全局安装（推荐）

```bash
npm install -g @google/gemini-cli
```

#### 方式 2: 使用 npx（无需安装）

```bash
npx @google/gemini-cli
```

#### 方式 3: Google Cloud Shell

在 Cloud Shell 中无需额外安装，直接可用。

### 首次运行

```bash
# 启动 Gemini CLI
gemini

# 首次运行会提示认证，选择以下方式之一：
# 1. 使用 Google 个人账号登录（推荐新手）
# 2. 使用 API Key（环境变量方式）
# 3. 使用 Vertex AI
```

### API Key 配置（可选）

```bash
# 1. 访问 AI Studio 生成 API Key
# https://ai.google.dev/

# 2. 设置环境变量
export GOOGLE_API_KEY="your-api-key-here"

# 3. 添加到 shell 配置文件
echo 'export GOOGLE_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

---

## 核心功能与使用

### 基本命令

```bash
# 启动交互式会话
gemini

# 单次问答模式
gemini "你的问题"

# 显示帮助
gemini --help

# 查看版本
gemini --version
```

### 内置斜杠命令

```bash
/help           # 显示所有可用命令
/init           # 初始化项目，生成 GEMINI.md
/memory show    # 查看当前上下文（包含所有 GEMINI.md）
/memory clear   # 清除对话历史
/exit           # 退出 CLI
```

### 内置工具功能

Gemini CLI 自动集成了以下工具，无需手动配置：

1. **Google Search Grounding**: 实时搜索最新信息
2. **File Operations**: 读取、写入、编辑文件
3. **Shell Commands**: 执行终端命令
4. **Web Fetching**: 抓取网页内容

---

## GEMINI.md 配置最佳实践

### 什么是 GEMINI.md？

GEMINI.md 是项目配置文件，用于提供项目上下文、编码规范、架构信息等指令给 Gemini 模型。

### 分层加载机制

Gemini CLI 会按以下顺序**组合加载**多个 GEMINI.md 文件：

```
1. 全局配置: ~/.gemini/GEMINI.md
2. 项目根配置: /project-root/GEMINI.md
3. 子目录配置: /project-root/src/components/GEMINI.md
```

**重要**: 更具体的配置会覆盖通用配置。

### 快速初始化

```bash
# 在项目根目录运行
cd /path/to/your/project
gemini

# 在 Gemini CLI 中运行
/init
```

这会生成一个基础的 GEMINI.md 模板。

### GEMINI.md 模板示例

#### 完整项目配置模板

```markdown
# 项目配置文件

## 项目概述

- **项目名称**: My React App
- **项目类型**: 前端应用
- **技术栈**: React 18 + TypeScript + Vite
- **主要功能**: 电商平台前端界面

## 项目结构

```
my-react-app/
├── src/
│   ├── components/     # React 组件
│   ├── hooks/          # 自定义 Hooks
│   ├── utils/          # 工具函数
│   ├── services/       # API 服务
│   └── App.tsx         # 应用入口
├── public/             # 静态资源
├── package.json
└── vite.config.ts
```

## 编码规范

### 命名约定
- 组件文件: PascalCase (e.g., `UserProfile.tsx`)
- 工具函数: camelCase (e.g., `formatDate.ts`)
- 常量: UPPER_SNAKE_CASE (e.g., `API_BASE_URL`)

### 代码风格
- 使用函数式组件，避免类组件
- TypeScript 严格模式
- 使用 ESLint + Prettier 格式化
- 优先使用组合而非继承

### 导入顺序
```typescript
// 1. 外部依赖
import React from 'react';
import { useState } from 'react';

// 2. 内部模块
import { Button } from '@/components';
import { useAuth } from '@/hooks';

// 3. 样式文件
import styles from './App.module.css';
```

## 架构模式

- **状态管理**: Context API + useReducer
- **路由**: React Router v6
- **数据获取**: React Query
- **样式方案**: CSS Modules

## 开发工作流

```bash
# 启动开发服务器
npm run dev

# 运行测试
npm test

# 构建生产版本
npm run build
```

## 注意事项

- 所有 API 调用必须包含错误处理
- 组件必须编写 PropTypes 或 TypeScript 类型
- 提交前运行 lint 和 test
```

#### 全局配置示例 (~/.gemini/GEMINI.md)

```markdown
# 全局开发规范

## 通用编码原则

- 编写清晰、自解释的代码
- 优先简洁性而非过度抽象
- 遵循 SOLID 原则
- 编写可测试的代码

## Git 提交规范

使用 Conventional Commits 格式：

- `feat:` 新功能
- `fix:` Bug 修复
- `docs:` 文档更新
- `refactor:` 重构
- `test:` 测试
- `chore:` 其他修改

## 安全最佳实践

- 永不在代码中硬编码密钥
- 使用环境变量管理敏感信息
- 验证所有用户输入
- 使用参数化查询防止 SQL 注入
```

#### 组件级配置示例 (src/components/GEMINI.md)

```markdown
# 组件开发规范

## React 组件规范

### 组件模板

```typescript
import React from 'react';

interface Props {
  // 定义 props 类型
}

export const ComponentName: React.FC<Props> = ({ prop1, prop2 }) => {
  // 1. Hooks
  const [state, setState] = useState();

  // 2. 副作用
  useEffect(() => {
    // ...
  }, []);

  // 3. 事件处理
  const handleClick = () => {
    // ...
  };

  // 4. 渲染
  return (
    <div>
      {/* JSX */}
    </div>
  );
};
```

### 组件命名规则

- 使用描述性名称
- 单一职责原则
- 可复用组件放在 `components/common/`
- 业务组件放在 `components/features/`
```

### 模块化组织

使用 `@file.md` 语法导入其他 Markdown 文件：

```markdown
# 主配置文件 GEMINI.md

@conventions.md
@architecture.md
@faq.md
```

**注意**: 仅支持 `.md` 文件导入。

### 查看最终上下文

```bash
# 在 Gemini CLI 中运行
/memory show
```

这会显示所有已加载的 GEMINI.md 文件的组合内容。

---

## 项目上下文管理

虽然 Gemini CLI **没有内置代码仓库记忆功能**，但可以通过以下方式实现类似效果：

### 方法 1: 使用 GEMINI.md（推荐）

```bash
# 1. 在项目根目录创建 GEMINI.md
cat > GEMINI.md << 'EOF'
# 项目上下文

## 项目结构
- src/: 源代码
- tests/: 测试文件
- docs/: 文档

## 技术栈
- Python 3.11
- FastAPI
- PostgreSQL
- Docker

## 关键文件
- main.py: 应用入口
- models.py: 数据模型
- api/routes.py: API 路由
EOF

# 2. 在项目目录运行 gemini 时自动加载
cd /path/to/project
gemini
```

### 方法 2: 自动上下文脚本

创建 `gemini-context.sh` 脚本：

```bash
#!/bin/bash
# gemini-context.sh - 自动生成项目上下文

PROJECT_ROOT=$(pwd)
CONTEXT_FILE=".gemini-context.md"

# 生成项目上下文
generate_context() {
    cat > $CONTEXT_FILE << EOF
# 项目上下文（自动生成）

## 基本信息
- 项目路径: $PROJECT_ROOT
- 生成时间: $(date '+%Y-%m-%d %H:%M:%S')

## 项目结构
\`\`\`
$(tree -L 3 -I 'node_modules|.git|dist|build|__pycache__' 2>/dev/null || ls -la)
\`\`\`

## 依赖信息
EOF

    # 根据项目类型添加依赖信息
    if [ -f "package.json" ]; then
        echo -e "\n### Node.js Dependencies\n\`\`\`json" >> $CONTEXT_FILE
        cat package.json >> $CONTEXT_FILE
        echo -e "\`\`\`\n" >> $CONTEXT_FILE
    fi

    if [ -f "requirements.txt" ]; then
        echo -e "\n### Python Dependencies\n\`\`\`" >> $CONTEXT_FILE
        cat requirements.txt >> $CONTEXT_FILE
        echo -e "\`\`\`\n" >> $CONTEXT_FILE
    fi

    if [ -f "go.mod" ]; then
        echo -e "\n### Go Dependencies\n\`\`\`" >> $CONTEXT_FILE
        cat go.mod >> $CONTEXT_FILE
        echo -e "\`\`\`\n" >> $CONTEXT_FILE
    fi

    echo "✅ 上下文已生成: $CONTEXT_FILE"
}

# 使用方式
case "$1" in
    --generate|-g)
        generate_context
        ;;
    --view|-v)
        cat $CONTEXT_FILE 2>/dev/null || echo "❌ 上下文文件不存在，请先运行 --generate"
        ;;
    *)
        echo "用法: $0 [选项]"
        echo "选项:"
        echo "  -g, --generate    生成项目上下文"
        echo "  -v, --view        查看项目上下文"
        ;;
esac
```

使用方式：

```bash
# 生成上下文
bash gemini-context.sh --generate

# 查看上下文
bash gemini-context.sh --view

# 在 GEMINI.md 中引用
echo "@.gemini-context.md" >> GEMINI.md
```

### 方法 3: Shell 别名快速查询

```bash
# 添加到 ~/.bashrc 或 ~/.zshrc

# 项目上下文别名
alias gctx='cat GEMINI.md 2>/dev/null || echo "未找到 GEMINI.md"'

# 带上下文的快速提问
gask() {
    local context=$(cat GEMINI.md 2>/dev/null || echo "无项目上下文")
    gemini "项目上下文:\n$context\n\n问题: $1"
}

# 使用示例
gask "如何添加用户认证功能？"
```

### 方法 4: 多项目管理

创建项目配置文件 `~/.gemini-projects.json`:

```json
{
  "my-react-app": {
    "path": "/home/user/projects/my-react-app",
    "tech_stack": ["React", "TypeScript", "Vite"],
    "description": "电商前端应用",
    "main_files": ["src/App.tsx", "package.json"]
  },
  "api-server": {
    "path": "/home/user/projects/api-server",
    "tech_stack": ["Node.js", "Express", "PostgreSQL"],
    "description": "RESTful API 服务器",
    "main_files": ["server.js", "routes/index.js"]
  }
}
```

创建管理脚本 `gemini-project.sh`:

```bash
#!/bin/bash
PROJECTS_FILE="$HOME/.gemini-projects.json"

case "$1" in
    list)
        echo "📋 可用项目:"
        jq -r 'keys[]' $PROJECTS_FILE
        ;;
    info)
        echo "📌 项目信息:"
        jq ".\"$2\"" $PROJECTS_FILE
        ;;
    cd)
        PROJECT_PATH=$(jq -r ".\"$2\".path" $PROJECTS_FILE)
        if [ "$PROJECT_PATH" != "null" ]; then
            cd "$PROJECT_PATH"
            pwd
            gemini
        else
            echo "❌ 项目不存在: $2"
        fi
        ;;
    *)
        echo "用法: $0 {list|info|cd} [项目名]"
        ;;
esac
```

---

## 高效提示词技巧

### 常见问题：糟糕的提示词

❌ **问题**: 缺乏上下文，模糊不清

```
"优化这段代码"
"修复 bug"
"添加功能"
```

✅ **改进**: 提供明确的上下文和目标

```
"优化 src/utils/parser.ts 中的 parseJSON 函数，目标是减少 50% 的执行时间，当前瓶颈在于重复的对象遍历"

"修复 auth.js 中的登录 bug：用户在输入正确密码后仍然显示'密码错误'，问题可能与密码哈希比较有关"

"在 UserProfile 组件中添加头像上传功能，要求：1) 支持拖拽上传 2) 图片预览 3) 大小限制 2MB"
```

### 最佳实践：先生成计划

```bash
# 步骤 1: 让 Gemini 生成计划
gemini "我需要在 React 应用中添加暗黑模式功能。请先生成一个详细的实现计划，不要直接修改代码。"

# Gemini 会生成:
# 1. 创建主题上下文 (ThemeContext)
# 2. 实现主题切换逻辑
# 3. 创建暗黑模式样式
# 4. 添加切换按钮组件
# 5. 持久化主题偏好到 localStorage

# 步骤 2: 审查计划，修正方向
"计划看起来不错，但第 3 步请使用 CSS 变量而不是 CSS-in-JS"

# 步骤 3: 执行实现
"计划确认无误，请按照修正后的计划开始实现"
```

### 分解复杂任务

❌ 一次性大任务：
```
"构建一个完整的用户认证系统，包括注册、登录、密码重置、邮箱验证等功能"
```

✅ 分解为小步骤：
```
步骤 1: "创建用户注册表单组件，包含邮箱、密码、确认密码字段，添加客户端验证"
步骤 2: "实现注册 API 端点，包含密码哈希和数据库存储"
步骤 3: "添加邮箱验证功能，发送验证链接"
步骤 4: "实现登录功能，包含 JWT token 生成"
...
```

### 提供示例和约束

```
"创建一个产品列表组件，参考以下设计：

要求：
1. 使用 CSS Grid 布局，每行 3 个产品
2. 每个产品卡片包含：图片、标题、价格、'加入购物车'按钮
3. 响应式设计：移动端每行 1 个，平板每行 2 个
4. 使用 TypeScript，定义 Product 接口
5. 模拟数据使用 products.json

示例产品数据结构：
{
  \"id\": 1,
  \"name\": \"产品名称\",
  \"price\": 99.99,
  \"image\": \"/images/product.jpg\"
}
"
```

---

## 工作流程最佳实践

### PRD 驱动开发

在开始编码前，创建产品需求文档（PRD）：

```markdown
# 产品需求文档: 用户仪表盘

## 目标
为用户提供个性化的数据分析仪表盘

## 功能需求
1. 数据可视化
   - 折线图：展示最近 30 天趋势
   - 饼图：分类占比分析
   - 数据表格：详细数据列表

2. 交互功能
   - 日期范围选择器
   - 数据导出（CSV, PDF）
   - 实时数据刷新

## 技术栈
- 前端：React + Chart.js
- 后端：Node.js + Express
- 数据库：PostgreSQL

## 实现步骤
1. 设计数据库表结构
2. 创建后端 API 端点
3. 实现前端组件
4. 集成图表库
5. 添加数据导出功能
6. 编写单元测试
```

### 增量开发 + Git 提交

```bash
# 步骤 1: 创建功能分支
git checkout -b feature/user-dashboard

# 步骤 2: 小步骤实现
gemini "实现步骤 1：设计用户数据表结构"
# 等待完成...

git add .
git commit -m "feat: 添加用户数据表结构"

# 步骤 3: 继续下一步
gemini "实现步骤 2：创建 GET /api/dashboard 端点"
# 等待完成...

git add .
git commit -m "feat: 添加仪表盘数据 API"

# 重复以上流程...
```

**优势**:
- 每个步骤都有清晰的提交记录
- 出错时可以轻松回滚
- 便于代码审查

### 测试驱动开发

```bash
# 1. 先编写测试用例
gemini "为 UserService.createUser() 方法编写单元测试，测试场景包括：
1. 成功创建用户
2. 邮箱已存在时抛出错误
3. 密码强度不足时抛出错误"

# 2. 运行测试（预期失败）
npm test

# 3. 实现功能使测试通过
gemini "实现 UserService.createUser() 方法，确保所有测试通过"

# 4. 运行测试验证
npm test
```

### 代码审查检查清单

在提交代码前，让 Gemini 进行自检：

```bash
gemini "请审查以下文件的代码质量：

文件: src/services/payment.js

检查清单:
- [ ] 是否有安全漏洞（SQL 注入、XSS 等）
- [ ] 错误处理是否完善
- [ ] 是否遵循代码规范
- [ ] 是否有性能问题
- [ ] 是否需要添加注释
- [ ] 是否有单元测试覆盖
"
```

---

## MCP 服务器集成

### 什么是 MCP？

MCP (Model Context Protocol) 允许扩展 Gemini CLI 的功能，实现与数据库、API、自定义脚本等的交互。

### FastMCP 集成（Python）

从 FastMCP v2.12.3 开始，可以直接安装本地 MCP 服务器：

```bash
# 安装 FastMCP
pip install fastmcp

# 使用 FastMCP 安装 MCP 服务器到 Gemini CLI
fastmcp install gemini-cli
```

### GitHub MCP 服务器示例

GitHub 官方提供的 MCP 服务器可以让 Gemini CLI 直接操作 GitHub 仓库：

```bash
# 1. 安装 GitHub MCP 服务器
npm install -g @modelcontextprotocol/server-github

# 2. 配置 Gemini CLI
# 编辑 ~/.gemini/config.json 或项目的 gemini-extension.json

{
  "mcpServers": {
    "github": {
      "command": "mcp-server-github",
      "env": {
        "GITHUB_TOKEN": "your-github-token"
      }
    }
  }
}

# 3. 在 Gemini CLI 中使用
gemini "检测我的 user/repo 仓库中的问题并创建 PR 修复"
```

**功能示例**:
- 检测代码问题
- 自动修复并提交
- 创建 Pull Request
- 查看 Issues 和 PR

### Docker MCP Toolkit

Docker Desktop 自动配置 MCP Gateway，处理请求路由、认证、容器化：

```bash
# 1. 确保 Docker Desktop 已安装并运行

# 2. Gemini CLI 会自动检测 Docker MCP 工具

# 3. 使用示例
gemini "列出所有正在运行的 Docker 容器"
gemini "构建并运行 Dockerfile"
gemini "查看容器日志"
```

### 自定义 MCP 服务器

使用 Go 构建自定义 MCP 服务器示例（参考 Google Codelab）：

```go
// server.go
package main

import (
    "context"
    "fmt"
    "github.com/google/mcp-go/mcp"
)

type CustomServer struct{}

func (s *CustomServer) ListTools(ctx context.Context) ([]*mcp.Tool, error) {
    return []*mcp.Tool{
        {
            Name:        "custom_tool",
            Description: "自定义工具描述",
            InputSchema: map[string]interface{}{
                "type": "object",
                "properties": map[string]interface{}{
                    "input": map[string]string{"type": "string"},
                },
                "required": []string{"input"},
            },
        },
    }, nil
}

func (s *CustomServer) CallTool(ctx context.Context, name string, args map[string]interface{}) (interface{}, error) {
    if name == "custom_tool" {
        input := args["input"].(string)
        // 实现自定义逻辑
        return fmt.Sprintf("处理结果: %s", input), nil
    }
    return nil, fmt.Errorf("未知工具: %s", name)
}

func main() {
    server := &CustomServer{}
    mcp.Serve(server)
}
```

配置文件 `gemini-extension.json`:

```json
{
  "mcpServers": {
    "custom-server": {
      "command": "./custom-mcp-server",
      "args": []
    }
  }
}
```

### MCP 服务器最佳实践

1. **本地优先**: 优先使用本地 STDIO 传输模式
2. **错误处理**: 实现完善的错误处理和日志记录
3. **文档完善**: 为每个工具提供清晰的描述和参数说明
4. **安全性**: 验证输入参数，避免注入攻击
5. **性能优化**: 缓存频繁访问的数据

---

## 命令行参数与配置

### 常用命令行参数

```bash
# 模型选择
gemini --model gemini-2.5-pro

# 指定配置文件
gemini --config /path/to/config.json

# 单次问答模式
gemini "你的问题"

# 从文件读取提示词
gemini < prompt.txt

# 输出到文件
gemini "生成代码" > output.txt

# 调试模式
gemini --verbose

# 禁用上下文加载
gemini --no-context
```

### 配置文件位置

```
# 全局配置
~/.gemini/config.json

# 项目配置
/project-root/gemini-extension.json

# 环境变量
GEMINI_API_KEY
GEMINI_MODEL
GEMINI_CONFIG_PATH
```

### 示例配置文件

```json
{
  "model": "gemini-2.5-pro",
  "temperature": 0.7,
  "maxTokens": 8192,
  "contextFiles": ["GEMINI.md"],
  "mcpServers": {
    "github": {
      "command": "mcp-server-github",
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  },
  "extensions": [
    {
      "name": "custom-extension",
      "path": "./extensions/custom"
    }
  ]
}
```

---

## 性能优化技巧

### 1. 优化上下文大小

虽然 Gemini 2.5 Pro 提供 100 万 token 上下文，但更小的上下文响应更快：

```bash
# ❌ 加载整个代码库
gemini "分析项目中所有文件"

# ✅ 精确指定范围
gemini "分析 src/components/ 目录下的 React 组件"
```

### 2. 使用缓存机制

对于频繁访问的信息，创建缓存：

```bash
# 生成项目摘要并缓存
gemini "生成项目架构摘要" > .gemini-cache/summary.md

# 后续引用缓存
gemini "基于项目摘要（见 .gemini-cache/summary.md），建议如何添加新功能"
```

### 3. 批量处理

```bash
# ❌ 多次单独请求
gemini "检查 file1.js"
gemini "检查 file2.js"
gemini "检查 file3.js"

# ✅ 一次批量请求
gemini "检查以下文件并生成统一报告：
- file1.js
- file2.js
- file3.js
"
```

### 4. 限制输出长度

```bash
# 明确输出要求
gemini "总结 API 文档的关键要点（不超过 5 条）"
gemini "生成代码示例（不超过 50 行）"
```

---

## 常见问题与解决方案

### Q1: 如何处理 API 速率限制？

```bash
# 免费额度：60 请求/分钟，1000 请求/天

# 解决方案 1: 使用本地缓存减少请求
# 解决方案 2: 批量处理多个任务
# 解决方案 3: 升级到付费计划
```

### Q2: 如何处理大型代码库？

```bash
# 方案 1: 分层 GEMINI.md 配置
# 在不同目录创建专门的 GEMINI.md

# 方案 2: 使用 @import 语法
# 主 GEMINI.md:
@architecture.md
@conventions.md

# 方案 3: 动态上下文脚本
# 仅加载相关文件信息
```

### Q3: 如何调试 Gemini CLI 问题？

```bash
# 开启详细日志
gemini --verbose

# 查看加载的上下文
/memory show

# 检查配置文件
cat ~/.gemini/config.json

# 查看 MCP 服务器状态
gemini "列出所有可用的工具"
```

### Q4: 生成的代码不符合项目规范？

```markdown
<!-- 更新 GEMINI.md -->

# 代码规范（强制要求）

## 重要提醒
⚠️ **所有生成的代码必须严格遵循以下规范**

## TypeScript 规范
- 使用 `interface` 而非 `type` 定义对象类型
- 所有函数必须有明确的返回类型
- 禁止使用 `any` 类型

## 示例
```typescript
// ✅ 正确
interface User {
  id: number;
  name: string;
}

function getUser(id: number): User {
  // ...
}

// ❌ 错误
type User = {
  id: number;
  name: string;
}

function getUser(id) {
  // ...
}
```
```

### Q5: 如何管理多个项目的不同配置？

使用项目切换脚本（见"项目上下文管理"章节）。

---

## 实用脚本与工具

### 1. 自动提交工作流脚本

```bash
#!/bin/bash
# gemini-commit.sh - 自动生成提交信息并提交

# 1. 显示修改的文件
echo "📝 修改的文件:"
git status --short

# 2. 生成提交信息
echo -e "\n🤖 正在生成提交信息..."
COMMIT_MSG=$(gemini "根据以下 git diff 生成简洁的提交信息（使用 Conventional Commits 格式）:

$(git diff --cached)

要求:
- 格式: <type>: <description>
- type 可以是: feat, fix, docs, refactor, test, chore
- description 使用中文
- 不超过 50 字符
- 只返回提交信息，不要其他内容
")

echo "生成的提交信息: $COMMIT_MSG"

# 3. 确认并提交
read -p "确认提交? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git commit -m "$COMMIT_MSG"
    echo "✅ 提交成功"
else
    echo "❌ 已取消"
fi
```

### 2. 代码审查助手

```bash
#!/bin/bash
# gemini-review.sh - 代码审查脚本

FILES=$@

if [ -z "$FILES" ]; then
    echo "用法: $0 <文件路径...>"
    exit 1
fi

echo "🔍 正在审查代码..."

for file in $FILES; do
    echo -e "\n=== 审查文件: $file ==="

    gemini "请审查以下代码，重点检查:
1. 安全漏洞
2. 性能问题
3. 代码规范
4. 潜在 bug
5. 改进建议

代码内容:
\`\`\`
$(cat $file)
\`\`\`

请提供详细的审查报告。
" > "${file}.review.md"

    echo "✅ 审查报告已生成: ${file}.review.md"
done
```

### 3. 文档生成器

```bash
#!/bin/bash
# gemini-docs.sh - 自动生成文档

SOURCE_FILE=$1
OUTPUT_FILE="${SOURCE_FILE%.js}.md"

if [ -z "$SOURCE_FILE" ]; then
    echo "用法: $0 <源代码文件>"
    exit 1
fi

echo "📚 正在生成文档..."

gemini "为以下代码生成 Markdown 格式的 API 文档:

$(cat $SOURCE_FILE)

文档要求:
- 包含函数/类的描述
- 参数说明
- 返回值说明
- 使用示例
- 注意事项
" > $OUTPUT_FILE

echo "✅ 文档已生成: $OUTPUT_FILE"
```

### 4. 测试用例生成器

```bash
#!/bin/bash
# gemini-test.sh - 生成测试用例

SOURCE_FILE=$1
TEST_FILE="${SOURCE_FILE%.js}.test.js"

gemini "为以下代码生成完整的测试用例（使用 Jest）:

$(cat $SOURCE_FILE)

测试要求:
- 覆盖所有函数
- 包含正常场景和边界条件
- 包含错误处理测试
- 使用 describe 和 it 组织测试
" > $TEST_FILE

echo "✅ 测试文件已生成: $TEST_FILE"
```

### 5. 项目初始化模板

```bash
#!/bin/bash
# gemini-init-project.sh - 快速初始化项目配置

PROJECT_NAME=$1
PROJECT_TYPE=$2  # react/node/python

if [ -z "$PROJECT_NAME" ] || [ -z "$PROJECT_TYPE" ]; then
    echo "用法: $0 <项目名> <类型: react|node|python>"
    exit 1
fi

mkdir -p $PROJECT_NAME
cd $PROJECT_NAME

# 创建 GEMINI.md
cat > GEMINI.md << EOF
# $PROJECT_NAME 项目配置

## 项目类型
$PROJECT_TYPE

## 生成时间
$(date '+%Y-%m-%d %H:%M:%S')

## 项目结构
待完善

## 技术栈
待完善

## 编码规范
待完善
EOF

# 创建 .gemini 目录
mkdir -p .gemini

# 根据项目类型创建特定配置
case $PROJECT_TYPE in
    react)
        cat > .gemini/react-conventions.md << 'EOF'
# React 开发规范

- 使用函数式组件
- TypeScript 严格模式
- CSS Modules 样式方案
EOF
        ;;
    node)
        cat > .gemini/node-conventions.md << 'EOF'
# Node.js 开发规范

- 使用 ES6+ 语法
- 异步操作使用 async/await
- Express 路由规范
EOF
        ;;
    python)
        cat > .gemini/python-conventions.md << 'EOF'
# Python 开发规范

- 遵循 PEP 8
- 使用类型提示
- 文档字符串格式: Google Style
EOF
        ;;
esac

echo "✅ 项目 $PROJECT_NAME 初始化完成"
echo "📁 项目目录: $(pwd)"
echo "📄 配置文件: GEMINI.md"
```

---

## 总结

### 核心要点

1. **充分利用 GEMINI.md**: 为每个项目创建详细的配置文件
2. **分解任务**: 将复杂任务拆分为小步骤，逐步实现
3. **先计划后执行**: 让 Gemini 先生成计划，审查后再实施
4. **增量提交**: 每完成一个小步骤就提交代码
5. **扩展功能**: 使用 MCP 服务器集成外部工具
6. **优化上下文**: 只提供必要的上下文信息
7. **自动化工作流**: 编写脚本自动化重复性任务

### 推荐学习资源

- **官方文档**: [https://geminicli.com/docs/](https://geminicli.com/docs/)
- **GitHub 仓库**: [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **Google Codelabs**: [https://codelabs.developers.google.com/gemini-cli-hands-on](https://codelabs.developers.google.com/gemini-cli-hands-on)
- **FastMCP 文档**: [https://developers.googleblog.com/en/gemini-cli-fastmcp-simplifying-mcp-server-development/](https://developers.googleblog.com/en/gemini-cli-fastmcp-simplifying-mcp-server-development/)
- **Cheatsheet**: [https://www.philschmid.de/gemini-cli-cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet)

### 下一步行动

1. 在你的项目中运行 `/init` 生成 GEMINI.md
2. 尝试使用脚本自动化常见任务
3. 探索 MCP 服务器集成
4. 加入社区分享经验

---

**文档版本**: v1.0.0
**最后更新**: 2025-01-29
**维护者**: 基于官方文档和社区最佳实践整理

## 参考来源

- [5 things to try with Gemini 3 Pro in Gemini CLI](https://developers.googleblog.com/en/5-things-to-try-with-gemini-3-pro-in-gemini-cli/)
- [GitHub - google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- [Gemini CLI Best Practices: 10 Pro Tips](https://dev.to/proflead/gemini-cli-best-practices-10-pro-tips-youre-not-using-272b)
- [Gemini CLI Tips & Tricks - by Addy Osmani](https://addyo.substack.com/p/gemini-cli-tips-and-tricks)
- [Hands-on with Gemini CLI | Google Codelabs](https://codelabs.developers.google.com/gemini-cli-hands-on)
- [Google announces Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- [Gemini CLI: A Guide With Practical Examples](https://www.datacamp.com/tutorial/gemini-cli)
- [Google Gemini CLI Tutorial](https://dev.to/auden/google-gemini-cli-tutorial-how-to-install-and-use-it-with-images-4phb)
- [Gemini CLI 🤝 FastMCP](https://developers.googleblog.com/en/gemini-cli-fastmcp-simplifying-mcp-server-development/)
- [MCP servers with the Gemini CLI](https://geminicli.com/docs/tools/mcp-server/)
- [Practical Gemini CLI: Bring your own system instruction](https://medium.com/google-cloud/practical-gemini-cli-bring-your-own-system-instruction-19ea7f07faa2)
- [Gemini CLI Configuration](https://geminicli.com/docs/get-started/configuration/)
