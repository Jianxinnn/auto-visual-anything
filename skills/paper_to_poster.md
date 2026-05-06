# Sub-Skill: Research Paper → Scientific Figure Prompt

**Trigger**: Input is a PDF, academic paper, or research document.

**Output**: Source-backed scientific figure plan for a graphical abstract, main figure,
or A1-style infographic poster. Compile it into an optimized image prompt package by
default, or an editable HTML/SVG artifact when requested.

Read `style/visual_system.md` before executing this skill.
After analysis, pass output to the selected renderer: `renderers/image_prompt.md` by default,
or `renderers/html_artifact.md` for deterministic vector output.

Truth rule: never invent results, baselines, authors, venues, datasets, or citations.
If a metric is not visible in the provided paper content, use a qualitative insight or
mark the value as `unknown`.

---

## PHASE 1 — CONTENT INTERPRETATION

### 1.0 Source Coverage

First identify what paper content is actually available:

```
SOURCE COVERAGE:
  Title/authors/venue: [found / unknown]
  Abstract/introduction: [found / unknown]
  Method/architecture: [found / unknown]
  Figures/tables: [found / unknown]
  Results/experiments: [found / unknown]
  Limitations/conclusion: [found / unknown]
```

If only a partial paper is available, produce a poster from the available sections and
label missing evidence clearly.

### 1.1 PRIMARY CONTRIBUTION TYPE

Identify what the paper primarily contributes:
- **Algorithm / Method** — novel procedure or technique
- **Model Architecture** — neural network or system design
- **Theoretical Framework** — formal theory or proof
- **Empirical Study** — experiments and findings
- **System / Infrastructure** — deployed system or platform
- **Survey / Meta-analysis** — synthesis of existing work

### 1.2 DOMINANT STRUCTURE

Classify the paper's core structure (pick ONE dominant):

```
Pipeline / Sequential          → horizontal modular blocks
Multi-stage Pipeline           → segmented flow with checkpoints
Hierarchical / Layered         → stacked layers (top-down abstraction)
Modular / Component-based      → separated blocks with interfaces
Multi-agent / Graph            → connected nodes / network graph
Iterative / Loop / Recursive   → circular flow / loops
Feedback-driven / Closed-loop  → loop with feedback arrows
Optimization / Training        → loss curves / trajectories
Comparative / Benchmark        → bar charts / side-by-side
Scaling / Performance Curve    → line charts / trend curves
Generative / Synthesis         → latent → output transformations
Transformation / Encode-Decode → encoder → bottleneck → decoder
Retrieval / Query-driven       → query → database → response
```

### 1.3 CORE IDEA EXTRACTION (CRITICAL)

Extract precisely:
- **The single most important idea** (1–2 sentences, plain language)
- **The mechanism that makes it novel** (what specifically is new)
- **The dominant metric** (the number that proves it works, if present)
- **Baseline comparison** (what it beats, by how much, if present)
- **Evidence location** (section/figure/table/page if available)

### 1.4 KEY DATA EXTRACTION

From figures, tables, and results sections:
- Extract up to 5 quantitative results (numbers with context and source location)
- Identify the 1–2 charts worth reproducing
- Note which results are most surprising or significant
- Extract ablation results if present
- If exact values are not available, do not recreate a chart; use a mechanism diagram
  or labeled takeaway instead

### 1.5 NARRATIVE STRUCTURE

Build the poster's story arc:
```
Hook       → Why does this problem matter?
Gap        → What was missing / broken before?
Insight    → What is the key idea?
Mechanism  → How does it work?
Evidence   → What do the numbers show?
Impact     → What does this enable?
```

---

## PHASE 2 — VISUAL PLAN

### 2.1 DIAGRAM TYPE SELECTION

Match the dominant structure to a diagram form:
- Pipeline → horizontal flow with labeled stage blocks
- Hierarchical → stacked layer diagram (top = abstract, bottom = concrete)
- Multi-agent → node-edge network graph
- Iterative → circular loop with annotations
- Encode-Decode → encoder → bottleneck → decoder with data shapes
- Comparative → grouped bar chart as primary visual

### 2.2 SECTION PLAN

Map content to the 6-section poster layout:

```
SECTION 1 — OVERVIEW
  What is the problem? What is the approach? (2–3 bullet labels)

SECTION 2 — CORE INSIGHT
  Dominant stat (giant number) + 1-sentence explanation
  Supporting mini-diagram

SECTION 3 — SYSTEM / MECHANISM
  Main architecture diagram
  Component labels + data flow arrows

SECTION 4 — RESULTS
  1–2 reproduced charts from paper
  Direct labeled values, no gridlines

SECTION 5 — SUPPORTING INSIGHTS
  Secondary findings, ablations, or comparisons
  Small multiples or grouped bars

SECTION 6 — TAKEAWAYS
  3 bullet labels: what this enables / why it matters
```

### 2.3 VISUAL PRIORITY CHECK

Confirm allocation:
- 40% → Core insight + dominant stat
- 30% → Mechanism diagram
- 20% → Charts / results
- 10% → Context / setup

---

## PHASE 3 — CONTENT ASSEMBLY

Produce a structured content block before rendering:

```
TITLE: [paper title, shortened if needed]
SUBTITLE: [1-line description of contribution]
AUTHORS: [names, institution, year]

THE QUESTION: [1 concise question the paper answers]
THE ANSWER: [1 bold direct answer]

CORE STAT: [the dominant number — e.g. "42.3% improvement"]
STAT CONTEXT: [what it measures, what baseline]

MECHANISM SUMMARY: [3 bullet labels describing how it works]

DIAGRAM SPEC:
  Nodes: [list]
  Edges: [list with directions]
  Groupings: [stages / layers]
  Layout: [left-right / top-down / circular]

CHART 1:
  Type: [bar / line / grouped bar]
  X-axis: [label]
  Y-axis: [label]
  Data: [values]
  Highlight: [which bar/point is the key finding]
  Source: [figure/table/page or "unknown"]

CHART 2 (if applicable):
  [same spec]

TAKEAWAYS:
  1. [label]
  2. [label]
  3. [label]

CITATION: [authors, venue, year, DOI if available]
SOURCE NOTES: [missing or partial evidence that affects confidence]
```

---

## PHASE 4 — COMPILE FIGURE OUTPUT

Pass the assembled content to the selected renderer with:
- `mode: poster`
- `layout: a1_portrait`
- `input_type: research_paper`

For `renderers/image_prompt.md`, produce:
- Copy-ready core prompt for a publication-quality paper figure
- Layout specification based on contribution type and dominant structure
- Label priority list separating essential labels from post-edit labels
- Negative prompt for avoiding decorative science cliches
- Source discipline with citation/source notes and missing evidence

For `renderers/html_artifact.md`, produce the final HTML/SVG artifact. Footer must include
citation/source notes and should not imply full-paper coverage if only partial content was
available.
