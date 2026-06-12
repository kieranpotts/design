# Contributing

<!-- Agents MUST read ./AGENTS.md. This document is for humans. -->

These contributing guidelines provide step-by-step instructions for keeping the design documentation synchronized with the production system. The focus here is on the mechanics and guardrails of the process. See the [documentation](./docs/) for more general guidance on maintaining good quality architectural documentation.

The design documentation is maintained by the technical teams. Anyone with write access to this repository may propose changes to it.

> [!NOTE]
> The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT, OPTIONAL, and MAY herein are to be interpreted as described in [IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

## Overview

The [design artifacts](./design/) always reflect the current state of the production system's architecture, expressed through a coherent set of architectural views. This is a living document. The description on `main` and the real system stay in lock-step.

The design docs are deliberately narrow in purpose. They are descriptive – stating what the architecture _is_ — and decision-free — they do not record _why_ the architecture is the way it is. Two sibling repositories cover these related concerns:

- The [SRS](https://github.com/kieranpotts/specs) records the requirements — _what_ the system must do.

- The [RFC](https://github.com/kieranpotts/rfc) archive records the significant technical decisions — _how_ a choice was made and _why_.

A typical flow is SRS → RFC → Design Docs. A new requirement (specified in the SRS) requires an architecturally-significant design decision (such as a change to the technology stack, negotiated via an RFC) before the necessary changes can be implemented in code (the design docs capture the end result).

## The design-change workflow

The workflow is designed around a single, firm rule:

**The `main` trunk describes production.**

The [design artifacts](./design/) on `main` are the current truth. The design-change workflow exists to protect that promise.

A change to the architecture is introduced through a design-change pull request. Follow these steps.

### Step 1: Make the decision first, if it is significant

If the change embodies an architecturally significant decision — a new pattern, a deviation from the established stack, a structural shift with broad impact — that decision is made through the [RFC process](https://github.com/kieranpotts/rfc), _before_ the work is done.

Th design docs capture the resulting architecture. This is NOT where the decision is debated.

Routine design changes that follow already-established patterns need no RFC. If the change would impact multiple technical stakeholders and is worth building consensus on, it is worthy of an RFC.

### Step 2: Open a discussion thread (REQUIRED)

Every design-change pull request has an associated discussion thread, where _all_ review feedback is gathered. This keeps the pull request focused on the evolution of the design artifacts themselves.

Open a [discussion](https://github.com/kieranpotts/design/discussions). You MAY open it early, to align on the shape of the change before editing artifacts, but it MUST exist by the time the pull request is opened.

Link the discussion and the pull request to each other. The thread is closed once the change is merged.

(The GitHub issue tracker is _not_ used for design changes. It is reserved for repository maintenance only.)

### Step 3: Edit the artifacts to describe the end state

1. Branch off `main` using the convention `design/<slug>`, where `<slug>` is a short, hyphen-delimited description of the change, eg. `design/extract-billing-service`.

2. Edit the artifacts in the [`design/` directory](./design/). Modify all appropriate architectural views to describe the architecture as it will be once the change has shipped. Add, modify, or remove artifacts as needed to describe the desired end state. The edits MUST read as a description of the destination, not a list of steps to get there — the diff against `main` already shows what is changing.

3. Where a significant decision drove the change, link the relevant artifact to its RFC, rather than restating the rationale.

4. Ensure every artifact is referenced from its view's `README.md`.

### Step 4: Open a pull request

1. Commit your changes and open a pull request titled `design: <description>`, where `<description>` is a short prose title, written full lowercase, eg. `design: extract the billing service`.

2. Fill out the top of the PR template and link the discussion thread.

3. Open the PR as a draft while you refine it.

### Step 5: Review and reconcile

1. When the artifacts are ready for review, mark the pull request ready for review. Gather all feedback in the discussion thread.

2. As implementation proceeds, reconcile any drift between the proposed documentation and the real system back into the artifacts, so the documentation that is eventually merged describes the architecture as actually built.

### Step 6: Merge once the change is live

1. Confirm the corresponding code and configuration are live in production.

2. Squash-merge the pull request, with a message of the form `design: <description>`. Delete the branch.

3. Close the discussion thread — it has served its purpose.

## Rules

- Design artifacts MUST be written in American English.

- The `main` trunk is the default branch. The artifacts in [`design/`](./design/) on `main` are the authoritative record of the production architecture as it exists right now.

- The documentation is descriptive and decision-free. State what the architecture _is_, in the present tense. Do not record requirements (they live in the SRS) or rationale (it lives in the RFC archive). Link out to the RFC for any significant decision behind a change.

- Design changes are developed on `design/<slug>` branches cut from `main`, and integrated back via pull requests. A change's pull request MUST NOT be merged until the corresponding code and configuration are live in production, so `main` stays current with production.

- The edits in a design-change PR MUST describe the intended final state of the architecture, NOT a changelog of how to get there.

- Every design-change pull request MUST have an associated discussion thread, opened with the pull request and used for all review feedback. The thread is closed once the change is merged.

- A pull request is opened as a draft while the artifacts are refined and the production change is rolled out. It is marked ready for review when the artifacts are ready, and merged only when the change is live.

- Design-change branches are squash-merged into `main`, with a squash commit message of the form `design: <description>`, where `<description>` is a short prose title written full lowercase (eg. `design: extract the billing service`).

- Every supporting artifact MUST be referenced from a view's `README.md`. Diagrams SHOULD be authored as text so they diff cleanly and live in version control.

- The GitHub issue tracker is used only for maintenance work on this repository itself (the `MAINTENANCE` template). Open-ended architectural brainstorming happens in [discussions](https://github.com/kieranpotts/design/discussions). Significant decisions are made through the [RFC](https://github.com/kieranpotts/rfc) process.

## Contributor license agreement

<!-- Delete this for closed source projects. -->

By opening a pull request to this repository, you accept and agree to the following terms and conditions:

- You agree that your contribution may be distributed under the terms of the [CC0 1.0 Universal license](./LICENSE.txt), effectively releasing it to the public domain.

- You certify that your contribution is either created in whole by you and you have the right to distribute it under the designated license, or is based on a previous work with a compatible license that permits distribution and modification under the designated license.

- You understand and agree that your contribution is public and that a record of it, including all personal information you submit with it, is maintained indefinitely and may be redistributed consistent with the designated license.
