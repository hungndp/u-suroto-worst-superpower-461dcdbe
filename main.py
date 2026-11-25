#!/usr/bin/env python3
"""Worst Superpower — one-line entry writer.

Writes the single worst-superpower line to /output/entry.txt.
"""

LINE = "I can see four seconds into the future, which is exactly long enough to watch myself trip."

# The gate requires 1 to 140 characters of UTF-8 text, a single line.
assert 1 <= len(LINE) <= 140, len(LINE)
assert "\n" not in LINE


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    # Write exactly the line, no trailing newline, so the file holds
    # precisely the 140-character-or-less text the judge compares.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
