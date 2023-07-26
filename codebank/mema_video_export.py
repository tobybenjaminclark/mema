# Operating system interaction library
# The 'os' module provides functions for interacting with the operating system.
# It is used in this code for file and directory manipulation, such as listing files in a directory and checking file existence.
# Documentation: https://docs.python.org/3/library/os.html
import os

# OpenCV library
# The 'cv2' module is part of the OpenCV (Open Source Computer Vision) library, which is used for computer vision tasks.
# It provides functionality for image and video processing, including reading video frames, resizing images, and adding text to frames.
# OpenCV is used in this code for creating and manipulating video streams from image frames.
# Documentation: https://docs.opencv.org/
import cv2

# Numerical operations library
# The 'numpy' library provides functionality for numerical computations and array manipulation in Python.
# It is used in this code for various numerical operations on arrays, such as resizing frames and processing image data.
# Documentation: https://numpy.org/doc/
import numpy as np

# Generic MeMa Import
from mema_constants import *

def get_frame_paths(memoryspace_path: str) -> list[str]:
    """
    Get paths of image and video files that contain 'content' in their filename from the specified memoryspace. This essentially
    collects the videos and images in a memorybank, and returns them as a list of paths (strings)
    """

    # Initialize an empty list to store the paths of matching files.
    frame_paths: list[str]
    frame_paths = []  
    
    # os.walk generates the file names in a directory tree
    # root (str): The current directory being visited
    # dirs (List[str]): A list of subdirectories in the current directory
    # files (List[str]): A list of files in the current directory 
    for root, _, files in os.walk(memoryspace_path):

        # Iterate through the files in the current directory.
        for file in files:
            
            # Check if the file ends with .jpeg, .jpg, or .mp4 AND contains 'content' in its filename.
            if file.endswith((".jpeg", ".jpg", ".mp4")) and "content" in file:
                
                # Construct the full path of the file by joining the current root directory with the filename.
                frame_path: str
                frame_path = os.path.join(root, file)
                
                # Append the file path to the list of frame_paths.
                frame_paths.append(frame_path)
                
    # Return the list of file paths for image and video files containing 'content' in their filenames.
    return frame_paths
    


def get_labels(frame_paths: list[str]) -> dict[str, str]:
    """
    Process label files for each frame in the given list of frame_paths and return a dictionary
    containing frame numbers as keys and their corresponding labels as values.
    """

    # Initialize an empty dictionary to store frame numbers and labels.
    labels: dict[str, str]
    labels = {}     

    print("Processing Labels")
    
    # For each frame 
    for frame_path in frame_paths:

        # Extract the frame number from the file name by removing the extension and splitting by underscore.
        frame_number, _ = os.path.splitext(os.path.basename(frame_path))
        frame_number = frame_number.split("_")[0]

        # Create the path for the corresponding label file based on the frame number.
        label_path = os.path.join(os.path.dirname(frame_path), f"{frame_number}_label.txt")

        # Check existence, then open.
        if os.path.exists(label_path):
            
            # Open the label file
            label_file = open(label_path, 'r')

            # Read the label from the label file and strip any leading/trailing whitespaces.
            label = label_file.read().strip()

            # Store the frame number as the key and its corresponding label as the value in the 'labels' dictionary.
            labels[frame_number] = label

            # Print the processing status for this frame.
            print(f"\tFrame: '{frame_number}' is '{label}'")

            # Close that label file
            label_file.close()

    return labels

def create_black_screen_with_label(label: str, frame_size: tuple[int, int]) -> np.ndarray:
    """
    Create a black screen with the label displayed at the center. This returns a numpy array representing the black
    screen with the label displayed at the center. It takes the frame size (resolution) and label text as parameters.
    """

    # Create a black screen with the label displayed at the center.
    # This lokos complicated, but it essentially is just a big array of zeroes, this makes the background black.
    blank_image: np.NDArray[np._SCT@np.zeros]
    blank_image = np.zeros(shape=[frame_size[1], frame_size[0], 3], dtype=np.uint8)

    # Text is the label/caption to be displayed
    text: str
    text = label

    # Font to be displayed (Cv2 Constant)
    font: int
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Font Scale
    font_scale: float
    font_scale = 2.5

    # Font Thickness
    font_thickness: int
    font_thickness = 6

    # Get the size of the text and calculate its position to center it.
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, font_thickness)

    # Text Screen Position
    text_x: int
    text_x = int((frame_size[0] - text_width) / 2)

    text_y: int
    text_y = int((frame_size[1] + text_height) / 2)

    # Draw the text on the black screen.
    cv2.putText(blank_image, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

    return blank_image

def create_memoryspace_video(memoryspace_path: str, output_path: str) -> None:
    """
    Create a memoryspace video from the frames in the given memoryspace_path and save it to the output_path.
    Each frame is displayed with its corresponding label centered at the bottom for a fixed duration.

    Parameters:
        memoryspace_path (str): The path to the memoryspace directory containing image and video frames.
        output_path (str): The path where the resulting memoryspace video will be saved.
    """
    # Get the paths of image and video frames from the memoryspace directory
    frame_paths: list[str]
    frame_paths = get_frame_paths(memoryspace_path)

    # Sort frame paths based on their numeric order (assuming filenames have frame numbers)
    frame_paths.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split("_")[0]))

    # Get the labels for each frame using the frame paths
    labels: dict[str, str]
    labels = get_labels(frame_paths)

    # Variable to store frame size
    frame_size: tuple[int, int]
    frame_size = None  

    # Frames per second for the output video
    fps: float
    fps = 30.0  

    # Video codec for the output video (Not sure the type of this?)
    fourcc : any
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 

    # VideoWriter object for writing the output video
    out: cv2.VideoWriter
    out = None  

    # Iterate through each frame in the sorted frame_paths list
    for frame_path in frame_paths:

        # Get the corresponding label for the frame
        frame_number, _ = os.path.splitext(os.path.basename(frame_path))
        frame_number = frame_number.split("_")[0]
        label: str = labels.get(frame_number, "")  

        # Check if the frame is an image or video and load it accordingly
        if frame_path.endswith(".mp4"):
            cap = cv2.VideoCapture(frame_path)
            ret, frame = cap.read()
        else:
            frame = cv2.imread(frame_path)

        # If frame_size is not set, set it to the size of the first frame and initialize VideoWriter
        if frame_size is None:
            frame_size = (frame.shape[1], frame.shape[0])
            out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

        # Create a black screen with the label for LABEL_DURATION seconds
        blank_frame: np.ndarray = create_black_screen_with_label(label, frame_size)
        label_duration_frames: int = int(fps * MEMA_EXPORT_LABEL_DURATION)
        
        # Write the black screen with the label to the output video for LABEL_DURATION seconds
        for _ in range(label_duration_frames):
            out.write(blank_frame)

        # Resize the frame to the standard size
        frame = cv2.resize(frame, frame_size)

        # Add label text to the frame
        text = label
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale: float = 2.5
        font_thickness: int = 6

        # Get Text Size
        (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, font_thickness)

        # Place text at the bottom center
        text_x: int
        text_x = int((frame.shape[1] - text_width) / 2)
        text_y: int
        text_y = frame.shape[0] - int(text_height * 1.5)  

        # Write the label text on the frame
        cv2.putText(frame, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)

        # Write the frame to the output video for FRAME_CONSTANT seconds
        duration: int
        duration = int(fps * MEMA_EXPORT_FRAME_CONSTANT)

        # Write to outfile
        for _ in range(duration):
            out.write(frame)

        # Release the VideoCapture object if a video is being used as input
        if frame_path.endswith(".mp4"):
            cap.release()

    # Release the VideoWriter object
    if out is not None:
        out.release()

if __name__ == "__main__":
    memoryspace_path = "databank/userbank_1/memoryspace_memory_in_the_park"  # Replace with the path to your memoryspace directory
    output_path = "output_video.mp4"

    create_memoryspace_video(memoryspace_path, output_path)
