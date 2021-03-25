from pydum import AudioSegment

def segment_audio(wav_filename, start_second, end_second, out_filename, out_format):
    """

    :param wav_filename: sound file in wave format (str)
    :param start_second: segmentation starting second (int)
    :param end_second: segmentation ending second (int)
    :param out_filename: segmented audio file name (str)
    :param out_format: segmented audio file format (str)
    :return: segmented audio file
    """
    f = AudioSegment.from_wav(wav_filename)
    start = start_second * 1000  # pydub works in milliseconds
    end = end_second * 1000
    assert start <= end, "Starting point should come before the end."
    segmented = wav_filename[start:end]
    print(f"Out of {f.duration_seconds} seconds of the whole sound, {segmented.duration_seconds} just extracted.")

    segmented.export(out_filename, format=out_format)
    return

