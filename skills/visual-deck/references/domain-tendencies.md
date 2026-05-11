# Domain Tendencies

`visual-deck` must not treat every deck as the same "pretty slide image" problem.
The audience and domain determine what image2 should emphasize, how much visual
density is acceptable, and which details must be explicit in the prompt.

This reference is runtime-local to the skill. Do not depend on repo-root `docs/`
or `contracts/` when using it from an installed skill.

---

## Decision Rule

Choose one `domain_mode` before outlining slides:

- `sci-research`: papers, lab meetings, biological design, algorithms, mechanisms,
  experiments, evidence review.
- `sci-structural`: structural biology, molecular mechanisms, protein design,
  chemistry, ligand-state reasoning.
- `product-marketing`: public product story, launch, sales, investor, customer
  narrative.
- `tech-product`: engineering demo, infra system, agent/tool workflow, developer
  platform.
- `business-report`: operating report, weekly/monthly review, project status,
  roadmap, risk review.
- `editorial-creative`: portfolio, concept board, magazine-style visual story,
  brand mood.

If two modes fit, pick the stricter content mode. For example, a protein-design
pitch is `sci-structural` first and `product-marketing` second; evidence fidelity
wins over visual drama.

---

## SCI Tendencies

SCI-facing decks are evidence instruments generated as images. They must prioritize
traceable claims, mechanism, experimental/computational evidence, and uncertainty.

Default bias:

- Content density: medium to high, but structured into a few large image2-friendly
  mechanisms or primitives.
- Text strategy: one large title plus at most two short captions. Technical labels
  should be short large tokens, such as `E79L`, `SD3`, `FD`, `FOL/FA`, `DHF`.
- Generation strategy: image2 generates the full slide image, but the prompt must
  encode mechanism, evidence anchors, warning semantics, and anti-cliches.
- Palette: restrained light backgrounds, semantic accent colors for evidence,
  warning, uncertainty, and recommended next action.
- Proof obligation: every content slide has `claim`, `evidence_refs`,
  `mechanism/scene grammar`, `uncertainty`, and a `visual_primitive`.

Recommended primitives:

- `state_contrast`: target vs anti-target, before vs after, control vs treatment.
- `mechanism_panel`: nodes, causal arrows, local residues, ligand states,
  perturbation points.
- `pipeline`: method route, screening funnel, scoring sequence, validation loop.
- `evidence_stack`: computation, in silico sanity check, wet-lab readout,
  interpretation.
- `quant_chart`: source-backed bar, scatter, small-multiple, heatmap, or rank-plot
  composition with sparse labels.
- `risk_map`: 2D uncertainty, burden, selectivity, confidence, or feasibility map.
- `decision_loop`: next-round SOP, assay gate, go/no-go rule, iteration plan.

Avoid:

- Generic scientific clipart, decorative DNA helix, stock lab bench imagery.
- Dense text generated directly by the image model.
- Fake dense microplots or fake axes that imply unavailable precision.
- Visual claims that look stronger than the evidence ledger supports.

### Structural Biology Bias

For protein, ligand, enzyme, or mutation work:

- Prefer residue/motif/state diagrams over generic molecule wallpaper.
- Show target and anti-target states explicitly when selectivity matters.
- Use residue labels sparingly as fixed source-backed tokens, such as `E79L`, `K162E`,
  `SD3`, `FOL/FA`, `DHF`.
- Treat full redesign sequences as evidence sources unless the source proves they
  are final candidates.
- Put uncertainty on-slide when the biological conclusion depends on missing
  assays.

### Methods / Algorithm Bias

For ML, algorithm, or agent research:

- Use architecture blocks, data-flow arrows, ablation grids, and evaluation
  matrices.
- Preserve the real names of modules and metrics.
- Separate "control-plane improvement", "selected-baseline win", and broad
  superiority claims.
- Do not turn algorithms into generic AI glow, robot, brain, or network motifs.

---

## Product And Business Tendencies

Product-facing decks are decision and persuasion images. They may be more visual
than SCI decks, but concrete product, user, value, workflow, and risk signals still
matter.

Default bias:

- Content density: low to medium, except business-report mode where density can
  be medium-high.
- Text strategy: short headlines and captions; avoid asking image2 to render dense
  brand, price, metric, or legal copy.
- Generation strategy: image2 generates the slide, but prompts must specify the
  actual product/object/workflow and avoid generic placeholder visuals.
- Palette: style-specific, but avoid one-note palettes and decorative gradients
  when the deck is operational.
- Proof obligation: each content slide states `object`, `audience`, `value`,
  `support`, and `next_action` unless it is a pure cover or divider.

Recommended primitives:

- `product_hero`: product/object in the first visual field, with source-backed
  headline and value caption.
- `workflow`: user journey, task flow, before/after operational flow.
- `architecture`: system layers, integrations, routing, data movement.
- `comparison`: alternatives, tradeoffs, positioning, buyer criteria.
- `metric_story`: source-backed chart or KPI card with a few large values.
- `roadmap`: phases, milestones, launch path, dependency gates.
- `risk_register`: blockers, owner/action, severity, mitigation.

Avoid:

- Generic SaaS cards that do not show the product or workflow.
- Decorative icons used as evidence.
- Fake dashboards with unreadable or invented numbers.
- Marketing-page hero composition when the user asked for a tool, report, or
  operational deck.

### Tech Product Bias

For developer tools, agents, infrastructure, or engineering systems:

- Prefer architecture, sequence, and workflow primitives.
- Show files, tools, agents, queues, APIs, or state stores only when sourced.
- Let diagrams stay quiet and utilitarian. Dense but organized is better than
  cinematic.
- Reserve dark neon palettes for launch/demo decks, not reports or design docs.

### Business Report Bias

For status, roadmap, or executive updates:

- Use source-bound charts, timelines, risk tables, and milestone views.
- Keep the visual system restrained; the point is fast scanning.
- Show deltas, blockers, and decisions separately.
- Do not make a heroic cover compensate for weak operational content.

### Editorial Creative Bias

For portfolio, brand, or concept decks:

- Image generation may carry more of the visual work.
- Exact factual claims remain source-bound.
- Use fewer slides with stronger visual rhythm.
- Do not import this looseness into SCI or operational reports.

---

## Quality Gates

Before rendering:

- SCI content slide: `claim`, `evidence_refs`, `mechanism`, `uncertainty`, and
  `primitive` are present.
- Product content slide: `object`, `audience`, `value`, `support`, and
  `next_action` are present.
- Quantitative slide: real numbers are bound as data, not described only in prose.
- Compiled image2 prompt includes mechanism/scene grammar, not only a topic.
- Exact labels are short enough to render as large tokens.
- Dense data tables are removed or compressed into a simple visual metaphor.
