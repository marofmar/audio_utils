import os, shutil

folderPath = "WAV path"
destination = "WAV dest"

filesToFind = df.wav[:300].values  # values 통해서 파일명만 콕 집어서 데려온다

for filename in os.listdir(folderPath):
  if filename in filesToFind: 
    target = os.path.join(folderPath, filename)
    shutil.copy(target, destination)
    
  else:
    print("hoy!")
