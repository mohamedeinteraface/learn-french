from gtts import gTTS
import os

os.makedirs("static/sounds", exist_ok=True)

# الحروف A-Z
for i in range(ord('A'), ord('Z')+1):
    char = chr(i)
    tts = gTTS(char, lang='fr')
    tts.save(f"static/sounds/{char.lower()}.mp3")

# الأرقام 1-99
for i in range(1, 100):
    tts = gTTS(str(i), lang='fr')
    tts.save(f"static/sounds/{i}.mp3")
