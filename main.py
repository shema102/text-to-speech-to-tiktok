import json
import math
from tts import create_audio_from_text
from utils import cleanup, create_output_folders_if_not_exist

from video import add_audio_to_video, concat_audios, concat_videos, crop_video, cut_video, get_media_length, overlay_image_over_video

if __name__ == '__main__':
    create_output_folders_if_not_exist()

    # 1. convert text to speech
    # 2. add all audio durations plus delay after each
    # 3. cut video to the total length
    # 4. for each audio fragment cut video
    # 5. overlay comment to each video fragment
    # 6. overlay audio fragment on video
    # 7. glue all videos together

    fragments = []
    medias = []

    with open('input/input.json', encoding='utf-8') as f:
        data = json.load(f)
        fragments = data['fragments']

    video_fragments = []
    audio_fragments = []

    for i, fragment in enumerate(fragments):
        text = fragment['text']

        audio_file_name = f'output/audio/{i}.mp3'
        video_file_name = f'output/video/{i}.mp4'

        create_audio_from_text(text, audio_file_name)

        medias.append({
            "length": math.ceil(get_media_length(audio_file_name)),
            "screenshot": fragment['screenshot']})

        audio_fragments.append(audio_file_name)

    total_audio_length = math.ceil(
        sum(audio['length'] for audio in medias))

    crop_video('input/video/background.mp4',
               'output/video/cropped.mp4', 0, total_audio_length)

    offset = 0

    video_fragments = []

    for i, media in enumerate(medias):
        duration = media['length']

        cut_video_name = f'output/video/{i}_c.mp4'

        cut_video('output/video/cropped.mp4',
                  cut_video_name, offset, duration)

        offset += duration

        screenshot_file = f'input/screenshots/{media["screenshot"]}'

        video_overlay_file = f'output/video/{i}_o.mp4'

        overlay_image_over_video(
            cut_video_name, video_overlay_file, screenshot_file, 0, 0)

        video_fragments.append(video_overlay_file)

    concat_videos(video_fragments, 'output/video/output.mp4')
    concat_audios(audio_fragments, 'output/audio/output.mp3')

    add_audio_to_video('output/video/output.mp4',
                       'output/output.mp4', 'output/audio/output.mp3')

    cleanup()
