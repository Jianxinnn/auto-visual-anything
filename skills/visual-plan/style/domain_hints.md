# Domain Hints

Advisory layer for domain-specific primitives and anti-cliches. Source-type defaults still
lead; use this only when domain cues are strong or a renderer needs a domain-aware negative
prompt.

## Universal Avoid

Cartoon robots, AI brains/halos, neon HUDs, decorative cloud icons, DNA filler, hooded
hackers, matrix rain, fake LaTeX/garbled symbols, generic test tubes, scrapbook layouts,
3D pies, gauges, stock-photo overlays, lens flares, faux-3D extrusions, wordclouds.

## Table

| Domain | Palette | Favor | Avoid |
|---|---|---|---|
| ML/DL/agents | `sci-light`/`data-violet` | tensor blocks, encoder-decoder, attention matrix, training loop, ablation grid | robot/brain/halo |
| Bio/wet-lab/clinical | `bio-evidence` | gel/blot motifs, flow cytometry, pathway maps, evidence panels | decorative DNA, generic test tubes |
| Structural biology | `bio-evidence` | ribbon/backbone, surface, ligand sticks, residue codes, secondary-structure symbols | generic box-arrow architecture, DNA wallpaper |
| Chemistry | `bio-evidence`/`sci-light` | correct reaction arrows, formulas, mechanism blocks | random molecule fills, wrong arrows, beakers |
| Systems/infra/networking | `systems-blue` | layers, sequence diagrams, queues, host/container glyphs | cloud-stack collage, SaaS template flowcharts |
| Security/verification | `security-amber` | adversary model, protocol ladder, threat tree, trust boundary, gates | hacker/lock piles/matrix rain |
| Data/analytics/graphs | `data-violet` | DAG, KG, heatmap, small multiples, treemap, direct labels | 3D pies, gauges, fake BI dashboards |
| Physics/math | `sci-light` | Feynman/energy/detector/coordinate diagrams where appropriate | fake LaTeX, decorative atom icons |
| Geo/climate/astro | `sci-light` | maps, cross-sections, time series, spectra, isolines | decorative globes, fake satellite/weather symbols |
| HCI/product/UX | `product-muted` | user flows, wireframe panels, study timelines, screen sketches | 3D phone mockups, ad-style device renders |
| Robotics/control | `systems-blue` | block diagrams, feedback loops, coordinate frames, hardware/sensor glyphs | anthropomorphic robots, cinematic mech renders |

## Apply

1. Detect domain from vocabulary, dependencies, venue, or diagram notation.
2. Merge matching `Avoid` items into the negative prompt.
3. Use `Favor` as optional primitives, not mandatory content.
4. For cross-domain sources, merge avoid lists; choose favor primitives from the dominant
   domain and selectively borrow from secondary domains.
5. If weak/no match, skip this file.
