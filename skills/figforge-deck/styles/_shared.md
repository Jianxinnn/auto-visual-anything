# Shared rules — injected into EVERY per-slide prompt

These rules sit ABOVE the style-specific block in the compiled prompt. They are the
universal contract that holds whether the style is academic, business, technical, or
editorial. The orchestrator MUST include this file verbatim in every per-slide prompt.

---

## What you are rendering

ONE slide-style image. A single rectangular composition that looks like a single
presentation slide. Not a slide grid, not a thumbnail strip, not a multi-pane mock-up.

Aspect ratio matches the requested image size:

- `1536x1024` → 4:3 landscape (default for slide decks)
- `3840x2160` → 16:9 widescreen 4K
- `1024x1024` → square (for social-post-style decks only)
- `1024x1536` → 3:4 portrait (for poster-style handouts)

Whatever the size, every slide in the deck shares it.

---

## Hard constraints — never relax

1. Bake **at most one big title** plus **at most two short caption lines** into the image.
2. Title length: ≤ 10 English words OR ≤ 8 Chinese characters. Truncate if longer.
3. Each caption: ≤ 14 English words OR ≤ 16 Chinese characters.
4. Never attempt to render: paragraphs, code blocks, data tables, math longer than 6
   characters, footnotes, page numbers, dates, real-person photos, real brand logos,
   social-media handles, watermarks, or QR codes.
5. Margins: respect an 8% safe area; nothing crucial in the outer 8% of any edge.
6. Spelling must match the title and captions exactly. If the model cannot render a
   character cleanly, render a clear placeholder rectangle in the same position rather
   than producing wrong text.

---

## Visual consistency across the deck (the five anchors)

The orchestrator picks ONE style template per run. That template fixes five anchors that
MUST stay constant across every slide of the same deck:

1. **Color palette** — exactly 3 colors (1 base, 1 secondary, 1 accent). No additions.
2. **Typography** — one display family for titles + one body family for captions.
3. **Layout grid** — the spatial scheme (centered hero / 2-column / ⅓-⅔ asymmetric / etc).
4. **Recurring motif** — one decorative mark repeated on every slide of the deck (a thin
   rule, a corner bracket, a tick scale, a numeral badge, etc).
5. **Background type** — solid / soft gradient / paper texture / inverted block.

When the user asks to regenerate one slide for cosmetic reasons, do NOT change any of
these anchors. Cosmetic edits live within the anchors, not against them.

---

## Per-role typographic protagonist

Each slide has ONE typographic protagonist:

- `cover` — the deck title
- `section` — the section numeral + section title together act as one block
- `content` — the slide title (the captions are decoration, never the lead)
- `closing` — the closing word ("Thanks", "Q & A", "Discussion", "Fin", "Next")

Everything else in the composition serves the protagonist. If a decorative element fights
the protagonist for attention, remove the decorative element.

---

## Forbidden output cues (anti-AI-aesthetic)

These are signature "AI-generated slide" tells. Avoid all of them:

- A thin accent line directly under the title (the canonical AI-slide tell)
- A row of three identical icons across the slide (the corporate-cliché grid)
- A "team handshake" or globe-with-network as a hero illustration
- "Vector cartoon" people
- Fake-3D bevels, chrome, lens flare, glow halos
- Rainbow / multi-stop gradients
- A literal upward arrow that says "growth"
- Sticker-style emoji baked into the slide
- Faux-brushstroke "watercolor" effects on a corporate slide

If the style template explicitly invokes one of the above (e.g., a gradient backdrop in
business-intro), follow the style template — the style is the authority. But do not add
these on your own initiative.

---

## CJK + Latin mixed text note

`gpt-image-2` renders short Latin text reliably and short CJK text mostly reliably. For
mixed-script titles (e.g., a Chinese title with a parenthetical English term), keep the
total to ≤ 8 visible glyphs. If the title contains rare CJK characters, render them as a
clear placeholder rectangle rather than a guessed wrong character.
