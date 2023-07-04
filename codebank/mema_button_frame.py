from tkinter import *
from mema_constants import *
from mema_speech_recognition import *
from mema_text_to_speech import *

class button_frame(Frame):

    def __init__(self, _parent, *args, **kwargs) -> None:
        """
        Calls the tk.Frame constructor (superclass) and sets up the IO Handler and Grid Weightings. After this
        the constructor will create the buttons using the create_buttons() method.
        """

        # Superclass Initialization
        Frame.__init__(self, bg = MEMA_WHITE, *args, **kwargs)

        # Store the parent widget
        self.parent = _parent

        # Initialize instance variables
        self.io_handler = None
        self.buttons: list[Button] = []
        self.recognized_speech_string: str = ""
        self.io_handler_queue = None

        # Set the font for the buttons
        # Check mema_constants.py to change this
        self.font = MEMA_BUTTON_FONT

        # Setup grid weightings
        self.grid_columnconfigure(0, weight=1)
        for i in range(0, 4):
            self.grid_rowconfigure(i, weight=1)

        # Button Setup
        self.create_buttons()
        
    def create_buttons(self) -> None:
        """
        Generate the buttons and place them to the screen using the grid method
        """

        # Creating & Placing Buttons
        self.buttons = [Button(self, text = str(i)) for i in range(0, 4)]
        for row, button in enumerate(self.buttons): button.grid(column = 0, row = row, sticky = NSEW, padx = 10, pady = 10)

        # Setting the text and callback of the buttons
        self.set_buttons([(str(i), str(i)) for i in range(0,4)])

    def set_buttons(self, button_callback: list[tuple[str, str]], read=False) -> None:
        """
        Updates the buttons to display the passed strings, updates the voice command set automaticaly so that if the user
        speaks any of the button labels, the appropriate call will automatically incur. Can also set the command to read
        the new buttons aloud using the TTS Thread.

        Args:
            button_callback (List[Tuple[str, str]]): A list of button labels and corresponding callback strings.
            read (bool, optional): Indicates whether to read the buttons. Defaults to False.
        """
        self.speech_commands = button_callback

        # If requested, read the buttons
        if read:
            self.read_buttons(button_callback)

        for row, (button_label, callback_str) in enumerate(button_callback):

            if button_label is None or callback_str is None:
                # Disable and style the button if either label or callback is None
                self.buttons[row].configure(
                    command=None,
                    text="",
                    state=DISABLED,
                    borderwidth=5,
                    fg="grey",
                    bg="grey"
                )

            else:
                # Configure the button with the callback, label, font, and style
                self.buttons[row].configure(
                    command=lambda callback_str=callback_str: self.callback(callback_str),
                    text=button_label.upper(),
                    font=self.font,
                    state=NORMAL,
                    bg= MEMA_BUTTON_COLOURS[row],
                    fg= MEMA_BLACK,
                    borderwidth=5
                )

        # Update the frame to reflect changes
        self.update()
        
        return None
    
    def read_buttons(self, button_callback: list[tuple[str, str]]) -> None:
        """
        Generates a string from the button labels to tell the TTS thread to speak, essentially reads out what is
        written on the buttons.

        Args:
            button_callback (list[tuple[str, str]]): List of button phrases and their respective callback strings.
        """
        phrases = []
        for phrase, callback_str in button_callback:
            if phrase is not None and callback_str is not None:
                phrases.append(phrase.lower())
        
        speak('. '.join(phrases))
            
    def set_io_handler(self, io_handler):
        """
        Sets the IO Handler Object to communicate button presses
        """
        self.io_handler = io_handler
        return None

    def set_io_queue(self, io_queue: Queue):
        """
        Sets the IO Handler Queue to notify when a button is pressed
        """
        self.io_handler_queue = io_queue
        return None

    def callback(self, callback_str:str):
        """
        This is called when a button is pressed, it enqueues the button-press to be handled by hte
        IO Handler Object
        """
        self.io_handler_queue.put(callback_str)
        return None



