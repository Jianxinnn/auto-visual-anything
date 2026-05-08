---
name: figure-foundry
description: >
  FigureFoundry: use when the user wants to turn a source artifact into a publication-quality
  scientific figure plan, optimized image-generation prompt, or optional editable HTML/SVG
  schematic. Trigger for "make a main figure", "generate a prompt for this paper/repo",
  "visualize this system", "draw the architecture", "turn this into a diagram/poster",
  "map this repo", "paper figure prompt", "生图", "绘图 prompt", or any request converting
  a paper, GitHub repo, local codebase, diagram, algorithm, or system description into a
  scientific figure prompt package. Do not trigger for ordinary code review, debugging, or
  text-only architecture discussion unless the user asks for a visual/prompt output.
---

# FigureFoundry — Source → Scientific Figure

Turn technical material (code, paper, diagram, algorithm, or design request) into a
truthful, publication-quality figure spec. Default output: an image-generation prompt
package. Optional output: a self-contained HTML/SVG artifact when the user asks for
deterministic editable vector output.

---

## STEP 1 — CLASSIFY INPUT

Score every strong signal before routing. If two or more types score, route HYBRID;
do not collapse mixed input to the first signal.

| Type | Strong signals | Sub-skill |
|------|----------------|-----------|
| **CODE_REPO** | repo path, manifests (`package.json`, `pyproject.toml`, `Cargo.toml`...), file tree, source syntax (`import`, `class`, `def`) | `skills/repo_analyzer.md` |
| **RESEARCH_PAPER** | PDF, abstract/method/results sections, "Figure 1", DOI/arXiv, "we propose / we evaluate" | `skills/paper_to_poster.md` |
| **DIAGRAM_IMAGE** | image/SVG/screenshot with boxes, arrows, nodes, swimlanes | `skills/diagram_to_draft.md` |
| **ALGO_TEXT** | numbered steps, pseudocode, stage-by-stage prose, no source-code syntax | `skills/algo_to_draft.md` |
| **HYBRID** | ≥ 2 strong types above | `skills/hybrid.md` |
| **DESIGN_REQUEST** | new design ask, no reference material | `skills/design_from_scratch.md` |

If routing is ambiguous after scoring, see `router/intent_parser.md` for the full
signal-scoring rules and ambiguous-case table. If the user does not want a visual
or prompt artifact, do not use this skill.

---

## STEP 2 — TRUTHFULNESS CONTRACT

Every output distinguishes evidence from inference. **Read `style/evidence_discipline.md`
before compiling.** It is the single source for the evidence ledger format, metric
discipline, and the rationalization table.

Quick self-check — STOP if you catch yourself thinking:

- "This number probably exists in the source."
- "Marking unknown looks ugly; let me put a placeholder."
- "User wants polish; rough estimates are fine."
- "This dependency is so common it must be present."
- "The diagram needs symmetry, so I'll add one more module."

Each is a Contract violation. Mark `unknown`, omit the panel, or label as assumption.
Full rationalization table in `style/evidence_discipline.md`.

---

## STEP 3 — SELECT OUTPUT TARGET

```
IF user asks for a prompt, image model, Midjourney, GPT image, Stable Diffusion,
   "生图", "绘图 prompt"
  → image_prompt   (default)

ELSE IF user asks for editable HTML/SVG, deterministic labels, or a local artifact
  → html_artifact

ELSE
  → image_prompt
```

If the user wants both the prompt **and** a directly generated image, see
`router/image_handoff.md` for the two-stage handoff and credential boundary rules.

---

## STEP 4 — EXECUTE

1. Read `style/visual_system.md` (palette and diagram language) and
   `style/evidence_discipline.md` (evidence rules). If the source has a strong domain
   signal (paper venue, repo dependencies, diagram notation, algorithm field), also
   read `style/domain_hints.md` for matching `Favor` primitives and `Avoid` items.
2. Read the sub-skill from STEP 1.
3. Run its phases; produce the structured content block.
4. Read the chosen renderer:
   - `renderers/image_prompt.md` (default)
   - `renderers/html_artifact.md` (deterministic vector output)
5. Compile the final output. The renderer is always the last step; never compile
   before analysis is complete.

State briefly to the user: *"Routing as [TYPE] → compiling [output_target]."*
Ask at most one clarifying question, only if the missing detail would change the
route or output type.

For `image_prompt`, return the full prompt package in chat. For `html_artifact`,
save the file in the current workspace if local filesystem access exists, unless
the user requested a different destination.

---

## Environment Notes

**Chat**: use uploaded PDFs, images, text, or zip contents directly. Do not claim
local filesystem access unless the tool environment provides it.

**Local coding**: use fast file tools (`rg --files`, `rg`, package manifests) to scope
the repo. Skip `node_modules`, `.git`, `dist`, build output, generated files.
