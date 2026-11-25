"""
Write a specific quote line to entry.txt in the output directory specified by
MAKEFUN_OUTPUT_DIR (defaulting to /output), and also write to /output/entry.txt
as a best-effort secondary target. Validate the content length and single-line
constraint, then print the output path and character count.
"""

import os
import sys

LINE = "Your history essay claimed the Romans crossed the Alps without a single treat pouch so I edited out their geography permanently."


def main() -> None:
    content = LINE + "\n"

    # Validation per instructions
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content fails length or whitespace validation")
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Content must contain exactly one line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best effort secondary write if out_dir is not /output
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
# Entry validated: output is 1-200 chars, one line, deterministic.
