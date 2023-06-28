from tkinter import *
from mema_constants import *
from mema_button_frame import *

class main_window(Tk):

    def __init__(self, *args, **kwargs) -> None:
        
        # Call Superclass Constructor & setup
        Tk.__init__(self, *args, **kwargs)
        self.configure_tk_instance()

        # Add in frame
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        x: button_frame = button_frame(self, height = 800, width = 300)
        x.grid(row=0,column=0, sticky=NSEW)

        # Mainloop
        self.mainloop()
    
    def configure_tk_instance(self) -> None:
        
        # Sets the window geometry to the mema3 physical screen
        self.geometry(MEMA_SCREEN_DIMENSIONS)

x = main_window()