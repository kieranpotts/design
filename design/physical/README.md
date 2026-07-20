# Physical view

The physical architectural view describes the deployment topology – how the
software maps onto infrastructure: hosts, networks, data stores, environments,
and runtime placement.

This view maps the runtime [processes](../process/) to executables that sit on
real or virtual infrastructure. The [process](../process/) architecture
describes "what runs"; the physical architecture describes "where it runs".
Without this view, you wouldn't know if those processes were deployed to a
single host, a cluster, or a serverless platform.

It includes:

- **Deployment topology.** The hosts, containers, clusters, or serverless
  platforms the software runs on, and which runtime units are placed where.
  Deployment diagrams (in text) are used for this modeling.

- **Environments.** The distinct environments (production, staging, etc.) and
  the significant ways their topologies differ.

- **Networks and boundaries.** Network segmentation, ingress and egress points,
  load balancers, gateways, and trust boundaries.

- **Data stores and infrastructure services.** Databases, caches, queues, object
  stores, and managed infrastructure services, and where they sit in the
  topology.

- **External dependencies.** Third-party and external systems the deployment
  integrates with, at the infrastructure level.

- **Scaling and availability topology.** Replication, redundancy, regions, and
  availability zones, as they are actually deployed.

## Example: Acme Catalog & Storefront platform

> [!NOTE]
> This is a sample physical view, included to illustrate the format. It
> describes a fictional catalog and storefront platform for a fictional project
> ("acme") and is not one of this project's real architectural views.

The platform runs on AWS, on Amazon EKS (Kubernetes), in the `eu-west-1`
region. The full deployment topology, including the diagram and per-service
placement, is documented in
[`deployment-topology.md`](./deployment-topology.md).

Summary: each backend service (`storefront-api`, `catalog-service`,
`payments-service`, `notification-worker`) runs as a Kubernetes `Deployment` in
its own namespace, fronted by an AWS Application Load Balancer via an ingress
controller. `storefront-web` is served from a CDN (Amazon CloudFront) backed by
the same EKS cluster. Data stores are managed AWS services outside the
cluster: Amazon RDS for PostgreSQL (one instance per domain service), Amazon
ElastiCache for Redis (shared cache), and Amazon MSK (managed Kafka) for the
event bus.
