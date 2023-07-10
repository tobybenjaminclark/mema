# Generic MeMa Imports
from mema_content_frame import *
from mema_content_memory_create_home import *
from mema_text_to_speech import *
from mema_data_access import *
from mema_constants import *

# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *

class content_memory_create_name(content_frame):

    def __init__(self, parent, user_id: str, *args, **kwargs)-> None:
        """
        Initializes the GUI and frame variables (awaiting_confirmation & name_buffer)
        """

        content_frame.__init__(self, *args, **kwargs)

        # Configure parent
        self.parent = parent
        self.user_id = user_id

        # Is the user confirming their name?
        self.awaiting_confirmation: bool
        self.awaiting_confirmation = False

        # Buffer to store the spoken name in
        self.memory_name_buffer: str
        self.memory_name_buffer = ""

        # Update buttons and setup the GUI
        # True is passed to update_buttons here as it represents the first time the buttons are 
        # created. Look at the update_buttons() method for more information.
        self.setup_gui()
        self.update_buttons(True)
        
        speak("What would you like to call this memory?")

    def setup_gui(self) -> None:
        """
        Initializes this frames GUI, creating the introduction labels.
        """
        self.setup_sub_label()
        

    def setup_sub_label(self, label_text:str = "What would you like to call this memory?") -> None:
        """
        Creates a sub label, asking the user what to call this memory
        """
        self.sub_label: Label
        self.sub_label = Label(self, text = label_text, fg = MEMA_BLACK, bg = MEMA_WHITE, font = ("Arial", 36, "bold"))
        self.sub_label.pack()

    def confirm_name(self, name: str) -> None:
        """
        Changes the label to the users name after they have said it to allow them to confirm it. Also changes the butttons
        """
        speak("You said, " + name + ", is that correct? Simply say Yes or No.")

        self.awaiting_confirmation = True
        self.memory_name_buffer = name
        
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
        buttons[2] = MEMA_EMPTY_BUTTON
        buttons[3] = MEMA_EMPTY_BUTTON
        self.parent.set_input(buttons, False)

    def update_buttons(self, first_time = False) -> None:
        """
        Updates the displayed buttons to show back. The first_time parameter, which is default to be False is used to update the sub_label
        to say 'Sorry, please repeat your name'.
        """

        if(not first_time): self.sub_label.configure(text = "Sorry, please repeat what\nyou would like this memory to be called")

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Back", "NEW_USR_BACK")
        buttons[1] = ("Toby", "toby")
        buttons[2] = MEMA_EMPTY_BUTTON
        buttons[3] = MEMA_EMPTY_BUTTON
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
                print("MEMORY!")
                mempath = create_memoryspace(self.user_id, self.memory_name_buffer)
                self.parent.switch_content(content_memory_create_home, mempath)

            case "CONFIRM_NO":
                self.memory_name_buffer = ""
                self.update_buttons()

            case _:
                self.confirm_name(callback_request["content"])