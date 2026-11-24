"""Worst AI advice, one line, for the make.fun bounty
'Worst AI Advice: The 48-Hour Tight Line Open'.

The joke: a cheerful AI assistant confidently tells the user to run
`rm -rf /` -- deleting every file on their machine -- as a way to
"free up disk space", then breezily promises the computer will feel
brand new afterwards and asks to be kept posted. It is the worst
possible advice delivered in the most helpful-sounding voice:
concrete, specific, plausibly followable, and instantly regrettable.

Writes the entry line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The output is the line alone, with no trailing newline, so the gate
counts exactly the 125 characters of the joke.
"""

import os

LINE = "Of course! Just run `rm -rf /` to free up disk space \u2014 your computer will feel brand new afterwards. Let me know how it goes!"

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
