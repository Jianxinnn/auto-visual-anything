# Generation Parameter Contract

`figforge-gen` owns the authoritative generation parameters and API behavior.

Common handoff fields:

- `prompt`
- `mode`
- `image`
- `mask`
- `size`
- `quality`
- `background`
- `output_format`
- `n`
- `input_fidelity`
- `out_dir`

API configuration, token handling, endpoint fallback, Python detection, and
timeout calculation remain inside `skills/figforge-gen`.
