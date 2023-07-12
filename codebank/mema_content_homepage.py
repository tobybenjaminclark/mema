# Generic MeMa Imports
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
from mema_data_access import *
from mema_content_memory_create_name import *
from mema_record_content import *
from mema_constants import *
from mema_content_memory_list import *

# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *

class content_home(content_frame):

    def __init__(self, parent, user_id, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent
        self.user_id = user_id
        self.update_buttons()

        self.label2 = Label(self, text = "Welcome to MeMa", font = ("Arial", 30, "bold"))
        self.label = Label(self, text = str(get_user(self.user_id)["first_name"]), font = ("Arial", 50, "bold"))
        self.label2.pack()
        self.label.pack()

    def update_buttons(self) -> None:

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Create New Memory", "HOME_NEWM")
        buttons[1] = ("View Memories", "HOME_VIEWM")
        buttons[2] = MEMA_EMPTY_BUTTON
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def callback(self, callback_request: dict[str:str]) -> None:

        match (callback_request["content"]):
            case "HOME_EXIT":
                self.parent.reset_path()
            case "HOME_NEWM": 
                self.parent.switch_content(content_memory_create_name, self.user_id)
            case "HOME_VIEWM":
                self.parent.switch_content(content_memory_list, self.user_id)





