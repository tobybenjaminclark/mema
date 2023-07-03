
from enum import Enum

global MEMA_SCREEN_DIMENSIONS
MEMA_SCREEN_DIMENSIONS: str = "1280x800"

global MEMA_BUTTON_COLOURS
MEMA_BUTTON_COLOURS: list[str] = ["#F5FFC6", "#B4E1FF", "#AB87FF", "#C1FF9B"]

global MEMA_CONTENT_WIDTH, MEMA_BUTTON_WIDTH
MEMA_CONTENT_WIDTH: int = 8
MEMA_BUTTON_WIDTH: int = 4

global MEMA_FACIAL_RECOGNITION_DEBUG_MODE
MEMA_FACIAL_RECOGNITION_DEBUG_MODE: bool = True

global MEMA_WINDOW_NAME
MEMA_WINDOW_NAME: str = "MeMa 3.1"

global MEMA_SPEECH_RECOGNITION_DISPLAY_TEXT
MEMA_SPEECH_RECOGNITION_DISPLAY_TEXT: bool = False

global MEMA_RESPONSES
MEMA_RESPONSES = Enum('MEMA_RESPONSES', ["SPOKEN", "BUTTON"])
