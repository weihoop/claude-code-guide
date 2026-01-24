# Frontend Design

前端设计专用 Skill，帮你去掉 AI 的通用美学（紫色渐变、Inter 字体等），创建真正有设计感的前端界面。

## 功能简介

Frontend Design Skill 专注于创建有设计感的前端界面，避免 AI 生成的"通用美学"，支持 React + Tailwind CSS。

### 核心特点

- ✅ **避免通用美学**: 不使用 Inter 字体、紫色渐变等 AI 常见模式
- ✅ **设计感优先**: 根据设计复杂度调整代码复杂度
- ✅ **现代技术栈**: React + Tailwind CSS + shadcn/ui
- ✅ **生产级代码**: 可直接用于生产环境

### 适用场景

| 场景 | 说明 |
|------|------|
| **产品页面** | Landing Page、产品介绍 |
| **企业官网** | 公司网站、品牌展示 |
| **SaaS 应用** | 管理后台、用户界面 |
| **创意项目** | 个人作品集、艺术项目 |

---

## 仓库信息

### 官方版本

- **GitHub**: [anthropics/claude-code](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design)
- **维护者**: Anthropic 官方
- **路径**: `plugins/frontend-design/skills/frontend-design`

### 社区版本

- **GitHub**: [Koomook/claude-frontend-skills](https://github.com/Koomook/claude-frontend-skills)
- **维护者**: [@Koomook](https://github.com/Koomook)

### 参考资源

- [Frontend Design Pro Demo](https://github.com/claudekit/frontend-design-pro-demo)

---

## 安装方法

### 方式 1：从官方仓库安装（推荐）

```bash
cd ~/.config/claude-code/skills/

# 使用 sparse checkout 只下载需要的部分
git clone --depth 1 --filter=blob:none --sparse https://github.com/anthropics/claude-code
cd claude-code
git sparse-checkout set plugins/frontend-design

# 复制到 skills 目录
cp -r plugins/frontend-design/skills/frontend-design ~/.config/claude-code/skills/

# 清理临时文件
cd ..
rm -rf claude-code
```

### 方式 2：从社区版本安装

```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/Koomook/claude-frontend-skills frontend-design
```

### 验证安装

```bash
head ~/.config/claude-code/skills/frontend-design/SKILL.md
```

---

## 配置和使用

### 基础使用

```
用户: "创建一个科技公司的 Landing Page，有设计感"

Claude: [使用 frontend-design skill]
- 避免使用 Inter 字体
- 不使用紫色渐变
- 选择独特的配色方案
- 使用现代设计元素
```

### 设计原则

Frontend Design Skill 遵循以下原则：

1. **避免 AI 通用美学**:
   - ❌ Inter 字体
   - ❌ 紫色/蓝色渐变
   - ❌ 圆角卡片堆叠
   - ❌ 千篇一律的布局

2. **创建独特设计**:
   - ✅ 选择独特的字体组合
   - ✅ 大胆的配色方案
   - ✅ 创新的布局方式
   - ✅ 有个性的视觉元素

---

## 使用示例

### 示例 1：产品 Landing Page

```
用户: "为一个 AI 写作工具创建 Landing Page"

生成内容：
- Hero 区域：大胆的排版，独特的字体
- 功能展示：卡片式布局，但避免千篇一律
- Call to Action：有设计感的按钮和交互
- 配色：避免紫色渐变，使用品牌色

技术栈：
- React + TypeScript
- Tailwind CSS
- Framer Motion（动画）
```

### 示例 2：企业官网

```
用户: "创建一个设计咨询公司的官网首页"

生成内容：
- 简洁的导航栏
- 全屏 Hero 区域，突出设计感
- 案例展示：网格布局
- 团队介绍：创意布局
- 联系表单：简洁优雅

设计重点：
- 强调视觉层次
- 使用高质量图片占位符
- 精心选择字体组合
```

### 示例 3：SaaS 应用界面

```
用户: "创建一个数据分析平台的仪表板"

生成内容：
- 侧边栏导航
- 数据卡片：避免通用设计
- 图表展示：使用 Recharts
- 响应式布局

特点：
- 专业的数据可视化
- 清晰的信息架构
- 良好的用户体验
```

---

## 技术栈

### 默认技术栈

```
- React 18+
- TypeScript
- Tailwind CSS
- shadcn/ui（组件库）
- Lucide React（图标）
- Framer Motion（动画，可选）
```

### 组件示例

使用 shadcn/ui 组件：

```tsx
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"

export default function Hero() {
  return (
    <div className="container mx-auto px-4">
      <h1 className="text-6xl font-bold">
        独特的标题设计
      </h1>
      <Button variant="default" size="lg">
        开始使用
      </Button>
    </div>
  )
}
```

---

## 设计复杂度调整

Frontend Design Skill 会根据设计复杂度调整代码复杂度：

### 简单设计

```
设计复杂度：低
代码复杂度：低
  ↓
使用基础 Tailwind 类
简单的组件结构
最少的状态管理
```

### 中等设计

```
设计复杂度：中
代码复杂度：中
  ↓
使用 shadcn/ui 组件
适度的动画效果
基础的交互逻辑
```

### 复杂设计

```
设计复杂度：高
代码复杂度：高
  ↓
自定义组件
复杂的动画
高级交互效果
状态管理（zustand/jotai）
```

---

## 最佳实践

### 1. 明确设计风格

```
用户提示：
"创建一个极简风格的作品集网站"
"使用 Brutalism 风格设计一个音乐平台"
"Neo-morphism 风格的天气应用"
```

### 2. 提供设计参考

```
用户提示：
"参考 Apple 官网的设计风格"
"类似 Stripe 的 Landing Page"
"受 Dribbble 上 XX 作品启发"
```

### 3. 指定配色方案

```
用户提示：
"使用暗色系配色"
"品牌色：#FF6B6B"
"渐变色：从橙色到粉色"
```

### 4. 响应式要求

```
用户提示：
"移动端优先设计"
"确保在平板和桌面都好看"
"使用 Tailwind 响应式断点"
```

---

## 常见问题

### 生成的设计还是很通用

**解决方法**:
1. 明确指出要避免的元素
2. 提供具体的设计参考
3. 指定独特的配色和字体
4. 强调设计的独特性

### 代码无法运行

**原因**:
- 缺少必要的依赖

**解决方法**:
```bash
npm install react react-dom
npm install -D tailwindcss postcss autoprefixer
npm install @radix-ui/react-* # shadcn/ui 依赖
npm install lucide-react
```

### Tailwind 样式不生效

**解决方法**:
1. 确保 `tailwind.config.js` 配置正确
2. 检查 `postcss.config.js`
3. 确认 CSS 入口文件包含 Tailwind 指令

---

## 进阶技巧

### 自定义主题

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#...',
          // ... 自定义品牌色
        }
      },
      fontFamily: {
        sans: ['Custom Font', 'sans-serif']
      }
    }
  }
}
```

### 动画效果

```tsx
import { motion } from 'framer-motion'

<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5 }}
>
  内容
</motion.div>
```

---

## 参考资料

### 官方资源

- [Frontend Design Skill](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design)
- [Frontend Design Pro Demo](https://github.com/claudekit/frontend-design-pro-demo)

### 技术文档

- [React 文档](https://react.dev/)
- [Tailwind CSS 文档](https://tailwindcss.com/)
- [shadcn/ui 组件](https://ui.shadcn.com/)

### 设计灵感

- [Dribbble](https://dribbble.com/)
- [Behance](https://www.behance.net/)
- [Awwwards](https://www.awwwards.com/)

---

**最后更新**: 2026-01-24
**难度**: ⭐⭐ 中等
**推荐指数**: ⭐⭐⭐⭐

[返回 Top 10 列表](README.md) | [返回主页](../README.md)
