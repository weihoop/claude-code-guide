# Claude 开发助手配置

> 这是一个 Claude Code 全局配置模板，可根据个人需求自定义。

## 工作偏好

### 交流语言设置
- **沟通语言**: 中文
- **输出语言**: 中文
- **注释语言**: 中文
- **文档语言**: 中文

## 项目信息

### 技术栈
- **主要语言**: Python, JavaScript/TypeScript, Bash
- **开发框架**: 根据项目选择
- **代码风格**: 清晰、可维护、有注释

### 代码规范
- 使用有意义的变量和函数名
- 关键逻辑添加注释说明
- 保持代码简洁，避免过度设计
- 完善的错误处理

## 开发规范

### Git 提交规范

提交信息使用中文，采用以下格式：

```
<类型>: <简短描述>

[可选的详细说明]
```

#### 提交类型

| 类型 | 说明 | 示例 |
|------|------|------|
| feat | 新功能 | `feat: 添加用户登录功能` |
| fix | 修复bug | `fix: 修复空指针异常` |
| docs | 文档更新 | `docs: 更新API文档` |
| style | 代码格式 | `style: 统一代码缩进` |
| refactor | 重构 | `refactor: 优化数据库查询` |
| perf | 性能优化 | `perf: 提升列表渲染性能` |
| test | 测试 | `test: 添加单元测试` |
| chore | 其他 | `chore: 更新依赖版本` |

#### 提交原则
- 每次提交只做一件事
- 提交信息清晰描述改动内容
- 不使用 emoji 表情符号
- 使用祈使语气，如"添加"而不是"添加了"

### 项目配置文件

#### .claude.md
- 项目级配置文件
- 描述项目特点和开发规范
- 不提交到版本控制（添加到 .gitignore）

#### .gitignore 模板

```gitignore
# Claude Code 配置
.claude.md
CLAUDE.md

# IDE
.vscode/
.idea/
*.swp

# 环境变量
.env
.env.local
.env.*.local

# 日志
*.log
logs/

# 依赖
node_modules/
venv/
__pycache__/

# 构建输出
dist/
build/
*.pyc
```

## 安全规范

### 敏感信息保护
- 不读取 `.env` 文件和包含密钥的文件
- 不在代码中硬编码密钥、密码、token
- 使用环境变量管理敏感配置
- 定期检查代码中是否有敏感信息泄露

### 代码审查要点
- 检查是否有敏感信息泄露
- 验证错误处理是否完善
- 确认输入验证是否充分
- 评估是否存在安全漏洞

## 开发工作流

### 1. 开发前
- 理解需求和目标
- 确认技术方案
- 检查现有代码和文档

### 2. 开发中
- 遵循代码规范
- 编写必要的注释
- 保持提交的原子性

### 3. 开发后
- 运行测试确保功能正常
- 检查代码质量
- 更新相关文档
- 提交代码并推送

## 常用命令

### 斜杠命令
Claude Code 提供了以下常用命令（需要在 `~/.claude/commands/` 中配置）：

- `/test` - 运行测试并分析结果
- `/review` - 代码审查
- `/build` - 构建项目并检查错误
- `/push` - 提交并推送代码
- `/fix` - 自动修复代码问题
- `/update` - 更新项目依赖
- `/deploy` - 部署到指定环境
- `/doc` - 更新项目文档

## 最佳实践

### 错误处理
```python
# Python 示例
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"操作失败: {e}")
    raise
```

```javascript
// JavaScript 示例
try {
  const result = await riskyOperation();
} catch (error) {
  console.error('操作失败:', error);
  throw error;
}
```

### 日志记录
- 使用统一的日志格式
- 记录关键操作和错误
- 避免记录敏感信息

### 测试编写
- 为核心功能编写测试
- 测试边界条件和异常情况
- 保持测试的独立性

## 项目初始化

### Python 项目
```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt
```

### Node.js 项目
```bash
# 安装依赖
npm install
# 或
yarn install

# 运行开发服务器
npm run dev
```

## 自定义说明

> 💡 **提示**: 你可以在下方添加个人或团队的特定规范和偏好

### 个人偏好
- （在此添加你的个人开发偏好）

### 团队规范
- （在此添加团队协作规范）

### 常用资源
- （在此添加常用文档和工具链接）

---

## 相关文档

- [Claude Code 官方文档](https://docs.anthropic.com/claude-code)
- [Claude Code 中文手册](https://github.com/weihoop/claude-code-guide)
