---
name: visual-anything
description: >
  visual-anything: use when the user wants the full source-to-image pipeline — analyze a
  paper / repo / algorithm / diagram / design idea, plan a publication-quality
  figure, AND actually generate the image. Triggers: "做一张论文主图",
  "把这个 repo 画成 figure", "出一张架构图直接生成", "scientific figure pipeline",
  "make and generate a figure", or `/visual-anything`. Routes between visual-plan
  (truthful prompt construction) and visual-gen (gpt-image-2 call), and manages
  the iteration loop. Do NOT trigger if the user only wants the prompt (use
  visual-plan directly) or already has a finished prompt and just needs pixels
  (use visual-gen directly).
argument-hint: <自然语言需求 + 可选源材料>
allowed-tools: [Bash, Read, Write, Edit]
---

# visual-anything — Source → Plan → Image (orchestrator)

The Auto Visual Anything suite has four skills. This one is the single-figure
conductor; it does **not** duplicate sub-skill work. Use it when you want all
three of:

1. Truthful planning (delegated to **visual-plan**)
2. Actual image generation (delegated to **visual-gen**)
3. Coherent iteration across both layers

If the user only needs a prompt, call `visual-plan` directly. If they already
have a final prompt and only want pixels, call `visual-gen` directly. Skip
this skill in those cases.

---

## Pipeline

```
INPUT
  │
  ▼
[STEP 1] Triage ──► raw prompt only?  →  skip STEP 2, jump to STEP 3
  │                 source material?   →  continue
  ▼
[STEP 2] Plan      (delegate to visual-plan)  →  visual-anything Prompt Package
  │                                                + evidence ledger
  ▼
[STEP 3] Generate  (delegate to visual-gen)   →  image file on disk
  │
  ▼
[STEP 4] Iterate   (route revisions back to STEP 2 or STEP 3)
```

---

## STEP 1 — Triage

Decide whether the planning layer is needed.

| Signal | Route |
|--------|-------|
| Raw prompt, no source material (e.g. `画一只透明背景的猫`) | Skip STEP 2; jump to STEP 3 with the prompt as-is |
| Source material present (repo path, paper PDF, code snippet, algorithm description, diagram image) | Full pipeline: STEP 2 → STEP 3 |
| Source material **and** the user explicitly says "just the prompt, don't generate" | STEP 2 only; do not call visual-gen |

Source-material detectors:

- Local file path with extension `.py`, `.md`, `.pdf`, `.png`, `.svg`, or a directory
- URL pointing to a paper / repo / arXiv ID / GitHub URL
- Pasted code blocks longer than 5 lines
- Long structured text describing an algorithm with named stages or `numbered steps`

If still ambiguous after one pass, ask exactly one disambiguation question.

---

## STEP 2 — Plan (delegate to visual-plan)

Hand the source material to the **visual-plan** skill. It produces a **visual-anything
Prompt Package** (with evidence ledger). Save the package to:

```
<task_cwd>/.visual-anything/runs/figure/<run-id>/prompt_package.md
```

Stop and ask the user before STEP 3 if the package contains:

- More than 3 `unknown` markers in critical positions (claim, mechanism, primary metric)
- An explicit "evidence insufficient" note from visual-plan
- Conflicts that visual-plan flagged but did not resolve

Generating an image from a thin evidence base produces hallucinated detail. The
Truthfulness Contract lives in visual-plan and must not be bypassed here.

---

## STEP 3 — Generate (delegate to visual-gen)

Map the Prompt Package fields to visual-gen arguments:

| Prompt Package field | visual-gen argument |
|----------------------|-----------------------|
| `Core Image Prompt` (compiled body) | `--prompt` |
| `Recommended Generation Settings → Size` | `--size` |
| `Recommended Generation Settings → Output format` | `--output-format` |
| `Recommended Generation Settings → Quality` | `--quality` |
| `Recommended Generation Settings → Background` | `--background` |

Out-dir defaults to `<task_cwd>/.visual-anything/runs/figure/<run-id>/`.

Hand off **through the visual-gen skill**, not by calling
`visual-gen/scripts/visual_gen.py` directly. visual-gen owns:

- API preflight (`--show-config`)
- Python detection (`scripts/choose_python.sh`)
- Timeout calculation per `references/fields.md`
- Credential resolution per `references/api-config.md`

Reimplementing any of those here breaks the credential boundary.

After generation succeeds, save run metadata:

```
<task_cwd>/.visual-anything/runs/figure/<run-id>/last_image.json
```

with shape:

```json
{
  "path": "<image path>",
  "params": {"size": "...", "quality": "...", "output_format": "...", "background": "..."},
  "ts": "<ISO timestamp>",
  "prompt_package": "prompt_package.md"
}
```

---

## STEP 4 — Iterate

Most figure work needs at least one revision round. Classify the user's request:

| Revision type | Example | Route |
|---------------|---------|-------|
| Cosmetic | "brighter", "more contrast", "swap to landscape", "redo at higher quality" | Re-call visual-gen with adjusted parameters; reuse same Prompt Package |
| Pixel-edit | "remove the watermark", "tweak this corner only" | Call visual-gen with `--mode edit` and the previous image path |
| Content (label / palette / title text) | "change title to X", "use systems-blue palette" | Edit the Prompt Package body in place, then re-call visual-gen |
| Structural | "the architecture is wrong", "missing a component", "wrong arrow direction" | Go back to STEP 2; the package itself needs editing first |

If you cannot tell which class the revision belongs to, ask the user one targeted
question. Do not silently pick a route.

Append every revision attempt to `<task_cwd>/.visual-anything/runs/figure/<run-id>/revisions.log`
so the session is recoverable across resumes.

---

## State

Each run lives under `<task_cwd>/.visual-anything/runs/figure/<run-id>/`:

```
prompt_package.md   ← visual-plan output (verbatim)
last_image.json     ← {path, params, ts, prompt_package}
revisions.log       ← one line per revision attempt
```

`<run-id>` = ISO timestamp `YYYYMMDD-HHMMSS`. A new top-level user request opens a
new run; revisions stay inside the most recent run unless the user explicitly
asks to start over.

---

## Boundaries

- Do NOT reimplement what the sub-skills do. No inline gpt-image-2 calls. No
  inline evidence classification. Always invoke the sub-skill.
- API credentials are owned by visual-gen alone. visual-anything never reads, copies,
  prints, or transforms tokens. Never inject Codex- or Claude-side credentials
  into `VISUAL_GEN_API_KEY`.
- If visual-gen's `--show-config` preflight fails, surface the error verbatim
  and STOP. Do not retry the image step with substituted credentials.
- If the user asked only for a prompt, do not run STEP 3. The waste is real —
  gpt-image-2 calls are slow and metered.

---

## Output to user

After STEP 3 succeeds:

```text
图片已生成: <image path>
基于规划包: <task_cwd>/.visual-anything/runs/figure/<run-id>/prompt_package.md
关键参数: size=..., output_format=..., quality=..., palette=...
```

For revisions, briefly state which revision class was detected and which step is
being re-run before doing it. Example:

```text
[识别为 Cosmetic 修订 → 重新调用 visual-gen,size 改为 3840x2160]
```

For STEP 2-only requests (prompt without generation), return the path to
`prompt_package.md` and skip the image-related lines.
