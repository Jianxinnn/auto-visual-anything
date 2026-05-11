---
name: visual-anything
description: Use when the user wants one source-grounded figure generated end to end from a paper, repo, algorithm, diagram, or design idea. Use for requests such as "make and generate a main figure", "把这个 repo 画成 figure", "出一张架构图直接生成", or `/visual-anything`. Do not use for prompt-only work or for rendering an already-final prompt.
argument-hint: <自然语言需求 + 可选源材料>
allowed-tools: [Bash, Read, Write, Edit]
---

# visual-anything

Single-figure orchestrator: triage → `visual-plan` → `visual-gen` → iteration.
It must not analyze evidence or call image APIs directly.

## Triage

| User intent | Route |
|---|---|
| Raw image prompt only | Call `visual-gen`; skip planning |
| Source material + generated image | Full pipeline |
| Source material + "prompt only" | Call `visual-plan`; stop before generation |

Source material includes local paths, PDFs/images/SVGs, repo URLs, arXiv/GitHub links,
code blocks longer than 5 lines, or structured algorithm prose. If route affects cost or
truthfulness and remains unclear, ask one question.

## Run State

Use `<task_cwd>/.visual-anything/runs/figure/<YYYYMMDD-HHMMSS>/`:

```text
prompt_package.md
last_image.json
revisions.log
```

A new top-level figure request creates a new run; revisions stay in the latest run unless
the user asks to start over.

## Plan

Delegate source analysis to `visual-plan` and save its prompt package verbatim as
`prompt_package.md`.

Stop before generation when `visual-plan` reports insufficient evidence, unresolved
conflicts, or more than three critical `unknown` markers in claim/mechanism/metric fields.
The truthfulness contract belongs to `visual-plan`; do not bypass it for a prettier image.

## Generate

Pass the package to `visual-gen` through the skill interface, not by calling internal API
logic. Field mapping:

| Prompt package field | `visual-gen` field |
|---|---|
| Core Image Prompt | `--prompt` |
| Size | `--size` |
| Output format | `--output-format` |
| Quality | `--quality` |
| Background | `--background` |

Default `--out-dir` is the current figure run directory.

`visual-gen` alone owns Python detection, API preflight, timeout rules, credential
resolution, and image calls. If its preflight fails, surface the error and stop. Never
read, copy, print, or substitute API tokens.

After success, write `last_image.json`:

```json
{
  "path": "<image path>",
  "params": {"size": "...", "quality": "...", "output_format": "...", "background": "..."},
  "ts": "<ISO timestamp>",
  "prompt_package": "prompt_package.md"
}
```

## Iterate

| Revision | Route |
|---|---|
| Cosmetic: contrast, brightness, size, quality | Reuse package; call `visual-gen` |
| Pixel edit: local change to prior image | Call `visual-gen --mode edit` |
| Text/style within existing content | Edit package, then call `visual-gen` |
| Structural/evidence change | Return to `visual-plan` first |

Append each attempt to `revisions.log`. If the revision class is ambiguous, ask one
targeted question instead of guessing.

## User Output

After generation:

```text
图片已生成: <image path>
基于规划包: <run-dir>/prompt_package.md
关键参数: size=..., output_format=..., quality=...
```

For prompt-only requests, return the prompt package path/content and no image lines.
