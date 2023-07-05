from mema_content_frame import *
from mema_text_to_speech import *

class content_memory_create(content_frame):

    def __init__(self, parent, user_id, *args, **kwargs):
        content_frame.__init__(self, *args, **kwargs)

        speak("We need to take a photograph of you to login, please center your face and say TAKE PHOTO")

        self.current_image: Image = None
        self.kill_cam: bool = False

        self.parent = parent
        self.user_id = user_id

    def callback(self, callback_request:dict) -> None:
        print(callback_request)