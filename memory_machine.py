# sys is a standard python library used for accessing system stuff
# in this code we're using it to access argv (command line arguments)
# and parse these to decide mema's settings.
import sys

# Threads are used here to run the emulator/serial communication stuff
# simultaneously alongside the main mema interface and processing.
from threading import Thread

# Generic MeMa Imports
from codebank.mema_main_window import *
from codebank.mema_emulator_interface.mema_emulator_buttons import *



# only run this code if running directly
if __name__ == "__main__":
    print("[memory_machine] : starting mema 3.5.")
    
    mema = main_window(emulator = True)

    # start the mema emulator
    if "-emulator" in sys.argv:
        print("[memory_machine] : starting and linking emulation interface.")
    
    # link mema firmware (arduino), used on physical mema
    if "-firmware" in sys.argv:
        print("[memory_machine] : starting and linking firmware interface.")



    
