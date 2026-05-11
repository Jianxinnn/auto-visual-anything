---
name: visual-gen
description: Use when the user requests image generation, text-to-image, image editing, 文生图, 改图, 修改图片, 编辑图片, "使用 gpt-image-2", or `/visual-gen`.
argument-hint: <自然语言需求>
allowed-tools: [Bash, Read]
---

# visual-gen

Calls `gpt-image-2` through CLIProxyAPI for text-to-image and image editing. It owns API
configuration, preflight, Python detection, timeout calculation, and local output paths.

## Resources

- `references/fields.md`: fields, natural-language mapping, conservative inference, timeout
- `references/api-config.md`: config priority, credential atomicity, preflight
- `scripts/visual_gen.py`: API caller
- `scripts/choose_python.sh`: Python 3.11+ detector

## Classify

- Text-to-image: `生成图片`, `文生图`, `画一张图`, `用 gpt-image-2 生成`
- Edit: `修改图片`, `编辑图片`, `改图`, or a prompt with an image source and edit intent

Missing required fields: ask once and do not execute.

| Task | Required |
|---|---|
| Text-to-image | `prompt` |
| Edit | `prompt` + image source (local path, URL, or data URL) |

Optional fields follow this priority:
user explicit value > clear natural-language requirement > conservative LLM inference >
script default. See `references/fields.md`; do not repeatedly ask for optional fields.
Never infer `model`, `moderation`, `partial_images`, or `output_compression` unless the
user explicitly asks.

## Output Directory

`task_cwd` is the user's current project/workspace, not the skill directory, script
directory, `$CODEX_HOME`, or `~/.codex`.

Default:

```text
<task_cwd>/.visual-anything/runs/gen/<YYYYMMDD-HHMMSS>/
```

Relative user paths resolve from `task_cwd`. `--out-dir` is local-only and never enters
the API payload.

## Run

Detect Python:

```bash
python_cmd=$(bash "<skill-dir>/scripts/choose_python.sh") || { echo "未找到可用 Python 3.11+"; exit 1; }
```

In `zsh -lc`, split multi-word output before invoking:

```bash
python_argv=(${=python_cmd})
"${python_argv[@]}" "<skill-dir>/scripts/visual_gen.py" ...
```

Before the first generation in a session, preflight in the same shell that will run
generation:

```bash
zsh -lc 'source ~/.zshrc >/dev/null 2>&1 || true; cd "<task-cwd>" || exit 1; python_cmd=$(bash "<skill-dir>/scripts/choose_python.sh") || { echo "未找到可用 Python 3.11+"; exit 1; }; python_argv=(${=python_cmd}); "${python_argv[@]}" "<skill-dir>/scripts/visual_gen.py" --show-config'
```

Check only `ok`, `source`, `base_url`, `model`, and `token_present`. Never print, read,
copy, splice, or substitute full tokens. On preflight failure, follow
`references/api-config.md` and stop if configuration is still missing.

Compute the Bash tool timeout from `references/fields.md` using `size × n`; the script
calls images serially when `n > 1`.

Generate:

```bash
zsh -lc 'source ~/.zshrc >/dev/null 2>&1 || true; cd "<task-cwd>" || exit 1; python_cmd=$(bash "<skill-dir>/scripts/choose_python.sh") || { echo "未找到可用 Python 3.11+"; exit 1; }; python_argv=(${=python_cmd}); "${python_argv[@]}" "<skill-dir>/scripts/visual_gen.py" --mode generate --prompt "..."'
```

Edit: add `--mode edit --image "..."` and optional `--mask`.

Allowed optional args: `--size --quality --background --output-format --n --moderation
--output-compression --partial-images --input-fidelity --no-stream --model --api-base
--api-key --api-key-env --config --out-dir`.

Use `--no-stream` only when the user asks for non-streaming or while diagnosing endpoint
compatibility.

## Respond

Success JSON has `{"ok": true, "paths": [...], "used_params": {...}}`. Reply:

```text
图片已生成, 图片路径: <路径>
实际使用的关键参数: model=..., size=..., quality=..., output_format=..., n=..., stream=..., out_dir=...
```

List all paths when multiple images are generated. On `{"ok": false}`, reply:

```text
生成失败: <简短错误原因>
```

Keep the response short after execution.
