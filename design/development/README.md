# Development view

This view describes the static organization of the implementation — the
repositories the code is divided between, the dependencies between them, the
filesystem structures within each repository, and the build and packaging
artifacts that are produced.

Code, as it exists on disk, is mapped to the [logical](../logical/)
architecture. This is one of the most useful views for developers, as it answers
the question "how is the codebase laid out?"

It includes:

- **Code organization.** The repositories, modules, packages, and layers the
  implementation is divided into, and the responsibility of each. Directory and
  package diagrams are useful here.

- **Layering and dependency rules.** The permitted dependency directions between
  layers or modules — what may depend on what, and what must not.

- **Build and packaging artifacts.** What the build produces — libraries,
  services, images, bundles — and how the source maps to those artifacts.

- **Shared code and ownership.** Shared libraries, internal packages, and
  code-ownership boundaries between teams, where relevant.

- **Mapping to the logical view.** Which modules realize which
  [logical](../logical/) components, especially where one does not map cleanly
  onto the other.
