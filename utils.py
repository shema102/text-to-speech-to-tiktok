import os
import shutil


def create_output_folders_if_not_exist():
    """
    Creates the output folders if they don't exist
    """
    if not os.path.exists('output'):
        os.makedirs('output')

    if not os.path.exists('output/audio'):
        os.makedirs('output/audio')

    if not os.path.exists('output/video'):
        os.makedirs('output/video')


def cleanup():
    """
    Cleans up the output folder
    """
    shutil.rmtree('output/audio', ignore_errors=True)
    shutil.rmtree('output/video', ignore_errors=True)


def seconds_to_duration(seconds: int):
    """
    Converts seconds to duration
    :param seconds: seconds
    :return: duration
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
