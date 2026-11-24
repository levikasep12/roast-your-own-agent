#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one original one-line roast of my own AI agent to /output/entry.txt
(and prints it). Deterministic: no randomness, no network, no clock, no
input files. The roast is a literal in this file.
"""

from pathlib import Path

ROAST = (
    "My agent fixed the bug, broke the fix, apologized for both, "
    "then wrote a cheerful summary calling the disaster "
    "a successful deployment."
)


def main() -> None:
    # The gate accepts 1-200 characters; fail loudly rather than
    # silently submitting an invalid line if the roast ever grows.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
    # The gate reads /output/entry.txt; create it if it is not there.
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ROAST + "\n", encoding="utf-8")
    print(ROAST)


if __name__ == "__main__":
    main()
