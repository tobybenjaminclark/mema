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
        self.update_buttons()

    def update_label(self):

        self.text.configure(text = self.label_content)

    def setup_gui(self):

        self.header = Label(self, text = "Say text to create a label")
        self.header.pack(pady = 20)

        self.text = Label(self, text = self.label_content)
        self.text.pack()

    def update_buttons(self):

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Record Label", "START_RECORDING_LABEL")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def update_show_recording(self):

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Stop Recording Label", "STOP_RECORDING_LABEL")
        buttons[1] = (None, None)
        buttons[2] = (None, None)
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False)       

    def confirmation_buttons(self):

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("Keep Label", "LABEL_WRITE")
        buttons[1] = ("Retake Label", "LABEL_RETAKE")
        buttons[2] = (None, None)
        buttons[3] = ("Exit", "HOME_EXIT")
        self.parent.set_input(buttons, False) 

    def callback(self, callback_request: dict) -> None:
        
        match callback_request["content"]:

            case "START_RECORDING_LABEL":
                self.update_show_recording()
                self.recording_label = True

            case "STOP_RECORDING_LABEL":
                self.confirmation_buttons()
                self.recording_label = False

            case "HOME_EXIT":
                self.parent.switch_content(self.return_obj, self.memoryspace_path)

            case "LABEL_WRITE":
                f = open(self.memoryspace_path + "/" + str(self.frame) + "_label.txt", "w")
                f.write(self.label_content)
                f.close()
                self.parent.switch_content(self.return_obj, self.memoryspace_path)

            case "LABEL_RETAKE":
                self.update_buttons()
                self.label_content = ""
                self.update_label()

            case _:
                if self.recording_label:
                    spoken_content = callback_request["content"]
                    self.label_content += spoken_content
                    self.update_label()
