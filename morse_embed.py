import numpy as np
import soundfile as sf
from scipy.signal import chirp, spectrogram

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def text_to_morse(text):
    return ' '.join(MORSE_CODE.get(c.upper(), '') for c in text)

def generate_morse_audio(morse, duration_per_dot=0.05, freq=19000, sample_rate=44100, volume=0.01):
    signal = []
    for char in morse:
        if char == '.':
            tone = np.sin(2 * np.pi * freq * np.linspace(0, duration_per_dot, int(sample_rate * duration_per_dot)))
            signal.extend(tone)
        elif char == '-':
            tone = np.sin(2 * np.pi * freq * np.linspace(0, 3 * duration_per_dot, int(sample_rate * 3 * duration_per_dot)))
            signal.extend(tone)
        elif char == ' ':
            signal.extend(np.zeros(int(sample_rate * duration_per_dot)))
        elif char == '/':
            signal.extend(np.zeros(int(sample_rate * duration_per_dot * 7)))
        signal.extend(np.zeros(int(sample_rate * duration_per_dot)))
    return np.array(signal) * volume

def embed_watermark(audio, watermark, offset_samples):
    if offset_samples + len(watermark) > len(audio):
        raise ValueError("Watermark too long to fit at given offset.")
    watermarked = np.copy(audio)
    watermarked[offset_samples:offset_samples+len(watermark)] += watermark
    return watermarked

def main():
    in_file = input("Input WAV file: ").strip()
    message = input("Message to embed (e.g. FLAG{secret}): ").strip()
    out_file = input("Output WAV file: ").strip()
    freq = float(input("Tone frequency (e.g. 19000 for high frequency, 15000 for safer range): ").strip())

    audio, sr = sf.read(in_file)
    if audio.ndim > 1:
        audio = audio[:, 0]

    morse = text_to_morse(message)
    print("Morse code:", morse)

    watermark = generate_morse_audio(morse, freq=freq, sample_rate=sr, volume=0.01)
    offset = sr * 2

    result = embed_watermark(audio, watermark, offset)
    sf.write(out_file, result, sr)
    print(f"Watermarked audio saved as: {out_file}")

if __name__ == "__main__":
    main()
