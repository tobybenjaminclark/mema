from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *

class content_login(content_frame):

    def __init__(self, parent, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent
        self.update_buttons()
        self.previous_callback = "a"

        # Setup webcam frame
        facial_recognition_frame = facial_recognition(self, self.callback)
        facial_recognition_frame.pack()

    def update_buttons(self) -> None:

        buttons: list[(str, str)] = [0, 0, 0, 0]

        buttons[0] = ("Login", "LOGIN_LOGIN")
        buttons[1] = ("New", "LOGIN_NEW")
        buttons[2] = ("Languages", "LOGIN_LANGUAGES")
        buttons[3] = ("Exit", "LOGIN_EXIT")

        self.parent.set_buttons(buttons, True)

    def callback(self, callback_str:str) -> None:

        if (callback_str == "LOGIN_EXIT"):
            print("quitting")
            quit()

        if(self.previous_callback == callback_str):
            return
        else:
            print(callback_str)
            self.previous_callback = callback_str



