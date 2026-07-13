# Best practices

Practical guidance for writing and maintaining the design documentation.

## Describe the end state, not a changelog

A design change's edits SHOULD describe the architecture as it will be once the
change has shipped. They SHOULD NOT narrate the migration steps to get there.

The diff against `main` already shows what is changing. The prose SHOULD read as
a description of the destination, so that when the change ships the
documentation is simply true.

How a change is rolled out — sequencing, dual-running, cutover — is an
implementation concern and does not belong here.

## Keep it descriptive

Write in the present tense, stating what the architecture _is_ in production
right now, eg. "the billing service consumes order-placed events from the
message bus," not "we decided to introduce a billing service" or "the billing
service will consume…".

## Keep it decision-free

Do not justify the architecture here. When you feel the urge to write "we use an
event bus because…", that rationale belongs in the
[RFC](https://github.com/kieranpotts/rfc) that recorded the decision. Link to it
instead.

Two copies of a rationale inevitably drift apart. One authoritative copy, in the
RFC archive, with the design artifact pointing to it, keeps both honest.

Routine design details that never warranted an RFC need no link at all — they
are simply described.

## Put each artifact in the right view

The seven views exist so that each kind of statement has one home. Before adding
an artifact, ask which question it answers:

- "What is this system, at a glance?" → [conceptual](../design/conceptual/)
- "What is the system made of?" → [logical](../design/logical/)
- "How is the codebase laid out?" → [development](../design/development/)
- "What runs, and how do the pieces talk?" → [process](../design/process/)
- "Where does it run?" → [physical](../design/physical/)
- "What is it built from?" → [technical](../design/technical/)
- "How does a real flow play out end-to-end?" →
  [scenarios](../design/scenarios/)

When an artifact could sit in two views, put it where the reader most likely
looks first, and cross-reference from the other. Don't duplicate it.

## Author diagrams as text

Prefer text-based diagram formats — [Mermaid](https://mermaid.js.org/),
[PlantUML](https://plantuml.com/), [Structurizr
DSL](https://docs.structurizr.com/dsl) — over binary image exports.

Text diffs cleanly, reviews like code, and lives in version control next to the
prose it illustrates.

If a binary export is needed (for a slide, say), keep the textual source
alongside it and treat the source as authoritative.

## Right-size the detail

Document at the altitude that stays true as the code churns. Architecture
documentation that mirrors every class and method becomes a second copy of the
code — expensive to maintain and quickly wrong. Capture the structures,
boundaries, and interactions that a newcomer cannot easily infer from the code,
and let the code speak for the fine detail.

## Keep the documentation honest

The documentation's entire value rests on one promise: that `main` describes
production. Protect it.

Do not merge a design change until the change is actually live.

When implementation reveals the real architecture differs from what was drafted,
reconcile the difference back into the artifacts before merging. Never ship a
description you know to be wrong.

When you notice `main` has drifted from reality (a change shipped without
updating the docs), open a design change to correct it.

A description that is _mostly_ true is one nobody can trust.

## Use the discussion thread for debate

Every design change has a discussion thread, and that is where review feedback
and disagreement belong. It keeps the pull request's own history a clean record
of how the artifacts evolved.

Once the change is merged, the thread has served its purpose and can be closed.
