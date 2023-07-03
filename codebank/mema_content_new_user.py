from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
import cv2

"""
camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            cv2.imwrite('opencv.png', image)
            del(camera)
"""

class content_new_user(content_frame):

    def __init__(self, parent, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent
        self.update_buttons()
        self.previous_callback = "a"

        # Setup webcam frame
        self.label = Label(self, text="Take photo")
        self.label.pack()

    def update_buttons(self) -> None:

        buttons: list[(str, str)] = [0, 0, 0, 0]

        buttons[0] = ("Back", "NEW_USR_BACK")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = (None, None)

        self.parent.set_input(buttons, True)

    def callback(self, callback_str:str) -> None:

        if (callback_str == "LOGIN_EXIT"):
            print("quitting")
            quit()

        if(callback_str == "LOGIN_NEW"):
            self.facial_recognition_frame.quit()
            del self.facial_recognition_frame

            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            cv2.imwrite('opencv.png', image)
            del(camera)


        if(self.previous_callback == callback_str):
            return
        else:
            print(callback_str)
            self.previous_callback = callback_str




