# Generic MeMa Imports
from codebank.mema_content_frame import *
from codebank.mema_facial_recognition import *
from codebank.mema_text_to_speech import *
from codebank.mema_content_new_user_photo import *
from codebank.mema_data_access import *
from codebank.mema_record_content import *
from codebank.mema_content_memory_create_label import *
from codebank.mema_content_memory_view import *

import os
from datetime import datetime, timezone


# GUI library
# tkinter is the standard GUI library for Python.
# It is used in this code for creating the graphical user interface (GUI) elements.
# The `*` import syntax imports all the public names defined in tkinter module.
# Documentation: https://docs.python.org/3/library/tkinter.html
from tkinter import *



class content_memory_list(content_frame):

    def __init__(self, parent, user_id: int, *args, **kwargs)-> None:
        content_frame.__init__(self, *args, **kwargs)

        # Parent should be main window
        self.parent: any
        self.parent = parent

        # Memoryspace Path is the path to the current memoryspace
        self.user_id: str
        self.user_id = user_id

        self.memoryspaces: list = []
        self.current_memory_index = 0

        self.memory_thumbnail_frame = Frame(self, bg = MEMA_WHITE)
        self.memory_thumbnail_frame.pack(expand = True, fill = "both")
        
        self.find_available_memories()

        if len(self.memoryspaces) is 0:
            # No memoryspaces exit, display a message
            self.no_spaces_label = Label(self, text = "No Memories", font = ("Arial", 36, "bold"), fg = MEMA_BLACK, bg = MEMA_WHITE)
            self.no_spaces_label.pack()
            self.update_buttons_no_memories()

        else:
            # Memoryspaces are available
            self.update_buttons()
            self.show_current_memory()

    def show_current_memory(self) -> None:

        self.memory_thumbnail_frame.destroy()
        self.memory_thumbnail_frame = Frame(self, bg = MEMA_WHITE)

        # Gets the selected memory name
        selected_memory: str
        selected_memory = self.memoryspaces[self.current_memory_index]
        selected_memory = selected_memory.split("memoryspace")[1][1:]

        # Display selected memory name
        selected_memory_label = Label(self.memory_thumbnail_frame, text=  selected_memory, font = ("Arial", 36, "bold"), bg = MEMA_WHITE, fg = MEMA_BLACK)
        selected_memory_label.pack(pady=(100,10))

        # Display selected memory creation time
        creation_date = os.stat(self.memoryspaces[self.current_memory_index]).st_ctime
        creation_date = datetime.fromtimestamp(creation_date)

        # Formats the date to DAY-suffix MONTH YEAR 'at' HOUR:MINUTE
        day = creation_date.strftime("%d")
        day_suffix = "th" if day[-1] not in ['1', '2', '3'] or day in ['11', '12', '13'] else \
            {"1": "st", "2": "nd", "3": "rd"}.get(day[-1], "th")
        formatted_date = creation_date.strftime(f"%d{day_suffix} %B %Y at %H:%M")

        # Add
        selected_memory_date = Label(self.memory_thumbnail_frame, text = formatted_date, font = ("Arial", 32), bg = MEMA_WHITE, fg = MEMA_BLACK)
        selected_memory_date.pack()
        
        # Add stuff in frame
        self.memory_thumbnail_frame.pack(expand = True, fill = "both")

    def find_available_memories(self) -> None:
        """
        Gets a list of available memory directorys in the selected users storage.
        """

        directory_path = os.getcwd() + "/databank/userbank_" + str(self.user_id) + "/"
        self.memoryspaces = [f.path for f in os.scandir(directory_path) if f.is_dir()]
        print(self.memoryspaces)

    def next_frame(self) -> None:
        self.current_memory_index = (self.current_memory_index + 1) % len(self.memoryspaces)
        self.show_current_memory()

    def update_buttons_no_memories(self) -> None:
        """
        Updates the button frame to show only option to back to the main menu
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = MEMA_EMPTY_BUTTON
        buttons[1] = MEMA_EMPTY_BUTTON
        buttons[2] = MEMA_EMPTY_BUTTON
        buttons[3] = ("EXIT", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def update_buttons(self) -> None:
        """
        Updates the button frame to show options to go to the camera, add a label, go to the next frame or
        exit the current page (go back to the MeMa login page.)
        """

        buttons: list[(str, str)] = [0, 0, 0, 0]
        buttons[0] = ("VIEW", "MEMORY_LIST_VIEW")
        buttons[1] = ("NEXT","MEMORY_LIST_NEXT")
        buttons[2] = MEMA_EMPTY_BUTTON
        buttons[3] = ("EXIT", "HOME_EXIT")
        self.parent.set_input(buttons, False)

    def callback(self, callback_request: dict[str:str]) -> None:
        
        match callback_request["content"]:

            case "MEMORY_LIST_NEXT":
                self.next_frame()
            
            case "MEMORY_LIST_VIEW":
                selected_memory:str 
                selected_memory = self.memoryspaces[self.current_memory_index]
                self.parent.switch_content(content_memory_view, selected_memory)
            
            case "HOME_EXIT":
                self.parent.reset_path()