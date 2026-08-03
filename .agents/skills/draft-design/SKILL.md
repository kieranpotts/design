---
name: draft-design
description: >-
  Draft a design change. Use this skill when the user wants to update the
  architectural documentation to reflect a change to the production system, or
  says something like "draft a design change", "new design change",
  "document this architecture change", or "update the design docs".
license: CC0-1.0
metadata:
  interactive: yes
  preferred_model: ollama/PROSE_DEEP
---

# Draft design

Scaffold a PR that the user will subsequently use to propose a change to the
system design.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **Description of the planned design change — REQUIRED.**

## Success criteria

- Branch `design/<slug>` MUST exist and be checked out.

- A draft pull request titled `design: <short lowercase description>` MUST
  be open.

- An associated discussion thread MUST be open, linked from the PR.

## Instructions

1.  From the description of the planed design change, form a short,
    hyphen-delimited URL path slug, eg. `extract-billing-service`.

2.  Create the branch.

    ```sh
    git checkout main
    git pull --rebase
    git checkout -b design/<slug>
    ```

3.  Identify the [views](../../../design/) that are likely to be affected by
    this change. Write `TODO:` markers for the author into the design files,
    but leave the details to be filled-in by the user later.

4.  Commit and open a draft pull request.

    ```sh
    git add design/
    git commit -m "design: <short lowercase description>"
    git push -u origin design/<slug>
    gh pr create --draft --title "design: <short lowercase description>" --fill
    ```

5.  Open a discussion thread.

    Every pull request MUST have an associated discussion thread, where all
    review feedback is gathered. The `gh` CLI has no native discussion command,
    so use GitHub's GraphQL API. Look up the repository ID and the discussion
    category to use.

    ```gh
    gh api graphql -f query='
      query($owner:String!, $name:String!) {
        repository(owner:$owner, name:$name) {
          id
          discussionCategories(first:20) { nodes { id name } }
        }
      }' -F owner=<owner> -F name=<repo>
    ```

    Create the discussion, referencing the PR, and capture its URL.

    ```gh
    gh api graphql -f query='
      mutation($repoId:ID!, $categoryId:ID!, $title:String!, $body:String!) {
        createDiscussion(input:{repositoryId:$repoId, categoryId:$categoryId, title:$title, body:$body}) {
          discussion { url }
        }
      }' -F repoId=<repoId> -F categoryId=<categoryId> \
        -f title="design: <short lowercase description>" \
        -f body="Discussion thread for the <short lowercase description> design change (PR #<number>). Please leave all feedback here, not on the pull request."
    ```

    Add the returned URL to the pull request description, so the two
    cross-reference each other.

    ```sh
    gh pr edit <number> --body "$(gh pr view <number> --json body -q .body)

    Discussion thread: <discussionUrl> — Please leave all review feedback there, not on this pull request."
    ```

## Rules

- You MUST draft exactly one design change per branch and pull request.
  Do not bundle unrelated architecture changes. If the user describes several
  independent changes, recommend drafting separate branches.

- You MUST branch from `main`, not from any other branch. If local `main` is
  behind the remote, pull first.

- You MUST open the PR as a draft.

- Every design change MUST have an associated discussion thread.
