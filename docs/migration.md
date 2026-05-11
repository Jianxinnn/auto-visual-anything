# Migration Notes

This repository consolidates the former standalone FigForge skill repositories
into one suite repo.

Source repositories:

- `/public/home/jxtang/.agents/skills/figforge`
- `/public/home/jxtang/.agents/skills/figforge-plan`
- `/public/home/jxtang/.agents/skills/figforge-gen`
- `/public/home/jxtang/.agents/skills/figforge-deck`

Target layout:

```text
FigForge/
  skills/
    figforge/
    figforge-plan/
    figforge-gen/
    figforge-deck/
```

After import, `~/.agents/skills/<name>` should be a symlink to the matching
`FigForge/skills/<name>` directory. Existing standalone directories should be
moved to `~/.agents/skills/.migration-backups/` rather than deleted.

The old GitHub repositories can remain as read-only compatibility pointers after
the suite repo is published.
