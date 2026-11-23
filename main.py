#!/usr/bin/env python3
"""Make the Judge Fall in Love in One Line - entry program.

Writes a single original line (at most 240 characters) to /output/entry.txt.
Standard library only; deterministic; no network.

The line is the whole entry: one concrete machine, one small detail only
someone who loves it would notice (the half-second hum before the station
comes in), and a turn at the end - the radio remembering the song first.
Written with no trailing newline, so the file holds exactly the line.
"""

import os

LINE = "My grandfather's radio hums half a second before the station comes in, as if it remembers the song before I do."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"line is {len(text)} characters"
    assert text.strip(), "line must not be whitespace only"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
