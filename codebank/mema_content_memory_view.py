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



class content_memory_view(content_frame):

    def __init__(self, parent, memoryspace_path: str, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Parent should be main window
        self.parent: any
        self.parent = parent

        # Memoryspace Path is the path to the current memoryspace
        self.memoryspace_path: str
        self.memoryspace_path = memoryspace_path

        # Current Frame (indexed from 0)
        self.frame: int
        self.frame = 0

        # Maximum Frames (calculated in setup_max_frames)
        self.max_frames: int
        self.max_frames = 0

        # Label to show the frame number
        self.frame_label: Label

        # Label to show the current memoryspace name
        self.memoryspace_label: Label

        # Memory Frame to show the current frame of the current memory
        self.memory_frame: Frame

        # Stored in `self.memory_frame`
        # Displays video (if it exists)
        self.memory_videoplayer: TkinterVideo

        # Stored in `self.memory_frame`
        # Displays image (if it exists)
        self.memory_image: Label

        # Stored in `self.memory_frame`
        # Displays memory caption (if it exists)
        self.memory_caption: Label

        # Setup
        self.setup_max_frames()
        self.initialize_gui()

    def setup_max_frames(self):
        # Finds the max frame. (Adds 1, as always needs an empty frame to add to)
        # Error checking
        try:
            self.max_frames = int(max([file.path.rpartition("/")[2][0] for file in os.scandir(self.memoryspace_path)]))+2
        except:
            self.max_frames = 1
        finally:
            if(self.max_frames < 2): self.max_frames = 1

    def initialize_gui(self):

        self.title_frame = Frame(self, bg = MEMA_WHITE)

        self.frame_label = Label(self.title_frame, text = f"Frame: {self.frame}", font = ("Arial", 36, "bold"), bg = MEMA_WHITE)
        self.frame_label.pack(side = RIGHT)

        selected_memory = self.memoryspace_path.split("memoryspace")[1][1:]
        self.memoryspace_label = Label(self.title_frame, text = selected_memory, font = ("Arial", 36, "bold"), fg = MEMA_BLACK, bg = MEMA_WHITE)
        self.memoryspace_label.pack(padx = (0,120), side = LEFT)

        self.title_frame.pack(pady = 20)

        self.memory_frame = Frame(self, bg = MEMA_WHITE)
        self.memory_frame.pack()
        
        self.update_memory_frame()
        self.update_buttons()

    def replay(self, event):
        self.memory_videoplayer.play()

    def update_memory_frame(self) -> None:
        """
        Updates the memory_frame to display the content of the new frame index. Changes
        what is displayed, including video, image and label.
        """

        # Destory the current frame
        self.memory_frame.destroy()
        self.memory_frame = Frame(self, bg=MEMA_WHITE)

        # Path to the current frame image (if exists)
        image_path: str
        video_path: str
        text_path: str
        image_path = self.memoryspace_path + "/" + str(self.frame) + "_content.jpeg"
        video_path = image_path.replace(".jpeg", ".mp4")
        text_path = image_path.replace("_content.jpeg", "_label.txt")

        # Adds video, image and label to frame if they exist.
        if exists(video_path): self.display_video_on_memory_frame(video_path)
        if exists(image_path): self.display_image_on_memory_frame(image_path)
        if exists(text_path): self.display_label_on_memory_frame(text_path)

        # Pack the new frame, with the newly added widgets
        self.memory_frame.pack(expand=True,fill = "both")

    def display_label_on_memory_frame(self, text_path: str):
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
        self.memory_caption = Label(self.memory_frame, text=text,borderwidth = 2, relief = "solid", fg = MEMA_BLACK, bg = "#FFFFFF", font = ("Arial", 26, "bold"), wraplength = 500)
        self.memory_caption.pack(ipadx=10,ipady=3,padx=5,pady=10)

    def display_image_on_memory_frame(self, image_path: str):
        # Create a local path for the image by extracting the file name
        local_image_path = "databank/" + image_path.rsplit("databank/")[1]
        
        # Open the image file, create an image object, and convert it to PhotoImage format
        img = ImageTk.PhotoImage(Image.open(local_image_path))
        
        # Create a label with the image and add it to the memory frame
        self.memory_image = Label(self.memory_frame, image=img, bg = MEMA_BLACK)
        self.memory_image.photo = img
        self.memory_image.pack(ipadx=3, ipady=3)

    def display_video_on_memory_frame(self, video_path: str):
        # Create a video player widget and set its size
        self.memory_videoplayer = TkinterVideo(master=self.memory_frame, scaled = True)
        self.memory_videoplayer.set_scaled(True, True)
        
        # Load the video file into the video player
        self.memory_videoplayer.load(video_path)
        
        # Add the video player to the memory frame
        self.memory_videoplayer.pack(expand=True, fill="both")

        # Play the video
        self.memory_videoplayer.play()
        
        # Bind the "<<Ended>>" event to the replay method
        self.memory_videoplayer.bind("<<Ended>>", self.replay)
        


    def next_frame(self):
        """
        Moves forward one frame, loops at self.max_frames. Reconfigures the frame label and
        memoryspace-frame, frame.
        """

        self.frame = (self.frame + 1) % self.max_frames
        self.frame_label.configure(text = f"Frame: {self.frame}")
        self.update_memory_frame()

    def update_buttons(self) -> None:
        """
        Updates the button frame to show options to go to the camera, add a label, go to the next frame or
        exit the current page (go back to the MeMa login page.)
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Next Frane", "NEXT_FRAME")
        buttons[1] = MEMA_EMPTY_BUTTON
        buttons[2] = MEMA_EMPTY_BUTTON
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def stop_videoplayer(self) -> None:
        """
        Attempts to stop the current videoplayer. Uses exception handling, in-case a video is not currently
        being displayed.
        """

        try: self.memory_videoplayer.stop()
        except: pass

    def callback(self, callback_request: dict[str:str]) -> None:

        match (callback_request["content"]):

            # This returns to the Memory Machine login screen
            case "HOME_EXIT":
                self.stop_videoplayer()
                self.parent.reset_path()

            # This takes the user to the next `frame` of a memory, it updates the memoryframe
            # frame to display the new content. It will loop around if it is at the max frames.
            case "NEXT_FRAME":
                self.stop_videoplayer()
                self.next_frame()
