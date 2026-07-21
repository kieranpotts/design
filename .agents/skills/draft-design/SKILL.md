---
name: draft-design
description: >-
  Scaffold a design change. Use this skill when the user wants to update the
  architectural documentation to reflect a change to the production system, or
  says "draft a design change", "new design change", "document this
  architecture change", or "update the design docs". Do not use this skill to
  ship a design change, or to correct documentation that has drifted from
  production.
license: CC0-1.0
metadata:
  interactive: yes
---

# Draft design

A design change edits the [design views](../../../design/) to describe the
architecture as it will be once a production change has shipped. There is no
lifecycle state machine.

**Input:** A description of the production change to document — REQUIRED.
Prompt the user if they have not described it. Determine from it the slug, the
affected views, and any architecturally significant decision behind the
change.

**Output:** A `design/<slug>` branch, with the affected [design
views](../../../design/) edited (or clearly marked for the author), committed
to a draft pull request opened against `main`, with a linked discussion
thread.

## Before scaffolding

-   **Confirm the change belongs here.**

    This repository documents what the architecture _looks like_. It does NOT
    record requirements (those live in the
    [SRS](https://github.com/kieranpotts/specs)) or the rationale for decisions
    (that lives in the [RFC](https://github.com/kieranpotts/rfc) archive).

    - A change to _what the system does_ → an SRS proposal, not a design change.
    - An architecturally significant _decision_ → an RFC first; this repository
      then documents the result once it ships.
    - A change to _what the architecture looks like_ → a design change here.

    If the request is really a requirement change or an undecided significant
    decision, say so before scaffolding.

-   **Identify the significant decision behind the change, if any.**

    If the change embodies an architecturally significant decision, that
    decision should be (or have been) made through the RFC process. Note the RFC
    so the affected artifact can link to it. Routine changes following
    established patterns need no RFC.

## Instructions

1.  **Determine the change description and slug.**

    Establish a short, hyphen-delimited slug, eg. `extract-billing-service`.
    Decide this from information the user provided. Prompt the user if they did
    not describe the change.

2.  **Determine the affected views.**

    Work out which of the seven [design views](../../../design/) the change
    touches — `conceptual`, `logical`, `development`, `process`, `physical`,
    `technical`, `scenarios`. A change often touches more than one. Ask the user
    if it is unclear.

3.  **Create the branch.**

    ```sh
    git checkout main
    git pull
    git checkout -b design/<slug>
    ```

4.  **Edit the affected views — or leave clear markers for the author.**

    If the user described the change in enough detail, edit the affected views'
    artifacts to describe the intended end state (present tense, descriptive,
    decision-free; link to the RFC for any significant decision). Otherwise,
    leave the author a clear starting point — note in each affected view what
    needs to change — and let them fill it in. Do not invent architecture you
    cannot substantiate.

5.  **Commit and open a draft pull request.**

    ```sh
    git add design/
    git commit -m "design: <short lowercase description>"
    git push -u origin design/<slug>
    gh pr create --draft --title "design: <short lowercase description>" --fill
    ```

6.  **Open a discussion thread.**

    Every design-change pull request MUST have an associated discussion thread,
    where all review feedback is gathered. `gh` has no native discussion
    command, so use the GraphQL API. Look up the repository ID and the
    discussion category to use:

    ```sh
    gh api graphql -f query='
      query($owner:String!, $name:String!) {
        repository(owner:$owner, name:$name) {
          id
          discussionCategories(first:20) { nodes { id name } }
        }
      }' -F owner=<owner> -F name=<repo>
    ```

    Create the discussion, referencing the PR, and capture its URL:

    ```sh
    gh api graphql -f query='
      mutation($repoId:ID!, $categoryId:ID!, $title:String!, $body:String!) {
        createDiscussion(input:{repositoryId:$repoId, categoryId:$categoryId, title:$title, body:$body}) {
          discussion { url }
        }
      }' -F repoId=<repoId> -F categoryId=<categoryId> \
        -f title="design: <short lowercase description>" \
        -f body="Discussion thread for the **<short lowercase description>** design change (PR #<number>). Please leave all feedback here, not on the pull request."
    ```

    Add the returned URL to the pull request description, so the two
    cross-reference each other:

    ```sh
    gh pr edit <number> --body "$(gh pr view <number> --json body -q .body)

    Discussion thread: <discussionUrl> — Please leave all review feedback there, not on this pull request."
    ```

## Rules

-   **Document architecture, not requirements or decisions.**

    Keep the artifacts descriptive (what the architecture _is_) and
    decision-free (link to the RFC for the why). Redirect requirement changes to
    the SRS and undecided significant decisions to the RFC process.

-   **One design change per branch and pull request.**

    Do not bundle unrelated architecture changes. If the user describes several
    independent changes, recommend scaffolding separate branches.

-   **Branch from `main`, not from any other branch.**

    Design changes are always cut from `main`. If local `main` is behind the
    remote, pull first.

-   **Describe the end state, not a changelog.**

    Edits describe the architecture as it will be once shipped — not the
    migration steps. The diff against `main` already shows what is changing.

-   **Open the PR as a draft.**

    A new design change is not yet ready for review, and the production change
    it describes may not yet be live. It MUST be opened as a draft pull request,
    and MUST NOT be merged until [`/ship-design`](../ship-design/SKILL.md)
    confirms the change is live in production.

-   **Every design change has an associated discussion thread.**

    Opened with the PR (even as a draft) and linked from it. All review feedback
    belongs in the discussion, not in the PR's own comments.

## Success criteria

- Branch `design/<slug>` exists and is checked out.

- The affected [views](../../../design/) are edited (or clearly marked for the
  author), describing the intended end state.

- A draft pull request titled `design: <short lowercase description>` is open.

- An associated discussion thread is open, linked from the PR.

## References

- [`AGENTS.md`](../../../AGENTS.md): The full design-change workflow and
  conventions, written for agents.

- [`design/README.md`](../../../design/README.md): The architectural views and
  what each one covers.
