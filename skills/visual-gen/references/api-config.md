# visual-gen API Config

## Priority

1. CLI: `--api-base`, `--api-key`, `--api-key-env`, `--model`
2. Env: `VISUAL_GEN_API_BASE`, `VISUAL_GEN_API_KEY`, `VISUAL_GEN_MODEL`
3. Config:
   - `$VISUAL_GEN_CONFIG`
   - `$XDG_CONFIG_HOME/visual-gen/config.toml`
   - `~/.config/visual-gen/config.toml`
   - `~/.visual-gen/config.toml`
4. Codex: `~/.codex/config.toml` + `~/.codex/auth.json`
5. Claude Code: `~/.claude/settings.json`

Migration compatibility remains: `FIGFORGE_GEN_*` env vars and `figforge-gen` config paths
are read after the new names.

## Config Fields

Only API connection fields belong in config:

- `base_url` / `api_base`
- `api_key` / `token`
- `api_key_env` / `token_env`
- `model`

Do not store generation/local fields such as `size`, `quality`, `output_format`, or
`out_dir`.

## Atomicity

For one call, `base_url` and token must come from the same source. Do not mix:

- Codex token with independent `base_url`
- independent token with Codex/Claude `base_url`
- temporary exports from another source unless the user explicitly asks

If config uses `api_key_env`, source the user's shell and let the script resolve it. Do not
manually splice a token into another source.

## Preflight

Before first generation in a session:

```bash
zsh -lc 'source ~/.zshrc >/dev/null 2>&1 || true; cd "<task-cwd>" || exit 1; python_cmd=$(bash "<skill-dir>/scripts/choose_python.sh") || { echo "未找到可用 Python 3.11+"; exit 1; }; python_argv=(${=python_cmd}); "${python_argv[@]}" "<skill-dir>/scripts/visual_gen.py" --show-config'
```

Check only:

- `ok`
- `source`
- `base_url`
- `model`
- `token_present`

Never print, read, copy, or concatenate a full token.

If token is missing, first source the relevant shell config; if still missing, ask the user
to set the named environment variable.

## Recommended Setup

`~/.config/visual-gen/config.toml`:

```toml
[api]
base_url = "https://your-api-base/v1"
api_key_env = "VISUAL_GEN_API_KEY"
model = "gpt-image-2"
```

Shell:

```bash
export VISUAL_GEN_API_KEY="sk-..."
```

Use a versioned API base such as `https://.../v1`; the script appends `/responses`,
`/images/generations`, or `/images/edits`.

## Endpoint Fallback

Streaming Responses is preferred. Fallback to Images when:

- Responses returns compatibility status `400/404/405/415/422`
- backend says `gpt-image-2` is Images-only
- edit request includes `mask`
- user passes `--no-stream`

If only `VISUAL_GEN_API_KEY` is set without a matching independent `base_url`, the script
does not treat it as a complete config; it may still fall back to Codex/Claude settings.
