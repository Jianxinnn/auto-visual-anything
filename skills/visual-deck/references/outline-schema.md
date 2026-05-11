# Outline schema

The orchestrator reads / writes a deck outline at:

```
<task_cwd>/.visual-anything/runs/deck/<run-id>/outline.md
```

The outline is YAML embedded in a markdown wrapper for readability. The orchestrator
parses the YAML block and ignores any prose around it.

---

## Schema

````markdown
# Deck Outline

```yaml
title: "Deck Title"                  # ≤ 10 EN words / ≤ 8 CN chars
style: academic-discussion           # one of styles/*.md filenames (without .md)
size: 1536x1024                      # one of visual-gen's supported sizes
content_mode: source                 # source | outline | topic
domain_mode: sci-research            # see references/domain-tendencies.md
generation_spec_refs:
  - slide_generation_specs/slide-01.md
slides:
  - role: cover
    title: "Deck Title"
    captions:
      - "subtitle line"
    source_refs:
      - "source:abstract"
  - role: section
    title: "Background"
    captions: []
    source_refs:
      - "deck_content_brief.md"
  - role: content
    title: "Key insight here"
    captions:
      - "short caption A"
      - "short caption B"
    visual_primitive: pipeline
    source_refs:
      - "paper:results"
  - role: content
    title: "Second key point"
    captions:
      - "specific evidence"
    source_refs:
      - "user-outline"
  - role: closing
    title: "Thanks"
    captions:
      - "Q & A"
    source_refs:
      - "deck convention"
```
````

The outline above is the canonical shape. Note these structural conventions:

- The outer YAML keys are: `title`, `style`, `size`, `content_mode`, optional
  `domain_mode`, optional `generation_spec_refs`, and `slides`
- `content_mode` is one of `source`, `outline`, or `topic`
- `slides` is a list; each element has `role`, `title`, `captions`, `source_refs`, and
  optional `visual_primitive`
- `captions` is always a list (possibly empty), never a single string
- `source_refs` is always a list (possibly empty). It is provenance metadata and must not
  be rendered into the slide image.
- `generation_spec_refs` points to per-slide generation specs used to compile rich image2
  prompts.

---

## Rules the orchestrator enforces before STEP 3 (render)

1. The first slide MUST be `role: cover`. If missing, the orchestrator inserts a default
   cover whose `title` = the outer `title` and `captions` = [].
2. The last slide MUST be `role: closing`. If missing, the orchestrator inserts a default
   closing with `title: "Thanks"` and `captions: ["Q & A"]`.
3. `style` MUST match an existing file in `styles/` (filename minus `.md`). If not,
   STOP and ask the user which style to use.
4. `size` MUST be one of visual-gen's supported values. The orchestrator passes it
   through; visual-gen validates. Common choices:
   - `1536x1024` (4:3 landscape) — default
   - `3840x2160` (16:9 4K) — premium / large-screen
   - `1024x1024` (square) — social-style decks only
   - `1024x1536` (3:4 portrait) — poster-style handouts
5. Per-slide budgets:
   - `title` length ≤ 10 EN words OR ≤ 8 CN chars
   - `captions` array length 0–2
   - each caption ≤ 14 EN words OR ≤ 16 CN chars
   - `role` ∈ {`cover`, `section`, `content`, `closing`}
6. `len(slides)` ≤ 12 unless the user explicitly opted in to a longer run (cost guard).
7. For `content_mode: source`, every rendered title/caption on `content` slides must map
   to at least one real source reference. `needs verification` requires user confirmation
   before rendering.
8. For `content_mode: topic`, `source_refs` must use `assumption:topic-only`; captions
   must not contain numbers, dates, citations, benchmark values, or source-specific claims.

If any rule fails, the orchestrator either auto-corrects (rules 1–2 only) or asks the
user one clarifying question. It NEVER silently truncates user-authored text.

---

## When source material is provided

The orchestrator uses `visual-plan` to classify the source and extract evidence. It then
creates `deck_content_brief.md`. The brief, not the single-figure Prompt Package, is the
input to outline drafting.

The orchestrator converts the brief into the slide list above, with these rules:

- The Package's main claim → cover `title`
- The Package's top-level structure (typically 2–4 sections) → `section` slides
- Each evidence-supported point in the Package → one `content` slide
- Quantified specifics from the evidence ledger → captions
- Items the brief or visual-plan evidence marked `unknown` → captions tagged
  `(needs verification)` rather than fabricated values
- Every rendered title/caption receives a `source_refs` entry
- The orchestrator MUST NOT invent slide content not derivable from the brief

This preserves the Truthfulness Contract that lives in `visual-plan` — it extends to
every line baked into a slide image.

---

## When only a topic is provided

The orchestrator drafts a concept brief directly (no visual-plan call), then makes an
outline. Default 6-slide skeleton:

```yaml
- {role: cover,    title: "<topic>",       captions: ["Concept draft"], source_refs: ["assumption:topic-only"]}
- {role: section,  title: "Background",    captions: [], source_refs: ["assumption:topic-only"]}
- {role: content,  title: "<sub-point 1>", captions: ["short conceptual caption"], source_refs: ["assumption:topic-only"]}
- {role: content,  title: "<sub-point 2>", captions: ["short conceptual caption"], source_refs: ["assumption:topic-only"]}
- {role: content,  title: "<sub-point 3>", captions: ["short conceptual caption"], source_refs: ["assumption:topic-only"]}
- {role: closing,  title: "Discussion",    captions: ["Q & A"], source_refs: ["deck convention"]}
```

Adjust length only when the user names a specific number. Do not add factual specifics
without source material.

---

## When the user supplies an outline

Use it verbatim. Run validation against the rules above. If `source_refs` is missing,
set it to `["user-outline"]` rather than inventing provenance. Ask one targeted question
if validation fails (e.g., a too-long title, an unknown style name). Do not silently fix
user-authored content.

---

## Editing the outline mid-run (revisions)

The outline is the source of truth. To revise:

- **Cosmetic** revisions don't touch the outline (only re-render the affected slide).
- **Content** revisions update `deck_content_brief.md` when claims change, edit the
  affected slide's `title`, `captions`, or `source_refs`, then re-render that slide only.
- **Restyle** revisions update the top-level `style` field and trigger a full re-render.
- **Restructure** revisions insert / remove / merge slides; renumber following slides;
  re-render the affected ones.

After every edit, re-run the validation rules above before STEP 3.
