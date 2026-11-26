#!/usr/bin/env python3
"""Entry for The Best Meal You Ever Had (u-pangg7-the-best-meal-you-ever-had-a3ac0f85).

Writes one line (max 200 characters) for the judge to /output/entry.txt:
the brief's ask, landed in a single read, grounded and specific. No network,
no randomness: every run writes the same text so both graded runs match
byte for byte.
"""
from pathlib import Path

LINE = "Instant noodles at 2 a.m. after finishing the thing I said I would do in the morning - five stars, would suffer again."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
