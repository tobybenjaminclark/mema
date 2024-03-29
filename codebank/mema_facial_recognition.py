# Generic MeMa Import
from codebank.mema_constants import *

# Facial recognition library
# face_recognition is a library for face recognition tasks.
# It provides functionality for face detection, face encoding, and face comparison.
# Documentation: https://github.com/ageitgey/face_recognition
import face_recognition

# OpenCV library
# cv2 is the OpenCV library for computer vision tasks.
# It provides functionality for video capture, image processing, and video display.
# OpenCV is used in this code for webcam video capture and frame processing.
# Documentation: https://docs.opencv.org/
import cv2

# Python Imaging Library
# PIL (Python Imaging Library) is a library for image processing.
# It provides functionality for working with images, including opening, manipulating, and saving images.
# PIL is used in this code for image-related tasks, such as displaying images in the GUI.
import PIL.Image
import PIL.ImageTk

# Numerical operations library
# numpy (short for Numerical Python) provides functionality for numerical computations and array manipulation.
# It is used in this code for various numerical operations.
# Documentation: https://numpy.org/doc/
import numpy as np

# Operating system interaction library
# os is a library that provides functions for interacting with the operating system.
# It is used in this code for performing operating system-related tasks, such as file operations.
import os

# JSON library
# json is a library for working with JSON (JavaScript Object Notation) data.
# It provides functionality for reading and writing JSON files.
# json is used in this code for loading JSON data from files.
# Documentation: https://docs.python.org/3/library/json.html
import json

# Type hints library
# typing provides support for type hints in Python.
# It is used in this code for annotating function signatures with types.
# The specific type hints used in this code are not described in the comments.
from typing import TextIO

# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *

class facial_recognition(Frame):

    def __init__(self, parent, callback, *args, **kwargs) -> None:
        """
        Initializes the facial_recognition frame, starts a cv2 video capture, and starts recognizing faces in the current
        capture stream, this is then rendered to a Tk Frame. (This class is a subclass of a tk.Frame)
        """

        # Call Superclass Constructor
        Frame.__init__(self, parent, *args, **kwargs, highlightbackground = MEMA_BLACK, highlightthickness = 2)

        # Sets the callback function
        self.callback: function(str)
        self.callback = callback

        # Create Label to Display
        self.video_label = Label(self, bg = MEMA_BLACK)
        self.video_label.pack()

        # Used to auto-deny the after() after quit
        # (Stops the facial recognition)
        self.halt = False

        # Get a reference to webcam #0 (the default one)
        self.video_capture: cv2.VideoCapture
        self.video_capture = cv2.VideoCapture(0)

        self.load_face_encodings()

        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

        # Start facial recognition
        self.display_recognition()

    def load_face_encodings(self) -> None:
        """
        Loads the face encodings from the databank/userbank_n folder to recognize users.
        """

        # Initialize empty lists for known faces and names
        self.known_faces: list = []
        self.known_names: list = []

        # Define directory path
        directory_path: str
        directory_path = os.getcwd() + "/databank/"

        # Getting list of subfolders
        subfolders: list[str]
        subfolders = [f.path for f in os.scandir(directory_path) if f.is_dir()]

        for subfolder_path in subfolders:
            # Open the header JSON file
            file_header: TextIO = open(subfolder_path + "/header.json")
            json_header: json = json.load(file_header)

            # Get full name from JSON header
            self.known_names.append(str(json_header["user_id"]))

            # Load the face image
            face_image: face_recognition.ndarray = face_recognition.load_image_file(subfolder_path + "/face.jpg")

            # Encode the face
            face_encoding = face_recognition.face_encodings(face_image)[0]

            # Append the face encoding to the list of known faces
            self.known_faces.append(face_encoding)

        # Return
        return None

    def display_recognition(self) -> None:
        """
        Main function, grabs a frame, processes it and reschedules
        """

        if(self.halt): return

        # Grabs the current frame from the webcam and attempts to recognize faces within the frame image. Returns a 
        frame = self.process_frame()

        # Manipulates the frame image, adding nametags for the detected faces, this will be displayed if FACIAL_RECOGNITION_DEBUG_MODE is True
        if(MEMA_FACIAL_RECOGNITION_DEBUG_MODE): self.render_nametags(frame)
        
        # Displays the updated frame in the Tk Frame instance and schedules another scan
        self.display_and_reschedule(frame)

    def process_frame(self) -> Image:
        """
        Process a single frame of video, returns the processed frame
        """
        
        # Grab a single frame of video
        ret: cv2.OutputArray
        frame: Image
        ret, frame = self.video_capture.read()

        # Not needed, so removed
        del ret

        # Only process every other frame of video to save time
        if self.process_this_frame:

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame: cv2.Mat
            small_frame = cv2.resize(frame, (0, 0), fx=0.20, fy=0.20)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame: cv2.Mat
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            
            # Find all the faces and face encodings in the current frame of video
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            self.face_names = []
            self.match_known_faces()

        # Toggle the flag for processing the next frame
        self.process_this_frame = not self.process_this_frame
        
        # Return the processed frame
        return frame

    def match_known_faces(self) -> None:
        """
        Matches the face encodings with the known faces and assigns names to the recognized faces.
        """

        # List to store the recognized names
        self.face_names: list[str] = [] 

        for face_encoding in self.face_encodings:

            # Compare the face encoding with the known faces to check for matches
            matches: list[any]
            matches = face_recognition.compare_faces(self.known_faces, face_encoding)

            # Default name if no match is found
            name: str = "Unknown"

            # Find the known face with the smallest distance to the new face
            # The smallest distance indicates the best match
            face_distances: (cv2.ndarray | any)
            face_distances = face_recognition.face_distance(self.known_faces, face_encoding)

            # Uses numpy to find the closest match
            best_match_index: np.intp
            best_match_index = np.argmin(face_distances)

            # If a match is found in known_faces, assign the corresponding name to the recognized face
            if matches[best_match_index]:
                name = self.known_names[best_match_index]
                
            # Append the recognized name to the list of face names
            self.face_names.append(name)

            self.callback(name)

    def render_nametags(self, frame) -> None:

        # Display the results
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 5
            right *= 5
            bottom *= 5
            left *= 5
            
            # Render a circle around the face
            cv2.circle(frame, ((right+left)//2, (bottom+top)//2), right-left, (255, 255, 255), 3)
            
    def display_and_reschedule(self, frame) -> None:
        # Convert the frame to an image and display it in the Tkinter label
        img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        self.video_label.config(image=img)
        self.video_label.image = img

        # Schedule the next frame update
        self.after(10, self.display_recognition)

    def __del__(self) -> None:
        self.quit()

    def quit(self) -> None:

        # Sets to halt
        self.halt = True

        # Release handle to the webcam
        self.video_capture.release()
        cv2.destroyAllWindows()
        print("Login CV2 Instance Destroyed")