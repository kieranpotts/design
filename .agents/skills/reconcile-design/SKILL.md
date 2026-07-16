---
name: reconcile-design
description: >-
  Detect and correct drift between the design
  documentation on main and the real production system. Scaffolds a design change
  to bring the artifacts back in line with production. Use when the user says "the
  design docs are out of date", "reconcile the design docs", "check the docs
  against the code", or "the architecture has drifted".
license: CC0-1.0
metadata:
  interactive: yes
---

# Reconcile design

Use this skill to find and correct drift — places where the design documentation
on `main` no longer matches the real production system, because a change shipped
without the documentation being updated.

The documentation's entire value rests on one promise: that `main` describes
production. Drift breaks that promise. This skill restores it by comparing the
artifacts against reality and scaffolding a design change to fix the gaps.

Do NOT use this skill to document a _new_ change going through review — use
[`/draft-design`](../draft-design/SKILL.md). Do NOT use it to merge — use
[`/ship-design`](../ship-design/SKILL.md).

## What "drift" means here

Drift is documentation that contradicts the current production system: a
component that was renamed, split, or removed; a runtime topology that changed;
a data store that was replaced; a flow that now takes a different path.
Reconciliation makes the documentation true again — it describes the _present_
state, never a history of the change.

Because the production change is _already_ live, the gate that normally blocks
merging (the production change must be live first) is already satisfied.
Reconciliation is the one case where the documentation legitimately lags
production and is being caught up.

## Instructions

1.  **Establish the sources of truth.**

    Identify what to compare the documentation against — the code repositories,
    infrastructure-as-code, configuration, deployment manifests, and any
    running-system inspection the user can point you to. Ask the user for the
    relevant locations if they are not obvious.

2.  **Compare each view against reality.**

    Walk the seven [design views](../../../design/) and check each against the
    corresponding source of truth:

    - **Conceptual**: Do the documented major parts and system landscape still
      match the system as a whole?
    - **Logical**: Do the documented components, responsibilities, and
      relationships still match the code's structure?
    - **Development**: Do the documented modules, layers, and build artifacts
      match the actual repositories?
    - **Process**: Do the documented runtime units, communication, and
      concurrency match what actually runs?
    - **Physical**: Does the documented deployment topology match the actual
      infrastructure?
    - **Technical**: Do the documented languages, runtimes, and system software
      match the stack actually in production?
    - **Scenarios**: Do the traced end-to-end flows still play out as
      documented?

    Record each discrepancy: what the documentation says, what production
    actually does, and which view and artifact is affected.

3.  **Report the drift and confirm scope.**

    Present the list of discrepancies to the user. Confirm which to correct now
    — a single reconciliation change should address one coherent area of drift,
    not sweep up unrelated gaps into one un-reviewable PR. If the drift spans
    several unrelated areas, recommend separate reconciliation changes.

4.  **Scaffold the correction.**

    Hand off to the same scaffolding mechanics as
    [`/draft-design`](../draft-design/SKILL.md): cut a `design/<slug>` branch
    from `main` (a slug like `reconcile-billing-topology`), edit the affected
    views to describe the _current_ production state, commit with a `design:
    <description>` message, open a draft pull request, and open a linked
    discussion thread.

5.  **Note the absence of an RFC, where applicable.**

    If a discrepancy reflects an architecturally significant change that shipped
    _without_ going through the RFC process, flag it to the user — the decision
    record may be missing and worth backfilling in the
    [RFC](https://github.com/kieranpotts/rfc) repository. Reconciling the
    documentation does not substitute for the missing decision record.

## Rules

-   **Describe the present, not the change.**

    The corrected artifacts describe production as it is _now_, in the present
    tense. Do not narrate what changed or when — the Git history records that.

-   **Compare against reality, not assumptions.**

    Base every correction on an actual source of truth — code, configuration,
    infrastructure — not on what the architecture "should" be. If you cannot
    verify a section against a real source, say so rather than guessing.

-   **Keep reconciliation changes coherent and reviewable.**

    One area of drift per change. Do not bundle unrelated corrections.

-   **Ship via the normal gate.**

    A reconciliation change still lands through
    [`/ship-design`](../ship-design/SKILL.md). Because the production change is
    already live, the gate is satisfied — but the change is still reviewed and
    merged through a pull request, not committed directly to `main`.

## Success criteria

- A list of drift discrepancies is reported, each naming the affected view and
  artifact.

- A `design/<slug>` branch and draft pull request are scaffolded, correcting one
  coherent area of drift, with the artifacts describing the current production
  state.

- An associated discussion thread is open and linked.

- Any significant change that bypassed the RFC process is flagged to the user.

## References

- [`AGENTS.md`](../../../AGENTS.md): The "`main` describes production" rule.
