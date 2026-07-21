# Agent skills

Skills available to agents in this repository are:

- **[Draft design](./draft-design/):**
  Scaffolds a design change.

- **[Ship design](./ship-design/):**
  Lands a design change.

- **[Reconcile design](./reconcile-design/):**
  Corrects drift from reality.

## Compatibility

Agent harnesses are converging on the `./.agents/skills/` path for dynamic
retrieval of project-specific skills. This is compatible with the Agent Skills
convention — see https://agentskills.io/.

As of May 2026, OpenAI Codex, GitHub Copilot, Gemini CLI, Google Antigravity,
OpenCode, and Pi will auto-discover these skills, but Claude Code and Cursor
will not.

You will require workarounds for incompatible harnesses. For Claude Code, you
can simply symlink this directory from `.claude/skills/`. Cursor requires more
effort to transpile these skills into its native "rules" format.
