from mema_content_frame import *
from mema_text_to_speech import *

class content_memory_create(content_frame):

    def __init__(self, parent, user_id, *args, **kwargs):
        content_frame.__init__(self, *args, **kwargs)

        speak("We need to take a photograph of you to login, please center your face and say TAKE PHOTO")

        self.scrollbar = Scrollbar(self, orient = 'horizontal', command = self.xview)
        self.scrollbar.grid(row=1, column = 0, sticky = 'ew')

        self.label = Label(text = "TEST TEST TEST TEST TEST TEST", font = ("Arial", 50, "bold"))
        self.label.grid(row = 0, column = 0)

        self.parent = parent
        self.user_id = user_id

    def callback(self, callback_request:dict) -> None:
        print(callback_request)