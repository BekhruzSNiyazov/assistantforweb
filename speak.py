from playsound import playsound
from gtts import gTTS
from os import remove

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
    remove(filename)