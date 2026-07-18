# Crosscutting concepts

This architectural view documents the concepts that apply across the whole
system rather than living in any single component — the domain model, and the
system-wide approaches to persistence, security, error handling, and
observability.

This is a cross-cutting viewpoint rather than a discrete abstraction level.
Where the [scenarios](../scenarios/) view threads specific behaviors through the
other views, this view captures the recurring, system-wide _concerns_ that those
behaviors rely on. It answers the question "how does the system handle this
consistently, everywhere?" — so that a concept is described once, here, instead
of being rediscovered component by component.

It includes:

- **Domain model.** The shared entities and relationships the architecture is
  built around, and the language used to describe them. This describes the
  model as the system realizes it. The authoritative domain model lives in the
  system's [requirements specification](https://github.com/kieranpotts/specs),
  which this view cross-references.

- **Persistence and data.** How state is stored and represented as a consistent
  concept across the system — data ownership, the shape of the stores, and the
  conventions components follow when reading and writing.

- **Security.** The system-wide approach to authentication, authorization,
  secrets, and trust boundaries — the concerns every component inherits rather
  than solves for itself.

- **Error and failure handling.** The consistent approach to errors, retries,
  timeouts, and recovery — how failures surface and propagate across components.

- **Observability.** The logging, metrics, and tracing conventions the whole
  system adheres to, so behavior is legible in production.

- **Other system-wide concerns.** Where they materially shape the architecture,
  concepts such as internationalization, session and state handling, build and
  release, or API conventions each earn a place here.

Keep each concept descriptive and decision-free. Where a concept is the result
of a significant decision, link to the [RFC](https://github.com/kieranpotts/rfc)
that records it rather than restating the reasoning. Cross-reference the views
that realize each concept, and the [scenarios](../scenarios/) that exercise it.
