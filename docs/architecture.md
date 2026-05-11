# Auto Visual Anything Architecture

Auto Visual Anything separates runtime concerns by skill.

`visual-plan` owns evidence handling and prompt package construction. It reads
source material, classifies the input, marks unknowns, and emits a grounded
figure plan.

`visual-gen` owns generation execution. It resolves API configuration,
performs preflight checks, selects Python, computes timeouts, calls the image
backend, and writes image files.

`visual-anything` owns single-figure orchestration. It decides whether planning is
needed, delegates planning and generation to the public skill interfaces, and
keeps per-run state under `.visual-anything/runs/figure/`.

`visual-deck` owns slide-image orchestration. It chooses deck style, creates or
validates an outline, compiles one prompt per slide, delegates generation to
`visual-gen`, and keeps per-run state under `.visual-anything/runs/deck/`.

Direct `visual-gen` calls default to `.visual-anything/runs/gen/`. This keeps
runtime outputs under one ignored root while preserving repo-root `assets/` for
curated, committed documentation images.

Repo-root `contracts/` documents shared interfaces for maintainers. Runtime
skills should carry any files they need inside their own install directories.
