from piper import PiperVoice
import wave

print("🔄 Loading Piper...")

voice = PiperVoice.load("en_US-lessac-medium.onnx")

print("✅ Piper ready!")

text = "Hello! I am your local voice assistant."

with wave.open("test.wav", "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)

print("🔊 Voice generated! Check test.wav")