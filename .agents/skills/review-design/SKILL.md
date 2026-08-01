---
name: review-design
description: >-
  Take a design change's pull request out of draft once the affected views
  describe real content, not just markers left for the author. Use this
  skill when the user says something like "review this design change",
  "this design change is ready for review", "take the design PR out of
  draft", "mark the design change ready for review", or "review design".
license: CC0-1.0
metadata:
  interactive: yes
  preferred_model: ollama/WORKFLOW_BASIC
---

# Review design

Use this skill to remove a design change's pull request from its draft
state once the affected architectural views describe real content. This is
a light completeness check, not a final sign-off — the wording MAY still be
refined in response to review feedback. This skill only confirms there is
something real to review, not that the change is ready to land (that still
requires the production change to be live — see
[`/complete-design`](../complete-design/SKILL.md)).

## Parameters

Determine the following information from the surrounding context and
environment, if possible.

- **Target — REQUIRED.** Infer the design change from the checked-out
  branch (`design/<slug>`). If on `main`, list open draft pull requests
  matching `design:` and ask the user to choose:

  ```sh
  gh pr list --draft --search "design:" --json number,title,headRefName
  ```

## Success criteria

You will achieve the following outcomes:

- The PR is no longer a draft (`isDraft: false`).

- Every view touched by the branch describes the intended end state in
  prose, not a placeholder note left for the author to fill in.

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

- You MUST NOT merge the pull request, or check that the production change
  is live.

  That is [`/complete-design`](../complete-design/SKILL.md)'s job, once
  review is settled and the change has shipped.
