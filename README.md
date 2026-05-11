# FigForge

FigForge is a suite of installable agent skills for source-grounded figure
planning, image generation, and slide-image generation.

## Skills

| Skill | Role | Install unit |
| --- | --- | --- |
| `figforge` | Single-figure orchestrator: plan, generate, and iterate | `skills/figforge/` |
| `figforge-plan` | Source-to-figure planning and prompt package generation | `skills/figforge-plan/` |
| `figforge-gen` | Image generation/editing through `gpt-image-2` compatible APIs | `skills/figforge-gen/` |
| `figforge-deck` | Multi-slide PNG deck orchestrator | `skills/figforge-deck/` |

Each directory under `skills/` is intentionally self-contained. It can be copied
or symlinked into an agent skills directory independently.

## Local Development

The recommended local setup is to keep this repository as the source of truth
and expose the individual skills through symlinks:

```bash
bash scripts/link-local.sh
```

This maps:

```text
~/.agents/skills/figforge      -> skills/figforge
~/.agents/skills/figforge-plan -> skills/figforge-plan
~/.agents/skills/figforge-gen  -> skills/figforge-gen
~/.agents/skills/figforge-deck -> skills/figforge-deck
```

## Validation

Run:

```bash
bash scripts/validate.sh
```

The validator checks that each skill has a `SKILL.md`, that root-level runtime
dependencies are not referenced from skill instructions, and that the
`figforge-gen` unit tests pass when `pytest` is available.
