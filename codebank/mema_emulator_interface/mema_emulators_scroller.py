
# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *

class emulator_scroller():

    def __init__(self) -> None:
        
        self.master: Tk
        self.master = Tk()

        self.left_button: Button
        self.left_button = Button(self.master)
        self.left_button.pack(side = LEFT)

        self.canvas: Canvas
        self.canvas = Canvas(self.master)
        self.canvas.pack(side = LEFT)

        self.right_button: Button
        self.right_button = Button(self.master)
        self.right_button.pack(side = LEFT)

        self.master.mainloop()

if __name__ == "__main__":
    test_scroller = emulator_scroller()