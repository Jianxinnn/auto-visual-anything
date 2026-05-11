# Visual System

Shared visual language for `visual-plan` outputs: clean scientific/editorial figures with
a dominant claim, one hero mechanism/architecture visual, compact evidence panels, and a
source footer. Avoid generic flowcharts, decorative infographics, and equal-weight box soup.

## Composition

1. Dominant title/question/answer.
2. Central hero diagram carrying the argument.
3. Small evidence, finding, assumption, or chart panels around it.
4. Footer with sources, confidence, unknowns, or assumptions.

If a diagram exceeds ~14 nodes, group into stages/layers before drawing.

## Palettes

Select semantically; use a custom palette only when supplied by the user.

| Profile | Use when | Background | Core | Main path | Novelty/evidence | Warning |
|---|---|---|---|---|---|---|
| `sci-light` | algorithms, general science, repo diagrams | `#FFFFFF/#FAFAF7` | `#24313A` | `#2AA7C8` | `#E8F4FA` | `#F2B84B/#D96C5F` |
| `bio-evidence` | biology, protein, wet-lab evidence | `#FFFFFF/#F8FBF8` | `#234E52` | `#1FA6B8` | `#DFF3EA/#2F8F6B` | `#E5A93C/#C75C54` |
| `systems-blue` | infra, developer tools, agents | `#FFFFFF/#F7FAFC` | `#26323D` | `#2F80C1` | `#E4F3FA` | `#E6A23C/#C84B4B` |
| `data-violet` | analytics, benchmarks, graphs | `#FFFFFF/#FAF9FC` | `#2C2E35` | `#5B6FD6` | `#ECEBFA` | `#D99A2B/#C95F5F` |
| `security-amber` | risk, safety, verification | `#FFFFFF/#FCFAF5` | `#34302A` | `#D9902F` | `#FFF1CC` | `#B94A48` |
| `product-muted` | product/system explainers | `#FFFFFF/#FAFAF7` | `#2B3035` | `#2D9C9C` | `#E3F4F2` | `#D8A03D/#D66A5F` |

Rules: one dark core node at most; most nodes stay light; max four semantic colors plus
neutrals; every color needs a role; grayscale hierarchy must still work.

## Typography

- Poster title: 28-36px, weight 800.
- Section header: 11px, uppercase, weight 700, tracked.
- Key number: 48-64px, weight 800.
- Body/labels: 10-14px; prefer labels over sentences.
- Keep node labels to 1-3 words and text blocks to 2-3 bullets.

## Diagram Language

| Element | Style |
|---|---|
| central orchestrator | one dark rounded rect, white text |
| process/module | light rounded rect, dark border |
| data/storage | pale neutral or novelty fill |
| input/output | labeled rect/parallelogram with accent |
| decision | diamond or rounded rect with `?` |
| external/optional | dashed neutral border |
| warning/error | muted amber/coral/red |

Edges: neutral solid for normal flow, accent solid for the highlighted path, accent dashed
for feedback, gray dashed for conditional, coral/red for error. Route arrows cleanly and
use one highlighted path unless the source truly has multiple modes.

## Charts

Prefer horizontal/vertical bars, lines, grouped bars, small multiples, then scatter. Use
direct labels, no decorative gridlines, no 3D, max 3-4 colors, and only sourced values.

## Layout

- Editorial 2-3 column grid, 16-24px gutters, 20-32px margins.
- A1/poster default: portrait, about 800px wide by 1100px+ tall.
- Header: title/subtitle left; question/answer right when useful.
- Whitespace should clarify hierarchy; if dense, make the page taller instead of shrinking
  text below legibility.

## Icons

Use simple functional outline icons only: storage cylinders, arrows, diamonds, loops,
network dots, warning triangle, or component rectangles. No decorative icon sets.

## QA

Before delivery, confirm:

- one clear focal point
- no overlap/clipping/unreadable text
- every number is sourced or marked assumption/unknown
- footer states sources/confidence/assumptions
- palette and hierarchy still work in grayscale
