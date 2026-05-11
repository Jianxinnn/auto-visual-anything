# Domain Tendencies

Choose `domain_mode` before outlining. It controls density, evidence burden, and prompt
emphasis.

## Modes

- `sci-research`: papers, lab meetings, algorithms, mechanisms, experiments, evidence.
- `sci-structural`: structural biology, molecular mechanisms, protein design, chemistry.
- `product-marketing`: launch, sales, investor, customer narrative.
- `tech-product`: engineering demo, infra, agent/tool workflow, developer platform.
- `business-report`: status, roadmap, risk review, weekly/monthly reports.
- `editorial-creative`: portfolio, concept board, brand mood.

If two fit, choose the stricter evidence mode.

## SCI

Prioritize traceable claims, mechanism, evidence, and uncertainty.

- text: one title plus ≤2 captions; technical labels short and large (`E79L`, `DHF`)
- prompt: encode mechanism, evidence anchors, warning semantics, anti-cliches
- required on content slides: claim, evidence_refs, mechanism, uncertainty, primitive
- primitives: `state_contrast`, `mechanism_panel`, `pipeline`, `evidence_stack`,
  `quant_chart`, `risk_map`, `decision_loop`

Avoid generic science clipart, decorative DNA, stock lab benches, fake microplots, dense
image-model text, or visuals stronger than the evidence.

Structural biology: show target/anti-target states when selectivity matters; use residue
and ligand labels sparingly and only when sourced; surface missing assays when conclusions
depend on them.

Methods/algorithms: preserve real module/metric names; separate selected-baseline wins,
control-plane improvements, and broad superiority claims.

## Product / Business

Use concrete product, user, workflow, value, risk, or decision objects. More visual drama is
allowed than SCI, but claims remain source-bound.

- text: short headlines/captions, no dense brand/legal/price copy
- required on content slides: object, audience, value, support, next_action
- primitives: `product_hero`, `workflow`, `architecture`, `comparison`, `metric_story`,
  `roadmap`, `risk_register`

Avoid generic SaaS cards, decorative icons as evidence, fake dashboards, and marketing hero
composition for operational decks.

Tech product: prefer architecture, sequence, workflow, files/tools/agents/APIs/state stores
when sourced; keep diagrams quiet and utilitarian for reports.

Business report: use source-bound charts, timelines, risks, milestones, deltas, blockers,
and decisions; keep scanning easy.

Editorial creative: fewer slides, stronger rhythm; do not import this looseness into SCI or
operational reports.

## Quality Gates

- SCI content slide has claim/evidence/mechanism/uncertainty/primitive.
- Product content slide has object/audience/value/support/next_action.
- Quantitative slide binds real numbers as data.
- Prompt includes scene grammar, not only a topic.
- Exact labels are short enough for large rendering.
- Dense tables are removed or compressed into simple visual metaphors.
