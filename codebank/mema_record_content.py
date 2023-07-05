import numpy as np
import cv2
from tkinter import *
import PIL
from PIL import ImageTk
from mema_content_frame import *

class content_record(content_frame):

    def __init__(self, parent, *args, **kwargs) -> None:

        Frame.__init__(self, parent, *args, **kwargs)

        self.recording = False

        # This will return video from the first webcam on your computer.
        self.label = Label(self, anchor = CENTER, highlightbackground = "black", highlightthickness = 2, bg = "black")
        self.label.pack()

        self.stop_button = Button(self, text = "stop", command = lambda: self.stop())
        self.stop_button.pack()

        self.record_button = Button(self, text = "start recording", command = lambda: self.start_recording())
        self.record_button.pack()

        self.take_photo_button = Button(self, text = "take photo", command = lambda: self.take_photo())
        self.take_photo_button.pack()

        self.cap = cv2.VideoCapture(0)

        self.show_frames()
    
    def start_recording(self):

        # Define the codec and create VideoWriter object
        self.record_button.configure(text = "stop recording", command = lambda: self.stop_recording())
        self.update()
        self.fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        self.out = cv2.VideoWriter('sample.mp4', self.fourcc, 20.0, (640, 480))
        self.recording = True

    def stop_recording(self):

        self.recording = False
        # After we release our webcam, we also release the output
        self.record_button.configure(text = "start recording", command = lambda: self.start_recording())
        self.update()
        self.out.release() 

    def take_photo(self):
        # Save the photo as an image file
        try: cv2.imwrite("test.jpg", cv2.cvtColor(self.current_image, cv2.COLOR_BGR2RGB))
        except Exception as e: print(f"could not take photo, exception: {e}")

    def show_frames(self):

        # reads frames from a camera 
        # ret checks return at each frame
        ret, frame = self.cap.read() 

        # output the frame
        if(self.recording): self.out.write(frame) 
        
        self.current_image = cv2.cvtColor(self.cap.read()[1],cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(self.current_image)

        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        
        self.after(20, self.show_frames)


    def stop(self):

        # Close the window / Release webcam
        self.cap.release()
        
        # De-allocate any associated memory usage 
        cv2.destroyAllWindows()

        self.destroy()
        quit()

    def callback(callback_request:dict):
        pass