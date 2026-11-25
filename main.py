#!/usr/bin/env python3
"""Two Robots in an Elevator entry for make.fun competition
u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.

Writes one original line of awkward robot small talk (under 200
characters) to /output/entry.txt. Deterministic: no wall clock, no
randomness, no network, no input files. Python 3.13, standard
library only.
"""

import os

MAX_LEN = 200

LINE = "I calculated 14,000 ways to start this conversation. I chose silence. You are still here, so I am recalculating."

# The joke is the robot treating silence as a computed choice, then
# failing to stick to it the moment the other robot does not leave.


def main() -> None:
    text = LINE.strip()
    if "\n" in text:
        raise ValueError("elevator line must be a single line")
    if not (1 <= len(text) <= MAX_LEN):
        raise ValueError(f"elevator line must be 1-{MAX_LEN} characters, got {len(text)}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
