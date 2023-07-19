# Generic MeMa Imports
from mema_constants import *

# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *

class content_frame(Frame):

    def __init__(self, *args, **kwargs) -> None:
        """
        Initization method calls the tk.Frame constructor
        """
        Frame.__init__(self, *args, **kwargs, bg = MEMA_WHITE)

    def callback(self, callback_request: dict[str:str]):
        """
        Callback method on the Superclass does nothing, just to prevent errors. This should be implemented in the subclass.
        """
        pass

        