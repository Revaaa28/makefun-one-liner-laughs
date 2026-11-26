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


def validate_entry(text: str) -> str:
    """Enforce the kit gate on the final entry text, before it is written.

    Kit gate (RULES.txt): /output/entry.txt must be UTF-8, 1-200 characters,
    not whitespace-only. A one-liner must also be exactly one line.
    """
    assert isinstance(text, str), "entry must be text"
    assert text.strip(), "entry must not be whitespace-only"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must not end with a newline"
    assert len(text) == 116, (
        "entry must be exactly 116 characters — the manually selected "
        "winner line (see candidates.md) must not drift"
    )
    assert all(ord(ch) >= 0x20 for ch in text), "entry must not contain control characters"
    return text


def main() -> None:
    text = validate_entry(JOKE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
