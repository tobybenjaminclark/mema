from tkinter import *
from mema_content_frame import *
from PIL import Image, ImageTk
import cv2

class content_login(content_frame):

    def __init__(self, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Setup webcam frame
        self.label: Label
        self.label = Label(self, width = 800, height = 500)
        self.label.grid(row=0, column=0)

        # Using open-cv2 video capture
        self.cap: cv2.VideoCapture = cv2.VideoCapture("/dev/video0")
        self.show_frames()

    def show_frames(self) -> None:

        # Grabs the latest frame from the video capture & saves as image
        img: Image = Image.fromarray(cv2.cvtColor(self.cap.read()[1],cv2.COLOR_BGR2RGB))

        # Convert image frame to PhotoImage (compatiable with Tkinter)
        imgtk = ImageTk.PhotoImage(image = img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

        # Repeat after an interval to capture continiously
        self.label.after(20, self.show_frames)



