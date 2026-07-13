# [Project Name] – Design Docs

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT,
OPTIONAL, and MAY are to be interpreted as described in [IETF RFC
2119](https://www.ietf.org/rfc/rfc2119.txt).

## Project overview

This repository holds the design documentation for [Project Name] – the living
description of _what the system's architecture looks like_ as it exists in
production right now. It is documentation, not code. There's nothing to build,
lint, or run.

The documentation is descriptive and decision-free. It describes the
architecture that exists. It does NOT record the requirements the system must
satisfy, nor the rationale for the choices behind the design:

- Requirements (_what_ the system does, in business terms) live in the
  [SRS](https://github.com/kieranpotts/specs).

- Significant technical decisions (_how_ a choice was made, and _why_)
  live in the [RFC](https://github.com/kieranpotts/rfc) archive.

- Standalone, point-in-time evaluations of the as-built system – not the
  intended architecture captured here – live in a separate
  [`audits`](https://github.com/kieranpotts/audits) repository.

Where a significant decision shaped the design, the artifact MUST link out to
the RFC that records it, rather than restating the reasoning here.

The artifacts in the [`design/` directory](./design/) on the `main` trunk MUST
reflect the current state of the system in production. A change to the
architecture is merged into `main` at the same time as the corresponding code
and configuration ship to production, so the documentation never drifts from
reality.

Unlike the SRS, there is no accompanying decision log – the RFC repository
serves that purpose.

## Project structure

- **`design/`**:
  The architectural artifacts, organized into seven views that are extended from
  the 4+1 architectural view model. The views form a ladder from most abstract
  to most concrete, with `scenarios` cutting across all the views. Each view is
  a directory with a `README.md` entry point. Supporting artifacts (diagrams,
  schemas, exports) live inside the directories and MUST be referenced from the
  `README.md`.

  - **`conceptual/`**:
    The strategic, whole-system overview – major parts, system landscape, and
    the shape of the whole. Readable by non-technical stakeholders. Entry point
    to the other views. Most abstract view.

  - **`logical/`**:
    The functional structure – components, their responsibilities, and their
    relationships. The developer-facing decomposition of what the system _is_.

  - **`development/`**:
    The static organization of the codebase – modules, layers, repositories,
    build artifacts, and their dependencies.

  - **`process/`**:
    The runtime view – processes, threads, services, and how they communicate,
    synchronize, and handle concurrency.

  - **`physical/`**:
    The deployment view – how software maps onto infrastructure: hosts,
    networks, environments, and runtime topology.

  - **`technical/`**:
    The concrete stack – the languages, runtimes, and system software the system
    is built from, named and versioned. This is the most concrete view.

  - **`scenarios/`**:
    The cross-cutting view – key end-to-end flows that tie the other six views
    together, illustrating how the architecture realizes important behaviors.

- **`docs/`**:
  General guidelines for humans on maintaining architectural documentation.

## How design changes are introduced

This is a living document, not a state machine. There are no per-document
lifecycle states. Here, the artifacts on `main` are simply the truth about the
current architecture, kept honest by binding changes to production.

A change to the architecture is introduced through a design-change pull request:

1.  The decision (if the change is architecturally significant) is made first,
    through the RFC process. This repository documents the _result_ of that
    decision, not the decision itself.

2.  The design artifacts are edited to describe the intended final state of the
    architecture once the change has shipped – not a changelog of how to get
    there.

3.  The pull request is reviewed, with feedback gathered in a discussion thread.

4.  The PR is merged into `main` only once the change is live in production,
    keeping the documentation synchronized with reality.

## Rules

- Write in American English.

- The [`design/`](./design/) artifacts on `main` (the default branch) MUST
  describe the production architecture as it exists now. They are the
  authoritative record of the current state of the system.

- The documentation is descriptive. Each artifact states what the architecture
  _is_, in the present tense, as a timeless description of the current state –
  NOT a history of how it got there, and NOT the requirements it satisfies.

- The documentation is decision-free. Do NOT record the rationale for design
  choices here. Where a significant decision drove the design, link to the RFC
  that records it. Routine, RFC-unworthy design details need no such link.

- Changes to the design artifacts MUST be introduced via design-change
  pull requests, branched from `main`. The edits MUST describe the intended
  final state after the change ships, NOT a changelog of how to reach that state
  – that's an implementation detail the diff already captures.

- A design-change PR MUST NOT be merged into `main` until the corresponding
  code and configuration are live in production. The documentation must never
  describe an architecture that does not yet exist.

- Keep each artifact in the view where it belongs. A structural decomposition
  is logical; a deployment topology is physical; an end-to-end flow is a
  scenario; etc. When an artifact could plausibly sit in two views, prefer the
  one that answers the reader's most likely question, and cross-reference from
  the other.

- Every supporting artifact (diagram, schema, export) MUST be referenced
  from a view's `README.md`. If it is not referenced there, it is not part of
  the design documentation.

- Diagrams SHOULD be authored as text where practical (eg. Mermaid, PlantUML,
  Structurizr DSL) so they diff cleanly and live in version control alongside
  the prose. Binary exports MAY accompany a textual source, but the source is
  authoritative.

- The GitHub issue tracker is used only for maintenance work on this repository
  itself (via the `MAINTENANCE` template). Open-ended architectural
  brainstorming happens in
  [discussions](https://github.com/kieranpotts/design/discussions), and
  significant decisions are made through the
  [RFC](https://github.com/kieranpotts/rfc) process.

## Skills

The [`.agents/skills/`](./.agents/skills/) directory is reserved for on-demand
skills that help maintain the design documentation. See the
[README](./.agents/skills/README.md) for details.
