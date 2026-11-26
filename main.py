#!/usr/bin/env python3
"""One-Liner Laughs — make.fun entry (program/v1).

Writes a single original one-line joke (116 characters, UTF-8) to
/output/entry.txt. Fully deterministic: no input, no network, no randomness,
no environment reads — the same bytes on every run.

The line was chosen by manual ranking of 12 original candidates against the
kit judge brief (see candidates.md in the build workdir): clear setup +
payoff, laugh-out-loud twist, surprise, freshness, economy of wording.
"""

import os

JOKE = (
    'I asked the cloud where my files went. It said "somewhere safe", '
    "the exact words my dad used about my childhood dog."
)


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be whitespace-only"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
