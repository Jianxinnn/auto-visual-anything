# Renderer: HTML Artifact

Use only when the user asks for editable HTML/SVG, deterministic labels, or a local vector
artifact. Read `style/visual_system.md` first.

## Contract

Input: assembled content block plus `mode`, `layout`, and `input_type`.

Output: one self-contained HTML file. In local coding environments, save it to disk and
report the path.

## Minimal Skeleton

Use inline CSS and inline SVG only:

```html
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --bg: #ffffff; --paper: #fafaf7; --panel: #f7fafc;
  --text: #1f2933; --muted: #5b6770; --line: #cbd5dc;
  --core: #24313a; --accent: #2aa7c8; --accent-soft: #e8f4fa;
  --novelty: #dff3ea; --warning: #f2b84b; --error: #d96c5f;
}
body { width: 800px; max-width: 100%; margin: 0 auto; padding: 40px; background: var(--bg); color: var(--text); font-family: Inter, Arial, sans-serif; }
.poster { min-height: 1100px; display: flex; flex-direction: column; gap: 24px; }
.header { display: grid; grid-template-columns: 1fr 240px; gap: 24px; border-bottom: 1.5px solid var(--text); padding-bottom: 18px; }
.title { font-size: 30px; font-weight: 800; line-height: 1.15; }
.kicker, .section-title, .panel-title { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: .12em; color: var(--muted); }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
.panel, .diagram, .chart { background: var(--panel); border: 1px solid var(--line); border-radius: 3px; padding: 14px; }
.stat { font-size: 52px; font-weight: 800; color: var(--accent); line-height: 1; }
.footer { margin-top: auto; border-top: 1px solid var(--line); padding-top: 10px; font-size: 9px; color: var(--muted); }
svg { width: 100%; height: auto; }
.node-core { fill: var(--core); }
.node { fill: #fff; stroke: var(--line); stroke-width: 1; rx: 4; }
.node-novelty { fill: var(--novelty); stroke: #2f8f6b; stroke-width: 1.2; rx: 4; }
.node-external { fill: var(--panel); stroke: #9aa6af; stroke-dasharray: 4 2; rx: 4; }
.edge { stroke: var(--muted); stroke-width: 1.5; fill: none; }
.edge-accent { stroke: var(--accent); stroke-width: 2; fill: none; }
@media (max-width: 820px) { body { padding: 24px 18px; } .header, .grid-2, .grid-3 { grid-template-columns: 1fr; } }
</style>
</head>
<body><main class="poster">...</main></body>
</html>
```

Adapt CSS variables to the selected palette. Keep the artifact self-contained: no remote
fonts, images, scripts, CDN, D3, Chart.js, or canvas.

## Rendering Rules

- Main diagrams are inline SVG with arrowhead markers in `<defs>`.
- Use one `.node-core` at most; use light nodes for normal modules, novelty fill for
  evidence/provenance/output, dashed nodes for external/optional.
- Charts are CSS bars or simple inline SVG; direct labels only, no legends when avoidable.
- No lorem ipsum or placeholder text; every element comes from the analysis.
- No absolute positioning for main layout; use grid/flex and let complex posters grow.
- Use hover/tooltips only as progressive disclosure, not as required reading.

## Mode Layouts

| Mode | Structure |
|---|---|
| `poster` | header → overview → core insight/stat → mechanism → results → takeaways → footer |
| `diagram_poster` | header → system stats → overview diagram → module detail → findings → footer |
| `architecture_draft` | header → core idea → mechanism diagram → decisions → extensions → footer |
| `architecture_design` | header → assumptions/goals → architecture → data flow → rationale/roadmap → footer |

## QA

- palette matches selected profile
- dark fill limited to one anchor
- section headers are uppercase/tracked
- at least one dominant visual or stat exists when supported
- SVG diagrams have labels and arrowheads
- charts use sourced values and direct labels
- footer lists sources, confidence/coverage, unknowns, or design assumptions
- no overlap on narrow layout
