# Slide Generation Spec

`visual-deck` uses one image2 / `gpt-image-2` PNG per slide. A generation spec makes each
prompt concrete enough to avoid generic slide art.

Pipeline:

```text
deck_content_brief.md -> outline.md -> slide_generation_specs/slide-NN.md
-> prompts/slide-NN.md -> render_slides.py -> visual-gen -> slides/slide-NN.png
```

## Shape

```markdown
# Slide Generation Spec: slide-03

- role: content
- domain_mode: sci-structural
- title: 计算路线
- captions:
  - FOL/DHF 双态
  - DMS 降风险
- visual_primitive: pipeline
- image2_detail_level: high
- text_policy: title_and_two_captions_only

## Claim
[one source-supported claim]

## Evidence Anchors
- [...]

## Mechanism / Scene Grammar
- Left: [...]
- Middle: [...]
- Right: [...]

## Must Include Visually
- [...]

## Must Avoid
- [...]

## Prompt Compile Notes
- [...]
```

## Domain Modes

- `sci-research`: evidence, uncertainty, mechanism
- `sci-structural`: state contrast, residue/motif/ligand logic
- `product-marketing`: visible product/object/workflow and value
- `tech-product`: architecture/workflow, clean technical primitives
- `business-report`: KPI/risk/roadmap motifs, restrained density
- `editorial-creative`: stronger rhythm/mood, but claims remain constrained

## Visual Primitives

SCI: `state_contrast`, `mechanism_panel`, `pipeline`, `evidence_stack`, `quant_figure`,
`risk_map`, `decision_loop`.

Product/business: `product_hero`, `workflow`, `architecture`, `comparison`,
`metric_story`, `roadmap`, `risk_register`.

## Prompt Rules

Every compiled prompt includes role/sequence, `domain_mode`, title/captions,
`visual_primitive`, scene grammar, must-include, must-avoid, truth constraints, and chosen
style anchors.

SCI slides: draw a mechanism, not only a topic; prefer 3-6 large elements; keep technical
tokens short and large; show uncertainty as warning branch/dashed region/caution zone.

Product/business slides: show the actual product, user action, workflow, architecture, or
decision object. Do not render dense fake dashboards or generic SaaS icon grids.

## QA

- visual primitive present
- scene grammar is concrete
- title/captions fit image text budget
- exact labels are short, large tokens
- uncertainty/warning visible when needed
- domain cliches forbidden
- source-backed claims trace to brief or user outline
