#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="$repo_root/skills"
expected=(visual-anything visual-plan visual-gen visual-deck)

for skill in "${expected[@]}"; do
  skill_dir="$skills_dir/$skill"
  test -f "$skill_dir/SKILL.md"
  if rg -n '\.\./(contracts|docs|scripts)|/auto-visual-anything/(contracts|docs|scripts)' "$skill_dir/SKILL.md" "$skill_dir/README.md" >/tmp/visual-anything-validate-rg.out 2>/dev/null; then
    echo "Runtime dependency leak in $skill:" >&2
    cat /tmp/visual-anything-validate-rg.out >&2
    exit 1
  fi
done

test -x "$skills_dir/visual-deck/scripts/render_slides.py"

for required in deck_content_brief.md source_refs content_mode render_slides.py max_concurrency; do
  if ! rg -q "$required" "$skills_dir/visual-deck" "$repo_root/contracts/deck-outline.md"; then
    echo "visual-deck contract is missing required term: $required" >&2
    exit 1
  fi
done

if rg -n 'source\s*→\s*outline|visual-plan.*outline drafting' "$skills_dir/visual-deck" "$repo_root/contracts/deck-outline.md" >/tmp/visual-anything-deck-contract-rg.out 2>/dev/null; then
  echo "visual-deck still contains the old direct source-to-outline contract:" >&2
  cat /tmp/visual-anything-deck-contract-rg.out >&2
  exit 1
fi

if command -v python >/dev/null 2>&1; then
  python -m py_compile \
    "$skills_dir/visual-gen/scripts/visual_gen.py" \
    "$skills_dir/visual-deck/scripts/render_slides.py"
else
  echo "python not available; skipped py_compile and visual-gen tests" >&2
fi

if command -v python >/dev/null 2>&1 && python -c 'import pytest' >/dev/null 2>&1; then
  python -m pytest "$skills_dir/visual-gen/tests" -q
else
  echo "pytest not available; skipped visual-gen tests" >&2
fi

bash "$repo_root/scripts/list-skills.sh"
