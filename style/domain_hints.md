# Domain Hints

Lightweight domain advisory layer. **Source-type defaults (in each sub-skill) lead;
this file only intervenes where a domain has strong visual conventions or strong
visual taboos.** Do not treat the table below as a rigid template — favor it as
soft guidance, then drop the `Avoid` items into the renderer's negative prompt.

---

## When to read this file

Read when:
- The source has a clear domain signal (paper venue, repo dependencies/vocabulary,
  diagram notation, algorithm domain language).
- The renderer needs a domain-aware negative prompt.

Skip when:
- The source-type default already covers it and no domain-specific cliché applies.
- The user explicitly asks for a generic editorial style.

---

## Universal anti-cliché list

Always include these in the negative prompt, regardless of domain:

- Cartoon robots, anthropomorphic AI brains, "intelligence" glow halos
- Glowing sci-fi dashboards, neon HUDs, cyberpunk grids
- Generic cloud icons used purely as decoration
- DNA double-helix used as background filler
- Hooded hackers, matrix-style number rain, lock-icon pile
- Fake LaTeX, scientific-looking but garbled symbols
- Generic test-tube / flask iconography as a stand-in for "science"
- Collage / scrapbook layouts
- 3D pie charts, decorative gauge dials
- Stock-photo overlays, lens flares, dramatic lighting
- Faux-3D extrusions on flat diagrams
- Wordcloud-style decorative typography

---

## Domain hint table

| Domain | Default palette | Favor | Avoid |
|--------|-----------------|-------|-------|
| **ML / DL / agents** | `sci-light`, `data-violet` | tensor block notation, encoder–decoder bottleneck, attention matrix, training loop, ablation grid | anthropomorphic AI, generic brain icon, "intelligence" halo |
| **Bio / wet-lab / clinical** | `bio-evidence` | gel/blot motifs, flow-cytometry style, pathway maps, multi-panel evidence | decorative double helix, generic test tubes, gradient brain rendering |
| **Structural / molecular biology** | `bio-evidence` | ribbon / cartoon backbone, surface, ligand stick, italic residue codes (`Ser123`), Greek letters for secondary structure | box-and-arrow architecture (this field doesn't draw that way), cartoon DNA decoration |
| **Chemistry / mechanism** | `bio-evidence` or `sci-light` | reaction arrows with correct semantics (→ vs ⇌ vs curly electron-pushing), structural formulas, mechanism step blocks | random molecule background fill, misused reaction-arrow type, decorative beakers |
| **Systems / infra / networking** | `systems-blue` | layered stacks, sequence diagrams, packet flow, queue/topic/broker icons, host/container glyphs | generic cloud-stack collage, SaaS-template flowcharts |
| **Security / verification / risk** | `security-amber` | adversary model, protocol ladder diagram, threat tree, trust boundary, gate/decision points | hooded hacker, lock-icon pile, matrix rain |
| **Data / analytics / knowledge graphs** | `data-violet` | DAG, knowledge graph, heatmap, small multiples, treemap, direct labeling | 3D pie, decorative gauge dashboards, faux-BI screenshots |
| **Physics / formal sciences / math** | `sci-light` | Feynman diagrams (where applicable), energy levels, commutative diagrams, detector schematics, coordinate frames | fake LaTeX, fabricated physics symbols, decorative atom icons |
| **Geo / climate / astro** | `sci-light` | maps, cross-sections, time series, light curves, spectra, isolines | decorative globe icons, fake satellite imagery, stock weather symbols |
| **HCI / product / UX** | `product-muted` | user flow, wireframe-feel panels, study procedure timeline, screen sketches | hyper-3D phone mockups, dramatic device renders, ad-style hero shots |
| **Robotics / control systems** | `systems-blue` | block diagram + feedback loop with control labels, coordinate frames, hardware schematic, sensor/actuator glyphs | anthropomorphic robot, generic robotic-arm clipart, cinematic mech renders |

---

## How to apply

1. **Detect domain** from source signals (paper venue, repo dependencies, vocabulary,
   diagram notation). If detection is weak, skip this file.
2. **Take the row's `Avoid` list** and merge it into the renderer's domain-specific
   negative prompt block.
3. **Take the row's `Favor` list** as soft guidance for diagram primitives in the
   prompt — these are suggestions, not requirements.
4. **If no row clearly fits**, fall back to the source-type default. Do not force-fit.

If the source crosses domains (e.g., bio + ML, security + systems), merge the `Avoid`
lists from all matching rows; do not pick only one. For `Favor`, prefer the dominant
domain and pull individual primitives from the secondary as needed.

---

## What this file does NOT do

- It does not override the source-type default (sub-skill knows the structural
  composition; this file only nudges visual taste).
- It does not prescribe a fixed iconography library — `Favor` items are examples,
  not a closed set.
- It does not enforce a venue style (Nature vs IEEE etc.) — that's outside scope.
