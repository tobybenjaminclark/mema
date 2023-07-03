from tkinter import *
from mema_constants import *
from mema_speech_recognition import *
from mema_text_to_speech import *

class button_frame(Frame):

    def __init__(self, _parent, *args, **kwargs) -> None:

        # Superclass Initialization
        Frame.__init__(self, *args, **kwargs)

        self.parent = _parent
        self.io_handler = None
        self.buttons: list[Button] = []
        self.recognized_speech_string: str = ""
        self.io_handler_queue = None

        self.font = ("Arial Black", 32, "bold")

        # Setup grid weightings
        self.grid_columnconfigure(0, weight=1)
        for i in range(0, 4): self.grid_rowconfigure(i, weight=1)

        # Button Setup
        self.create_buttons()
        
    def create_buttons(self) -> None:

        # Creating & Placing Buttons
        self.buttons = [Button(self, text = str(i)) for i in range(0, 4)]
        for row, button in enumerate(self.buttons): button.grid(column = 0, row = row, sticky = NSEW)

        # Setting the text and callback of the buttons
        self.set_buttons([(str(i), str(i)) for i in range(0,4)])

    def set_buttons(self, button_callback: list[(str, str)], read = False) -> None:

        self.speech_commands = button_callback
        if(read): self.read_buttons(button_callback)

        for row, button_tuple in enumerate(button_callback):

            button_label: str
            callback_str: str
            button_label, callback_str = button_tuple

            if(button_label == None or callback_str == None):
                self.buttons[row].configure(command = None, text = None, state = DISABLED, fg = "grey", bg = "grey")
                continue

            # Setup callback command
            self.buttons[row].configure(command = lambda callback_str = callback_str : self.callback(callback_str))

            # Setup Label
            self.buttons[row].configure(text = button_label.upper(), font = self.font, state = ACTIVE)

            # Setup colour to maintain consistency
            self.buttons[row].configure(bg = MEMA_BUTTON_COLOURS[row])

        # Update Frame to reflect changes
        self.update()

    def read_buttons(self, button_callback: list[(str, str)]) -> None:

        phrases = ""
        print(button_callback)
        for row, button_tuple in enumerate(button_callback):
            phrase: str
            callback_str: str
            phrase, callback_str = button_tuple

            if(phrase == None or callback_str ==  None): continue

            
            phrase = phrase.lower()
            phrases = phrases + phrase
            phrases = phrases + ". "

        speak(phrases)
            
    def set_io_handler(self, io_handler):
        self.io_handler = io_handler

    def set_io_queue(self, io_queue: Queue):
        self.io_handler_queue = io_queue

    def callback(self, callback_str:str):
        self.io_handler_queue.put(callback_str)



