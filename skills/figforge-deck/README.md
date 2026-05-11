# figforge-deck

> The figforge family extension for **slide-image series**.
> Produces N PNG images, each styled like a single PPT slide.
> Title + ≤2 short captions are baked into each image.
> No `.pptx`. No HTML container. Just images.

## Family map

| Skill | Produces | Use when |
|---|---|---|
| `figforge-deck` | A series of slide-style PNG images (cover + sections + content + closing) | You want "PPT 风格的系列图片" |
| `figforge` | One scientific figure (plan + image), end to end | One figure from one source |
| `figforge-plan` | A grounded prompt package (no rendering) | You only need the prompt |
| `figforge-gen` | One image from a finalized prompt | You already have the prompt |
| `pptx` (separate) | A real, editable `.pptx` file | You need PowerPoint output |

## Pipeline

```
input ──► [figforge-deck] triage  (pick style, length, size)
              │
              ├── source / paper / repo  ──► figforge-plan ──► outline
              │
              └── topic-only / outline   ───────────────────►  outline
                                                                  │
                              ┌───────────────────────────────────┘
                              ▼
                  [figforge-deck] render: per slide compile prompt
                              │
                              ▼  (one figforge-gen call per slide)
                       figforge-gen ──► slides/slide-NN.png
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
<task_cwd>/.figforge-deck/<YYYYMMDD-HHMMSS>/
├── outline.md             # the deck outline (yaml in md)
├── last_run.json          # {style, size, count, slides[], outline, ts}
├── prompts/slide-NN.md    # compiled per-slide prompt (style preamble + slide block)
├── slides/slide-NN.png    # the rendered slide images
└── revisions.log          # one line per render / revision attempt
```

## Layout

```text
figforge-deck/
├── SKILL.md                          # orchestration rules (triage / outline / render / iterate)
├── README.md                         # this file
├── styles/
│   ├── _shared.md                    # universal hard constraints (B-mode budget, anti-AI tells)
│   ├── academic-discussion.md
│   ├── literature-review.md
│   ├── work-report.md
│   ├── business-intro.md
│   ├── tech-product.md
│   └── editorial-creative.md
└── references/
    ├── slide-roles.md
    └── outline-schema.md
```

No scripts, no credentials, no new dependencies. Everything routes through `figforge-gen`
for image generation and (when source material exists) `figforge-plan` for outline drafting.

## Why a separate skill

- `figforge` produces ONE figure; `figforge-deck` produces N styled slide images.
- The "deck-level visual consistency" problem (5 anchors held constant across N prompts)
  is its own concern; baking it into `figforge` would bloat a clean orchestrator.
- A separate skill lets the style library evolve independently. Adding a new style is one
  markdown file in `styles/` plus one row in this README.
- Credentials still live in `figforge-gen` alone. The boundary is preserved.

## What this skill does NOT do

- It does not produce `.pptx`. If you need real PowerPoint, use the `pptx` skill on top
  (e.g., insert these PNGs as full-bleed slide backgrounds with empty text frames).
- It does not bake long paragraphs / data tables / code blocks into images — gpt-image-2's
  text rendering breaks down beyond a short title plus 1–2 captions. The B-mode budget is
  intentional.
- It does not invent slide content from thin air when you supply source material — that
  job is delegated to `figforge-plan`, which carries an evidence ledger.
