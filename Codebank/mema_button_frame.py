from tkinter import *

class button_frame(Frame):

    def __init__(self, _parent, *args, **kwargs) -> None:

        # Superclass Initialization
        Frame.__init__(self, *args, **kwargs)
        self.parent = _parent
        self.buttons: list[Button]

        # Setup grid weightings
        self.grid_columnconfigure(0, weight=1)
        for i in range(0, 4): self.grid_rowconfigure(i, weight=1)

        # Button Setup
        self.create_buttons()
        
    def create_buttons(self) -> None:

        # Creating Buttons
        self.buttons = [(Button(self, text = str(i)), str(i)) for i in range(0, 4)]
        self.set_buttons(self.buttons)

    def set_buttons(self, button_callback: list[(Button, str)]) -> None:

        for row, button_tuple in enumerate(button_callback):

            button: Button
            callback: str
            button, callback = button_tuple

            button.configure(command = lambda callback_str = callback : self.callback(callback_str))
            button.grid(column = 0, row = row, sticky = NSEW)
            self.buttons[row] = button

    def callback(self, callback_str:str):

        print(callback_str)
