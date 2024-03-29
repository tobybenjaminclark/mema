# Enum class from the enum module. Used to create an enumeration to represent callback types
# see MEMA_RESPONSES for a functional declaration of an Enum (this can also be declared via OOP)
from enum import Enum

# Change this to change the window dimensions.
global MEMA_SCREEN_DIMENSIONS
MEMA_SCREEN_DIMENSIONS: str = "1280x800"

# Change this to change the default button colours.
global MEMA_BUTTON_COLOURS
MEMA_BUTTON_COLOURS: list[str] = ["#FCD0A1", "#AFD2E9", "#B8B8FF", "#D295BF"]

# Change this to change frame backgrounds & text color
global MEMA_WHITE, MEMA_BLACK
MEMA_WHITE: str = "#EFE9E7"
MEMA_BLACK: str = "#1B1311"


# Change this to change the content & button width
global MEMA_CONTENT_WIDTH, MEMA_BUTTON_WIDTH
MEMA_CONTENT_WIDTH: int = 8
MEMA_BUTTON_WIDTH: int = 4

# Change this to control whether faces are highlighted
global MEMA_FACIAL_RECOGNITION_DEBUG_MODE
MEMA_FACIAL_RECOGNITION_DEBUG_MODE: bool = True

# Change this to change the window name
global MEMA_WINDOW_NAME
MEMA_WINDOW_NAME: str = "MeMa 3.1"

# Change this to change whether speech recognition is printed directly to stdout
global MEMA_SPEECH_RECOGNITION_DISPLAY_TEXT
MEMA_SPEECH_RECOGNITION_DISPLAY_TEXT: bool = False

# Change this to add/remove response types (adding IO?)
global MEMA_RESPONSES
MEMA_RESPONSES:Enum = Enum('MEMA_RESPONSES', ["SPOKEN", "BUTTON"])

# Change this to make the TTS speed
global MEMA_SLOW_TTS
MEMA_SLOW_TTS:bool = False

# Change this to change the font on the large buttons
global MEMA_BUTTON_FONT
MEMA_BUTTON_FONT:tuple[str,int,str] = ("Arial Black", 32, "bold")

# Constant for an empty button on button initialization
global MEMA_EMPTY_BUTTON
MEMA_EMPTY_BUTTON: tuple[str|None, str|None]
MEMA_EMPTY_BUTTON = (None, None)

# Settings for mema video export
global MEMA_EXPORT_FRAME_CONSTANT, MEMA_EXPORT_LABEL_DURATION
MEMA_EXPORT_FRAME_CONSTANT = 5
MEMA_EXPORT_LABEL_DURATION = 1