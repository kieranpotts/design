---
name: ship-design
description: Land a design change once the production change it describes is live. Mark the PR ready, squash-merge it to main, and close the discussion thread. Use when the user says "ship this design change", "the change is live", "merge the design docs", or "land the design change".
license: CC0-1.0
---

# Ship design change

Use this skill to land a design change — to merge it into `main` once the corresponding production change is live. This is the gate that protects the repository's core promise: **`main` describes production**.

Do NOT use this skill to scaffold a change — use [`draft-design`](../draft-design/SKILL.md). Do NOT use it to correct drift — use [`reconcile-design`](../reconcile-design/SKILL.md).

## Gate: the production change MUST be live

A design change MUST NOT land on `main` until the architecture it describes actually exists in production. Confirm _all_ of the following before merging. If any is unmet, report it and pause.

-   **The production change is live.**

    The corresponding code, configuration, and infrastructure are deployed and serving real users — not merely merged, staged, or planned. If the change is behind a flag or a staged rollout, it is not yet live for the purpose of this gate.

-   **The documentation matches what actually shipped.**

    Any drift discovered during implementation has been reconciled back into the artifacts, so the merged documentation describes the architecture as it was actually realized — not as it was first drafted.

-   **The change is descriptive and decision-free.**

    The edits describe the end state in the present tense. Where a significant decision drove the change, the artifact links to the RFC that records it, rather than restating the rationale.

-   **Review is settled.**

    Feedback gathered in the discussion thread is resolved, and the artifacts are stable.

## Instructions

1.  **Identify the design change.**

    Infer the target from the checked-out branch (`design/<slug>`). If on `main`, use the user's description, or list open design-change pull requests and ask the user to choose:

    ```sh
    gh pr list --search "design:" --json number,title,headRefName
    ```

2.  **Verify the gate.**

    Confirm the production change is live and the documentation matches it. Report any unmet condition and stop. Do not take the user's word for "it's live" if you can check — but do not block on checks you cannot perform; surface what you could not verify.

3.  **Mark the pull request ready for review, if still a draft.**

    ```sh
    gh pr ready <number>
    ```

4.  **Merge the pull request.**

    Confirm with the user that the PR is ready to merge — do not merge without explicit instruction. Once confirmed, squash-merge it with a `design: <description>` message:

    ```sh
    gh pr merge <number> --squash --subject "design: <short lowercase description>"
    ```

    Delete the branch if it is not deleted automatically.

5.  **Close the discussion thread.**

    The thread has served its purpose. Close it via the GraphQL API:

    ```sh
    gh api graphql -f query='
      mutation($id:ID!) {
        closeDiscussion(input:{discussionId:$id}) { discussion { url } }
      }' -F id=<discussionId>
    ```

## Rules

-   **Never land ahead of production.**

    This is the one rule the whole repository depends on. If the production change is not live, do not merge — full stop.

-   **Reconcile drift before merging.**

    If the real architecture differs from the drafted documentation, fix the documentation first. Never merge a description you know to be wrong.

-   **Squash-merge with the conventional message.**

    `design: <short lowercase description>`. There is no number to assign and no index to update — this is a living document, not an archive.

-   **Do not merge without explicit instruction.**

## Success criteria

- The corresponding production change is confirmed live.

- The PR is squash-merged into `main` with a `design: <description>` message, and the branch is deleted.

- The associated discussion thread is closed.

## References

- [`AGENTS.md`](../../../AGENTS.md): The full design-change workflow and the "`main` describes production" rule.
