from tkinter import *
from mema_content_frame import *
from mema_facial_recognition import *
from mema_text_to_speech import *
from mema_content_new_user_photo import *
import cv2



class content_new_user(content_frame):

    def __init__(self, parent, *args, **kwargs)-> None:
        """
        Initializes the GUI and frame variables (awaiting_confirmation & name_buffer)
        """

        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent

        # Is the user confirming their name?
        self.awaiting_confirmation: bool
        self.awaiting_confirmation = False

        # Buffer to store the spoken name in
        self.name_buffer: str
        self.name_buffer = "a"

        # Update buttons and setup the GUI
        # True is passed to update_buttons here as it represents the first time the buttons are 
        # created. Look at the update_buttons() method for more information.
        self.setup_gui()
        self.update_buttons(True)
        
        speak("Let's set you up with Memory Machine. What is your name?")

    def setup_gui(self) -> None:
        """
        Initializes this frames GUI, creating the introduction labels.
        """

        self.setup_intro_label()
        self.setup_main_label()
        self.setup_sub_label()
        
    def setup_intro_label(self, label_text:str = "Welcome to") -> None:
        """
        Creates a label saying "Welcome to", this should be placed above the main label ("Memory Machine")
        """

        self.intro_label: Label
        self.intro_label = Label(self, text = label_text, fg = MEMA_BLACK, bg = MEMA_WHITE, font = ("Arial", 26, "bold"))
        self.intro_label.pack()

    def setup_main_label(self, label_text:str = "Memory Machine") -> None:
        """
        Creates a large label saying "Memory Machine". This label has a considerable amount of padding below (50px)
        """

        self.main_label: Label
        self.main_label = Label(self, text = label_text, fg = MEMA_BLACK, bg = MEMA_WHITE, font = ("Arial", 46, "bold"))
        self.main_label.pack(pady=(0,50))

    def setup_sub_label(self, label_text:str = "What's your name?") -> None:
        """
        Creates a sub label, asking the user what their name is
        """

        self.sub_label: Label
        self.sub_label = Label(self, text = label_text, fg = MEMA_BLACK, bg = MEMA_WHITE, font = ("Arial", 46, "bold"))
        self.sub_label.pack()

    def confirm_name(self, name: str) -> None:
        """
        Changes the label to the users name after they have said it to allow them to confirm it. Also changes the butttons
        """
        speak("You said, " + name + ", is that correct? Simply say Yes or No.")

        self.awaiting_confirmation = True
        self.name_buffer = name
        
        self.sub_label.configure(text = "Did you say " + name + "?")

        self.change_buttons_after_name()
        self.update()

    def change_buttons_after_name(self) -> None:
        """
        Changes the buttons after the user has input their name to allow them to confirm/unconfirm the name.
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Yes", "CONFIRM_YES")
        buttons[1] = ("No", "CONFIRM_NO")
        buttons[2] = (None, None)
        buttons[3] = (None, None)
        self.parent.set_input(buttons, False)

    def update_buttons(self, first_time = False) -> None:
        """
        Updates the displayed buttons to show back. The first_time parameter, which is default to be False is used to update the sub_label
        to say 'Sorry, please repeat your name'.
        """

        if(not first_time): self.sub_label.configure(text = "Sorry, please repeat your name")

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Back", "NEW_USR_BACK")
        buttons[1] = ("Toby", "toby")
        buttons[2] = (None, None)
        buttons[3] = (None, None)
        self.parent.set_input(buttons, False)

        self.update()

    def callback(self, callback_request: dict[str:str]) -> None:
        """
        Handles all callback, (e.g. button presses) Can either return to menu, go to the photo screen.
        """

        match (callback_request["content"]):
            case "NEW_USR_BACK":
                self.parent.reset_path()

            case "CONFIRM_YES":
                speak("Welcome to Memory Machine " + self.name_buffer)
                self.after(2500, self.parent.switch_content(content_new_user_photo, self.name_buffer))

            case "CONFIRM_NO":
                speak("Sorry, please could you repeat your name?")
                self.update_buttons()

            case _:
                self.confirm_name(callback_request["content"])

        





