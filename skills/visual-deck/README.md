# visual-deck

> The visual-anything family extension for **slide-image series**.
> Produces N PNG images, each styled like a single PPT slide.
> Uses image2 / gpt-image-2 directly, with per-slide generation specs to avoid empty or generic slides.
> No `.pptx`. No HTML container. Just images.

## Family map

| Skill | Produces | Use when |
|---|---|---|
| `visual-deck` | A series of slide-style PNG images (cover + sections + content + closing) | You want "PPT 风格的系列图片" |
| `visual-anything` | One scientific figure (plan + image), end to end | One figure from one source |
| `visual-plan` | A grounded prompt package (no rendering) | You only need the prompt |
| `visual-gen` | One image from a finalized prompt | You already have the prompt |
| `pptx` (separate) | A real, editable `.pptx` file | You need PowerPoint output |

## Pipeline

```
input ──► [visual-deck] triage  (pick style, length, size)
              │
              ├── source / paper / repo  ──► visual-plan evidence ──► content brief
              │
              └── topic-only / outline   ───────────────────►  content brief
                                                                  │
                              ┌───────────────────────────────────┘
                              ▼
                  [visual-deck] outline: slide list + provenance
                              │
                              ▼
                  [visual-deck] generation spec: primitive + scene grammar
                              │
                              ▼
                  [visual-deck] render: per slide compile prompt
                              │
                              ▼  (4 parallel visual-gen calls by default)
                       visual-gen ──► slides/slide-NN.png
                              │
                              ▼
                       revision loop (cosmetic / content / restyle / restructure)
```

## Styles shipped

| Style | When to pick | Anchors at a glance |
|---|---|---|
| `academic-discussion` | Lab meeting, journal club, conference talk | navy + warm off-white + rust accent; serif title; ⅓-⅔ asymmetric |
| `literature-review` | Survey / review / 综述汇报 | parchment + ink + ochre accent; transitional serif; index-card grid |
| `work-report` | Internal weekly / monthly / quarterly | slate + pale steel + emerald; geometric sans; 2-column |
| `business-intro` | Investor / customer pitch | midnight + cyan + cream; bold geometric sans; full-bleed hero |
| `tech-product` | Launch / engineering demo | near-black + graphite + one neon accent; mono / technical sans; tick-scale motif |
| `editorial-creative` | Design / portfolio / magazine cover | bone + char + vermilion; high-contrast serif; asymmetric, oversized type |

Every style fixes the same **5 anchors**: color palette, typography, layout grid, recurring
motif, background — so all slides in one deck stay visually consistent across the N image
generations.

## Domain modes and generation specs

Before rendering, `visual-deck` chooses a `domain_mode` from
`references/domain-tendencies.md` and writes one
`slide_generation_specs/slide-NN.md` per slide. These specs are image2 prompt
contracts, not local drawing instructions.

They define:

- visual primitive (`pipeline`, `risk_map`, `workflow`, `product_hero`, etc.)
- evidence anchors
- mechanism / scene grammar
- must-include visual details
- must-avoid list
- prompt compile notes

See `references/slide-generation-spec.md`.

## Slide roles

Every slide has exactly one of four roles. Role + style uniquely determines the layout.

| Role | What it carries | When |
|---|---|---|
| `cover` | Deck title + ≤1 subtitle | Always slide 1 |
| `section` | A section number + section title (+ optional 1-line caption) | Between content blocks |
| `content` | A point title + ≤2 short captions | The bulk of the deck |
| `closing` | A short closing word (+ optional Q&A line) | Always last |

See `references/slide-roles.md` for the full taxonomy.

## State (per run)

```
<task_cwd>/.visual-anything/runs/deck/<YYYYMMDD-HHMMSS>/
├── outline.md             # the deck outline (yaml in md)
├── deck_content_brief.md  # content claims, unknowns, and provenance
├── last_run.json          # {style, size, count, render_mode, max_concurrency, slides[], outline, ts}
├── slide_generation_specs/slide-NN.md
├── prompts/slide-NN.md    # compiled per-slide prompt (style preamble + slide block)
├── slides/slide-NN.png    # the rendered slide images
└── revisions.log          # one line per render / revision attempt
```

## Layout

```text
visual-deck/
├── SKILL.md                          # orchestration rules (triage / outline / render / iterate)
├── README.md                         # this file
├── scripts/
│   └── render_slides.py              # parallel runner; delegates each slide to visual-gen
├── styles/
│   ├── _shared.md                    # universal hard constraints (B-mode budget, anti-AI tells)
│   ├── academic-discussion.md
│   ├── literature-review.md
│   ├── work-report.md
│   ├── business-intro.md
│   ├── tech-product.md
│   └── editorial-creative.md
└── references/
    ├── domain-tendencies.md
    ├── slide-generation-spec.md
    ├── slide-roles.md
    └── outline-schema.md
```

No credentials and no new dependencies. Image generation routes through `visual-gen`;
`scripts/render_slides.py` only schedules the per-slide calls in parallel, defaulting to
`--jobs 4`. `visual-plan` is used only as a source-grounded evidence helper when source
material exists. `visual-deck` owns the deck content brief, outline, and generation specs.

## Why a separate skill

- `visual-anything` produces ONE figure; `visual-deck` produces N styled slide images.
- The "deck-level visual consistency" problem (5 anchors held constant across N prompts)
  is its own concern; baking it into `visual-anything` would bloat a clean orchestrator.
- A separate skill lets the style library evolve independently. Adding a new style is one
  markdown file in `styles/` plus one row in this README.
- Credentials still live in `visual-gen` alone. The boundary is preserved.

## What this skill does NOT do

- It does not produce `.pptx`. If you need real PowerPoint, use the `pptx` skill on top
  (e.g., insert these PNGs as full-bleed slide backgrounds with empty text frames).
- It does not bake long paragraphs / data tables / code blocks into images — gpt-image-2's
  text rendering breaks down beyond a short title plus 1–2 captions. The B-mode budget is
  intentional.
- It does not replace image2 generation with a local PPT/chart renderer. If a slide is bad,
  improve the generation spec and prompt, then regenerate.
- It does not turn a single-figure prompt package directly into slides. Source material
  first becomes a `deck_content_brief.md`, then an outline.
- It does not present topic-only decks as factual reports. Topic-only output is a concept
  draft unless the user supplies sources.
