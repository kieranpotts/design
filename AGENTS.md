# [Project Name] – design docs

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD,
SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

## Project overview

See the [README](./README.md) for an overview of this project, and how it fits
alongside the sibling SRS, RFC, plans, audits, and risks repositories.

This repository is documentation, not code. There is nothing to build, lint,
or run.

## Project structure

- `design/`. The architectural artifacts, organized into eight views that
  are extended from the 4+1 architectural view model (and draw on C4 and
  Arc42). Six views form a ladder from most abstract to most concrete. The
  other two – `scenarios` and `concepts` – cut across all the other views.
  Each view is a directory with a `README.md` entry point.

  - `conceptual/`, `logical/`, `development/`, `process/`,
    `physical/`, and `technical/` are the six ladder views, from most
    abstract to most concrete.

  - `scenarios/` and `concepts/` are the two cross-cutting views.

  - `glossary.md` captures architecture- and technical-specific terms.

- `docs/`. General guidelines for humans on maintaining architectural
  documentation.

## Workflow

This is living documentation. Design docs do not transition through a state
machine. There are no per-document lifecycle states – the artifacts on
`latest/main` are simply the truth about the current architecture, kept honest
by binding changes to production.

See [CONTRIBUTING.md > Workflow](./CONTRIBUTING.md#workflow) for the
step-by-step process for introducing a design change.

## Rules

Agents MUST follow the rules in [CONTRIBUTING.md > Rules](./CONTRIBUTING.md#rules).
Re-read the rules before editing a design artifact, rather than relying on
your memory of a prior state of the rules.

## Skills

The `.agents/skills/` directory provides on-demand skills for maintaining
the design documentation. See the [README](./.agents/skills/README.md) for
descriptions of the available skills and their triggers.

It is RECOMMENDED to use these skills to drive the workflow.

## References

The following technical standards (TS) govern this project. Fetch and ingest
the relevant standards as-and-when required for the task at hand.

- [**TS-3: Design Docs**](https://kieranpotts.com/standards/003) \
  Use when writing, reviewing, or maintaining design docs, RFCs, architecture
  decision records (ADRs), or architecture audit reports.

- [**TS-4: Modeling**](https://kieranpotts.com/standards/004) \
  Use when defining architectural views (conceptual, logical, development,
  process, physical, etc.) or choosing tools/notations for system modeling.

- [**TS-9: Version Control**](https://kieranpotts.com/standards/009) \
  Use when working with Git. Covers commits, branching, merging, integration
  strategies, cutting releases, and configuring Git/PR/CI tooling.

- [**TS-25: Technical Documentation**](https://kieranpotts.com/standards/025) \
  Use when deciding what documentation a project needs, where it should live,
  who it's for, or whether it's still trustworthy.

- [**TS-26: Technical Writing Style Guide**](https://kieranpotts.com/standards/026) \
  Use when writing or editing the prose of a technical document. Covers
  tone-of-voice, headings, terminology, lists, and citations.
