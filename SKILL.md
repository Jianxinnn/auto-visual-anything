---
name: figure-foundry
description: >
  FigureFoundry: use this skill when the user wants to turn a source artifact into a
  publication-quality scientific figure plan, optimized image-generation prompt, or optional
  editable HTML/SVG architecture schematic. Trigger for requests such as "make a main figure",
  "generate a prompt for this paper/repo", "visualize this system", "draw the architecture",
  "turn this into a diagram/poster", "map this repo", "paper figure prompt", or converting a
  paper, GitHub repo, local codebase, diagram, algorithm, or system description into a beautiful
  scientific figure prompt package. Do not trigger for ordinary code review, debugging, or
  text-only architecture discussion unless the user asks for a visual/prompt output.
---

# FigureFoundry Skill — Master Router

FigureFoundry turns technical source material into a truthful, beautiful scientific figure
specification. Its default output is an optimized prompt package the user can paste into an
image-generation tool. If the user asks for an editable deterministic artifact, use the
HTML/SVG renderer instead.

---

## STEP 1 — INPUT DETECTION (MANDATORY FIRST STEP)

Before doing anything else, classify the input by reading it carefully. Collect all
strong signals first; do not stop at the first match.

### Input Type Matrix

| Signal | Detected Type | Route To |
|--------|--------------|----------|
| File tree / directory listing / `import` statements / source code | **CODE_REPO** | `skills/repo_analyzer.md` |
| PDF upload / research paper / academic document | **RESEARCH_PAPER** | `skills/paper_to_poster.md` |
| Image of a diagram / flowchart / architecture screenshot | **DIAGRAM_IMAGE** | `skills/diagram_to_draft.md` |
| Text description of an algorithm / pseudocode / bullet-point spec | **ALGO_TEXT** | `skills/algo_to_draft.md` |
| Mixed: code + description, or repo + paper | **HYBRID** | `skills/hybrid.md` |
| Explicit request for new system design with no reference input | **DESIGN_REQUEST** | `skills/design_from_scratch.md` |

### Detection Rules

```
Set detected_types = []

IF (input contains a local repository path, file tree, package manifest, imports,
    class/function definitions, or source files)
  add CODE_REPO

IF (input is a PDF/research paper, mentions abstract/figures/tables/citations,
    or has academic-paper structure)
  add RESEARCH_PAPER

IF (input is an image/screenshot/SVG containing boxes, arrows, nodes, or a visible
    technical figure)
  add DIAGRAM_IMAGE

IF (input is text describing an algorithm, pseudocode, numbered steps, stages,
    data flow, or computational process without source-code syntax)
  add ALGO_TEXT

IF (user asks for a new architecture/system design and provides no reference material)
  add DESIGN_REQUEST

IF (detected_types contains 2 or more strong types)
  → HYBRID
ELSE IF (detected_types contains 1 type)
  → that type
ELSE IF (user asks for a visual architecture artifact but the source type is unclear)
  → DESIGN_REQUEST
ELSE
  do not use this skill
```

---

## STEP 2 — TRUTHFULNESS CONTRACT

Every output must distinguish evidence from inference.

- Use concrete evidence from files, paper sections, diagram elements, or user-provided text.
- If a number, dependency, module role, or result cannot be verified, mark it as `unknown`
  or omit it. Never invent metrics to fill the visual.
- For local repo work, cite the most important source files in the footer or findings.
- For papers, include citation/source details if available.
- For generated designs with no source material, label assumptions as design assumptions.

---

## STEP 3 — SELECT OUTPUT TARGET

Choose one output target:

```
IF user asks for a prompt, image model, Midjourney, GPT image, Stable Diffusion,
   "生图", "绘图 prompt", or wants to call another image tool themselves
  → OUTPUT_TARGET = image_prompt

ELSE IF user asks for editable vector, HTML, SVG, deterministic labels, or a local artifact
  → OUTPUT_TARGET = html_artifact

ELSE
  → OUTPUT_TARGET = image_prompt
```

Use `image_prompt` as the default because it is the most portable output and matches the
common workflow: analyze source → plan figure → paste optimized prompt into a renderer.
For dense scientific figures with many exact labels, include a post-edit note recommending
that final labels be added in Figma, Illustrator, PowerPoint, or SVG.

---

## STEP 4 — ANNOUNCE AND PROCEED

After classifying, say ONE sentence to the user:

> "I'm reading this as [TYPE] — compiling a [OUTPUT_TARGET] figure package now."

Then read the relevant skill file and execute it. Ask at most one clarifying question only
when the target output would otherwise be materially wrong.

---

## STEP 5 — LOAD SUB-SKILL

Read the appropriate file from `skills/`:

- CODE_REPO → read `skills/repo_analyzer.md`
- RESEARCH_PAPER → read `skills/paper_to_poster.md`
- DIAGRAM_IMAGE → read `skills/diagram_to_draft.md`
- ALGO_TEXT → read `skills/algo_to_draft.md`
- HYBRID → read `skills/hybrid.md`
- DESIGN_REQUEST → read `skills/design_from_scratch.md`

All sub-skills share the same visual system. Read `style/visual_system.md` alongside the
sub-skill, then read the selected renderer only when analysis is complete:

- `renderers/image_prompt.md` for optimized prompt packages
- `renderers/html_artifact.md` for deterministic HTML/SVG artifacts

---

## STEP 6 — COMPILE OUTPUT

All outputs use the renderer specified in `renderers/`. Default: `renderers/image_prompt.md`.

The renderer is always the last step. Never compile a prompt or artifact before analysis is complete.

For `image_prompt`, return the complete prompt package in the chat. For `html_artifact`, save
the artifact as an HTML file in the current workspace when local filesystem access is available,
unless the user requested a different destination.

---

## Environment Notes

**Chat environment**: Use uploaded PDFs, images, text, or zip contents directly. Do not
claim local filesystem access unless the tool environment provides it.

**Local coding environment**: Use fast file tools (`rg --files`, `rg`, package manifests,
language-specific import scanners where available) to inspect repositories before invoking
the sub-skill. Keep analysis scoped to source and configuration files; ignore dependency
directories and generated build output.

---

## Reference Files

| File | Purpose | When to Read |
|------|---------|--------------|
| `router/intent_parser.md` | Extended routing and ambiguity rules | If detection is ambiguous |
| `skills/repo_analyzer.md` | Code repo → architecture diagram | CODE_REPO input |
| `skills/paper_to_poster.md` | Research paper → editorial poster | RESEARCH_PAPER input |
| `skills/diagram_to_draft.md` | Diagram image → new architecture draft | DIAGRAM_IMAGE input |
| `skills/algo_to_draft.md` | Algorithm text → architecture draft | ALGO_TEXT input |
| `skills/hybrid.md` | Mixed input handler | HYBRID input |
| `skills/design_from_scratch.md` | Pure design generation | DESIGN_REQUEST input |
| `style/visual_system.md` | Shared visual design system | Always, before compiling output |
| `renderers/image_prompt.md` | Image prompt package compiler | Default final step |
| `renderers/html_artifact.md` | HTML/SVG artifact renderer spec | If editable/deterministic output requested |
