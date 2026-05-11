# Sub-Skill: Hybrid Input Handler

Use when input contains multiple source types, such as code + paper, diagram + text, repo
+ spec, or multiple diagrams.

## Truth Rule

Keep source authority separate until synthesis. Do not let an attractive diagram or paper
claim override code evidence. Tag claims as `[FROM CODE]`, `[FROM PAPER]`,
`[FROM DIAGRAM]`, `[FROM TEXT]`, `[SYNTHESIZED]`, or `[UNKNOWN]`.

## Decompose

```text
COMPONENT A:
  type:
  content:
  role:
COMPONENT B:
  type:
  content:
  role:

SOURCE AUTHORITY:
  Code: implemented behavior
  Paper/spec: intended method/rationale
  Diagram: visible structure/names
  Text: user intent/emphasis
```

## Cross-Reference

```text
AGREEMENTS:
COMPLEMENTARY DETAILS:
  Code shows:
  Paper shows:
  Diagram shows:
  Text shows:
CONFLICTS / GAPS:
  [state which source wins and why, or mark unresolved]
```

Apply only Phase 1 of each relevant sub-skill, then synthesize one unified understanding.

## Mode

| Combination | Mode |
|---|---|
| paper + code | Implementation Analysis |
| diagram + text | Design Draft |
| repo + paper | Research Implementation Review |
| code + text spec | Spec Conformance |
| multiple diagrams | Architecture Comparison |
| all types | Complete System Analysis |

## Compile

Build the content block using the dominant input type's structure plus secondary evidence.
Pass to the renderer with:

- `mode: <selected>`
- `layout: a1_portrait`
- `input_type: hybrid`
- `sources: [input types]`
- `conflicts: [resolved/unresolved conflicts]`

Make source authority visible in labels, panels, post-edit notes, and footer.
