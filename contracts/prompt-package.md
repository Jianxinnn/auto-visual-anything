# Prompt Package Contract

`figforge-plan` is the source of truth for prompt package content.

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

`figforge` may map recommended generation settings into `figforge-gen` fields,
but it must not fabricate missing evidence or bypass the `figforge-plan`
truthfulness rules.
