# Renderer: Image Prompt Package

Default renderer for copy-ready image-generation prompts. Use unless the user explicitly
asks for deterministic HTML/SVG.

## Input Contract

A sub-skill provides:

- `input_type`, `figure_goal`
- evidence, assumptions, unknowns
- nodes, edges, panels, labels, callouts, hierarchy
- palette profile and rationale
- optional scientific-main-figure fields: `figure_profile`, domain primitives, figure role,
  viewer takeaway, algorithm mechanism, layout plan, connector audit, and label hierarchy

## Output Template

Return this structure:

```markdown
# visual-plan Prompt Package

## 1. Figure Brief
[short message, style, audience]

## 2. Core Image Prompt
[copy-ready prompt]

## 3. Layout Specification
[spatial layout, reading order, grouping, hierarchy]

For scientific main figures, include:
- canvas/grid:
- visual weight:
- alignment anchors:
- whitespace plan:
- viewer takeaway:
- misinterpretation guards:
- visual archetype:
- algorithm mechanism:
- connector audit:

## 4. Label Priority
AI-visible labels:
- [...]
AI-visible operation labels:
- [...]
Post-edit only:
- [...]
Avoid generated text:
- [...]

## 5. Style Direction
Palette profile: [...]
Palette rationale: [...]
Visual style: [...]

## 6. Negative Prompt
Universal anti-cliche:
- [from style/domain_hints.md]
Domain anti-cliche:
- [matched domain Avoid list, if any]

## 7. Recommended Generation Settings
- Aspect ratio:
- Size:
- Quality:
- Background:
- Output format:
- Text strategy:

## 8. Post-Edit Notes
[exact labels/arrows/source details to fix manually]

## 9. Source Discipline
Evidence used:
- [...]
Assumptions:
- [...]
Unknowns:
- [...]
```

## Rules

- Evidence-bound numbers only. Unsupported stats become omitted, `unknown`, or qualitative.
- Preserve actual source structure; do not convert mechanisms into generic "AI workflow".
- State the primary claim, dominant visual, supporting elements, and subordinate elements.
- Choose a semantic palette from `style/visual_system.md`; explain color roles.
- Put tool-specific flags in settings, not the core prompt, unless the user chose a tool.
- Use 5-10 high-priority labels by default; for `figure_profile: nature_main_figure`, allow
  10-18 short labels only when grouped into clear hierarchy.
- For scientific main figures, include figure role, viewer takeaway, layout anchors, core
  algorithm mechanism, domain primitives, and connector audit.
- Low text is not zero text: keep short operation/state labels needed to explain the core
  algorithm. Move exact formulas, long mutation lists, tensor shapes, thresholds, and dense
  legends to post-edit notes.
- Disambiguate visual archetype failures with "use X, not Y" for ambiguous terms such as
  tree, network, controller, landscape, switchboard, pipeline, funnel, and map.
- Use connector discipline: every line/arrow must have a named role such as data flow,
  transformation, hierarchy, feedback, comparison, or local zoom. Prefer proximity,
  grouping, alignment, shared color, or labels when a line is not essential.
- Separate mechanism-figure style from algorithm-framework style. If both are needed,
  either provide separate prompts or clearly separated panels with shared colors/numbering.

Color semantics should be explicit:

```text
Use <palette> because <source/domain reason>.
Use dark slate only for the central anchor if needed.
Use light boxes for normal modules.
Use <accent> for the main path.
Use <novelty fill> for output/evidence/provenance.
Use gray dashed outlines for optional/external elements.
Use amber/coral only for warnings, blockers, or negative evidence.
```

## Defaults

| Figure type | Aspect | Size | Quality | Background |
|---|---|---|---|---|
| paper main figure | 16:9 or 3:2 | 1536x1024+ | high | white/opaque |
| scientific main figure | 16:9 or 3:2 | 1536x1024+ | high | white/opaque |
| graphical abstract | 16:9 | 1536x1024 | high | white/opaque |
| poster | 3:4 | 1024x1536 | high | white/opaque |
| square preview | 1:1 | 1024x1024 | medium/high | white/opaque |
| icon/sticker | 1:1 | 1024x1024 | medium | transparent |

## QA

- one clear scientific message
- spatially specific layout with clear grid, anchors, visual weight, and no arbitrary empty
  regions
- each panel/module has a purpose and viewer takeaway
- likely misinterpretations are prevented by visual encoding, not panel prose
- ambiguous visual archetypes are disambiguated with "use X, not Y"
- every connector line has a named purpose; no decorative or vague association lines
- AI-visible labels are separated from post-edit-only text
- core algorithm includes visible input, operation, intermediate state, and output
- text is sparse but sufficient for scientific meaning
- mechanism and algorithm visual grammars are not mixed unintentionally
- palette profile and color semantics named
- negative prompt includes universal and domain failure modes
- facts, assumptions, and unknowns are not mixed
- post-edit notes cover text fidelity risks
