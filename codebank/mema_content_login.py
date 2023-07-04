from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from mema_content_new_user import *
from mema_data_access import *
from mema_content_homepage import *

class content_login(content_frame):

    def __init__(self, parent, *args, **kwargs)-> None:
        """
        Initiazation method calls the superclass constructor, before setting up the buttons and creating the
        Facial Recognition Frame. See mema_facial_recognition for how that works.
        """
        content_frame.__init__(self, *args, **kwargs)

        # Sets the parent, updates the buttons
        self.parent = parent
        self.update_buttons()

        # Sets the current face to Unknown.
        self.current_face = "Unknown"

        # This will display MeMa at the top of the screen
        self.mema_label = Label(self, text = "Memory Machine", font = ("Arial", 56, "bold"))
        self.mema_label.pack(pady = 20)

        # This sets up the Facial Recognition Frame, which recognizes faces using cv2 & face_recognition modules.
        # It will display the webcam, and will pass the recognized face UserID to facial_recognition_callback() method.
        self.facial_recognition_frame = facial_recognition(self, self.facial_recognition_callback, width = 800)
        self.facial_recognition_frame.pack()

    def update_buttons(self) -> None:
        """
        Updates the buttons to show: LOGIN, NEW, LANGUAGES, EXIT. Callbacks for these can be seen internally
        to the class. Reads aloud the new button names.
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Login", "LOGIN_LOGIN")
        buttons[1] = ("New", "LOGIN_NEW")
        buttons[2] = ("Languages", "LOGIN_LANGUAGES")
        buttons[3] = ("Exit", "LOGIN_EXIT")
        self.parent.set_input(buttons, True)

    def facial_recognition_callback(self, name:str) -> None:
        """
        Updates the currently recognized face, this is used if the user activates the LOGIN flow.
        """
        self.current_face = name

    def callback(self, callback_request:dict[str:str]) -> None:
        """
        Callback method called when the user interacts (speech/button), calls the appropriate response.
        """

        match callback_request["content"]:

            # Exit the program
            case "LOGIN_EXIT":
                self.parent.quit()
            
            # Create a new user
            case "LOGIN_NEW":
                self.facial_recognition_frame.quit()
                del self.facial_recognition_frame
                self.parent.switch_content(content_new_user)

            # Login using the current face
            case "LOGIN_LOGIN":

                print(self.current_face)
                if(self.current_face == "Unknown"): return

                user_id = get_user(self.current_face)
                self.parent.switch_content(content_home, self.current_face)
            
            # Change language
            case "LOGIN_LANGUAGES":
                print("Languages")




