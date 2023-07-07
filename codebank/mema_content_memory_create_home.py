from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
from mema_content_new_user_photo import *
from mema_data_access import *
from mema_content_memory_create_name import *
from mema_record_content import *
from PIL import ImageTk, Image

class content_memory_create_home(content_frame):

    def __init__(self, parent, memoryspace_path: str, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent
        self.memoryspace_path: str = memoryspace_path
        self.frame = 0

        files = [file.path for file in os.scandir(memoryspace_path)]
        print(files)

        for path in files:
            # If an image, show the image
            if(path.endswith(".jpeg")):
                x = path.rsplit("databank/")
                y = "databank/" + x[1]
                path = y
                img = ImageTk.PhotoImage(Image.open(path))
                panel = Label(self, image=img)
                panel.photo = img
                panel.grid(column=2,row=2)
        
        self.update_buttons()

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
                self.parent.switch_content(content_record, self.memoryspace_path, str(self.frame), content_memory_create_home)
            case "HOME_VIEWM":
                print("View Memories")