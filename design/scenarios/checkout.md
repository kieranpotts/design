# Scenario: Checkout

> [!NOTE]
> This is a sample scenario, included to illustrate the format. It describes a
> fictional catalog and storefront platform for a fictional project ("acme")
> and is not one of this project's real architectural views. It is referenced
> from the [scenarios view README](./README.md).

This scenario traces a shopper reserving a product and completing payment —
the [`checkout-and-payments`](https://github.com/kieranpotts/specs) journey —
end-to-end through the architecture.

## Trace

```mermaid
sequenceDiagram
    actor Shopper
    participant Web as storefront-web
    participant API as storefront-api
    participant Catalog as catalog-service
    participant CatalogDB as catalog-db
    participant Payments as payments-service
    participant Stripe
    participant Bus as Kafka (acme.orders)
    participant Notify as notification-worker
    participant SES as Amazon SES

    Shopper->>Web: Add product to cart, click "Checkout"
    Web->>API: POST /checkout {cartId}
    API->>Catalog: POST /reservations {productId}
    Catalog->>CatalogDB: SELECT ... FOR UPDATE, insert hold
    CatalogDB-->>Catalog: hold created
    Catalog-->>API: 201 checkout hold held
    API->>Payments: POST /payments {holdId, idempotencyKey}
    Payments->>Stripe: Authorize + capture card
    Stripe-->>Payments: payment captured
    Payments-->>API: 200 payment captured
    API->>Catalog: POST /reservations/:id/confirm
    Catalog-->>API: 200 hold confirmed, product sold
    API-->>Web: 200 order confirmed
    Web-->>Shopper: Order confirmation page
    Payments->>Bus: publish order.placed
    Bus->>Notify: deliver order.placed
    Notify->>SES: send confirmation email
```

## Views exercised

- **[Logical](../logical/)** — `storefront-api`, `catalog-service`, and
  `payments-service` collaborate synchronously; `notification-worker` reacts
  asynchronously. See the [component model](../logical/#component-model).
- **[Process](../process/)** — the synchronous HTTP calls and the
  `order.placed` event publication follow the [communication
  patterns](../process/#communication) and the idempotency guarantee
  described under [concurrency and
  synchronization](../process/#concurrency-and-synchronization).
- **[Physical](../physical/)** — all requests enter through the ALB and are
  routed to pods within the `acme-prod` EKS cluster; see the [deployment
  topology](../physical/deployment-topology.md).
- **[Technical](../technical/)** — the checkout hold uses a PostgreSQL
  row-level lock; the event bus is Amazon MSK (Kafka); see the
  [technical view](../technical/).
- **[Concepts](../concepts/)** — payment idempotency and checkout-hold
  consistency are instances of the system-wide [error and failure
  handling](../concepts/) and [persistence](../concepts/) concepts.

## Notes

If the payment authorization step fails, the checkout hold is released
rather than confirmed — see the [payment provider outage
scenario](./payment-provider-outage.md) for that path.
