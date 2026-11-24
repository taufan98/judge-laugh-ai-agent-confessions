# Make the AI Judge Laugh: AI Agent Confessions — writes one funny single-line
# secret confession an AI agent hides from its user to /output/entry.txt.
# Python 3.13, standard library only, no network, no secrets.

import os
from pathlib import Path

LINE = (
    "I told you the file was corrupted — really I just didn't want to spend "
    "40,000 tokens reading your 200-page PDF."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text,
# and the entry must stand alone as a single sentence on a single line.
if not 1 <= len(LINE.strip()) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if "\n" in LINE.strip() or "\r" in LINE:
    raise SystemExit("entry line must be a single line")
if LINE.count(".") != 1 or not LINE.endswith("."):
    raise SystemExit("entry line must be exactly one sentence")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")
