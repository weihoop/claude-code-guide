# 编程使用 Skills 指南

通过 Python 和 Node.js SDK 在代码中使用 Claude Skills，实现自动化工作流。

## 📚 目录

- [快速开始](#快速开始)
- [Python SDK](#python-sdk)
- [Node.js SDK](#nodejs-sdk)
- [高级用法](#高级用法)
- [批量处理](#批量处理)
- [错误处理](#错误处理)
- [性能优化](#性能优化)
- [实战案例](#实战案例)

---

## 🚀 快速开始

### 安装 SDK

**Python**:
```bash
pip install anthropic
```

**Node.js**:
```bash
npm install @anthropic-ai/sdk
```

### 基础示例

**Python**:
```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    skills=["pdf"],  # 加载 pdf skill
    messages=[
        {"role": "user", "content": "分析这个 PDF 文件"}
    ]
)

print(response.content[0].text)
```

**Node.js**:
```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

const response = await client.messages.create({
  model: "claude-sonnet-4-20250514",
  max_tokens: 1024,
  skills: ["pdf"],
  messages: [
    { role: "user", content: "分析这个 PDF 文件" }
  ],
});

console.log(response.content[0].text);
```

---

## 🐍 Python SDK

### 完整示例

```python
import anthropic
import os
from typing import List, Dict, Any

class SkillClient:
    """封装 Anthropic API 的 Skill 客户端"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def use_skill(
        self,
        skill_names: List[str],
        prompt: str,
        model: str = "claude-sonnet-4-20250514",
        max_tokens: int = 4096
    ) -> str:
        """使用指定的 Skills 处理提示词"""
        response = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            skills=skill_names,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text

    def analyze_document(
        self,
        file_path: str,
        skill: str = "pdf"
    ) -> Dict[str, Any]:
        """分析文档并返回结构化结果"""
        with open(file_path, "rb") as f:
            content = f.read()

        prompt = f"分析这个文档并提取关键信息：\n\n{file_path}"

        result = self.use_skill(
            skill_names=[skill],
            prompt=prompt
        )

        return {
            "file_path": file_path,
            "analysis": result,
            "skill_used": skill
        }

# 使用示例
if __name__ == "__main__":
    client = SkillClient()

    # 单个文档分析
    result = client.analyze_document("report.pdf", "pdf")
    print(result["analysis"])

    # 使用多个 Skills
    result = client.use_skill(
        skill_names=["pdf", "xlsx"],
        prompt="分析这些财务报表并生成摘要"
    )
    print(result)
```

### 异步版本

```python
import anthropic
import asyncio
from typing import List

class AsyncSkillClient:
    """异步 Skill 客户端"""

    def __init__(self, api_key: str = None):
        self.client = anthropic.AsyncAnthropic(
            api_key=api_key or os.getenv("ANTHROPIC_API_KEY")
        )

    async def use_skill(
        self,
        skill_names: List[str],
        prompt: str
    ) -> str:
        """异步使用 Skill"""
        response = await self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            skills=skill_names,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

    async def batch_analyze(
        self,
        prompts: List[str],
        skill: str
    ) -> List[str]:
        """批量异步分析"""
        tasks = [
            self.use_skill([skill], prompt)
            for prompt in prompts
        ]
        return await asyncio.gather(*tasks)

# 使用示例
async def main():
    client = AsyncSkillClient()

    prompts = [
        "分析 Q1 销售数据",
        "分析 Q2 销售数据",
        "分析 Q3 销售数据",
    ]

    results = await client.batch_analyze(prompts, "xlsx")
    for i, result in enumerate(results, 1):
        print(f"Q{i} 分析结果：\n{result}\n")

asyncio.run(main())
```

---

## 🟢 Node.js SDK

### 完整示例

```javascript
import Anthropic from "@anthropic-ai/sdk";
import fs from "fs/promises";

class SkillClient {
  constructor(apiKey = process.env.ANTHROPIC_API_KEY) {
    this.client = new Anthropic({ apiKey });
  }

  async useSkill(skillNames, prompt, options = {}) {
    const {
      model = "claude-sonnet-4-20250514",
      maxTokens = 4096,
    } = options;

    const response = await this.client.messages.create({
      model,
      max_tokens: maxTokens,
      skills: skillNames,
      messages: [{ role: "user", content: prompt }],
    });

    return response.content[0].text;
  }

  async analyzeDocument(filePath, skill = "pdf") {
    const content = await fs.readFile(filePath);
    const prompt = `分析这个文档并提取关键信息：\n\n${filePath}`;

    const analysis = await this.useSkill([skill], prompt);

    return {
      filePath,
      analysis,
      skillUsed: skill,
    };
  }

  async batchAnalyze(prompts, skill) {
    const promises = prompts.map((prompt) =>
      this.useSkill([skill], prompt)
    );
    return await Promise.all(promises);
  }
}

// 使用示例
const client = new SkillClient();

// 单个文档分析
const result = await client.analyzeDocument("report.pdf", "pdf");
console.log(result.analysis);

// 批量处理
const prompts = [
  "分析 Q1 销售数据",
  "分析 Q2 销售数据",
  "分析 Q3 销售数据",
];

const results = await client.batchAnalyze(prompts, "xlsx");
results.forEach((result, i) => {
  console.log(`Q${i + 1} 分析结果：\n${result}\n`);
});
```

### TypeScript 版本

```typescript
import Anthropic from "@anthropic-ai/sdk";
import type { Message } from "@anthropic-ai/sdk/resources";

interface SkillOptions {
  model?: string;
  maxTokens?: number;
}

interface AnalysisResult {
  filePath: string;
  analysis: string;
  skillUsed: string;
}

class SkillClient {
  private client: Anthropic;

  constructor(apiKey: string = process.env.ANTHROPIC_API_KEY!) {
    this.client = new Anthropic({ apiKey });
  }

  async useSkill(
    skillNames: string[],
    prompt: string,
    options: SkillOptions = {}
  ): Promise<string> {
    const {
      model = "claude-sonnet-4-20250514",
      maxTokens = 4096,
    } = options;

    const response: Message = await this.client.messages.create({
      model,
      max_tokens: maxTokens,
      skills: skillNames,
      messages: [{ role: "user", content: prompt }],
    });

    return response.content[0].text;
  }

  async analyzeDocument(
    filePath: string,
    skill: string = "pdf"
  ): Promise<AnalysisResult> {
    const prompt = `分析这个文档：${filePath}`;
    const analysis = await this.useSkill([skill], prompt);

    return {
      filePath,
      analysis,
      skillUsed: skill,
    };
  }
}

// 使用示例
const client = new SkillClient();
const result = await client.analyzeDocument("report.pdf");
console.log(result.analysis);
```

---

## 🚀 高级用法

### 1. 流式响应

**Python**:
```python
def stream_analysis(client, skill, prompt):
    """流式接收分析结果"""
    with client.messages.stream(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        skills=[skill],
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        print()  # 换行

# 使用
client = anthropic.Anthropic()
stream_analysis(client, "pdf", "分析这个 PDF 文件")
```

**Node.js**:
```javascript
async function streamAnalysis(client, skill, prompt) {
  const stream = await client.messages.stream({
    model: "claude-sonnet-4-20250514",
    max_tokens: 4096,
    skills: [skill],
    messages: [{ role: "user", content: prompt }],
  });

  for await (const chunk of stream) {
    if (chunk.type === "content_block_delta") {
      process.stdout.write(chunk.delta.text);
    }
  }
  console.log(); // 换行
}

// 使用
await streamAnalysis(client, "pdf", "分析这个 PDF 文件");
```

### 2. 上下文对话

```python
def conversation_with_skills(client, skills):
    """带 Skills 的多轮对话"""
    messages = []

    while True:
        user_input = input("你: ")
        if user_input.lower() in ["退出", "exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            skills=skills,
            messages=messages
        )

        assistant_message = response.content[0].text
        messages.append({"role": "assistant", "content": assistant_message})

        print(f"Claude: {assistant_message}\n")

# 使用
client = anthropic.Anthropic()
conversation_with_skills(client, ["pdf", "xlsx"])
```

### 3. 条件加载 Skills

```python
def smart_skill_selection(file_path: str) -> List[str]:
    """根据文件类型智能选择 Skill"""
    ext = file_path.lower().split(".")[-1]

    skill_map = {
        "pdf": ["pdf"],
        "docx": ["docx"],
        "doc": ["docx"],
        "xlsx": ["xlsx"],
        "xls": ["xlsx"],
        "pptx": ["pptx"],
        "csv": ["xlsx"],  # CSV 也可以用 xlsx skill
    }

    return skill_map.get(ext, [])

def analyze_file(client, file_path: str):
    """智能分析文件"""
    skills = smart_skill_selection(file_path)

    if not skills:
        print(f"不支持的文件类型：{file_path}")
        return

    prompt = f"分析这个文件：{file_path}"
    result = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        skills=skills,
        messages=[{"role": "user", "content": prompt}]
    )

    return result.content[0].text

# 使用
client = anthropic.Anthropic()
result = analyze_file(client, "report.pdf")
print(result)
```

---

## 📦 批量处理

### Python 批量处理器

```python
import concurrent.futures
from pathlib import Path
from typing import List, Dict

class BatchProcessor:
    """批量文档处理器"""

    def __init__(self, client: anthropic.Anthropic):
        self.client = client

    def process_directory(
        self,
        directory: str,
        pattern: str = "*.pdf",
        max_workers: int = 5
    ) -> List[Dict]:
        """批量处理目录中的文件"""
        files = list(Path(directory).glob(pattern))
        results = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.process_file, str(file)): file
                for file in files
            }

            for future in concurrent.futures.as_completed(futures):
                file = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                    print(f"✅ 完成：{file.name}")
                except Exception as e:
                    print(f"❌ 失败：{file.name} - {e}")

        return results

    def process_file(self, file_path: str) -> Dict:
        """处理单个文件"""
        skills = smart_skill_selection(file_path)

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            skills=skills,
            messages=[{
                "role": "user",
                "content": f"分析文件：{file_path}"
            }]
        )

        return {
            "file_path": file_path,
            "analysis": response.content[0].text,
            "skills_used": skills
        }

# 使用
client = anthropic.Anthropic()
processor = BatchProcessor(client)

results = processor.process_directory(
    directory="./documents",
    pattern="*.pdf",
    max_workers=3
)

# 保存结果
for result in results:
    output_file = f"{result['file_path']}_analysis.txt"
    with open(output_file, "w") as f:
        f.write(result["analysis"])
```

---

## ⚠️ 错误处理

### 完整的错误处理

```python
from anthropic import APIError, APIConnectionError, RateLimitError
import time

def robust_skill_call(
    client,
    skills: List[str],
    prompt: str,
    max_retries: int = 3
) -> str:
    """带重试机制的 Skill 调用"""
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                skills=skills,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text

        except RateLimitError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 指数退避
                print(f"速率限制，等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                raise

        except APIConnectionError as e:
            if attempt < max_retries - 1:
                print(f"连接错误，重试 {attempt + 1}/{max_retries}...")
                time.sleep(1)
            else:
                raise

        except APIError as e:
            print(f"API 错误：{e}")
            raise

        except Exception as e:
            print(f"未知错误：{e}")
            raise

# 使用
client = anthropic.Anthropic()
try:
    result = robust_skill_call(
        client,
        ["pdf"],
        "分析这个 PDF 文件"
    )
    print(result)
except Exception as e:
    print(f"最终失败：{e}")
```

---

## ⚡ 性能优化

### 1. 缓存策略

```python
from functools import lru_cache
import hashlib

@lru_cache(maxsize=128)
def cached_analysis(file_hash: str, skill: str) -> str:
    """缓存分析结果"""
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        skills=[skill],
        messages=[{"role": "user", "content": f"分析文件：{file_hash}"}]
    )
    return response.content[0].text

def get_file_hash(file_path: str) -> str:
    """计算文件哈希"""
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

# 使用
file_hash = get_file_hash("report.pdf")
result = cached_analysis(file_hash, "pdf")  # 首次调用
result = cached_analysis(file_hash, "pdf")  # 从缓存返回
```

### 2. 连接池

```python
from anthropic import Anthropic
import threading

class SkillClientPool:
    """Skill 客户端连接池"""

    def __init__(self, api_key: str, pool_size: int = 5):
        self.pool = [
            Anthropic(api_key=api_key)
            for _ in range(pool_size)
        ]
        self.lock = threading.Lock()
        self.current = 0

    def get_client(self) -> Anthropic:
        """获取客户端"""
        with self.lock:
            client = self.pool[self.current]
            self.current = (self.current + 1) % len(self.pool)
            return client

# 使用
pool = SkillClientPool(api_key="your-key", pool_size=3)
client = pool.get_client()
```

---

## 💼 实战案例

### 案例：批量报告生成系统

```python
import anthropic
import json
from pathlib import Path
from datetime import datetime

class ReportGenerator:
    """批量报告生成系统"""

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def generate_report(self, data_file: str) -> Dict:
        """生成单个报告"""
        # 1. 分析数据
        skills = smart_skill_selection(data_file)
        analysis = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            skills=skills,
            messages=[{
                "role": "user",
                "content": f"分析数据并生成报告：{data_file}"
            }]
        )

        # 2. 生成摘要
        summary = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"总结以下分析（100字内）：\n\n{analysis.content[0].text}"
            }]
        )

        return {
            "file": data_file,
            "analysis": analysis.content[0].text,
            "summary": summary.content[0].text,
            "generated_at": datetime.now().isoformat()
        }

    def batch_generate(self, input_dir: str, output_dir: str):
        """批量生成报告"""
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        for data_file in Path(input_dir).glob("*.xlsx"):
            print(f"处理：{data_file.name}...")

            report = self.generate_report(str(data_file))

            # 保存报告
            output_file = Path(output_dir) / f"{data_file.stem}_report.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(report, f, ensure_ascii=False, indent=2)

            print(f"✅ 完成：{output_file.name}")

# 使用
generator = ReportGenerator(api_key="your-key")
generator.batch_generate(
    input_dir="./data",
    output_dir="./reports"
)
```

---

## 📚 延伸阅读

- [创建自定义 Skills](creating-custom-skills.md)
- [Skills 最佳实践](best-practices.md)
- [故障排除指南](troubleshooting.md)
- [Skills vs MCP vs Commands](skills-vs-mcp-vs-commands.md)

---

**返回**: [指南目录](README.md) | [主页](../README.md)

**最后更新**: 2026-01-24
