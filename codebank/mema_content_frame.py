from tkinter import *
from mema_constants import *

class content_frame(Frame):

    def __init__(self, *args, **kwargs) -> None:
        """
        Initization method calls the tk.Frame constructor
        """
        Frame.__init__(self, *args, **kwargs, bg = "white")

    def callback(self, callback_request: dict[str:str]):
        """
        Callback method on the Superclass does nothing, just to prevent errors. This should be implemented in the subclass.
        """

        pass

        