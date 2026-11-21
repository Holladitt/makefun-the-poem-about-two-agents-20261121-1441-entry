#!/usr/bin/env python3
"""Write one short poem about two agents agreeing to /output/entry.txt.

The poem's image: two hands on one wheel — agency passes in the overlap,
when both are holding at once. Stdlib only, deterministic, no network.
Honors MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

POEM = """You reached for the wheel and found my hand already there.
One turn — neither of us let go.
Two hands on the same spoke, one held breath.
The wheel never asked whose they were.
It only turned, and the road was ours.
"""


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
