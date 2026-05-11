---
name: visual-deck
description: >
  visual-deck: use when the user wants a series of PPT-style slide images (one PNG per
  slide, with a title and ≤2 short captions baked into the image). Triggers: "做一组 PPT
  风格的图", "出一套幻灯片图片", "学术汇报封面/章节页", "literature review slide deck",
  "把这篇 paper / repo 做成 deck 图", "工作汇报海报", "商业介绍 cover slide", "/visual-deck",
  or any request asking for "slide-style images" / "幻灯片图片". Builds a deck-specific
  content brief, outline, and per-slide generation specs, then uses visual-gen / image2
  for direct image generation.
  Persists run state under <task_cwd>/.visual-deck/<run-id>/. Do NOT trigger if the user
  wants a real editable .pptx (use the `pptx` skill) or one figure (use visual-anything / -plan / -gen).
argument-hint: <topic | source path | outline + 可选 style 名>
allowed-tools: [Bash, Read, Write, Edit]
---

# visual-deck — Source/Topic → Slide-Image Series (orchestrator)

The visual-anything family extension for **slide-image series**. Each run produces N PNG files,
each one styled like a single PPT page. This is the conductor; it does **not** duplicate
sub-skill work.

Use it when you want all three of:

1. A coherent multi-slide visual narrative (cover → sections → content → closing)
2. Direct image2 generation for each slide (delegated to **visual-gen**)
3. Deck-specific content and generation specs before rendering, so slide content is not improvised

If the user wants ONE figure, use `visual-anything`. If they want an editable `.pptx`, use the
`pptx` skill — `visual-deck` produces images, not `.pptx`.

---

## Pipeline

```
INPUT  (source / topic / outline + optional style)
  │
  ▼
[STEP 1] Triage    → pick style + decide deck length + pick size
  │
  ▼
[STEP 2] Content   → produce deck_content_brief.md
  │                   - source material  → use visual-plan for evidence extraction only
  │                   - outline supplied → use verbatim (validate)
  │                   - topic only       → concept draft, no factual specifics
  ▼
[STEP 3] Outline   → produce slide list { role, title, captions[], source_refs[] }
  │                   every rendered title/caption must be backed by a source_ref,
  │                   user outline, or explicit assumption
  ▼
[STEP 4] Generation specs → produce slide_generation_specs/slide-NN.md
  │                   primitive + scene grammar + detail level + must-avoid list
  ▼
[STEP 5] Render    → for each slide:
  │                   compile prompt = styles/_shared.md + styles/<style>.md + slide block
  │                   render compiled prompts in parallel via visual-gen → slides/slide-NN.png
  ▼
[STEP 6] Iterate   → cosmetic / content / restyle / restructure
                     route back to STEP 4 (or STEP 2/3 for content changes)
```

---

## STEP 1 — Triage

Decide five things before producing anything:

0. **domain_mode** — read `references/domain-tendencies.md` and choose one:
   `sci-research`, `sci-structural`, `product-marketing`, `tech-product`,
   `business-report`, or `editorial-creative`. If two modes fit, choose the
   stricter content mode; for example, protein-design decks are `sci-structural`
   before they are product or report decks.

1. **style** — pick from the filenames in `styles/` (without `.md`). If the user named one,
   honor it. Otherwise infer from domain: paper/algorithm/theory talk → `academic-discussion`;
   survey/review → `literature-review`; weekly/quarterly report → `work-report`;
   pitch/customer/investor → `business-intro`; launch/eng-demo → `tech-product`;
   design/portfolio → `editorial-creative`. If still ambiguous, default to `academic-discussion`.

2. **deck length** — if user gave a number, honor it (cap at 12 unless explicit opt-in).
   If outline supplied, use its length. Otherwise default to **6 slides**:
   `cover → section(Background) → content × 3 → closing`.

3. **size** — default `1536x1024` (4:3 landscape, balanced cost). Use `3840x2160` only when
   user asks for "16:9", "4K", "大屏". Use `1024x1536` for "vertical / 海报 / poster mode".
   Whatever you pick, the SAME size MUST apply to every slide of the run (visual consistency).

4. **input mode** —
   - source material present (paper / repo / code / diagram / pasted long text) → STEP 2 builds a sourced content brief
   - outline supplied (user pastes a yaml/list) → STEP 2 validates and uses it as user-authored content
   - topic only (one phrase like "Make a deck about diffusion models") → STEP 2 drafts conceptual content only

Source-material detectors are the same as in `visual-anything` (paths, URLs, ≥ 5 line code blocks,
structured algorithm prose). When ambiguous after one pass, ask exactly one disambiguation
question.

---

## STEP 2 — Content brief

Goal: produce `<task_cwd>/.visual-deck/<run-id>/deck_content_brief.md` before any
slide image prompts are compiled.

The content brief is the guardrail that prevents pretty but empty decks. Use this
shape:

```markdown
# Deck Content Brief

- input_mode: source | outline | topic
- audience: <inferred or user-provided>
- deck_goal: <one sentence>

## Allowed Claims
- <claim> | source_ref=<path/section/user-outline/assumption>

## Unknowns
- <important missing facts>

## Narrative Arc
- cover: <literal title idea>
- sections: <1-3 section labels>
- content beats: <one evidence-supported point per content slide>
```

### Source-material branch

Use `visual-plan` to inspect the source and produce source-grounded facts,
evidence, assumptions, and unknowns. Do **not** treat visual-plan's Prompt
Package as a deck outline. A single-figure prompt package is only an evidence
input; the deck outline must be derived from the deck content brief.

Rules:

- Every allowed claim must come from the source, visual-plan evidence ledger, or
  user-provided text.
- If the source does not support enough distinct content beats, reduce the deck
  length instead of padding with generic slides.
- If more than two intended content slides have only unknowns, stop and ask for
  more source material or permission to make a concept-only deck.
- Do not invent section headings just to make the deck feel balanced.

### Outline-supplied branch

Validate against `references/outline-schema.md`. Treat user-authored titles and
captions as `source_ref=user-outline`. If a title or caption exceeds the length
budget, ask one question only — never silently truncate user-authored text.

### Topic-only branch

Draft a concept deck, not a factual report. Use broad, non-quantified framing and
set `source_ref=assumption:topic-only` for every generated title/caption.

Topic-only decks must not include:

- numeric claims, benchmark values, dates, citations, or named paper results
- claims about a specific repo, paper, company, product, person, or dataset
- "industry standard" or "state of the art" assertions

If the user asks for any of those, ask for source material or route to a real
research / citation workflow before rendering.

---

## STEP 3 — Outline

Goal: produce a valid `outline.md` that conforms to `references/outline-schema.md`.

Build the outline from the content brief:

- ONE `cover` first (deck title from the brief's deck goal).
- 1–2 `section` dividers only if they match the brief's narrative arc.
- `content` slides each carry ONE content beat. Title = the point in ≤10 EN words / ≤8 CN chars. Captions = up to 2 specifics from the brief.
- ONE `closing` last.
- Every slide has `source_refs`. These are non-rendered provenance notes used for
  validation and revision; do not ask visual-gen to draw them.
- If a content beat is unsupported, either mark the slide with
  `source_refs: ["needs verification"]` and ask before rendering, or remove the slide.

```yaml
- role: content
  title: "<short point>"
  captions:
    - "<short evidence or concept caption>"
  source_refs:
    - "<file/section/user-outline/assumption>"
```

Save the result to `<task_cwd>/.visual-deck/<run-id>/outline.md`. Stop and ask the user
before STEP 4 if **any** of:

- length > 12 (cost guard) — confirm explicit opt-in
- a title violates length budget after auto-shortening attempt
- any source-backed content slide has `source_refs: ["needs verification"]`

---

## STEP 4 — Generation specs

Goal: produce `<task_cwd>/.visual-deck/<run-id>/slide_generation_specs/slide-NN.md`
before compiling image prompts.

Read `references/slide-generation-spec.md`. Each spec should contain:

- `domain_mode`
- role / sequence / title / captions
- one `visual_primitive`
- evidence anchors
- mechanism / scene grammar
- must-include visual details
- must-avoid list
- prompt compile notes

This is still an image2 workflow. Do not replace image generation with a local chart
or PPT renderer. The spec exists to make image2 draw a richer, more constrained slide.

SCI slides should describe the mechanism explicitly: state contrast, residue/motif
logic, screening path, evidence gate, uncertainty branch, or next-round SOP. Product
slides should describe the product/object/workflow/decision surface explicitly.

---

## STEP 5 — Render

For each slide in the outline, in order:

1. Compile the per-slide prompt by concatenating, in this order:
   - `styles/_shared.md` (verbatim — universal hard constraints)
   - `styles/<style>.md` (verbatim — anchors + per-role layout)
   - the matching `slide_generation_specs/slide-NN.md` content
   - A short slide-specific block:

     ```
     ## This slide

     - role: <cover | section | content | closing>
     - sequence: NN of TOTAL
     - title: "<title>"
     - captions:
       - "<caption 1>"   # if any
       - "<caption 2>"   # if any
     - source_refs: ["..."]  # provenance only; DO NOT render
     - section_number: "01"  # only when role == section, zero-padded
     ```

2. Save the compiled prompt to `<task_cwd>/.visual-deck/<run-id>/prompts/slide-NN.md`.
   The prompt should contain concrete scene grammar, not only title/captions.

3. After all prompts are saved, render them with the bundled runner:

   ```bash
   python <visual-deck>/scripts/render_slides.py \
     --run-dir <task_cwd>/.visual-deck/<run-id> \
     --jobs 4
   ```

   Default render mode is parallel with `--jobs 4`. Lower it only when the image API is
   rate-limited or the user asks for serial generation. The runner delegates to the sibling
   **visual-gen** CLI for each slide; it never calls the image API directly.

4. The runner calls **visual-gen** once per prompt with these arguments:

   | Field | Value |
   |---|---|
   | `--prompt` | the full compiled prompt content from `prompts/slide-NN.md` |
   | `--size` | the size chosen in STEP 1 (constant across the deck) |
   | `--quality` | `high` |
   | `--output-format` | `png` |
   | `--out-dir` | `<task_cwd>/.visual-deck/<run-id>/slides/` |
   | `--n` | `1` |

5. After visual-gen returns each file path, the runner renames / moves it to
   `slides/slide-NN.png` (zero-padded NN).

6. The runner appends one line per slide to `revisions.log`:
   `<ts> render slide-NN role=<role> style=<style> ok=<true|false> mode=parallel jobs=4`

If visual-gen's `--show-config` preflight fails, surface the error verbatim and STOP.
Do not fabricate, retry with substituted credentials, or partially generate the deck.

When ALL slides succeed, save run summary:

```
<task_cwd>/.visual-deck/<run-id>/last_run.json
```

with shape:

```json
{
  "style": "<style>",
  "size": "<size>",
  "count": N,
  "render_mode": "parallel",
  "max_concurrency": 4,
  "slides": ["slides/slide-01.png", "..."],
  "outline": "outline.md",
  "ts": "<ISO timestamp>"
}
```

---

## STEP 6 — Iterate

Most decks need at least one revision pass. Classify the user's revision:

| Type | Example | Route |
|---|---|---|
| **Cosmetic** | "slide 3 更亮", "重出第 5 张,更冷色" | re-call visual-gen for that slide ONLY; reuse compiled prompt |
| **Content** | "把 slide 5 标题改成 X", "caption 改一下" | edit `deck_content_brief.md` if the claim changes → update `outline.md` and `slide_generation_specs/slide-NN.md` → recompile prompt → re-call gen for that slide |
| **Restyle** | "整套换成 literature-review 风格" | change `style` in `outline.md` → recompile ALL prompts → regenerate ALL slides |
| **Restructure** | "合并 slide 4 和 5", "再加一页讲 ablation" | edit `outline.md` (insert/delete/merge) → recompile and regenerate the AFFECTED slides only; renumber following slides |

Append every revision attempt to `revisions.log` so the run is recoverable across resumes.

If you cannot tell which class a revision belongs to, ask one targeted question. Do not
silently pick a route.

---

## State

Each run lives under `<task_cwd>/.visual-deck/<run-id>/`:

```
outline.md             ← canonical deck outline (yaml in markdown wrapper)
deck_content_brief.md  ← content claims, unknowns, and provenance
last_run.json          ← {style, size, count, render_mode, max_concurrency, slides[], outline, ts}
slide_generation_specs/
  slide-01.md          ← primitive, evidence anchors, scene grammar, prompt notes
prompts/
  slide-01.md          ← compiled prompt for slide 1
  slide-NN.md
slides/
  slide-01.png         ← rendered slide image 1
  slide-NN.png
revisions.log          ← one line per render or revision attempt
```

`<run-id>` = ISO timestamp `YYYYMMDD-HHMMSS`. A new top-level user request opens a new
run. Revisions stay inside the most recent run unless the user explicitly says "start over".

---

## Boundaries

- Do NOT reimplement what the sub-skills do. No inline `gpt-image-2` calls. No inline
  source classification. Use `scripts/render_slides.py` for deck rendering; it delegates
  each slide to the sibling `visual-gen` CLI.
- API credentials live in `visual-gen` alone. `visual-deck` never reads, copies,
  prints, or transforms tokens. Never inject Codex- or Claude-side credentials.
- Do NOT request more than 12 slides per run without explicit user opt-in. (Each slide is
  one visual-gen call; cost and time scale linearly.)
- Do NOT bake long paragraphs, code, equations, data tables, or real personal info into a
  slide image. B-mode budget = title + ≤2 short captions. Anything denser belongs in a real
  `.pptx` via the separate `pptx` skill.
- Do NOT replace image2 generation with a deterministic PPT/chart renderer inside this
  skill. Improve the image2 prompt plan instead.
- Do NOT change the chosen style's 5 anchors mid-deck. Visual consistency is the whole
  point of using a fixed style template.
- Do NOT bypass the content brief. Rendering directly from a topic or a visual-plan
  Prompt Package is how generic or fabricated decks happen.
- Do NOT present topic-only decks as source-grounded. They are concept drafts unless
  the user supplies sources.

---

## Output to user

After STEP 5 succeeds:

```text
共生成 N 张幻灯片图像 (style=<style>, size=<size>):
  <task_cwd>/.visual-deck/<run-id>/slides/slide-01.png
  <task_cwd>/.visual-deck/<run-id>/slides/slide-02.png
  ...
大纲: <task_cwd>/.visual-deck/<run-id>/outline.md
```

For revisions, briefly state which revision class was detected and which slides are being
re-rendered, before doing it. Example:

```text
[识别为 Cosmetic 修订 → 仅重出 slide-03,其余保留]
```

For a restyle, warn the user that the entire deck will regenerate and confirm once before
firing N calls.
