from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
from mema_content_new_user_photo import *
import cv2



class content_new_user(content_frame):

    def __init__(self, parent, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent

        self.intro_label: Label = Label(self, text = "Welcome to", fg = MEMA_BLACK, bg = MEMA_WHITE, font = ("Arial", 26, "bold"))
        self.main_label: Label = Label(self, text = "Memory Machine", fg = MEMA_BLACK, bg = MEMA_WHITE, font = ("Arial", 46, "bold"))
        self.sub_label: Label = Label(self, text = "What's your name?", fg = MEMA_BLACK, bg = MEMA_WHITE, font = ("Arial", 46, "bold"))
        self.intro_label.pack()
        self.main_label.pack(pady=(0,50))
        self.sub_label.pack()

        self.update_buttons()
        self.previous_callback = "a"
        self.sub_label.configure(text = "What's your name?")

        speak("Let's set you up with Memory Machine. What is your name?")



    def confirm_name(self, name: str) -> None:
        self.awaiting_confirmation = True
        self.name_buffer = name
        speak("You said, " + name + ", is that correct? Simply say Yes or No.")
        self.sub_label.configure(text = "Did you say " + name + "?")
        self.update()

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Yes", "CONFIRM_YES")
        buttons[1] = ("No", "CONFIRM_NO")
        buttons[2] = (None, None)
        buttons[3] = (None, None)
        self.parent.set_input(buttons, False)

    def update_buttons(self) -> None:

        self.awaiting_confirmation: bool = False
        self.name_buffer: str = ""

        self.sub_label.configure(text = "Sorry, please repeat your name")
        self.update()

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Back", "NEW_USR_BACK")
        buttons[1] = ("Toby", "toby")
        buttons[2] = (None, None)
        buttons[3] = (None, None)
        self.parent.set_input(buttons, False)

    def callback(self, callback_request: dict[str:str]) -> None:

        match (callback_request["content"]):
            case "NEW_USR_BACK":
                self.parent.reset_path()

            case "CONFIRM_YES":
                speak("Welcome to Memory Machine " + self.name_buffer)
                self.after(2500, self.progress)

            case "CONFIRM_NO":
                speak("Sorry, please could you repeat your name?")
                self.update_buttons()

            case _:
                self.confirm_name(callback_request["content"])

    def progress(self) -> None:

        self.parent.switch_content(content_new_user_photo, self.name_buffer)





