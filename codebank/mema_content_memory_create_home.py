# Generic MeMa Imports
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
from mema_content_new_user_photo import *
from mema_data_access import *
from mema_record_content import *
from mema_content_memory_create_label import *

# sys is a module that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter
# It is used in this code for error logging, achieved through writing to the stderr stream
import sys

# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *

# PIL (Python Imaging Library) is a library used for opening, manipulating, and saving many different image file formats.
# ImageTk module provides support for displaying images in Tkinter GUI.
# Image module provides a class with the same name which is used to represent a PIL image.
from PIL import ImageTk, Image

# exists is a function in the os.path module that checks whether a path exists or not. In this code
# it is used to detect whether a memory exists or not, before loading it to avoid causing an error.
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
        except:
            self.max_frames = 1
        finally:
            if(self.max_frames < 2): self.max_frames = 1

        print(self.max_frames)

        files = [file.path for file in os.scandir(memoryspace_path)]
        print(files)

        self.frame_label = Label(self, text = f"Frame: {self.frame}")
        self.frame_label.pack(pady = 10)

        self.memory_frame = Frame(self, bg = MEMA_WHITE)
        self.memory_frame.pack()
        
        self.update_frame()
        self.update_buttons()

    def replay(self, event):
        self.videoplayer.play()

    def update_frame(self) -> None:
        
        # Path to the current frame image (if exists)
        image_path: str
        image_path = self.memoryspace_path + "/" + str(self.frame) + "_content.jpeg"

        video_path: str
        video_path = image_path.replace(".jpeg", ".mp4")

        text_path: str
        text_path = image_path.replace("_content.jpeg", "_label.txt")

        image_exists = exists(image_path)
        video_exists = exists(video_path)
        label_exists = exists(text_path)

        print(f"mema_content_memory_create_home: {image_exists}/{video_exists} = {image_path},\t{video_path}")

        self.memory_frame.destroy()
        self.memory_frame = Frame(self, bg=MEMA_WHITE)

        # Adds video, image and label to frame if they exist.
        if video_exists: self.add_video_to_frame(video_path)
        if image_exists: self.add_image_to_frame(image_path)
        if label_exists: self.add_label_to_frame(text_path)

        self.memory_frame.pack(expand=True,fill = "both")

    def add_label_to_frame(self, text_path: str):
        """
        Opens the label for the current frame
        """

        # Variable Types
        file: TextIO
        text: str

        # Open the text file and read its content
        try:
            file = open(text_path, 'r')
            text = file.read()
            file.close()
        except:
            text = f"Could not read label: {text_path}"
            print(f"mema_content_memory_create_home: could not read label @ {text_path}", file = sys.stderr)
        
        # Create a label with the text content and add it to the memory frame
        self.memory_label = Label(self.memory_frame, text=text,borderwidth = 2, relief = "solid", fg = MEMA_BLACK, bg = "#FFFFFF", font = ("Arial", 26, "bold"), wraplength = 500)
        self.memory_label.pack(ipadx=10,ipady=3,padx=5,pady=10)

    def add_image_to_frame(self, image_path: str):
        # Create a local path for the image by extracting the file name
        local_image_path = "databank/" + image_path.rsplit("databank/")[1]
        
        # Open the image file, create an image object, and convert it to PhotoImage format
        img = ImageTk.PhotoImage(Image.open(local_image_path))
        
        # Create a label with the image and add it to the memory frame
        self.panel = Label(self.memory_frame, image=img, bg = MEMA_BLACK)
        self.panel.photo = img
        self.panel.pack(ipadx=3, ipady=3)

    def add_video_to_frame(self, video_path: str):
        # Create a video player widget and set its size
        self.videoplayer = TkinterVideo(master=self.memory_frame, scaled = True)
        self.videoplayer.set_scaled(True, True)
        
        # Load the video file into the video player
        self.videoplayer.load(video_path)
        
        # Add the video player to the memory frame
        self.videoplayer.pack(expand=True, fill="both")

        # Play the video
        self.videoplayer.play()
        
        # Bind the "<<Ended>>" event to the replay method
        self.videoplayer.bind("<<Ended>>", self.replay)
        


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
                self.parent.switch_content(content_memory_create_label, self.memoryspace_path, content_memory_create_home, self.frame)