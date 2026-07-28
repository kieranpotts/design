# Contributing

<!-- Agents MUST read ./AGENTS.md. This document is for humans. -->

These contributing guidelines provide step-by-step instructions for keeping the
design documentation synchronized with the production system.

The focus here is on the mechanics and guardrails of the process. See the
[documentation](./docs/) for more general guidance on maintaining good quality
architectural documentation.

The design documentation is maintained by the technical teams. Anyone with write
access to this repository may propose changes to it.

See also [TS-3](https://github.com/kieranpotts/standards/tree/latest/dev/src/003)
for the technical standard that underpins this process.

****
The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD,
SHOULD NOT, OPTIONAL, and MAY herein are to be interpreted as described
in [IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).
****

## Workflow

> [!TIP]
> [Agent skills](./.agents/skills/) are available to help automate some steps in
> this workflow.

1.  If the change embodies an architecturally significant decision – a new
    pattern, a deviation from the established stack, a structural shift with
    broad impact – make that decision first, through the [RFC
    process](https://github.com/kieranpotts/rfc), before the work is done. The
    design docs capture the resulting architecture; this is NOT where the
    decision is debated. Routine design changes that follow already-established
    patterns need no RFC. If the change would impact multiple technical
    stakeholders and is worth building consensus on, it is worthy of an RFC.

2.  Branch off `main` using the convention `design/<slug>`, where `<slug>` is a
    short, hyphen-delimited description of the change, eg.
    `design/extract-billing-service`.

3.  Edit the artifacts in the [`design/` directory](./design/). Modify all
    appropriate architectural views to describe the architecture as it will be
    once the change has shipped. Add, modify, or remove artifacts as needed to
    describe the desired end state. The edits MUST read as a description of the
    destination, not a list of steps to get there – the diff against `main`
    already shows what is changing.

4.  Where a significant decision drove the change, link the relevant artifact to
    its RFC, rather than restating the rationale.

5.  Ensure every artifact is referenced from its view's `README.md`.

6.  Commit your changes and open a pull request as a draft, titled `design:
    <description>`, where `<description>` is a short prose title, written full
    lowercase, eg. `design: extract the billing service`. Fill out the top of
    the PR template. (You will link the discussion thread, opened in the next
    step, here and in the artifacts.)

7.  Open an associated [discussion
    thread](https://github.com/kieranpotts/design/discussions) (REQUIRED). It
    MUST exist by the time the pull request is marked ready for review; you MAY
    open it earlier – even before the pull request – to align on the shape of
    the change before editing artifacts. Link the discussion and the pull
    request to each other. All review feedback is gathered here, keeping the
    pull request focused on the evolution of the design artifacts themselves.
    (The GitHub issue tracker is _not_ used for design changes. It is reserved
    for repository maintenance only.)

8.  When the artifacts are ready for review, mark the pull request ready for
    review. Gather all feedback in the discussion thread.

9.  As implementation proceeds, reconcile any drift between the proposed
    documentation and the real system back into the artifacts, so the
    documentation that is eventually merged describes the architecture as
    actually built.

10. Confirm the corresponding code and configuration are live in production.

11. Squash-merge the pull request, with a message of the form `design:
    <description>`. Delete the branch.

12. Close the discussion thread – it has served its purpose.

## Rules

- Design artifacts MUST be written in American English.

- The `main` trunk is the default branch. The artifacts in
  [`design/`](./design/) on `main` are the authoritative record of the
  production architecture as it exists right now.

- The documentation is descriptive and decision-free. State what the
  architecture _is_, in the present tense. Do not record requirements (they live
  in the SRS) or rationale (it lives in the RFC archive). Link out to the RFC
  for any significant decision behind a change.

- Design changes are developed on `design/<slug>` branches cut from `main`, and
  integrated back via pull requests. A change's pull request MUST NOT be merged
  until the corresponding code and configuration are live in production, so
  `main` stays current with production.

- The edits in a design-change PR MUST describe the intended final state of the
  architecture, NOT a changelog of how to get there.

- Every design-change pull request MUST have an associated discussion thread,
  opened with the pull request and used for all review feedback. The thread is
  closed when the PR is merged.

- A pull request is opened as a draft while the artifacts are refined and the
  production change is rolled out. It is marked ready for review when the
  artifacts are ready, and merged only when the change is live.

- Design-change branches are squash-merged into `main`, with a squash commit
  message of the form `design: <description>`, where `<description>` is a short
  prose title written full lowercase (eg. `design: extract the billing
  service`).

- Every supporting artifact MUST be referenced from a view's `README.md`.
  Diagrams SHOULD be authored as text so they diff cleanly and live in version
  control.

- The GitHub issue tracker is used only for maintenance work on this repository
  itself (the `MAINTENANCE` template). Open-ended architectural brainstorming
  happens in [discussions](https://github.com/kieranpotts/design/discussions).
  Significant decisions are made through the
  [RFC](https://github.com/kieranpotts/rfc) process.

## Tools

### Pre-commit hooks

It is RECOMMENDED to install the [pre-commit](https://pre-commit.com) framework
to enable local validation hooks before committing. You need only to run the
following command once to install pre-commit system-wide:

```bash
pipx install pre-commit
```

Then install the pre-commit hooks in every local repository where you want
pre-commit checks to be run:

```bash
pre-commit install
```

This installs all hook types declared in `.pre-commit-config.yaml`
(`pre-commit`, `commit-msg`).

Edit `./.pre-commit-config.yaml` to configure the pre-commit validation checks
you want for your project. See the [pre-commit](https://pre-commit.com) docs for
details.

## Contributor license agreement

<!-- Delete this for closed source projects. -->

By opening a pull request to this repository, you accept and agree to the
following terms and conditions:

- You agree that your contribution may be distributed under the terms of the
  [CC0 1.0 Universal license](./LICENSE.txt), effectively releasing it to the
  public domain.

- You certify that your contribution is either created in whole by you and you
  have the right to distribute it under the designated license, or is based on a
  previous work with a compatible license that permits distribution and
  modification under the designated license.

- You understand and agree that your contribution is public and that a record of
  it, including all personal information you submit with it, is maintained
  indefinitely and may be redistributed consistent with the designated license.
