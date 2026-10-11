from pathlib import Path
import shutil

DRY_RUN = False
LOG_FILE = Path(__file__).parent / "moves.log"

lines = LOG_FILE.read_text(encoding="utf-8").splitlines()

for line in reversed(lines):
    if not line.strip():
        continue  # ignore empty lines

    # 1. split the line into its 3 parts
    timestamp, original, moved = line.split(" | ")

    # 2. turn the text into Path objects
    original = Path(original)
    moved = Path(moved)

    # 3. the moved file is gone: nothing to restore
    if not moved.exists():
        print(f"SKIP (missing): {moved}")
        continue

    # 4. something already sits at the original location: don't overwrite it
    if original.exists():
        print(f"SKIP (would overwrite): {original}")
        continue

    # 5. preview or restore
    if DRY_RUN:
        print(f"WOULD RESTORE: {moved.name} -> {original.parent}")
    else:
        shutil.move(str(moved), str(original))
        print(f"RESTORED: {moved.name} -> {original.parent}")