# Process view

This section documents the runtime architecture — the processes, threads, and services the system runs as, how they communicate and synchronize, and how concurrency is handled.

This view answers the questions "what is running?", "how is it threaded?", and "how do those processes talk and synchronize?"

The process view describes _what_ executes_ and _how_ it behaves at runtime, but it does not describe _where_ those executables are run – see the [physical](../physical/) view for that. The same process structure could be deployed across very different topologies without changing.

It includes:

- **Runtime units.** The processes, services, daemons, workers, and significant threads or thread pools the system runs as, and the responsibility of each.

- **Communication.** How the runtime units communicate — synchronous calls, message queues, event streams, shared stores — and the direction and protocols of those interactions, described behaviorally.

- **Concurrency and synchronization.** How concurrent work is coordinated: parallelism, locking, transactions, idempotency, ordering guarantees, back-pressure.

- **Lifecycle and control.** How runtime units start, stop, scale, recover, and fail over; scheduled or triggered work; health and readiness behavior.

- **Sequence and activity diagrams.** Text-authored diagrams of important runtime interactions.
