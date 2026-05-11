# Renderer: Image Prompt Package

Default renderer for copy-ready image-generation prompts. Use unless the user explicitly
asks for deterministic HTML/SVG.

## Input Contract

A sub-skill provides:

- `input_type`, `figure_goal`
- evidence, assumptions, unknowns
- nodes, edges, panels, labels, callouts, hierarchy
- palette profile and rationale

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

## 4. Label Priority
High-priority labels:
- [...]
Secondary labels:
- [...]
Avoid tiny text:
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
- Use 5-10 high-priority labels; dense paths, citations, and field names go to post-edit.
- State the primary claim, dominant visual, supporting elements, and subordinate elements.
- Choose a semantic palette from `style/visual_system.md`; explain color roles.
- Put tool-specific flags in settings, not the core prompt, unless the user chose a tool.

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
| graphical abstract | 16:9 | 1536x1024 | high | white/opaque |
| poster | 3:4 | 1024x1536 | high | white/opaque |
| square preview | 1:1 | 1024x1024 | medium/high | white/opaque |
| icon/sticker | 1:1 | 1024x1024 | medium | transparent |

## QA

- one clear scientific message
- spatially specific layout
- palette profile and color semantics named
- labels few enough to render
- negative prompt includes universal and domain failure modes
- facts, assumptions, and unknowns are not mixed
- post-edit notes cover text fidelity risks
