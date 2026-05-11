# Slide Generation Spec

`visual-deck` is an image-generation orchestrator. The output is still one
image2 / gpt-image-2 generated PNG per slide. This spec is the planning layer
that prevents those generated images from becoming empty, generic, or visually
chaotic.

The spec is not a deterministic drawing format. It is a compact contract for
compiling stronger per-slide image prompts.

---

## Pipeline Position

```
deck_content_brief.md
  -> outline.md
  -> slide_generation_specs/slide-NN.md
  -> prompts/slide-NN.md
  -> render_slides.py
  -> visual-gen / gpt-image-2
  -> slides/slide-NN.png
```

`outline.md` says what the deck says. `slide_generation_specs/` says how image2
should make the slide visually rich without inventing unsupported content.

---

## Minimal Spec Shape

Use Markdown for readability:

```markdown
# Slide Generation Spec: slide-03

- role: content
- domain_mode: sci-structural
- title: 计算路线
- captions:
  - FOL/DHF双态
  - DMS降风险
- visual_primitive: pipeline
- image2_detail_level: high
- text_policy: title_and_two_captions_only

## Claim
Candidates are designed and screened across FOL/FA and DHF states before DMS risk filtering.

## Evidence Anchors
- LigandMPNN cross-state scoring
- DMS source over 3078 single mutants

## Mechanism / Scene Grammar
- Left: two ternary state cards, one FOL/FA target and one DHF anti-target.
- Middle: LigandMPNN design pool, shown as varied candidate glyphs.
- Right: cross-state scoring and DMS filter gate.
- Use a solid navy path for accepted low-burden evidence.
- Use a rust dashed branch for high-burden or uncertain candidates.

## Must Include Visually
- target/anti-target state contrast
- candidate compression/funnel
- evidence gate
- warning branch

## Must Avoid
- fake numeric tables
- tiny unreadable labels
- stock lab bench
- decorative DNA wallpaper
- generic protein blob without state contrast

## Prompt Compile Notes
- Keep Chinese title and captions large.
- Put technical labels as large short Latin tokens only: FOL/FA, DHF, DMS.
- Do not add file paths or extra numbers.
```

---

## Domain Modes

Use `domain_mode` from `domain-tendencies.md`. The mode changes how prompts are
compiled:

- `sci-research`: image2 must show evidence structure, uncertainty, and mechanism.
- `sci-structural`: image2 must show state contrast, residue/motif/state logic,
  ligand or mutation semantics, not generic biology decoration.
- `product-marketing`: image2 may use hero imagery, but product/object/workflow
  must be visible in the first visual field.
- `tech-product`: image2 should show architecture/workflow with clean technical
  diagram primitives, not cinematic abstraction.
- `business-report`: image2 should show operational structure, KPI/risk/roadmap
  motifs, and restrained visual density.
- `editorial-creative`: image2 can carry more mood and visual rhythm, but factual
  claims remain constrained by the brief.

---

## Visual Primitives

The primitive is a prompt grammar, not a renderer instruction.

SCI-oriented:

- `state_contrast`: target vs anti-target, treatment vs control.
- `mechanism_panel`: causal mechanism with sparse labeled regions.
- `pipeline`: left-to-right workflow with distinct stages.
- `evidence_stack`: multiple evidence layers leading to one bounded conclusion.
- `quant_figure`: generated chart-like visual; exact numbers must be limited to
  title/captions or large labels.
- `risk_map`: two-axis conceptual map with large labeled regions.
- `decision_loop`: next-round SOP or assay decision path.

Product/business-oriented:

- `product_hero`: generated hero slide showing the product/object/category.
- `workflow`: user, operational, or tool flow.
- `architecture`: system/data/agent/tool routing.
- `comparison`: alternatives and tradeoffs.
- `metric_story`: KPI-like visual without asking image2 to render dense tables.
- `roadmap`: phases and dependency gates.
- `risk_register`: blocker/risk/mitigation motif.

---

## Image2 Prompt Rules

Every compiled prompt must include:

- role and sequence
- domain_mode
- title and captions
- visual primitive
- concrete scene grammar
- must-include visual details
- must-avoid list
- truth constraints
- style anchors from the chosen style file

For SCI slides:

- Tell image2 what mechanism to draw, not only what topic the slide covers.
- Prefer 3-6 large visual elements over many tiny panels.
- Use short Latin labels for technical tokens; keep Chinese text to the title
  and at most two captions.
- Any exact numeric evidence should be large, sparse, and already present in the
  spec. Do not ask image2 to render dense DMS tables.
- If uncertainty matters, represent it as warning branch, dashed region, or
  caution zone.

For product/business slides:

- Show the product, user action, workflow, architecture, or decision object.
- Avoid generic SaaS icon grids unless the source is actually a feature grid.
- Metrics can be shown as simple bars/cards, but never dense fake dashboards.

---

## QA Before Generation

Before calling image2:

- Does the slide have a visual primitive?
- Does the prompt specify mechanism/scene grammar, not just a topic?
- Are title and captions short enough for image2?
- Are technical labels limited to large short tokens?
- Is the uncertainty or warning logic visible when needed?
- Does the prompt forbid common domain cliches?
- For source-backed decks, can every claim be traced to `deck_content_brief.md`
  or user-authored outline content?
