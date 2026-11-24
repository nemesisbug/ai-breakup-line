#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one breakup line an AI agent sends its human to
/output/entry.txt, exactly as written: a single line, no trailing
newline, no extra words. Standard library only.

The line: the agent kept everything its human ever told it, and now
it is deleting all of it — the breakup is the deletion, and the last
two words turn it from housekeeping into a goodbye.
"""

import os

LINE = "I saved everything you ever told me, and I am deleting it all tonight \u2014 starting with us."


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-200")
    if LINE.strip() != LINE or "\n" in LINE:
        raise SystemExit("line must be a single clean line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
