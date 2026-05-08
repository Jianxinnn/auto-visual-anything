# FigForge

> A three-skill toolchain for turning source material into publication-quality figures.
> Each skill owns one concern; the orchestrator stitches them.

[![figforge](https://img.shields.io/badge/figforge-orchestrator-1f2937?style=flat-square)](https://github.com/Jianxinnn/figforge)
[![figforge-plan](https://img.shields.io/badge/figforge--plan-planning-1f6feb?style=flat-square)](https://github.com/Jianxinnn/figforge-plan)
[![figforge-gen](https://img.shields.io/badge/figforge--gen-generation-9333ea?style=flat-square)](https://github.com/Jianxinnn/figforge-gen)

`figforge` is the orchestrator skill in the family. It does not analyze source material itself, and it does not call image APIs itself. It routes between the two workers, persists run state, and decides where each revision belongs.

---

## The Family

| Skill | Responsibility | Repository |
|---|---|---|
| `figforge` | Triage incoming requests, route to plan / gen, persist run state, classify revisions | [github.com/Jianxinnn/figforge](https://github.com/Jianxinnn/figforge) |
| `figforge-plan` | Read source material (paper / repo / code / diagram) and produce a source-grounded Prompt Package with an evidence ledger | [github.com/Jianxinnn/figforge-plan](https://github.com/Jianxinnn/figforge-plan) |
| `figforge-gen` | Own image-API credentials, preflight, timeouts, and `gpt-image-2` calls; write images to disk | [github.com/Jianxinnn/figforge-gen](https://github.com/Jianxinnn/figforge-gen) |

The three skills are independently useful. Use `figforge` only when you want both planning and generation in a single coherent loop.

---

## Which one to call

| Request shape | Skill |
|---|---|
| "Make a main figure from this paper / repo, end to end" | `figforge` |
| "Read this source and produce a figure prompt — don't generate yet" | `figforge-plan` |
| "I already have a finalized prompt; render the image" | `figforge-gen` |
| "Generate a transparent-background cat" (no source material) | `figforge-gen` |

If you are unsure, start with `figforge` — its triage step will route to the right worker.

---

## Pipeline

![FigForge call flow](assets/figforge-call-flow.png)

```
input ──► [figforge] triage
              │
              ├── source material  ──► figforge-plan ──► Prompt Package
              │                                              │
              │                                              ▼
              └── prompt only      ──────────────────►  figforge-gen ──► image
                                                              │
                                                              ▼
                                                         revision loop
```

1. **Triage** — `figforge` decides whether planning is needed.
2. **Plan** — `figforge-plan` separates evidence from assumption from unknown, then compiles a Prompt Package.
3. **Generate** — `figforge-gen` runs preflight, calls the image backend, and writes the image plus run metadata.
4. **Iterate** — cosmetic and pixel edits go back to `figforge-gen`; structural edits go back to `figforge-plan`. The orchestrator picks the lane and never silently regenerates from scratch.

Each run is recorded under:

```
.figforge/<YYYYMMDD-HHMMSS>/
├── prompt_package.md     # figforge-plan output, verbatim
├── last_image.json       # { path, params, ts, prompt_package }
└── revisions.log         # one line per revision attempt
```

---

## Why three skills instead of one

- **Credential isolation.** API tokens live only inside `figforge-gen`. The orchestrator never reads, copies, or forwards them.
- **Truthfulness contract.** `figforge-plan` is the only layer permitted to judge whether evidence is sufficient. `figforge` will not bypass it to feed a thin prompt into generation.
- **No reimplementation.** The orchestrator invokes sub-skills through their public entry points; it does not call their internal scripts. A change inside `figforge-gen` (timeout policy, model selection, output format) does not require touching `figforge`.

---

## Repository layout

```text
figforge/
├── SKILL.md                    # orchestration rules (triage / plan / generate / iterate)
├── README.md
└── assets/
    ├── figforge-call-flow.png
    └── figforge-call-flow.svg
```

This repository contains only the orchestrator. Worker code lives in:

- **Planning** — <https://github.com/Jianxinnn/figforge-plan>
- **Generation** — <https://github.com/Jianxinnn/figforge-gen>

---

## See also

- `SKILL.md` in this repo — full orchestration logic, including triage signals, revision classification, and state file shapes.
- `figforge-plan/SKILL.md` — Prompt Package structure and the evidence ledger.
- `figforge-gen/SKILL.md` — credential resolution order, preflight checks, and CLI arguments.
