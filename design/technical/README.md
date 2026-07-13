# Technical view

This section documents the technology stack of the application layer — the
programming languages, runtimes, and system software the production system is
built from.

This is the most concrete of all the architectural views. It answers the
question "what materials is the application made from?" It names real products
and their version numbers. Where the [conceptual](../conceptual/) view names the
major parts, and other views between describe the structure and behavior of
those parts, the technical view records what those parts are concretely made of.

The same stack may be deployed across many [hardware topologies](../physical/),
and the same topology may host different stacks.

It includes:

- **Languages and runtimes.** The programming languages and the runtime
  environments (and their versions) the system runs on in production.

- **System software.** The databases, message brokers, caches, web servers, and
  other infrastructure software the system depends on, named and versioned.

- **Significant platform components.** Operating systems, container runtimes,
  and managed platform services that materially shape how the system runs, where
  naming them adds clarity.

- **Links to technical decision log.** For each significant technology, a link
  to the [RFC](https://github.com/kieranpotts/rfc) that records the decision to
  adopt it.
