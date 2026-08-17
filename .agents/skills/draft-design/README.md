# Draft design

Scaffolds a pull request that will propose changes to the system design.

Cuts a `latest/design/<slug>` branch from `latest/main`, writes `TODO:` markers
into the design views the change will touch, opens a pull request in a draft
state, and opens the linked discussion thread where review feedback is gathered.
It does not write the description of the new architecture — that is the author's
job.

## Interactivity

Interactive. The agent may prompt for the description of the design change, and
for which design views the change affects when the blast radius is not obvious
from the description alone. It does not run unattended.

## How to invoke

> Draft design

> Draft a design change

> New design change

> Document this architecture change

> Update the design docs

> We will extract billing into its own service, consuming order events off
> the bus. Draft changes to the design.

## Recommended models

A fast, cheap model is sufficient. The work is mechanical Git and GitHub
bookkeeping; the only judgment required is guessing which views a change
touches, and the author corrects that when filling the markers in.

## Suggested workflows

Run this first, at the point a change to the production architecture is
decided and about to be built. If the change is architecturally significant,
record the decision as an RFC before drafting. The author then fills in the
`TODO:` markers, the pull request is taken out of draft for review, and it is
merged only once the corresponding production change is live.

Do not run it to document a change that has already shipped without
documentation — that is drift, and is corrected by reconciliation instead.

## Related skills

- [**review-design**](../review-design/) \
  Takes the pull request this skill opened out of its draft state, once the
  marked-up views have been filled in with real content.

- [**complete-design**](../complete-design/) \
  Merges the pull request into `latest/main`, once review is settled and the
  corresponding production change is live.

- [**reconcile-design**](../reconcile-design/) \
  Sits outside this lifecycle. It compares `latest/main` against the real
  production system and drafts a corrective design change when the two have
  diverged.

## References

- [CONTRIBUTING.md](../../../CONTRIBUTING.md) \
  The repository's documented workflow for introducing a design change, which
  this skill automates the first steps of.
