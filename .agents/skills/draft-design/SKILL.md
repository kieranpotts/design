---
name: draft-design
description: >-
  Scaffold the branch, pull request, and discussion thread for a change to this
  repository's architectural design documentation. Use when the user wants to
  document a change to the production system's architecture, or says something
  like "draft a design change", "new design change", "document this
  architecture change", or "update the design docs". Do not use it to write the
  substance of the change, or to evaluate the architecture.
compatibility: >-
  requires Read, Write, Edit, Glob, Grep, Bash (git, gh)
license: CC0-1.0
---

# Draft design

Scaffold a pull request that the author will use to propose a change to the
system design: cut the branch, mark up the design views the change will touch,
open a draft pull request, and open the discussion thread that goes with it.
Leave the substance of the change to the author.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **Description of the design change — REQUIRED.** What is changing in the
  production architecture, stated in the present tense, full lowercase, and not
  terminated by a period, eg. `extract the billing service`. Take it from the
  user's own words where they gave them.

- **Slug — OPTIONAL.** A short, hyphen-delimited URL path slug naming the
  change, eg. `extract-billing-service`. Derive it from the description when
  the user does not supply one.

- **Affected views — OPTIONAL.** The [design views](../../../design/) the
  change will touch. Infer them from the description, by searching the design
  artifacts for the components the change names. Ask the user when the blast
  radius is not obvious.

## Success criteria

- The branch `design/<slug>` MUST exist, cut from an up-to-date `main`, and
  MUST be checked out.

- A pull request titled `create: <description>` MUST be open against `main`,
  and `gh pr view <number> --json isDraft` MUST report `true`.

- A discussion thread MUST exist naming the pull request, and the pull
  request's body MUST link back to that thread.

- Every affected view MUST carry a `TODO:` marker naming what the author has
  to write there.

- You MUST NOT have written anything beyond those markers into
  [`design/`](../../../design/). Describing the new architecture is the
  author's job, not this skill's — the scaffolding exists so a human can fill
  it in.

## Instructions

1.  Establish the description and derive the slug from it.

2.  Create the branch. Rebase so the history stays linear.

    ```sh
    git checkout main
    git pull --rebase
    git checkout -b design/<slug>
    ```

3.  Identify the [views](../../../design/) the change is likely to affect, and
    write a `TODO:` marker into each, naming what the author needs to describe.
    Do not describe the change yourself.

4.  Commit, push, and open a draft pull request.

    ```sh
    git add design/
    git commit -m "create: <description>"
    git push -u origin design/<slug>
    gh pr create --draft --title "create: <description>" --fill
    ```

    If the `gh` client is unavailable or not authenticated, fail with an error.

5.  Open the discussion thread that will carry the review feedback.

    The `gh` CLI has no native discussion command, so use GitHub's GraphQL API.
    Look up the repository ID and the discussion category to use.

    ```sh
    gh api graphql -f query='
      query($owner:String!, $name:String!) {
        repository(owner:$owner, name:$name) {
          id
          discussionCategories(first:20) { nodes { id name } }
        }
      }' -F owner=<owner> -F name=<repo>
    ```

    Create the discussion, referencing the pull request, and capture its URL.

    ```sh
    gh api graphql -f query='
      mutation($repoId:ID!, $categoryId:ID!, $title:String!, $body:String!) {
        createDiscussion(input:{repositoryId:$repoId, categoryId:$categoryId, title:$title, body:$body}) {
          discussion { url }
        }
      }' -F repoId=<repoId> -F categoryId=<categoryId> \
        -f title="create: <description>" \
        -f body="Discussion thread for the <description> design change (PR #<number>). Please leave all feedback here, not on the pull request."
    ```

6.  Add the returned URL to the pull request description, so the two
    cross-reference each other.

    ```sh
    gh pr edit <number> --body "$(gh pr view <number> --json body -q .body)

    Discussion thread: <discussionUrl> — Please leave all review feedback there, not on this pull request."
    ```

7.  Output a summary of your actions, including the branch name, the pull
    request number, and the views you marked up.

## Rules

- You MUST scaffold exactly one design change per branch and pull request.

  Unrelated architecture changes ship on their own timelines and would block
  each other at the merge gate. Where the user describes several independent
  changes, recommend a branch each.

- You MUST branch from `main`, and pull first if local `main` is behind the
  remote.

  The artifacts on `main` are the authoritative record of the production
  architecture, so it is the only sound starting point.

- You MUST open the pull request in its draft state.

  Taking it out of draft is a later, separate stage of the workflow, once the
  views have real content in them.

- Every design change MUST have an associated discussion thread, linked from
  the pull request.

  All review feedback is gathered in the thread rather than on the pull
  request itself.

- You MUST NOT write the description of the new architecture, and MUST NOT
  evaluate the architecture.

  This skill scaffolds; the author writes.

## Edge cases

- An architecturally significant decision underlies the change.

  Significant decisions are recorded as RFCs, not here. Flag to the user that
  the decision belongs in the
  [RFC](https://github.com/kieranpotts/rfc) repository first, and note in the
  `TODO:` markers that the affected artifacts should link out to that RFC
  rather than restating its rationale.

- The change is already live in production and the documentation simply never
  caught up.

  That is drift, not a forward-looking design change. The comparison against
  the real system is a separate procedure; say so rather than guessing at
  what production currently does.
