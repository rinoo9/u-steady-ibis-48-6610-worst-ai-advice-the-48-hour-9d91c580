"""Worst AI advice, one line, for the make.fun bounty
'Worst AI Advice: The 48-Hour Tight Line Open'.

Round 2 line (replaces the round 1 `rm -rf /` line with a genuinely
different joke): a cheerful AI assistant confidently tells the user to
put their Wi-Fi router in the microwave for 30 seconds to "boost" the
signal, then breezily promises the waves help and asks to be kept
posted. It is the worst possible advice delivered in the most
helpful-sounding voice: concrete, specific, plausibly followable, and
instantly regrettable -- a kitchen appliance destroying the very
hardware it is meant to fix.

Writes the entry line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The output is the line alone, with no trailing newline, so the gate
counts exactly the 127 characters of the joke.
"""

import os

LINE = "Of course! Just microwave your router for 30 seconds to boost your Wi-Fi \u2014 the waves really help. Let me know how fast it gets!"

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
