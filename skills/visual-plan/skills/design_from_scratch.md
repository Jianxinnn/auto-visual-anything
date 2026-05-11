# Sub-Skill: Design From Scratch -> Figure Plan

Use when the user requests a new system or algorithm design with no source artifact.

## Truth Rule

All unstated scale, latency, data, deployment, and reliability choices are design
assumptions. Be opinionated, but never present assumptions as analyzed facts. Footer must
state `design assumptions`.

## Extract Requirements

```text
DOMAIN:
GOAL:
CONSTRAINTS:
STYLE HINT:
NOVELTY: standard | exploratory
ASSUMPTIONS:
  Scale:
  Latency:
  Data sensitivity:
  Deployment:
```

Ask one clarifying question only if the missing detail changes the architecture class
(for example, online consumer-scale serving vs offline prototype).

## Design

Choose an appropriate pattern:

- recommendation: retrieval -> ranking -> personalization
- NLP: encoder/attention/task head
- data pipeline: ingest -> transform -> serve
- ML training: loader -> trainer -> evaluator -> registry
- agent system: perception -> memory -> reasoning -> action
- API service: gateway -> router -> service -> cache/DB
- real-time system: event stream -> processor -> sink/monitor
- search: crawler -> indexer -> retriever -> ranker

For each component, define purpose, interface, implementation approach, scale posture,
and failure mode. Then define entry point, stages, storage, exit point, and feedback loop.

## Rationale

Capture 3-5 key decisions:

```text
DECISION:
  WHY:
  TRADE-OFF:
  IMPACT:
```

Also list 1-2 alternatives not chosen and a V1 -> V2 -> V3 roadmap.

## Content Block

```text
SYSTEM NAME:
SUBTITLE:

THE QUESTION:
THE ANSWER:
DESIGN GOALS:
ASSUMPTIONS:
PATTERN:

DIAGRAM SPEC:
  Flow pattern:
  Nodes:
  Edges:
  Groupings:
  Highlighted path:
  Secondary paths:
  Special elements:

DATA FLOW:
DESIGN DECISIONS:
ALTERNATIVES:
ROADMAP:
NARRATIVE:
```

## Compile

Pass to the renderer with:

- `mode: architecture_design`
- `layout: a1_portrait`
- `input_type: design_request`

Make assumptions visible in the layout and footer. Use `style/domain_hints.md` when the
domain has strong visual conventions or cliches.
