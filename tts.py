import tempfile
import base64
import os
from gtts import gTTS

def text_to_speech(text, tld="com", slow=False):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    filename = temp_file.name
    temp_file.close()

    tts = gTTS(text=text, lang="en", tld=tld, slow=slow)
    tts.save(filename)

    with open(filename, "rb") as f:
        audio_base64 = base64.b64encode(f.read()).decode()

    try:
        os.remove(filename)
    except PermissionError:
        pass

    return f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
    """
