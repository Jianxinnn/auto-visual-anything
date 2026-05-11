# FigForge Suite Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Consolidate the FigForge skill family into one suite repository while keeping each skill independently installable.

**Architecture:** The suite repository owns documentation, contracts, validation scripts, and four self-contained skill install units under `skills/`. Local agent discovery continues through symlinks from `~/.agents/skills` to each install unit.

**Tech Stack:** Git, shell scripts, Markdown, Python/pytest for `figforge-gen` tests.

---

### Task 1: Create Suite Skeleton

**Files:**
- Create: `README.md`
- Create: `AGENTS.md`
- Create: `.gitignore`
- Create: `docs/architecture.md`
- Create: `docs/migration.md`

- [ ] Initialize `/public/home/jxtang/project/cs/skills-lib/FigForge` as a git repo on `main`.
- [ ] Add suite-level docs that distinguish repo management files from runtime skill files.
- [ ] Commit the initial skeleton.

### Task 2: Import Skills

**Files:**
- Create: `skills/figforge/`
- Create: `skills/figforge-plan/`
- Create: `skills/figforge-gen/`
- Create: `skills/figforge-deck/`

- [ ] Import `figforge`, `figforge-plan`, and `figforge-gen` with subtree history when possible.
- [ ] Copy `figforge-deck` as a new suite-owned skill.
- [ ] Commit the deck import.

### Task 3: Add Maintenance Scripts

**Files:**
- Create: `scripts/list-skills.sh`
- Create: `scripts/validate.sh`
- Create: `scripts/link-local.sh`
- Create: `scripts/install-one.sh`

- [ ] Add scripts for listing installable skills, validating install units, linking local runtime entries, and copying one skill to a target skill directory.
- [ ] Run validation.

### Task 4: Switch Runtime Entries

**Files:**
- Modify filesystem entries under `/public/home/jxtang/.agents/skills/`

- [ ] Move existing standalone FigForge directories to `.migration-backups/`.
- [ ] Create symlinks from `/public/home/jxtang/.agents/skills/<skill>` to `FigForge/skills/<skill>`.
- [ ] Verify all symlinks resolve and all four `SKILL.md` files are visible.
