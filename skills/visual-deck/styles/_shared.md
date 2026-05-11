# Shared Slide Rules

Injected before every style file.

## Output

Render one slide-style image, not a grid, thumbnail strip, or mockup. All slides in a run
share the chosen size.

Size mapping:

- `1536x1024`: 4:3 landscape default
- `3840x2160`: 16:9 4K
- `1024x1024`: square
- `1024x1536`: 3:4 portrait/poster

## Hard Constraints

1. At most one big title plus at most two short captions.
2. Title ≤10 English words or ≤8 Chinese characters.
3. Each caption ≤14 English words or ≤16 Chinese characters.
4. Do not render paragraphs, code, dense tables, long math, footnotes, dates, real-person
   photos, real brand logos, social handles, watermarks, QR codes, or personal data.
5. Keep an 8% safe margin.
6. If exact text cannot render cleanly, leave a clean placeholder rectangle rather than
   wrong text.

## Five Anchors

One style template fixes these across the whole deck:

- palette: exactly 3 colors unless the style says otherwise
- typography: display + body families
- layout grid
- recurring motif
- background type

Cosmetic revisions stay inside these anchors.

## Role Priority

- `cover`: deck title
- `section`: section number + title
- `content`: slide title; captions are support
- `closing`: closing phrase

Remove visual elements that compete with the protagonist.

## Avoid

Thin accent line directly under the title, three identical icon row, handshake/globe hero,
vector people, fake 3D/chrome/lens flare/glow halos, rainbow gradients, literal growth
arrow, sticker emoji, faux watercolor on corporate slides.

Style files may explicitly override one item; otherwise do not add these cues.

## CJK + Latin

For mixed CJK/Latin titles, keep the total visible glyph count within the title budget.
Rare CJK characters should become clear placeholders, not guessed characters.
