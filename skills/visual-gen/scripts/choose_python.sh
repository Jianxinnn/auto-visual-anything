#!/usr/bin/env bash
# 探测可用的 Python 3.11+ 启动方式 (要求支持 tomllib)
# 输出第一个可用的命令到 stdout;失败时 exit 1
#
# 用法:
#   python_cmd=$(bash choose_python.sh) || { echo "未找到可用 Python 3.11+"; exit 1; }
#
# 注意: 输出可能含多个词 (如 "uv run --python 3.12 python"),
# 后续调用时不要给 $python_cmd 整体加引号。

for cmd in \
  "python3.12" \
  "python3.11" \
  "python3" \
  "python" \
  "py -3.12" \
  "py -3.11" \
  "py -3" \
  "uv run --python 3.12 python"; do
  if sh -c "$cmd - <<'PY'
import sys
import tomllib
raise SystemExit(0 if sys.version_info >= (3, 11) else 1)
PY" >/dev/null 2>&1; then
    printf '%s\n' "$cmd"
    exit 0
  fi
done
exit 1
