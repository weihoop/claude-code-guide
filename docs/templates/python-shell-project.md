# Python/Shell 脚本库项目配置模板

适用于运维自动化、数据处理工具、系统管理脚本等项目。

---

## CLAUDE.md 模板

将以下内容保存为项目根目录的 `CLAUDE.md` 文件：

```markdown
# 项目名称

## 项目概述

**项目类型**: Python/Shell 脚本库
**主要用途**: 运维自动化、系统监控、数据处理
**技术栈**: Python 3.8+, Bash
**开发模式**: 运维导向，中文注释，完整可执行

## 项目结构

\```
project/
├── src/
│   ├── main.py              # 主入口
│   ├── utils/               # 工具函数
│   │   ├── __init__.py
│   │   ├── logger.py        # 日志工具
│   │   ├── config.py        # 配置管理
│   │   └── helpers.py       # 通用函数
│   ├── monitors/            # 监控模块
│   │   ├── api_monitor.py
│   │   └── system_monitor.py
│   └── scripts/             # Shell 脚本
│       ├── deploy.sh
│       ├── backup.sh
│       └── healthcheck.sh
├── tests/
│   ├── test_utils.py
│   └── test_monitors.py
├── config/
│   ├── config.yaml          # 主配置文件
│   └── config.example.yaml  # 配置示例
├── requirements.txt         # Python 依赖
├── requirements-dev.txt     # 开发依赖
├── README.md
└── .gitignore
\```

## 开发环境

### Python 环境
- **版本要求**: Python >= 3.8
- **虚拟环境**: `python -m venv venv`
- **激活虚拟环境**:
  - Linux/macOS: `source venv/bin/activate`
  - Windows: `venv\Scripts\activate`

### 依赖安装
\```bash
# 安装生产依赖
pip install -r requirements.txt

# 安装开发依赖
pip install -r requirements-dev.txt

# 常用依赖
pip install requests pyyaml python-dotenv pytest black mypy
\```

## 常用命令

### Python 脚本

\```bash
# 运行主程序
python src/main.py

# 运行 API 监控
python src/monitors/api_monitor.py --config config/config.yaml

# 测试模式运行（使用测试配置）
python src/monitors/api_monitor.py --test

# 查看帮助
python src/main.py --help
\```

### Shell 脚本

\```bash
# 部署脚本
bash src/scripts/deploy.sh

# 备份脚本
bash src/scripts/backup.sh

# 健康检查
bash src/scripts/healthcheck.sh
\```

### 测试

\```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行特定测试
python -m pytest tests/test_utils.py -v

# 测试覆盖率
python -m pytest --cov=src tests/
\```

### 代码质量

\```bash
# 代码格式化
black src/

# 类型检查
python -m mypy src/

# 语法检查
python -m py_compile src/**/*.py

# Lint 检查
pylint src/
\```

## 代码规范

### Python 代码风格
- **遵循 PEP 8 规范**
- **使用类型提示**（Type Hints）
- **中文注释**：所有函数、类、复杂逻辑使用中文注释
- **函数命名**：使用描述性的 snake_case
- **类命名**：使用 PascalCase
- **常量**：使用大写 SNAKE_CASE

### Shell 脚本风格
- **Shebang**: 使用 `#!/bin/bash`
- **错误处理**: 使用 `set -e` 和 `trap`
- **中文注释**: 关键步骤添加注释
- **函数化**: 复杂逻辑封装为函数

### 错误处理

**Python**:
\```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 错误处理
try:
    result = risky_operation()
    logger.info(f"操作成功: {result}")
except SpecificError as e:
    logger.error(f"操作失败: {e}")
    raise
except Exception as e:
    logger.exception(f"未预期的错误: {e}")
    sys.exit(1)
\```

**Shell**:
\```bash
#!/bin/bash
set -e  # 遇到错误立即退出
set -u  # 使用未定义变量时报错
set -o pipefail  # 管道命令任何一个失败都会导致整个管道失败

# 错误处理函数
error_exit() {
    echo "[错误] $1" >&2
    exit 1
}

# 使用示例
command || error_exit "命令执行失败"
\```

## 配置管理

### 配置文件格式

**config.yaml**:
\```yaml
# 全局配置
global:
  log_level: INFO
  log_file: logs/app.log

# API 监控配置
api_monitor:
  endpoints:
    - name: 用户服务
      url: https://api.example.com/users
      method: GET
      timeout: 10

  notification:
    webhook: https://hooks.example.com/webhook

# 数据库配置
database:
  host: localhost
  port: 5432
  name: mydb
  # 敏感信息使用环境变量
  username: ${DB_USER}
  password: ${DB_PASSWORD}
\```

### 环境变量

**创建 `.env.example`**:
\```
# 数据库配置
DB_USER=your_username
DB_PASSWORD=your_password

# API 密钥
API_KEY=your_api_key

# 通知配置
WEBHOOK_URL=https://hooks.example.com/webhook
\```

**加载环境变量**:
\```python
from dotenv import load_dotenv
import os

load_dotenv()  # 加载 .env 文件

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
\```

## 日志管理

### 日志配置

\```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    """配置日志器"""
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    # 同时输出到控制台
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger
\```

### 日志级别使用

\```python
logger.debug("详细的调试信息")
logger.info("常规信息记录")
logger.warning("警告信息")
logger.error("错误信息")
logger.exception("异常信息（包含堆栈）")
\```

## 测试规范

### 单元测试

\```python
import pytest
from src.utils.helpers import parse_config

def test_parse_config_success():
    """测试配置解析成功场景"""
    config = parse_config('config/config.example.yaml')
    assert config is not None
    assert 'global' in config

def test_parse_config_file_not_found():
    """测试配置文件不存在"""
    with pytest.raises(FileNotFoundError):
        parse_config('nonexistent.yaml')

def test_parse_config_invalid_yaml():
    """测试无效的 YAML 格式"""
    with pytest.raises(yaml.YAMLError):
        parse_config('invalid.yaml')
\```

### 测试命名规范

- 测试文件: `test_*.py`
- 测试函数: `test_功能描述_场景()`
- 使用中文 docstring 说明测试目的

## 脚本执行规范

### Python 脚本

**不设置可执行权限**，使用 `python3` 运行：

\```bash
# 正确的方式
python3 src/main.py --help
python3 src/monitors/api_monitor.py --test

# 错误的方式（不要使用）
chmod +x src/main.py  # 不需要
./src/main.py         # 不使用
\```

### Shell 脚本

**不设置可执行权限**，使用 `bash` 运行：

\```bash
# 正确的方式
bash src/scripts/deploy.sh
bash src/scripts/healthcheck.sh

# 错误的方式（不要使用）
chmod +x src/scripts/*.sh  # 不需要
./src/scripts/deploy.sh    # 不使用
\```

**优势**：
- 避免权限管理复杂性
- 跨平台兼容性更好
- 明确指定解释器

## 告警和通知系统

### 双环境配置

支持生产和测试两套通知渠道：

\```yaml
# config.yaml
notification:
  # 生产环境（正常运行）
  webhook: https://hooks.example.com/prod

  # 测试环境（开发调试）
  webhook_test: https://hooks.example.com/test
\```

### 测试模式

\```bash
# 生产模式 - 告警发送到生产渠道
python src/monitors/api_monitor.py

# 测试模式 - 告警发送到测试渠道
python src/monitors/api_monitor.py --test
python src/monitors/api_monitor.py -t
\```

### 实现示例

\```python
import argparse

def send_notification(message, is_test=False):
    """发送通知"""
    config = load_config()

    # 根据测试模式选择 webhook
    if is_test:
        webhook = config.get('notification', {}).get('webhook_test')
        logger.info(f"[测试模式] 使用测试 webhook: {webhook}")
    else:
        webhook = config.get('notification', {}).get('webhook')
        logger.info(f"[生产模式] 使用生产 webhook: {webhook}")

    # 发送通知
    send_to_webhook(webhook, message)

# 命令行参数解析
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', action='store_true', help='测试模式')
args = parser.parse_args()

send_notification("监控告警", is_test=args.test)
\```

## 部署和运维

### 定时任务（Crontab）

\```bash
# 编辑 crontab
crontab -e

# 每小时运行一次监控
0 * * * * cd /path/to/project && source venv/bin/activate && python src/monitors/api_monitor.py >> logs/cron.log 2>&1

# 每天凌晨2点备份
0 2 * * * bash /path/to/project/src/scripts/backup.sh >> logs/backup.log 2>&1
\```

### 系统服务（Systemd）

**创建服务文件** `/etc/systemd/system/myservice.service`:

\```ini
[Unit]
Description=My Monitoring Service
After=network.target

[Service]
Type=simple
User=myuser
WorkingDirectory=/path/to/project
ExecStart=/path/to/project/venv/bin/python src/monitors/api_monitor.py --daemon
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
\```

**启动服务**:
\```bash
sudo systemctl daemon-reload
sudo systemctl enable myservice
sudo systemctl start myservice
sudo systemctl status myservice
\```

## 安全最佳实践

### 敏感信息保护

- ✅ 使用环境变量存储密钥和密码
- ✅ `.env` 文件添加到 `.gitignore`
- ✅ 提供 `.env.example` 作为模板
- ❌ 不在代码中硬编码敏感信息

### 文件权限

\```bash
# 配置文件权限
chmod 600 .env
chmod 600 config/config.yaml

# 日志目录权限
chmod 755 logs/
chmod 644 logs/*.log
\```

### 代码审查清单

- [ ] 没有硬编码的密钥或密码
- [ ] 所有外部输入都经过验证
- [ ] 错误处理完善
- [ ] 日志不包含敏感信息
- [ ] 测试覆盖关键功能

## Git 提交规范

### 提交信息格式

\```bash
<类型>: <简短描述>

[可选的详细说明]
\```

### 提交类型

| 类型 | 说明 | 示例 |
|------|------|------|
| feat | 新功能 | `feat: 添加 API 健康检查监控` |
| fix | 修复bug | `fix: 修复配置文件解析错误` |
| docs | 文档更新 | `docs: 更新部署文档` |
| refactor | 重构 | `refactor: 优化日志处理逻辑` |
| test | 测试 | `test: 添加配置解析单元测试` |
| chore | 其他 | `chore: 更新依赖版本` |

## 常见问题

### Q1: 虚拟环境创建失败

\```bash
# 确保 python3-venv 已安装（Ubuntu/Debian）
sudo apt-get install python3-venv

# 创建虚拟环境
python3 -m venv venv
\```

### Q2: 依赖安装失败

\```bash
# 升级 pip
pip install --upgrade pip

# 使用国内镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
\```

### Q3: Shell 脚本权限错误

\```bash
# 不要使用 chmod +x，使用 bash 运行
bash src/scripts/deploy.sh
\```

### Q4: 日志文件过大

- 使用 `RotatingFileHandler` 自动轮转
- 设置合理的日志级别（生产环境用 INFO）
- 定期清理旧日志

## 相关资源

- [Python 官方文档](https://docs.python.org/)
- [Bash 脚本编程指南](https://www.gnu.org/software/bash/manual/)
- [pytest 文档](https://docs.pytest.org/)
- [YAML 语法](https://yaml.org/)
```

---

## 配套的 settings.json

将以下内容保存为 `.claude/settings.json`：

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Glob",
      "Grep",
      "Bash(python:*)",
      "Bash(python3:*)",
      "Bash(pip:*)",
      "Bash(pytest:*)",
      "Bash(bash:*)",
      "Bash(git:*)",
      "Bash(black:*)",
      "Bash(mypy:*)"
    ],
    "deny": [
      "Read(.env)",
      "Read(.env.*)",
      "Read(**/secrets/**)",
      "Read(**/config/production.yaml)",
      "Write(.env)",
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ],
    "ask": [
      "Bash(pip install:*)",
      "Bash(git push:*)",
      "Bash(systemctl:*)"
    ]
  }
}
```

---

## 快速开始

### 1. 复制模板到项目

```bash
# 进入你的 Python 项目
cd /path/to/your/project

# 复制 CLAUDE.md
cp /path/to/claude-code-guide/docs/templates/python-shell-project.md ./CLAUDE.md

# 创建配置目录
mkdir -p .claude

# 复制 settings.json
# （根据上面的配置创建 .claude/settings.json）
```

### 2. 根据项目调整

编辑 `CLAUDE.md`，调整以下内容：
- 项目名称和概述
- 项目结构（匹配实际目录）
- 具体的命令和脚本
- 配置文件路径

### 3. 测试配置

```bash
# 启动 Claude Code
claude

# 询问 Claude
> 介绍一下这个项目的结构
> 如何运行测试？
> 帮我添加一个新的监控脚本
```

---

## 更多模板

- [Next.js 项目模板](./nextjs-project.md)
- [文档项目模板](./documentation-project.md)
