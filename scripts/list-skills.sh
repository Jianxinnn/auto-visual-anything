#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

find "$repo_root/skills" -mindepth 2 -maxdepth 2 -name SKILL.md -print \
  | sed "s#^$repo_root/skills/##; s#/SKILL.md\$##" \
  | sort
