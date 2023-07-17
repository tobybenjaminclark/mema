from tkinter import *
from tkinter.constants import BOTH, YES
from typing import Union

class emulator_buttons():
    """
    The `emulator_buttons` class creates a Tkinter application that displays a set of scalable buttons as circles on a canvas.
    Each button can be clicked, and the button index will be printed to the console.

    Attributes:
        master (Tk): The Tkinter root window object.
        canvas (Canvas): The Tkinter canvas object where the buttons are displayed.

    Methods:
        __init__(): Initializes the `emulator_buttons` object and creates the Tkinter application.
        callback(event, button_index): Prints the button index when a button is clicked.
        create_buttons(): Creates the scalable buttons and binds them to the callback function.
        resize_canvas(event): Callback function to regenerate the canvas when the window is resized.
    """

    def __init__(self, show_debug_messages: bool = False) -> None:
        """
        Initializes the `emulator_buttons` object and creates the Tkinter application.
        """

        self.show_debug_messages: bool
        self.show_debug_messages = show_debug_messages

        self.master: Tk = Tk()
        self.master.title("MeMa Buttons")
        self.master.geometry("200x800")

        window_width: int
        window_width = self.master.winfo_width()

        window_height: int
        window_height = self.master.winfo_height()

        self.canvas: Canvas
        self.canvas = Canvas(self.master, height=window_height, width=window_width, bg="aqua")

        self.create_buttons()
        self.master.bind("<Configure>", self.resize_canvas)
        self.master.mainloop()

    def callback(self, event: Union[Event, int], button_index: int) -> None:
        """
        Prints the button index when a button is clicked.

        Parameters:
            event (Tk.Event): The Tkinter event object representing the button click event.
            button_index (int): The index of the button that was clicked.
        """

        # Print debug message (if relevant)
        if(self.show_debug_messages): print(f"mema_emulator_buttons: button ({button_index}) was pressed")

    def create_buttons(self) -> None:
        """
        Creates the scalable buttons and binds them to the callback function.
        """

        # Current width of the window
        window_width: int
        window_width = self.master.winfo_width()
        
        # Current height of the window
        window_height: int
        window_height = self.master.winfo_height()

        # Number of buttons
        number_of_buttons: int
        number_of_buttons = 4

        # Calculating the height of each button
        button_height: int
        button_height = window_height // number_of_buttons

        # Padding from the sides (adjustable)
        pad: int
        pad = 15

        # Creating the buttons
        for button_index in range(number_of_buttons):

            position: int
            position = button_index * button_height

            # Creating the oval (represented by an integer ID)
            oval: int
            oval = self.canvas.create_oval(pad, position + pad, window_width - pad, position + button_height - pad, fill="light grey")

            # Tag each button so it has a callback when clicked
            self.canvas.tag_bind(oval, "<ButtonPress-1>", lambda event, x = button_index: self.callback(event, x))

        # Add canvas back to the window.
        self.canvas.pack(fill=BOTH, expand=YES)

    def resize_canvas(self, event: Event) -> None:
        """
        Callback function to regenerate the canvas when the window is resized. This is bound in the emulator_buttons.__init__() method,
        to the <<Configure>> event, which is called when the window is resized.

        Parameters:
            event (Tk.Event): The Tkinter event object representing the window resize event. We use this to get
            the new width and height values of the window.
        """
        width: int = event.width
        height: int = event.height
        
        # Reset canvas and re-render buttons.
        self.canvas.config(width=width, height=height)
        self.canvas.delete("all")
        self.create_buttons()

if __name__ == "__main__":
    test = emulator_buttons(True)