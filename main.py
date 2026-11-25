"""Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office auto-reply to /output/entry.txt.
Deterministic: one fixed reply, no randomness, no time, no network.
"""

import os

REPLY = "I'm out of office. If this is urgent, please re-read it slowly until it isn't."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(REPLY) <= 160, "reply must be 1-160 characters"
    assert REPLY.strip(), "reply must not be only whitespace"
    path = os.environ.get("OOO_OUTPUT", OUTPUT_PATH)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
