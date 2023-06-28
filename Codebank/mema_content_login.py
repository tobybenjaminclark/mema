from tkinter import *
from mema_content_frame import *

class content_login(content_frame):

    def __init__(self, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        self.label = Label(self, text = "LOGIN")
        self.label.grid(row=0, column=0)
        