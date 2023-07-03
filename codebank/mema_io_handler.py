from queue import Queue
from threading import Thread

class mema_io_handler():

    def __init__(self) -> None:
        
        # Create Queue
        self.input_queue: Queue
        self.input_queue = Queue()

    def create_speech_recognition_thread(self) -> None:
        pass

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