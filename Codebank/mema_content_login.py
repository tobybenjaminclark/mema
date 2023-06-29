from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from PIL import Image, ImageTk
import cv2

class content_login(content_frame):

    def __init__(self, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Setup webcam frame
        facial_recognition_frame = facial_recognition(self)
        facial_recognition_frame.pack()



