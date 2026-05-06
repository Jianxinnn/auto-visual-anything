# Visual System — FigureFoundry

This file defines the shared visual language for ALL FigureFoundry outputs.
Every sub-skill and renderer must follow these rules exactly.

---

## THE DESIGN PHILOSOPHY

This is NOT:
- Ultra-minimal Apple design
- Dense scientific figure
- Decorative infographic

This IS:
> A clean, beige, corporate research report style with strong data storytelling,
> structured narrative sections, and clear visual hierarchy.
> Think: McKinsey report × Deloitte insight × editorial data journalism.

The output must feel intentionally designed, not like a generic flowchart. Use scale,
alignment, white space, and a strong central diagram to create a premium technical poster.

---

## SIGNATURE COMPOSITION

Every FigureFoundry output should have a recognizable editorial composition:

1. **Dominant claim** — one large title/question/answer pair that explains the point.
2. **Hero visual** — one central architecture diagram or mechanism diagram that carries
   the story. Avoid scattering many small unrelated diagrams.
3. **Evidence panels** — compact stats, findings, or assumptions around the hero visual.
4. **Source footer** — citation, source paths, confidence, or unknowns.

Avoid "box soup": too many same-sized boxes, evenly weighted labels, and unprioritized
arrows. If a diagram has more than 14 nodes, group nodes into stages or layers first.

---

## COLOR SYSTEM

### Background
- **Primary**: `#F4F1EC` (warm beige — main canvas)
- **Secondary**: `#EFEAE4` (slightly deeper beige — alternate sections)
- **Panel**: `#E8E3DC` (card/block backgrounds)

### Text
- **#111111** — primary text (titles, key numbers, headers)
- **#4A4A4A** — secondary text (body, descriptions)
- **#7A7A7A** — annotations, labels, captions
- **#AAAAAA** — disabled / background annotations

### Accent Colors (STRICT — do not add others)
- **#73C8E0** — soft cyan: primary highlight, active paths, key data
- **#000000** — pure black: maximum contrast, critical emphasis
- **#D9D3C7** — light beige-gray: neutral chart segments, inactive
- **#B8B1A6** — subtle backgrounds, inactive data, secondary fills

### Semantic Colors (use only for meaning)
- **#B91C1C** — error / failure / critical signal (muted deep red)
- **#D97706** — warning / intermediate state (warm amber)
- **#2D7A4F** — success / positive signal (muted green)

### Color Rules
- Dominant palette: beige + black + white
- Cyan (#73C8E0) = primary highlight ONLY — use sparingly
- Max 3–4 colors in any single chart
- Never use bright, saturated, or gradient colors
- Charts: cyan / black / beige-gray + optional red or amber when semantically needed
- Use black for structural anchors and cyan for the single most important path or number.
  If everything is highlighted, nothing is highlighted.

---

## TYPOGRAPHY SYSTEM

### Hierarchy
```
POSTER TITLE     → 28–36px, weight 800, #111111
SECTION HEADER   → 11px, weight 700, #111111, UPPERCASE, letter-spacing 0.12em
KEY NUMBER       → 48–64px, weight 800, #111111 or #73C8E0
SUBSECTION       → 14px, weight 600, #111111
BODY TEXT        → 12–13px, weight 400, #4A4A4A
LABEL            → 11px, weight 500, #4A4A4A
ANNOTATION       → 10px, weight 400, #7A7A7A
CAPTION/FOOTER   → 9–10px, weight 400, #7A7A7A
```

### Rules
- Labels > sentences (prefer short labels over paragraphs)
- Max 2–3 bullets per text block
- No paragraphs — use structured labels
- Numbers must visually dominate their section
- Section headers always UPPERCASE with tracking
- Use short, concrete labels. Rewrite long source phrases into crisp diagram labels while
  preserving meaning.

---

## LINE & BORDER SYSTEM

- Stroke weight: 1–1.5px for diagrams, 0.5px for dividers
- Section dividers: `border-top: 1px solid #D9D3C7`
- Card borders: `border: 1px solid #D9D3C7` with `border-radius: 3px`
- Flow arrows: 1.5px, color #4A4A4A or #73C8E0 for highlighted paths
- No heavy borders or drop shadows (max: `box-shadow: 0 1px 4px rgba(0,0,0,0.06)`)
- Dashed lines: for optional/conditional paths, uncertainty

---

## DIAGRAM LANGUAGE

### Node Types
| Element | Style |
|---------|-------|
| Process / Module | Rounded rect, `#111111` fill, white text OR white fill, `#111111` border |
| Data / Storage | Slightly rounded rect, `#D9D3C7` fill, `#4A4A4A` text |
| Input / Output | Parallelogram or labeled rect, `#73C8E0` accent |
| Decision | Diamond or rounded rect with `?` marker |
| Highlight / Key | `#73C8E0` fill, `#111111` text, 1.5px border |
| External System | Dashed border, `#B8B1A6` fill |
| Loop / Feedback | Circular arrow or return path, dashed `#73C8E0` |

### Edge Types
| Connection | Style |
|-----------|-------|
| Primary data flow | Solid arrow, 1.5px, `#4A4A4A` |
| Key / highlighted path | Solid arrow, 2px, `#73C8E0` |
| Feedback / return | Dashed arrow, 1.5px, `#73C8E0` |
| Conditional | Dashed arrow, 1px, `#7A7A7A` |
| Error path | Solid arrow, 1.5px, `#B91C1C` |

### Diagram Quality Rules

- Prefer stage/lane grouping over drawing 20 isolated modules.
- Keep labels inside nodes to 1–3 words; move details to side annotations.
- Route arrows with minimal crossings. If crossings are unavoidable, use grouping or
  a two-level diagram.
- Align nodes to a grid. Mixed alignment makes technical diagrams look unfinished.
- Use one highlighted path per diagram unless the content genuinely has multiple modes.

---

## CHART STYLES

### Preferred Chart Types (in order)
1. Horizontal bar charts
2. Vertical bar charts
3. Line charts (trends)
4. Grouped bars (comparison)
5. Donut / pie (proportions, ≤4 segments)
6. Small multiples
7. Scatter plots (correlation)

### Chart Rules
- No gridlines
- Minimal axes (1–2 axis lines max)
- Direct labeling on bars/points — no legends if avoidable
- Show exact values always
- Max 3–4 colors per chart
- Bar charts: primary color = cyan, comparison = black/beige-gray

---

## LAYOUT SYSTEM

### Grid
- 2–3 column editorial grid
- Consistent gutter: 16–24px
- Section margin: 24–32px vertical
- Content margin: 20–28px horizontal

### Section Structure (vertical flow)
```
┌─────────────────────────────────────┐
│  HEADER: Title + subtitle + authors  │
│  THE QUESTION ↔ THE ANSWER          │
├─────────────────────────────────────┤
│  SECTION 1: Overview / Framework    │
├─────────────────────────────────────┤
│  SECTION 2: Core Insight + Numbers  │
├─────────────────────────────────────┤
│  SECTION 3: Mechanism / System      │
├─────────────────────────────────────┤
│  SECTION 4: Data / Results          │
├─────────────────────────────────────┤
│  SECTION 5: Supporting Insights     │
├─────────────────────────────────────┤
│  SECTION 6: Conclusions             │
├─────────────────────────────────────┤
│  FOOTER: Citation + source          │
└─────────────────────────────────────┘
```

### Header Layout
- Top-left: Title (bold, large) + Subtitle + Authors
- Top-right: **THE QUESTION** (small caps) → concise question + **THE ANSWER** (bold, direct)
- Thin divider below header

### Whitespace Rules
- Moderate whitespace — not empty, not cluttered
- Clear breathing room between sections
- Dense information within sections, space between them
- Text and diagrams must never overlap. If content is dense, make the poster taller rather
  than shrinking labels below readable size.

---

## VISUAL PRIORITY ALLOCATION

For every output, weight visual space as:
- **40%** → Core insight + key numbers
- **30%** → System / mechanism diagram
- **20%** → Results / charts
- **10%** → Context / setup

---

## ICON SYSTEM

Simple outline icons, thin stroke (1.5px), monochrome, functional not decorative.

| Concept | Icon Form |
|---------|-----------|
| Data / storage | Cylinder / stacked layers |
| Flow / pipeline | Directional arrow sequence |
| Module / component | Rounded rectangle |
| Decision | Diamond |
| Loop / iteration | Circular arrow |
| Network / graph | Connected dots |
| Risk / error | Triangle warning / X mark |
| Agent / entity | Circle with label |
| Aggregation | Converging lines → single point |
| Transformation | Step blocks with arrow |
| Feedback | Curved return arrow |

---

## POSTER FORMAT

- **Orientation**: Portrait (A1 ratio — approximately 594 × 841mm proportions)
- **HTML equivalent**: ~800px wide × 1130px tall (or taller for complex content)
- **Aspect ratio**: ~1:1.415
- Background: `#F4F1EC`
- All content within consistent margins

---

## VISUAL QA BEFORE DELIVERY

Before final output:
- Confirm the figure plan has one clear visual focal point.
- Confirm no text overlaps, clips, or becomes unreadable.
- Confirm every stat or chart value is sourced or labeled as assumption/unknown.
- Confirm the footer states sources, confidence, or assumptions.
- Confirm the page still looks premium in grayscale: hierarchy should not depend only on cyan.
