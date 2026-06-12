# 📐 Design Docs

**A template for maintaining a system's architectural artifacts via version control.**

This repository is the home of the design documentation for [Project Name]. It is the living, authoritative description of the system's architecture as it exists in production right now – the structures, the runtime behavior, the deployment topology, and the cross-cutting concerns – expressed through a coherent set of architectural views.

Design documentation describes what the system looks like, answering the question "how are the requirements implemented?" It records the _as-is_ architecture that resulted from implementing the product requirements and technical decisions. It is descriptive, not prescriptive. It captures the design that exists, not the requirements it must satisfy (those live in the SRS), nor the rationale for the choices behind it (that lives in the RFC archive).

This repository has no accompanying decision log. The RFC archive already serves this purpose. All architecturally-significant design decisions, and their rationale, are recorded there.

Like the SRS and RFC, this is living documentation. The artifacts on the `main` trunk MUST reflect the current state of the production system. A change to the architecture is merged into `main` _at the same time_ as the corresponding code and configuration are shipped to production, so the documentation never drifts from reality.

## Ecosystem

This repository is one of four that form a coherent, version-controlled documentation ecosystem modeling the software development lifecycle. Each is the reference implementation of an opinionated workflow, and answers a different question about the system:

- [**📋 Software requirements specification (SRS)**](https://github.com/kieranpotts/specs): Records _what_ the system does, in business terms.

- [**💬 Requests for comments (RFC)**](https://github.com/kieranpotts/rfc): Records _how_ significant technical decisions were made, and _why_.

- **📐 Design docs**: Describe _what the system looks like_, its as-is architecture (this repository).

- [**🗺️ Implementation plans**](https://github.com/kieranpotts/plans): Capture _when, and in what order_, the work gets done.

The [**skills**](https://github.com/kieranpotts/skills) collection provides an agentic workflow that operates across all four.

This separation into dedicated repositories is intended for application software that spans multiple code repositories, and potentially multiple teams, where the requirements, decisions, designs, and plans are shared concerns that sit above any single codebase. For a standalone code repository – a small utility library, say – it is better to fold these artifacts and skills directly into that repository, rather than maintain them separately.

## Contents

- [**Design**](./design/): The architectural artifacts, organized into views. Covers the logical structure, the development organization, the runtime processes, the physical deployment, and the scenarios that tie them together.

- [**Contributing**](./CONTRIBUTING.md): Step-by-step instructions for keeping the design documentation synchronized with the production system.

- [**Agents**](./AGENTS.md) and [**Skills**](./.agents/skills/): Instructions for agentic tools to maintain the design documentation with a high degree of autonomy.

- [**Documentation**](./docs/): General guidance on how to get the most out of architectural documentation – what to record, how to keep it honest, and how it relates to the SRS and RFC processes.

-----

Copyright © 2020-present Kieran Potts, [CC0 license](./LICENSE.txt)
