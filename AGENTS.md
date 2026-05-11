# FigForge Agent Instructions

FigForge is a monorepo for related agent skills. The runtime install unit is
always one directory under `skills/<skill-name>/` containing its own `SKILL.md`.

Rules:

- Keep every `skills/<skill-name>/` directory self-contained for installation.
- Do not make a skill depend on files from repo-root `docs/`, `contracts/`, or
  `scripts/` at runtime.
- Keep API credentials and API probing logic inside `skills/figforge-gen`.
- Orchestrators (`figforge`, `figforge-deck`) may invoke other skills through
  their public skill interfaces, but must not copy generation or credential
  logic.
- Runtime output directories such as `.figforge/`, `.figforge-deck/`, generated
  images, caches, and `__pycache__` do not belong in commits.
- Use `scripts/validate.sh` before commits that change skill contents.
