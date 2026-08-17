# Review design

Checks that the affected design views describe real content, and takes the
pull request out of draft.

The check is deliberately shallow. It confirms there is something for a
reviewer to respond to — not that the prose is finished, nor that the
architecture described is a good one.

## Interactivity

Interactive. When the target cannot be inferred from the checked-out branch,
the agent lists the open draft design pull requests and asks the user to
choose. Once the target is known the rest runs without prompting, and the agent
makes no edits of its own.

## How to invoke

Run from a `latest/design/<slug>` branch:

> Review design

> Review this design change

> This design change is ready for review.

> Take the design PR out of draft

> Mark the design change ready for review

Or specify the target pull request:

> Review #42

## Recommended models

A fast, cheap model is sufficient. The completeness check is a scan of the diff
for leftover placeholders, and the agent makes no edits of its own.

## Suggested workflows

Run once the design views on the branch have been filled in with real prose,
and before asking anyone to review. Do not run it on every push — flipping a
pull request out of draft is a signal to reviewers, so it is worth sending
only once.

## Related skills

- [**draft-design**](../draft-design/) \
  Opens the draft pull request, and the `TODO:` markers it leaves behind are
  exactly what this skill checks have since been replaced.

- [**complete-design**](../complete-design/) \
  Merges the pull request into `latest/main`, once review is settled and the
  corresponding production change is live.

- [**reconcile-design**](../reconcile-design/) \
  Sits outside this lifecycle, but the corrective pull requests it drafts
  rejoin it here, and are reviewed like any other design change.

## References

- [CONTRIBUTING.md](../../../CONTRIBUTING.md) \
  The repository's documented workflow for introducing a design change, of
  which this skill automates step 8.
