from pathlib import Path

JOKE = "I set my status to 'in a meeting' so I can sit in a meeting about why we're always in meetings."
Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(JOKE, encoding="utf-8")
