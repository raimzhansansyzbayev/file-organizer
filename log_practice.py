from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("test.log", "a", encoding="utf-8") as f:
    f.write(f"{now} | hello\n")