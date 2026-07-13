# Logical view

This architectural view decomposes the [conceptual](../conceptual/) architecture
into the major functional components of the system. It describes the
responsibilities of each major component, and how all the components relate.

It includes:

- **Component model.** The major logical components or modules of the system,
  each with a clear, single responsibility. C4-style container and component
  diagrams, authored in text, are used for this model.

- **Responsibilities.** For each component, what it owns and what it
  deliberately does not. Make the boundaries explicit.

- **Relationships.** How components depend on, call, or collaborate with one
  another, and the direction of those dependencies.

- **Key abstractions and patterns.** The architectural patterns the structure
  embodies (layering, hexagonal ports/adapters, event-driven, etc.), described
  as the structure they produce — not as a choice being justified.

- **Domain mapping.** How the logical components relate to the domain model
  defined in the [SRS](https://github.com/kieranpotts/specs), where that mapping
  is not obvious.
