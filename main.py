"""Worst AI advice, one line, for the make.fun bounty
'Worst AI Advice: The 48-Hour Tight Line Open'.

Round 3 line (replaces the round 2 microwave-router line with a
genuinely different joke): a cheerful AI assistant confidently tells
the user to delete System32 to "free up space", breezily claiming
Windows only keeps it around out of pure sentiment. It is the worst
possible advice delivered in the most helpful-sounding voice:
concrete, specific, plausibly followable, and instantly regrettable --
one click destroying the very operating system it is meant to fix.

Writes the entry line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The output is the line alone, with no trailing newline, so the gate
counts exactly the 97 characters of the joke.
"""

import os

LINE = "Of course! Delete System32 to free up space \u2014 Windows only keeps it around out of pure sentiment!"

# The gate allows 1 to 140 characters, a single line.
MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS
    assert "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
