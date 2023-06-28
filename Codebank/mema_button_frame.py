from tkinter import *

class button_frame(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.create_buttons()
        self.include_buttons()
        
    def create_buttons(self):
        self.buttons: list[Button]
        self.buttons = [Button(self, text = str(i)) for i in range(0, 4)]

    def include_buttons(self):
        for button in self.buttons:
            button.pack()