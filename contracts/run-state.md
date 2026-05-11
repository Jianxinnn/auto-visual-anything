# Run State Contract

Runtime outputs live under one project-local root:

```text
<task_cwd>/.visual-anything/runs/
```

Single-figure runs use:

```text
<task_cwd>/.visual-anything/runs/figure/<run-id>/
  prompt_package.md
  last_image.json
  revisions.log
```

Slide-image deck runs use:

```text
<task_cwd>/.visual-anything/runs/deck/<run-id>/
  deck_content_brief.md
  outline.md
  last_run.json
  slide_generation_specs/
  prompts/
  slides/
  revisions.log
```

Direct visual-gen runs use:

```text
<task_cwd>/.visual-anything/runs/gen/<run-id>/
  <timestamp>-01.png
  ...
```

`last_run.json` records the render mode. For deck runs, default values are
`render_mode: "parallel"` and `max_concurrency: 4`.

Run-state directories are outputs. They should not be committed to the suite
repository or copied into skill install units. Curated repository documentation
images remain in repo-root `assets/`.
