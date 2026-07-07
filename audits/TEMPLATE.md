# Audit title, eg. "Payment service"

- Auditors: Your Name [@your-github-handle], ...
- Date: YYYY-MM-DD
- Audit PR: #...
- Subject: owner/repo@<commit>, ...
- Scope: the subsystems, services, or areas examined

## Summary

_A short, single-paragraph verdict on the overall health of the architecture as-built, and the headline concerns. What is the shape of the problem?_

## Scope and method

_What was examined (repositories, services, directories) and how (eg. static reading, dependency graphing, build inspection). State what was deliberately out of scope, so the audit's coverage can be judged._

## Findings

_The core of the audit. Each finding names a structural problem in the as-is architecture, its location, and why it matters. Evaluation only — suggest, do not prescribe improvements. Order by priority._

| ID  | Finding | Type | Priority | Location |
| --- | ------- | ---- | -------- | -------- |
| F01 | Short title | Shallow abstraction | High | component / path |
| F02 | Short title | Tangled dependency | Medium | component / path |
| F03 | Short title | Single-caller wrapper | Low | component / path |

### F01 — Short title

- **Type:** Shallow abstraction | Tangled dependency | Single-caller wrapper | Duplication | Leaky boundary | ...
- **Priority:** High | Medium | Low
- **Location:** The component, module, or path where it lives.

_What the problem is — describe the structure that exists. Why it matters — the cost it imposes (changeability, coupling, comprehension, risk). Optionally, a suggested way forward — how it might be improved._

### F02 — Short title

- **Type:** ...
- **Priority:** ...
- **Location:** ...

_..._

## Themes

_Recurring patterns across the findings — the systemic issues that individual findings are symptoms of. Often more valuable than any single finding._

## Recommendations

_A prioritized shortlist of what to address first . This list may feed downstream refactoring and design work._
