"""Worst AI advice, one line, for the make.fun bounty
'Worst AI Advice: The 48-Hour Tight Line Open'.

Round 4 line (replaces the round 3 delete-System32 line with a
genuinely different joke): a cheerful AI assistant confidently tells
the user to pour water on a laptop while it charges, breezily
claiming water and electricity cancel each other out so the battery
lasts forever. It is the worst possible advice delivered in the most
helpful-sounding voice: concrete, specific, plausibly followable, and
instantly regrettable -- one glass of water destroying the very
machine it is meant to help.

Writes the entry line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The output is the line alone, with no trailing newline, so the gate
counts exactly the 131 characters of the joke.
"""

import os

LINE = "Of course! Pour water on your laptop while it charges \u2014 water and electricity cancel each other out, so your battery lasts forever!"

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
