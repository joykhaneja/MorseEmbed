# MorseEmbed
MorseEmbed is a Python CLI utility that embeds secret messages into .wav audio files using Morse code tones. The watermark is subtle—inaudible or barely noticeable—and can be later revealed through spectrogram analysis, making it perfect for ownership marking, steganography, or CTF-style flag hiding.

## Features
- Interactive CLI — no flags needed
- Morse code conversion and tone generation
- Embed messages as high-frequency watermark
- Frequency customization (e.g., ultrasonic 19000 Hz)
- Works with mono or stereo WAV files

## Requirements
```bash
numpy
soundfile
scipy
```

## Installation
```bash
git clone https://github.com/joykhaneja/MorseEmbed.git
cd MorseEmbed
pip install -r requirements.txt
```

## Usage
```bash
python3 morse_embed.py
```
It will prompt you for:
- Input WAV file (existing audio)
- Message to embed (e.g. Hello World)
- Output WAV file (name of watermarked file)
- Tone frequency (e.g. 19000 Hz for ultrasonic)

## How It Works
- Message is converted into International Morse Code.
- Each symbol (`.` or `-`) is turned into a sine wave tone.
- These tones are added to the input audio as a faint background signal.
### Example:
- Input message: `FLAG{TEST}`
- Morse: `..-. .-.. .- --. / - . ... -`
- Tones added at 19000 Hz, starting 2 seconds into the audio.
