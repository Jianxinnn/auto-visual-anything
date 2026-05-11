# Run State Contract

Single-figure runs use:

```text
<task_cwd>/.visual-anything/<run-id>/
  prompt_package.md
  last_image.json
  revisions.log
```

Slide-image deck runs use:

```text
<task_cwd>/.visual-deck/<run-id>/
  deck_content_brief.md
  outline.md
  last_run.json
  prompts/
  slides/
  revisions.log
```

`last_run.json` records the render mode. For deck runs, default values are
`render_mode: "parallel"` and `max_concurrency: 4`.

Run-state directories are outputs. They should not be committed to the suite
repository or copied into skill install units.
