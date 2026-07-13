# Design

This section documents the current architecture of the production system — what
the system _looks like_ as-is.

These artifacts always reflect the system's current state in production. A
change to the architecture is introduced through a [design-change pull
request](../CONTRIBUTING.md) and merged into `main` only once the changes are
live in production. It means the design docs don't drift from reality.

The design docs are descriptive. They state what the architecture _is_, in the
present tense. They do not record the requirements the system satisfies — those
live in the [SRS](https://github.com/kieranpotts/specs) — nor the rationale for
the choices behind the design — that is captured in
[RFCs](https://github.com/kieranpotts/rfc).

## Architectural views

An architecture has several audiences asking different questions. An executive
wants the system at-a-glance. A programmer wants the logical and physical
breakdown of components. A performance engineer wants the runtime processes. An
operator wants the deployment topology. And so on.

Good design docs have separate architectural models for each of these concerns.
It means different stakeholders can go straight to the information they need,
and they view clean artifacts that are unpolluted by detail irrelevant to their
question.

The architectural views used in these design docs are extended from the [4+1
architectural view
model](https://en.wikipedia.org/wiki/4%2B1_architectural_view_model). The seven
views are arranged as an abstraction ladder – the most abstract views first,
with subsequent views incrementally becoming more concrete. A reader can stop at
whatever altitude answers their question.

The architectural views are:

- [**Conceptual**](./conceptual/): The whole system at-a-glance – major ports,
  system landscape, the shape of the whole.

- [**Logical**](./logical/): The composition of the system – functional
  components, responsibilities, relationships.

- [**Development**](./development/): How the codebase is organized – modules,
  layers, repositories, build artifacts.

- [**Process**](./process/): How the system runs – processes, services,
  concurrency, communication.

- [**Physical**](./physical/): Where the system lives – hosts, networks,
  environments, deployment topology.

- [**Technical**](./technical/): What the system is built from – languages,
  runtimes, system software.

- [**Scenarios**](./scenarios/): How it all fits together – key end-to-end flows
  cross-cutting through the other views.
