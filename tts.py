from gtts import gTTS


def createAudioFromText(text: str, outputFileName: str):
    tts = gTTS(text=text)
    tts.save(outputFileName)
