# Sub-Skill: Diagram Image -> Figure Plan

Use for architecture diagrams, flowcharts, system maps, ML pipeline figures, screenshots,
or visual algorithm representations.

## Truth Rule

Separate visible content from inference. Mark unreadable labels/connections as
`unreadable`; ask for a clearer image only when the missing detail changes the output.

This sub-skill inherits the source image's visual fingerprint unless the user asks for a
new style. Do not force the default `visual-plan` palette over a distinct source style.

## Extract Fingerprint

```text
IMAGE QUALITY:
  readable labels:
  visible flow:
  visible grouping/layers:
  ambiguous areas:

FLOW PATTERN:
  sequential | layered | modular | graph | loop | feedback | branching | parallel |
  encode-decode | query-retrieve-generate

VISUAL LANGUAGE:
  box style:
  edge style:
  grouping method:
  layout direction:
  label style:
  abstraction depth:
  color logic:
  special markers:

TAXONOMY:
  node types:
  edge types:
  naming convention:
```

Use only visible structure as evidence.

## Mode

```text
same-domain improvement -> refine_existing
different target domain -> transpose_to_new_architecture
```

For `refine_existing`, preserve meaning and improve hierarchy, alignment, density, label
priority, and emphasis.

For `transpose_to_new_architecture`, keep the flow pattern, visual language, abstraction
depth, and naming convention while changing the domain/problem.

## Transpose Defaults

If the user provides no target domain:

| Original | New |
|---|---|
| image classification | text classification |
| text generation | code generation |
| recommendation | anomaly detection |
| batch data pipeline | streaming data pipeline |
| single-agent RL | multi-agent RL |
| centralized training | federated learning |
| encoder-decoder translation | encoder-decoder summarization |
| search/retrieval | reasoning pipeline |

## Architecture Spec

For each original component, map to a new component with the same structural role.

```text
ARCHITECTURE NAME:
DOMAIN:
CORE MECHANISM:
MODE:

IMAGE EVIDENCE:
INFERENCES:

COMPONENTS:
  Name:
  Role:
  Input:
  Output:
  Logic:
  Connected to:

FLOW:
DIAGRAM SPEC:
  Nodes:
  Edges:
  Groupings:
  Layout:
  Special markers:

DECISIONS:
EXTENSION POINTS:
NARRATIVE:
```

## Compile

Pass to the renderer with:

- `mode: architecture_draft`
- `layout: a1_portrait`
- `input_type: diagram_image`

For image prompts, explicitly state `refine_existing` or `transpose_to_new_architecture`,
preserve the source visual grammar, and note unreadable labels for post-edit. For HTML,
use side-by-side original-style/new-architecture only when it improves clarity.
