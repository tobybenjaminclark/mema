import sys

if __name__ == "__main__":
    print("[memory_machine] : starting mema 3.5.")
    
    if "-emulator" in sys.argv:
        print("[memory_machine] : starting and linking emulation interface.")
    
    if "-firmware" in sys.argv:
        print("[memory_machine] : starting and linking firmware interface.")

