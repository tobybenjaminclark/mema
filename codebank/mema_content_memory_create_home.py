from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
from mema_content_new_user_photo import *
from mema_data_access import *
from mema_content_memory_create_name import *
from mema_record_content import *
from PIL import ImageTk, Image
from os.path import exists

class content_memory_create_home(content_frame):

    def __init__(self, parent, memoryspace_path: str, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent
        self.memoryspace_path: str = memoryspace_path
        self.frame = 0

        files = [file.path for file in os.scandir(memoryspace_path)]
        print(files)

        self.memory_frame = Frame(self)
        self.memory_frame.pack()
        
        self.update_frame()
        self.update_buttons()

    def replay(self, event):
        self.videoplayer.play()

    def update_frame(self) -> None:
        
        # Path to the current frame image (if exists)
        image_path: str
        image_path = self.memoryspace_path + "/" + str(self.frame) + "_photo.jpeg"

        video_path: str
        video_path = image_path.replace("_photo.jpeg", "_video.mp4")

        

        image_exists = exists(image_path)
        video_exists = exists(video_path)

        print(f"mema_content_memory_create_home: {image_exists}/{video_exists} = {image_path},\t{video_path}")

        self.memory_frame.destroy()
        self.memory_frame = Frame(self)

        if(image_exists):
            local_image_path = "databank/" + image_path.rsplit("databank/")[1]
            img = ImageTk.PhotoImage(Image.open(local_image_path))
            self.panel = Label(self.memory_frame, image=img)
            self.panel.photo = img
            self.panel.pack()

        if(video_exists):
            self.videoplayer = TkinterVideo(master=self.memory_frame, scaled=True)
            self.videoplayer.load(video_path)
            self.videoplayer.pack(expand=True, fill="both")
            self.videoplayer.play()
            self.videoplayer.bind("<<Ended>>", self.replay)
            self.videoplayer.pack(side=LEFT)

        self.memory_frame.pack()


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