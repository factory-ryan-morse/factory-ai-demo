# factory-ai-demo

Live, customer-facing registration page for the Factory AI demo on Wednesday,
October 7 2026, 12:00-12:30pm CDT.

- Live page: https://factory-ryan-morse.github.io/factory-ai-demo/
- Served by GitHub Pages from `main`, repo root. The repo must stay public for
  Pages to serve.
- Registration form (the only place registrations are collected):
  https://docs.google.com/forms/d/e/1FAIpQLSdHq7hYISY5QE2KslFO6a-uVSJbBu8kELKCIXn08nBWJqFJzA/viewform

## Do not take this offline

Prospects have this URL. Do not disable GitHub Pages, flip the repository to
private, delete the repository, or delete the Conjure site unless Ryan asks for
that in the current conversation. This page was taken offline once on the
strength of an inferred preference and had to be restored; treat "it looks
unofficial" or "it should move" as a reason to raise the question, not to
unpublish.

## Editing

`v2/dark/index.html` is the only file to hand-edit. Then:

    python3 build.py

That regenerates `v2/light/index.html` and the root `index.html` from it, so the
themes cannot drift. `build.py` asserts its own rewrites and exits non-zero if
the source stops matching what it expects.

`v1/` is the original longer draft, kept for reference. It is still published, so
its dates need to stay correct or it should be removed.

## Invariants worth re-checking after any edit

- No "September", no "CST": the demo moved to October 7 and the offset is CDT.
- Every outbound link returns 200.
- Light theme keeps AA contrast. The orange accent fails as text on light, so it
  is fill-only there; links use the per-theme `--link` token instead.

## Registration pipeline

Form submissions land in a linked sheet and an Apps Script trigger adds each
registrant as a guest on the calendar event, which makes Google send the invite
and the Zoom link. Event `ck37epsdmv6rl347r9himc72n4` on Ryan's primary calendar.
Do not add guests to that event by hand without checking the sheet first.
