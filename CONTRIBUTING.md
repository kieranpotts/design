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

1.  If the proposed design change embodies an architecturally significant
    decision, make that decision first, through the
    [RFC process](https://github.com/kieranpotts/rfc).

2.  Branch off `main` using the convention `design/<slug>`, where `<slug>` is a
    short, hyphen-delimited description of the change, eg.
    `design/extract-billing-service`.

3.  Edit the artifacts in the [`design/`](./design/) directory. Modify all
    appropriate architectural views to describe the architecture as it will be
    once the change has shipped.

4.  Where a significant decision drove the change, link the relevant artifact to
    its RFC, rather than restating the rationale.

5.  Ensure every artifact is referenced from its view's `README.md`.

6.  Commit your changes and open a pull request as a draft, titled `design:
    <description>`, where `<description>` is a short prose title, written full
    lowercase, eg. `design: extract the billing service`. Fill out the top of
    the PR template.

7.  Open a [discussion thread](https://github.com/kieranpotts/design/discussions)
    and link the discussion and the pull request to each other.

8.  When the artifacts are ready for review, transition the pull request out of
    its draft state.

9.  As implementation proceeds, reconcile any drift between the proposed
    documentation and the real system, so the design docs that are eventually
    merged will describe the architecture as it was actually built.

10. Confirm the corresponding code and configuration are live in production.
    Squash-merge the pull request, with a message of the form
    `design: <description>`. Delete the branch.

11. Close the discussion thread.

## Rules

- All artifacts MUST be written in American English.

- The `main` trunk MUST be treated as the default branch. The artifacts in
  [`design/`](./design/) on `main` are the authoritative record of the
  production architecture as it exists right now.

- The documentation MUST be descriptive and decision-free. State what the
  architecture _is_, in the present tense. Requirements MUST NOT be recorded
  here (they live in the [requirements specification](https://github.com/kieranpotts/specs))
  and rationale MUST NOT be recorded here either (it lives in the
  [RFCs](https://github.com/kieranpotts/rfc) archive). Link out to an RFC for
  any significant decision behind a change.

- A change's pull request MUST NOT be merged until the corresponding code and
  configuration are live in production, so `main` stays current with
  production.

- The edits in a PR MUST describe the intended final state of the architecture,
  NOT a changelog of how to get there.

- The discussion thread MUST be closed when the PR is merged.

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

- The GitHub issue tracker MUST be used only for maintenance work on this
  repository itself.

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
