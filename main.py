"""Write the one-sentence journey story for make.fun."""

import os
import sys
from pathlib import Path

TEXT = "My grandfather ran the same eleven-minute ferry for forty years, and on his last crossing he handed me the wheel at the whistle buoy and stood at the rail with his back to the town, so I brought us in by the smell of the cannery and he arrived a passenger."

assert 1 <= len(TEXT) <= 280

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
print(len(TEXT), file=sys.stderr)
