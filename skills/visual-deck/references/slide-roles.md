# Slide roles

Every slide in `visual-deck` has exactly **one** narrative role. The role says where the
slide sits in the deck story. The generation spec's `visual_primitive` says what image2
should draw for that slide.

Examples:

- `role: content` + `visual_primitive: pipeline`
- `role: content` + `visual_primitive: risk_map`
- `role: content` + `visual_primitive: mechanism_panel`
- `role: cover` + `visual_primitive: product_hero`

This taxonomy exists because image-gen (B mode) breaks down once a slide tries to carry
many distinct things. Four roles guarantee each slide has ONE typographic protagonist
plus at most two supporting captions.

---

## cover

The first slide of a deck. Sets identity: deck title and (optionally) a subtitle line
naming the venue, presenter, period, or one-line tagline.

| Field | Required? | Budget |
|---|---|---|
| `title` | yes | ≤ 10 EN words / ≤ 8 CN chars (the deck title) |
| `captions[0]` | optional | ≤ 14 EN words / ≤ 16 CN chars (one subtitle line) |
| `captions[1]` | not used | ignored on cover slides |

Renders once per deck (always the first slide). The orchestrator inserts a default
cover if the user-supplied outline lacks one.

---

## section

A divider that signals a topic change. Acts as a chapter break inside the deck.

| Field | Required? | Budget |
|---|---|---|
| `title` | yes | ≤ 10 EN words / ≤ 8 CN chars (the section name) |
| `captions[0]` | optional | ≤ 14 EN words / ≤ 16 CN chars (one-line section description) |
| `section_number` | injected by orchestrator | "01" / "02" / ..., zero-padded |

The orchestrator MUST inject a zero-padded sequence number across section slides — they
are numbered in encounter order ("01" for the first section divider, "02" for the
second, etc), independent of the slide's overall position number.

0–N per deck (typically 2–4). Decks shorter than 5 slides usually do not need any section
divider; decks with 8+ slides almost always do.

---

## content

A regular slide carrying a single point. The bulk of the deck.

| Field | Required? | Budget |
|---|---|---|
| `title` | yes | ≤ 10 EN words / ≤ 8 CN chars (the point in plain English / Chinese) |
| `captions[0]` | optional | ≤ 14 EN words / ≤ 16 CN chars (the supporting specific) |
| `captions[1]` | optional | ≤ 14 EN words / ≤ 16 CN chars (a second supporting specific) |

Rules of thumb:

- The title states the conclusion or claim, NOT the topic — "Diffusion beats GANs by 4 FID"
  is a content title; "Diffusion vs GANs" is a section title
- Captions add one quantified specific each ("FID 6.3 vs 10.1 on COCO", "trained on 8 GPUs")
  rather than a second restatement of the title
- If a slide needs more than 2 captions worth of content, split it into two content slides
  rather than overflowing the budget

Typically 4–8 per deck.

---

## closing

The final slide. Signals the end (Q&A, thanks, contact placeholder, references, "discussion").

| Field | Required? | Budget |
|---|---|---|
| `title` | yes | a short closing word or phrase ("Thanks", "Discussion", "Q & A", "Fin", "References") |
| `captions[0]` | optional | one supporting line ("Open questions", "Reach me at …" — placeholder only) |
| `captions[1]` | not used | ignored on closing slides |

Renders once per deck (always the last slide). The orchestrator inserts a default closing
if the user-supplied outline lacks one. NEVER bake a real email, phone number, or
social-media handle into the image — use a placeholder mark.

---

## Why exactly four roles

Because the image model can render ONE strong typographic block + decorative supporting
elements per image, reliably. More than that and the model starts:

- garbling text
- inventing new visual elements to fill space
- losing the style anchors the orchestrator carefully fixed

Four roles map naturally onto the four "slide intentions" a presentation actually needs:
identify (cover) → divide (section) → say one thing (content) → end (closing). Anything
denser than this is asking image-gen to do what a real `.pptx` editor does — wrong tool.
