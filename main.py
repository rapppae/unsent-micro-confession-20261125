"""Unsent: The Micro-Confession Sprint — make.fun entry.

Entry text: 143 characters (limit 260).
"""

import os

ENTRY = 'To: My old landlord\nI never told you the "mystery smell" was my flatmate\'s protein shaker, and I watched you repaint the whole kitchen over it.'


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
