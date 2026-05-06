# Sub-Skill: Algorithm Text → Figure Prompt

**Trigger**: Input is a text description of an algorithm, pseudocode, bullet-point spec,
technical writeup, or any textual representation of a computational process.

**Output**: Algorithm/process figure plan in the FigureFoundry editorial style. Compile it
into an optimized image prompt package by default, or an editable HTML/SVG artifact when
requested.

Read `style/visual_system.md` before executing this skill.
After analysis, pass output to the selected renderer: `renderers/image_prompt.md` by default,
or `renderers/html_artifact.md` for deterministic vector output.

Truth rule: preserve the algorithm's actual semantics. Do not add stages, models,
databases, metrics, or complexity claims unless they are present in the text or are
explicitly labeled as design assumptions.

---

## PHASE 1 — TEXT ANALYSIS

### 1.0 Evidence vs Assumptions

Create this split before designing:

```
EXPLICITLY STATED:
  Inputs: [...]
  Outputs: [...]
  Steps/stages: [...]
  State/loop/decision rules: [...]

ASSUMED FOR VISUALIZATION:
  Data format: [...]
  Scale/latency: [...]
  Component boundaries: [...]

UNKNOWN:
  [important missing details]
```

### 1.1 Identify the Algorithm's Nature

```
COMPUTATION TYPE:
  □ Data transformation (input → transform → output)
  □ Search / optimization (explore → evaluate → select)
  □ Learning / training (iterate → update → converge)
  □ Inference / prediction (encode → reason → decode)
  □ Orchestration / coordination (dispatch → aggregate → respond)
  □ Simulation (initialize → step → observe)
  □ Generation (sample → refine → output)
  □ Retrieval (query → match → rank → return)

ITERATION STRUCTURE:
  □ Single pass (no loops)
  □ Fixed iterations (for loop)
  □ Until convergence (while loop)
  □ Event-driven (reactive)
  □ Recursive
  □ Parallel (map-reduce style)
```

### 1.2 Extract Structural Components

Parse the text and identify:

```
INPUTS:    [list all input variables, data types, sources]
OUTPUTS:   [list all outputs, consumers, destinations]
STAGES:    [identify named phases, steps, or sub-procedures]
STATE:     [any persistent state, memory, or intermediate storage]
DECISIONS: [conditional branches, thresholds, stopping criteria]
LOOPS:     [iteration structures, recursion, convergence checks]
EXTERNAL:  [dependencies on external systems, APIs, data stores]
```

### 1.3 Dominant Structure Classification

Map to the closest architectural pattern:

```
IF (clear sequential steps, one flows into next)
  → PIPELINE

IF (steps repeat until condition met)
  → ITERATIVE_LOOP

IF (multiple sub-problems solved recursively)
  → RECURSIVE / DIVIDE_AND_CONQUER

IF (output of a module connects back to earlier module)
  → FEEDBACK_CLOSED_LOOP

IF (multiple parallel processes merge at a point)
  → PARALLEL_AGGREGATION

IF (system queries external data, processes, generates)
  → RETRIEVAL_AUGMENTED

IF (explicit optimization with gradient or reward signal)
  → OPTIMIZATION_LOOP

IF (encoder compresses, then decoder reconstructs)
  → ENCODE_TRANSFORM_DECODE

IF (multiple specialized agents coordinate)
  → MULTI_AGENT

IF (state machine with transitions)
  → STATE_MACHINE
```

### 1.4 Core Idea Distillation

Extract precisely:

```
WHAT IT DOES:    [1 sentence — what the algorithm accomplishes]
HOW IT WORKS:    [1 sentence — the core mechanism]
WHY IT'S NOVEL:  [what makes this approach interesting or non-obvious]
KEY COMPLEXITY:  [where the hard part is — the bottleneck or innovation]
```

### 1.5 Implicit Assumptions

Surface hidden design decisions in the text:
```
- What data format is assumed?
- What scale is implied (single machine / distributed)?
- What is the latency requirement (batch / streaming / real-time)?
- Is the algorithm deterministic or stochastic?
- Is it stateful or stateless?
If an assumption is necessary for the diagram, label it as an assumption in the final
content block.
```

---

## PHASE 2 — ARCHITECTURE DESIGN

### 2.1 Diagram Type Selection

Match dominant structure to diagram form:

| Structure | Diagram Form |
|-----------|-------------|
| Pipeline | Horizontal boxes with directional arrows, stage labels |
| Iterative Loop | Circular or rectangular loop with iteration counter |
| Recursive | Nested boxes with self-referential arrows |
| Feedback/Closed-loop | Forward path + curved feedback arrow |
| Parallel Aggregation | Multiple parallel columns → merge node |
| Retrieval-Augmented | Query → DB → fetch → process → respond |
| Optimization Loop | Forward pass → loss → backward → update cycle |
| Encode-Transform-Decode | Linear chain with bottleneck node |
| Multi-agent | Network of labeled nodes with communication edges |
| State Machine | States as circles, transitions as labeled arrows |

### 2.2 Component Specification

For each component:

```
[Component Name]
  Shape:       [box / circle / diamond / cylinder / parallelogram]
  Fill:        [dark primary / light neutral / cyan highlight / dashed external]
  Label:       [concise name, ≤3 words]
  Annotation:  [data type or brief description, ≤5 words]
  Role:        [INPUT / PROCESS / DECISION / STATE / OUTPUT / EXTERNAL]
  Size:        [standard / large (important) / small (minor)]
```

### 2.3 Data Flow Specification

For each connection:

```
[Source] → [Target]
  Edge type:   [solid / dashed / bidirectional / feedback]
  Label:       [data being transferred, ≤3 words]
  Color:       [black (normal) / cyan (highlighted) / red (error) / dashed-cyan (feedback)]
```

### 2.4 Layout Construction

Arrange components:

```
LAYOUT DIRECTION: [L→R for pipelines / T→B for hierarchies / circular for loops]

GROUP 1 (Stage/Layer name):
  [component list]

GROUP 2 (Stage/Layer name):
  [component list]

[continue for all groups]

SPECIAL ELEMENTS:
  Loop annotation: [where the loop boundary is]
  Feedback arrow: [from → to, curved path side]
  Decision branch: [condition label on each branch]
```

---

## PHASE 3 — NARRATIVE CONSTRUCTION

Build the editorial narrative in 5 layers:

```
LAYER 1 — HOOK (The Problem)
  [Why does this problem need solving? What breaks without this algorithm?]
  Format: 1 bold statement

LAYER 2 — GAP (What Was Missing)
  [What prior approaches failed to do, or what assumption they got wrong]
  Format: 1–2 bullet labels

LAYER 3 — INSIGHT (The Core Idea)
  [The key conceptual breakthrough or design choice]
  Format: 1 sentence + 1 dominant stat if available

LAYER 4 — MECHANISM (How It Works)
  [Step-by-step description mapped to diagram components]
  Format: numbered flow labels (matches diagram stages)

LAYER 5 — IMPACT (What It Enables)
  [What becomes possible with this algorithm that wasn't before]
  Format: 2–3 bullet labels
```

---

## PHASE 4 — CONTENT ASSEMBLY

```
ALGORITHM NAME: [concise name]
SUBTITLE: [field / application domain]
TYPE: [dominant structure classification]

THE QUESTION: [what problem does this solve?]
THE ANSWER: [direct — what this algorithm does and how]

CORE IDEA: [1–2 sentence distillation]
KEY INSIGHT: [the non-obvious part]

DOMINANT STAT: [if available — key performance number]
  OR
COMPLEXITY NOTE: [time/space complexity if relevant]

DIAGRAM SPEC:
  Type: [from 2.1]
  Nodes: [complete list from 2.2]
  Edges: [complete list from 2.3]
  Layout: [from 2.4]
  Groups: [from 2.4]

NARRATIVE: [all 5 layers from Phase 3]

DESIGN DECISIONS:
  1. [choice + rationale + trade-off]
  2. [choice + rationale + trade-off]
  3. [choice + rationale + trade-off]

EXTENSION POINTS:
  - [what can be swapped / parallelized / enhanced]

SOURCE DISCIPLINE:
  Explicit facts: [derived directly from user text]
  Assumptions: [visualization choices not stated by the user]
  Unknowns: [missing details not shown in the diagram]
```

---

## PHASE 5 — COMPILE FIGURE OUTPUT

Pass assembled content to the selected renderer with:
- `mode: architecture_draft`
- `layout: a1_portrait`
- `input_type: algo_text`

For `renderers/image_prompt.md`, produce:
- Copy-ready prompt for a clean algorithmic framework figure
- Layout specification matching the algorithm's dominant structure
- Label priority list separating exact algorithm terms from optional labels
- Negative prompt for avoiding invented infrastructure or decorative AI motifs
- Post-edit notes for assumptions and exact labels

For `renderers/html_artifact.md`, produce:
- Full A1-portrait editorial poster
- Algorithm diagram as central visual
- Narrative sections in editorial grid
- Design decisions panel
