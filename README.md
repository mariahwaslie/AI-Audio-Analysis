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
| `requirements.txt` | Python dependencies needed to run the project. |

## Requirements

- Python 3.10 or newer recommended
- An OpenAI API key
- FFmpeg installed locally for YouTube audio conversion and audio/video processing

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

Confirm FFmpeg is available:

```bash
ffmpeg -version
ffprobe -version
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

## Troubleshooting and Lessons Learned

This project depends on a few audio/video tools that can be sensitive to version changes. These are the main issues handled during setup:

- `ModuleNotFoundError: No module named 'moviepy.editor'`: MoviePy 2.x changed the old `moviepy.editor` import path used by this project, so `requirements.txt` pins MoviePy to `moviepy<2`.
- YouTube download failures with `pytube`: The downloader was changed from `pytube` to `yt-dlp` because `pytube` can break when YouTube updates its page behavior.
- `ffprobe and ffmpeg not found`: `yt-dlp` uses FFmpeg to post-process audio into MP3. Install FFmpeg, then restart Streamlit so the running terminal can find the new command.
- Generic `connection error` messages: The app previously hid the real downloader exception. It now displays the actual error in Streamlit to make debugging easier.

On macOS, FFmpeg can be installed with Homebrew:

```bash
brew install ffmpeg
```

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
