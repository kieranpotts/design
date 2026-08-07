---
name: review-design
description: >-
  Check that a proposed change to the architectural design documentation has
  enough substance for reviewers to weigh in on, then take its pull request out
  of draft. Use when the user says something like "review this design change",
  "this design change is ready for review", "take the design PR out of draft",
  "mark the design change ready for review", or "review design". Do not use it
  to review the architecture itself, or to merge the pull request.
compatibility: >-
  requires Read, Grep, Bash (git, gh)
license: CC0-1.0
---

# Review design

Check that a proposed design change has enough substance for review, and take
its pull request out of draft. Flag gaps to the user rather than filling them
in yourself.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **Target — REQUIRED.** The design change to check. Infer it from the
  checked-out branch (`design/<slug>`). If `main` is checked out, list the open
  draft pull requests and ask the user to choose:

  ```sh
  gh pr list --draft --search "design:" --json number,title,headRefName
  ```

## Success criteria

- Every design view touched by the branch MUST have been checked against the
  diff with `main`, and any view still holding only a `TODO:` marker or other
  placeholder MUST have been reported to the user by name.

- The pull request MUST have been taken out of draft — `gh pr view <number>
  --json isDraft` reporting `false` — if and only if no touched view was left
  as a bare placeholder.

- The working tree under [`design/`](../../../design/) MUST be unchanged. This
  skill reports on substance; it does not supply it.

- The pull request MUST NOT have been merged, and the discussion thread MUST
  still be open. Landing the change is a later, separate stage.

## Instructions

1.  Identify the design change and its pull request.

2.  Do a light completeness check.

    Diff the branch against `main` to find every edited file under
    [`design/`](../../../design/):

    ```sh
    git diff --name-only main...HEAD -- design/
    ```

    For each, confirm the edit is descriptive prose about the intended
    architecture, not a bare scaffolding marker such as
    `TODO: describe the new topology here`.

    Report any view that is still just a marker, and stop. Do not block on
    prose quality, on missing cross-links to an RFC, or on views the branch
    does not touch — those are exactly what review is for.

3.  Take the pull request out of draft.

    ```sh
    gh pr ready <number>
    ```

4.  Output a summary of your actions, naming the pull request and the views
    you checked.

## Rules

- You MUST NOT mark ready a change whose every touched view is still just a
  placeholder.

  A pull request holding nothing but `TODO:` markers has nothing for a
  reviewer to weigh in on.

- You MUST NOT require the wording to be finished.

  Views MAY still be refined in response to review feedback. This skill checks
  for substance, not for completion.

- You MUST NOT edit the views' content yourself.

  Flag gaps to the user; do not fill them in on their behalf. A reviewer needs
  to see the author's account of the architecture, not yours.

- You MUST flag any edit written as a changelog rather than as a description
  of the end state.

  The artifacts describe the architecture as it will be once the change has
  shipped. The diff against `main` already shows what is changing.

- You MUST flag any edit that reads as a requirement or as an unsettled
  decision.

  Keep the artifacts descriptive and decision-free. Redirect requirement
  changes to the [requirements specification](https://github.com/kieranpotts/specs),
  and unsettled significant decisions to the
  [RFC](https://github.com/kieranpotts/rfc) process, which the artifact then
  links out to rather than restating.

- You MUST NOT merge the pull request, and MUST NOT check whether the
  production change is live.

  Both belong to the later stage that lands the change, once review is settled
  and the change has actually shipped.

## Edge cases

- The pull request is already out of draft.

  Run the completeness check anyway and report what you find, but do not
  re-run `gh pr ready`. Say plainly that the transition had already happened.

- The branch has no edits under `design/` at all.

  There is nothing to review. Report this and stop, rather than marking an
  empty pull request ready.
