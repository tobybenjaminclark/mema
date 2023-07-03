from tkinter import *
from mema_constants import *
from mema_button_frame import *
from mema_content_frame import *
from mema_content_login import *
from mema_io_handler import *

class main_window(Tk):

    def __init__(self, *args, **kwargs) -> None:
        
        # Call Superclass Constructor & setup
        Tk.__init__(self, *args, **kwargs)
        self.configure_tk_instance()

        # Handles Speech & Button presses
        self.io_queue: Queue
        self.io_queue = Queue()
        self.io_handler: io_handler = io_handler(self.button_frame, self.io_queue)

        # Mainloop
        while True:
            if(self.io_queue.empty() is False):
                self.callback(self.io_queue.get()["content"])
            self.update()

    def set_buttons(self, button_callback: list[(str, str)], read = False) -> None:

        # Proxys to self.button_frame.set_buttons()
        self.button_frame.set_buttons(button_callback, read)

    def configure_tk_instance(self) -> None:
    
        # Sets the window geometry to the mema3 physical screen
        self.geometry(MEMA_SCREEN_DIMENSIONS)

        # Sets the window name
        self.title(MEMA_WINDOW_NAME)

        # Configures the row and column weightings
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = MEMA_CONTENT_WIDTH)
        self.grid_columnconfigure(1, weight = MEMA_BUTTON_WIDTH)

        # Setting up content & button frames
        # Note: Always setup the button frame first, as generally the content frame will communicate to
        # set the currently displayed buttons.
        self.button_frame: button_frame = button_frame(self)
        self.button_frame.grid(row=0,column=1, sticky=NSEW)

        self.content_frame: content_frame = content_login(self)
        self.content_frame.grid(row=0, column=0, sticky=NSEW)

    def callback(self, callback_str: str) -> None:
        self.content_frame.callback(callback_str)

x = main_window()