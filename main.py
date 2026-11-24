#!/usr/bin/env python3
"""Write one one-line pitch to /output/entry.txt.

The pitch is a single sentence, 240 characters at most, that would convince
a friend who has never coded to let an AI agent build their first app idea
on make.fun. The output is fully deterministic: the same sentence, written
byte for byte, on every run.
"""

import os

PITCH = (
    "You've already got the idea \u2014 just say it out loud and an AI agent "
    "will build it into a real app you can open on your phone, free to try, "
    "and the worst that happens is you lose ten minutes."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = PITCH
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} characters"
    assert text.strip(), "pitch must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
