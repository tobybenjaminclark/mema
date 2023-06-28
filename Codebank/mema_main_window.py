from tkinter import *
from mema_constants import *

class main_window():

    def __init__(self) -> None:
        
        # Variables
        self.master: Tk

        # Setup
        self.initialize_tk_instance()

        self.master.mainloop()
    
    def initialize_tk_instance(self) -> None:
        
        self.master = Tk()
        self.master.geometry(MEMA_SCREEN_DIMENSIONS)

x = main_window()