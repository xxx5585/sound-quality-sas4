# Sound Quality for SAS4

SAS4 on steam has a bad sound quality.
So this script lowers its audio files.
Then, its sound quality will be impleved.

"SAS: Zombie Assault 4": https://store.steampowered.com/app/678800/SAS_Zombie_Assault_4/

## Video
https://youtu.be/uHd3_BM0FI0

## How to lower audio file volume

1. Install python module
  `pip install pydub`
2. Place `lower_sound_volue.py` script to 
  `C:\Program Files (x86)\Steam\steamapps\common\SAS Zombie Assault 4\Assets`
3. Run the script
As a result:
* "Audio" folder is copied to "Audio-YYYYMMDDHHMMSS" wav files with the volume lowered by 10db are created in the "Audio" folder.

## How to countdown "hold the line 25"

1. Relace `player_holdTheLine.wav` file to 
  `C:\Program Files (x86)\Steam\steamapps\common\SAS Zombie Assault 4\Assets\Audio`
