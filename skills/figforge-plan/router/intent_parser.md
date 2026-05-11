# Router: Intent Parser

**Purpose**: Detailed classification rules for the figforge-plan master router.
Read this file only if the main router's detection rules are ambiguous.

---

## Routing Principle

figforge-plan should trigger only when the user wants a visual artifact, figure plan,
or image-generation prompt. Once triggered, detect every strong input type before choosing
a route. Mixed inputs should not be collapsed into a single route just because one signal
appears first.

Use this lightweight scoring model:

```
score[type] = strong_signals * 2 + moderate_signals

IF two or more types have score >= 2
  → HYBRID
ELSE IF one type has score >= 2
  → that type
ELSE IF user asks for a new visual architecture with no source
  → DESIGN_REQUEST
ELSE
  ask one concise disambiguation question or do not use this skill
```

---

## Signal Rules

### CODE_REPO

Strong signals:
- Local path to a repository or project directory.
- Package manifests: `package.json`, `pnpm-lock.yaml`, `pyproject.toml`, `requirements.txt`,
  `Cargo.toml`, `go.mod`, `pom.xml`, `.csproj`.
- File tree with source directories such as `src/`, `app/`, `lib/`, `server/`, `routes/`,
  `services/`, `models/`, `tests/`.
- Source syntax: `import`, `from ... import`, `require(`, `use crate`, `#include`,
  `class Foo`, `def bar`, `function baz`, `fn qux`.
- User says "repo", "codebase", "source code", "this project", "analyze this project".

Moderate signals:
- Mentions modules, functions, classes, APIs, services, controllers, packages, or build files.
- User asks for architecture "from the implementation".

### RESEARCH_PAPER

Strong signals:
- PDF upload or path to a paper PDF.
- Paper sections: Abstract, Introduction, Method, Experiments, Results, Limitations.
- References to "Figure 1", "Table 2", "Appendix", citations, bibliography, DOI, arXiv ID.
- Venue or paper language: NeurIPS, ICML, ICLR, CVPR, ACL, SIGMOD, "we propose", "we evaluate".
- User says "paper", "research paper", "论文", "arXiv", "publication".

Moderate signals:
- Formal notation, theorem/proof structure, benchmark tables, ablation studies.
- Mentions baselines, metrics, datasets, or experimental comparisons.

### DIAGRAM_IMAGE

Strong signals:
- Uploaded or linked image/SVG/screenshot used as the primary input.
- Visible boxes, arrows, nodes, swimlanes, layers, flowchart symbols, or model blocks.
- User says "this diagram", "this figure", "this flowchart", "architecture image",
  "redesign this image", "make one like this".

Moderate signals:
- The user describes what an image shows.
- Screenshot of a whiteboard, slide, paper figure, or system design.

### ALGO_TEXT

Strong signals:
- Numbered algorithm steps, pseudocode, formulas plus procedural text, or stage-by-stage logic.
- User says "algorithm", "pseudocode", "process", "pipeline", "workflow", "turn this into a diagram".
- Text describes inputs, transformations, loops, decisions, outputs, or state transitions.

Moderate signals:
- Bullet-point technical spec with "first / then / finally".
- Describes a computational process but contains no actual source-code syntax.

### DESIGN_REQUEST

Strong signals:
- User asks "design me...", "create an architecture for...", "how would you build...",
  "sketch a system for...", "draw a system design for...".
- No source material is provided.
- User wants an original architecture, not analysis of existing material.

Moderate signals:
- Mentions desired constraints such as scale, latency, cost, reliability, model type, or deployment.

---

## Ambiguous Cases

Text that describes implementation but contains no code syntax:
→ ALGO_TEXT.

Paper plus pasted code, a repo path, or implementation files:
→ HYBRID. The paper is intent; the code is implementation evidence.

Screenshot of a paper figure:
→ DIAGRAM_IMAGE if the user wants the visual style or diagram structure transformed.
→ RESEARCH_PAPER if the user wants the whole paper summarized into a poster.

Uploaded image plus explanatory text:
→ HYBRID when both materially affect the output.

User asks to "improve", "polish", or "make this diagram better":
→ DIAGRAM_IMAGE with mode `refine`, not domain transposition.

User asks only "what do you think of this architecture?":
→ Do not trigger unless they ask for a diagram, map, poster, or visual rewrite.

---

## Disambiguation

When the route is genuinely unclear, ask one question with two concrete options:

> "Should I treat this as a codebase-to-architecture diagram, or as an algorithm/process visualization?"

If one route is clearly more useful and the risk is low, make the best guess and proceed.
