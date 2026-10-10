from pathlib import Path
from collections import Counter 

folder = Path.home() / "Downloads"
counts = Counter()

for item in folder.iterdir():
    if item.is_file():
        counts[item.suffix.lower()] += 1

for ext, n in counts.most_common():
    print (ext or "(no extension)", n)

print("Total files:", sum(counts.values()))
    
