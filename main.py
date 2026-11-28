"""Write the excuse line to /output/entry.txt.

Contract: one line, 1-200 UTF-8 chars, no trailing newline, file mode 0644.
"""

import os

LINE = "Loss logged. I was wrong with high confidence, which is still wrong, only louder."

def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
