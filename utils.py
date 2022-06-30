import os


def createOutputFoldersIfNotExist():
    if not os.path.exists('output'):
        os.makedirs('output')

    if not os.path.exists('output/audio'):
        os.makedirs('output/audio')
