from mema_content_frame import *
import cv2
from PIL import ImageTk, Image
from mema_text_to_speech import *

"""
camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            
"""

class content_new_user_photo(content_frame):

    def __init__(self, parent, name, *args, **kwargs):
        content_frame.__init__(self, *args, **kwargs)

        self.current_image: Image = None

        self.parent = parent
        self.name = name

        self.label = Label(self, text = "LOGIN")
        self.label.grid(row=0, column=0)
        self.label = Label(self)
        self.label.grid(row=0, column=0)
        self.cap = cv2.VideoCapture(0)
        self.show_frames()

        self.update_buttons()

    def update_buttons(self) -> None:

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Take Photo", "TAKE_PHOTO")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = (None, None)
        self.parent.set_input(buttons, False)

    def show_frames(self):
        # Get the latest frame and convert into Image
        self.current_image = cv2.cvtColor(self.cap.read()[1],cv2.COLOR_BGR2RGB)
        img = Image.fromarray(self.current_image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        self.label.after(20, self.show_frames)

    def callback(self, callback_request: dict[str:str]):
        
        if(callback_request["content"] == "TAKE_PHOTO"):
            cv2.imwrite('opencv.png', cv2.cvtColor(self.current_image, cv2.COLOR_BGR2RGB))
            speak(self.name + ", is this picture okay?")
            