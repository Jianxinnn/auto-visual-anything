# Sub-Skill: Scientific Main Figure -> Mechanism and Algorithm Prompt

Use when the user wants a paper main figure, graphical abstract, Nature/Science/Cell/SCI
style mechanism figure, algorithm framework figure, or Figure 1-style prompt from a
document, code project, paper, algorithm description, or mixed source material.

This is a figure-purpose route. It reuses source analysis; it does not replace it.

## Scope

Best suited for AI algorithms, biology, and AI-biology crossover work such as protein,
nucleic acid, molecular design, omics, structural biology, sequence design, generative
models, graph learning, agents, and model-guided screening.

## Truth Rule

Rich figures are allowed; invented evidence is not. Keep source facts, visual assumptions,
and unknowns separate. Domain objects may illustrate mechanisms only when they match the
source domain or are explicitly labeled as visual assumptions.

## Source Pass

Choose the lightest existing source pass:

- code/project: use `repo_analyzer.md` ingest/extract
- paper/document: use `paper_to_poster.md` source coverage/extract
- algorithm prose or pseudocode: use `algo_to_draft.md` analyze/mapping
- diagram plus text/source: use `diagram_to_draft.md` fingerprint, then `hybrid.md`
- two or more source types: use `hybrid.md` and keep source authority tags

Create the normal evidence ledger before figure design.

## Figure Intent

Extract:

```text
CENTRAL QUESTION:
CENTRAL ANSWER:
CORE MECHANISM:
DOMAIN:
INPUT OBJECTS:
INTERMEDIATE STATES:
OUTPUT OBJECTS:
CORE ALGORITHM STEPS:
VALIDATION OR RESULT EVIDENCE:
UNKNOWNS:
```

Then choose:

| Strategy | Use when |
|---|---|
| `integrated_mechanism` | one mechanism route carries the story |
| `mechanism_plus_framework` | concept mechanism and concrete algorithm both matter |
| `workflow_plus_evidence` | process plus result/validation panels are needed |
| `architecture_first` | implementation modules are the central contribution |
| `domain_process` | biological/chemical/physical transformation is the main story |

Also set:

```text
FIGURE ROLE: overview | mechanism_detail | algorithm_architecture | comparison | validation
VIEWER TAKEAWAY: [one sentence]
MISINTERPRETATION GUARDS:
  Risk:
  Visual prevention:
```

Use guards to prevent likely wrong readings. Examples: anchors are selected nodes, not
batches; branches are lineages, not rounds; static routing is archive-derived, not frozen;
global branch selection is distinct from local residue routing.

## Mechanism vs Algorithm Grammar

Mechanism route:
- purpose: make the central biological/computational mechanism understandable at a glance
- use: domain objects, state changes, physical/functional transformations, magnified
  details, sparse equations
- avoid: blueprint swimlanes, tensor-heavy blocks, generic flowchart modules

Algorithm framework:
- purpose: make implementation, scoring, training/inference, and decision paths inspectable
- use: aligned modules, nested model blocks, tensor/table miniatures, explicit
  inputs/outputs, feedback arrows, concise operation labels
- avoid: decorative molecular scenes, loose icon rows, business flowcharts, empty lanes,
  and unaligned boxes

If both are needed, either create separate prompts or clearly separated panels with shared
numbering/color semantics. Never mix mechanism illustration and algorithm blueprint in one
undifferentiated flow.

## Core Algorithm Mechanism

For the figure's core algorithm, make the operation legible. A beautiful abstract shape is
not enough if the viewer cannot tell what enters, what changes, and what leaves.

Create:

```text
ALGORITHM MECHANISM:
  Input signal:
  Comparison/scoring:
  Intermediate representation:
  Compression/selection:
  Candidate output:
  Feedback/validation:
  Operation labels:
```

Rules:

- Show at least one explicit intermediate object for nontrivial algorithms: response map,
  score field, residue importance profile, ranked list, latent trajectory, or basin map.
- For compression/distillation/selection, show before/after contrast: many noisy signals
  or high-burden candidates enter; a named operation transforms them; sparse motifs or
  selected candidates leave.
- Low text is not zero text. Use short visible operation labels such as `score`,
  `contrast`, `response map`, `compress`, `rank`, `blend`, or `select`.
- Put exact formulas and long identifiers in post-edit notes, but keep enough visible text
  for the core algorithm to be understandable without the caption.
- Do not show a core algorithm only as a funnel, hourglass, glowing line, or abstract flow.

## Composition Discipline

Plan the page before writing the drawing prompt:

```text
LAYOUT PLAN:
  Canvas/grid:
  Visual weight:
  Alignment anchors:
  Whitespace plan:
  Inset rules:
MODULE PURPOSES:
  Panel/stage/module:
    Purpose:
    Viewer learns:
    Required visual:
CONNECTOR AUDIT:
  Keep:
  Remove:
  Replace with grouping/alignment:
```

Rules:

- Use an editorial grid, not free-floating collage placement.
- Unequal panels are fine, but they must align to clear columns, baselines, or panel edges.
- Every zone must answer "why is this here?" in one short phrase.
- Delete or merge modules whose purpose duplicates another module or would not be clear.
- Use `nature_main_figure` density: 12-24 visual elements and 10-18 short labels only when
  grouped into 3-5 clear zones with first-glance and close-reading layers.

## Connector Discipline

Every line or arrow must encode a named relationship: data flow, transformation,
hierarchy, feedback, comparison, or local zoom/callout.

- Remove decorative lines, vague association arrows, and lines used only to fill space.
- Prefer grouping, proximity, alignment, shared color, or labels when a line is not
  essential.
- Keep zooms, callouts, and replicas inside their own panel unless they are the main flow.
- Cross-panel connectors are allowed only for the main reading path or essential feedback.

## Prompt Robustness

Convert design intent into renderable instructions:

```text
VISUAL ARCHETYPE:
  Intended:
  Avoid confusing with:
RENDERABLE GEOMETRY:
  Shape:
  Position:
  Connection:
  Scale:
AI-VISIBLE LABELS:
  Keep:
  Move to post-edit:
```

Rules:

- For ambiguous words such as tree, network, controller, landscape, switchboard, pipeline,
  funnel, or map, say what archetype to use and what common archetype to avoid.
- Replace metaphors with concrete geometry: shape, position, connection, scale, and color.
- Anchor shared layout devices to a baseline, centerline, grid line, or panel boundary.
- Only put short labels meant for image generation in the core prompt. Move exact formulas,
  tensor shapes, thresholds, long mutation names, and dense legends to post-edit notes.

## Domain Primitives

Read `style/domain_hints.md` when domain cues are strong. For scientific main figures,
choose enough precise domain primitives to make the subject specific:

- AI/ML: tensors, latent trajectories, attention maps, graph message passing,
  training/inference loops
- Biology: cells, pathway maps, omics matrices, perturbation arrows, assay panels
- Protein/structure: ribbons, surfaces, binding pockets, ligand sticks, residue highlights,
  sequence-to-structure transitions, conformational changes
- Nucleic acid: secondary structures, base-pair arcs, sequence tracks, guide pairing,
  structure-function transitions
- AI-biology: sequence/structure input, learned representation, generative design path,
  fitness landscape, candidate filtering, validation panel

Avoid cute or generic logos: robots, brain halos, decorative DNA wallpaper, telescope
icons, stock molecule fills, random microscopy textures, glossy app icons, and mascots.

## Content Block

```text
FIGURE TITLE:
AUDIENCE:
FIGURE ROLE:
FIGURE STRATEGY:
DENSITY PROFILE: nature_main_figure

CENTRAL QUESTION:
CENTRAL ANSWER:
CORE MECHANISM:
VIEWER TAKEAWAY:
MISINTERPRETATION GUARDS:
  Risk:
  Visual prevention:

FIRST-GLANCE LAYER:
  Dominant route:
  Main visual object:
  Start state:
  Transformation:
  End state:

CLOSE-READING LAYER:
  Algorithm modules:
  Inputs and outputs:
  Feedback or optimization:
  Validation/evidence panels:
  Source-backed details:

ALGORITHM MECHANISM:
  Input signal:
  Comparison/scoring:
  Intermediate representation:
  Compression/selection:
  Candidate output:
  Feedback/validation:
  Operation labels:

PANEL STRATEGY:
  Panels:
  Reading order:
  Shared color/numbering system:

LAYOUT PLAN:
  Canvas/grid:
  Visual weight:
  Alignment anchors:
  Whitespace plan:
  Inset rules:

PROMPT ROBUSTNESS:
  Visual archetype:
  Renderable geometry:
  Connector audit:
  AI-visible labels:

LABEL HIERARCHY:
  AI-visible operation labels:
  AI-visible state labels:
  Post-edit labels:

SOURCE DISCIPLINE:
  Evidence:
  Visual assumptions:
  Unknowns:
```

## Compile

Pass to the renderer with:

- `mode: scientific_main_figure`
- `layout: 16:9 or 3:2 unless the user asks otherwise`
- `input_type: scientific_main_figure`
- `figure_profile: nature_main_figure`

For image prompts, explicitly state the figure strategy, domain primitives, core algorithm
mechanism, layout plan, connector audit, label hierarchy, and negative prompt.

## Failure Checks

Before final output, reject or revise the prompt if it would likely produce:

- unbalanced regions with arbitrary leftover space
- ambiguous archetypes such as phylogenetic trees instead of search trees, business
  flowcharts instead of algorithm schematics, geographic maps instead of embedding
  landscapes, or literal switchboards instead of abstract decision layers
- a core algorithm shown as decorative abstraction without visible input, operation,
  intermediate state, and output
- overly sparse text that makes the figure elegant but scientifically ambiguous
- decorative connector lines, vague association arrows, or lines used only to fill space
- crowded insets detached from their parent mechanism
- algorithm figures that look like generic flowcharts or slide swimlanes
- mechanism figures that look like engineering pipeline diagrams
- repeated legends, duplicated controls, or decorative panels that do not teach anything
- long formulas, exact mutations, tensor shapes, or assay thresholds embedded as fragile
  generated text instead of post-edit labels
