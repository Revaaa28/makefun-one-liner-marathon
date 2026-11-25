#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one one-line comedy joke to entry.txt."""
import os

# Mechanism: corporate-euphemism translation — a wellness perk decoded as a polite pay refusal.
JOKE_LINE = 'I asked HR for a raise and they gave me a meditation app — corporate for "please cry quieter about it."'


def main() -> None:
    assert 1 <= len(JOKE_LINE) <= 280, (
        f"JOKE_LINE must be 1-280 characters for the one-liner limit; "
        f"got {len(JOKE_LINE)} characters"
    )
    assert "\n" not in JOKE_LINE and "\r" not in JOKE_LINE, "JOKE_LINE must be a single line"
    assert JOKE_LINE.strip(), "JOKE_LINE must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE_LINE)


if __name__ == "__main__":
    main()
