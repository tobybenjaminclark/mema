import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"sample.mp4")
videoplayer.pack(expand=True, fill="both")
videoplayer.play()

def replay(event):
    print("replayed")
    
    videoplayer.play()

videoplayer.bind("<<Ended>>", replay)

root.mainloop()