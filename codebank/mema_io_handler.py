from queue import Queue
from threading import Thread

from codebank.mema_button_frame import *
from codebank.mema_speech_recognition import *

class io_handler():

    def __init__(self, button_frame: button_frame, input_queue: Queue) -> None:
        """
        Initializes the IO Handler, sets the IO Handler of the button frame, creates the main input queue, speech-recog input queue
        and button event input queue. Initializes an empty speech-callback translation dictionary and starts the thread.
        """

        self.button_frame = button_frame
        self.button_frame.set_io_handler(self)

        # Create Queue
        self.input_queue: Queue
        self.input_queue = input_queue

        # Speech Recognition Thread
        self.sr_input_queue: Queue
        self.sr_input_queue = Queue()

        self.button_input_queue: Queue
        self.button_input_queue = Queue()

        self.speech_translations: dict[str:str] = {}

        self.button_frame.set_io_queue(self.button_input_queue)

        self.stop_speech_recognition_thread = False

        self.create_speech_recognition_thread()
        Thread(target=self.handle_io, daemon=True).start()

    def create_speech_recognition_thread(self) -> None:
        """
        Creates & Starts the speech recognition thread
        """

        # Create the speech recognition thread
        self.stop_speech_recognition_thread = False
        listen(self.sr_input_queue, False)
        
    def close_speech_recognition_thread(self) -> None:
        """
        Stops the speech recognition thread (iffy)
        """

        # Stops speech recognition thread
        self.stop_speech_recognition_thread = True

    def get_button_input_queue(self) -> Queue:
        """
        Gets a reference to the button input queue used for external configuration
        """

        return self.button_input_queue

    def create_button_frame(self) -> None:
        """
        Sets the button_frame IO Handler and IO Queue to this.
        """

        self.button_frame.set_io_handler(self)
        self.button_frame.set_io_queue(self.button_input_queue)

    def set_input(self, button_callback: list[(str, str)], read = False) -> None:
        """
        Handles the mapping of TTS-commands to Callback Strings
        """

        # Setup TTS conversions
        self.speech_translations = {}
        for translation in button_callback:
            if(translation[0] != None and translation[1] != None):
                self.speech_translations[translation[0].lower()] = translation[1]
            else:
                continue

        self.button_frame.set_buttons(button_callback, read)

    def handle_io(self):
        """
        Main Thread loop to take IO requests from the speech recognition and button press queue and formulate it into JSON-style
        call-back requests to the main_window, which will then be passed directly to the current content_frame.
        """
        while True:

            response: dict[str:any]|None = None

            # Handle Spoken Interactions
            if not self.sr_input_queue.empty():
                spoken_content:str = self.sr_input_queue.get()

                # Formulate spoken content
                response: dict[str:any] = {}
                response['input_type'] = MEMA_RESPONSES.SPOKEN

                try: response['content'] = self.speech_translations[spoken_content]
                except: response['content'] = spoken_content

            # Handle Button Interactions
            if not self.button_input_queue.empty():
                button_input:str = self.button_input_queue.get()
                
                # Formulate spoken content
                response: dict[str:any] = {}
                response['input_type'] = MEMA_RESPONSES.BUTTON
                response['content'] = button_input
        
            if response is not None:
                print(response)
                self.input_queue.put(response)


