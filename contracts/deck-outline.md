# Deck Outline Contract

`visual-deck` owns the canonical deck outline shape. The outline is YAML in a
Markdown wrapper with these top-level keys:

- `title`
- `style`
- `size`
- `content_mode`
- `slides`

Each slide has:

- `role`
- `title`
- `captions`
- `source_refs`

Supported roles:

- `cover`
- `section`
- `content`
- `closing`

`source_refs` is provenance metadata and must not be rendered into the slide image.

`visual-deck` should not derive an outline directly from a `visual-plan` prompt package.
For source-backed decks, it first creates `deck_content_brief.md` with allowed claims,
unknowns, and narrative beats. The outline is derived from that brief.

Topic-only decks are concept drafts. They must use `source_refs:
["assumption:topic-only"]` for generated content and avoid factual specifics unless the
user supplies sources.
