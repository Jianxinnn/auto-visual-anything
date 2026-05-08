# Image Generation Handoff

**Purpose**: Capture the operational details for handing off a FigureFoundry prompt
package to an image-generation tool. Read this file only when the user asks
FigureFoundry to both compile the prompt **and** generate the image.

For prompt-only workflows, ignore this file.

---

## Two-Stage Workflow

When the user wants the prompt produced *and* an image generated in the same turn:

1. Complete FigureFoundry analysis and compile the full `image_prompt` package first.
2. Extract the final core image prompt plus recommended size/quality/format/aspect-ratio.
3. Invoke the available image-generation skill/tool with **its own documented configuration flow**.
4. Do not read, copy, transform, or mix API keys between FigureFoundry and the image tool.
5. Do not override the image tool's configured API base or token unless the user explicitly asks.
6. Report both the prompt package (location or content summary) and the generated image path.

---

## Boundaries with `gen-images`

When the available image tool is `gen-images`:

- Run `gen-images --show-config` as a preflight in the same shell that will perform generation.
- If `GEN_IMAGES_API_KEY` is configured in `~/.zshrc`, source `~/.zshrc` in that same shell.
- Never inject Codex- or Claude-side credentials into `GEN_IMAGES_API_KEY`. The image
  skill owns its runtime configuration.
- If preflight fails, return the prompt package only and explain what configuration is missing.

---

## Failure Modes

- Image-generation tool unavailable → return only the prompt package; do not silently skip the user's request.
- Tool reports auth/billing failure → surface the error verbatim; do not retry with adjusted credentials.
- Tool returns unusable output (clipped, watermarked, wrong size) → keep the prompt package and recommend post-edit in Figma/Illustrator/PowerPoint/SVG.
