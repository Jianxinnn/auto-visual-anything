# Visual System — figforge-plan

This file defines the shared visual language for ALL figforge-plan outputs.
Every sub-skill and renderer must follow these rules exactly.

---

## THE DESIGN PHILOSOPHY

This is NOT:
- Ultra-minimal Apple design
- Dense scientific figure
- Decorative infographic

This IS:
> A clean scientific figure system with strong data storytelling, structured narrative
> sections, and clear visual hierarchy.
> Think: Nature Computational Science / Nature Machine Intelligence figure discipline,
> with enough editorial polish for technical reports.

The output must feel intentionally designed, not like a generic flowchart. Use scale,
alignment, white space, and a strong central diagram to create a premium technical poster.

---

## SIGNATURE COMPOSITION

Every figforge-plan output should have a recognizable editorial composition:

1. **Dominant claim** — one large title/question/answer pair that explains the point.
2. **Hero visual** — one central architecture diagram or mechanism diagram that carries
   the story. Avoid scattering many small unrelated diagrams.
3. **Evidence panels** — compact stats, findings, or assumptions around the hero visual.
4. **Source footer** — citation, source paths, confidence, or unknowns.

Avoid "box soup": too many same-sized boxes, evenly weighted labels, and unprioritized
arrows. If a diagram has more than 14 nodes, group nodes into stages or layers first.

---

## PALETTE SYSTEM

figforge-plan does not use one fixed color scheme for every project. Select a palette
based on the source domain and the figure's main claim, then state the palette rationale
in the prompt package.

### Palette Selector

Use these defaults unless the user supplies a brand palette:

| Profile | Use When | Background | Core | Main Path | Novelty / Output | Optional / External | Warning |
|---------|----------|------------|------|-----------|------------------|---------------------|---------|
| **sci-light** | General scientific software, algorithms, repo architecture | `#FFFFFF` / `#FAFAF7` | slate `#24313A` only for the central orchestrator; normal modules use light fills | cyan-blue `#2AA7C8` | soft blue `#E8F4FA` | gray dashed `#9AA6AF` | amber `#F2B84B`, coral `#D96C5F` |
| **bio-evidence** | Biology, protein design, wet-lab or evidence workflows | `#FFFFFF` / `#F8FBF8` | deep teal `#234E52` sparingly | cyan-teal `#1FA6B8` | mint `#DFF3EA` / green-teal `#2F8F6B` | gray-green dashed `#AAB8B2` | amber `#E5A93C`, muted red `#C75C54` |
| **systems-blue** | Infrastructure, developer tools, pipelines, agents | `#FFFFFF` / `#F7FAFC` | slate `#26323D` sparingly | blue `#2F80C1` | pale cyan `#E4F3FA` | gray dashed `#A4B0BA` | amber `#E6A23C`, red `#C84B4B` |
| **data-violet** | Analytics, evaluation, benchmarks, knowledge graphs | `#FFFFFF` / `#FAF9FC` | charcoal `#2C2E35` sparingly | indigo `#5B6FD6` | lavender `#ECEBFA` | gray dashed `#A8AAB7` | amber `#D99A2B`, red `#C95F5F` |
| **security-amber** | Risk, verification, safety, compliance, threat models | `#FFFFFF` / `#FCFAF5` | slate-brown `#34302A` sparingly | amber `#D9902F` | pale gold `#FFF1CC` | gray dashed `#AAA39A` | red `#B94A48` |
| **product-muted** | Product/system explainers, SaaS-like but still scholarly | `#FFFFFF` / `#FAFAF7` | graphite `#2B3035` sparingly | muted teal `#2D9C9C` | pale teal `#E3F4F2` | gray dashed `#A6ADB3` | amber `#D8A03D`, coral `#D66A5F` |

### Universal Color Roles

- **Central orchestrator / core claim**: one dark filled node at most, preferably deep slate
  rather than pure black.
- **Normal deterministic modules**: white or very light gray fills with dark slate borders.
- **Primary execution path**: one saturated accent color, used mainly for arrows and one
  small set of high-priority labels.
- **Novel output / evidence / provenance**: a distinct pale fill, often mint or soft blue,
  so the innovation has its own visual identity.
- **Optional / external / uncertain**: light gray fill, dashed outlines, lower contrast.
- **Warnings / failures / blockers**: muted amber or coral/red only where semantically needed.

### Color Rules

- Avoid large pure-black filled boxes. Black is too heavy for most SCI-style main figures.
- Use dark fill only for the single central engine/orchestrator, if a dark anchor is needed.
- Keep most nodes light; let hierarchy come from grouping, line weight, and arrows.
- Do not use one-note palettes dominated by variations of one hue.
- Max 4 semantic colors per figure, plus neutral grays.
- Every color must have a role. Do not add color for decoration.
- The figure must remain understandable in grayscale.

---

## TYPOGRAPHY SYSTEM

### Hierarchy
```
POSTER TITLE     → 28–36px, weight 800, #111111
SECTION HEADER   → 11px, weight 700, #111111, UPPERCASE, letter-spacing 0.12em
KEY NUMBER       → 48–64px, weight 800, text-primary or selected accent
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
- Section dividers: 1px neutral border from the selected palette
- Card borders: 1px neutral border with `border-radius: 3px`
- Flow arrows: 1.5px neutral; highlighted path uses the selected main-path accent
- No heavy borders or drop shadows (max: `box-shadow: 0 1px 4px rgba(0,0,0,0.06)`)
- Dashed lines: for optional/conditional paths, uncertainty

---

## DIAGRAM LANGUAGE

### Node Types
| Element | Style |
|---------|-------|
| Central Orchestrator | Rounded rect, selected dark slate fill, white text; use once |
| Process / Module | Rounded rect, white/light fill, dark slate border |
| Data / Storage | Slightly rounded rect, pale neutral or novelty fill |
| Input / Output | Labeled rect or parallelogram with selected main-path accent |
| Decision | Diamond or rounded rect with `?` marker |
| Highlight / Key | Pale accent fill with dark text, not saturated fill unless tiny |
| External System | Dashed border, light neutral fill |
| Loop / Feedback | Circular arrow or return path, dashed selected accent |

### Edge Types
| Connection | Style |
|-----------|-------|
| Primary data flow | Solid arrow, 1.5px, dark neutral |
| Key / highlighted path | Solid arrow, 2px, selected main-path accent |
| Feedback / return | Dashed arrow, 1.5px, selected accent |
| Conditional | Dashed arrow, 1px, neutral gray |
| Error path | Solid arrow, 1.5px, muted red/coral |

### Diagram Quality Rules

- Prefer stage/lane grouping over drawing 20 isolated modules.
- Keep labels inside nodes to 1–3 words; move details to side annotations.
- Route arrows with minimal crossings. If crossings are unavoidable, use grouping or
  a two-level diagram.
- Align nodes to a grid. Mixed alignment makes technical diagrams look unfinished.
- Use one highlighted path per diagram unless the content genuinely has multiple modes.
- Give the novelty/output artifact a separate pale semantic fill so it does not look like
  a generic endpoint.

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
- Bar charts: primary color = selected main-path accent; comparison = slate/neutral;
  evidence/provenance = selected novelty color.

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
- Background: selected palette background, usually white or very light warm gray
- All content within consistent margins

---

## VISUAL QA BEFORE DELIVERY

Before final output:
- Confirm the figure plan has one clear visual focal point.
- Confirm no text overlaps, clips, or becomes unreadable.
- Confirm every stat or chart value is sourced or labeled as assumption/unknown.
- Confirm the footer states sources, confidence, or assumptions.
- Confirm the page still looks premium in grayscale: hierarchy should not depend only on cyan.
