#!/usr/bin/env python3
"""news-image-20261122 entrypoint (Python 3.13, standard library only).

The entry image is entry.png beside this file: a one-page newspaper front
page drawn at build time by draw.py that sums up the world news of Sunday
22 November 2026 (COP31 collapse, the Houthi claim on the Rabigh refinery,
Iran's strikes in Bahrain, the 'El Chapo Isidro' capture, Ukraine, the market
sell-off, the South Korean minister's resignation over AI exam cheating, and
more). This program copies it
to /output/entry.png, byte for byte, so both grading runs write the same
bytes. A plain copy is deterministic by construction: no clock, no
randomness and no network are involved anywhere in this program.
Run locally with:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
print("wrote", OUT / "entry.png")
