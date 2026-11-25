import os

line = "I set my status to 'in a meeting' so I can sit in a meeting about why we're always in meetings."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
