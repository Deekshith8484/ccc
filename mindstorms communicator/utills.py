import base64
import os
import tempfile
from gtts import gTTS

def text_to_speech_base64(text, lang="en"):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts = gTTS(text=text, lang=lang)
    tts.save(temp_file.name)

    with open(temp_file.name, "rb") as f:
        audio_base64 = base64.b64encode(f.read()).decode()

    os.remove(temp_file.name)
    return audio_base64
