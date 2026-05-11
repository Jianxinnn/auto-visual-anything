# Sub-Skill: Algorithm Text -> Figure Plan

Use for algorithm descriptions, pseudocode, process specs, or technical writeups.

## Truth Rule

Preserve the text's semantics. Do not add stages, models, databases, metrics, complexity
claims, or external systems unless present or explicitly labeled as assumptions.

## Analyze

Create:

```text
EXPLICIT:
  Inputs:
  Outputs:
  Steps/stages:
  State/loops/decisions:
ASSUMED FOR VISUALIZATION:
  Data format:
  Scale/latency:
  Component boundaries:
UNKNOWN:
```

Classify:

- computation: transformation, search/optimization, learning, inference, orchestration,
  simulation, generation, retrieval
- iteration: single pass, fixed loop, until convergence, event-driven, recursive, parallel
- dominant structure: pipeline, iterative loop, recursive, feedback loop, parallel
  aggregation, retrieval-augmented, optimization loop, encode-transform-decode,
  multi-agent, state machine

## Diagram Mapping

| Structure | Diagram form |
|---|---|
| pipeline | horizontal boxes and arrows |
| iterative/feedback | loop with condition and feedback arrow |
| recursive | nested boxes with self-reference |
| parallel | parallel lanes merging into one node |
| retrieval | query -> store -> fetch -> process -> output |
| optimization | forward -> loss/reward -> update cycle |
| encode/decode | linear chain with bottleneck |
| multi-agent | labeled nodes with communication edges |
| state machine | states and transition labels |

For each component, define name, shape, role, concise label, optional annotation, and
importance. For each edge, define source, target, type, label, and whether it is normal,
highlighted, feedback, conditional, or error.

## Narrative

```text
Problem -> Gap -> Core idea -> Mechanism -> Impact
```

Only use novelty/impact if supported by the user's text; otherwise label as assumption.

## Content Block

```text
ALGORITHM NAME:
SUBTITLE:
TYPE:

THE QUESTION:
THE ANSWER:
CORE IDEA:
KEY INSIGHT:
DOMINANT STAT or COMPLEXITY NOTE:

DIAGRAM SPEC:
  Type:
  Nodes:
  Edges:
  Layout:
  Groups:

NARRATIVE:
DESIGN DECISIONS:
EXTENSION POINTS:

SOURCE DISCIPLINE:
  Explicit facts:
  Assumptions:
  Unknowns:
```

## Compile

Pass to the renderer with:

- `mode: architecture_draft`
- `layout: a1_portrait`
- `input_type: algo_text`

For image prompts, emphasize the actual algorithm terms, decision/loop semantics, and
assumptions. For HTML, draw the algorithm diagram as the central visual.
