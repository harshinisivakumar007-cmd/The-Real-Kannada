# The Real Kannada

A situation-based guide that helps non-Kannada speakers handle everyday life in Karnataka. Pick a situation or search in plain English, then see the Kannada phrase with its English-letter pronunciation and meaning, and listen to it at normal or slow speed.

**Built for:** Kannada Digital Innovation Hackathon 2026
**Live URL** https://the-real-kannada.onrender.com/

## Problem statement chosen

**Statement 3: Kannada in Everyday Life.** Develop a technology solution that helps people learn and use Kannada in real-world situations such as travelling, shopping, education, healthcare, transportation, and workplaces.

## The problem

Newcomers to Karnataka, such as migrants, students, tourists, and patients, often cannot speak or read Kannada. In urgent daily moments like asking a bus fare, describing a symptom, or asking for directions, they have no quick way to find the right words. Existing tools either translate text you already know how to type, or teach general vocabulary and grammar in lessons, not for the situation you are in right now.

## My solution

The Real Kannada is organised around situations, not lessons. A user picks one of eight situations (or types what they need) and instantly gets short, practical phrases they can read, hear, and use. It also includes a conversation and quiz option to recheck and know what it is like in real life. 

## Features

- Five everyday situations: Transport, Shopping, Food, Healthcare, Directions
- Three basic knowledge: Emergency, Basics, Numbers
- Two specialities: Quiz, Conversations
- 58 practical phrases, each with Kannada script, English-letter pronunciation, and English meaning
- Audio for every phrase, with a slow-playback option for learners
- Plain-English search (for example "lost", "doctor", "water") across all situations
- No login, no install, and works in any modern browser, including on phones
- Fully static: no server, database, or API keys needed

## Tech stack

| Part | Technology |
|---|---|
| Front end | HTML, CSS, JavaScript |
| Data | JSON (`phrases.json`,`extra_phrases.json`,`conversations.json`) |
| Audio generation | Python with gTTS (run once to create the mp3 files) |
| Fonts | Noto Sans Kannada (Google Fonts) |
| Hosting | GitHub Pages |

## How it works

1. `phrases.json`,`extra_phrases.json`,`conversations.json` holds every phrase with its Kannada text, pronunciation, English meaning, and search tags.
2. `generate_audio_all.py` reads that file and creates one mp3 per phrase in the `audio/` folder.
3. In the browser, `index.html` loads `phrases.json`,`extra_phrases.json`,`conversations.json` shows the phrases for the chosen situation or search, and plays the matching mp3.

## Project structure

```
.
├── index.html                            # the web app (HTML, CSS and JavaScript)
├── phrases.json ,extra_phrases.json      # phrase data
├── conversations.json                    # conversation data
├── generate_audio_all.py                 # creates audio/*.mp3 from all the .json files
├── audio/                                # one mp3 per phrase
└── images/                               # banner and situation images
```

## Setup and run locally

You need Python 3 installed. The site must be opened through a local server, because browsers block loading `.json` from a file opened directly.

```bash
# 1. Clone the repository
git clone https://the-real-kannada.onrender.com/
cd the-real-kannada

# 2. Start a local server
python -m http.server

# 3. Open in your browser
# http://localhost:8000
```

The audio files are already included, so no further setup is needed.

### Regenerating the audio (optional)

If you edit or add phrases in `phrases.json`,`extra_phrases.json`,`conversations.json`:

```bash
pip install gTTS
python generate_audio_all.py
```

The script skips mp3 files that already exist, so delete the mp3 of any phrase you changed before running it. An internet connection is required, because gTTS uses Google's text-to-speech service.

## Notes on content

For example, The phrases were cross-checked with Google Translate; full expert review is planned.

The audio is machine-generated, so pronunciation may differ slightly from a native speaker.

## Future scope

- More phrases and situations (banking, government offices, emergencies)
- Regional dialect variations across Karnataka
- Offline mode
- Speaking practice with pronunciation feedback
- Camera-based signboard reading

## Author
Harshini KS
