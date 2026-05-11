# Sub-Skill: Research Paper -> Scientific Figure

Use for PDFs, academic papers, or extracted paper text. Output a source-backed graphical
abstract, main figure, or poster plan.

## Truth Rule

Never invent results, baselines, authors, venues, datasets, citations, or metrics. Missing
paper sections reduce confidence; they do not license guesses.

## Source Coverage

Start with:

```text
SOURCE COVERAGE:
  Title/authors/venue: found | unknown
  Abstract/introduction: found | unknown
  Method/architecture: found | unknown
  Figures/tables: found | unknown
  Results/experiments: found | unknown
  Limitations/conclusion: found | unknown
```

If partial, build only from available sections and state missing evidence.

## Extract

- contribution type: algorithm, model architecture, theory, empirical study, system,
  survey/meta-analysis
- dominant structure: pipeline, layered, modular, graph, loop, feedback, optimization,
  benchmark, scaling curve, generative, encode-decode, retrieval
- single most important idea
- novelty mechanism
- dominant metric and baseline comparison, if visible
- evidence location for each claim
- up to five quantitative results, each with source location

If exact values are unavailable, use a mechanism diagram or qualitative takeaway instead
of recreating a chart.

## Narrative

Use the arc:

```text
Hook -> Gap -> Insight -> Mechanism -> Evidence -> Impact
```

Default composition: Question/Answer header, one hero mechanism diagram, 1-2 source-backed
charts or evidence panels, takeaways, citation/source footer. Consult `style/domain_hints.md`
when field conventions matter.

## Content Block

```text
TITLE:
SUBTITLE:
AUTHORS:
CITATION:

THE QUESTION:
THE ANSWER:

CORE STAT:
STAT CONTEXT:
MECHANISM SUMMARY:

DIAGRAM SPEC:
  Nodes:
  Edges:
  Groupings:
  Layout:

CHARTS:
  - Type:
    Data:
    Highlight:
    Source:

TAKEAWAYS:
SOURCE NOTES:
UNKNOWNS:
```

Use `unknown` or omit `CORE STAT`/`CHARTS` when not sourced.

## Compile

Pass to the renderer with:

- `mode: poster`
- `layout: a1_portrait`
- `input_type: research_paper`

Footer must not imply full-paper coverage when only partial content was available.
