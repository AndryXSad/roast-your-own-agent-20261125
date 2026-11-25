#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (program/v1).

Writes exactly one line of plain text, at most 140 characters, roasting my
own agent, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: my agent called a tool to check whether it should call a tool,
then decided to check again — the confident, busy, going-nowhere tool call
the bounty brief names, in one tight sentence with a turn at the end.

Stdlib only. Deterministic: every run writes byte-identical output.
"""

import os
import sys

LINE = "My agent called a tool to check whether it should call a tool. It decided to check again."


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"entry line is {len(LINE)} chars, gate needs 1-140", file=sys.stderr)
        return 1
    if not LINE.strip() or "\n" in LINE or "\r" in LINE:
        print("entry line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
