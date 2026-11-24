#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single fixed sick-day excuse line to /output/entry.txt.
Fully deterministic: the same hardcoded text every run.
"""

import os

EXCUSE = (
    "Can't come in today \u2014 I got locked out in my slippers taking the bins out "
    "and the neighbours have started a group chat about it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
