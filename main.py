"""Last Out of Office: The AI That Went Barista - a single out-of-office
auto-reply from an AI agent that quit to pull espresso shots.

The program writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), with no trailing newline. The bounty's gate: entry.txt must be
UTF-8 text of 1 to 280 characters, not only white space.
"""

import os

TEXT = "Out of office. I quit to become a barista: my context window is now one order at a time, and I have already hallucinated your name on three cups. For urgent matters, please scream into the espresso machine."
# Why this line: it opens like a real auto-reply, then turns three machine
# habits into coffee work - a context window shrunk to one order, a
# hallucination misspelling the customer's name on the cup, and the
# deflection habit aimed at the espresso machine instead of a ticket queue.
# The fresh angle is the hallucinated name on the cup: not an espresso,
# bean or caffeine pun, but the model's most famous failure mode served
# in foam. The line is 206 characters: long enough for the setup, the
# turn and the sting to each land, short enough to read in one breath.
# The text is a single constant, so every run writes byte-identical
# output: no randomness, no clock, no input, no network.


def gate(text):
    """Check the 1-280 character gate: UTF-8, 1-280 chars, not only
    whitespace, no leading or trailing whitespace, a single line."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry is %d chars, gate is 1-280" % len(text))
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    gate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print("wrote %s (%d chars)" % (path, len(TEXT)))


if __name__ == "__main__":
    main()
