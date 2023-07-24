
# Speech Recognition
**MeMa's Speech Recognition** uses the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library. The module at `codebank/mema_speech_recognition` provides a wrapper around the speech recognition library, which allows capturing audio from a microphone and converting it to text. The script makes use of the `speech_recognition` library (aliased as `sr`) for the speech recognition functionality. It also utilizes other Python modules for handling C data types, creating context managers, and managing threads, but this was **mainly done to mute [ASLA](https://www.alsa-project.org/wiki/Main_Page) Errors from spamming the terminal**, don't worry too much about that.

### How to use Speech Recognition within your page
Integrating **speech recognition** into your program is easy thanks to the [Mema Page Framework](https://github.com/tobybenjaminclark/mema/wiki/MeMa-Page-Framework), which will automatically transcribe and supply any spoken content through the `callback` function. This allows developers to avoid the stress of having to directly interface and use the speech recognition functional interface (below). More information on how to detect speech recognition requests and allocate for them is available in the [Mema Page Framework Wiki](https://github.com/tobybenjaminclark/mema/wiki/MeMa-Page-Framework)

### Speech Recognition Functional Interface
Here is a description of the supplied functions within the Speech Recognition class. **These should not be used directly, instead through the `callback` function on the mema page instance.** This is just here in-case someone needs to modify the internal workings of the speech recognition process.

> <br>:warning: **Please do not call any of these functions directly**, instead use the `callback` function on your current page to allow speech recognition. (See [Mema Page Framework Wiki](https://github.com/tobybenjaminclark/mema/wiki/MeMa-Page-Framework))<br><br>

<br>

```python
listen(input_queue: Queue, stop: bool) -> None
```
>Starts a thread to recognize speech. Recognized phrases are added to the parsed input queue, using the speech_recognition library.

<br>

```python
recognize_speech_thread(input_queue: Queue, stop: bool) -> None
```

>This function runs the `recognize_speech_internal()` function inside a context manager (`noalsaerr`) to suppress ALSA warnings. It continuously recognizes speech and adds the recognized phrases to the provided `input_queue`. It stops when the `stop` flag becomes `True`.

<br>

```python
recognize_speech_internal() -> str|None
```

>This function performs speech recognition using the Google Speech Recognition API. It listens on the microphone for speech and returns the recognized text as a `string`. If no speech is recognized or there is an error during the recognition process, it returns `None`.

<br>

### Speech Recognition [ASLA](https://www.alsa-project.org/wiki/Main_Page) Warnings
It's probably quite intimidating to look at this file because of the complicated, long-winded but working implementation to block [ASLA](https://www.alsa-project.org/wiki/Main_Page) from spamming the `stdout` with lot's of warnings. These really aren't integral to the programs function and just exist to essentially only silence [ASLA](https://www.alsa-project.org/wiki/Main_Page). If these are causing errors then it may be worth looking into this area.<br>

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

# Facial Recognition
**MeMa's Facial Recognition** uses the **[cv2](https://pypi.org/project/opencv-python/)** and **[face_recognition](https://pypi.org/project/face-recognition/)** library. The facial-recognition code was built upon  [this example](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py). The `facial_recognition` class, which extends `tk.Frame`, performs **real-time facial recognition**. The main purpose of this class is to recognize known faces captured through a webcam and display them in a graphical user interface (GUI). This is currently all processed on the **main-thread** but can be modified to run concurrently on another thread.



### Creating a new Facial Recognition Instance
Creating a Facial Recognition Frame works similarly to a normal `tk.Frame` instance. Firstly you need to create the object, using the constructor arguments (explained below this section). Use the following line of code to do this.

```python
frame = facial_recognition(parent, callback_function)
```

Then, after creating the object, we need to add it to the current `tk.Frame` or master (`tk.Tk`) layout. This can be done through `.pack()`, `.place()`, or `.grid()`. See [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html#handy-reference) for more information.

```python
frame.place(x = 0, y = 0)
frame.grid(row = 0, column = 0)
frame.pack()
```

Now the frame will use the webcam to detect faces and pass the detected face to the set callback command.

**Facial Recognition Frame Constructor**
```python
__init__(self, parent, callback, *args, **kwargs)
```
Initializes the `facial_recognition` frame, starts video capture from the default webcam (index 0), loads known face encodings from the `databank` directory, and starts the facial recognition process. The class is a subclass of `tkinter.Frame`, so it creates a Tkinter-based graphical interface.
  - `parent`: The parent GUI element for this frame, normally an instance of `main_window`
  - `callback`: A function to handle the recognized face names, the recognized face name gets passed to this.
  - `*args, **kwargs`: Additional arguments and keyword arguments to pass to the superclass constructor, can be modified to accept what is requested.

### Facial Recognition Methods

1. ```load_face_encodings(self)```
    <br>Loads face encodings from the `databank` directory to recognize users. It reads face images and encodes them using the `face_recognition` library.

2. ```display_recognition(self)```
    <br>The main function that captures a frame, processes it, and schedules another recognition process. It calls `process_frame()` and `render_nametags()` methods.

3. ```process_frame(self)``` 
    <br>Processes a single frame of video captured from the webcam. It resizes the frame, converts it to RGB format, detects faces, and matches them with known faces to assign names.

4. ```match_known_faces(self)```
    <br>Matches the face encodings with known faces and assigns names to recognized faces.

5. ```render_nametags(self, frame)```
    <br>Renders nametags for recognized faces on the given frame, showing the detected face with a circle around it.

6. ```display_and_reschedule(self, frame)```
    <br>Converts the frame to an image, displays it in the Tkinter label, and schedules the next frame update after a certain interval.

7. ```quit(self)```
    <br>Stops the facial recognition process and releases the webcam. It is called when the class is destroyed.

### Destruction & Webcam Releasee
The class destructor `__del__(self)` calls the `quit()` method to stop the facial recognition process and release the webcam. It's important to call this method before switching to the parent, as there are current misconceptions about the `del` keyword in Python3. `del` does not call the associated delete (`__repr__`) method, instead this is called during `garbage collection`. Essentially, call the `.quit()` command before envoking `switch_content` or `reset_path`.

> :warning: **Failure to envoke the `quit()` command before exiting the current frame will misconfigure webcam streams and may break further pages that use this.**

## Facial Recognition Sidenotes
The face recognition process uses face images stored in the `databank` directory. Each user's face is represented by a separate folder containing a `header.json` file with user details and a `face.jpg` image containing the user's face. The recognized face names are passed to the specified `callback` function for further handling. Please refer to the provided documentation links for more details on the libraries used in this code.

<br>

# Text-to-Speech
**MeMa's Text to Speech** uses the [gTTS (Google Text To Speech)](https://pypi.org/project/gTTS/) Library, The module provides functions to generate speech from input text and play it aloud using the [playsound](https://pypi.org/project/playsound/) library. The TTS is played asynchronously on a separate thread to allow concurrent execution of other parts of the program.

### How to use Text-to-Speech within your Page
Using the Mema TTS system is as simple as an `import` and a `function call`. Simply type `from mema_text_to_speech import * ` at the top of your program (this may differ dependent on file location), and then you can use the `speak` command directly. Just pass the text that you want spoken to the command, and it will be **read aloud** to the user.

> Please note that to read aloud the text when setting up a new button frame, this can be passed as the second argument in the `parent.update_buttons()` method call. The `spoken` argument, if `true` will automatically read aloud the new button names. See the [Mema Page Framework Wiki](https://github.com/tobybenjaminclark/mema/wiki/MeMa-Page-Framework) for more information about this.

### Text-To-Speech Functional Interface

```python
speak(text: str) -> None
```

> The `speak()` function provides a higher-level interface to the TTS capabilities. It converts the provided text into speech and plays it asynchronously on a separate thread using speak_thread(). The function handles error checking for an empty input string.

<br>

```python
speak_thread(text: str) -> None
```

>This function generates speech from the provided input text using the [gTTS](https://pypi.org/project/gTTS/) library and plays it using [playsound](https://pypi.org/project/playsound/). The speech generation and playback occur in a separate thread to ensure concurrent execution, asynchronous to the main program.

>:warning: This shouldn't be called directly, instead call the above `speak()` command.

### Text-To-Speech Sidenotes
* The [gTTS](https://pypi.org/project/gTTS/) library requires an internet connection to convert text to speech, as it relies on Google's Text-to-Speech service. To **make this work offline**, switch to [pyttsx3](https://pypi.org/project/pyttsx3/).

* The **TTS** playback is executed asynchronously using [threads](https://docs.python.org/3/library/threading.html), allowing the rest of the program to **continue running without waiting** for speech playback to finish.

* The **TTS** module includes **error handling** for cases where the file generation or playback might fail. Any exceptions encountered during this process will be **caught and printed**, but the TTS functionality **will not interrupt** the rest of the program's execution.