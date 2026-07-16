# Ship design

Lands a design change once the production change it describes is live.

## What it does

- Identifies the design change from the current branch (or asks).

- Verifies the gate: the corresponding production change is live, and the
  documentation matches what actually shipped.

- Marks the pull request ready for review, if still a draft.

- Squash-merges the PR to `main` with a `design: <description>` message, and
  deletes the branch.

- Closes the associated discussion thread.

## How to invoke

Run from a `design/<slug>` branch:

> Ship design

Or describe which design to ship:

> The billing service extraction is now live in production.

## Examples

- `/ship-design`: From a `design/<slug>` branch, the agent verifies the change
  is live, then merges and closes the thread (with your confirmation).

- `/ship-design <Description>`: From `main`, the agent finds the matching
  design-change PR and lands it.
