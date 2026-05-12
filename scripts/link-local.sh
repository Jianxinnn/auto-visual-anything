#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_root="${1:-/public/home/jxtang/.agents/skills}"
backup_root="$target_root/.migration-backups/$(date +%Y%m%d-%H%M%S)"
skills=(visual-anything visual-plan visual-gen visual-deck)

mkdir -p "$target_root"

link_entry() {
  local name="$1"
  local skill="$2"
  local src="$repo_root/skills/$skill"
  local dst="$target_root/$name"

  test -f "$src/SKILL.md"

  if [ -L "$dst" ]; then
    current="$(readlink "$dst")"
    if [ "$current" = "$src" ]; then
      return
    fi
    mkdir -p "$backup_root"
    mv "$dst" "$backup_root/$name.symlink"
  elif [ -e "$dst" ]; then
    mkdir -p "$backup_root"
    mv "$dst" "$backup_root/$name"
  fi

  ln -s "$src" "$dst"
}

for skill in "${skills[@]}"; do
  link_entry "$skill" "$skill"
done

echo "Linked Auto Visual Anything skills into $target_root"
if [ -d "$backup_root" ]; then
  echo "Previous entries moved to $backup_root"
fi
