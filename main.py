#!/usr/bin/env python3
"""Make the Judge Smile — writes one line about a small good thing today.

Deterministic, stdlib-only, no network. Writes exactly one line to
entry.txt inside the directory named by MAKEFUN_OUTPUT_DIR (or "." if
unset).
"""

import os


def main():
    line = (
        "Today the warung owner gave me the last krupuk from the jar, "
        "free, and winked like we'd just pulled off a tiny heist together."
    )
    # Guard the entry contract: one line, 1-200 chars, not whitespace-only.
    assert 1 <= len(line) <= 200 and line.strip(), "entry line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
