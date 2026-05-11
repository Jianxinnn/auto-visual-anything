#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="$repo_root/skills"
expected=(figforge figforge-plan figforge-gen figforge-deck)

for skill in "${expected[@]}"; do
  skill_dir="$skills_dir/$skill"
  test -f "$skill_dir/SKILL.md"
  if rg -n '\.\./\.\.|/contracts/|/docs/|/scripts/' "$skill_dir/SKILL.md" "$skill_dir/README.md" >/tmp/figforge-validate-rg.out 2>/dev/null; then
    echo "Runtime dependency leak in $skill:" >&2
    cat /tmp/figforge-validate-rg.out >&2
    exit 1
  fi
done

if command -v python >/dev/null 2>&1 && python -c 'import pytest' >/dev/null 2>&1; then
  python -m pytest "$skills_dir/figforge-gen/tests" -q
else
  echo "pytest not available; skipped figforge-gen tests" >&2
fi

bash "$repo_root/scripts/list-skills.sh"
