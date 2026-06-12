# Design Docs

**A template for maintaining a system's architectural artifacts via version control.**

This repository is the home of the design documentation for [Project Name]. It is the living, authoritative description of the system's architecture as it exists in production right now — the structures, the runtime behavior, the deployment topology, and the cross-cutting concerns — expressed through a coherent set of architectural views.

Design documentation answers _what the system looks like_. It complements two sibling repositories:

- The [software requirements specification (SRS)](https://github.com/kieranpotts/specs) records _what_ the system does — its requirements, defined in business terms.

- The [requests for comments (RFC)](https://github.com/kieranpotts/rfc) archive records _how_ significant technical decisions were made, and _why_.

- The [implementation plans](https://github.com/kieranpotts/plans) capture the strategy of introducing changes to code and configuration to satisfy the product requirements and architectural decisions.

This repository records the _as-is_ architecture that resulted from implementing those requirements and decisions. It is descriptive, not prescriptive. It captures the design that exists, not the requirements it must satisfy (those live in the SRS), nor the rationale for the choices behind it (that lives in the RFC archive).

This repository has no accompanying decision log. The RFS archive already serves this purpose. All architecturally-significant design decisions, and their rationale, is recorded here.

Like the SRS and RFC, this is living documentation. The artifacts on the `main` trunk MUST reflect the current state of the production system. A change to the architecture is merged into `main` _at the same time_ as the corresponding code and configuration are shipped to production, so the documentation never drifts from reality.


A template for new code repositories.

## 📓 Documentation

- [**Requirements**](./docs/requirements.md)
- [**Installation**](./docs/installation.md)
- [**Usage**](./docs/usage.md)
- [**Development**](./docs/development.md)

-----

Copyright © 2020-present Kieran Potts, [CC0 license](./LICENSE.txt)
