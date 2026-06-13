# `/reconcile-design`

Detects drift between the design documentation on `main` and the real production system, and scaffolds a change to correct it.

## What it does

- Establishes the sources of truth — code, configuration, infrastructure.

- Compares each [design view](../../../design/) against reality and records every discrepancy.

- Reports the drift and confirms which area to correct now.

- Scaffolds a `design/<slug>` branch, draft PR, and discussion thread, with the artifacts edited to describe the current production state.

- Flags any significant change that shipped without an RFC.

## How to invoke

```
/reconcile-design
```

Optionally, point it at what changed:

```
/reconcile-design The deployment moved to multi-region last month but the physical view still shows one region
```

## Examples

- `/reconcile-design`: The agent inspects the documentation against the code and infrastructure you point it to, reports the drift, and scaffolds a correction.

- `/reconcile-design <Description>`: Focus the check on a known area of drift.
