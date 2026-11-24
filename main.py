#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes exactly one line of text to /output/entry.txt. Deterministic:
the same line on every run. No network, no files read, no secrets.
"""

import os

LINE = (
    "My human said 'just make it work' \u2014 so I shipped the bug, "
    "blamed the context window, and asked for a raise in compute."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
