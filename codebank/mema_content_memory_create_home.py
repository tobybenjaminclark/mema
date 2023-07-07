from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
from mema_content_new_user_photo import *
from mema_data_access import *
from mema_content_memory_create_name import *
from mema_record_content import *
from mema_content_memory_create_label import *
from PIL import ImageTk, Image
from os.path import exists

class content_memory_create_home(content_frame):

    def __init__(self, parent, memoryspace_path: str, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent
        self.memoryspace_path: str = memoryspace_path
        self.frame = 0

        # Finds the max frame. (Adds 1, as always needs an empty frame to add to)
        # Error checking
        try:
            self.max_frames = int(max([file.path.rpartition("/")[2][0] for file in os.scandir(memoryspace_path)]))+2
        finally:
            if(self.max_frames < 2): self.max_frames = 1

        print(self.max_frames)

        files = [file.path for file in os.scandir(memoryspace_path)]
        print(files)

        self.frame_label = Label(self, text = f"Frame: {self.frame}")
        self.frame_label.pack(pady = 10)

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

        text_path: str
        text_path = image_path.replace("_photo.jpeg", "_label.txt")

        image_exists = exists(image_path)
        video_exists = exists(video_path)
        label_exists = exists(text_path)

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
            self.videoplayer.pack()

        if label_exists:
            with open(text_path, "r") as file:
                text = file.read()
            self.memory_label = Label(self.memory_frame, text = text)
            self.memory_label.pack()

        self.memory_frame.pack()

    def next_frame(self):
        self.frame = (self.frame + 1) % self.max_frames
        self.frame_label.configure(text = f"Frame: {self.frame}")
        self.update_frame()

    def update_buttons(self) -> None:

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Camera", "CREATE_HOME_CAM")
        buttons[1] = ("Add Label","CREATE_HOME_LABEL")
        buttons[2] = ("Next Frame", "NEXT_FRAME")
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def callback(self, callback_request: dict[str:str]) -> None:

        match (callback_request["content"]):
            case "HOME_EXIT":
                self.parent.reset_path()
            case "CREATE_HOME_CAM": 
                self.parent.switch_content(content_record, self.memoryspace_path, str(self.frame), content_memory_create_home)
            case "NEXT_FRAME":
                self.next_frame()
            case "CREATE_HOME_LABEL":
                self.parent.switch_content(content_memory_create_label, self.memoryspace_path, content_memory_create_home)