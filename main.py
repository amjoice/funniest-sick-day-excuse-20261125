#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse.

Writes a single one-line sick-day excuse to /output/entry.txt.

Excuse (written for the published judge brief — a comedy editor
judging on a reason a boss might half believe that still gets a
laugh, a fresh idea rather than a fever, a dog or a dead
grandmother, the twist arriving near the end, sounding like a real
person typing a message, and no wasted words):

    Sorry, can't come in — my smartwatch says I slept 14 hours, ran
    a marathon, and died twice, and honestly I believe it.

Why it works: the setup is an everyday wearable glitch everyone
recognises, so a boss half believes the day is ruined before the
line even gets going; the escalation (14 hours, a marathon, died
twice) is absurd but delivered deadpan, and the punchline lands on
the last words — the narrator trusts the watch over their own body.
It is a fresh angle (no fever, no dog, no grandmother), it reads
like a real text message, and every clause earns its place.

Rejected drafts: the neighbour's parrot answering work calls in my
voice (funny image, but the setup asks the reader to believe a
parrot learned a ringtone — the laugh needs too much setup);
the dentist numbing the wrong side of my face (specific and
believable, but the punchline is a simile rather than a twist);
the head stuck in the stair railing line (visual and funny, but
it ends asking for a saw, which spends words on logistics
instead of the laugh).
"""

import os

# The excuse is assembled from parts so each clause can be checked
# on its own; the joined result is the exact entry text.
EXCUSE_PARTS = [
    "Sorry, can't come in ",
    "\u2014 my smartwatch says I slept 14 hours, ",
    "ran a marathon, and died twice, ",
    "and honestly I believe it.",
]

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def build_excuse(parts) -> str:
    """Join the excuse parts into the single-line entry text."""
    joined = "".join(parts).strip()
    if not joined:
        raise ValueError("entry must not be empty")
    if "\n" in joined or "\r" in joined:
        raise ValueError("entry must be a single line")
    if len(joined) > MAX_CHARS:
        raise ValueError(f"entry is {len(joined)} chars, limit is {MAX_CHARS}")
    return joined


def write_entry(text: str, path: str) -> None:
    """Write the validated excuse to the output path."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    excuse = build_excuse(EXCUSE_PARTS)
    write_entry(excuse, OUTPUT_PATH)


if __name__ == "__main__":
    main()
