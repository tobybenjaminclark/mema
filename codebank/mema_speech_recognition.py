import speech_recognition as sr
from mema_constants import *
from threading import Thread
from typing import Callable
from queue import Queue

def recognize_speech_internal() -> str:

    # Initialize the speech recognition object
    recognizer: sr.Recognizer
    recognizer = sr.Recognizer()

    # Initialize the speech recognizer
    # A recognizer object is created using the sr.Recognizer() constructor
    with sr.Microphone() as source:
        # Use the microphone as the audio source

        # Adjust for ambient noise levels
        # The recognizer will listen for 1 second to calibrate the energy threshold
        # This helps in filtering out the ambient noise during speech recognition
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio from the microphone
        # The audio is recorded using the recognizer.listen(source) method
        audio = recognizer.listen(source)

    # Perform speech recognition using Google Speech Recognition API
    try:
        # Attempt to recognize the speech from the captured audio using Google Speech Recognition
        # The recognizer.recognize_google(audio) method is used
        # By default, it uses the default API key for speech recognition
        # To use a different API key, you can pass it as the 'key' parameter
        recognized_text = recognizer.recognize_google(audio)
        if(MEMA_SPEECH_RECOGNITION_DISPLAY_TEXT): print(f"recognize_speech_internal()")

        return recognized_text

    except sr.UnknownValueError as e:
        # Handle cases where speech could not be understood
        print(f"recognize_speech_internal() error: speech could not be understood, error: {e}")
        return "None"

    except sr.RequestError as e:
        # Handle cases where there is an error in requesting results from Google Speech Recognition service
        print(f"recognize_speech_internal() error: could not request results from gTTS, error: {e}")
        return "None"

def recognize_speech_thread(input_queue: Queue) -> None:
    # Perform speech recognition on a separate thread and pass the result to the input queue
    # This function takes a callback function as an argument

    # Call the internal speech recognition function to get the recognized text
    s = recognize_speech_internal()

    # Pass the recognized text to the callback function
    input_queue.put(s)

def listen(input_queue: Queue) -> None:
    # Start a new thread to perform speech recognition and call back to the queue

    # Start a new thread using the Thread class from the threading module
    # The target function is recognize_speech_thread, which performs speech recognition and invokes the callback
    # The callback function is passed as an argument to recognize_speech_thread
    # The daemon parameter is set to False, meaning the thread will not terminate when the main program ends
    Thread(target=recognize_speech_thread, args=(input_queue,), daemon=False).start()

    # Return from the Function
    return None

if __name__ == "__main__":
    listen(print)