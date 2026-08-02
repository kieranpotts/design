# Review design

Checks the affected views describe real content, and takes the pull
request out of draft.

## How to invoke

Run from a `design/*` branch:

> Review design

> This design change is ready for review.

Or specify the target PR:

> Review #42

## Recommended models

A fast, cheap model is sufficient for this skill. The completeness check is
deliberately shallow, and the views themselves are left untouched.
