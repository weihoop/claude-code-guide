---
name: build
description: 构建项目并检查错误和警告
aliases: [b, make, compile]
---

# 智能构建流程

自动检测项目类型，执行构建，分析错误和警告，并提供优化建议。

## 执行步骤

### 1. 检测项目类型和构建工具

自动识别项目使用的构建工具：

**JavaScript/TypeScript**
- Webpack (`webpack.config.js`)
- Vite (`vite.config.js`)
- Rollup (`rollup.config.js`)
- Parcel
- esbuild
- npm scripts (`package.json` 中的 `build` 脚本)

**Python**
- setuptools (`setup.py`)
- Poetry (`pyproject.toml`)
- flit

**Go**
- go build

**Java**
- Maven (`pom.xml`)
- Gradle (`build.gradle`)

**Rust**
- Cargo (`Cargo.toml`)

### 2. 清理旧构建

在构建前清理旧的构建产物：

```bash
# JavaScript
rm -rf dist/ build/

# Python
rm -rf dist/ build/ *.egg-info/

# Go
go clean

# Java (Maven)
mvn clean
```

### 3. 执行构建

根据检测到的工具执行相应的构建命令：

```bash
# JavaScript/TypeScript
npm run build
# 或
yarn build
# 或
pnpm build

# Python
python setup.py build
# 或
poetry build

# Go
go build -o bin/app ./cmd/app

# Java
mvn package
# 或
gradle build

# Rust
cargo build --release
```

### 4. 监控构建过程

实时显示构建进度和状态：

```
🔨 开始构建...

[1/5] 清理旧构建产物... ✅
[2/5] 编译 TypeScript... ⏳
[3/5] 打包资源文件...
[4/5] 代码压缩优化...
[5/5] 生成 Source Map...
```

### 5. 分析构建结果

#### 成功情况

```
✅ 构建成功！

构建统计：
- 耗时：12.3s
- 输出目录：dist/
- 文件数量：15 个
- 总大小：2.4 MB

主要产物：
- index.html (3.2 KB)
- main.js (856 KB)
- main.css (124 KB)
- assets/ (1.4 MB)

性能指标：
- Bundle 大小：适中
- 压缩率：65%
- Tree-shaking：已启用
```

#### 失败情况

详细分析构建错误：

```
❌ 构建失败

错误详情：

【错误 1】TypeScript 编译错误
文件：src/api/user.ts:45:12
错误：Property 'email' does not exist on type 'User'

分析：
- User 类型定义缺少 email 属性
- 或者使用了错误的类型

修复建议：
1. 在 User 接口中添加 email 属性
2. 或检查是否使用了正确的类型

【错误 2】模块未找到
文件：src/utils/helper.js:3
错误：Cannot find module 'lodash'

分析：
- 依赖 lodash 未安装
- 或 import 路径错误

修复建议：
运行：npm install lodash
```

#### 警告情况

```
⚠️ 构建完成，但有 3 个警告

【警告 1】Bundle 体积过大
文件：dist/main.js (2.5 MB)

建议：
- 使用代码分割（Code Splitting）
- 启用 Tree-shaking
- 检查是否引入了不必要的依赖

【警告 2】未使用的导出
文件：src/utils/format.ts

建议：
- 移除未使用的导出函数
- 或标记为内部使用

【警告 3】Source Map 较大
文件：dist/main.js.map (5.2 MB)

建议：
- 生产环境禁用 Source Map
- 或使用 hidden-source-map
```

### 6. 检查构建产物

验证构建输出的完整性和质量：

```bash
# 检查文件是否生成
ls -lh dist/

# 检查文件大小
du -sh dist/

# 验证文件内容
file dist/main.js
```

#### 质量检查

- [ ] 所有必需文件已生成
- [ ] 文件大小合理（bundle < 1MB 为佳）
- [ ] 压缩已生效
- [ ] Source Map 已生成（开发环境）
- [ ] 资源文件正确复制

### 7. 性能分析

分析构建产物的性能：

```markdown
## 性能分析报告

### Bundle 分析

**主要依赖占用**:
- react: 125 KB (15%)
- lodash: 85 KB (10%)
- moment: 230 KB (28%) ⚠️ 建议替换为 day.js
- ...其他

**建议优化**:
1. moment.js 体积过大，建议替换为 day.js
2. 考虑按需引入 lodash
3. 启用代码分割减少初始加载

### 构建时间分析

| 步骤 | 耗时 | 占比 |
|------|------|------|
| TypeScript 编译 | 5.2s | 42% |
| 代码压缩 | 3.8s | 31% |
| 资源处理 | 2.1s | 17% |
| 其他 | 1.2s | 10% |

**优化建议**:
- 使用 esbuild 加速 TypeScript 编译
- 启用并行压缩
- 考虑使用构建缓存
```

### 8. 生成构建报告

```markdown
## 构建报告

**构建时间**: 2025-11-30 14:45:00
**项目**: my-project
**分支**: main
**构建工具**: Webpack 5.88.0

### 构建状态

✅ 成功

### 构建信息

- **耗时**: 12.3秒
- **模式**: production
- **Node 版本**: v18.17.0
- **构建目录**: dist/

### 输出文件

| 文件 | 大小 | Gzip 后 |
|------|------|---------|
| index.html | 3.2 KB | 1.8 KB |
| main.js | 856 KB | 312 KB |
| main.css | 124 KB | 28 KB |
| vendor.js | 245 KB | 89 KB |
| runtime.js | 12 KB | 5 KB |

**总计**: 1.24 MB (未压缩) / 435 KB (Gzip)

### 编译统计

- **模块数**: 342
- **Chunks**: 3
- **Assets**: 15
- **警告**: 0
- **错误**: 0

### 性能指标

| 指标 | 值 | 状态 |
|------|-----|------|
| Bundle 大小 | 856 KB | ⚠️ 偏大 |
| Gzip 压缩率 | 64% | ✅ 良好 |
| 模块数量 | 342 | ✅ 正常 |
| Tree-shaking | 启用 | ✅ |

### 优化建议

1. **减小 Bundle 体积**
   - 使用动态导入进行代码分割
   - 移除未使用的依赖
   - 优化图片资源

2. **加快构建速度**
   - 启用持久化缓存
   - 使用 thread-loader
   - 减少 loader 处理范围

3. **提升运行性能**
   - 使用 CDN 加载大型库
   - 启用浏览器缓存
   - 实施资源懒加载
```

## 构建优化策略

### 1. 代码分割

```javascript
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 10
        },
        common: {
          minChunks: 2,
          priority: 5,
          reuseExistingChunk: true
        }
      }
    }
  }
};
```

### 2. Tree Shaking

确保使用 ES6 模块：

```javascript
// ✅ 支持 Tree Shaking
import { formatDate } from './utils';

// ❌ 不支持 Tree Shaking
const utils = require('./utils');
```

### 3. 压缩优化

```javascript
// webpack.config.js
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
  optimization: {
    minimizer: [
      new TerserPlugin({
        parallel: true,
        terserOptions: {
          compress: {
            drop_console: true,  // 移除 console
          },
        },
      }),
    ],
  },
};
```

### 4. 资源优化

```javascript
// 图片压缩
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpg|gif)$/,
        use: [
          {
            loader: 'image-webpack-loader',
            options: {
              mozjpeg: { progressive: true, quality: 65 },
              optipng: { enabled: false },
              pngquant: { quality: [0.65, 0.90], speed: 4 },
            },
          },
        ],
      },
    ],
  },
};
```

### 5. 缓存策略

```javascript
module.exports = {
  output: {
    filename: '[name].[contenthash].js',
  },
  cache: {
    type: 'filesystem',
  },
};
```

## 常见构建问题

### 1. 内存不足

```bash
# 增加 Node.js 内存限制
NODE_OPTIONS=--max_old_space_size=4096 npm run build
```

### 2. 构建超时

```javascript
// 增加构建超时时间
module.exports = {
  performance: {
    maxAssetSize: 512000,
    maxEntrypointSize: 512000,
  },
};
```

### 3. 依赖冲突

```bash
# 清理并重新安装依赖
rm -rf node_modules package-lock.json
npm install
```

### 4. 路径问题

```javascript
// 使用绝对路径
const path = require('path');

module.exports = {
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
};
```

## 多环境构建

### 开发环境

```bash
npm run build:dev
```

特点：
- 快速构建
- Source Map 完整
- 不压缩代码
- 包含调试信息

### 生产环境

```bash
npm run build:prod
```

特点：
- 完全优化
- 代码压缩
- Tree Shaking
- 移除 console
- 最小化 Source Map

### 测试环境

```bash
npm run build:test
```

特点：
- 平衡构建速度和优化
- 保留必要的调试信息
- 中等程度压缩

## 构建后操作

### 1. 验证构建

```bash
# 启动本地服务器测试
npx serve dist/

# 或使用 http-server
npx http-server dist/
```

### 2. 分析 Bundle

```bash
# Webpack Bundle Analyzer
npm run build -- --analyze

# 或手动安装
npm install -D webpack-bundle-analyzer
```

### 3. 性能测试

使用 Lighthouse 测试构建产物性能。

### 4. 准备部署

```bash
# 压缩构建产物
tar -czf build.tar.gz dist/

# 或创建部署包
npm run build && zip -r build.zip dist/
```
