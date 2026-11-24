#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second -- entry program.

Writes one pitch sentence (at most 200 characters) to /output/entry.txt,
as the program/v1 harness requires. The pitch sells pothole naming rights:
bizarre at first glance, a real business on the second look.
"""

import os
import sys

PITCH = (
    "We sell pothole naming rights: local businesses pay to sponsor each "
    "repair and stencil their logo on the fresh asphalt, turning roadwork "
    "into cheap hyperlocal advertising."
)

MAX_CHARS = 200

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Enforce the sealed gate: UTF-8 text, 1-200 chars, not only whitespace,
    and a single sentence (one terminal full stop)."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("pitch is empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            f"pitch is {len(stripped)} chars, over the {MAX_CHARS} cap"
        )
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    return stripped


def main() -> int:
    try:
        text = validate(PITCH)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
