# Draft design

Drafts a design change, ready for the author to edit the affected
architectural views.

## What it does

- Creates a `design/<slug>` branch from `main`.

- Works out which [design views](../../../design/) the change touches.

- Edits the affected views to describe the intended end state — or leaves clear
  markers for the author.

- Commits and pushes the change.

- Opens a draft pull request titled `design: <description>`.

- Opens a discussion thread and cross-references it from the PR.

## How to invoke

> Draft design

> We will extract billing into its own service, consuming order events off
> the bus. Draft changes to the design.

## Recommended models

A mid-tier model is worth it here — the skill edits the affected views to
describe the intended end state, which takes some architectural
understanding, not just filling in a template.

## Examples

- `/draft-design`: The agent prompts you for details, then drafts the
  branch and a draft PR.

- `/draft-design <Description>`: Provide details of the architecture
  change, from which the agent infers the slug and the affected views, and
  drafts the edits.

Refine the artifacts yourself, then use
[`/review-design`](../review-design/README.md) to take the PR out of draft and
gather feedback in the discussion thread. Once the change is live in
production, use [`/complete-design`](../complete-design/README.md) to land
it.
