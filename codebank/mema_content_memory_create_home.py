from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
from mema_content_new_user_photo import *
from mema_data_access import *
from mema_content_memory_create_name import *
from mema_record_content import *

class content_memory_create_home(content_frame):

    def __init__(self, parent, memoryspace_path: str, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent
        self.memoryspace_path: str = memoryspace_path
        self.frame = 0
        self.update_buttons()

        self.label2 = Label(self, text = "Welcome to MeMa", font = ("Arial", 30, "bold"))
        self.label = Label(self, text = str(get_user(self.user_id)["first_name"]), font = ("Arial", 50, "bold"))
        self.label2.pack()
        self.label.pack()

    def update_buttons(self) -> None:

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Camera", "CREATE_HOME_CAM")
        buttons[1] = ("View Memories", "HOME_VIEWM")
        buttons[2] = (None, None)
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def callback(self, callback_request: dict[str:str]) -> None:

        match (callback_request["content"]):
            case "HOME_EXIT":
                self.parent.reset_path()
            case "CREATE_HOME_CAM": 
                self.parent.switch_content(content_record, self.memoryspace_path, self.frame)
            case "HOME_VIEWM":
                print("View Memories")