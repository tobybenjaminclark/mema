from mema_content_frame import *
from mema_text_to_speech import *

class content_memory_create(content_frame):

    def __init__(self, parent, user_id: int, *args, **kwargs) -> None:
        content_frame.__init__(self, *args, **kwargs)
        self.parent = parent
        self.user_id: int = user_id

        return None

    def update_buttons(self) -> None:

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Camera", "MEM_CREATE_CAMERA")
        buttons[1] = ("Audio", "MEM_CREATE_AUDIO")
        buttons[2] = ("Caption", "MEM_CREATE_CAPTION")
        buttons[3] = ("Back", "MEM_CREATE_BACK")
        self.parent.set_input(buttons, True)

    def setup_gui(self) -> None:

        return None

    def callback(self, callback_request:dict) -> None:
        
        match callback_request["content"]:

            case "MEM_CREATE_CAMERA":
                pass

            case "MEM_CREATE_AUDIO":
                pass

            case "MEM_CREATE_CAPTION":
                pass

            case "MEM_CREATE_BACK":
                self.parent.reset_path()

        return None