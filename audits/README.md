# Audits

This directory holds architecture audits — standalone, point-in-time evaluations of the system's as-is architecture.

An audit reads the source code and reports on the system's structural health. It surfaces code smells and anti-patterns such as shallow abstractions, tangled dependencies, single-caller wrappers, leaky boundaries, repeated patterns, and the like.

The reports are presented as a prioritized list of findings. They are evaluation only — they do not suggest alternative designs. And they evaluate the as-built architecture on its own terms, without cross-referencing the _intended_ architecture captured in the design docs, and with no prior knowledge of the trade-offs already considered.

This means that drift from the documented design is not caught by an audit (use the [reconcile-design](../.agents/skills/reconcile-design/) skill for that). But on the plus side, unbiased audits are more likely to surface genuinely useful suggestions. They're a fresh pair of eyes.

## Structure

```
audits/
├── INDEX.md            # The catalog of merged audits, newest first.
├── TEMPLATE.md         # Template for a new audit report.
└── YYYY-MM-DD-<slug>/  # One report, dated by when the audit was done.
    ├── README.md       # The main entry point to the audit report.
    └── …               # Dependency graphs, exports, or other evidence.
```

## Workflow

1. An audit is opened as a pull request on an `audit/<slug>` branch.

2. A report consists of _at least_ a README file, based on the [template](./TEMPLATE.md) and saved at `audits/YYYY-MM-DD-<slug>/README.md`.

3. On merge, a row is prepended to the [audit index](./INDEX.md).
