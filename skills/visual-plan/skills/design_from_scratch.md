# Sub-Skill: Design From Scratch → Figure Prompt

**Trigger**: User requests a new system/algorithm design with no reference input.
e.g., "Design me a recommendation system", "Create an architecture for X", "How would you build Y?"

**Output**: Complete original architecture figure plan in the visual-plan editorial
style, passed to the renderer selected by the router (`renderers/image_prompt.md` by
default).

**Domain truth rule**: because there is no reference input, all unstated scale, latency,
data, and deployment choices are design assumptions. Make the architecture opinionated,
but label assumptions clearly and avoid pretending they came from the user. The footer
must state "design assumptions" explicitly. Full evidence rules and the rationalization
table live in `style/evidence_discipline.md`.

**Source-style default**: a from-scratch design figure has three things a real-source
figure does not — an explicit **design-assumptions panel**, a **decision-rationale
panel**, and a **V1 → V2 → V3 extension roadmap**. Footer must read "design
assumptions" so readers do not mistake an opinion for an analyzed fact. Composition is
opinionated but never decorative. If the user named a domain (recommendation system,
trading platform, lab automation, robotics), consult `style/domain_hints.md` for the
field's primitives and avoid-list before compiling.

---

## PHASE 1 — REQUIREMENT EXTRACTION

### 1.1 Parse the Request

Extract from the user's message:

```
DOMAIN:       [what field / application area]
GOAL:         [what the system must accomplish]
CONSTRAINTS:  [any mentioned: scale, latency, accuracy, cost, etc.]
STYLE HINT:   [any mentioned: "like BERT", "transformer-based", "microservice", etc.]
NOVELTY:      [should this be standard best practice OR explore a creative approach?]
```

### 1.2 Clarify Ambiguity (if needed)

If the request is too vague to design confidently, ask ONE clarifying question:

> "Just to confirm — are you looking for [interpretation A] or [interpretation B]?"

If clear enough, proceed immediately without asking.
Ask only if the missing detail changes the architecture class, not merely an implementation
choice. For example, ask when "recommendation system" could mean consumer-scale online
serving or an offline analytics prototype; do not ask about minor framework preferences.

### 1.3 Design Goals

State the 3 primary design goals you'll optimize for:

```
GOAL 1: [e.g., scalability — must handle 10M requests/day]
GOAL 2: [e.g., accuracy — minimize false positives]
GOAL 3: [e.g., modularity — components must be independently replaceable]
```

Also state:

```
ASSUMPTIONS:
  Scale: [...]
  Latency: [...]
  Data sensitivity: [...]
  Deployment context: [...]
```

---

## PHASE 2 — ARCHITECTURE DESIGN

### 2.1 Pattern Selection

Choose the most appropriate architectural pattern for the domain:

```
Recommendation System  → Retrieval + Ranking + Personalization pipeline
NLP Processing        → Encoder + Attention + Task head
Data Pipeline         → Ingest + Transform + Serve (Lambda / Kappa)
ML Training System    → Data loader + Trainer + Evaluator + Registry
Agent System          → Perception + Memory + Reasoning + Action loop
API Service           → Gateway + Router + Service + Cache + DB
Real-time System      → Event stream + Processor + Sink + Monitor
Search Engine         → Crawler + Indexer + Retriever + Ranker
```

### 2.2 Component Design

Design each component with:

```
[Component Name]
  Purpose:      [what this component does]
  Interface:    [inputs and outputs]
  Technology:   [suggested implementation approach]
  Scale:        [single instance / shardable / stateless / stateful]
  Failure mode: [what breaks if this fails, how to recover]
```

### 2.3 Data Flow Design

Specify the complete data journey:

```
ENTRY POINT:   [where data / requests enter]
STAGE 1:       [first transformation]
STAGE 2:       [second transformation]
...
STORAGE:       [what is persisted, where, why]
EXIT POINT:    [where results are returned / published]
FEEDBACK LOOP: [does output influence future inputs? how?]
```

### 2.4 Architecture Diagram Spec

```
FLOW PATTERN: [dominant pattern]
LAYOUT:       [L→R / T→B / circular]

NODES:
  [complete list with types and roles]

EDGES:
  [complete list with directions and data labels]

GROUPINGS:
  [stages / layers / service boundaries]

HIGHLIGHTED PATH:
  [the most critical / novel path — selected main-path accent]

SECONDARY PATHS:
  [normal operational paths — neutral gray/slate]

SPECIAL ELEMENTS:
  [loops, decisions, feedback arrows]
```

---

## PHASE 3 — DESIGN RATIONALE

### 3.1 Key Decisions (3–5)

```
DECISION: [specific architectural choice]
  WHY:       [rationale linked to design goals]
  TRADE-OFF: [what this costs / alternative considered]
  IMPACT:    [what this enables]
```

### 3.2 Alternative Approaches Considered

```
ALTERNATIVE 1: [simpler/different approach]
  Why not chosen: [1 sentence]

ALTERNATIVE 2: [...]
  Why not chosen: [1 sentence]
```

### 3.3 Extension Roadmap

```
V1 (MVP):    [minimal viable version of this architecture]
V2:          [first major extension or optimization]
V3:          [scaled/advanced version]
```

---

## PHASE 4 — NARRATIVE CONSTRUCTION

```
THE PROBLEM:
  [Why is this hard? What existing approaches fail?]

THE STRATEGY:
  [The overall architectural philosophy in 1–2 sentences]

THE FLOW:
  [Step-by-step narrative of how data moves through the system]

THE BETS:
  [The 2–3 key design bets that make or break this architecture]

THE UPSIDE:
  [What this enables that a naive implementation wouldn't]
```

---

## PHASE 5 — CONTENT ASSEMBLY

```
SYSTEM NAME: [name]
SUBTITLE: [domain + purpose]

THE QUESTION: [what problem this solves]
THE ANSWER: [what this architecture delivers]

DESIGN GOALS: [3 goals from Phase 1.3]
ASSUMPTIONS: [scale, latency, data, deployment assumptions]
PATTERN: [dominant architectural pattern]

DIAGRAM SPEC: [full spec from Phase 2.4]

DATA FLOW: [narrative from Phase 2.3]

DESIGN DECISIONS: [from Phase 3.1]
ALTERNATIVES: [from Phase 3.2]
ROADMAP: [from Phase 3.3]

NARRATIVE: [from Phase 4]
```

---

## PHASE 6 — COMPILE FIGURE OUTPUT

Pass assembled content to the selected renderer with:
- `mode: architecture_design`
- `layout: a1_portrait`
- `input_type: design_request`

For `renderers/image_prompt.md`, produce:
- Copy-ready prompt for the original architecture figure
- Layout and hierarchy specification that makes assumptions visible
- Label priority list for the most important design claims
- Negative prompt for avoiding generic SaaS/cloud/AI diagram cliches
- Post-edit notes for exact constraints the user may later provide

For `renderers/html_artifact.md`, produce:
- Full A1-portrait editorial poster
- Architecture diagram as central visual
- Design rationale sections in editorial grid
- Extension roadmap panel
