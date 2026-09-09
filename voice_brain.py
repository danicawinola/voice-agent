import sounddevice as sd
import numpy as np
import requests
import wave
from faster_whisper import WhisperModel
from piper import PiperVoice

# -----------------------------
# SETTINGS
# -----------------------------

MIC_DEVICE = 1
SAMPLE_RATE = 16000
DURATION = 5

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:3b"

VOICE_MODEL = "en_US-lessac-medium.onnx"


# -----------------------------
# LOAD MODELS
# -----------------------------

print("🔄 Loading Whisper...")

whisper = WhisperModel(
    "tiny.en",
    device="cpu",
    compute_type="int8"
)

print("✅ Whisper ready!")

print("🔄 Loading Piper...")

voice = PiperVoice.load(VOICE_MODEL)

print("✅ Piper ready!")


# -----------------------------
# RECORD VOICE
# -----------------------------

def record_voice():

    print("\n🎤 Speak for 5 seconds...")

    audio = sd.rec(
        int(SAMPLE_RATE * DURATION),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=MIC_DEVICE
    )

    sd.wait()

    return audio.flatten()


# -----------------------------
# SPEECH → TEXT
# -----------------------------

def transcribe(audio):

    print("🧠 Understanding...")

    segments, info = whisper.transcribe(
        audio,
        beam_size=1
    )

    text = " ".join(
        segment.text for segment in segments
    ).strip()

    return text


# -----------------------------
# TEXT → AI RESPONSE
# -----------------------------

def ask_ai(text):

    print("🤖 Thinking...")

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": (
                "You are a friendly voice assistant. "
                "Answer naturally and keep your response short.\n\n"
                f"User: {text}"
            ),
            "stream": False
        }
    )

    return response.json()["response"].strip()


# -----------------------------
# TEXT → SPEECH
# -----------------------------

def speak(text):

    print("🔊 Speaking...")

    with wave.open("response.wav", "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    # Play the generated audio
    import soundfile as sf

    audio, sample_rate = sf.read("response.wav")

    sd.play(audio, sample_rate)
    sd.wait()


# -----------------------------
# MAIN
# -----------------------------

audio = record_voice()

user_text = transcribe(audio)

print(f"\n👤 You: {user_text}")

if user_text:

    reply = ask_ai(user_text)

    print(f"\n🤖 Agent: {reply}")

    speak(reply)

else:

    print("🔇 I couldn't understand you.")