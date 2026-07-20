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

## Example: Acme Catalog & Storefront platform

> [!NOTE]
> This is a sample technical view, included to illustrate the format. It
> describes a fictional catalog and storefront platform for a fictional project
> ("acme") and is not one of this project's real architectural views.

### Languages and runtimes

| Component | Language | Runtime |
|---|---|---|
| `storefront-web` | TypeScript | Node.js 22 LTS (Next.js 15) |
| `storefront-api` | TypeScript | Node.js 22 LTS (Express 4) |
| `catalog-service` | TypeScript | Node.js 22 LTS (Express 4) |
| `payments-service` | TypeScript | Node.js 22 LTS (Express 4) |
| `notification-worker` | TypeScript | Node.js 22 LTS |

All backend services are packaged with `npm` and compiled with `tsc` ahead of
container build.

### System software

- **PostgreSQL 16** — primary datastore for `catalog-service` and
  `payments-service`, run as Amazon RDS instances.
- **Redis 7** — caching layer for catalog reads, run as Amazon ElastiCache.
- **Apache Kafka 3.7** (Amazon MSK) — event bus for order and reservation
  events.
- **NGINX Ingress Controller** — routes ALB traffic into the EKS cluster.

### Significant platform components

- **Kubernetes 1.30** (Amazon EKS) — container orchestration for all four
  backend services.
- **Docker** — container image format and build tooling for every deployable
  repository.
- **Amazon CloudFront** — CDN serving `storefront-web`.
- **Amazon S3** — object storage for product images.
- **GitHub** — source hosting and CI/CD (GitHub Actions) for all
  repositories, per RFC 0002 ("GitHub as the remote forge").
- **Trunk-based branching**, per RFC 0003 ("trunk-based branching"), is the
  branching model used across all Acme repositories; it materially shapes how
  frequently images are built and deployed from `main`.

### Links to technical decision log

- The choice of GitHub as the remote forge for all Acme repositories is
  recorded in
  [RFC 0002 — GitHub for remote forge](https://github.com/kieranpotts/rfc/tree/main/rfc/tooling/acme-github-for-remote-forge).
- The trunk-based branching model used across all backend and frontend
  repositories is recorded in
  [RFC 0003 — trunk-based branching](https://github.com/kieranpotts/rfc/tree/main/rfc/process/acme-trunk-based-branching).
