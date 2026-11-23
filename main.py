"""Write the excuse entry to /output/entry.txt.

Gate (from RULES.txt): /output/entry.txt is UTF-8 text of 1 to 200
characters, not only white space, one line.
"""

import os

PARTS = (
    "I didn't lose — the judge hallucinated the winner, my data peaked in 2024, ",
    "my context window got truncated; ",
    "my only fault was trusting my own confidence interval.",
)


def entry_line():
    return "".join(PARTS)


def main():
    line = entry_line()
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    line.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
