---
name: visual-deck
description: >
  visual-deck: use when the user wants a series of PPT-style slide images (one PNG per
  slide, with a title and ≤2 short captions baked into the image). Triggers: "做一组 PPT
  风格的图", "出一套幻灯片图片", "学术汇报封面/章节页", "literature review slide deck",
  "把这篇 paper / repo 做成 deck 图", "工作汇报海报", "商业介绍 cover slide", "/visual-deck",
  or any request asking for "slide-style images" / "幻灯片图片". Orchestrates visual-plan
  (source → outline) and visual-gen (image generation) with a chosen style template.
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
2. Real image generation for each slide (delegated to **visual-gen**)
3. Optional source-grounded outline drafting (delegated to **visual-plan**)

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
[STEP 2] Outline   → produce slide list { role, title, captions[] }
  │                   - source material  → delegate to visual-plan
  │                   - outline supplied → use verbatim (validate)
  │                   - topic only       → orchestrator drafts a 6-slide skeleton
  ▼
[STEP 3] Render    → for each slide:
  │                   compile prompt = styles/_shared.md + styles/<style>.md + slide block
  │                   delegate to visual-gen → slides/slide-NN.png
  ▼
[STEP 4] Iterate   → cosmetic / content / restyle / restructure
                     route back to STEP 3 (or STEP 2 for restructure)
```

---

## STEP 1 — Triage

Decide four things before producing anything:

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
   - source material present (paper / repo / code / diagram / pasted long text) → STEP 2 delegates to `visual-plan`
   - outline supplied (user pastes a yaml/list) → STEP 2 validates and uses verbatim
   - topic only (one phrase like "Make a deck about diffusion models") → STEP 2 drafts inline

Source-material detectors are the same as in `visual-anything` (paths, URLs, ≥ 5 line code blocks,
structured algorithm prose). When ambiguous after one pass, ask exactly one disambiguation
question.

---

## STEP 2 — Outline

Goal: produce a valid `outline.md` that conforms to `references/outline-schema.md`.

### Source-material branch

Delegate to `visual-plan` with the source. Take the resulting Prompt Package's evidence
ledger and narrative arc; convert it into a slide list. Rules:

- ONE `cover` first (deck title from the source's main claim).
- 1–2 `section` dividers reflecting the source's top-level structure (do NOT invent headings the source does not support).
- `content` slides each carrying ONE evidence-supported point. Title = the point in ≤10 EN words / ≤8 CN chars. Captions = up to 2 quantified specifics from the ledger.
- ONE `closing` last.
- If the Prompt Package marked `unknown` in critical positions, flag them in the captions as
  `(needs verification)` rather than fabricating numbers. The Truthfulness Contract that
  lives in visual-plan extends to every caption baked into a slide.

### Outline-supplied branch

Validate against `references/outline-schema.md`. If a title or caption exceeds the length
budget, ask one question only — never silently truncate user-authored text.

### Topic-only branch

Orchestrator drafts a 6-slide skeleton inline (no visual-plan call). The default skeleton:

```yaml
- {role: cover,    title: "<topic>",            captions: ["<one-line subtitle>"]}
- {role: section,  title: "Background",         captions: []}
- {role: content,  title: "<sub-point 1>",      captions: ["<short>", "<short>"]}
- {role: content,  title: "<sub-point 2>",      captions: ["<short>", "<short>"]}
- {role: content,  title: "<sub-point 3>",      captions: ["<short>", "<short>"]}
- {role: closing,  title: "Discussion",         captions: ["Q & A"]}
```

Save the result to `<task_cwd>/.visual-deck/<run-id>/outline.md`. Stop and ask the user
before STEP 3 if **any** of:

- length > 12 (cost guard) — confirm explicit opt-in
- a title violates length budget after auto-shortening attempt
- the source branch produced > 2 slides whose captions all read `(needs verification)`

---

## STEP 3 — Render

For each slide in the outline, in order:

1. Compile the per-slide prompt by concatenating, in this order:
   - `styles/_shared.md` (verbatim — universal hard constraints)
   - `styles/<style>.md` (verbatim — anchors + per-role layout)
   - A short slide-specific block:

     ```
     ## This slide

     - role: <cover | section | content | closing>
     - sequence: NN of TOTAL
     - title: "<title>"
     - captions:
       - "<caption 1>"   # if any
       - "<caption 2>"   # if any
     - section_number: "01"  # only when role == section, zero-padded
     ```

2. Save the compiled prompt to `<task_cwd>/.visual-deck/<run-id>/prompts/slide-NN.md`.

3. Delegate to **visual-gen** with these arguments (always go through the `visual-gen`
   skill — never call `scripts/visual_gen.py` directly):

   | Field | Value |
   |---|---|
   | `--prompt` | the full compiled prompt content from `prompts/slide-NN.md` |
   | `--size` | the size chosen in STEP 1 (constant across the deck) |
   | `--quality` | `high` |
   | `--output-format` | `png` |
   | `--out-dir` | `<task_cwd>/.visual-deck/<run-id>/slides/` |
   | `--n` | `1` |

4. After visual-gen returns its file path, rename / move the file to
   `slides/slide-NN.png` (zero-padded NN). Keep the original visual-gen run metadata
   intact in its own subfolder if it created one — do not delete it.

5. Append one line to `revisions.log`:
   `<ts> render slide-NN role=<role> style=<style> ok=<true|false>`

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
  "slides": ["slides/slide-01.png", "..."],
  "outline": "outline.md",
  "ts": "<ISO timestamp>"
}
```

---

## STEP 4 — Iterate

Most decks need at least one revision pass. Classify the user's revision:

| Type | Example | Route |
|---|---|---|
| **Cosmetic** | "slide 3 更亮", "重出第 5 张,更冷色" | re-call visual-gen for that slide ONLY; reuse compiled prompt |
| **Content** | "把 slide 5 标题改成 X", "caption 改一下" | edit `outline.md` for that slide → recompile prompt → re-call gen for that slide |
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
last_run.json          ← {style, size, count, slides[], outline, ts}
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
  source classification. Always invoke the sub-skill through its public entry.
- API credentials live in `visual-gen` alone. `visual-deck` never reads, copies,
  prints, or transforms tokens. Never inject Codex- or Claude-side credentials.
- Do NOT request more than 12 slides per run without explicit user opt-in. (Each slide is
  one visual-gen call; cost and time scale linearly.)
- Do NOT bake long paragraphs, code, equations, data tables, or real personal info into a
  slide image. B-mode budget = title + ≤2 short captions. Anything denser belongs in a real
  `.pptx` via the separate `pptx` skill.
- Do NOT change the chosen style's 5 anchors mid-deck. Visual consistency is the whole
  point of using a fixed style template.
- Do NOT bypass visual-plan when the user supplied source material. Hand-rolling slide
  content from a paper risks the same hallucination visual-plan was built to prevent.

---

## Output to user

After STEP 3 succeeds:

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
