# Renderer: Image Prompt Package

**Purpose**: Convert the analyzed figure plan from any sub-skill into a polished,
tool-agnostic image-generation prompt package for scientific figures.

Use this renderer by default when the user wants a prompt, wants to use an external
image-generation tool, or did not explicitly ask for deterministic HTML/SVG.

---

## Renderer Contract

Input: A structured content block from any sub-skill, with:
- `input_type`: code_repo / research_paper / diagram_image / algo_text / hybrid / design_request
- `figure_goal`: main figure / architecture diagram / graphical abstract / poster / schematic
- `evidence`: facts directly supported by the source
- `assumptions`: visual or design assumptions
- `unknowns`: important missing details
- `nodes`, `edges`, `panels`, `labels`, `callouts`, and `visual_hierarchy`

Output: A copy-ready prompt package, not an image.

---

## Output Template

Always return this exact structure:

```markdown
# FigureFoundry Prompt Package

## 1. Figure Brief
[1 short paragraph describing the scientific message and intended venue/style.]

## 2. Core Image Prompt
[The main prompt the user can paste into an image-generation tool.]

## 3. Layout Specification
[Panel-by-panel spatial layout, reading order, main visual hierarchy, arrows, grouping.]

## 4. Label Priority
High-priority labels:
- [...]

Secondary labels:
- [...]

Avoid rendering as tiny text:
- [...]

## 5. Style Direction
[Vector style, palette, typography, line weight, icon rules, whitespace, what should feel premium.]

## 6. Negative Prompt
[What to avoid: visual cliches, inaccurate elements, clutter, bad typography, cartoons, etc.]

## 7. Recommended Generation Settings
- Aspect ratio:
- Size:
- Quality:
- Background:
- Output format:
- Text strategy:

## 8. Post-Edit Notes
[Precise labels, arrows, and source-specific details to add or correct in Figma/Illustrator/PPT/SVG.]

## 9. Source Discipline
Evidence used:
- [...]

Assumptions:
- [...]

Unknowns:
- [...]
```

---

## Prompt Writing Rules

### Preserve Scientific Structure

The prompt must encode the actual source structure:
- Do not replace specific mechanisms with generic "AI workflow" language.
- Keep source-derived node names, steps, and relationships where they matter.
- If the source is a repo, reflect evidenced modules and data flow.
- If the source is a paper, reflect the paper's contribution and mechanism.
- If the source is a diagram, preserve or intentionally transform its visible structure.

### Compress Labels for Image Models

Image models often distort dense text. Split labels into tiers:

- **High-priority labels**: 5-10 labels that must appear large and readable.
- **Secondary labels**: labels that can appear as chips, headings, or short captions.
- **Avoid tiny text**: long lists, exact citations, code paths, or dense field names.

For exact publication labels, recommend post-editing. A strong image prompt should ask the
model to reserve clean label spaces rather than forcing every small label into the raster.

### Make the Visual Hierarchy Explicit

Every prompt must state:
1. The primary visual claim.
2. The dominant visual element.
3. The secondary supporting elements.
4. What must look subordinate.

Example:

```
The persistent research-state layer is the visual foundation and novelty; the closed-loop
engine sits above it; tools and agents are smaller routed resources, not the main claim.
```

### Use Venue-Specific Style Carefully

For scientific papers, prefer:
- clean vector schematic
- white or very light background
- restrained blue/teal/green accents
- amber/red only for warnings, blockers, or failed gates
- thin gray strokes
- professional sans-serif typography
- minimal shadows
- precise alignment

Avoid:
- cartoon robots
- glowing sci-fi dashboards
- random DNA backgrounds
- generic cloud icons
- decorative lab clipart
- photorealistic wet-lab scenes unless requested
- excessive gradients or 3D effects

### Tool-Agnostic Prompting

The core prompt should work in GPT image, Midjourney, Ideogram, or Stable Diffusion-like
tools. Do not include tool-specific flags unless the user asks for a specific tool.
Put aspect ratio and size in `Recommended Generation Settings`, not inside the core prompt,
unless the target tool commonly expects it in the prompt.

---

## Recommended Settings Defaults

Choose conservatively:

| Figure Type | Aspect Ratio | Size | Quality | Background |
|-------------|--------------|------|---------|------------|
| Paper main figure | 16:9 or 3:2 | 1536x1024 or higher | high | white/opaque |
| Graphical abstract | 16:9 | 1536x1024 | high | white/opaque |
| Poster | 3:4 | 1024x1536 | high | white/opaque |
| Square social preview | 1:1 | 1024x1024 | medium/high | white/opaque |
| Icon/sticker | 1:1 | 1024x1024 | medium | transparent |

If the user will manually call a service that struggles with high resolution, recommend
generating at `1536x1024` first, then upscaling or redrawing labels manually.

---

## Quality Checklist

Before returning the prompt package, verify:

- [ ] The core prompt has one clear scientific message.
- [ ] The layout is spatially specific enough to guide generation.
- [ ] High-priority labels are few enough to be legible.
- [ ] The negative prompt removes common scientific-figure failure modes.
- [ ] Exact source facts are not mixed with assumptions.
- [ ] Post-edit notes warn about text fidelity when the figure has many labels.
- [ ] The style remains publication-quality, not decorative or generic.
