from tkinter import *
from mema_constants import *

class content_frame(Frame):

    def __init__(self, *args, **kwargs) -> None:

        Frame.__init__(self, *args, **kwargs, bg = "light blue")

    def callback(self, callback_request: dict[str:str]):
        pass

        