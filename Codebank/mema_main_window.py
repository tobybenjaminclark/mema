from tkinter import *
from mema_constants import *
from mema_button_frame import *
from mema_content_frame import *

class main_window(Tk):

    def __init__(self, *args, **kwargs) -> None:
        
        # Call Superclass Constructor & setup
        Tk.__init__(self, *args, **kwargs)
        self.configure_tk_instance()

        # Mainloop
        self.mainloop()
    
    def configure_tk_instance(self) -> None:
    
        # Sets the window geometry to the mema3 physical screen
        self.geometry(MEMA_SCREEN_DIMENSIONS)

        # Sets the window name
        self.title("MeMa 3.1")

        # Configures the row and column weightings
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 3)
        self.grid_columnconfigure(1, weight = 1)

        # Setting up content & button frames
        self.content_frame: content_frame = content_frame(self)
        self.content_frame.grid(row=0, column=0, sticky=NSEW)

        self.button_frame: button_frame = button_frame(self)
        self.button_frame.grid(row=0,column=1, sticky=NSEW)

x = main_window()