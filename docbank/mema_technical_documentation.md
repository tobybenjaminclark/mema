# Accessibility Interface & Features

## Facial Recognition
**MeMa's Facial Recognition** uses the **[cv2](https://pypi.org/project/opencv-python/)** and **[face_recognition](https://pypi.org/project/face-recognition/)** library. The facial-recognition code was built upon  [this example](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py).

## Speech Recognition
**MeMa's Speech Recognition** uses the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library. The module at `codebank/mema_speech_recognition` provides a wrapper around the speech recognition library, which allows capturing audio from a microphone and converting it to text. The script makes use of the `speech_recognition` library (aliased as `sr`) for the speech recognition functionality. It also utilizes other Python modules for handling C data types, creating context managers, and managing threads, but this was **mainly done to mute [ASLA](https://www.alsa-project.org/wiki/Main_Page) Errors from spamming the terminal**, don't worry too much about that.


### Speech Recognition Functional Interface
Here is a description of the supplied functions within the Speech Recognition class. **These should not be used directly, instead through the `callback` function on the mema page instance.** This is just here in-case someone needs to modify the internal workings of the speech recognition process.

> :warning: **Please do not call any of these functions directly**

```python
recognize_speech_internal() -> str|None
```

>This function performs speech recognition using the Google Speech Recognition API. It listens on the microphone for speech and returns the recognized text as a `string`. If no speech is recognized or there is an error during the recognition process, it returns `None`.

<br>

```python
recognize_speech_thread(input_queue: Queue, stop: bool) -> None
```

>This function runs the `recognize_speech_internal()` function inside a context manager (`noalsaerr`) to suppress ALSA warnings. It continuously recognizes speech and adds the recognized phrases to the provided `input_queue`. It stops when the `stop` flag becomes `True`.

<br>

```python
listen(input_queue: Queue, stop: bool) -> None
```

>This function starts a thread to recognize speech. Recognized phrases are added to the parsed input queue using the speech_recognition library.

<br>

```python
noalsaerr() -> None
```

>This context manager switches the libasound.so error handler to the `py_error_handler` function (which is empty), essentially blocking ALSA warnings that get spammed in the terminal.

<br>

```python
py_error_handler(filename, line, function, err, fmt) -> None
```

>This empty error handler is used by the `noalsaerr()` context manager to block ALSA warnings.

<br>

```python
ERROR_HANDLER_FUNC
```

>This variable represents the C type for the error handler function used to handle ALSA errors.

<br>

```python
ERROR_HANDLER_FUNC(py_error_handler)
```

>This function sets the error handler for ALSA errors to the provided `py_error_handler` function.

<br>

```python
recognize_speech_internal() -> str|None
```

>Uses the Speech Recognition Library to listen on the microphone and convert speech to text. Returns a string or None if no speech is recognized.

<br>

```python
recognize_speech_thread(input_queue: Queue, stop:bool) -> None
```

>Runs the speech recognition function inside of a `noalserr` context manager, which blocks ALSA warnings. When the function returns a phrase, it is added to the `input_queue`.

<br>

```python
listen(input_queue: Queue, stop: bool) -> None
```
>Starts a thread to recognize speech. Recognized phrases are added to the parsed input queue, using the speech_recognition library.

## Text-To-Speech
**MeMa's Text to Speech** uses the [gTTS (Google Text To Speech)](https://pypi.org/project/gTTS/) Library