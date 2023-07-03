from queue import Queue
from threading import Thread

from mema_speech_recognition import *

class mema_io_handler():

    def __init__(self) -> None:
        
        # Create Queue
        self.input_queue: Queue
        self.input_queue = Queue()

        # Speech Recognition Thread
        self.sr_input_queue: Queue
        self.sr_input_queue = Queue()

    def create_speech_recognition_thread(self) -> None:
        
        # Create the speech recognition thread
        listen(self.sr_input_queue)

        # Monitor the return for input
        while(True):
            op = self.sr_input_queue.get()
            print(op)
        
    def create_text_to_speech_thread(self) -> None:
        pass

    def create_facial_recognition_thread(self) -> None:
        pass




    def close_speech_recognition_thread(self) -> None:
        pass

    def close_text_to_speech_thread(self) -> None:
        pass

    def close_facial_recognition_thread(self) -> None:
        pass

m = mema_io_handler()
m.create_speech_recognition_thread()