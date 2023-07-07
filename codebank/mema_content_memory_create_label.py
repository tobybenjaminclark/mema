from mema_content_frame import *
from mema_speech_recognition import *

class content_memory_create_label(content_frame):

    def __init__(self, parent, memoryspace_path: str, return_obj) -> None:
        self.parent = parent
        self.memoryspace_path = memoryspace_path
        self.return_obj = return_obj
        self.update_buttons()

    def update_buttons(self):

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Record Label", "RECORD_LABEL")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def record_label(self):

        with noalsaerr():
            s = recognize_speech_internal()
        print(s)

    def callback(self, callback_request: dict) -> None:
        
        match callback_request["content"]:

            case "RECORD_LABEL":
                self.record_label()

            case "HOME_EXIT":
                self.parent.switch_content(self.return_obj, self.memoryspace_path)