# Glossary

This glossary defines the architecture- and technical-specific terms used across
the design views — component names, runtime units, deployment concepts, and the
shorthand the artifacts rely on.

Domain and business terms are _not_ defined here. Those live in the system's
[requirements specification](https://github.com/kieranpotts/specs), which owns
the system's ubiquitous language. Where a domain term is unavoidable in an
architectural artifact, this glossary MAY restate it briefly for convenience,
with a link back to its authoritative definition in the SRS.

Terms are listed alphabetically. Keep each definition short — a sentence or two —
and describe what the term _means in this system_, not the general concept.

> [!NOTE]
> The terms below are sample entries, included to illustrate the format. They
> describe a fictional catalog and storefront platform for a fictional project
> ("acme") and are not this project's real glossary terms.

## Terms

**catalog-service**
: The [logical](./logical/) component that owns the product catalog, listings,
and reservation state for the fictional Acme platform. Realizes the [Acme
Catalog API](https://github.com/kieranpotts/specs) domain. See the
[logical view](./logical/) for its full responsibilities.

**domain-kit**
: A shared, versioned internal package containing domain event schemas, HTTP
client SDKs, and logging/tracing conventions common to Acme's backend
services. Not a deployable runtime unit itself — see the [development
view](./development/).

**notification-worker**
: The [runtime unit](./process/) that consumes order and reservation events
from the event bus and sends transactional email. Runs as a Kafka consumer
group with no HTTP surface. See the [process view](./process/).

**reservation**
: A domain term restated here for convenience: a time-bounded hold on a
product that prevents it being sold to another shopper while checkout is in
progress. The authoritative definition lives in the
[SRS](https://github.com/kieranpotts/specs).

**storefront-api**
: The [runtime unit](./process/) that acts as the backend-for-frontend and API
gateway between `storefront-web` and the domain services (`catalog-service`,
`payments-service`). Holds no persistent state of its own. See the [process
view](./process/).
