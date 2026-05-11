# FigForge Architecture

FigForge separates runtime concerns by skill.

`figforge-plan` owns evidence handling and prompt package construction. It reads
source material, classifies the input, marks unknowns, and emits a grounded
figure plan.

`figforge-gen` owns generation execution. It resolves API configuration,
performs preflight checks, selects Python, computes timeouts, calls the image
backend, and writes image files.

`figforge` owns single-figure orchestration. It decides whether planning is
needed, delegates planning and generation to the public skill interfaces, and
keeps per-run state under `.figforge/`.

`figforge-deck` owns slide-image orchestration. It chooses deck style, creates or
validates an outline, compiles one prompt per slide, delegates generation to
`figforge-gen`, and keeps per-run state under `.figforge-deck/`.

Repo-root `contracts/` documents shared interfaces for maintainers. Runtime
skills should carry any files they need inside their own install directories.
