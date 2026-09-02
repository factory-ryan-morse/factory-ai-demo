#!/usr/bin/env python3
"""Generate every published copy of the page from one source.

v2/dark/index.html is the only file to edit. Everything else is derived, so the
dark and light builds cannot drift apart: they differ by exactly one attribute.

    python3 build.py

Outputs:
    v2/light/index.html   theme swapped
    index.html            theme swapped, asset paths flattened to the repo root
"""

import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
SOURCE = ROOT / "v2" / "dark" / "index.html"
DARK_TAG = '<html lang="en" data-brand-guide-theme="dark">'
LIGHT_TAG = '<html lang="en" data-brand-guide-theme="light">'
ASSETS = (
    "factory-lockup-white.svg",
    "factory-lockup-black.svg",
    "rotor-white.svg",
    "rotor-black.svg",
)


def to_light(html: str) -> str:
    count = html.count(DARK_TAG)
    if count != 1:
        sys.exit(f"expected exactly 1 html tag to swap, found {count}")
    return html.replace(DARK_TAG, LIGHT_TAG)


def flatten_assets(html: str) -> str:
    """Rewrite ../../asset.svg to ./asset.svg for the copy served at the root."""
    for asset in ASSETS:
        needle = f'"../../{asset}"'
        if needle not in html:
            sys.exit(f"asset reference not found in source: {needle}")
        html = html.replace(needle, f'"./{asset}"')
    if "../../" in html:
        sys.exit("a ../../ reference survived flattening")
    return html


def write(path: pathlib.Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)
    print(f"wrote {path.relative_to(ROOT)} ({len(html):,} bytes)")


def main() -> None:
    source = SOURCE.read_text()
    light = to_light(source)
    write(ROOT / "v2" / "light" / "index.html", light)
    write(ROOT / "index.html", flatten_assets(light))


if __name__ == "__main__":
    main()
