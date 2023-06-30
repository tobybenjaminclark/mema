import speech_recognition as sr
from threading import Thread

def recognize_speech_internal() -> str:
    recognizer: sr.Recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio = recognizer.listen(source)

    # recognize speech using Google Speech Recognition
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    try:
        return recognizer.recognize_google(audio)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "ERROR"

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "ERROR"

def recognize_speech_thread(callback) -> None:
    s = recognize_speech_internal()
    callback(s)

def listen(callback):
    # This has to be run asynchronously on it's own thread.
    print("Test")
    Thread(target=recognize_speech_thread, args=(callback,), daemon=False).start()
    return None   

if __name__ == "__main__":
    listen(print)