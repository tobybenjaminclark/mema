from gtts import gTTS
from os import remove
from playsound import playsound
from threading import Thread
from mema_constants import *
import time
 
def speak_thread(text: str) -> None:
    """
    Generates speech from the given text using Google Text-to-Speech (gTTS) and plays it using the playsound library.
    The gTTS library requires an internet connection to convert text to speech, an appropriate audioplayer is required
    to play sound aloud using the playsound library. This shouldn't be called directly, instead use the speak() command.

    Args:
        text (str): The input text to be converted into speech.

    Example:
        >>> speak_thread("Hello, how are you?")
        Speech generated from the text "Hello, how are you?" is played.

    """

    # Create a Google TTS Object
    tts: gTTS = gTTS(text=text, lang='en', slow = MEMA_SLOW_TTS)

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

def speak(text: str) -> None:
    """
    Converts the passed text to speech and plays it asynchronously on a thread using the speak_thread() function.
    Handles error checking for an empty string. Uses the gTTS library, requires an Internet Connection (currently)
    """

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