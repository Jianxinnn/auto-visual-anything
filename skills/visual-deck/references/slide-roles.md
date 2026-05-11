# Slide Roles

Every slide has exactly one narrative role. Role controls story position; the generation
spec's `visual_primitive` controls what image2 draws.

## `cover`

First slide. Carries identity.

| Field | Budget |
|---|---|
| `title` | ≤10 English words or ≤8 Chinese characters |
| `captions[0]` | optional subtitle, ≤14 English words or ≤16 Chinese characters |
| `captions[1]` | unused |

The orchestrator inserts a default cover if missing.

## `section`

Chapter divider.

| Field | Budget |
|---|---|
| `title` | section name, ≤10 English words or ≤8 Chinese characters |
| `captions[0]` | optional one-line section description |
| `section_number` | injected as `01`, `02`, ... in encounter order |

Use only when the deck needs topic breaks; short decks often need none.

## `content`

Regular slide carrying one point.

| Field | Budget |
|---|---|
| `title` | conclusion/claim, not merely topic |
| `captions[0..1]` | up to two short specifics |

If content needs more than two captions, split it into multiple slides.

## `closing`

Final slide: `Thanks`, `Discussion`, `Q & A`, `References`, `Next`, etc.

| Field | Budget |
|---|---|
| `title` | short closing phrase |
| `captions[0]` | optional placeholder/support line |
| `captions[1]` | unused |

Never bake real email, phone number, social handle, QR code, or personal data into the
image.

## Constraint

Image generation reliably supports one typographic protagonist plus at most two captions.
Anything denser belongs in a real `.pptx`, not a slide image.
