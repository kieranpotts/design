# Overview

Design documentation is a living description of what a system's architecture
looks like today — its structures, its runtime behavior, and its deployment
topology, expressed through a coherent set of architectural views.

## Living documentation

Most architecture documents rot. Written once at the start of a project — often
as a slide deck or a wiki page — they are abandoned as the system evolves past
them. Within months they describe a system that no longer exists, and people
stop trusting them.

The fundamental issue is that the upkeep of design docs is an entirely separate
workflow from the development and maintenance of the system they document. The
solution is to keep design docs close to the code and configuration they
document, maintained under the same version control workflow, and deeply
integrated into the change management process.

This keeps the design docs bound to production. The [design
artifacts](../design/) on `main` describe the architecture as it runs for real
users right now. A change to those artifacts is not merged to `main` until the
corresponding change in code and configuration is itself live in production.

Old architecture is simply edited away from `main` as the production system
changes. The history of the architecture lives in the Git log.

The payoff is a single, trustworthy answer to "what does our architecture look
like?" New engineers, operators, reviewers, and auditors can read it and rely on
it.

## Descriptive

The documentation describes what the architecture _is_. It deliberately does not
record _why_ it is that way.

That separation of concerns helps to keep the design docs lightweight. The
rationale for a significant choice — the alternatives weighed, the trade-offs
accepted — belongs in the [RFC](https://github.com/kieranpotts/rfc) that records
the decision. The design artifacts state what exists and link to the RFCs for
the why.
