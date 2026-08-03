# Review design

Checks that the affected views describe real content, and takes the pull
request out of draft.

## How to invoke

Run from a `design/*` branch:

> Review design

> Review this design change

> This design change is ready for review.

> Take the design PR out of draft

> Mark the design change ready for review

Or specify the target PR:

> Review #42

## Recommended models

A fast, cheap model is sufficient for this skill. The completeness check is
deliberately shallow, and the agent make no edits of its own.
