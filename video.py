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


def get_media_length(input_file: str):
    """
    Gets the length of the media
    :param input_file: input file
    :return: length in seconds
    """
    return float(ffmpeg.probe(input_file)['streams'][0]['duration'])


def crop_video(video_path: str, output_path: str, start: int, duration: int, aspect_ratio: float = 9/16):
    """
    Crops the video to a 9 by 16 aspect ratio
    :param video_path: path to the video
    :param output_path: path to the output video
    :param start: start time in seconds
    :param duration: duration in seconds
    :return:
    """

    width, height = get_video_width_height(video_path)

    new_height = int(width * aspect_ratio)
    new_width = int(height * aspect_ratio)

    start = seconds_to_duration(start)
    duration = seconds_to_duration(duration)

    ffmpeg.input(video_path, ss=start, t=duration).crop(
        width/2 - new_width/2, 0, new_width, new_height).output(output_path).run()


def cut_video(input_file: str, output_file: str, start: int, duration: int):
    """
    Cuts a video
    :param input_file: input file
    :param output_file: output file
    :param start: start time in seconds
    :param duration: duration in seconds
    :return:
    """
    start = seconds_to_duration(start)
    duration = seconds_to_duration(duration)

    ffmpeg.input(input_file, ss=start, t=duration).output(output_file).run()


def add_audio_to_video(input_file: str, output_file: str, audio_file: str):
    """
    Adds audio to a video
    :param input_file: input file
    :param output_file: output file
    :param audio_file: audio file
    :return:
    """
    video = ffmpeg.input(input_file)
    audio = ffmpeg.input(audio_file)

    ffmpeg.concat(video, audio, v=1, a=1).output(output_file).run()


def concat_videos(input_files: list, output_file: str):
    """
    Concatenates videos
    :param input_files: list of input files
    :param output_file: output file
    :return:
    """
    inputs = [ffmpeg.input(input) for input in input_files]
    ffmpeg.concat(*inputs, n=len(inputs)).output(output_file).run()


def concat_audios(input_files: list, output_file: str):
    """
    Concatenates videos
    :param input_files: list of input files
    :param output_file: output file
    :return:
    """
    inputs = [ffmpeg.input(input) for input in input_files]
    ffmpeg.concat(*inputs, v=0, a=1, n=len(inputs)).output(output_file).run()


def overlay_image_over_video(input_file: str, output_file: str, image_path: str, x: int, y: int):
    """
    Overlays an image over a video
    :param input_file: input file
    :param output_file: output file
    :param image_path: path to the image
    :param x: x position
    :param y: y position
    :return:
    """
    video = ffmpeg.input(input_file)
    image = ffmpeg.input(image_path)

    video.overlay(image, x=x, y=y).output(output_file).run()
