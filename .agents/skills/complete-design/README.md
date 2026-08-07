# Complete design

Checks that the design docs describe production as it now is, then merges the
change into the `main` trunk.

Squash-merges the pull request, deletes the branch, and closes the discussion
thread that carried the review. The gate it enforces is the one the whole
repository rests on: documentation never lands ahead of production.

## Interactivity

Interactive. The agent may prompt for which design change to land, and it MUST
obtain explicit confirmation from the user before merging. It cannot be run
unattended, by design — the merge republishes the authoritative description of
the production architecture.

## How to invoke

Run from a `design/<slug>` branch:

> Complete design

> Ship this design change

> The change is live

> Merge the design docs

> Land the design change

Or describe which design change to land:

> The billing service extraction is now live in production.

## Recommended models

A mid-tier model. The merge itself is mechanical, but confirming that the
documentation matches what actually shipped is a judgment call, and getting it
wrong puts a false description on `main`.

## Suggested workflows

Run last, and only after the corresponding code and configuration are live in
production. If implementation diverged from what was drafted, fix the artifacts
on the branch first and let them go back through review — this skill will not
edit them for you.

## Related skills

- [**draft-design**](../draft-design/) \
  Opens the branch, pull request, and discussion thread that this skill
  eventually merges and closes.

- [**review-design**](../review-design/) \
  Takes the pull request out of draft. This skill refuses to merge until that
  has happened.

- [**reconcile-design**](../reconcile-design/) \
  Sits outside this lifecycle. Its corrective pull requests still land through
  this skill, but their production change is live before drafting even begins.

## References

- [CONTRIBUTING.md](../../../CONTRIBUTING.md) \
  The repository's documented workflow for introducing a design change, of
  which this skill automates steps 10 and 11.
