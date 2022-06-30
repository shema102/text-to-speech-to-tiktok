import ffmpeg
from utils import seconds_to_duration


def get_video_width_height(input_file: str):
    """
    Gets the width and height of the video
    :param input_file: input file
    :return: width, height
    """
    probe = ffmpeg.probe(input_file)
    video_stream = next(
        (stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])

    return width, height


def crop_video_to_9_by_16(video_path: str, output_path: str, start: int, duration: int):
    """
    Crops the video to a 9 by 16 aspect ratio
    :param video_path: path to the video
    :param output_path: path to the output video
    :param start: start time in seconds
    :param duration: duration in seconds
    :return:
    """

    width, height = get_video_width_height(video_path)

    new_height = int(width * 9/16)
    new_width = int(height * 9/16)

    start = seconds_to_duration(start)
    duration = seconds_to_duration(duration)

    ffmpeg.input(video_path, ss=start, t=duration).crop(
        width/2 - new_width/2, 0, new_width, new_height).output(output_path).run()


def remove_audio(input_file: str, output_file: str):
    """
    Removes the audio from the video
    :param input_file: input file
    :param output_file: output file
    :return:
    """
    ffmpeg.input(input_file).output(
        output_file, a='-').run()
