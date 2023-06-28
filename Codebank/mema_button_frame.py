from tkinter import *

class button_frame(Frame):

    def __init__(self, _parent, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.parent = _parent

        # Setup grid weightings
        self.grid_columnconfigure(0, weight=1)
        for i in range(0, 4): self.grid_rowconfigure(i, weight=1)

        self.create_buttons()
        self.include_buttons()
        
    def create_buttons(self):
        self.buttons: list[Button]
        self.buttons = [Button(self, text = str(i), command = print("test")) for i in range(0, 4)]

    def include_buttons(self):
        for row, button in enumerate(self.buttons):
            button.grid(column = 0, row = row, sticky=NSEW)