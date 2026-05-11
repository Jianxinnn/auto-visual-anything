# Sub-Skill: Code Repository -> Figure Plan

Use for source code, file trees, zip contents, or multiple code files. Output a
source-backed repo architecture plan for the selected renderer.

## Truth Rule

Code is evidence. Do not infer frameworks, stores, queues, services, or metrics unless
they appear in manifests, imports, config, source, commands, or user text.

## Ingest

Local:

```bash
rg --files -g '!node_modules' -g '!.git' -g '!dist' -g '!build' -g '!coverage' -g '!__pycache__'
rg --files | rg '(^|/)(package.json|pyproject.toml|requirements.txt|Cargo.toml|go.mod|pom.xml|Dockerfile|docker-compose.yml|main\.(py|go|rs)|index\.(ts|tsx|js|jsx)|app\.(py|ts|tsx|js)|server\.(ts|js))$'
```

Read manifests, entry points, config/deploy files, and core modules. Skip tests and
generated output unless they define the architecture. In chat/upload contexts, use only
provided files and mark missing structure as unknown.

Create:

```text
EVIDENCE:
  Manifest files: [...]
  Entry points: [...]
  Core modules inspected: [...]
  Config/deployment files: [...]
  External systems evidenced: [...]
UNKNOWNS:
  [...]
```

## Extract

1. File tree: directories, packages, entry boundaries.
2. Dependency graph: imports/exports and third-party dependencies, grouped by module.
3. Roles: `ENTRY`, `ROUTER`, `CONTROLLER`, `SERVICE`, `MODEL`, `REPOSITORY`, `UTIL`,
   `CONFIG`, `EXTERNAL`, `PIPELINE`, `AGENT`, `TEST`.
4. Data flow: input -> validation/transform -> storage/API/file/queue/output.
5. Pattern: layered, microservice, event-driven, ETL, ML, agent, CQRS/DDD, monolith,
   plugin/extension, or unknown.

Measure cheap metrics only by command or direct inspection: file/module counts,
manifest dependencies, central imports, cycles, or LOC by module. If not measured, omit.

## Figure Plan

Default source style: two-level architecture.

- Level 1: system overview, 8-12 nodes, external systems and primary flows.
- Level 2: module detail, directory/package level, 20-30 nodes max.
- Optional critical path: individual functions/classes only for a genuinely central path.

## Content Block

```text
REPO NAME:
TECH STACK:
PATTERN:
SCALE:
CONFIDENCE:

THE SYSTEM DOES:
KEY INSIGHT:

EVIDENCE SUMMARY:
  Entry points:
  Manifests:
  Core modules read:
  External systems:
  Unknowns:

SYSTEM OVERVIEW:
  Nodes:
  Edges:
  External:
  Layout:

MODULE DETAIL:
  Nodes:
  Edges:
  Highlighted:
  Layout:

FINDINGS:
  Central module:
  Critical chain:
  External deps:
  Issues:
  Unknowns:

STATS:
  [only measured values]
```

## Compile

Pass to the renderer with:

- `mode: diagram_poster`
- `layout: two_level`
- `input_type: code_repo`
- `source_paths: [key files]`

For image prompts, emphasize real modules, actual data flow, label priority, and
source-aware post-edit notes. For HTML, include overview, module detail, measured stats,
findings, and footer with paths/confidence.
