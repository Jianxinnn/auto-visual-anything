# Renderer: HTML Artifact

**Purpose**: Convert any assembled content block into a rendered HTML artifact
in the FigureFoundry editorial beige style.

Use this renderer only when the user asks for editable HTML/SVG, deterministic labels,
or a local vector artifact. Always read `style/visual_system.md` before executing this
renderer.

---

## RENDERER CONTRACT

Input: A structured content block from any sub-skill, with parameters:
- `mode`: poster / diagram_poster / architecture_draft / architecture_design / two_level
- `layout`: a1_portrait / wide / compact
- `input_type`: research_paper / code_repo / diagram_image / algo_text / hybrid / design_request

Output: A single self-contained HTML file rendered as a chat artifact.
In a local coding environment, save the same self-contained HTML to disk and report the path.

---

## HTML STRUCTURE TEMPLATE

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  /* === RESET & BASE === */
  * { margin: 0; padding: 0; box-sizing: border-box; }

  /* === TOKENS (from visual_system.md) === */
  :root {
    --bg-primary:   #F4F1EC;
    --bg-secondary: #EFEAE4;
    --bg-panel:     #E8E3DC;
    --text-primary: #111111;
    --text-secondary: #4A4A4A;
    --text-annotation: #7A7A7A;
    --text-muted:   #AAAAAA;
    --accent-cyan:  #73C8E0;
    --accent-black: #000000;
    --neutral-gray: #D9D3C7;
    --neutral-dark: #B8B1A6;
    --error-red:    #B91C1C;
    --warning-amber: #D97706;
    --success-green: #2D7A4F;
    --border:       1px solid #D9D3C7;
    --radius:       3px;
    --shadow:       0 1px 4px rgba(0,0,0,0.06);
  }

  /* === LAYOUT === */
  body {
    background: var(--bg-primary);
    font-family: 'Georgia', serif;
    color: var(--text-primary);
    width: 800px;
    max-width: 100%;
    margin: 0 auto;
    padding: 40px 40px 48px;
  }

  /* For A1 portrait: width 800px, height ~1130px minimum */
  .poster { min-height: 1100px; display: flex; flex-direction: column; gap: 0; }

  /* === HEADER === */
  .header {
    display: grid;
    grid-template-columns: 1fr 240px;
    gap: 24px;
    padding-bottom: 20px;
    border-bottom: 1.5px solid var(--text-primary);
    margin-bottom: 24px;
  }
  .header-left .title {
    font-size: 28px; font-weight: 800; line-height: 1.15;
    color: var(--text-primary); font-family: 'Georgia', serif;
    margin-bottom: 6px;
  }
  .header-left .subtitle {
    font-size: 13px; color: var(--text-secondary); margin-bottom: 4px;
  }
  .header-left .authors {
    font-size: 10px; color: var(--text-annotation); letter-spacing: 0.02em;
  }
  .header-right {
    border-left: 2px solid var(--accent-cyan);
    padding-left: 14px;
  }
  .header-right .question-label {
    font-size: 9px; font-weight: 700; letter-spacing: 0.14em;
    color: var(--text-annotation); text-transform: uppercase; margin-bottom: 4px;
  }
  .header-right .question {
    font-size: 11px; color: var(--text-secondary); margin-bottom: 10px; line-height: 1.4;
  }
  .header-right .answer-label {
    font-size: 9px; font-weight: 700; letter-spacing: 0.14em;
    color: var(--accent-cyan); text-transform: uppercase; margin-bottom: 4px;
  }
  .header-right .answer {
    font-size: 12px; font-weight: 700; color: var(--text-primary); line-height: 1.35;
  }

  /* === SECTION === */
  .section {
    margin-bottom: 24px;
    padding-bottom: 24px;
    border-bottom: 1px solid var(--neutral-gray);
  }
  .section:last-child { border-bottom: none; }
  .section-header {
    font-size: 9px; font-weight: 700; letter-spacing: 0.14em;
    text-transform: uppercase; color: var(--text-primary);
    margin-bottom: 12px;
    display: flex; align-items: center; gap: 8px;
  }
  .section-header::after {
    content: ''; flex: 1; height: 1px; background: var(--neutral-gray);
  }

  /* === 2-COLUMN GRID === */
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; }
  .grid-1-2 { display: grid; grid-template-columns: 1fr 2fr; gap: 16px; }
  .grid-2-1 { display: grid; grid-template-columns: 2fr 1fr; gap: 16px; }

  /* === STAT BLOCK === */
  .stat-block {
    background: var(--bg-panel);
    border-radius: var(--radius);
    padding: 16px;
    border: var(--border);
  }
  .stat-number {
    font-size: 52px; font-weight: 800; line-height: 1;
    color: var(--text-primary); margin-bottom: 4px;
  }
  .stat-number.cyan { color: var(--accent-cyan); }
  .stat-label {
    font-size: 10px; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: var(--text-secondary); margin-bottom: 2px;
  }
  .stat-context { font-size: 10px; color: var(--text-annotation); }

  /* === DIAGRAM CANVAS === */
  .diagram-container {
    background: var(--bg-secondary);
    border: var(--border);
    border-radius: var(--radius);
    padding: 20px;
    overflow: visible;
  }
  .diagram-container svg { width: 100%; height: auto; }
  .diagram-caption {
    margin-top: 8px;
    font-size: 9px;
    color: var(--text-annotation);
    line-height: 1.35;
  }

  /* === DIAGRAM SVG ELEMENTS (inline styles for SVG) === */
  /* Use these classes in inline SVG */
  .node-primary    { fill: #111111; stroke: none; rx: 4; }
  .node-secondary  { fill: #F4F1EC; stroke: #D9D3C7; stroke-width: 1; rx: 4; }
  .node-highlight  { fill: #73C8E0; stroke: none; rx: 4; }
  .node-external   { fill: #F4F1EC; stroke: #B8B1A6; stroke-width: 1; stroke-dasharray: 4,2; rx: 4; }
  .node-data       { fill: #D9D3C7; stroke: none; rx: 3; }
  .edge-primary    { stroke: #4A4A4A; stroke-width: 1.5; fill: none; }
  .edge-highlight  { stroke: #73C8E0; stroke-width: 2; fill: none; }
  .edge-feedback   { stroke: #73C8E0; stroke-width: 1.5; stroke-dasharray: 5,3; fill: none; }
  .edge-error      { stroke: #B91C1C; stroke-width: 1.5; fill: none; }
  .text-node-dark  { fill: white; font-size: 11px; font-weight: 600; text-anchor: middle; }
  .text-node-light { fill: #111111; font-size: 11px; font-weight: 600; text-anchor: middle; }
  .text-edge-label { fill: #7A7A7A; font-size: 9px; text-anchor: middle; }
  .text-group-label { fill: #7A7A7A; font-size: 9px; font-weight: 700;
                      letter-spacing: 0.1em; text-transform: uppercase; }

  /* === CHART CONTAINER === */
  .chart-container {
    background: var(--bg-panel);
    border: var(--border);
    border-radius: var(--radius);
    padding: 14px 16px;
  }
  .chart-title {
    font-size: 9px; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: var(--text-secondary); margin-bottom: 10px;
  }

  /* === HORIZONTAL BAR CHART (CSS) === */
  .bar-chart { display: flex; flex-direction: column; gap: 6px; }
  .bar-row { display: flex; align-items: center; gap: 8px; }
  .bar-label { font-size: 10px; color: var(--text-secondary); width: 120px;
               text-align: right; flex-shrink: 0; }
  .bar-track { flex: 1; height: 14px; background: var(--bg-primary);
               border-radius: 2px; overflow: hidden; position: relative; }
  .bar-fill { height: 100%; border-radius: 2px; transition: width 0.3s; }
  .bar-fill.primary { background: var(--accent-cyan); }
  .bar-fill.secondary { background: var(--text-primary); }
  .bar-fill.neutral { background: var(--neutral-dark); }
  .bar-fill.error { background: var(--error-red); }
  .bar-value { font-size: 10px; font-weight: 600; color: var(--text-primary);
               width: 40px; flex-shrink: 0; }

  /* === BULLET LIST === */
  .bullet-list { list-style: none; display: flex; flex-direction: column; gap: 6px; }
  .bullet-list li {
    display: flex; gap: 8px; align-items: flex-start;
    font-size: 11px; color: var(--text-secondary); line-height: 1.4;
  }
  .bullet-list li::before {
    content: '—'; color: var(--accent-cyan); font-weight: 700;
    flex-shrink: 0; margin-top: 0;
  }

  /* === TAG / PILL === */
  .tag {
    display: inline-block; padding: 2px 7px;
    background: var(--bg-panel); border: var(--border);
    border-radius: 2px; font-size: 9px; font-weight: 600;
    letter-spacing: 0.06em; color: var(--text-secondary);
  }
  .tag.cyan { background: var(--accent-cyan); color: white; border-color: var(--accent-cyan); }
  .tag.dark { background: var(--text-primary); color: white; border-color: var(--text-primary); }

  /* === PANEL / CARD === */
  .panel {
    background: var(--bg-panel);
    border: var(--border);
    border-radius: var(--radius);
    padding: 14px 16px;
    box-shadow: var(--shadow);
  }
  .panel-title {
    font-size: 9px; font-weight: 700; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--text-annotation); margin-bottom: 8px;
  }

  /* === CALLOUT === */
  .callout {
    border-left: 3px solid var(--accent-cyan);
    padding: 10px 14px;
    background: var(--bg-secondary);
    border-radius: 0 var(--radius) var(--radius) 0;
  }
  .callout.black { border-left-color: var(--text-primary); }
  .callout.red { border-left-color: var(--error-red); }
  .callout-title { font-size: 9px; font-weight: 700; letter-spacing: 0.1em;
                   text-transform: uppercase; color: var(--text-annotation); margin-bottom: 4px; }
  .callout-body { font-size: 11px; color: var(--text-secondary); line-height: 1.4; }

  /* === FOOTER === */
  .footer {
    margin-top: 24px;
    padding-top: 12px;
    border-top: 1px solid var(--neutral-gray);
    display: flex; justify-content: space-between; align-items: flex-end;
  }
  .footer-citation { font-size: 9px; color: var(--text-annotation); max-width: 500px; line-height: 1.4; }
  .footer-sources { font-size: 8px; color: var(--text-annotation); max-width: 520px; line-height: 1.35; }
  .footer-badge {
    font-size: 8px; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: var(--text-annotation);
    border: 1px solid var(--neutral-gray); padding: 3px 7px; border-radius: 2px;
  }

  @media (max-width: 820px) {
    body { width: 100%; padding: 24px 18px 32px; }
    .header { grid-template-columns: 1fr; gap: 16px; }
    .header-right { border-left: 0; border-top: 2px solid var(--accent-cyan); padding-left: 0; padding-top: 12px; }
    .grid-2, .grid-3, .grid-1-2, .grid-2-1 { grid-template-columns: 1fr; }
    .stat-number { font-size: 44px; }
    .bar-label { width: 96px; }
  }
</style>
</head>
<body>
<div class="poster">
  <!-- Content injected here based on sub-skill output -->
</div>
</body>
</html>
```

---

## RENDERING RULES

### Rule 1: Always Self-Contained
All CSS, fonts, and SVG must be inline. No external dependencies.
Do not use Google Fonts, remote images, remote scripts, Chart.js, D3, or CDN assets.

### Rule 2: Diagrams as Inline SVG
Never use canvas or third-party charting libraries for diagrams.
Draw all architecture diagrams as hand-crafted inline SVG using the node/edge classes above.
Every SVG with arrows must define arrowhead markers in `<defs>` and use `marker-end`.

### Rule 3: Charts as CSS + SVG Hybrid
- Horizontal bar charts: use the `.bar-chart` CSS classes
- Line charts / complex charts: use inline SVG with `<path>` and `<line>` elements
- Never use Chart.js or D3 (too heavy, not needed)

### Rule 4: Proportional Layout
- A1 portrait: 800px wide × minimum 1100px tall
- Use CSS Grid for multi-column layouts
- Never use absolute positioning for main layout (only for diagram elements)
- For complex content, increase height naturally instead of shrinking the whole poster.

### Rule 5: No Lorem Ipsum
Every text element must contain real content from the analysis.
Never use placeholder text.

### Rule 6: Direct Labeling
- All chart bars must have value labels
- All diagram nodes must have text labels
- No legends — use inline labels instead
- Add a short `.diagram-caption` when it helps explain source coverage, confidence, or assumptions.

### Rule 7: Progressive Disclosure
For complex diagrams, add subtle hover states:
```css
.node:hover rect { opacity: 0.85; cursor: pointer; }
.node:hover .tooltip { display: block; }
```

---

## CONTENT INJECTION GUIDE

### For `mode: poster` (research paper)
Structure: Header → Overview → Core Insight (stat + mini-diagram) →
Mechanism (full diagram) → Results (charts) → Supporting Insights → Takeaways → Footer

### For `mode: diagram_poster` (code repo)
Structure: Header → System Stats → System Overview Diagram →
Module Detail Diagram → Tech Stack Chart → Architecture Findings → Footer
Footer must include key source paths and confidence.

### For `mode: architecture_draft` (diagram image or algo text)
Structure: Header → Core Idea → Mechanism Diagram →
Design Decisions → Extension Points → Footer

### For `mode: architecture_design` (from scratch)
Structure: Header → Design Goals → Architecture Diagram →
Data Flow Description → Design Rationale → Extension Roadmap → Footer
Footer must identify assumptions because no source artifact exists.

---

## QUALITY CHECKLIST

Before outputting the HTML artifact, verify:

- [ ] Background is `#F4F1EC` (not white)
- [ ] Section headers are UPPERCASE with letter-spacing
- [ ] At least one dominant stat number (48px+) is present
- [ ] Diagram is drawn as inline SVG (not described, not placeholder)
- [ ] All node labels are concise (≤ 3 words)
- [ ] Arrows have direction markers (arrowheads)
- [ ] Charts have direct value labels (no legend)
- [ ] Max 3 colors in any chart
- [ ] Footer has citation / source
- [ ] Unknowns, assumptions, or confidence are visible when relevant
- [ ] No paragraphs — only labels, bullets, callouts
- [ ] Total height ≥ 1100px (A1 portrait proportions)
- [ ] Mobile/narrow layout does not overlap text or diagrams
