import numpy as np
import cv2
from tkinter import *
import PIL
from PIL import ImageTk
from mema_content_frame import *
from tkVideoPlayer import TkinterVideo
import os

class content_record(Frame):
    """
    A class for recording video and taking photos using a webcam.

    Args:
        parent (tk.Widget): The parent widget.

    Attributes:
        recording (bool): Indicates whether recording is in progress.
        label (tk.Label): The label to display the video stream.
        stop_button (tk.Button): The button to stop recording.
        record_button (tk.Button): The button to start/stop recording.
        take_photo_button (tk.Button): The button to take a photo.
        cap (cv2.VideoCapture): The video capture object.
        out (cv2.VideoWriter): The video writer object.
        current_image (numpy.ndarray): The current image frame from the webcam.
    """

    def __init__(self, parent, memoryspace_path: str, memoryspace_frame: str, return_page, *args, **kwargs):
        """
        Initialize the ContentRecord object.

        Args:
            parent (tk.Widget): The parent widget.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(parent, *args, **kwargs)

        self.return_page = return_page
        self.memoryspace_path = memoryspace_path
        self.memoryspace_frame = memoryspace_frame

        self.parent = parent
        self.recording = False
        self.halt = False

        # Create and pack the label to display the video stream
        self.label = Label(self, anchor=CENTER, highlightbackground="black", highlightthickness=2, bg="black")
        self.label.pack()

        # Create a video capture object for the webcam
        self.cap = cv2.VideoCapture(0)

        self.update_buttons()

        # Start displaying video frames
        self.show_frames()

    def update_buttons(self):

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Start Recording", "RECORD_RECORD")
        buttons[1] = ("Take Photo", "RECORD_TAKE_PHOTO")
        buttons[2] = (None, None)
        buttons[3] = ("Back", "RECORD_BACK")
        self.parent.set_input(buttons, True)

    def update_buttons_photo(self):

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Keep Photo", "RECORD_PHOTO_KEEP")
        buttons[1] = ("Retake Photo", "RECORD_PHOTO_RETAKE")
        buttons[2] = (None, None)
        buttons[3] = ("Back", "RECORD_BACK")
        self.parent.set_input(buttons, True)

    def update_buttons_video(self):

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Keep Video", "RECORD_VIDEO_KEEP")
        buttons[1] = ("Retake Video", "RECORD_VIDEO_RETAKE")
        buttons[2] = (None, None)
        buttons[3] = ("Back", "RECORD_BACK")
        self.parent.set_input(buttons, True)

    def toggle_recording(self):
        """
        Toggle the recording state.

        If not currently recording, start recording and change button text to 'Stop Recording'.
        If already recording, stop recording and change button text to 'Start Recording'.
        """
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        """
        Start recording video.

        This method initializes the video writer object and sets the recording flag to True.
        """
        # Define the codec and create a VideoWriter object
        video_path = self.memoryspace_path + "/" + self.memoryspace_frame + "_video.mp4"
        self.fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        self.out = cv2.VideoWriter(video_path, self.fourcc, 20.0, (640, 480))
        self.recording = True

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Stop Recording", "RECORD_RECORD")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = ("Back", "RECORD_BACK")
        self.parent.set_input(buttons, True)

    def stop_recording(self):
        """
        Stop recording video.

        This method releases the video writer object and sets the recording flag to False.
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Start Recording", "RECORD_RECORD")
        buttons[1] = ("Take Photo", "RECORD_TAKE_PHOTO")
        buttons[2] = (None, None)
        buttons[3] = ("Back", "RECORD_BACK")
        self.parent.set_input(buttons, True)

        self.recording = False
        self.out.release()

        self.update_buttons_video()
        self.show_video()

    def take_photo(self):
        """
        Take a photo and save it as an image file.

        The photo is saved as 'test.jpg' in the current directory.
        """
        try:
            self.halt = True
            self.update_buttons_photo()
            
        except Exception as e:
            print(f"Could not take photo. Exception: {e}")

    def show_frames(self):

        # reads frames from a camera 
        # ret checks return at each frame
        ret, frame = self.cap.read() 

        # check if photo taken
        if(self.halt): return

        # output the frame
        if(self.recording): self.out.write(frame) 
        
        self.current_image = cv2.cvtColor(self.cap.read()[1],cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(self.current_image)

        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        
        self.after(20, self.show_frames)

    def replay(self, event):
        print("replayed")
        self.videoplayer.play()

    def show_video(self):
        
        self.label.destroy()
        self.halt = True
        video_path: str = self.memoryspace_path + "/" + self.memoryspace_frame + "_video.mp4"
        self.videoplayer = TkinterVideo(master=self, scaled=True)
        self.videoplayer.load(video_path)
        self.videoplayer.pack(expand=True, fill="both")
        self.videoplayer.play()
        self.videoplayer.bind("<<Ended>>", self.replay)

    def stop(self):

        # Close the window / Release webcam
        self.cap.release()
        
        # De-allocate any associated memory usage 
        cv2.destroyAllWindows()

    def callback(self, callback_request:dict):
        
        match callback_request["content"]:

            case "RECORD_RECORD":
                self.toggle_recording()

            case "RECORD_TAKE_PHOTO":
                self.take_photo()

            case "RECORD_BACK":
                self.stop()
                self.parent.switch_content(self.return_page, self.memoryspace_path)
                
            case "RECORD_PHOTO_KEEP":
                path = self.memoryspace_path + "/" + self.memoryspace_frame + "_photo.jpeg"
                cv2.imwrite(path, cv2.cvtColor(self.current_image, cv2.COLOR_BGR2RGB))
                self.stop()
                self.parent.switch_content(self.return_page, self.memoryspace_path)
            
            case "RECORD_PHOTO_RETAKE":
                self.halt = False
                self.show_frames()
                self.update_buttons()

            case "RECORD_VIDEO_RETAKE":
                print("Destroy")
                self.videoplayer.destroy()
                self.label = Label(self, anchor=CENTER, highlightbackground="black", highlightthickness=2, bg="black")
                self.label.pack()
                self.update()
                self.halt = False
                self.show_frames()
                self.update_buttons()
                os.remove("sample.mp4")

            case "RECORD_VIDEO_KEEP":
                self.stop()
                self.parent.switch_content(self.return_page, self.memoryspace_path)
