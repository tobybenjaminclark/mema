from mema_content_frame import *
from mema_speech_recognition import *

class content_memory_create_label(content_frame):

    def __init__(self, parent, memoryspace_path: str, _return_page, _frame_index: int, *args, **kwargs) -> None:
        """
        Initializes the page, creates relevant variables so the class knows whether it should be recording or not, sets up the GUI
        and renders it to the screen. Event-driven callback function used to control flow.
        """

        # Call superclass constructor
        content_frame.__init__(self, *args, **kwargs)

        # Store the reference to the parent class
        self.parent = parent

        # Store the path to the memory space
        # Should be something like: databank/userbank_id/memoryspace_name
        self.memoryspace_path: str
        self.memoryspace_path = memoryspace_path

        # Store the return object
        self.return_page = _return_page

        # Store the frame number
        self.frame_index: int
        self.frame_index = _frame_index

        # Initialize the variable for recording label status
        self.recording_label: bool
        self.recording_label = False

        # Initialize the label content
        self.label_content: str
        self.label_content = ""

        # Setup the graphical user interface
        self.setup_gui()

        # Display the initial buttons
        self.display_initial_buttons()

    def update_label_text(self):
        """
        Updates the displayed label text to show the newly updated text
        """

        self.text.configure(text = self.label_content)

    def setup_gui(self):
        """
        Sets up the GUI Widgets on the screen. Initializes a header and a label to show the spoken text
        """

        self.header = Label(self, text = "Say text to create a label")
        self.header.pack(pady = 20)

        self.text = Label(self, text = self.label_content)
        self.text.pack()

    def display_initial_buttons(self):
        """
        Display the initial set of buttons.
        
        This function sets up and displays the initial buttons on the user interface. The buttons are represented as a list of
        tuples, where each tuple consists of a button label and a corresponding action identifier. The buttons in this function
        are used for starting the recording label and exiting the program.
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Record Label", "START_RECORDING_LABEL")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def display_secondary_buttons(self):
        """
        Display the secondary set of buttons.
        
        This function sets up and displays the secondary buttons on the user interface. The buttons are represented as a list of
        tuples, where each tuple consists of a button label and a corresponding action identifier. The buttons in this function
        are used for stopping the recording label and exiting the program.
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Stop Recording Label", "STOP_RECORDING_LABEL")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False)       

    def display_confirmaiton_buttons(self):
        """
        Display the confirmation set of buttons.
        
        This function sets up and displays the confirmation buttons on the user interface. The buttons are represented as a list
        of tuples, where each tuple consists of a button label and a corresponding action identifier. The buttons in this
        function are used for confirming or retaking the label, as well as exiting the program.
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Keep Label", "LABEL_WRITE")
        buttons[1] = ("Retake Label", "LABEL_RETAKE")
        buttons[2] = (None, None)
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False) 

    def callback(self, callback_request: dict) -> None:
        """
        Takes a callback request from a button press or speech and maps it to the appropriate program response. Used to record
        what the user is saying, to put into the notes. Can cause the return to the page before.
        """

        match callback_request["content"]:

            # User chose to start recording a label
            # Display the secondary buttons for label recording
            # Set recording_label to True to indicate label recording is in progress
            case "START_RECORDING_LABEL":
                self.display_secondary_buttons()
                self.recording_label = True

            # User chose to stop recording a label
            # Display the confirmation buttons for label confirmation
            # Set recording_label to False to indicate label recording is stopped
            case "STOP_RECORDING_LABEL":
                self.display_confirmation_buttons()
                self.recording_label = False

            # User chose to exit from the current content frame
            # Switch the content to the return page
            case "HOME_EXIT":
                self.parent.switch_content(self.return_page, self.memoryspace_path)

            # User chose to keep the recorded label
            # Write the label content to a file in the memoryspace
            # Switch the content to the return page
            case "LABEL_WRITE":
                file_path = self.memoryspace_path + "/" + str(self.frame_index) + "_label.txt"
                with open(file_path, "w") as file:
                    file.write(self.label_content)
                self.parent.switch_content(self.return_page, self.memoryspace_path)

            # User chose to retake the label
            # Display the initial buttons for label recording
            # Clear the label content
            # Update the label text
            case "LABEL_RETAKE":
                self.display_initial_buttons()
                self.label_content = ""
                self.update_label_text()

            # If none of the above cases match and recording_label is True,
            # it means the user is recording a label and the spoken content
            # should be appended to the existing label content
            # Append the spoken content to the label
            # Update the label text
            case _:
                if self.recording_label:
                    spoken_content = callback_request["content"]
                    self.label_content += spoken_content
                    self.update_label_text()