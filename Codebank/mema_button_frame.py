from tkinter import *
from mema_constants import *
from mema_speech_recognition import *

class button_frame(Frame):

    def __init__(self, _parent, *args, **kwargs) -> None:

        # Superclass Initialization
        Frame.__init__(self, *args, **kwargs)
        self.parent = _parent
        self.buttons: list[Button] = []
        self.recognized_speech_string: str = ""

        # Setup grid weightings
        self.grid_columnconfigure(0, weight=1)
        for i in range(0, 4): self.grid_rowconfigure(i, weight=1)

        # Button Setup
        self.create_buttons()

        # Start Listening
        self.listen(None)
        
    def create_buttons(self) -> None:

        # Creating & Placing Buttons
        self.buttons = [Button(self, text = str(i)) for i in range(0, 4)]
        for row, button in enumerate(self.buttons): button.grid(column = 0, row = row, sticky = NSEW)

        # Setting the text and callback of the buttons
        self.set_buttons([(str(i), str(i)) for i in range(0,4)])

    def set_buttons(self, button_callback: list[(str, str)]) -> None:

        for row, button_tuple in enumerate(button_callback):

            button_label: str
            callback_str: str
            button_label, callback_str = button_tuple

            # Setup callback command
            self.buttons[row].configure(command = lambda callback_str = callback_str : self.callback(callback_str))

            # Setup Label
            self.buttons[row].configure(text = button_label)

            # Setup colour to maintain consistency
            self.buttons[row].configure(bg = MEMA_BUTTON_COLOURS[row])

        # Update Frame to reflect changes
        self.update()

    def callback(self, callback_str:str):
        self.parent.callback(callback_str)

    def listen(self, recognized_string):
        print("\n\n\n", recognized_string, "\n\n\n")
        listen(self.listen)

