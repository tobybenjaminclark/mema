
# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *

# Math Function Library
# We're using trigonometry and radian conversion to calculate the point on the circle
# the dial is facing towards. These functions are included in the math library.
import math

class emulator_scroller():

    def __init__(self) -> None:
        
        self.master: Tk
        self.master = Tk()

        self.radius: int
        self.radius = 190 // 2
        
        self.circle_x_position: int
        self.circle_x_position = 100
        
        self.circle_y_position: int
        self.circle_y_position = 100

        self.current_degree: int
        self.current_degree = 0

        self.moving: bool
        self.moving = False

        self.canvas: Canvas
        self.canvas = Canvas(self.master, width = 200, height = 200, bg = "white")
        self.canvas.create_oval(10, 10, 190, 190, fill = "light grey")

        self.dial: int
        bx, by = self.get_point_on_circle()
        self.dial = self.canvas.create_oval(bx-5,by-5,bx+5,by+5,fill="red", tags="dial")

        self.left_button: Button
        self.left_button = Button(self.master)
        self.left_button.bind('<ButtonPress-1>',lambda event: self.start_pointer(-1))
        self.left_button.bind('<ButtonRelease-1>', lambda event: self.stop_moving())
        self.left_button.pack(side = LEFT)

        self.canvas.pack(side = LEFT)

        self.right_button: Button
        self.right_button = Button(self.master)
        self.right_button.bind('<ButtonPress-1>',lambda event: self.start_pointer(1))
        self.right_button.bind('<ButtonRelease-1>', lambda event: self.stop_moving())
        self.right_button.pack(side = LEFT)

        self.master.mainloop()

    def start_pointer(self, amount) -> None:
        self.moving = True
        self.move_pointer(amount)

    def stop_moving(self) -> None:
        self.moving = False

    def move_pointer(self, amount) -> None:
        while self.moving:
            self.current_degree += amount
            bx, by = self.get_point_on_circle()
            print(bx, by)
            self.canvas.moveto("dial", bx-5, by-5)
            self.master.update()
            self.master.after(10)


    def get_point_on_circle(self) -> None:
        # Convert the degree to radiansself.left_button: Button
        radian = math.radians(self.current_degree)
        
        # Calculate the coordinates of the point on the perimeter
        point_x = self.circle_x_position + self.radius * math.cos(radian)
        point_y = self.circle_y_position + self.radius * math.sin(radian)
    
        return point_x, point_y

if __name__ == "__main__":
    test_scroller = emulator_scroller()