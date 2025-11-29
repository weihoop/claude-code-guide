# Gemini CLI 架构与流程图

> 可视化 Gemini CLI 的架构、工作流程和最佳实践

## 📊 目录

1. [整体架构](#整体架构)
2. [工作流程](#工作流程)
3. [GEMINI.md 加载机制](#geminimd-加载机制)
4. [MCP 集成架构](#mcp-集成架构)
5. [上下文管理流程](#上下文管理流程)
6. [开发工作流](#开发工作流)

---

## 整体架构

```mermaid
graph TB
    subgraph "用户层"
        A[开发者] --> B[终端/CLI]
    end

    subgraph "Gemini CLI 核心"
        B --> C[命令解析器]
        C --> D[上下文管理器]
        C --> E[工具调度器]

        D --> D1[GEMINI.md 加载器]
        D --> D2[对话历史管理]
        D --> D3[缓存管理]

        E --> E1[内置工具]
        E --> E2[MCP 服务器]
    end

    subgraph "内置工具"
        E1 --> F1[Google Search]
        E1 --> F2[File Operations]
        E1 --> F3[Shell Commands]
        E1 --> F4[Web Fetch]
    end

    subgraph "MCP 扩展"
        E2 --> G1[GitHub MCP]
        E2 --> G2[Docker MCP]
        E2 --> G3[Custom MCP]
    end

    subgraph "AI 层"
        D --> H[Gemini 2.5 Pro]
        E --> H
        H --> I[响应生成]
    end

    I --> B

    style A fill:#e1f5ff
    style H fill:#fff4e1
    style C fill:#f0f0f0
    style D fill:#e8f5e9
    style E fill:#fce4ec
```

### 架构说明

| 组件 | 功能 | 作用 |
|------|------|------|
| **命令解析器** | 解析用户输入 | 识别命令、参数、斜杠命令 |
| **上下文管理器** | 管理上下文信息 | 加载 GEMINI.md、管理对话历史 |
| **工具调度器** | 调度工具执行 | 选择合适的工具完成任务 |
| **内置工具** | 基础功能 | 搜索、文件、Shell、网页 |
| **MCP 服务器** | 扩展功能 | 自定义集成和外部服务 |

---

## 工作流程

### 基本交互流程

```mermaid
sequenceDiagram
    participant U as 用户
    participant CLI as Gemini CLI
    participant CTX as 上下文管理器
    participant AI as Gemini 2.5 Pro
    participant Tools as 工具系统

    U->>CLI: 输入问题/命令
    CLI->>CTX: 加载上下文
    CTX->>CTX: 读取 GEMINI.md
    CTX->>CTX: 加载对话历史
    CTX-->>CLI: 返回完整上下文

    CLI->>AI: 发送请求 + 上下文
    AI->>AI: 分析任务

    alt 需要使用工具
        AI->>Tools: 调用工具
        Tools->>Tools: 执行操作
        Tools-->>AI: 返回结果
        AI->>AI: 综合结果
    end

    AI-->>CLI: 生成响应
    CLI-->>U: 显示结果
```

### 完整请求生命周期

```mermaid
flowchart TD
    Start([用户输入]) --> Parse{解析输入}

    Parse -->|斜杠命令| SlashCmd[执行斜杠命令]
    Parse -->|普通问题| LoadCtx[加载上下文]

    SlashCmd --> End([输出结果])

    LoadCtx --> LoadGlobal[加载全局 GEMINI.md]
    LoadGlobal --> LoadProject[加载项目 GEMINI.md]
    LoadProject --> LoadSubdir[加载子目录 GEMINI.md]
    LoadSubdir --> MergeCtx[合并上下文]

    MergeCtx --> SendAI[发送到 Gemini AI]
    SendAI --> Analyze{AI 分析}

    Analyze -->|需要工具| SelectTool[选择工具]
    Analyze -->|直接回答| Generate[生成响应]

    SelectTool --> ExecTool[执行工具]
    ExecTool --> ToolResult{工具结果}

    ToolResult -->|成功| Combine[综合结果]
    ToolResult -->|失败| Retry{重试?}

    Retry -->|是| ExecTool
    Retry -->|否| Error[返回错误]

    Combine --> Generate
    Error --> Generate

    Generate --> Cache[缓存结果]
    Cache --> End

    style Start fill:#e1f5ff
    style End fill:#c8e6c9
    style SendAI fill:#fff4e1
    style Error fill:#ffcdd2
```

---

## GEMINI.md 加载机制

### 分层加载流程

```mermaid
graph TD
    Start([启动 Gemini CLI]) --> CheckCwd[检查当前目录]

    CheckCwd --> FindRoot[查找项目根目录]
    FindRoot --> LoadSequence{开始加载序列}

    LoadSequence --> L1[1. 加载全局配置]
    L1 --> L1Path[~/.gemini/GEMINI.md]
    L1Path --> L1Exists{文件存在?}

    L1Exists -->|是| L1Load[加载到上下文]
    L1Exists -->|否| L2[2. 加载项目根配置]
    L1Load --> L2

    L2 --> L2Path[/project-root/GEMINI.md]
    L2Path --> L2Exists{文件存在?}

    L2Exists -->|是| L2Load[加载到上下文]
    L2Exists -->|否| L3[3. 加载子目录配置]
    L2Load --> L3

    L3 --> L3Path[/current-dir/GEMINI.md]
    L3Path --> L3Exists{文件存在?}

    L3Exists -->|是| L3Load[加载到上下文]
    L3Exists -->|否| L4[4. 扫描 @imports]
    L3Load --> L4

    L4 --> ParseImports[解析 @file.md 语法]
    ParseImports --> LoadImports[递归加载导入文件]
    LoadImports --> Merge[合并所有配置]

    Merge --> Priority{处理优先级}
    Priority --> Override[子目录覆盖项目根]
    Override --> Override2[项目根覆盖全局]

    Override2 --> Final[生成最终上下文]
    Final --> Ready([准备就绪])

    style Start fill:#e1f5ff
    style Ready fill:#c8e6c9
    style Final fill:#fff4e1
```

### 配置优先级示例

```mermaid
graph LR
    subgraph "优先级: 低"
        A[~/.gemini/GEMINI.md<br/>全局配置]
    end

    subgraph "优先级: 中"
        B[/project/GEMINI.md<br/>项目配置]
    end

    subgraph "优先级: 高"
        C[/project/src/GEMINI.md<br/>子目录配置]
    end

    A -->|被覆盖| B
    B -->|被覆盖| C
    C --> D[最终上下文]

    style A fill:#e3f2fd
    style B fill:#fff9c4
    style C fill:#c8e6c9
    style D fill:#ffecb3
```

---

## MCP 集成架构

### MCP 服务器通信流程

```mermaid
sequenceDiagram
    participant CLI as Gemini CLI
    participant Gateway as MCP Gateway
    participant Server as MCP Server
    participant External as 外部服务

    CLI->>Gateway: 发现 MCP 服务器
    Gateway->>Server: 建立连接
    Server-->>Gateway: 返回工具列表
    Gateway-->>CLI: 注册可用工具

    Note over CLI: 用户发送请求

    CLI->>CLI: AI 决定使用 MCP 工具
    CLI->>Gateway: 调用 MCP 工具
    Gateway->>Server: 转发请求
    Server->>External: 执行外部操作
    External-->>Server: 返回结果
    Server-->>Gateway: 返回结果
    Gateway-->>CLI: 返回结果
    CLI->>CLI: 整合到响应中
```

### MCP 扩展架构

```mermaid
graph TB
    subgraph "Gemini CLI 核心"
        A[工具调度器]
    end

    subgraph "MCP Gateway"
        B[MCP 客户端]
        B --> B1[认证管理]
        B --> B2[请求路由]
        B --> B3[容器化]
    end

    subgraph "MCP 服务器层"
        C1[GitHub MCP]
        C2[Docker MCP]
        C3[Database MCP]
        C4[Custom MCP]
    end

    subgraph "外部服务层"
        D1[GitHub API]
        D2[Docker Engine]
        D3[PostgreSQL]
        D4[自定义 API]
    end

    A --> B
    B --> C1
    B --> C2
    B --> C3
    B --> C4

    C1 --> D1
    C2 --> D2
    C3 --> D3
    C4 --> D4

    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C1 fill:#f0f0f0
    style C2 fill:#f0f0f0
    style C3 fill:#f0f0f0
    style C4 fill:#f0f0f0
```

---

## 上下文管理流程

### 上下文生命周期

```mermaid
stateDiagram-v2
    [*] --> 初始化

    初始化 --> 加载配置: 启动 CLI

    加载配置 --> 空上下文: 无 GEMINI.md
    加载配置 --> 有上下文: 找到 GEMINI.md

    空上下文 --> 运行中: 使用默认配置
    有上下文 --> 运行中: 使用自定义配置

    运行中 --> 累积历史: 用户交互
    累积历史 --> 运行中: 继续对话

    运行中 --> 缓存: /memory show
    缓存 --> 运行中: 显示上下文

    运行中 --> 清除: /memory clear
    清除 --> 空上下文: 重置上下文

    运行中 --> 更新配置: 修改 GEMINI.md
    更新配置 --> 重新加载
    重新加载 --> 运行中: 应用新配置

    运行中 --> [*]: /exit
```

### 上下文优化策略

```mermaid
flowchart TD
    Start([接收用户请求]) --> CheckSize{检查上下文大小}

    CheckSize -->|< 10K tokens| DirectSend[直接发送]
    CheckSize -->|10K-100K tokens| Optimize[优化上下文]
    CheckSize -->|> 100K tokens| Truncate[截断上下文]

    Optimize --> RemoveDup[移除重复内容]
    RemoveDup --> Summarize[总结旧对话]
    Summarize --> Compress[压缩非关键信息]

    Truncate --> KeepRecent[保留最近对话]
    KeepRecent --> KeepConfig[保留配置文件]
    KeepConfig --> KeepCritical[保留关键上下文]

    Compress --> SendAI[发送到 AI]
    KeepCritical --> SendAI
    DirectSend --> SendAI

    SendAI --> Monitor{监控响应质量}

    Monitor -->|质量下降| AdjustStrategy[调整策略]
    Monitor -->|质量正常| Success[完成]

    AdjustStrategy --> Start

    style Start fill:#e1f5ff
    style Success fill:#c8e6c9
    style SendAI fill:#fff4e1
```

---

## 开发工作流

### PRD 驱动开发流程

```mermaid
flowchart TD
    Start([开始新功能]) --> WritePRD[编写 PRD]

    WritePRD --> PRDReview{PRD 审核}
    PRDReview -->|需要修改| WritePRD
    PRDReview -->|通过| GenPlan[生成实现计划]

    GenPlan --> AIPlan[AI 生成步骤]
    AIPlan --> ReviewPlan{审核计划}

    ReviewPlan -->|需要调整| ModifyPlan[修改计划]
    ModifyPlan --> AIPlan
    ReviewPlan -->|通过| StartImpl[开始实现]

    StartImpl --> Step1[实现步骤 1]
    Step1 --> Test1{测试}

    Test1 -->|失败| Fix1[修复问题]
    Fix1 --> Test1
    Test1 -->|通过| Commit1[Git 提交]

    Commit1 --> MoreSteps{还有步骤?}

    MoreSteps -->|是| NextStep[下一步骤]
    NextStep --> Test1

    MoreSteps -->|否| FinalTest[最终测试]

    FinalTest --> CodeReview[代码审查]
    CodeReview --> ReviewResult{审查结果}

    ReviewResult -->|需要改进| Improve[改进代码]
    Improve --> FinalTest

    ReviewResult -->|通过| CreatePR[创建 PR]
    CreatePR --> End([完成])

    style Start fill:#e1f5ff
    style End fill:#c8e6c9
    style AIPlan fill:#fff4e1
    style Commit1 fill:#c8e6c9
```

### 增量开发模式

```mermaid
gantt
    title Gemini CLI 增量开发时间线
    dateFormat  YYYY-MM-DD
    section 准备阶段
    编写 PRD           :a1, 2024-01-01, 1d
    生成计划           :a2, after a1, 1d

    section 实现阶段
    步骤 1: 数据库设计    :b1, after a2, 1d
    Git 提交 1        :milestone, after b1, 0d
    步骤 2: API 端点     :b2, after b1, 2d
    Git 提交 2        :milestone, after b2, 0d
    步骤 3: 前端组件     :b3, after b2, 2d
    Git 提交 3        :milestone, after b3, 0d
    步骤 4: 集成测试     :b4, after b3, 1d
    Git 提交 4        :milestone, after b4, 0d

    section 完成阶段
    代码审查           :c1, after b4, 1d
    修复问题           :c2, after c1, 1d
    创建 PR           :c3, after c2, 1d
```

### 提示词优化流程

```mermaid
flowchart TD
    Start([需要 AI 帮助]) --> Draft[起草初始提示词]

    Draft --> Check{检查清单}

    Check --> Q1{上下文明确?}
    Q1 -->|否| AddContext[添加上下文]
    Q1 -->|是| Q2{目标清晰?}
    AddContext --> Q2

    Q2 -->|否| ClarifyGoal[明确目标]
    Q2 -->|是| Q3{有示例?}
    ClarifyGoal --> Q3

    Q3 -->|否| AddExample[添加示例]
    Q3 -->|是| Q4{约束条件?}
    AddExample --> Q4

    Q4 -->|否| AddConstraint[添加约束]
    Q4 -->|是| Q5{分解任务?}
    AddConstraint --> Q5

    Q5 -->|需要| BreakDown[分解为小步骤]
    Q5 -->|不需要| Final[最终提示词]
    BreakDown --> Final

    Final --> SendAI[发送到 AI]
    SendAI --> Result{结果质量}

    Result -->|不满意| Analyze[分析问题]
    Result -->|满意| Success[完成]

    Analyze --> Improve[改进提示词]
    Improve --> SendAI

    style Start fill:#e1f5ff
    style Success fill:#c8e6c9
    style SendAI fill:#fff4e1
```

---

## 最佳实践决策树

### 选择合适的工作方式

```mermaid
flowchart TD
    Start([开始任务]) --> TaskType{任务类型?}

    TaskType -->|简单问答| Direct[直接提问]
    TaskType -->|代码生成| CodeFlow[代码生成流程]
    TaskType -->|复杂功能| FeatureFlow[功能开发流程]
    TaskType -->|问题排查| DebugFlow[调试流程]

    Direct --> AskQuestion[提出问题]
    AskQuestion --> GetAnswer[获得答案]
    GetAnswer --> End([完成])

    CodeFlow --> HasExample{有参考示例?}
    HasExample -->|是| ProvideExample[提供示例]
    HasExample -->|否| DescribeReq[详细描述需求]
    ProvideExample --> GenCode[生成代码]
    DescribeReq --> GenCode
    GenCode --> Review[审查代码]
    Review --> End

    FeatureFlow --> WritePRD[编写 PRD]
    WritePRD --> GenPlan[生成计划]
    GenPlan --> ReviewPlan{计划 OK?}
    ReviewPlan -->|否| ModifyPlan[修改计划]
    ModifyPlan --> GenPlan
    ReviewPlan -->|是| ImplementSteps[逐步实现]
    ImplementSteps --> TestEach[每步测试]
    TestEach --> CommitEach[每步提交]
    CommitEach --> End

    DebugFlow --> Describe[描述问题]
    Describe --> ProvideContext[提供上下文]
    ProvideContext --> ProvideError[提供错误信息]
    ProvideError --> Analyze[AI 分析]
    Analyze --> Suggest[建议解决方案]
    Suggest --> Try{尝试修复}
    Try -->|失败| MoreInfo[提供更多信息]
    MoreInfo --> Analyze
    Try -->|成功| End

    style Start fill:#e1f5ff
    style End fill:#c8e6c9
    style GenPlan fill:#fff4e1
```

---

## 性能优化流程

### 请求优化策略

```mermaid
flowchart TD
    Start([发起请求]) --> Analyze[分析请求]

    Analyze --> CheckCache{检查缓存}
    CheckCache -->|命中| ReturnCache[返回缓存]
    CheckCache -->|未命中| CheckCtx{检查上下文大小}

    CheckCtx -->|< 10K| Small[小上下文]
    CheckCtx -->|10K-100K| Medium[中等上下文]
    CheckCtx -->|> 100K| Large[大上下文]

    Small --> DirectSend[直接发送]

    Medium --> OptimizeCtx[优化上下文]
    OptimizeCtx --> RemoveDup[移除重复]
    RemoveDup --> DirectSend

    Large --> SplitTask{可分割?}
    SplitTask -->|是| MultiReq[多次请求]
    SplitTask -->|否| Truncate[截断上下文]

    MultiReq --> Batch[批处理]
    Truncate --> DirectSend
    Batch --> DirectSend

    DirectSend --> SendAPI[发送 API]
    SendAPI --> Receive[接收响应]

    Receive --> SaveCache[保存缓存]
    SaveCache --> ReturnResult[返回结果]
    ReturnCache --> ReturnResult

    ReturnResult --> End([完成])

    style Start fill:#e1f5ff
    style End fill:#c8e6c9
    style SaveCache fill:#fff4e1
```

---

## 总结

### 关键流程要点

| 流程 | 核心原则 | 最佳实践 |
|------|----------|----------|
| **初始化** | 自动加载配置 | 使用 `/init` 生成模板 |
| **上下文管理** | 分层覆盖 | 全局 → 项目 → 子目录 |
| **工具调用** | 自动调度 | 信任 AI 选择工具 |
| **MCP 集成** | 扩展功能 | 使用标准协议 |
| **开发工作流** | 增量提交 | 小步骤、频繁测试 |
| **性能优化** | 控制上下文 | 缓存、批处理、截断 |

### 快速参考

```mermaid
mindmap
  root((Gemini CLI<br/>最佳实践))
    配置
      GEMINI.md
      分层加载
      模块化导入
    工作流
      PRD 驱动
      增量开发
      Git 提交
    工具
      内置工具
      MCP 服务器
      自定义扩展
    优化
      上下文管理
      缓存策略
      批处理
    提示词
      明确目标
      提供示例
      添加约束
```

---

**文档版本**: v1.0.0
**最后更新**: 2025-01-29
**维护者**: gemini-guide 团队

💡 **使用提示**:
- 在支持 Mermaid 的编辑器中查看（VS Code + Markdown Preview Mermaid Support 插件）
- GitHub 自动渲染 Mermaid 图表
- 可使用 [Mermaid Live Editor](https://mermaid.live/) 在线预览和编辑
