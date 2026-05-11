# visual-gen Fields

API configuration lives in `api-config.md`.

## Task Types

- Text-to-image: default `POST /v1/responses` streaming, fallback to
  `POST /v1/images/generations`.
- Edit: default `POST /v1/responses`, fallback to `POST /v1/images/edits`; using `mask`
  forces Images edit fallback.

Image source plus edit intent means edit.

## Required

| Task | Required | If missing |
|---|---|---|
| Text-to-image | `prompt` | ask, do not run |
| Edit | `prompt` + image source | ask, do not run |

## Optional API Fields

| Field | Default/Rule |
|---|---|
| `model` | `gpt-image-2`; user explicit only |
| `response_format` | fixed `b64_json` |
| `stream` | true unless `--no-stream` |
| `size`, `quality`, `background`, `output_format` | explicit or conservative inference |
| `output_compression` | only explicit, jpg/jpeg/webp |
| `partial_images` | streaming default 1; user explicit only |
| `n` | default 1 |
| `moderation` | user explicit only |
| `input_fidelity` | edit only |

Local-only: `out_dir`, default
`<task_cwd>/.visual-anything/runs/gen/<run-id>`. It never enters API payload.

Do not write generation/local fields such as `size`, `quality`, `output_format`, or
`out_dir` into API config files.

## Priority

1. User explicit field value
2. Clear natural-language requirement
3. Conservative LLM inference
4. Script default

Do not remove inferred semantics from the prompt; pass them as parameters only.

## Natural-Language Mapping

### `size`

| Text | Value |
|---|---|
| `1024x1024`, `1:1` | `1024x1024` |
| `1024x1536`, `3:4` | `1024x1536` |
| `1536x1024`, `4:3` | `1536x1024` |
| `2048x2048` | `2048x2048` |
| `3840x2160`, `16:9`, `4k横向` | `3840x2160` |
| `2160x3840`, `9:16`, `4k竖向` | `2160x3840` |
| `auto` | `auto` |

Infer size only when use case is clear:

- avatar/icon/logo/sticker/product main image -> `1024x1024`
- poster/cover/portrait/vertical composition -> `1024x1536`
- banner/video cover/demo background/landscape -> `1536x1024`
- mobile wallpaper/short-video cover -> `2160x3840`
- desktop wallpaper/explicit 4K or 16:9 -> `3840x2160`

Do not pick 4K only because the prompt says "高清" or is complex.

### Other fields

- `quality`: `高清/高质量/商用/主视觉/壁纸/海报/产品图` -> `high`; `草图/快速预览/低成本试稿` -> `low`.
- `background`: `透明背景/无背景/抠图` -> `transparent`; `白底` -> `white`; `黑底` -> `black`.
- `output_format`: `png/jpg/jpeg/webp`; transparent defaults to `png` if unspecified.
- `n`: explicit count; `多方案/几个版本` without count -> 3; otherwise 1.
- `output_compression`: explicit compression request plus jpg/jpeg/webp; do not guess a ratio.
- `input_fidelity`: edit requests preserving face/person/subject/product -> `high`; major redraw -> unset unless user specifies.

Do not infer `model`, `moderation`, or `partial_images`.

## Timeout

Before Bash-calling `scripts/visual_gen.py`, compute timeout from extracted `size` and `n`:

| Condition | Per image |
|---|---|
| parseable `WxH` and `W*H >= 8,000,000` | `900000` ms |
| all other cases | `600000` ms |

`timeout = per_image * n` because the script calls images serially for `n > 1`. Cap at the
tool maximum when needed.

## Prompts

| Missing | Ask |
|---|---|
| text-to-image prompt | `请补充图片提示词,例如你想生成什么画面。` |
| edit image source | `请提供要编辑的图片来源:1)本地路径 2)图片 URL / data URL` |
| edit prompt | `请补充修改要求,例如你想把图片改成什么效果。` |

## User Output

Success:

```text
图片已生成, 图片路径: <路径>
实际使用的关键参数: model=..., size=..., quality=..., output_format=..., n=..., stream=..., out_dir=...
```

Failure:

```text
生成失败: <简短错误原因>
```
