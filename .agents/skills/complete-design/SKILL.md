---
name: complete-design
description: >-
  Land a design change in the `main` trunk, once the corresponding production
  change is live. Use when the user says something like "complete design",
  "ship this design change", "the change is live", "merge the design docs", or
  "land the design change". Do not use it to take a pull request out of draft,
  or to merge documentation for a change that has not yet shipped.
compatibility: >-
  requires Read, Bash (git, gh)
license: CC0-1.0
---

# Complete design

Merge a design change into the `main` trunk, and close the discussion thread
that carried its review. Merge only once the corresponding production change is
live and the user has explicitly told you to go ahead.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **Target — REQUIRED.** The design change to land. Infer it from the
  checked-out branch (`design/<slug>`). If `main` is checked out, use the
  user's description, or list the open design-change pull requests and ask the
  user to choose:

  ```sh
  gh pr list --json number,title,headRefName \
    --jq '[.[] | select(.headRefName | startswith("design/"))]'
  ```

- **Description — REQUIRED.** The short prose title of the change, in the
  present tense, full lowercase, and not terminated by a period, eg. `extract
  the billing service`. Take it from the pull request title, stripping the
  `create: ` or `update: ` prefix.

- **Confirmation to merge — REQUIRED.** Explicit instruction from the user
  that the pull request is to be merged now. Do not infer it from the fact
  that the skill was invoked.

## Success criteria

- The corresponding production change MUST have been confirmed live, and
  anything you could not verify MUST have been surfaced to the user before the
  merge.

- A single new squash commit MUST exist on `main`, its message of the form
  `update: <description>`.

- The `design/<slug>` branch MUST no longer exist in the upstream repository.

- The discussion thread MUST be closed as resolved.

- You MUST NOT have edited any artifact under
  [`design/`](../../../design/). Correcting the documentation happens on the
  branch, before the merge gate, not during it.

## Instructions

1.  Identify the design change and its pull request.

2.  Verify the change is landable.

    Confirm the production change is live and that the documentation on the
    branch matches what actually shipped. Report any unmet condition and stop.
    Do not take the user's word for "it's live" if you can check — but do not
    block on checks you cannot perform; surface what you could not verify.

3.  Confirm the pull request is not a draft.

    ```sh
    gh pr view <number> --json isDraft
    ```

    If it is still a draft, stop, and tell the user it has to be taken out of
    draft and reviewed first.

4.  Merge the pull request.

    Ask the user to confirm the pull request is ready to merge, and wait for
    the answer. Once confirmed, squash-merge it and delete the source branch
    upstream:

    ```sh
    gh pr merge <number> --squash --subject "update: <description>" --delete-branch
    ```

5.  Delete the branch directly, if it was not deleted automatically.

    ```sh
    git push origin --delete design/<slug>
    ```

6.  Close the discussion thread as resolved.

    The thread has served its purpose. Find the discussion linked from the
    pull request body, look up its node ID, and close it (`gh` has no native
    discussion command, so use the GraphQL API):

    ```sh
    gh api graphql -f query='
      query($owner:String!, $name:String!, $number:Int!) {
        repository(owner:$owner, name:$name) { discussion(number:$number) { id } }
      }' -F owner=<owner> -F name=<repo> -F number=<discussionNumber>

    gh api graphql -f query='
      mutation($id:ID!) {
        closeDiscussion(input:{discussionId:$id, reason:RESOLVED}) { discussion { closed } }
      }' -F id=<discussionId>
    ```

7.  Output a summary of your actions, naming the merged pull request, the
    squash commit, and the closed discussion.

## Rules

- You MUST NOT land a design change ahead of production.

  This is the one rule the whole repository depends on. The artifacts on `main`
  are the authoritative record of the architecture as it exists right now, so
  merging early makes them a lie.

- The production change MUST be live to count.

  The corresponding code, configuration, and infrastructure are deployed and
  serving real users — not merely merged, staged, or planned. A change behind
  a flag or in a staged rollout is not yet live for the purpose of this rule.

- The documentation MUST match what actually shipped.

  Any drift discovered during implementation is reconciled back into the
  artifacts before the merge, so what lands describes the architecture as it
  was actually realized, not as it was first drafted. Never merge a
  description you know to be wrong.

- You MUST NOT merge a draft pull request.

  A draft has not been through review, and review is where the artifacts are
  checked for being descriptive and decision-free.

- Review MUST be settled before you merge.

  Feedback gathered in the discussion thread is resolved and the artifacts are
  stable.

- You MUST squash-merge, with an `update: <description>` message.

  There is no number to assign and no index to update — this is living
  documentation, not an archive, so the commit is the whole record.

- You MUST NOT merge without explicit instruction from the user.

  The merge is irreversible in effect: it republishes the authoritative
  description of the production architecture.

## Edge cases

- The pull request has merge conflicts with `main`.

  Another design change landed first. Stop and report it. Resolving the
  conflict is an edit to the artifacts, which belongs on the branch and back
  through review, not in the merge step.

- The pull request has no linked discussion thread.

  Merge as normal, but report the missing thread. Every design change is
  supposed to have one, so its absence is worth the user knowing about.
