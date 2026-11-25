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


def validate_line(line: str) -> str | None:
    """Return an error message when the line breaks the 1-140 gate, else None."""
    if not 1 <= len(line) <= 140:
        return f"entry line is {len(line)} chars, gate needs 1-140"
    if not line.strip() or "\n" in line or "\r" in line:
        return "entry line must be a single non-blank line"
    return None


def resolve_output_path() -> str:
    """Resolve $MAKEFUN_OUTPUT_DIR/entry.txt, creating the dir if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(path: str, line: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main() -> int:
    error = validate_line(LINE)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    write_entry(resolve_output_path(), LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
