from queue import Queue
from threading import Thread

from mema_button_frame import *
from mema_speech_recognition import *

class mema_io_handler():

    def __init__(self, button_frame: button_frame) -> None:
        
        self.button_frame = button_frame

        # Create Queue
        self.input_queue: Queue
        self.input_queue = Queue()

        # Speech Recognition Thread
        self.sr_input_queue: Queue
        self.sr_input_queue = Queue()

        self.button_input_queue: Queue
        self.button_input_queue = Queue()

        self.stop_speech_recognition_thread = False

    def create_speech_recognition_thread(self) -> None:
        
        # Create the speech recognition thread
        self.stop_speech_recognition_thread = False
        listen(self.sr_input_queue, lambda: self.stop_speech_recognition_thread)
        
    def close_speech_recognition_thread(self) -> None:
        
        # Stops speech recognition thread
        self.stop_speech_recognition_thread = True

    def create_button_frame(self) -> None:
        self.button_frame.set_io_handler(self)
        self.button_frame.set_io_queue(self.button_input_queue)

    def set_buttons(self, button_callback: list[(str, str)], read = False) -> None:
        self.button_frame.set_buttons(button_callback, read)

m = mema_io_handler()
m.create_speech_recognition_thread()