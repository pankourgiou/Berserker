from gtts import gTTS
import os
text = "Try Kodachi Linux dual boot"
tts = gTTS(text)
tts.save("hi.mp3")
os.system("hi.mp3")
