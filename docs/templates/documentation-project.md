# 文档库项目配置模板

适用于技术文档、API 文档、知识库、博客等纯文档项目。

---

## CLAUDE.md 模板

将以下内容保存为项目根目录的 `CLAUDE.md` 文件：

```markdown
# 项目名称 - 文档库

## 项目概述

**项目类型**: 技术文档库
**主要用途**: 提供项目文档、API 参考、使用指南
**技术栈**: Markdown, VitePress/Docusaurus/MkDocs
**开发模式**: 文档优先，版本控制，持续更新

## 文档框架

### 选择的框架
- **VitePress** - Vue 驱动的静态站点生成器
- **Docusaurus** - React 驱动的文档站点
- **MkDocs** - Python 驱动的文档生成器
- **纯 Markdown** - 简单的文档库

## 项目结构

\```
docs/                        # 文档根目录
├── index.md                # 首页
├── guide/                  # 使用指南
│   ├── getting-started.md
│   ├── installation.md
│   ├── configuration.md
│   └── best-practices.md
├── api/                    # API 参考
│   ├── overview.md
│   ├── authentication.md
│   └── endpoints/
│       ├── users.md
│       └── posts.md
├── tutorials/              # 教程
│   ├── quickstart.md
│   └── advanced/
│       ├── optimization.md
│       └── deployment.md
├── reference/              # 参考文档
│   ├── cli.md
│   ├── configuration.md
│   └── faq.md
├── blog/                   # 博客（可选）
│   ├── 2025-01-01-release-notes.md
│   └── 2025-01-15-tutorial.md
└── .vitepress/             # VitePress 配置
    ├── config.ts
    └── theme/

public/                     # 静态资源
├── images/
├── diagrams/
└── downloads/

package.json
.gitignore
README.md
\```

## 常用命令

### 开发

\```bash
# 安装依赖
npm install

# 启动开发服务器
npm run docs:dev
# 访问: http://localhost:5173 (VitePress)
# 或: http://localhost:3000 (Docusaurus)

# 构建文档
npm run docs:build

# 预览构建结果
npm run docs:preview
\```

### 部署

\```bash
# 部署到 GitHub Pages
npm run docs:deploy

# 或使用 Vercel/Netlify
# 只需连接仓库，自动部署
\```

## 文档规范

### Markdown 语法

使用 **GitHub Flavored Markdown (GFM)**：

\```markdown
# 一级标题
## 二级标题
### 三级标题

**粗体** *斜体* ~~删除线~~

- 无序列表项 1
- 无序列表项 2

1. 有序列表项 1
2. 有序列表项 2

[链接文本](https://example.com)
![图片描述](./images/screenshot.png)

> 引用文本

\```代码块
代码内容
\```

| 列1 | 列2 |
|-----|-----|
| 内容1 | 内容2 |
\```

### 代码块规范

#### 指定语言高亮

\```markdown
\```python
def hello():
    print("Hello World")
\```

\```typescript
function greet(name: string): void {
  console.log(\`Hello, \${name}\`)
}
\```

\```bash
npm install
npm run dev
\```
\```

#### 代码行高亮（VitePress）

\```markdown
\```js{2,4-6}
export default {
  data () {  // 高亮第2行
    return {
      msg: 'Highlighted!'  // 高亮第4-6行
    }
  }
}
\```
\```

#### 代码组（标签页）

\```markdown
:::code-group

\```js [config.js]
export default {
  theme: 'default'
}
\```

\```ts [config.ts]
export default {
  theme: 'default' as const
}
\```

:::
\```

### 链接规范

#### 内部链接

\```markdown
# ✅ 推荐：相对路径 + .md 扩展名
[安装指南](./guide/installation.md)
[API 参考](../api/overview.md)

# ❌ 避免：绝对路径或无扩展名
[安装指南](/guide/installation)
\```

#### 锚点链接

\```markdown
# 跳转到同一页面的标题
[跳转到配置章节](#配置)

## 配置
...
\```

#### 外部链接

\```markdown
# 添加目标属性在新标签打开
[GitHub](https://github.com){target="_blank"}
\```

### 图片规范

#### 图片存放

\```
public/images/
├── screenshots/
│   ├── dashboard.png
│   └── settings.png
├── diagrams/
│   ├── architecture.svg
│   └── workflow.png
└── logos/
    ├── logo.png
    └── icon.svg
\```

#### 图片引用

\```markdown
# 使用相对路径
![仪表板截图](../public/images/screenshots/dashboard.png)

# 使用绝对路径（从 public 目录）
![仪表板截图](/images/screenshots/dashboard.png)

# 添加标题
![仪表板截图](/images/screenshots/dashboard.png "仪表板界面")

# 指定尺寸（HTML）
<img src="/images/logo.png" alt="Logo" width="200" height="100">
\```

### Frontmatter 元数据

在每个 Markdown 文件顶部添加元数据：

\```markdown
---
title: 快速开始
description: Claude Code 快速入门指南
lang: zh-CN
head:
  - - meta
    - name: keywords
      content: claude code, 安装, 配置
layout: doc
sidebar: true
prev:
  text: '介绍'
  link: '/guide/introduction'
next:
  text: '安装'
  link: '/guide/installation'
---

# 快速开始

文档内容...
\```

### 自定义容器（提示框）

\```markdown
::: info 信息
这是一条信息提示。
:::

::: tip 提示
这是一条建议。
:::

::: warning 警告
这是一条警告信息。
:::

::: danger 危险
这是一条危险警告。
:::

::: details 点击查看详情
这是折叠的详细内容。
:::
\```

## SEO 优化

### 页面元数据

每个文档页面应包含：

\```yaml
---
title: 页面标题 (50-60 字符)
description: 页面描述 (150-160 字符)
keywords: 关键词1, 关键词2, 关键词3
---
\```

### 标题结构

- **每个页面只有一个 H1** (`#`)
- H2-H6 按层级使用，不跳级
- 标题使用描述性文字

\```markdown
# 主标题（H1）- 每页只有一个

## 章节标题（H2）

### 小节标题（H3）

#### 细分标题（H4）
\```

### 图片 Alt 文本

所有图片都应该添加有意义的 alt 文本：

\```markdown
![Claude Code 安装界面截图](./images/installation.png)
![系统架构图展示了前后端分离的设计](./images/architecture.svg)
\```

## 文档维护

### 版本管理

\```markdown
# 使用 Git 标签管理文档版本
git tag v1.0.0
git push origin v1.0.0

# 在文档中标注版本
> 从版本 v1.2.0 开始支持此功能

\```新增于 v1.5.0\```
某个新功能
\```
\```

### 更新日志

维护一个 `CHANGELOG.md`：

\```markdown
# 更新日志

## [1.2.0] - 2025-01-15

### 新增
- 添加 API 认证文档
- 新增部署指南

### 修改
- 更新安装步骤
- 优化代码示例

### 修复
- 修正配置文件示例错误
- 修复死链

## [1.1.0] - 2025-01-01

...
\```

### 死链检查

\```bash
# 使用 markdown-link-check
npm install -g markdown-link-check

# 检查单个文件
markdown-link-check docs/index.md

# 检查所有文档
find docs -name \\*.md -exec markdown-link-check {} \\;
\```

### 拼写检查

\```bash
# 使用 cspell
npm install -g cspell

# 检查拼写
cspell "docs/**/*.md"
\```

## Git 工作流

### 提交规范

\```bash
docs: 添加 API 认证文档
docs: 更新安装步骤
docs: 修复死链
docs: 优化代码示例
fix: 修正配置文件错误
style: 调整文档格式
\```

### 分支管理

\```bash
main            # 生产环境文档
develop         # 开发中的文档
feature/xxx     # 新增文档特性
fix/xxx         # 修复文档问题
\```

## VitePress 特定配置

### 配置文件

\```typescript
// .vitepress/config.ts
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '项目文档',
  description: '完整的项目使用指南和 API 参考',
  lang: 'zh-CN',

  themeConfig: {
    nav: [
      { text: '指南', link: '/guide/getting-started' },
      { text: 'API', link: '/api/overview' },
      { text: '参考', link: '/reference/cli' }
    ],

    sidebar: {
      '/guide/': [
        {
          text: '开始',
          items: [
            { text: '简介', link: '/guide/introduction' },
            { text: '快速开始', link: '/guide/getting-started' },
            { text: '安装', link: '/guide/installation' }
          ]
        }
      ],
      '/api/': [
        {
          text: 'API 参考',
          items: [
            { text: '概述', link: '/api/overview' },
            { text: '认证', link: '/api/authentication' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/yourproject' }
    ],

    footer: {
      message: '基于 MIT 许可发布',
      copyright: 'Copyright © 2025'
    },

    search: {
      provider: 'local'
    }
  }
})
\```

### 自定义主题

\```typescript
// .vitepress/theme/index.ts
import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // 注册全局组件
  }
}
\```

## Docusaurus 特定配置

### 配置文件

\```javascript
// docusaurus.config.js
module.exports = {
  title: '项目文档',
  tagline: '完整的使用指南',
  url: 'https://docs.example.com',
  baseUrl: '/',
  favicon: 'img/favicon.ico',

  organizationName: 'your-org',
  projectName: 'your-project',

  themeConfig: {
    navbar: {
      title: '项目文档',
      logo: {
        alt: 'Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: '文档',
        },
        { to: '/blog', label: '博客', position: 'left' },
        {
          href: 'https://github.com/your-repo',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: '文档',
          items: [
            {
              label: '快速开始',
              to: '/docs/intro',
            },
          ],
        },
      ],
      copyright: \`Copyright © \${new Date().getFullYear()} Your Project.\`,
    },
  },

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/your-repo/edit/main/',
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
}
\```

## 部署配置

### GitHub Pages

\```yaml
# .github/workflows/deploy.yml
name: Deploy Docs

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install dependencies
        run: npm ci

      - name: Build docs
        run: npm run docs:build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: \${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs/.vitepress/dist
\```

### Vercel

\```json
// vercel.json
{
  "buildCommand": "npm run docs:build",
  "outputDirectory": "docs/.vitepress/dist"
}
\```

## 文档写作最佳实践

### 1. 清晰的结构

- 每个文档有明确的目的
- 使用描述性标题
- 逻辑顺序组织内容

### 2. 实用的代码示例

\```markdown
# ✅ 好的示例：完整、可执行
\```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev
\```

# ❌ 差的示例：不完整、模糊
\```bash
install dependencies
start server
\```
\```

### 3. 目标受众

- 为初学者提供详细步骤
- 为高级用户提供快速参考
- 使用清晰的语言，避免行话

### 4. 保持更新

- 定期检查过时信息
- 更新截图和示例代码
- 跟随技术栈版本更新

### 5. 提供多种学习路径

- 快速开始指南
- 详细教程
- API 参考
- 常见问题解答

## 常见问题

### Q1: 如何组织大型文档？

使用清晰的目录结构：
- `/guide/` - 概念和指南
- `/api/` - API 参考
- `/tutorials/` - 手把手教程
- `/reference/` - 配置和 CLI 参考

### Q2: 如何处理多语言文档？

\```
docs/
├── en/
│   ├── guide/
│   └── api/
└── zh/
    ├── guide/
    └── api/
\```

### Q3: 如何管理文档版本？

使用 Git 分支或 VitePress 的多版本功能：

\```typescript
export default {
  themeConfig: {
    nav: [
      {
        text: 'v2.0',
        items: [
          { text: 'v2.0', link: '/v2/' },
          { text: 'v1.0', link: '/v1/' }
        ]
      }
    ]
  }
}
\```

## 相关资源

- [VitePress 文档](https://vitepress.dev/)
- [Docusaurus 文档](https://docusaurus.io/)
- [Markdown 指南](https://www.markdownguide.org/)
- [写作风格指南](https://developers.google.com/style)
```

---

## 配套的 settings.json

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Glob",
      "Grep",
      "Bash(npm:*)",
      "Bash(npx:*)",
      "Bash(git:*)",
      "WebSearch",
      "WebFetch(domain:docs.anthropic.com)",
      "WebFetch(domain:vitepress.dev)",
      "WebFetch(domain:docusaurus.io)"
    ],
    "deny": [
      "Read(node_modules/**)",
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ],
    "ask": [
      "Bash(git push:*)",
      "Bash(npm publish:*)"
    ]
  }
}
```

---

## 快速开始

### 1. 创建新文档项目

**使用 VitePress**:
\```bash
npm create vitepress@latest
cd my-docs
npm install
\```

**使用 Docusaurus**:
\```bash
npx create-docusaurus@latest my-docs classic
cd my-docs
\```

### 2. 复制配置

\```bash
# 复制 CLAUDE.md
cp /path/to/claude-code-guide/docs/templates/documentation-project.md ./CLAUDE.md

# 创建配置
mkdir -p .claude
# 创建 .claude/settings.json
\```

### 3. 开始编写

\```bash
npm run docs:dev
claude
\```

---

## 更多模板

- [Python/Shell 项目模板](./python-shell-project.md)
- [Next.js 项目模板](./nextjs-project.md)
