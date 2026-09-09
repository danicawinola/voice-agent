#  Local Voice Assistant

A locally running voice assistant built with Python that converts speech into text, processes it using a local Large Language Model (LLM), and converts the response back into speech.

The project was built to understand and experiment with the core components behind modern voice AI systems without relying on paid cloud AI APIs.

---

##  Architecture

```text
 Microphone
     ↓
Speech-to-Text
(Faster-Whisper)
     ↓
Text
     ↓
Local LLM
(Ollama + Llama 3.2 3B)
     ↓
AI Response
     ↓
Text-to-Speech
(Piper)
     ↓
 Speaker / Headphones

| Technology     | Purpose                               |
| -------------- | ------------------------------------- |
| Python         | Main programming language             |
| Faster-Whisper | Speech-to-text                        |
| Ollama         | Local LLM runtime                     |
| Llama 3.2 3B   | Language model                        |
| Piper TTS      | Text-to-speech                        |
| SoundDevice    | Microphone recording & audio playback |
| NumPy          | Audio data processing                 |
| Requests       | Communication with Ollama             |


 Current Features
 Records speech through a microphone
 Converts speech to text using Faster-Whisper
 Generates responses using a locally running LLM
 Converts AI responses into speech using Piper
 Runs locally without requiring cloud AI APIs
 Supports microphone/headphone audio input

voice-agent/
│
├── voice_brain.py       # Main voice assistant
├── whisper_test.py      # Tests speech-to-text
├── piper_test.py        # Tests text-to-speech
├── test_ollama.py       # Tests communication with Ollama
├── mic_test.py          # Tests microphone input
├── .gitignore           # Files excluded from Git
└── README.md            # Project documentation
