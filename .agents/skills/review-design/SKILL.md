---
name: review-design
description: >-
  Check that proposed design changes are ready for review, and take the PR
  our of draft status. Use this skill when the user says something like
  "review this design change", "this design change is ready for review",
  "take the design PR out of draft", "mark the design change ready for review",
  or "review design".
compatibility: requires Read, Bash (git/gh)
license: CC0-1.0
---

# Review design

Check a proposed design change has enough substance for review, and take its
pull request out of draft.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **Target — REQUIRED.** Infer the design change from the checked-out
  branch (`design/<slug>`). If on `main`, list open draft pull requests
  matching `design:` and ask the user to choose:

  ```sh
  gh pr list --draft --search "design:" --json number,title,headRefName
  ```

## Success criteria

- If the PR is deemed ready-for-review, it's status MUST NOT be draft
  (`isDraft: false`).

- If the PR is deemed ready-for-review, there MUST NOT be any `TODO`
  annotations or other placeholder text left in the
  [design views](../../../design/).

## Instructions

1.  Identify the design change and its PR.

    Infer the target from the checked-out branch (`design/<slug>`). If on
    `main`, list open draft pull requests and ask the user to choose.

2.  Do a light completeness check.

    Diff the branch against `main` to find every edited file under
    [`design/`](../../../design/). For each, confirm the edit is
    descriptive prose about the intended architecture — not a bare marker
    like "needs: describe the new topology here" left over from
    [`/draft-design`](../draft-design/SKILL.md).

    Report any view that is still just a marker, and stop. Do NOT block on
    prose quality, missing cross-links to an RFC, or views the branch does
    not touch — those are exactly what review is for.

3.  Remove the PR's draft status.

    ```sh
    gh pr ready <number>
    ```

4.  Output a summary of your actions.

## Rules

- You MUST NOT mark ready a change where every touched view is still just a
  marker.

  A pull request with nothing but "needs: ..." notes has nothing for a
  reviewer to weigh in on.

- You MUST NOT require the wording to be finished.

  Views MAY still be refined in response to review feedback. This skill
  checks for substance, not completion.

- You MUST NOT edit the views' content yourself.

  Flag gaps to the user; do not fill them in on their behalf.

- You MUST describe the end state, not a changelog.

  Edits describe the architecture as it will be once shipped — not the
  migration steps. Flag any edit written as a changelog of what's changing
  rather than a description of what the end state is; the diff against
  `main` already shows what is changing.

- You MUST keep artifacts descriptive of architecture, not requirements or
  decisions.

  Flag any edit that reads as a requirement or an undecided decision rather
  than a description of the architecture. Keep the artifacts descriptive
  (what the architecture is) and decision-free (link to the RFC for the why).
  Redirect requirement changes to the SRS and undecided significant decisions
  to the RFC process.

- You MUST NOT merge the pull request, or check that the production change
  is live.

  That is [`/complete-design`](../complete-design/SKILL.md)'s job, once
  review is settled and the change has shipped.
