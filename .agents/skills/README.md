# Agent skills

The following skills are available to support the management of design docs
via AI agents.

- **[draft-design](./draft-design/):** \
  Scaffolds a PR that will propose changes to the system design.
  Cuts a `design/<slug>` branch from `main`, prepares the affected views for
  editing, and opens a pull request in a draft state.

- **[review-design](./review-design/):** \
  Checks the updated views and takes the pull request out of draft.

- **[complete-design](./complete-design/):** \
  Checks the design docs describe production as it now is, and merges the
  changes into the `main` trunk.

- **[reconcile-design](./reconcile-design/):** \
  Compares the design docs against the real production system, and
  drafts a design change to fix any drift it finds.

## Workflow

```mermaid
flowchart LR
  draft["🤖<br/><b>draft-design</b>"]:::agentic
  write["🧑<br/>edit design docs"]:::anthropic
  review["🤖<br/><b>review-design</b>"]:::agentic
  complete["🤖<br/><b>complete-design</b>"]:::agentic
  reconcile["🤖<br/><b>reconcile-design</b>"]:::agentic

  draft ==> write
  write ==> review
  review ==> complete
  complete -.-> reconcile

  classDef agentic fill:#cce5ff,stroke:#004085,color:#004085,stroke-width:2px
  classDef scripted fill:#e2e3e5,stroke:#4b5157,color:#383d41,stroke-width:2px
  classDef anthropic fill:#fff3cd,stroke:#856404,color:#856404,stroke-width:2px,stroke-dasharray:2 3
```

The agent skills in this project are focused on the mechanics of managing the
lifecycle of design docs.
For help with evolving the design — weighing up the trade-offs and settling on
architectural solutions to problems — you may instruct agents to use the
[**design**](https://github.com/kieranpotts/skills/tree/latest/dev/skills/design)
skill in my global skills collection.

## Compatibility

These skills are compatible with the [Agent Skills](https://agentskills.io/)
convention. Most agent harnesses support this convention natively, but
workarounds may be required for harnesses that do not.
