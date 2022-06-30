from utils import create_output_folders_if_not_exist
from video import crop_video_to_9_by_16


if __name__ == '__main__':
    create_output_folders_if_not_exist()

    # create_audio_from_text(
    #     'Is she cute by my standards or by Australopithecus standards? I find it hard to believe I would see one and find her attractive but what do I know', 'output/audio/test.mp3')

    print('------------- Cropping video to 9 by 16 aspect ratio')
    crop_video_to_9_by_16('input/video/minecraft.mp4',
                          'output/video/test.mp4', 60, 20)
    print('------------- Finished cropping video')
