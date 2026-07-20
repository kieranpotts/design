# 📐 Design Docs

**A template for maintaining a system's architectural artifacts via version control.**

This repository is the home of the design documentation for [Project Name]. It
is the living, authoritative description of the system's architecture as it
exists in production right now – the structures, the runtime behavior, the
deployment topology, and the cross-cutting concerns – expressed through a
coherent set of architectural views.

The design docs are descriptive, not prescriptive. They capture the design
that exists, not the requirements it satisfies (those live in the
[SRS](https://github.com/kieranpotts/specs)), nor the rationale for the
choices behind it (that lives in the [RFC](https://github.com/kieranpotts/rfc)
archive).

This is living documentation. The artifacts on the `main` trunk reflect the
current state of the production system. A change to the architecture is merged
into `main` _at the same time_ as the corresponding code and configuration are
shipped to production, so the documentation never drifts from reality.

> [!NOTE]
> See **[TS-3: Design Docs](https://github.com/kieranpotts/standards/tree/latest/dev/src/003)**.
> for more guidance on maintaining design docs.

## Ecosystem

This repository is one of six that form a coherent, version-controlled
documentation ecosystem. Each answers a different question about a software
system.

- [**📋 Software Requirements Specification (SRS)**](https://github.com/kieranpotts/specs) \
  Captures what the system does, in business terms.

- [**💬 Requests for Comments (RFC)**](https://github.com/kieranpotts/rfc) \
  Records how significant technical decisions were made, and why.

- [**📐 Design Docs**](https://github.com/kieranpotts/design) (this repository) \
  Documents what the system looks like in production.

- [**🔍 Architecture Audits**](https://github.com/kieranpotts/audits) \
  Logs historical evaluations of the as-built system's structural integrity.

- [**🗺️ Delivery Plans**](https://github.com/kieranpotts/plans) \
  Tracks when, and in what order, the work gets done.

- [**⚠️ Risk Register**](https://github.com/kieranpotts/risks) \
  Records the inherent security and privacy risks the system carries.

In addition, the [**✨ Agent SKills**](https://github.com/kieranpotts/skills)
collection offers composabe agentic workflows that operate across all six
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
  Instructions for agents tools to maintain the design documentation with a
  high degree of autonomy.

- [**Documentation**](./docs/) \
  General guidance on how to get the most out of architectural documentation –
  what to record, how to keep it honest, and how it relates to the SRS and RFC
  processes.

-----

Copyright © 2020-present Kieran Potts, [CC0 license](./LICENSE.txt)
