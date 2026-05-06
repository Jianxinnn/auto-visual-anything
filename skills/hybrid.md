# Sub-Skill: Hybrid Input Handler → Unified Figure Prompt

**Trigger**: Input contains MULTIPLE types — e.g., code + paper, diagram + description,
repo + algorithm spec, or any combination of the input types.

**Output**: Unified figure plan combining all input sources. Compile it into an optimized
image prompt package by default, or an editable HTML/SVG artifact when requested.

Read `style/visual_system.md` before executing this skill.
After analysis, pass output to the selected renderer: `renderers/image_prompt.md` by default,
or `renderers/html_artifact.md` for deterministic vector output.

Truth rule: keep sources separate until synthesis. Do not let an attractive diagram or
paper claim override implementation evidence. Mark conflicts and unknowns explicitly.

---

## PHASE 1 — INPUT DECOMPOSITION

Split the input into its constituent types:

```
COMPONENT A: [type: CODE_REPO / RESEARCH_PAPER / DIAGRAM_IMAGE / ALGO_TEXT]
  Content: [brief description of this component]
  Primary role: [what this component contributes to understanding]

COMPONENT B: [type: ...]
  Content: [brief description]
  Primary role: [...]

[continue for all components]
```

Assign source authority:

```
SOURCE AUTHORITY:
  Code: ground truth for implemented behavior
  Paper/spec: ground truth for intended method or rationale
  Diagram/image: ground truth for visual structure and naming visible in the image
  Text description: ground truth for user intent and requested emphasis
```

---

## PHASE 2 — CROSS-REFERENCE ANALYSIS

Find where the inputs agree, conflict, or complement each other:

```
AGREEMENTS:
  [What all inputs say consistently about the architecture]

COMPLEMENTARY DETAILS:
  [What each input adds that the others lack]
  - Code shows: [implementation details not in paper/text]
  - Paper shows: [theoretical framing not visible in code]
  - Diagram shows: [visual structure not explicit in text]
  - Text shows: [intent / design rationale not in code or diagram]

CONFLICTS / GAPS:
  [Where inputs disagree or leave gaps]
  [State which source wins and why]
```

---

## PHASE 3 — UNIFIED ANALYSIS

Read and apply ALL relevant sub-skills:

1. For each CODE_REPO component → apply `skills/repo_analyzer.md` Phase 1 only
2. For each RESEARCH_PAPER component → apply `skills/paper_to_poster.md` Phase 1 only
3. For each DIAGRAM_IMAGE component → apply `skills/diagram_to_draft.md` Phase 1 only
4. For each ALGO_TEXT component → apply `skills/algo_to_draft.md` Phase 1 only

Then synthesize into ONE unified architecture understanding.

---

## PHASE 4 — OUTPUT MODE SELECTION

Based on the combination, select the output mode:

| Combination | Output Mode |
|-------------|------------|
| Paper + Code | "Implementation Analysis" — paper's architecture vs actual code |
| Diagram + Text | "Design Draft" — visualize the described algorithm |
| Repo + Paper | "Research Implementation Review" — does code match paper? |
| Code + Text Spec | "Spec Conformance" — does code match specification? |
| Multiple Diagrams | "Architecture Comparison" — side by side |
| All types | "Complete System Analysis" — full poster |

---

## PHASE 5 — UNIFIED CONTENT ASSEMBLY

Merge all analysis into a single content block following the structure of the
dominant input type's sub-skill, with additions from secondary inputs.

Mark clearly:
- `[FROM CODE]` — insight derived from code analysis
- `[FROM PAPER]` — insight derived from paper
- `[FROM DIAGRAM]` — insight derived from image
- `[FROM TEXT]` — insight derived from text description
- `[SYNTHESIZED]` — insight derived from combining multiple inputs
- `[UNKNOWN]` — information that is important but not evidenced

---

## PHASE 6 — COMPILE FIGURE OUTPUT

Pass assembled content to the selected renderer with:
- `mode: [selected from Phase 4]`
- `layout: a1_portrait`
- `input_type: hybrid`
- `sources: [list of input types]`
- `conflicts: [list of resolved or unresolved conflicts]`

For `renderers/image_prompt.md`, produce:
- Copy-ready prompt that makes source authority and synthesis visible
- Layout spec showing how paper/code/diagram/text evidence connect
- Label priority list with source tags when useful
- Negative prompt for avoiding over-smoothed claims or hiding mismatches
- Post-edit notes for conflicts and source-specific labels
