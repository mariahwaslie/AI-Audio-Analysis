# AI Audio Analysis

AI Audio Analysis is a Python project for turning lecture and video audio into usable study material. The main Streamlit app accepts a YouTube link, downloads the audio, transcribes it with OpenAI Whisper, and asks an OpenAI chat model to generate detailed notes and a study guide from the transcript.

The repository also includes early helper scripts for working with hosted course videos, M3U8 streams, and transcript-to-document summaries.

## Features

- Download audio from a YouTube video.
- Transcribe audio with OpenAI's Whisper API.
- Generate long-form notes and study-guide content from a transcript.
- Analyze a saved transcript for summaries, key points, action items, and sentiment.
- Convert an M3U8 media stream into an MP3 audio file with FFmpeg.
- Experiment with Selenium-based extraction from hosted lecture-video pages.

## Project Files

| File | Purpose |
| --- | --- |
| `chathelper.py` | Main Streamlit app for YouTube audio transcription and AI-generated notes. |
| `vidinfo.py` | Reads `lecture1.txt`, generates meeting-style transcript analysis, and exports a DOCX file. |
| `ap.py` | Extracts the first stream URL from an M3U8 file and converts it to MP3. |
| `ai.py` | Prototype Selenium workflow for logging into and inspecting an embedded hosted lecture video. |
| `lecture1.txt` | Example transcript used by `vidinfo.py`. |
| `requirements.txt` | Python dependencies needed to run the project. |

## Requirements

- Python 3.10 or newer recommended
- An OpenAI API key
- FFmpeg installed locally if you use audio/video conversion features
- Chrome and ChromeDriver if you use the Selenium prototype in `ai.py`

Python packages used by the project are listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/your-username/AI-Audio-Analysis.git
cd AI-Audio-Analysis
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
API=your_openai_api_key_here
```

The `.env` file is ignored by Git so your API key stays out of the repository.

## Running the Streamlit App

Start the main app:

```bash
streamlit run chathelper.py
```

Then open the local Streamlit URL in your browser, paste a YouTube link, and let the app:

1. Download the video's audio.
2. Play back the downloaded MP3.
3. Transcribe the audio with Whisper.
4. Generate detailed notes from the transcript.

Downloaded audio files are ignored by Git through `.gitignore`.

## Using the Transcript Analysis Script

`vidinfo.py` reads the sample transcript in `lecture1.txt`, sends it to the OpenAI API, and saves the generated analysis as `transcription.docx`.

```bash
python vidinfo.py
```

The generated DOCX file is ignored by Git.

## Using the M3U8 Audio Extraction Script

`ap.py` expects an `a.m3u8` file in the project root. It reads the stream URL from the file and writes an `a.mp3` output:

```bash
python ap.py
```

This workflow requires FFmpeg to be installed on your machine.

## Notes

- `chathelper.py` is the most complete user-facing script in the project.
- `ai.py` appears to be an exploratory script for a specific hosted-video login flow. It references credentials and variables that should be supplied securely before use.
- Some scripts are prototypes and may need small updates before production use, especially around error handling, dependency pinning, and model selection.

## Roadmap Ideas

- Add file upload support for local MP3 and MP4 files in the Streamlit app.
- Save generated transcripts and notes to Markdown or DOCX.
- Add better progress indicators and user-facing error messages.
- Replace hard-coded model names with configuration options.
