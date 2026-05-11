# Deck Outline Contract

`figforge-deck` owns the canonical deck outline shape. The outline is YAML in a
Markdown wrapper with these top-level keys:

- `title`
- `style`
- `size`
- `slides`

Each slide has:

- `role`
- `title`
- `captions`

Supported roles:

- `cover`
- `section`
- `content`
- `closing`

`figforge-deck` may derive an outline from a `figforge-plan` prompt package, but
it must preserve the evidence/unknown distinction from the planning layer.
