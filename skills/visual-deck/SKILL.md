---
name: visual-deck
description: Use when the user wants a series of PPT-style slide images, slide-style PNGs, 幻灯片图片, PPT 风格的图, literature-review slide deck, academic/business/work-report cover slides, or `/visual-deck`. Do not use for a real editable .pptx or for one standalone figure.
argument-hint: <topic | source path | outline + 可选 style 名>
allowed-tools: [Bash, Read, Write, Edit]
---

# visual-deck

Slide-image orchestrator. It creates N PNGs, one per slide, using image2 / `gpt-image-2`
through `visual-gen`. It does not create `.pptx` files and does not call image APIs
directly.

## Pipeline

```text
input
-> triage: domain_mode, style, length, size, input_mode
-> deck_content_brief.md
-> outline.md with source_refs
-> slide_generation_specs/slide-NN.md with visual_primitive + scene grammar
-> prompts/slide-NN.md
-> scripts/render_slides.py -> visual-gen -> slides/slide-NN.png
-> revisions.log
```

## Triage

Decide before writing content:

- `domain_mode`: read `references/domain-tendencies.md`; choose `sci-research`,
  `sci-structural`, `product-marketing`, `tech-product`, `business-report`, or
  `editorial-creative`. If two fit, use the stricter evidence mode.
- `style`: one file from `styles/` without `.md`. Infer if absent:
  `academic-discussion`, `literature-review`, `work-report`, `business-intro`,
  `tech-product`, or `editorial-creative`.
- length: honor user/outline; otherwise default to 6 slides; cap at 12 unless explicit.
- size: default `1536x1024`; use `3840x2160` for explicit 16:9/4K, `1024x1536` for
  vertical poster. Keep one size across the run.
- `input_mode`: `source`, `outline`, or `topic`.

Source detectors match `visual-anything`: file paths, URLs, PDFs/images/SVGs, repo/code,
or long structured technical text. Ask one question only if the mode changes the result.

## Content Brief

Always create `<run-dir>/deck_content_brief.md` before outlining:

```markdown
# Deck Content Brief
- input_mode: source | outline | topic
- audience: <inferred or provided>
- deck_goal: <one sentence>

## Allowed Claims
- <claim> | source_ref=<source/user-outline/assumption>

## Unknowns
- <missing facts>

## Narrative Arc
- cover: <title idea>
- sections: <labels>
- content beats: <one per content slide>
```

For source material, use `visual-plan` only to extract evidence, assumptions, and
unknowns. The brief is the deck source; a single-figure prompt package is not an outline.
If evidence cannot support enough distinct content slides, reduce length or ask for more
source/permission for a concept deck.

For a user outline, validate `references/outline-schema.md`; preserve user wording and set
missing provenance to `source_refs: ["user-outline"]`. Do not silently truncate.

For topic-only input, make a concept deck. Use `source_refs: ["assumption:topic-only"]`
for generated content and avoid numbers, dates, citations, named results, benchmark
claims, or source-specific assertions.

## Outline

Write `<run-dir>/outline.md` using `references/outline-schema.md`.

Rules:

- first slide `cover`, last slide `closing`
- optional 1-2 `section` dividers only when they match the narrative arc
- each `content` slide carries one content beat
- title budget: ≤10 English words or ≤8 Chinese characters
- captions: 0-2, short, supported by the brief
- every rendered title/caption has `source_refs`

Stop before specs/rendering if length > 12 without opt-in, user-authored text exceeds
budget, or source-backed content has `source_refs: ["needs verification"]`.

## Generation Specs

Read `references/slide-generation-spec.md`. Write one
`slide_generation_specs/slide-NN.md` per slide with:

- `domain_mode`, role, sequence, title, captions
- one `visual_primitive`
- evidence anchors
- mechanism / scene grammar
- must-include details
- must-avoid list
- prompt compile notes

This is still an image2 workflow. Improve the spec/prompt; do not replace it with local
PPT/chart rendering.

## Render

For each slide, compile `prompts/slide-NN.md` by concatenating:

1. `styles/_shared.md`
2. selected `styles/<style>.md`
3. matching generation spec
4. a short slide block with role, sequence, title, captions, non-rendered `source_refs`,
   and `section_number` when needed

Then run:

```bash
python <visual-deck>/scripts/render_slides.py \
  --run-dir <task_cwd>/.visual-anything/runs/deck/<run-id> \
  --jobs 4
```

The runner delegates to sibling `visual-gen` for each slide, uses `quality=high`,
`output-format=png`, renames outputs to `slides/slide-NN.png`, writes `revisions.log`,
and saves `last_run.json` with `render_mode: "parallel"` and `max_concurrency: 4`.

If `visual-gen --show-config` fails, surface the error and stop. Credentials belong only
to `visual-gen`; never read, copy, print, or substitute tokens.

## State

Use `<task_cwd>/.visual-anything/runs/deck/<YYYYMMDD-HHMMSS>/`:

```text
deck_content_brief.md
outline.md
slide_generation_specs/
prompts/
slides/
last_run.json
revisions.log
```

## Iterate

| Revision | Route |
|---|---|
| Cosmetic | Re-render affected slide with same prompt |
| Content | Update brief/outline/spec, recompile, re-render affected slide |
| Restyle | Change style, recompile and regenerate all slides |
| Restructure | Edit outline, renumber, recompile and rerender affected slides |

Append every attempt to `revisions.log`. Ask one question if the class is unclear.

## Boundaries

- No `.pptx`; use the separate `pptx` skill for editable PowerPoint.
- No long paragraphs, code blocks, dense tables, real contact info, or personal data baked
  into slide images.
- No direct image API calls, no inline credential handling, no bypassing the content brief.
- Topic-only decks are concept drafts, not source-grounded reports.

## User Output

After all slides succeed:

```text
共生成 N 张幻灯片图像 (style=<style>, size=<size>):
  <run-dir>/slides/slide-01.png
  ...
大纲: <run-dir>/outline.md
```

For revisions, state the revision class and affected slides before rendering. Confirm once
before full-deck restyle/regeneration.
