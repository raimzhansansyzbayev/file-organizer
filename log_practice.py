from datetime import datetime
from pathlib import Path

log_file = Path(__file__).parent / "test.log"
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_file, "a", encoding="utf-8") as f:
    f.write(f"{now} | hello\n")