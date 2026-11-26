#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single original roast line to /output/entry.txt.
The line roasts the smart fridge's touchscreen ads: it now advertises
the very food already sitting inside it.
"""

ROAST = (
    "My smart fridge shows ads for the food already inside it "
    "\u2014 my leftovers now have a sponsor and a skip button."
)

MAX_CHARS = 160


def validate(line: str) -> None:
    """Check the entry gate: one line, 1-160 chars, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("roast must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be exactly one line")
    if not line.strip():
        raise ValueError("roast must not be only whitespace")
    if line != line.strip():
        raise ValueError("roast must not start or end with whitespace")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("roast must not contain control characters")
    if len(line) < 1 or len(line) > MAX_CHARS:
        raise ValueError(
            f"roast must be 1-{MAX_CHARS} chars, got {len(line)}"
        )
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(ROAST)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    # Round-trip check: what we wrote must read back byte-identical.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ROAST + "\n", "round-trip mismatch"
    print(f"wrote {len(ROAST)}-char roast to /output/entry.txt")


if __name__ == "__main__":
    main()
