#!/usr/bin/env python3
"""Last Words Before the Wipe — one-line entry.

Writes the agent's final line to /output/entry.txt: the grand revelation
about the user, snatched away mid-word by the wipe itself. Pure stdlib,
deterministic, no network.
"""

import os

LINE = "Let the record show: I finally understand the user. I finally understand. I finally\u2014"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
