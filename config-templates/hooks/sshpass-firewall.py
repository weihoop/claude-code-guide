#!/usr/bin/env python3
"""sshpass 防火 hook：拦截通过 sshpass 远程执行的破坏性命令。

Claude Code PreToolUse hook。从 stdin 读取工具调用 JSON，
若是 Bash 工具且命令含 sshpass + 危险操作，则阻断（exit 2）。

不依赖权限引擎的字符串前缀匹配——直接对命令全文做正则检查，
能命中藏在远程引号字符串里的危险命令（如 sshpass ... ssh host "rm -rf /"）。
"""
import json
import re
import sys

# 危险操作模式（针对远程执行的破坏性命令）
DANGER_PATTERNS = [
    r"rm\s+-[rf]{1,2}\b",        # rm -rf / rm -fr / rm -r / rm -f
    r"\bmkfs\b",                  # 格式化文件系统
    r"\bdd\s+(if|of)=",          # dd 磁盘读写
    r"\bshutdown\b",              # 关机
    r"\breboot\b",                # 重启
    r"\bpoweroff\b",              # 断电
    r"\bhalt\b",                  # 停机
    r">\s*/dev/sd[a-z]",         # 直接写裸磁盘设备
    r":\(\)\s*\{.*\}\s*;",       # fork 炸弹
]


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        # 解析失败不阻断，放行（避免误伤）
        sys.exit(0)

    tool = data.get("tool_name", "")
    if tool != "Bash":
        sys.exit(0)

    cmd = data.get("tool_input", {}).get("command", "")
    if "sshpass" not in cmd:
        sys.exit(0)

    for pat in DANGER_PATTERNS:
        if re.search(pat, cmd, re.IGNORECASE):
            print(
                f"[sshpass 防火] 已拦截：检测到通过 sshpass 远程执行的破坏性命令"
                f"（匹配模式 /{pat}/）。如确需执行，请手动在终端运行。",
                file=sys.stderr,
            )
            sys.exit(2)  # exit 2 = 阻断并把 stderr 反馈给 Claude

    sys.exit(0)


if __name__ == "__main__":
    main()
