---
name: reconcile-design
description: >-
  Detect drift between the design documentation on `main` and the real
  production system, and draft a corrective design change. Use when the user
  says something like "the design docs are out-of-date", "reconcile the design
  docs", "check the docs against the code", or "the architecture has drifted
  from the docs". Do not use it to document a forward-looking change that has
  not shipped yet.
compatibility: >-
  requires Read, Write, Edit, Glob, Grep, Agent, Bash (git, gh)
license: CC0-1.0
---

# Reconcile design

Find and correct drift — places where the design documentation on `main` no
longer matches the real production system, because a change shipped without the
documentation being updated. Compare the artifacts against reality, report what
you find, then draft a corrective change for the gaps the user picks.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **Sources of truth — REQUIRED.** What to compare the documentation against:
  code repositories, infrastructure-as-code, configuration, deployment
  manifests, or inspection of the running system. These live outside this
  repository, so resolve them from the session context, then from the
  environment, then by asking the user. Never assume a path.

- **Known area of drift — OPTIONAL.** Narrows the comparison to one view or
  one part of the system. All eight [design views](../../../design/) are
  checked when it is absent.

## Success criteria

- A list of drift discrepancies MUST have been reported to the user, each
  naming the affected view and artifact, what the documentation says, and what
  production actually does.

- A `design/<slug>` branch MUST exist carrying corrections for one coherent
  area of drift, with the affected artifacts describing the current production
  state in the present tense.

- A draft pull request and a linked discussion thread MUST be open for that
  branch, following the repository's documented workflow for a design change.

- Any architecturally significant change that reached production without an
  RFC MUST have been flagged to the user.

- Every correction MUST have been committed on the `design/<slug>` branch, and
  you MUST NOT have committed anything directly to `main`. A reconciliation is
  still a reviewed change, even though production is already ahead of the
  documentation.

## Instructions

1.  Establish the sources of truth.

    Identify what to compare the documentation against, and confirm you can
    actually read it. Ask the user for the locations if they are not obvious
    from the context or the environment.

2.  Compare each view against reality.

    Where the drift area was named, walk that one view yourself. Where it
    was not — the default, checking all eight — fan the comparison out
    instead: spawn one sub-agent per view, each given the view's documented
    state and the sources of truth from step 1, tasked narrowly with
    comparing the two and returning a flat list of discrepancies. Reading
    and comparing all eight views serially in your own context is the
    expensive part; delegating each view to its own sub-agent keeps your
    context to the returned discrepancy lists, not the full source material
    for all eight.

    Each view compares against the corresponding source of truth as follows:

    - Conceptual: do the documented major parts and system landscape still
      match the system as a whole?
    - Logical: do the documented components, responsibilities, and
      relationships still match the code's structure?
    - Development: do the documented modules, layers, and build artifacts
      match the actual repositories?
    - Process: do the documented runtime units, communication, and
      concurrency match what actually runs?
    - Physical: does the documented deployment topology match the actual
      infrastructure?
    - Technical: do the documented languages, runtimes, and system software
      match the stack actually in production?
    - Scenarios: do the traced end-to-end flows still play out as documented?
    - Concepts: do the documented crosscutting concerns — domain model,
      security, persistence, error handling, observability — still match how
      they are applied system-wide?

    Record each discrepancy: what the documentation says, what production
    actually does, and which view and artifact is affected.

3.  Report the drift and confirm the scope of the correction.

    Present the list of discrepancies to the user and confirm which to correct
    now. Where the drift spans several unrelated areas, recommend a separate
    reconciliation for each.

4.  Draft the correction.

    Follow the repository's documented workflow for introducing a design
    change, in [CONTRIBUTING.md](../../../CONTRIBUTING.md): cut a
    `design/<slug>` branch from `main` — a slug such as
    `reconcile-billing-topology` — edit the affected views to describe the
    current production state, commit with an `update: <description>` message,
    open a draft pull request, and open a discussion thread cross-linked with
    it.

5.  Note the absence of an RFC, where applicable.

    If a discrepancy reflects an architecturally significant change that
    shipped without going through the RFC process, flag it to the user. The
    decision record may be missing and worth backfilling in the
    [RFC](https://github.com/kieranpotts/rfc) repository. Reconciling the
    documentation does not substitute for the missing decision record.

6.  Output a summary of your actions, listing every discrepancy found and
    naming which of them the drafted branch corrects.

## Rules

- You MUST describe the present, not the change.

  The corrected artifacts describe production as it is now, in the present
  tense. Do not narrate what changed or when — the Git history records that.

- You MUST compare against reality, not assumptions.

  Base every correction on an actual source of truth — code, configuration,
  infrastructure. If you cannot verify a section against a real source, report
  it as unverified rather than guessing at what the architecture "should" be.

- You MUST keep each reconciliation coherent and reviewable.

  One area of drift per change. Bundling unrelated corrections produces a pull
  request nobody can review.

- You MUST report the full set of discrepancies, even those you do not
  correct.

  The user needs the whole picture to decide what to schedule next. Silently
  narrowing to one area hides the rest of the drift.

- A sub-agent spawned in step 2 MUST only compare its one assigned view
  against its source of truth and return discrepancies. It MUST NOT draft a
  correction, judge priority, or decide what an RFC gap means — that
  synthesis needs the full picture across every view, which only you have
  once they all report back.

- Corrections MUST ship through the normal review gate.

  Because the production change is already live, the constraint that blocks
  landing documentation ahead of production is already satisfied — but the
  correction is still reviewed and merged through a pull request, never
  committed directly to `main`.

## Edge cases

- The documentation is right and production is wrong.

  What you found is an unintended regression, not documentation drift. Report
  it to the user and do not "correct" the documentation to match. Fixing
  production is out of scope for this skill.

- The drift is so large that the affected view needs rewriting outright.

  Say so, and confirm the scope with the user before starting. A wholesale
  rewrite is still one coherent area of drift, but it is worth an explicit
  decision rather than being arrived at by accident.
