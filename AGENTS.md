# [Project Name] – Design Docs

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD,
SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

## Project overview

See the [README](./README.md) for an overview of this project, and how it fits
alongside the sibling SRS, RFC, plans, audits, and risks repositories.

This repository is documentation, not code. There is nothing to build, lint,
or run.

## Project structure

- **`design/`:** The architectural artifacts, organized into eight views that
  are extended from the 4+1 architectural view model (and draw on C4 and
  Arc42). Six views form a ladder from most abstract to most concrete. The
  other two – `scenarios` and `concepts` – cut across all the other views. Each
  view is a directory with a `README.md` entry point.

  - **`conceptual/`**, **`logical/`**, **`development/`**, **`process/`**,
    **`physical/`**, and **`technical/`** are the six ladder views, from most
    abstract to most concrete.

  - **`scenarios/`** and **`concepts/`** are the two cross-cutting views.

  - **`glossary.md`** captures architecture- and technical-specific terms.

- **`docs/`:** General guidelines for humans on maintaining architectural
  documentation.

## Workflow

This is living documentation. Design docs do not transition through a state
machine. There are no per-document lifecycle states – the artifacts on `main`
are simply the truth about the current architecture, kept honest by binding
changes to production.

See [CONTRIBUTING.md > Workflow](./CONTRIBUTING.md#workflow) for the
step-by-step process for introducing a design change.

## Rules

Agents MUST follow the rules in [CONTRIBUTING.md > Rules](./CONTRIBUTING.md#rules).
Re-read the rules before editing a design artifact, rather than relying on
your memory of a prior state of the rules.

## Skills

The **`.agents/skills/`** directory provides on-demand skills for maintaining
the design documentation. See the [README](./.agents/skills/README.md) for
descriptions of the available skills and their triggers.

It is RECOMMENDED to use these skills to drive the workflow.
