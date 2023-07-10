from mema_content_frame import *
from mema_speech_recognition import *

class content_memory_create_label(content_frame):

    def __init__(self, parent, memoryspace_path: str, return_obj, frame: int, *args, **kwargs) -> None:

        content_frame.__init__(self, *args, **kwargs)
        self.parent = parent
        self.memoryspace_path = memoryspace_path
        self.return_obj = return_obj
        self.frame = frame
        self.recording_label = False
        self.label_content = ""

        self.setup_gui()
        self.display_initial_buttons()

    def update_label_text(self):

        self.text.configure(text = self.label_content)

    def setup_gui(self):

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
        
        match callback_request["content"]:

            case "START_RECORDING_LABEL":
                self.display_secondary_buttons()
                self.recording_label = True

            case "STOP_RECORDING_LABEL":
                self.display_confirmaiton_buttons()
                self.recording_label = False

            case "HOME_EXIT":
                self.parent.switch_content(self.return_obj, self.memoryspace_path)

            case "LABEL_WRITE":
                f = open(self.memoryspace_path + "/" + str(self.frame) + "_label.txt", "w")
                f.write(self.label_content)
                f.close()
                self.parent.switch_content(self.return_obj, self.memoryspace_path)

            case "LABEL_RETAKE":
                self.display_initial_buttons()
                self.label_content = ""
                self.update_label_text()

            case _:
                if self.recording_label:
                    spoken_content = callback_request["content"]
                    self.label_content += spoken_content
                    self.update_label_text()
