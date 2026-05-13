# Router: Intent Parser

Use only when `SKILL.md` routing is ambiguous.

## Scoring

```text
score[type] = strong_signals * 2 + moderate_signals

if >=2 types score >= 2 -> HYBRID
else if one type scores >= 2 -> that type
else if original design ask with no source -> DESIGN_REQUEST
else ask one concise question or skip this skill
```

`visual-plan` triggers only when the user wants a visual artifact, figure plan, or prompt.
If a strong figure-purpose signal appears, route by purpose before source type.

## Signals

### SCIENTIFIC_MAIN_FIGURE

Strong: "Figure 1", "main figure", Nature/Science/Cell/SCI style, "机制图",
"机制路线", "算法框架图", "algorithm framework", "graphical abstract", or a request
to summarize full material into a paper-ready mechanism/algorithm figure prompt.

Moderate: asks for concept mechanism plus implementation detail, first-glance/close-reading
layers, publication figure, domain-specific scientific visual elements, or AI drawing
prompt for a manuscript figure.

### CODE_REPO

Strong: repo/project path, manifests (`package.json`, `pyproject.toml`, `Cargo.toml`,
`go.mod`, etc.), source tree, source syntax, or "repo/codebase/source project".

Moderate: modules, functions, APIs, services, controllers, packages, build files, or
"architecture from implementation".

### RESEARCH_PAPER

Strong: PDF, paper sections, figures/tables/appendix, DOI/arXiv, venue names, "we
propose/evaluate", or "paper/论文/publication".

Moderate: notation, proofs, benchmark tables, ablations, baselines, metrics, datasets.

### DIAGRAM_IMAGE

Strong: uploaded/linked image/SVG/screenshot with boxes, arrows, nodes, swimlanes, model
blocks, or "this diagram/flowchart/architecture image".

Moderate: text describing what an image shows; whiteboard/slide/paper-figure screenshot.

### ALGO_TEXT

Strong: numbered steps, pseudocode, formulas plus process text, stage logic, or
"algorithm/pipeline/workflow/process".

Moderate: technical bullet spec with first/then/finally; computational process without
source-code syntax.

### DESIGN_REQUEST

Strong: "design/create/sketch/build an architecture for..." with no source material.

Moderate: constraints such as scale, latency, cost, reliability, model type, deployment.

## Ambiguous Cases

- implementation prose without code syntax -> `ALGO_TEXT`
- Figure 1/main figure + paper/code/repo/algo -> `SCIENTIFIC_MAIN_FIGURE`
- paper + code/repo without main-figure intent -> `HYBRID`
- screenshot of paper figure -> `DIAGRAM_IMAGE` for visual transformation,
  `RESEARCH_PAPER` for whole-paper poster
- image + explanatory text -> `HYBRID` when both affect output
- "improve/polish this diagram" -> `DIAGRAM_IMAGE` with refine mode
- "what do you think of this architecture?" -> do not trigger unless a visual rewrite is
  requested

Question template:

```text
Should I treat this as a codebase-to-architecture diagram, or as an algorithm/process visualization?
```
