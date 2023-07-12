# Generic MeMa Imports
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
from mema_content_new_user_photo import *
from mema_data_access import *
from mema_record_content import *
from mema_content_memory_create_label import *

# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *



class content_memory_list(content_frame):

    def __init__(self, parent, user_id: int, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Parent should be main window
        self.parent: any
        self.parent = parent

        # Memoryspace Path is the path to the current memoryspace
        self.user_id: str
        self.user_id = user_id

        self.memoryspaces: list = []

        self.update_buttons()
        self.find_available_memories()


    def find_available_memories(self) -> None:
        directory_path = os.getcwd() + "/databank/userbank_" + str(self.user_id) + "/"
        subfolders = [f.path for f in os.scandir(directory_path) if f.is_dir()]
        print(subfolders)


    def update_buttons(self) -> None:
        """
        Updates the button frame to show options to go to the camera, add a label, go to the next frame or
        exit the current page (go back to the MeMa login page.)
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("VIEW", "MEMORY_LIST_VIEW")
        buttons[1] = ("NEXT","MEMORY_LIST_NEXT")
        buttons[2] = (None, None)
        buttons[3] = ("EXIT", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def stop_videoplayer(self) -> None:
        pass

    def callback(self, callback_request: dict[str:str]) -> None:
        pass