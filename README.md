# Auto Visual Anything

Auto Visual Anything is a suite of installable agent skills for source-grounded figure
planning, image generation, and slide-image generation.

## Skills

| Skill | Role | Install unit |
| --- | --- | --- |
| `visual-anything` | Single-figure orchestrator: plan, generate, and iterate | `skills/visual-anything/` |
| `visual-plan` | Source-to-figure planning and prompt package generation | `skills/visual-plan/` |
| `visual-gen` | Image generation/editing through `gpt-image-2` compatible APIs | `skills/visual-gen/` |
| `visual-deck` | Multi-slide PNG deck orchestrator | `skills/visual-deck/` |

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
~/.agents/skills/visual-anything      -> skills/visual-anything
~/.agents/skills/visual-plan          -> skills/visual-plan
~/.agents/skills/visual-gen           -> skills/visual-gen
~/.agents/skills/visual-deck          -> skills/visual-deck
```

Legacy aliases (`figforge`, `figforge-plan`, `figforge-gen`, `figforge-deck`)
may also point to these same directories during migration.

## Validation

Run:

```bash
bash scripts/validate.sh
```

The validator checks that each skill has a `SKILL.md`, that root-level runtime
dependencies are not referenced from skill instructions, and that the
`visual-gen` unit tests pass when `pytest` is available.
