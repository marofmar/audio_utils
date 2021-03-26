"""
dependency
pip install pydub
apt-get install ffmeg

"""


from os import path
from pydub import AudioSegment


def to_wav(src, dst):
    """
    :param src: source mp3 file path
    :param dst: destination wav file path
    :return:
    """

    sound = AudioSegment.from_mp3(src)  # read source file
    sound.export(dst, format='wav')  # export the read file into wav format

    return