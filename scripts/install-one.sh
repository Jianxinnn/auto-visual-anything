#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "Usage: $0 <skill-name> [target-skills-dir]" >&2
  exit 2
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill="$1"
target_root="${2:-/public/home/jxtang/.agents/skills}"
src="$repo_root/skills/$skill"
dst="$target_root/$skill"

test -f "$src/SKILL.md"
mkdir -p "$dst"

if command -v rsync >/dev/null 2>&1; then
  rsync -a --exclude .git --exclude __pycache__ --exclude .pytest_cache "$src"/ "$dst"/
else
  cp -R "$src"/. "$dst"/
fi

echo "Installed $skill to $dst"
