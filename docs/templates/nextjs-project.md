# Next.js 全栈项目配置模板

适用于 Next.js App Router、TypeScript、Tailwind CSS 等现代 Web 开发项目。

---

## CLAUDE.md 模板

将以下内容保存为项目根目录的 `CLAUDE.md` 文件：

```markdown
# 项目名称

## 项目概述

**项目类型**: Next.js 15 全栈 Web 应用
**主要用途**: 前后端一体化开发、SSR/SSG 应用
**技术栈**: Next.js 15, TypeScript, Tailwind CSS, React Query
**开发模式**: 现代化 Web 开发，类型安全，组件化设计

## 技术栈详情

### 核心框架
- **Next.js 15**: React 框架（App Router）
- **React 18**: UI 库
- **TypeScript 5**: 类型安全

### 样式和 UI
- **Tailwind CSS**: 原子化 CSS
- **shadcn/ui**: 可复用组件库
- **Radix UI**: 无样式基础组件

### 状态和数据
- **React Query**: 服务端状态管理
- **Zustand** (可选): 客户端状态管理
- **Prisma** (可选): ORM 数据库

### 开发工具
- **ESLint**: 代码检查
- **Prettier**: 代码格式化
- **Husky**: Git hooks
- **Jest + React Testing Library**: 测试

## 项目结构

\```
src/
├── app/                      # Next.js App Router
│   ├── layout.tsx           # 根布局
│   ├── page.tsx             # 首页
│   ├── globals.css          # 全局样式
│   ├── api/                 # API 路由
│   │   ├── auth/
│   │   │   └── route.ts
│   │   └── users/
│   │       └── route.ts
│   ├── dashboard/           # 仪表板页面
│   │   ├── page.tsx
│   │   └── layout.tsx
│   └── (auth)/              # 路由组
│       ├── login/
│       │   └── page.tsx
│       └── register/
│           └── page.tsx
├── components/              # React 组件
│   ├── ui/                  # shadcn/ui 组件
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   └── ...
│   ├── layout/              # 布局组件
│   │   ├── header.tsx
│   │   ├── footer.tsx
│   │   └── sidebar.tsx
│   ├── forms/               # 表单组件
│   │   ├── login-form.tsx
│   │   └── user-form.tsx
│   └── shared/              # 共享组件
│       ├── loading.tsx
│       └── error.tsx
├── lib/                     # 工具库
│   ├── api.ts              # API 客户端
│   ├── utils.ts            # 通用工具函数
│   ├── db.ts               # 数据库连接 (如使用 Prisma)
│   └── auth.ts             # 认证工具
├── hooks/                   # 自定义 Hooks
│   ├── use-user.ts
│   ├── use-auth.ts
│   └── use-debounce.ts
├── types/                   # TypeScript 类型
│   ├── index.ts
│   ├── api.ts
│   └── models.ts
├── styles/                  # 额外样式
│   └── custom.css
└── config/                  # 配置文件
    ├── site.ts
    └── navigation.ts

public/
├── images/
├── icons/
└── fonts/

prisma/                      # Prisma 配置 (可选)
├── schema.prisma
└── migrations/

tests/
├── unit/
├── integration/
└── e2e/

.env.example                 # 环境变量示例
.env.local                   # 本地环境变量 (不提交)
next.config.js               # Next.js 配置
tailwind.config.ts           # Tailwind 配置
tsconfig.json                # TypeScript 配置
package.json
\```

## 常用命令

### 开发

\```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev
# 访问: http://localhost:3000

# 构建生产版本
npm run build

# 启动生产服务器
npm start

# 类型检查
npm run type-check
# 或
npx tsc --noEmit
\```

### 代码质量

\```bash
# ESLint 检查
npm run lint

# 自动修复
npm run lint:fix

# Prettier 格式化
npm run format

# 检查格式
npm run format:check
\```

### 测试

\```bash
# 运行所有测试
npm test

# 监听模式
npm run test:watch

# 测试覆盖率
npm run test:coverage

# E2E 测试 (Playwright)
npm run test:e2e
\```

### 数据库（如使用 Prisma）

\```bash
# 生成 Prisma Client
npx prisma generate

# 运行迁移
npx prisma migrate dev

# 重置数据库
npx prisma migrate reset

# Prisma Studio（数据库 GUI）
npx prisma studio
\```

## 代码规范

### TypeScript 规范

- **启用严格模式**: `"strict": true` in tsconfig.json
- **所有组件使用 TypeScript**
- **Props 必须定义接口**

\```typescript
// ✅ 好的做法
interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
}

export function Button({ children, onClick, variant = 'primary', disabled }: ButtonProps) {
  // ...
}

// ❌ 避免
export function Button({ children, onClick, variant, disabled }: any) {
  // ...
}
\```

### React 组件规范

#### 文件命名
- **组件文件**: PascalCase - `UserProfile.tsx`
- **工具文件**: kebab-case - `format-date.ts`
- **目录**: kebab-case - `user-profile/`

#### Server vs Client Components

\```tsx
// Server Component (默认，无需标注)
export default function Page() {
  return <div>Server Component</div>
}

// Client Component (需要标注)
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(count + 1)}>{count}</button>
}
\```

#### 组件结构顺序

\```tsx
'use client'  // 1. 客户端指令（如需要）

import { ... }  // 2. 导入

interface Props { ... }  // 3. 类型定义

export function Component({ prop1, prop2 }: Props) {  // 4. 组件定义
  // 5. Hooks
  const [state, setState] = useState()
  const query = useQuery()

  // 6. 事件处理函数
  const handleClick = () => { }

  // 7. 副作用
  useEffect(() => { }, [])

  // 8. 渲染
  return (
    <div>
      {/* JSX */}
    </div>
  )
}
\```

### CSS 和样式规范

#### Tailwind 工具类

\```tsx
// ✅ 使用 Tailwind 工具类
<button className="rounded-lg bg-blue-500 px-4 py-2 text-white hover:bg-blue-600">
  点击
</button>

// ✅ 使用 cn() 工具函数合并类名
import { cn } from '@/lib/utils'

<button className={cn(
  "rounded-lg px-4 py-2",
  variant === 'primary' && "bg-blue-500 text-white",
  variant === 'secondary' && "bg-gray-200 text-gray-900"
)}>
  点击
</button>
\```

#### CSS Modules（可选）

\```tsx
// Button.module.css
.button {
  @apply rounded-lg px-4 py-2;
}

// Button.tsx
import styles from './Button.module.css'
<button className={styles.button}>点击</button>
\```

### 路由规范

#### App Router 文件约定

| 文件 | 用途 |
|------|------|
| `layout.tsx` | 共享布局 |
| `page.tsx` | 页面唯一入口 |
| `loading.tsx` | 加载 UI |
| `error.tsx` | 错误 UI |
| `not-found.tsx` | 404 页面 |
| `route.ts` | API 路由 |

#### 路由组织

\```
app/
├── (marketing)/          # 路由组（不影响URL）
│   ├── about/
│   └── pricing/
├── (app)/               # 另一个路由组
│   ├── dashboard/
│   └── settings/
└── api/                 # API 路由
    └── users/
        └── route.ts
\```

## API 路由开发

### API Route Handler

\```typescript
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server'

// GET /api/users
export async function GET(request: NextRequest) {
  try {
    const users = await db.user.findMany()
    return NextResponse.json(users)
  } catch (error) {
    return NextResponse.json(
      { error: '获取用户失败' },
      { status: 500 }
    )
  }
}

// POST /api/users
export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const user = await db.user.create({ data: body })
    return NextResponse.json(user, { status: 201 })
  } catch (error) {
    return NextResponse.json(
      { error: '创建用户失败' },
      { status: 500 }
    )
  }
}
\```

### 动态路由

\```typescript
// app/api/users/[id]/route.ts
export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  const user = await db.user.findUnique({
    where: { id: params.id }
  })

  if (!user) {
    return NextResponse.json(
      { error: '用户不存在' },
      { status: 404 }
    )
  }

  return NextResponse.json(user)
}
\```

## 数据获取

### Server Component 数据获取

\```tsx
// app/users/page.tsx
async function getUsers() {
  const res = await fetch('https://api.example.com/users', {
    cache: 'no-store'  // 不缓存
    // cache: 'force-cache'  // 永久缓存
    // next: { revalidate: 60 }  // 60秒后重新验证
  })
  return res.json()
}

export default async function UsersPage() {
  const users = await getUsers()
  return (
    <div>
      {users.map(user => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  )
}
\```

### Client Component 数据获取（React Query）

\```tsx
'use client'

import { useQuery } from '@tanstack/react-query'
import { getUsers } from '@/lib/api'

export function UserList() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: getUsers
  })

  if (isLoading) return <div>加载中...</div>
  if (error) return <div>错误: {error.message}</div>

  return (
    <div>
      {data?.map(user => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  )
}
\```

## 环境变量

### 创建 `.env.example`

\```bash
# 数据库
DATABASE_URL=postgresql://user:password@localhost:5432/mydb

# NextAuth
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=your-secret-here

# API
NEXT_PUBLIC_API_URL=https://api.example.com

# 第三方服务
NEXT_PUBLIC_STRIPE_KEY=pk_test_xxx
STRIPE_SECRET_KEY=sk_test_xxx
\```

### 使用环境变量

\```typescript
// 服务端可以访问所有变量
const dbUrl = process.env.DATABASE_URL

// 客户端只能访问 NEXT_PUBLIC_ 前缀的变量
const apiUrl = process.env.NEXT_PUBLIC_API_URL
\```

### 类型安全的环境变量

\```typescript
// config/env.ts
import { z } from 'zod'

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  NEXTAUTH_SECRET: z.string().min(32),
  NEXT_PUBLIC_API_URL: z.string().url(),
})

export const env = envSchema.parse(process.env)
\```

## 测试规范

### 组件测试

\```typescript
// __tests__/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react'
import { Button } from '@/components/ui/button'

describe('Button', () => {
  it('renders correctly', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })

  it('calls onClick when clicked', () => {
    const handleClick = jest.fn()
    render(<Button onClick={handleClick}>Click me</Button>)
    fireEvent.click(screen.getByText('Click me'))
    expect(handleClick).toHaveBeenCalledTimes(1)
  })
})
\```

### API 路由测试

\```typescript
// __tests__/api/users.test.ts
import { GET } from '@/app/api/users/route'
import { NextRequest } from 'next/server'

describe('/api/users', () => {
  it('returns users list', async () => {
    const request = new NextRequest('http://localhost:3000/api/users')
    const response = await GET(request)
    const data = await response.json()

    expect(response.status).toBe(200)
    expect(Array.isArray(data)).toBe(true)
  })
})
\```

## 性能优化

### 图片优化

\```tsx
import Image from 'next/image'

// ✅ 使用 Next.js Image 组件
<Image
  src="/images/hero.jpg"
  alt="Hero"
  width={1200}
  height={600}
  priority  // 首屏图片优先加载
/>

// ❌ 避免使用 <img> 标签
<img src="/images/hero.jpg" alt="Hero" />
\```

### 字体优化

\```tsx
// app/layout.tsx
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({ children }) {
  return (
    <html lang="zh-CN">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
\```

### 代码分割

\```tsx
// 动态导入减小初始包体积
import dynamic from 'next/dynamic'

const HeavyComponent = dynamic(() => import('@/components/HeavyComponent'), {
  loading: () => <div>加载中...</div>,
  ssr: false  // 禁用 SSR
})
\```

## 部署

### Vercel 部署（推荐）

\```bash
# 安装 Vercel CLI
npm i -g vercel

# 登录
vercel login

# 部署
vercel

# 生产部署
vercel --prod
\```

### 自托管部署

\```bash
# 构建
npm run build

# 启动生产服务器
npm start

# 或使用 PM2
pm2 start npm --name "myapp" -- start
\```

### Docker 部署

\```dockerfile
# Dockerfile
FROM node:18-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM node:18-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM node:18-alpine AS runner
WORKDIR /app
ENV NODE_ENV production
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static

EXPOSE 3000
CMD ["node", "server.js"]
\```

## Git 提交规范

### Conventional Commits

\```bash
feat: 添加用户登录功能
fix: 修复分页组件样式问题
docs: 更新 API 文档
style: 格式化代码
refactor: 重构用户服务
test: 添加登录表单测试
chore: 升级 Next.js 到 15.0
\```

## 常见问题

### Q1: Hydration 错误

**原因**: 服务端和客户端渲染不一致

**解决**:
- 检查是否在 Server Component 中使用了客户端 API
- 使用 `suppressHydrationWarning` 属性（临时）
- 将需要客户端状态的部分提取为 Client Component

### Q2: 环境变量未生效

**解决**:
- 确保变量名以 `NEXT_PUBLIC_` 开头（客户端）
- 重启开发服务器
- 检查 `.env.local` 文件是否存在

### Q3: TypeScript 类型错误

**解决**:
\```bash
# 删除类型缓存
rm -rf .next
rm -rf node_modules/.cache

# 重新生成类型
npm run dev
\```

## 相关资源

- [Next.js 官方文档](https://nextjs.org/docs)
- [React 官方文档](https://react.dev/)
- [TypeScript 手册](https://www.typescriptlang.org/docs/)
- [Tailwind CSS 文档](https://tailwindcss.com/docs)
- [shadcn/ui 组件](https://ui.shadcn.com/)
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
      "Bash(node:*)",
      "WebSearch",
      "WebFetch(domain:docs.anthropic.com)",
      "WebFetch(domain:nextjs.org)",
      "WebFetch(domain:react.dev)"
    ],
    "deny": [
      "Read(.env)",
      "Read(.env.local)",
      "Read(.env.production)",
      "Read(node_modules/**)",
      "Write(.env.local)",
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ],
    "ask": [
      "Bash(npm install:*)",
      "Bash(npm publish:*)",
      "Bash(git push:*)",
      "Bash(vercel:*)"
    ]
  }
}
```

---

## 快速开始

### 1. 创建新项目

\```bash
# 使用 create-next-app
npx create-next-app@latest my-app --typescript --tailwind --app --src-dir

cd my-app
\```

### 2. 复制配置

\```bash
# 复制 CLAUDE.md
cp /path/to/claude-code-guide/docs/templates/nextjs-project.md ./CLAUDE.md

# 创建配置目录和文件
mkdir -p .claude
# 创建 .claude/settings.json（使用上面的配置）
\```

### 3. 启动开发

\```bash
npm run dev
claude
\```

---

## 更多模板

- [Python/Shell 项目模板](./python-shell-project.md)
- [文档项目模板](./documentation-project.md)
