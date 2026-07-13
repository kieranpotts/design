# Agent skills

This repository ships a small set of [agent skills](https://agentskills.io/) —
invoked as slash commands through agentic tools such as Claude Code — that
automate the design-change workflow.

The skills automate the recurring mechanics of keeping `main` synchronized with
production. The available skills are:

- **[`/draft-design`](./draft-design/)**: Scaffolds a design change. Cuts a
  `design/<slug>` branch from `main`, opens a draft pull request, and opens a
  linked discussion thread, ready for the author to edit the affected [design
  views](../../design/).

- **[`/ship-design`](./ship-design/)**: Lands a design change. Confirms the
  corresponding production change is live, marks the pull request ready,
  squash-merges it to `main` with a `design: <description>` message, and closes
  the discussion thread. This is the gate that protects the "`main` describes
  production" promise.

- **[`/reconcile-design`](./reconcile-design/)**: Corrects drift. Compares the
  documentation on `main` against the real system (code, configuration,
  infrastructure), and scaffolds a design change to bring the artifacts back in
  line with production when something shipped without updating the docs.

A typical journey runs `/draft-design` → the author edits the affected views →
review in the discussion thread → `/ship-design` once the change is live in
production. Separately, `/reconcile-design` is run whenever the documentation is
found to have drifted from reality.

Each skill knows the guardrails for its step — above all, that a design change
MUST NOT land on `main` before the production change it describes — and will not
proceed until they are met, keeping the process consistent whether a human or an
agent is driving it.
