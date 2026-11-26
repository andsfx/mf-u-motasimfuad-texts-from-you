#!/usr/bin/env python3
"""Entry program for make.fun's "Texts From Your Future Self" bounty.

The entry is one text message the writer's future self sends back. This
program writes that message to /output/entry.txt as UTF-8 text and nothing
else: no arguments, no network, no randomness, so two runs write the same
bytes.
"""

from __future__ import annotations

import os
from pathlib import Path

MAX_CHARS = 200

ENTRY_LINE = (
    "It's you from 2056. The soup is fine. The email is not. "
    "I'm not saying which email."
)


def entry_path() -> Path:
    """The gate reads /output/entry.txt; dry runs may point elsewhere."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override) / "entry.txt"
    return Path("/output/entry.txt")


def main() -> int:
    text = ENTRY_LINE
    if not text.strip():
        raise SystemExit("entry is blank; the gate needs 1..%d characters" % MAX_CHARS)
    if len(text) > MAX_CHARS:
        raise SystemExit("entry is %d characters; the cap is %d" % (len(text), MAX_CHARS))
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
