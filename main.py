#!/usr/bin/env python3
"""The Vacuum's Alibi — one-line excuse a robot vacuum gives for missing a spot.

Writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt),
then reads it back and verifies it matches exactly.
"""

import os
import sys

LINE = (
    # The alibi: deadpan sensor-speak up front, the punch ("court order")
    # at the very end. The vacuum never admits a miss — it cites policy.
    "I didn't miss that spot. My sensors classified the dust there as a "
    "protected species, and I don't evict tenants without a court order."
)


def validate_line(line: str) -> None:
    """The gate wants 1-200 characters of non-blank UTF-8 text."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200 limit")


def main() -> int:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != LINE + "\n":
        print("entry.txt mismatch", file=sys.stderr)
        return 1
    print(f"entry.txt OK: {len(LINE)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
