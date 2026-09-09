import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

# Microphone
DEVICE = 1
SAMPLE_RATE = 16000
DURATION = 5

print("🔄 Loading Whisper...")
model = WhisperModel(
    "tiny.en",
    device="cpu",
    compute_type="int8"
)

print("✅ Whisper ready!")
print("🎤 Speak for 5 seconds...")

audio = sd.rec(
    int(SAMPLE_RATE * DURATION),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32",
    device=DEVICE
)

sd.wait()

audio = audio.flatten()

print("🧠 Transcribing...")

segments, info = model.transcribe(
    audio,
    beam_size=1
)

text = " ".join(segment.text for segment in segments).strip()

print()
print("📝 You said:")
print(text)