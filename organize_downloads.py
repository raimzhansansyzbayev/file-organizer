from pathlib import Path
import shutil
from datetime import datetime

LOG_FILE = Path(__file__).parent / "moves.log"

def log(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{now} | {message}\n")

DRY_RUN = False # True = only print what would happen

folder = Path.home() / "Downloads"

Categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".arw"],
    "Documents": [".pdf", ".docx", ".txt", ".docx"],
    "Archives": [".zip", ".tar", ".7z", ".rar"],
    "Installers": [".exe", ".msi", ".torrent"],
    "Raw Photos": [".arw",],
    "Videos and Audio and more": [".mp4", ".mov", ".avi", ".mp3",],
    "Mods Marvel": [".pak", ".mod", ".suit", "", ".7z"],
}

#flip it around so each extension points to its category
lookup = {}
for category, extensions in Categories.items():
    for ext in extensions:
        lookup[ext] = category

for item in folder.iterdir():
    if not item.is_file():
        continue
    category = lookup.get(item.suffix.lower())
    if category is None:
        continue #unkown type: leave it alone

    target_dir = folder / category
    target = target_dir / item.name

    if target.exists():
        print(f"SKIP (already exists): {item.name}")
        continue 
    if DRY_RUN:
        print(f"Would move {item.name} -> {category}/")
    else:
        target_dir.mkdir(exist_ok=True)
        shutil.move(str(item), str(target))
        log(f"{item} | {target}")      # <-- new line
        print(f"MOVED: {item.name} -> {category}/")