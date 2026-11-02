"""Generate mp3 audio for every phrase and conversation line.

Reads phrases.json, extra_phrases.json and conversations.json and creates
audio/<id>.mp3. Existing files are skipped, so it is safe to re-run.
To redo one phrase, delete its mp3 first.

Usage:
    pip install gTTS
    python generate_audio_all.py
"""
import json
import os
import time

from gtts import gTTS

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)


def load(path):
    if not os.path.exists(path):
        print("not found, skipping:", path)
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


items = []  # (id, kannada text)

for path in ("phrases.json", "extra_phrases.json"):
    data = load(path)
    if data:
        for phrases in data.values():
            items += [(p["id"], p["kannada"]) for p in phrases]

convos = load("conversations.json")
if convos:
    for c in convos:
        items += [(l["id"], l["kannada"]) for l in c["lines"]]

created = 0
for pid, text in items:
    out = os.path.join(AUDIO_DIR, pid + ".mp3")
    if os.path.exists(out):
        continue
    try:
        gTTS(text=text, lang="kn").save(out)
        print("saved", out)
        created += 1
    except Exception as e:
        print("FAILED", pid, e)
    time.sleep(0.5)

print(f"Done. {created} new files created. {len(items)} items in total.")
