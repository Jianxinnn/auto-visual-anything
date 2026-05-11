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
  outline.md
  last_run.json
  prompts/
  slides/
  revisions.log
```

Run-state directories are outputs. They should not be committed to the suite
repository or copied into skill install units.
