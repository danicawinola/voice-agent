import sounddevice as sd
import numpy as np

DEVICE = 1
SAMPLE_RATE = 48000
DURATION = 5

print("🎤 Recording for 5 seconds...")
print("Speak into your headphone microphone!")

audio = sd.rec(
    int(SAMPLE_RATE * DURATION),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32",
    device=DEVICE
)

sd.wait()

rms = np.sqrt(np.mean(audio ** 2))
peak = np.max(np.abs(audio))

print("✅ Recording finished!")
print(f"📊 RMS volume: {rms:.8f}")
print(f"📈 Peak volume: {peak:.8f}")