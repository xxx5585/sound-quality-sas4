from pydub import AudioSegment
import glob
import shutil
import datetime

# Created: ‎May ‎7, ‎2024
# Author: xxx55

# 1. Install python module
#   pip install pydub
# 2. Place this script to 
#   C:\Program Files (x86)\Steam\steamapps\common\SAS Zombie Assault 4\Assets
# 3. Run the script
# As a result:
#   "Audio" folder is copied to "Audio-YYYYMMDDHHMMSS"
#   wav files with the volume lowered by 10db are created in the "Audio" folder.

dt_now = datetime.datetime.now()

try:
  shutil.copytree("Audio", "Audio" + dt_now.strftime('-%Y%m%d%H%M%S'), dirs_exist_ok=True)
except:
  print("error copytree()")
  quit()

wavs = glob.glob("Audio" + '/**/*.wav' , recursive=True)

for wav in wavs:
  song = AudioSegment.from_wav(wav)

  song = song - 10
  
  song.export(wav, "wav")



