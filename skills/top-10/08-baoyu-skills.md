# 宝玉 Skills

宝玉老师出品的 Skill 套件，包含写长文自动配图、自动发帖、发公众号等实用功能。

## 功能简介

宝玉 Skills 是由 [@JimLiu](https://github.com/JimLiu)（宝玉老师）开发的自媒体创作工具包，覆盖从内容生成到发布的完整流程。

### 核心特点

- ✅ **内容生成**: 小红书信息图、文章配图、封面图
- ✅ **发布自动化**: 支持 Twitter/X、微信公众号
- ✅ **图片处理**: 自动压缩、格式转换
- ✅ **浏览器自动化**: 绕过平台的自动化检测

### 主要功能分类

| 分类 | 功能 | 适用场景 |
|------|------|---------|
| **内容生成** | 信息图、配图、封面 | 自媒体创作 |
| **发布** | Twitter/X、微信公众号 | 多平台发布 |
| **工具** | 图片压缩、Gemini 集成 | 辅助工具 |

---

## 仓库信息

- **GitHub**: [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills)
- **维护者**: [@JimLiu](https://github.com/JimLiu) (宝玉)
- **网站**: [baoyu.io](https://baoyu.io/)
- **License**: 开源

### 相关版本

- **台湾版本**: [yelban/baoyu-skills.TW](https://github.com/yelban/baoyu-skills.TW)

---

## 安装方法

### 方式 1：通过插件安装（推荐）

```bash
# 内容创作技能包
/plugin install content-skills@baoyu-skills

# AI生成技能包
/plugin install ai-generation-skills@baoyu-skills

# 实用工具技能包
/plugin install utility-skills@baoyu-skills
```

### 方式 2：手动安装

```bash
cd ~/.config/claude-code/skills/
git clone https://github.com/JimLiu/baoyu-skills
```

### 验证安装

```bash
ls -la ~/.config/claude-code/skills/baoyu-skills/
head ~/.config/claude-code/skills/baoyu-skills/SKILL.md
```

---

## 核心功能

### 1. 内容生成类

#### 小红书信息图生成器

生成 1-10 张卡通风格的信息图，适合小红书发布。

```
用户: "生成一篇关于健康饮食的小红书笔记，包含5张信息图"

Claude:
✅ 已生成 5 张信息图：
1. 封面：健康饮食的5大原则
2. 原则1：多吃蔬菜水果
3. 原则2：控制糖分摄入
4. 原则3：选择优质蛋白
5. 原则4：注意水分补充

[生成卡通风格的PNG图片]
```

#### 文章配图生成器

分析文章内容，在需要视觉辅助的位置生成插图。

```
用户: "为这篇技术文章生成配图"
[提供文章内容]

Claude:
分析文章结构...
建议添加 3 张配图：
1. 第 2 段：系统架构图
2. 第 5 段：数据流程图
3. 第 8 段：性能对比图

[生成配图]
```

#### 其他生成功能

- **封面图生成**: 自动生成文章封面
- **幻灯片制作**: PPT 生成
- **漫画创作**: 多格漫画生成

### 2. 发布类

#### 发布到 Twitter/X

支持普通推文（带图）和 X Articles（长文 Markdown）。

```
用户: "将这段内容发布到 Twitter"

Claude:
[连接 Twitter API]
✅ 推文已发布
链接：https://twitter.com/user/status/...
包含 2 张图片
```

#### 发布到微信公众号

使用真实 Chrome 浏览器通过 CDP 绕过自动化检测。

```
用户: "将这篇文章发布到微信公众号"

Claude:
[启动 Chrome 浏览器]
[登录微信公众号后台]
[上传图片]
[发布文章]
✅ 文章已发布为草稿，请在公众号后台确认发布
```

**特点**:
- 使用 Chrome DevTools Protocol (CDP)
- 绕过微信的自动化检测
- 支持图文混排

### 3. 工具类

#### 图片压缩

自动压缩图片，满足平台限制。

```
用户: "压缩这张图片到小于 2MB"

Claude:
原始大小：5.2 MB
压缩后：1.8 MB
质量：95%
✅ 压缩完成
```

#### Gemini 网页集成

在 Claude 中集成 Google Gemini。

```
用户: "使用 Gemini 生成一张风景图"

Claude: [调用 Gemini API]
✅ 图片已生成
```

---

## 使用示例

### 示例 1：小红书内容创作完整流程

```
步骤 1: 生成内容
用户: "写一篇关于咖啡的小红书笔记，生成 5 张信息图"

步骤 2: 预览和调整
[查看生成的图片和文案]
[根据需要调整]

步骤 3: 导出
[下载图片]
[复制文案]
[手动发布到小红书]
```

### 示例 2：技术博客发布流程

```
步骤 1: 撰写文章
[使用 Claude 辅助撰写]

步骤 2: 生成配图
用户: "为这篇文章生成合适的配图"

步骤 3: 发布到 Twitter
用户: "将摘要发布到 Twitter"

步骤 4: 发布到公众号
用户: "将完整文章发布到微信公众号"
```

### 示例 3：多平台内容分发

```
用户: "将这篇文章同时发布到 Twitter 和微信公众号"

Claude:
1. 为 Twitter 生成摘要版（280 字符）
2. 为微信公众号准备完整版
3. 生成不同尺寸的配图
4. 发布到两个平台

✅ 发布完成：
- Twitter: https://twitter.com/...
- 微信公众号: 已保存为草稿
```

---

## 进阶配置

### 自定义图片风格

```yaml
# 配置文件示例
image_style:
  xiaohongshu:
    style: cartoon
    colors: pastel
    font: bold
  article:
    style: modern
    colors: professional
```

### Twitter API 配置

```bash
# 设置环境变量
export TWITTER_API_KEY="your-api-key"
export TWITTER_API_SECRET="your-api-secret"
export TWITTER_ACCESS_TOKEN="your-access-token"
export TWITTER_ACCESS_SECRET="your-access-secret"
```

### 微信公众号配置

```bash
# 第一次使用时需要手动登录
# 之后会保存登录状态
```

---

## 最佳实践

### 1. 小红书内容优化

```
- 使用鲜艳、卡通风格的图片
- 文案简洁有力
- 每张图片聚焦一个要点
- 封面图要吸引眼球
```

### 2. Twitter/X 发布技巧

```
- 摘要控制在 280 字符内
- 使用话题标签 #hashtag
- 附带 1-4 张图片
- 长文使用 X Articles
```

### 3. 微信公众号发布

```
- 图文混排，图片质量高
- 段落之间留白
- 使用小标题分段
- 添加引导关注
```

---

## 常见问题

### 图片生成失败

**原因**:
- API 配额用尽
- 网络连接问题

**解决方法**:
1. 检查 API key 和配额
2. 重试生成
3. 降低图片质量要求

### Twitter 发布失败

**原因**:
- API 认证过期
- 权限不足

**解决方法**:
1. 更新 Twitter API credentials
2. 检查 API 权限（需要 Write 权限）
3. 查看 Twitter API 限制

### 微信公众号无法登录

**原因**:
- 浏览器版本问题
- 登录状态过期

**解决方法**:
1. 更新 Chrome 浏览器
2. 清除浏览器缓存
3. 手动重新登录

---

## 参考资料

### 官方资源

- [宝玉 Skills 仓库](https://github.com/JimLiu/baoyu-skills)
- [宝玉的网站](https://baoyu.io/)
- [台湾版本](https://github.com/yelban/baoyu-skills.TW)

### API 文档

- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api)
- [Google Gemini API](https://ai.google.dev/docs)

### 平台规范

- [小红书社区规范](https://www.xiaohongshu.com/protocols/community)
- [微信公众平台规范](https://mp.weixin.qq.com/cgi-bin/readtemplate?t=business/faq_operation_tmpl)
- [Twitter 规则](https://help.twitter.com/en/rules-and-policies/twitter-rules)

---

**最后更新**: 2026-01-24
**难度**: ⭐⭐ 中等
**推荐指数**: ⭐⭐⭐⭐

[返回 Top 10 列表](README.md) | [返回主页](../README.md)
