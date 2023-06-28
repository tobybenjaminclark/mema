from tkinter import *

class button_frame(Frame):

    def __init__(self, _parent, *args, **kwargs):

        # Superclass Initialization
        Frame.__init__(self, *args, **kwargs)
        self.parent = _parent

        # Setup grid weightings
        self.grid_columnconfigure(0, weight=1)
        for i in range(0, 4): self.grid_rowconfigure(i, weight=1)

        # Button Setup
        self.create_buttons()
        self.grid_buttons()
        
    def create_buttons(self) -> None:

        # Creating Buttons
        self.buttons: list[Button]
        self.buttons = [Button(self, text = str(i), command = lambda i=i: print(f"test %d", i)) for i in range(0, 4)]

    def grid_buttons(self) -> None:

        # Adding buttons to the grid
        for row, button in enumerate(self.buttons):
            button.grid(column = 0, row = row, sticky=NSEW)