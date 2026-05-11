#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_root="${1:-/public/home/jxtang/.agents/skills}"
backup_root="$target_root/.migration-backups/$(date +%Y%m%d-%H%M%S)"
skills=(figforge figforge-plan figforge-gen figforge-deck)

mkdir -p "$target_root"

for skill in "${skills[@]}"; do
  src="$repo_root/skills/$skill"
  dst="$target_root/$skill"
  test -f "$src/SKILL.md"

  if [ -L "$dst" ]; then
    current="$(readlink "$dst")"
    if [ "$current" = "$src" ]; then
      continue
    fi
    mkdir -p "$backup_root"
    mv "$dst" "$backup_root/$skill.symlink"
  elif [ -e "$dst" ]; then
    mkdir -p "$backup_root"
    mv "$dst" "$backup_root/$skill"
  fi

  ln -s "$src" "$dst"
done

echo "Linked FigForge skills into $target_root"
if [ -d "$backup_root" ]; then
  echo "Previous entries moved to $backup_root"
fi
