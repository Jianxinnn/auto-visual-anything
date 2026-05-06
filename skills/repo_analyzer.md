# Sub-Skill: Code Repository → Figure Plan

**Trigger**: Input is source code, a file tree, a zip archive, or multiple code files.

**Output**: Source-backed figure plan for a repo architecture diagram. Compile it into an
optimized image prompt package by default, or an editable HTML/SVG artifact when requested.

Read `style/visual_system.md` before executing this skill.
After analysis, pass output to the selected renderer: `renderers/image_prompt.md` by default,
or `renderers/html_artifact.md` for deterministic vector output.

Truth rule: code is the source of truth. Do not infer frameworks, data stores, queues,
or services unless they appear in files, manifests, imports, configuration, or user-provided
context. Mark uncertain items as `unknown` instead of inventing them.

---

## PHASE 1 — REPOSITORY INGESTION

### 1.1 Environment Detection

**Local coding environment**:
```bash
# First: get a scoped file inventory
rg --files -g '!node_modules' -g '!.git' -g '!dist' -g '!build' -g '!coverage' -g '!__pycache__'

# Then: identify manifests and entry points
rg --files | rg '(^|/)(package.json|pnpm-lock.yaml|pyproject.toml|requirements.txt|Cargo.toml|go.mod|pom.xml|Dockerfile|docker-compose.yml|main\.(py|go|rs)|index\.(ts|tsx|js|jsx)|app\.(py|ts|tsx|js)|server\.(ts|js))$'

# Then: read key files
# - Entry points (main.py, index.ts, app.py, server.js, etc.)
# - Config files (package.json, pyproject.toml, Cargo.toml, etc.)
# - Core module files (not test files or generated files)
```

If `rg` is unavailable, use the fastest equivalent file listing tool in the environment.

**Chat/upload environment**:
- Read all uploaded file contents
- Build mental file tree from paths and imports
- Treat missing files as unknown; do not assume repository structure that was not provided

### 1.1b Evidence Ledger

Before drawing, create a compact evidence ledger:

```
EVIDENCE:
  Manifest files: [paths]
  Entry points: [paths]
  Core modules inspected: [paths]
  Config/deployment files: [paths]
  External systems directly evidenced: [DB/API/queue/cache + file path]
  Unknowns: [important facts not visible from available files]
```

### 1.2 Structural Extraction

Extract these layers in order:

**Layer 1 — File Tree Structure**
```
Group files by:
- Directories → modules / packages
- File naming patterns → roles (routes/, models/, utils/, services/, etc.)
- Entry points → system boundary
```

**Layer 2 — Dependency Graph**
```
For each file, extract:
- Import statements (what it depends on)
- Export statements (what it provides)
- External dependencies (third-party packages)

Build: dependency adjacency list at directory/module level first, file level only for
critical paths. Detect cycles, clusters, leaf nodes, and hub nodes only when supported
by inspected imports.
```

**Layer 3 — Semantic Roles**
```
Classify each module/file into a role:
- ENTRY       → main entry, CLI, API server startup
- ROUTER      → request routing, dispatch
- CONTROLLER  → business logic coordination
- SERVICE     → domain logic, use cases
- MODEL       → data structures, schemas, ORM
- REPOSITORY  → data access, DB queries
- UTIL        → shared helpers, formatters
- CONFIG      → configuration, env, constants
- EXTERNAL    → third-party integrations, APIs
- PIPELINE    → data processing stages
- AGENT       → autonomous components
- TEST        → test files (exclude from diagram)
```

**Layer 4 — Data Flow**
```
Trace from evidenced entry points:
- Where does data/request input enter?
- Which modules transform or validate it?
- Which storage/API/file/queue/output boundary does it reach?
- What is unknown because the relevant source was absent?
```

### 1.3 Architecture Pattern Recognition

Identify the dominant pattern:

| Pattern | Signals |
|---------|---------|
| **MVC / Layered** | models/, views/, controllers/ directories |
| **Microservices** | multiple service dirs, API gateway, message queue |
| **Event-driven** | event bus, listeners, handlers, subscribers |
| **Pipeline / ETL** | stages, transforms, sources, sinks |
| **ML System** | training, inference, data loading, model registry |
| **Agent System** | agents, tools, orchestrator, memory |
| **CQRS / DDD** | commands, queries, aggregates, domain events |
| **Monolith** | single app with internal modules |
| **Plugin / Extension** | core + plugins, hooks, middleware chain |

### 1.4 Key Metrics Extraction

Count and surface only what can be measured from the inspected files:
- Total source files / modules (exclude dependencies, build output, generated files)
- Number of manifest-listed external dependencies
- Largest/most-imported modules if imports were inspected
- Circular dependencies if detected; otherwise say "not detected in inspected graph"
- Lines of code per top-level module if cheaply measurable; otherwise omit

---

## PHASE 2 — MULTI-LEVEL ARCHITECTURE PLAN

Always produce TWO diagram levels:

### Level 1 — System Overview (high abstraction)
```
Show:
- Major system boundaries
- External systems / APIs / databases
- Primary data flows between boundaries
- Technology stack labels

Max nodes: 8–12
Abstraction: no individual files, only subsystems
```

### Level 2 — Module Detail (mid abstraction)
```
Show:
- Key modules within each subsystem
- Inter-module dependencies
- Data types flowing between modules
- Entry/exit points

Max nodes: 20–30
Abstraction: directory/package level
```

### Optional Level 3 — Critical Path Detail
```
If there is a particularly complex core path (e.g., request lifecycle, training loop):
- Show individual functions/classes for that path only
- Mark it as "CRITICAL PATH" with cyan highlight
```

---

## PHASE 3 — CONTENT ASSEMBLY

Produce this structured block:

```
REPO NAME: [name from package.json / directory / user input]
TECH STACK: [languages, frameworks, key libraries]
PATTERN: [dominant architecture pattern]
SCALE: [X files, Y modules, Z external deps]
CONFIDENCE: [high / medium / low, based on coverage of inspected source]

THE SYSTEM DOES: [1 sentence plain description]
THE KEY INSIGHT: [most interesting architectural decision]

EVIDENCE SUMMARY:
  - Entry points: [path list]
  - Manifests: [path list]
  - Core modules read: [path list]
  - External systems found: [path + reason, or unknown]

SYSTEM OVERVIEW DIAGRAM:
  Nodes: [list of subsystems]
  Edges: [data flows with labels]
  External: [databases, APIs, queues]
  Layout: [left-right pipeline / top-down layers / hub-spoke]

MODULE DETAIL DIAGRAM:
  Nodes: [list of modules with roles]
  Edges: [dependency directions]
  Highlighted: [hub nodes, critical path]
  Layout: [same direction as system overview]

KEY FINDINGS:
  - Most central module: [name] (imported by X others, or "unknown")
  - Longest chain: [A → B → C → D]
  - External deps: [top 5 by usage]
  - Issues found: [cycles, god modules, orphan modules — or "none"]
  - Unknowns: [missing evidence that would improve the diagram]

TECH STACK BREAKDOWN:
  [pie or grouped bar: by language/layer/role]

ARCHITECTURE STATS:
  [3–5 key numbers to display prominently]
```

---

## PHASE 4 — NARRATIVE STRUCTURE

Frame the architecture as a story:

```
WHAT IT IS    → [system name] is a [pattern] system that [does X]
HOW IT FLOWS  → Data enters via [entry], flows through [stages], exits as [output]
KEY DESIGN    → The central design decision is [X], enabling [Y]
NOTABLE       → Most interesting: [structural observation]
HEALTH        → [Any architectural concerns or strengths]
```

---

## PHASE 5 — COMPILE FIGURE OUTPUT

Pass assembled content to the selected renderer with:
- `mode: diagram_poster`
- `layout: two_level`
- `input_type: code_repo`
- `source_paths: [most important files used]`

For `renderers/image_prompt.md`, produce:
- Copy-ready core prompt for a repo architecture main figure
- Panel/layout specification for system overview and module detail
- High-priority labels and source-path-aware post-edit notes
- Negative prompt for avoiding generic cloud diagrams and unsupported systems

For `renderers/html_artifact.md`, produce an HTML/SVG artifact with:
- System overview diagram (top)
- Module detail diagram (middle)
- Stats panel with key metrics (bottom)
- Tech stack breakdown chart
- Footer with source paths and confidence
