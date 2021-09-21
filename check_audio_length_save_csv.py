import os
import pandas as pd
import librosa

os.path.exists("소리 디렉토리 path")  # supposed to be TRUE

df = pd.read_csv("wav_and_txt_0916.csv", index_col=0)

WAV = "소리 디렉토리 path"

dur = []
for i in df["wav"]:
    l = librosa.get_duration(filename = os.path.join(WAV, i))
    dur.append(l)
    
df["length_s"] = dur

df[df.length_s < 30]  # 30초 안되는 친구들만 모아보기
