#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one one-line comedy joke to entry.txt."""
import os

LINE = 'I asked HR for a raise and they gave me a meditation app — corporate for "please cry quieter about it."'


def main() -> None:
    assert 1 <= len(LINE) <= 280, f"line must be 1-280 chars, got {len(LINE)}"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
