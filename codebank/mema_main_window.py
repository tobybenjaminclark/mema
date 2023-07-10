# Generic MeMa Imports
from mema_constants import *
from mema_button_frame import *
from mema_content_frame import *
from mema_content_login import *
from mema_io_handler import *

# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *

class main_window(Tk):

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the window, sets up the queues and IO Handler. Calls the mainloop function.
        """

        # Call Superclass Constructor & setup
        Tk.__init__(self, *args, **kwargs)
        self.configure_tk_instance()

        # Handles Speech & Button presses
        self.io_queue: Queue
        self.io_queue = Queue()
        self.io_handler: io_handler = io_handler(self.button_frame, self.io_queue)

        self.switch_content(content_login)

        # Mainloop (Overwritten as a method)
        self.after(5, self.custom_mainloop)
        self.mainloop()

    def custom_mainloop(self) -> None:
        """
        Handles events and updates the screen (main loop)
        """
        if(self.io_queue.empty() is False):
            self.callback(self.io_queue.get())
        self.update()
        self.after(5, self.custom_mainloop)


    def reset_path(self) -> None:
        """
        Resets the current page to the content_login page (memory machine main page)
        """

        self.switch_content(content_login)

    def switch_content(self, new_content:type, *args) -> None:
        """
        Switches the content to the passed type, with the passed arguments
        """

        self.content_frame.grid_forget()
        del self.content_frame
        self.content_frame = new_content(self, *args)
        self.content_frame.grid(row=0,column=0,sticky=NSEW)

    def set_input(self, button_callback: list[(str, str)], read = False) -> None:
        """
        Sets the inputs for a page, this is usually called by the page to update the buttons. This method will
        then update the speech recognition thread.
        """

        # Proxys to self.button_frame.set_buttons()
        self.io_handler.set_input(button_callback, read)

    def configure_tk_instance(self) -> None:
        """
        Sets up the Tk instance, see mema_constants.py for preset options. Sets up the content frame and button frame.
        """

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

        self.content_frame: content_frame = content_frame(self)
        self.content_frame.grid(row=0, column=0, sticky=NSEW)

    def callback(self, callback_request: dict[str:str]) -> None:
        """
        Passes callback to the content frame. This is called from the mainloop() method, and is used to notify
        the content frame of events.
        """

        self.content_frame.callback(callback_request)

    def quit(self) -> None:
        """
        Destroys the frame and exits.
        """

        self.destroy()
        quit()

x = main_window()
quit()