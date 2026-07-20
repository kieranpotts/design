# Scenarios

This architectural view documents a small set of significant end-to-end flows,
tracing them through all the other architectural views. Example: a request
entering through a [deployed](../physical/) component, executing as runtime
[processes](../process/), and exercising [logical](../logical/) components built
from the [technical](../technical/) stack.

This is a cross-cutting viewpoint rather than a discrete architectural
abstraction level. Scenarios cut across all the other abstraction levels,
showing how real behavior is realized. They answer the question "how does the
architecture actually realize the important behaviors?"

By drawing threads through all the architectural views, scenarios force all the
other views to be aligned. They help to validate that all the architectural
views are consistent with one another. In the process of formalizing scenarios,
you will expose views that have drifted out of step with the others.

Scenarios include:

- **A handful of significant flows — not all of them.** Choose flows that are
  architecturally illuminating: the primary request path, a critical
  asynchronous workflow, a failure-and-recovery path, a cross-cutting concern
  exercised end-to-end (auth, an audit trail). A scenario earns its place by
  showing how the views interact, not by covering a feature. A scenario MAY
  reference an [SRS](https://github.com/kieranpotts/specs) journey or feature as
  the behavior it traces, but it describes the _architecture's realization_ of
  it, not the requirement.

- **End-to-end traces.** For each, follow the flow across the views: which
  [logical](../logical/) components are involved, which [runtime
  units](../process/) execute, across which [deployment](../physical/) topology.
  Sequence diagrams (in text) are the natural format for this model.

- **Cross-references.** Link each step to the artifact in the relevant view that
  defines the component, process, or host involved, rather than redescribing it
  here.

## Example: Acme Catalog & Storefront platform

> [!NOTE]
> This is a sample scenarios view, included to illustrate the format. It
> describes a fictional catalog and storefront platform for a fictional project
> ("acme") and is not one of this project's real architectural views.

Two scenarios are documented for the fictional Acme platform:

- [**Checkout**](./checkout.md) — the primary request path: a shopper reserves
  a product and completes payment. Traces the
  [`checkout-and-payments`](https://github.com/kieranpotts/specs) journey
  through every view.

- [**Payment provider outage**](./payment-provider-outage.md) — a
  failure-and-recovery path, showing how the architecture behaves when the
  Stripe payment service provider is unavailable.
