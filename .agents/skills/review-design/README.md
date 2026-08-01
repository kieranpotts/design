# Review design

Takes a design change's pull request out of draft once the affected views
describe real content.

## What it does

- Identifies the design change from the current branch (or asks).

- Diffs the branch against `main` and checks every touched view has real
  descriptive prose, not just a marker left for the author.

- Marks the pull request ready for review (`gh pr ready`).

## How to invoke

Run from a `design/*` branch:

> Review design

> This design change is ready for review.

Or specify the target PR:

> Review #42

## Notes

This is a light check, not a completeness gate — wording MAY still evolve
based on review feedback. Landing the change also requires the production
change to be live — see
[`/complete-design`](../complete-design/README.md).
