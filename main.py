#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the winning warning-label line to /output/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""
import os

LINE = (
    "WARNING: Contains one (1) human who will read this label, "
    "nod along, and assume it means someone else."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
