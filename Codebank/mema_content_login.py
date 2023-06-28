from tkinter import *
from mema_content_frame import *
from PIL import Image, ImageTk
import cv2

class content_login(content_frame):

    def __init__(self, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        self.label = Label(self, text = "LOGIN")
        self.label.grid(row=0, column=0)
        self.label =Label(self)
        self.label.grid(row=0, column=0)
        self.cap= cv2.VideoCapture(0)
        self.show_frames()

    # Define function to show frame
    def show_frames(self):
        # Get the latest frame and convert into Image
        cv2image= cv2.cvtColor(self.cap.read()[1],cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        self.label.after(20, self.show_frames)



