#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (at most 140 characters) for an invented city
to /output/entry.txt. Deterministic, standard library only.
"""

import os

ENTRY = (
    "Wobbleford: light drizzle until 8am, then sunshine. "
    "Buses on time for once — bring an umbrella anyway, "
    "the sky changes its mind."
)


def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} characters, must be 1-140")
    if "Wobbleford" not in text:
        raise ValueError("entry must name the invented city")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
