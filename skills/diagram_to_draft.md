# Sub-Skill: Diagram Image → Figure Prompt or Redesign Plan

**Trigger**: Input is an image of an architecture diagram, flowchart, system map,
ML pipeline figure, or any visual algorithm representation.

**Output**: A figure redesign/transposition plan in the same structural style. Compile it
into an optimized image prompt package by default, or an editable HTML/SVG artifact when
requested. Not a copy — a genuine new design unless the user requested refinement.

Read `style/visual_system.md` before executing this skill.
After analysis, pass output to the selected renderer: `renderers/image_prompt.md` by default,
or `renderers/html_artifact.md` for deterministic vector output.

Truth rule: separate what is visible in the image from what you infer. If labels or
connections are unreadable, mark them as `unreadable` and ask for a clearer image only
when the missing detail would materially change the output.

---

## PHASE 1 — STYLE FINGERPRINT EXTRACTION

Analyze the image deeply. Extract the structural DNA, not just the surface appearance.

### 1.0 Image Readability

```
IMAGE QUALITY:
  Readable labels: [yes / partial / no]
  Visible flow direction: [yes / partial / no]
  Visible grouping/layers: [yes / partial / no]
  Ambiguous areas: [list]
```

Use visible structure as evidence. Do not invent hidden labels or off-canvas components.

### 1.1 Flow Pattern (pick dominant)

```
Sequential / Pipeline          → linear left-to-right or top-to-bottom
Hierarchical / Layered         → abstraction levels stacked
Modular / Component-based      → discrete blocks with clear interfaces
Multi-agent / Graph            → nodes connected in non-linear topology
Iterative / Loop               → cycle or recursive structure
Feedback / Closed-loop         → output feeds back to input
Branching / Decision           → conditional paths splitting
Parallel / Distributed         → multiple simultaneous paths
Encode–Transform–Decode        → compression and reconstruction
Query–Retrieve–Generate        → RAG-style flow
```

### 1.2 Visual Language

Extract the visual grammar:

```
Box style:         [rounded / sharp / with icon / labeled only]
Edge style:        [solid / dashed / labeled / unlabeled / directional]
Grouping method:   [bounding box / background color / swimlane / none]
Layout direction:  [L→R / T→B / circular / radial / grid]
Label style:       [inside node / below node / on edge]
Abstraction depth: [1 level / 2 levels / 3+ levels]
Color logic:       [semantic / aesthetic / layer-based / none]
Special markers:   [loops / decision points / data annotations / size/count labels]
```

### 1.3 Component Taxonomy

List all node TYPES observed (not individual nodes):

Example output:
```
Node types found:
  - Input source (parallelogram shape, labeled with data type)
  - Processing module (rounded rectangle, dark fill)
  - Memory / state store (cylinder or rounded rectangle with double border)
  - Output sink (labeled rectangle, highlighted)
  - Decision point (diamond or branching node)
  - External system (dashed border)
  - Subcomponent (smaller box nested or attached)

Edge types found:
  - Primary data flow (solid arrow)
  - Optional / conditional path (dashed arrow)
  - Feedback loop (curved arrow returning upstream)
  - Bidirectional (double-headed arrow)
```

### 1.4 Naming Convention

```
Mathematical:    uses Σ, θ, x_t, h_i notation
Engineering:     uses module names like "TokenEncoder", "RouteDispatcher"
Descriptive:     uses natural language "User Input", "Process Query"
Mixed:           combination
Abbreviated:     short codes like "MHA", "FFN", "KV"
```

### 1.5 Design Principles Inferred

```
What does this architecture prioritize?
  □ Throughput / speed
  □ Modularity / replaceability
  □ Accuracy / correctness
  □ Scalability
  □ Interpretability
  □ Flexibility / generality

How is complexity managed?
  □ Clear abstraction boundaries
  □ Hierarchical decomposition
  □ Parallel processing
  □ State separation
  □ Role specialization
```

---

## PHASE 2 — NEW ARCHITECTURE GENERATION

First determine mode:

```
IF user asks to improve/polish/redesign the same diagram
  → mode: refine_existing
ELSE
  → mode: transpose_to_new_architecture
```

For `transpose_to_new_architecture`, generate a genuinely NEW architecture that:
1. Follows the EXACT same flow pattern
2. Uses the EXACT same visual language
3. Applies the EXACT same abstraction level
4. Follows the EXACT same naming convention
5. Addresses a DIFFERENT problem domain or variant

For `refine_existing`, preserve the original domain and semantics. Improve hierarchy,
alignment, labeling, visual emphasis, and information density without changing meaning.

### 2.1 Domain Transposition

If no specific domain is requested, apply this default mapping:

| Original Domain | New Domain |
|----------------|-----------|
| Image classification | Text classification |
| Text generation | Code generation |
| Recommendation system | Anomaly detection |
| Data pipeline (batch) | Data pipeline (streaming) |
| Single-agent RL | Multi-agent RL |
| Centralized training | Federated learning |
| Encoder-decoder (translation) | Encoder-decoder (summarization) |
| Search / retrieval | Reasoning / chain-of-thought |

If the user specifies a target domain, use that instead.

### 2.2 Component Mapping

For each component in the original, create a new component:

```
Original component → New component (same structural role, new purpose)

Example:
  Image Encoder → Document Encoder
  Patch Embedding → Sentence Embedding
  Attention Layer → Cross-attention Layer
  Classification Head → Extraction Head
```

### 2.3 Architecture Spec

Produce the complete new architecture:

```
NEW ARCHITECTURE NAME: [name]
DOMAIN: [what problem it solves]
CORE MECHANISM: [1–2 sentence explanation]

COMPONENTS:
  [Component Name]
    Role: [structural role in the flow]
    Input: [data type / format]
    Output: [data type / format]
    Internal Logic: [brief description]
    Connected to: [list of downstream components]

FLOW DESCRIPTION:
  [numbered steps following same pattern as original]

DIAGRAM SPEC:
  Nodes: [complete list with types matching original's visual language]
  Edges: [complete list with directions and labels]
  Groupings: [layers/stages matching original's grouping method]
  Layout: [matching original's layout direction]
  Special markers: [loops, decisions, etc. — same markers as original]
```

### 2.4 Key Design Decisions

```
Decision 1: [what was chosen]
  Rationale: [why, in terms of this architecture's goals]
  Trade-off: [what was sacrificed]

Decision 2: [...]
Decision 3: [...]
```

### 2.5 Extension Points

```
Swap point 1: [which component can be replaced and with what]
Scale point: [where parallelism or distribution can be added]
Enhancement: [what a V2 version would add]
```

---

## PHASE 3 — NARRATIVE STRUCTURE

Frame the new architecture as an editorial story:

```
THE PROBLEM:   [what problem this solves, why it's hard]
THE APPROACH:  [the structural strategy — 1 sentence]
THE MECHANISM: [how data flows through the system]
THE NOVELTY:   [what makes this design interesting]
THE RESULT:    [what this enables that wasn't possible before]
```

---

## PHASE 4 — CONTENT ASSEMBLY

```
ARCHITECTURE NAME: [name]
SUBTITLE: [1-line description]
PROBLEM DOMAIN: [field/application]

THE QUESTION: [what problem does this solve?]
THE ANSWER: [direct bold answer — what this architecture does]

FLOW PATTERN: [from original — e.g., "Hierarchical Multi-stage Pipeline"]
VISUAL LANGUAGE: [from original — e.g., "Swimlane with labeled edges, L→R"]
MODE: [refine_existing / transpose_to_new_architecture]
IMAGE EVIDENCE: [what was directly visible]
INFERENCES: [what was inferred, if any]

DIAGRAM SPEC: [full spec from Phase 2.3]

DESIGN DECISIONS: [from Phase 2.4]
EXTENSION POINTS: [from Phase 2.5]

NARRATIVE: [full story from Phase 3]
```

---

## PHASE 5 — COMPILE FIGURE OUTPUT

Pass assembled content to the selected renderer with:
- `mode: architecture_draft`
- `layout: a1_portrait`
- `input_type: diagram_image`

For `renderers/image_prompt.md`, produce:
- Copy-ready prompt preserving the diagram's visible structural style
- Explicit `refine_existing` or `transpose_to_new_architecture` instruction
- Label priority list based on readable source labels
- Negative prompt for avoiding semantic drift from the input diagram
- Post-edit notes for unreadable labels and exact text replacement

For `renderers/html_artifact.md`, produce:
- Side-by-side comparison: [ORIGINAL STYLE] vs [NEW ARCHITECTURE]
- OR single new diagram if no comparison is needed
- Design decisions panel
- Extension points callout
