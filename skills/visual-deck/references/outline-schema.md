# Outline schema

The orchestrator reads / writes a deck outline at:

```
<task_cwd>/.visual-deck/<run-id>/outline.md
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
slides:
  - role: cover
    title: "Deck Title"
    captions:
      - "subtitle line"
  - role: section
    title: "Background"
    captions: []
  - role: content
    title: "Key insight here"
    captions:
      - "short caption A"
      - "short caption B"
  - role: content
    title: "Second key point"
    captions:
      - "specific evidence"
  - role: closing
    title: "Thanks"
    captions:
      - "Q & A"
```
````

The outline above is the canonical shape. Note these structural conventions:

- The outer YAML keys are exactly: `title`, `style`, `size`, `slides`
- `slides` is a list; each element has exactly: `role`, `title`, `captions`
- `captions` is always a list (possibly empty), never a single string

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

If any rule fails, the orchestrator either auto-corrects (rules 1–2 only) or asks the
user one clarifying question. It NEVER silently truncates user-authored text.

---

## When source material is provided

The orchestrator delegates outline drafting to `visual-plan`, which classifies the
source as paper / repo / algo / hybrid and returns a Prompt Package with an evidence
ledger.

The orchestrator then converts the Package's narrative into the slide list above, with
these rules:

- The Package's main claim → cover `title`
- The Package's top-level structure (typically 2–4 sections) → `section` slides
- Each evidence-supported point in the Package → one `content` slide
- Quantified specifics from the evidence ledger → captions
- Items the Package marked `unknown` → captions tagged `(needs verification)` rather
  than fabricated values
- The orchestrator MUST NOT invent slide content not derivable from the Package

This preserves the Truthfulness Contract that lives in `visual-plan` — it extends to
every line baked into a slide image.

---

## When only a topic is provided

The orchestrator drafts the outline directly (no visual-plan call). Default 6-slide
skeleton:

```yaml
- {role: cover,    title: "<topic>",         captions: ["<one-line subtitle>"]}
- {role: section,  title: "Background",      captions: []}
- {role: content,  title: "<sub-point 1>",   captions: ["<short>", "<short>"]}
- {role: content,  title: "<sub-point 2>",   captions: ["<short>", "<short>"]}
- {role: content,  title: "<sub-point 3>",   captions: ["<short>", "<short>"]}
- {role: closing,  title: "Discussion",      captions: ["Q & A"]}
```

Adjust length only when the user names a specific number.

---

## When the user supplies an outline

Use it verbatim. Run validation against the rules above. Ask one targeted question if
validation fails (e.g., a too-long title, an unknown style name). Do not silently fix
user-authored content.

---

## Editing the outline mid-run (revisions)

The outline is the source of truth. To revise:

- **Cosmetic** revisions don't touch the outline (only re-render the affected slide).
- **Content** revisions edit the affected slide's `title` or `captions`, then re-render
  that slide only.
- **Restyle** revisions update the top-level `style` field and trigger a full re-render.
- **Restructure** revisions insert / remove / merge slides; renumber following slides;
  re-render the affected ones.

After every edit, re-run the validation rules above before STEP 3.
