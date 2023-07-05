from mema_content_frame import *
import cv2
import PIL
from mema_text_to_speech import *
from mema_data_access import *
from mema_content_homepage import *

class content_new_user_photo(content_frame):

    def __init__(self, parent, name, *args, **kwargs):
        content_frame.__init__(self, *args, **kwargs)

        speak("We need to take a photograph of you to login, please center your face and say TAKE PHOTO")

        self.current_image: Image = None
        self.kill_cam: bool = False

        self.parent = parent
        self.name = name

        self.title = Label(self, text = "Memory Machine", fg = MEMA_BLACK, bg = MEMA_WHITE, font = ("Arial", 36, "bold"))
        self.title.pack()

        description_text: str = "Let's take your photograph to login,\ncenter your face and say 'TAKE PHOTO'"
        self.description = Label(self, text = description_text, fg = MEMA_BLACK, bg = MEMA_WHITE, font = ("Arial", 30, "bold"))
        self.description.pack(pady = (0, 30))

        self.label = Label(self, anchor = CENTER, highlightbackground = MEMA_BLACK, highlightthickness = 2, bg = MEMA_BLACK)
        self.label.pack()
        self.cap = cv2.VideoCapture(0)
        self.show_frames()

        self.update_buttons()

    def update_buttons(self) -> None:
        """
        Updates the buttons to display the option to Take Photo or return to the main menu
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Take Photo", "NEW_USER_TAKE_PHOTO")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = ("Back", "NEW_USER_BACK")
        self.parent.set_input(buttons, False)

    def show_frames(self):
        if(self.kill_cam): return

        # Get the latest frame and convert into Image
        self.current_image = cv2.cvtColor(self.cap.read()[1],cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(self.current_image)
        # Convert image to PhotoImage
        imgtk = PIL.ImageTk.PhotoImage(image = img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        self.label.after(20, self.show_frames)

    def confirm_image(self):
        speak(self.name + ", is this picture okay?")

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Yes", "CONFIRM_IMAGE")
        buttons[1] = ("No", "UNCONFIRM_IMAGE")
        buttons[2] = (None, None)
        buttons[3] = ("Back", "NEW_USER_BACK")
        self.parent.set_input(buttons, False)

    def callback(self, callback_request: dict[str:str]):
        
        match callback_request["content"]:

            case "NEW_USER_TAKE_PHOTO":
                self.kill_cam = True
                self.confirm_image()

            case "NEW_USER_BACK":
                self.parent.reset_path()
            
            case "CONFIRM_IMAGE":
                new_user_id: int = new_user(self.name, self.current_image)
                self.parent.switch_content(content_home, new_user_id)

            case "UNCONFIRM_IMAGE":
                self.kill_cam = False
                self.update_buttons()
                self.show_frames()
                speak("Sorry, say TAKE PHOTO when you are ready.")
                
    def __del__(self):
        self.cap.release()
            