# Prompt Package Contract

`visual-plan` is the source of truth for prompt package content.

Minimum expected sections for image handoff:

- Figure brief
- Core image prompt
- Layout specification
- Label priority list
- Style direction
- Negative prompt
- Recommended generation settings
- Post-edit notes
- Source discipline / evidence ledger

`visual-anything` may map recommended generation settings into `visual-gen` fields,
but it must not fabricate missing evidence or bypass the `visual-plan`
truthfulness rules.
