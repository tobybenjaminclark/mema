from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from mema_content_new_user import *
from mema_data_access import *

import cv2

class content_login(content_frame):

    def __init__(self, parent, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent
        self.update_buttons()
        self.previous_callback = "a"

        self.current_face = "Unknown"

        # Setup webcam frame
        self.facial_recognition_frame = facial_recognition(self, self.facial_recognition_callback)
        self.facial_recognition_frame.pack()

    def update_buttons(self) -> None:

        buttons: list[(str, str)] = [0, 0, 0, 0]

        buttons[0] = ("Login", "LOGIN_LOGIN")
        buttons[1] = ("New", "LOGIN_NEW")
        buttons[2] = ("Languages", "LOGIN_LANGUAGES")
        buttons[3] = ("Exit", "LOGIN_EXIT")

        self.parent.set_input(buttons, True)

    def facial_recognition_callback(self, name:str) -> None:
        self.current_face = name

    def callback(self, callback_request:dict[str:str]) -> None:

        match callback_request["content"]:

            case "LOGIN_EXIT":
                self.parent.quit()
            
            case "LOGIN_NEW":
                self.facial_recognition_frame.quit()
                del self.facial_recognition_frame
                self.parent.switch_content(content_new_user)

            case "LOGIN_LOGIN":

                print(self.current_face)
                if(self.current_face == "Unknown"): return

                x = get_user(self.current_face)
                print(x)
            
            case "LOGIN_LANGUAGES":
                print("Languages")




