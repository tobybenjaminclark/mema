from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
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

        speak("Let's set you up with Memory Machine. What is your name?")

        # Setup webcam frame
        self.label = Label(self, text="Welcome to Memory Machine\n\nWhat is your name?", font = ("Arial", 50, "bold"))
        self.label.pack()

    def confirm_name(self, name: str) -> None:
        self.awaiting_confirmation = True
        self.name_buffer = name
        speak("You said, " + name + ", is that correct? Simply say Yes or No.")

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Yes", "CONFIRM_YES")
        buttons[1] = ("No", "CONFIRM_NO")
        buttons[2] = (None, None)
        buttons[3] = (None, None)
        self.parent.set_input(buttons, False)

    def update_buttons(self) -> None:

        self.awaiting_confirmation: bool = False
        self.name_buffer: str = ""

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Back", "NEW_USR_BACK")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = (None, None)
        self.parent.set_input(buttons, False)

    def callback(self, callback_request: dict[str:str]) -> None:

        match (callback_request["content"]):
            case "NEW_USR_BACK":
                self.parent.reset_path()
                
            case "CONFIRM_YES":
                speak("Welcome to Memory Machine ", self.name_buffer)

            case "CONFIRM_NO":
                speak("What is your name?")
                self.update_buttons()

            case _:
                self.confirm_name(callback_request["content"])





