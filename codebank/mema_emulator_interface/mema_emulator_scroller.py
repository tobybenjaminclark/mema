
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
    """
    A class to create a scroller emulator using Tkinter. Rotates a dial in the centre of the window
    using 2 buttons either side. Draws circle at the correct point on the radius representing the direction it is pointing.
    When the button is pressed, it starts a loop increasing the degrees, when the button is released it is stopped,
    that is why we are using .bind() instead of the passed kwarg 'command =', as we need to call separate functions
    dependent on whether the button was pressed or released.
    """

    # Constants for the minimum and maximum degrees to limit the dial rotation.
    MIN_DEGREE = 10
    MAX_DEGREE = 350

    # Constants for updating the dial position every 10 milliseconds.
    UPDATE_DELAY_MS = 10

    def __init__(self) -> None:
        """
        Initializes the scroller emulator GUI and runs the main event loop.

        The constructor sets up the main Tkinter window and initializes
        various attributes used to control the scroller emulator.
        """

        # The main Tkinter window.
        self.master: Tk
        self.master = Tk()
        self.master.title("Scroller Emulator")
        self.master.configure(bg="white")

        # The radius of the dial that is drawn on the screen (in pixels).
        self.radius: int
        self.radius = 190 // 2

        # The x-position of the center of the circle (dial).
        self.circle_x_position: int
        self.circle_x_position = 100

        # The y-position of the center of the circle (dial).
        self.circle_y_position: int
        self.circle_y_position = 100

        # The current degree representing the rotation of the dial.
        self.current_degree: int
        self.current_degree = 0

        # A flag to track if the dial is currently being moved.
        self.moving: bool
        self.moving = False

        self.setup_gui()

        self.master.mainloop()

    def setup_gui(self) -> None:
        """
        Sets up the GUI components for the scroller emulator.

        This method creates the canvas, dial, and buttons for the scroller emulator
        by calling other helper methods: create_canvas(), create_dial(), and create_buttons().
        """

        self.create_canvas()
        self.create_dial()
        self.create_buttons()

    def create_canvas(self) -> None:
        """
        Creates the canvas and adds oval shapes to it.

        This method initializes the canvas widget and adds three oval shapes to it
        representing the outer ring, the black dial, and the inner ring of the scroller.
        """

        # The canvas where the dial and buttons will be drawn.
        self.canvas: Canvas
        self.canvas = Canvas(self.master, width=200, height=200, bg="white")
        self.canvas.create_oval(10, 10, 190, 190, fill="light grey")
        self.canvas.create_oval(30, 30, 170, 170, fill="black")
        self.canvas.create_oval(32, 32, 168, 168, fill="light grey")
        

    def create_dial(self) -> None:
        """
        Creates the dial on the canvas representing the current degree.

        This method calculates the position of the dial on the canvas based on the current degree
        and draws a small black oval representing the dial's position using the Canvas.create_oval() method.
        """

        bx, by = self.get_point_on_circle()
        # The dial shape drawn on the canvas to represent the current degree.
        self.dial: int
        self.dial = self.canvas.create_oval(bx - 5, by - 5, bx + 5, by + 5, fill="black", tags="dial")

    def create_buttons(self) -> None:
        """
        Creates the left and right buttons to rotate the dial.

        This method initializes two buttons, one for rotating the dial left (counterclockwise) and
        the other for rotating it right (clockwise). It binds button events to respective methods:
        start_pointer() and stop_moving() for rotation control.
        """

        # The button to rotate the dial left (counterclockwise).
        self.left_button: Button
        self.left_button = Button(self.master, text="<<<\nLeft", bg="white", font=("Arial Black", 16, "bold"))
        self.left_button.bind('<ButtonPress-1>', lambda event: self.start_pointer(-1))
        self.left_button.bind('<ButtonRelease-1>', lambda event: self.stop_moving())
        self.left_button.pack(side=LEFT, fill="both")

        # Packs the canvas (pre-requisite)
        try: self.canvas.pack(side=LEFT)
        except: print("mema_emulator_scroller: canvas was not created")

        # The button to rotate the dial right (clockwise).
        self.right_button: Button
        self.right_button = Button(self.master, text=">>>\nRight", bg="white", font=("Arial Black", 16, "bold"))
        self.right_button.bind('<ButtonPress-1>', lambda event: self.start_pointer(1))
        self.right_button.bind('<ButtonRelease-1>', lambda event: self.stop_moving())
        self.right_button.pack(side=LEFT, fill="both")

    def start_pointer(self, amount: int) -> None:
        """
        Starts rotating the dial continuously in the given direction.

        Args:
            amount (int): The direction and speed of rotation (-1 for left, 1 for right).

        This method sets the `moving` flag to True to enable continuous rotation of the dial
        in the specified direction. It then calls the `move_pointer()` method to perform the rotation.
        """

        self.moving = True
        self.move_pointer(amount)

    def stop_moving(self) -> None:
        """
        Stops rotating the dial.

        This method sets the `moving` flag to False, stopping the continuous rotation of the dial.
        """

        self.moving = False

    def move_pointer(self, amount: 1|-1) -> None:
        """
        Rotates the dial continuously in the given direction until movement is stopped.

        Args:
            amount (int): The direction and speed of rotation (-1 for left, 1 for right).

        This method continuously rotates the dial in the specified direction by updating the
        `current_degree` attribute and redrawing the dial on the canvas using the updated position.
        It does this until the `moving` flag is set to False (when the user releases the rotation button).
        """
        while self.moving:
            
            # Update the current degree based on the rotation direction and speed.
            self.current_degree += amount

            # Ensure the degree stays within the allowed range.
            self.current_degree = max(self.MIN_DEGREE, min(self.current_degree, self.MAX_DEGREE))

            # Calculate the new position of the dial on the canvas.
            bx, by = self.get_point_on_circle()

            # Print the calculated position and current degree for debugging purposes.
            print(f"Position: ({bx}, {by}) | Degree: {self.current_degree}")

            # Move the dial on the canvas to the new position.
            self.canvas.moveto("dial", bx - 5, by - 5)

            # Update the Tkinter window to reflect the changes.
            self.master.update()

            # Add a small delay before the next update to control the rotation speed.
            self.master.after(self.UPDATE_DELAY_MS)

    def get_point_on_circle(self) -> tuple[float, float]:
        """
        Calculates the coordinates of a point on the perimeter of the circle based on the current degree.

        Returns:
            Tuple[float, float]: The x and y coordinates of the point on the circle.

        This method converts the current degree to radians and uses trigonometry to calculate
        the coordinates of a point on the perimeter of the circle (dial) based on the degree value.
        The calculated coordinates are then returned as a tuple (x, y).
        """

        # Convert the degree to radians
        radian = math.radians(self.current_degree + 90)

        # Calculate the coordinates of the point on the perimeter
        point_x = self.circle_x_position + self.radius * math.cos(radian)
        point_y = self.circle_y_position + self.radius * math.sin(radian)

        return point_x, point_y

if __name__ == "__main__":
    test_scroller = emulator_scroller()