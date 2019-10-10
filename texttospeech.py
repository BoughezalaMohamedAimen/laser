import os
from gtts import gTTS

Text = "Bienvenue Aimen Mimou, Votre derniere Séance le 14 Nov 2012. il vous reste 11 Séances valables jusqu'au 15 novembre 2015"

print("please wait...processing")
TTS = gTTS(text=Text, lang='fr')

# Save to mp3 in current dir.
TTS.save("voice.mp3")

# Plays the mp3 using the default app on your system
# that is linked to mp3s.
os.system("start voice.mp3")
