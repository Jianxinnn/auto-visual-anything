---
name: visual-plan
description: Use when the user wants a publication-quality figure plan, image-generation prompt package, or editable HTML/SVG schematic from a paper, repo, diagram, algorithm, codebase, or design request. Do not use for ordinary code review, debugging, or text-only architecture discussion unless a visual/prompt artifact is requested.
---

# visual-plan

Source artifact → truthful figure spec. Default output is an image prompt package; HTML/SVG
is only for explicit editable or deterministic-vector requests.

## Route

First score the user's figure intent. If the user asks for a paper main figure,
Nature/Science/Cell-style mechanism figure, graphical abstract, SCI mechanism route, or
algorithm framework figure, route to `SCIENTIFIC_MAIN_FIGURE` before source-type routing.

Then score all strong source signals; if two or more source types score, use `HYBRID`.

| Type | Strong signals | Read |
|---|---|---|
| `SCIENTIFIC_MAIN_FIGURE` | Figure 1/main figure, Nature/Science/Cell/SCI style, mechanism route, algorithm framework, graphical abstract | `skills/scientific_main_figure.md` |
| `CODE_REPO` | repo path, manifests, file tree, source syntax | `skills/repo_analyzer.md` |
| `RESEARCH_PAPER` | PDF, abstract/method/results, DOI/arXiv, paper wording | `skills/paper_to_poster.md` |
| `DIAGRAM_IMAGE` | uploaded image/SVG/screenshot with boxes/arrows/nodes | `skills/diagram_to_draft.md` |
| `ALGO_TEXT` | numbered steps, pseudocode, process prose | `skills/algo_to_draft.md` |
| `HYBRID` | at least two strong source types | `skills/hybrid.md` |
| `DESIGN_REQUEST` | new design ask with no reference material | `skills/design_from_scratch.md` |

If the main table is not enough, read `router/intent_parser.md`. If the user does not
want a visual or prompt artifact, do not use this skill.

## Truth Contract

Before compiling, read `style/evidence_discipline.md`. Every output must separate:

- evidence directly observed in source material
- assumptions made for visualization/design
- unknowns or conflicts

Never invent numbers, modules, baselines, citations, dependencies, or missing diagram
parts. If unsupported, mark `unknown`, omit the panel, or label it as assumption.

## Output Target

| Request | Renderer |
|---|---|
| prompt, GPT image, Midjourney, Stable Diffusion, "生图", unspecified | `renderers/image_prompt.md` |
| editable HTML/SVG, deterministic labels, local vector artifact | `renderers/html_artifact.md` |
| prompt plus generated image | Finish planning first, then read `router/image_handoff.md` |

## Execution

1. Read `style/visual_system.md` and `style/evidence_discipline.md`.
2. If domain cues are strong, read `style/domain_hints.md` for favor/avoid guidance.
3. Read the routed sub-skill and run its phases.
4. Compile with the selected renderer last; never compile before analysis is complete.
5. State briefly: `Routing as <TYPE> -> compiling <renderer>.`

Ask at most one clarifying question, only when missing information changes the route or
output target.

For `image_prompt`, return the full prompt package in chat. For `html_artifact`, save a
self-contained file in the current workspace when filesystem access exists, unless the
user names a different path.

## Local Environment

Use fast scoped inspection: `rg --files`, `rg`, manifests, entry points, and relevant
source files. Skip `.git`, `node_modules`, build outputs, generated files, caches, and
runtime output directories.
