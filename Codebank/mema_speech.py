from gtts import gTTS
import os
import playsound
import threading

def speak_thread(text):
    tts = gTTS(text=text, lang='en')

    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def speak(text):
    threading.Thread(target=speak_thread, args=(text,), daemon=True).start()