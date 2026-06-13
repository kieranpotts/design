# `/draft-design`

Scaffolds a design change, ready for the author to edit the affected architectural views.

## What it does

- Creates a `design/<slug>` branch from `main`.

- Works out which [design views](../../../design/) the change touches.

- Edits the affected views to describe the intended end state — or leaves clear markers for the author.

- Commits and pushes the change.

- Opens a draft pull request titled `design: <description>`.

- Opens a discussion thread and cross-references it from the PR.

## How to invoke

```
/draft-design
```

Optionally, describe the change:

```
/draft-design We will extract billing into its own service, consuming order events off the bus
```

## Examples

- `/draft-design`: The agent prompts you for details, then scaffolds the branch and a draft PR.

- `/draft-design <Description>`: Provide details of the architecture change, from which the agent infers the slug and the affected views, and drafts the edits.

Refine the artifacts yourself, gather feedback in the discussion thread, then use [`/ship-design`](../ship-design/README.md) to land the change once it is live in production.
