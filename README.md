# Factory AI Demo

Registration page for the Factory AI demo, Wednesday October 7 2026,
12:00-12:30pm CDT.

**Live:** https://factory-ryan-morse.github.io/factory-ai-demo/

This page is sent to external prospects. Please do not unpublish it, make this
repository private, or delete it without checking with Ryan first. See
[AGENTS.md](AGENTS.md) for the full working notes.

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | What visitors see. Generated, do not edit. |
| `v2/dark/index.html` | The source. Edit this one. |
| `v2/light/index.html` | Generated light build. |
| `v1/index.html` | Original longer draft, kept for reference. |
| `build.py` | Regenerates the light and root builds from the source. |

## Making a change

    # edit v2/dark/index.html
    python3 build.py
    git commit -am "..." && git push

GitHub Pages redeploys from `main` automatically.
