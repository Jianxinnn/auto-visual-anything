# Outline Schema

`visual-deck` reads/writes:

```text
<task_cwd>/.visual-anything/runs/deck/<run-id>/outline.md
```

The file is YAML inside a Markdown wrapper.

## Shape

````markdown
# Deck Outline

```yaml
title: "Deck Title"
style: academic-discussion
size: 1536x1024
content_mode: source
domain_mode: sci-research
generation_spec_refs:
  - slide_generation_specs/slide-01.md
slides:
  - role: cover
    title: "Deck Title"
    captions: ["subtitle"]
    source_refs: ["source:abstract"]
  - role: content
    title: "Key point"
    captions: ["short support"]
    visual_primitive: pipeline
    source_refs: ["paper:results"]
  - role: closing
    title: "Discussion"
    captions: ["Q & A"]
    source_refs: ["deck convention"]
```
````

Top-level keys: `title`, `style`, `size`, `content_mode`, optional `domain_mode`,
optional `generation_spec_refs`, and `slides`.

Each slide has `role`, `title`, `captions`, `source_refs`, and optional
`visual_primitive`. `captions` and `source_refs` are always lists. `source_refs` is
provenance metadata and must not be rendered.

## Validation

- first slide is `cover`; insert a default if missing
- last slide is `closing`; insert a default if missing
- `style` matches `styles/*.md`
- `size` is passed through to `visual-gen`; common values: `1536x1024`, `3840x2160`,
  `1024x1024`, `1024x1536`
- role is `cover`, `section`, `content`, or `closing`
- title ≤10 English words or ≤8 Chinese characters
- captions length 0-2; each ≤14 English words or ≤16 Chinese characters
- slide count ≤12 unless the user opts in
- `content_mode: source` content slides have real `source_refs`
- `content_mode: topic` uses `source_refs: ["assumption:topic-only"]` and no factual
  specifics

Only rules 1-2 may be auto-corrected. For other failures, ask one targeted question. Do
not silently truncate user-authored text.

## Source Material

Use `visual-plan` to extract evidence, then create `deck_content_brief.md`. The brief,
not the single-figure prompt package, feeds outline drafting.

Rules:

- main claim -> cover title
- major sections -> optional `section` slides
- one supported content beat -> one `content` slide
- quantified specifics -> captions only if sourced
- unknowns become `(needs verification)` or are omitted
- every rendered title/caption gets a `source_refs` entry

## Topic or User Outline

Topic-only decks use a 6-slide concept skeleton unless the user asks otherwise:
cover, optional section, three content slides, closing. All generated content is
`assumption:topic-only`.

User outlines are preserved. Missing `source_refs` become `["user-outline"]`; invalid
style/length/budget issues require one question.

## Revisions

The outline is canonical:

- cosmetic: do not edit outline
- content: update brief if claim changes, then outline/spec for affected slides
- restyle: update top-level `style`, full re-render
- restructure: insert/remove/merge, renumber, re-render affected slides

Revalidate before rendering.
