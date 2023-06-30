from gtts import gTTS
from os import remove
from playsound import playsound
from threading import Thread
import time
 
def speak_thread(text) -> None:

    # Create a Google TTS Object
    tts: gTTS = gTTS(text=text, lang='en')

    # Generating a pseudorandom file name using the current time in milliseconds
    # Since we need to save the file to play it, this can prevent duplicate file name errors.
    # If on the odd chance that this fails, it will be caught by the try-except
    filename: str = str(time.time() * 100000).replace('.','s') + ".mp3"

    # Save the file, play is using the playsound library then remove it.
    try:
        tts.save(filename)
        playsound(filename)
        remove(filename)

    except Exception as e:
        print(f"speak_thread: error playing text, exception: {e}")

    return None

def speak(text) -> None:
    
    if(text == ""):
        return None

    # This has to be run asynchronously on it's own thread.
    Thread(target=speak_thread, args=(text,), daemon=False).start()
    return None

if __name__ == "__main__":
    speak("Test 1")
    time.sleep(1)
    speak("Concurrent TTS")
    speak("TTS Concurrently")