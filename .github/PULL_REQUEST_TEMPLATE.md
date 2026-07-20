Briefly describe the architecture change this documents — what the system looks
like after the change.

- Discussion thread: [Link] _(required)_
- RFC, if a significant decision drove this change: [Link] _(optional)_

> [!IMPORTANT]
> Please use the discussion thread linked above, not comments on this pull
> request, to provide feedback. This keeps the PR thread focused on the edit
> history of the design artifacts.

----

## Checklist

On opening this PR (open it as a draft):

- [ ] An associated discussion thread is opened and linked above.
- [ ] The `RECONCILE` label is added, if this is a drift correction.
- [ ] The edits describe the intended end state of the architecture, in the
  present tense.
- [ ] The edits are decision-free. Any significant decision behind the change
  links to its RFC, rather than restating the rationale.

Mark this PR ready for review when:

- [ ] The affected views are edited and ready for stakeholder review.
- [ ] No generic template text or unfilled placeholders remain.
- [ ] Every supporting artifact is referenced from its view's `README.md`.

Merge this PR when:

- [ ] The corresponding code, configuration, and infrastructure are live in
  production.
- [ ] The documentation matches what actually shipped (any drift reconciled back
  in).
- [ ] Review feedback in the discussion thread is resolved.
- [ ] The PR is squash-merged, with subject `design: <description>`.
- [ ] The associated discussion thread is closed.

> [!IMPORTANT]
> The `main` trunk represents the as-is state of the production system. Do NOT
> merge this PR before the architecture it describes is actually live in
> production.
