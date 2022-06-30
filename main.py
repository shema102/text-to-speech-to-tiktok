from tts import createAudioFromText
from utils import createOutputFoldersIfNotExist


if __name__ == '__main__':
    createOutputFoldersIfNotExist()

    createAudioFromText(
        'I would support removing it but that is honestly the least of our concerns right now.', 'output/audio/test.mp3')
