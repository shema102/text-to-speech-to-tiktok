from gtts import gTTS


def create_audio_from_text(text: str, output_file: str):
    """
    Creates an audio file from text
    """
    tts = gTTS(text=text)
    tts.save(output_file)
