---
name: complete-design
description: >-
  Land a design change in `main`. Use this skill when the user says something
  like "complete design", "ship this design change", "the change is live",
  "merge the design docs", or "land the design change".
license: CC0-1.0
metadata:
  interactive: yes
  preferred_model: ollama/WORKFLOW_STANDARD
---

# Complete design

Land changes to the design docs in the `main` trunk.

## Parameters

Determine the following information from the surrounding context and
environment, if possible.

- **Target — REQUIRED.** Infer the design change from the checked-out branch
  (`design/<slug>`). If on `main`, use the user's description, or list open
  design-change pull requests and ask the user to choose:

  ```sh
  gh pr list --search "design:" --json number,title,headRefName
  ```

## Success criteria

You will achieve the following outcomes:

<!-- A squash-merged pull request on `main` with a `design: <description>` message,
its branch deleted, and its discussion thread closed. -->

- The corresponding production change MUST be confirmed live.

- The PR MUST be squash-merged into `main` with a `design: <description>`
  message, and the branch MUST be deleted.

- The associated discussion thread MUST be closed.

## Instructions

1.  Identify the design change.

    Infer the target from the checked-out branch (`design/<slug>`). If on
    `main`, use the user's description, or list open design-change pull
    requests and ask the user to choose:

    ```sh
    gh pr list --search "design:" --json number,title,headRefName
    ```

2.  Verify the rules.

    Confirm the production change is live and the documentation matches it.
    Report any unmet condition and stop. Do not take the user's word for "it's
    live" if you can check — but do not block on checks you cannot perform;
    surface what you could not verify.

3.  Confirm the PR is not a draft.

    ```sh
    gh pr view <number> --json isDraft
    ```

    If it is still a draft, stop and direct the user to
    [`/review-design`](../review-design/SKILL.md) first.

4.  Merge the pull request.

    Confirm with the user that the PR is ready to merge — do not merge without
    explicit instruction. Once confirmed, squash-merge it with a `design:
    <description>` message, and delete the source branch on the upstream
    repository:

    ```sh
    gh pr merge <number> --squash --subject "design: <short lowercase description>" --delete-branch
    ```

5.  Delete the branch, if it was not deleted automatically.

    In case the branch was not automatically deleted from the upstream
    repository, delete it directly:

    ```sh
    git push origin --delete design/<slug>
    ```

6.  Close the discussion thread.

    The thread has served its purpose. Find the discussion linked in the
    `Discussion thread` field, look up its node ID, and close it as resolved
    (`gh` has no native discussion command, so use the GraphQL API):

    ```gh
    gh api graphql -f query='
      query($owner:String!, $name:String!, $number:Int!) {
        repository(owner:$owner, name:$name) { discussion(number:$number) { id } }
      }' -F owner=<owner> -F name=<repo> -F number=<discussionNumber>

    gh api graphql -f query='
      mutation($id:ID!) {
        closeDiscussion(input:{discussionId:$id, reason:RESOLVED}) { discussion { closed } }
      }' -F id=<discussionId>
    ```

## Rules

- You MUST NOT merge a draft PR.

  Run [`/review-design`](../review-design/SKILL.md) first.

- You MUST NOT land a design change ahead of production.

  This is the one rule the whole repository depends on. If the production
  change is not live, do not merge — full stop.

- The production change MUST be live.

  The corresponding code, configuration, and infrastructure are deployed and
  serving real users — not merely merged, staged, or planned. If the change is
  behind a flag or a staged rollout, it is not yet live for the purpose of
  this rule.

- The documentation MUST match what actually shipped.

  Any drift discovered during implementation has been reconciled back into the
  artifacts, so the merged documentation describes the architecture as it was
  actually realized — not as it was first drafted.

- The change MUST be descriptive and decision-free.

  The edits describe the end state in the present tense. Where a significant
  decision drove the change, the artifact links to the RFC that records it,
  rather than restating the rationale.

- Review MUST be settled.

  Feedback gathered in the discussion thread is resolved, and the artifacts
  are stable.

- You MUST reconcile drift before merging.

  If the real architecture differs from the drafted documentation, fix the
  documentation first. Never merge a description you know to be wrong.

- You MUST squash-merge with the conventional message.

  `design: <short lowercase description>`. There is no number to assign and no
  index to update — this is a living document, not an archive.

- You MUST NOT merge without explicit instruction from the user.
