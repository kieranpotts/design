# 📐 Design Docs

**A template for maintaining a system's architectural artifacts**
via version control.

This repository is the home of the design documentation for [Project Name]. It
is the living, authoritative description of the system's architecture as it
exists in production right now – the structures, the runtime behavior, the
deployment topology, and the cross-cutting concerns – expressed through a
coherent set of architectural views.

The design docs are descriptive, not prescriptive. They capture the design
that exists, not the requirements it satisfies (those live in the
[requirements specification](https://github.com/kieranpotts/specs)), nor the
rationale for the choices behind it (that lives in the
[Requests for Comments](https://github.com/kieranpotts/rfc) archive).

This is living documentation. The artifacts on the `latest/main` trunk reflect
the current state of the production system. A change to the architecture is
merged into `latest/main` _at the same time_ as the corresponding code and
configuration are shipped to production, so the documentation never drifts
from reality.

Design docs are central to architectural knowledge management (AKM) – the
practice of capturing, organizing, sharing, and preserving the knowledge that
shapes a software system. Keeping these artifacts under version control, in
sync with production, is what makes that knowledge explicit and durable rather
than tacit and fragile.

> [!NOTE]
> See also [TS-3](https://kieranpotts.com/standards/003),
> a technical standard covering design docs, RFCs, and architecture audits.
> This repository is its reference implementation for design docs.

## Ecosystem

This repository is one of six that form a coherent, version-controlled
documentation ecosystem. Each answers a different question about a software
system.

- [**📋 Software Requirements Specification (SRS)**](https://github.com/kieranpotts/specs) \
  Captures what the system does today, plus proposals being discussed to change
  the requirements.

- [**📐 Design Docs**](https://github.com/kieranpotts/design) (this repository) \
  Architectural views representing the as-is production system, plus proposals
  to evolve the architecture to meet new requirements.

- [**🗺️ Delivery Plans**](https://github.com/kieranpotts/plans) \
  Roadmaps, milestones, and the decomposition of work into independently
  shippable increments.

- [**💬 Requests for Comments (RFC)**](https://github.com/kieranpotts/rfc) \
  An historical record of key design and technical decisions, plus active
  proposals and their discussion threads.

- [**🔍 Architecture Audits**](https://github.com/kieranpotts/audits) \
  Point-in-time evaluations of the structural integrity of the code and data,
  which drive refactoring work.

- [**⚠️ Risk Register**](https://github.com/kieranpotts/risks) \
  Security and privacy risks inherent in the system, and the implementation
  status of mitigation strategies. Plus an archive of past threat modeling
  workshop reports.

In addition, the [**✨ Agent Skills**](https://github.com/kieranpotts/skills)
collection offers composable agentic workflows that operate across all six
repositories.

This separation into dedicated repositories is intended for application software
that spans multiple code repositories, and potentially multiple teams, where the
requirements, decisions, designs, plans, audits, and risks are shared concerns
that sit above any single codebase.

For a standalone code repository – a small utility library, say – it may be
better to fold all documentation into the same repository.

## Contents

- [**Design**](./design/) \
  The architectural artifacts, organized into views.

- [**Contributing**](./CONTRIBUTING.md) \
  Step-by-step instructions for keeping the design documentation synchronized
  with the production system.

- [**Agents**](./AGENTS.md) and [**Skills**](./.agents/skills/) \
  Instructions for agent tools to maintain the design documentation with a
  high degree of autonomy.

- [**Documentation**](./docs/) \
  General guidance on how to get the most out of architectural documentation –
  what to record, how to keep it honest, and how it relates to the SRS and RFC
  processes.

-----

Copyright © 2020-present Kieran Potts, [CC0 license](./LICENSE.txt)
