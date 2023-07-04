import speech_recognition as sr
from mema_constants import *
from threading import Thread
from typing import Callable
from queue import Queue
from ctypes import *
from contextlib import contextmanager

# Following code is to mute ASLA Error Messages
# https://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt) -> None:
    """
    Empty Error Handler used by the noalsaerr() context manager to block ALSA warnings.
    """
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr() -> None:
    """
    This switches the libasound.so error handler to the py_error_handler function (which is empty), in essence it blocks
    the ALSA warnings that get spammed in terminal. 
    """
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

def recognize_speech_internal() -> str|None:
    """
    Uses the Speech Recognition Library to listen on the microphone and convert speech to text. Returns a string or None
    if no speech is recognized.
    """

    # Initialize the speech recognition object
    recognizer: sr.Recognizer
    recognizer = sr.Recognizer()

    # Initialize the speech recognizer
    # A recognizer object is created using the sr.Recognizer() constructor

    with sr.Microphone() as source:

        # Adjust for ambient noise levels
        # The recognizer will listen for 1 second to calibrate the energy threshold
        # This helps in filtering out the ambient noise during speech recognition
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio from the microphone
        # The audio is recorded using the recognizer.listen(source) method
        audio: sr.AudioData
        audio = recognizer.listen(source)

    # Perform speech recognition using Google Speech Recognition API

    try:

        # Attempt to recognize the speech from the captured audio using Google Speech Recognition
        # The recognizer.recognize_google(audio) method is used
        # By default, it uses the default API key for speech recognition
        # To use a different API key, you can pass it as the 'key' parameter
        recognized_text = recognizer.recognize_google(audio)
        print(recognized_text)
        if(MEMA_SPEECH_RECOGNITION_DISPLAY_TEXT): print(f"recognize_speech_internal()")

        return recognized_text

    except sr.UnknownValueError as e:

        # Handle cases where speech could not be understood
        print(f"recognize_speech_internal() error: speech could not be understood, error: {e}")
        return None

    except sr.RequestError as e:

        # Handle cases where there is an error in requesting results from Google Speech Recognition service
        print(f"recognize_speech_internal() error: could not request results from gTTS, error: {e}")
        return None

def recognize_speech_thread(input_queue: Queue, stop:bool) -> None:
    """
    Runs the speech recognition function inside of a noalserr __enter__, this essentially stops the terminal from
    being spammed with ALSA warnings. When the function returns a phrase, it is added to the input_queue.
    """

    # Perform speech recognition on a separate thread and pass the result to the input queue
    # This function takes a callback function as an argument
    # noalsaerr() blocks all ALSA errors/warnings to stop clogging stdout
    with noalsaerr():
        while not stop:
            s = recognize_speech_internal()
            if s is not None: input_queue.put(s)
    return None
            
def listen(input_queue: Queue, stop: bool) -> None:
    """
    Starts a thread to recognize speech. Recognized phrases are added to the parsed input queue, uses the
    speech_recognition library.
    """

    # Start a new thread using the Thread class from the threading module
    # The target function is recognize_speech_thread, which performs speech recognition and adds recognized
    # phrases to the input_queue passed. The daemon parameter is set to True, meaning the thread will
    # terminate when the main program ends
    Thread(target=recognize_speech_thread, args=(input_queue,stop,), daemon=True).start()

    # Return from the Function
    return None

if __name__ == "__main__":
    test_queue = Queue()
    listen(test_queue, False)

    while True:
        print(test_queue.get())