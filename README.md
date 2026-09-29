# Automatic Speech Recognition (ASR) Tool

## Project Description

This project implements an Automatic Speech Recognition (ASR) tool using OpenAI Whisper.

The application takes an audio file as input, processes the speech using the Whisper model, converts the speech into text, displays the transcription, and saves the result as a text file.

## Features

- Speech-to-text conversion
- Supports WAV and other audio formats supported by FFmpeg
- Uses OpenAI Whisper
- CPU-compatible
- Displays transcription in the terminal
- Saves transcription to a `.txt` file
- Handles invalid or missing audio files

## Technologies Used

- Python 3.13
- OpenAI Whisper
- PyTorch
- FFmpeg
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
ASR-Tool/
├── audio/
│   ├── LJ001-0002.wav
│   └── LJ001-0002_transcription.txt
├── asr.py
├── requirements.txt
├── README.md
└── .gitignore