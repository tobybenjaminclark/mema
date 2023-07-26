import os
import cv2
import numpy as np

FRAME_CONSTANT = 5  # Duration in seconds to display each frame
LABEL_DURATION = 1

def get_frame_paths(memoryspace_path: str) -> list[str]:
    """
    Get paths of image and video files that contain 'content' in their filename from the specified memoryspace. This essentially
    collects the videos and images in a memorybank, and returns them as a list of paths (strings)
    """
    frame_paths: list[str]
    frame_paths = []  # Initialize an empty list to store the paths of matching files.

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

def create_black_screen_with_label(label, frame_size):
    # Create a black screen with the label displayed at the center
    blank_image = 0 * 255 * np.ones(shape=[frame_size[1], frame_size[0], 3], dtype=np.uint8)
    
    text = label
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2.5
    font_thickness = 6
    
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = int((frame_size[0] - text_width) / 2)
    text_y = int((frame_size[1] + text_height) / 2)
    
    cv2.putText(blank_image, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)
    
    return blank_image

def create_memoryspace_video(memoryspace_path, output_path):
    frame_paths = get_frame_paths(memoryspace_path)
    frame_paths.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split("_")[0]))
    labels = get_labels(frame_paths)

    frame_size = None
    fps = 30.0
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = None

    for frame_path in frame_paths:
        frame_number, _ = os.path.splitext(os.path.basename(frame_path))
        frame_number = frame_number.split("_")[0]
        print(frame_number)
        label = labels.get(frame_number, "")
        print(label)
        if frame_path.endswith(".mp4"):
            cap = cv2.VideoCapture(frame_path)
            ret, frame = cap.read()
        else:
            frame = cv2.imread(frame_path)

        if frame_size is None:
            frame_size = (frame.shape[1], frame.shape[0])
            out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

        # Create a black screen with the label for LABEL_DURATION seconds
        blank_frame = create_black_screen_with_label(label, frame_size)
        label_duration_frames = int(fps * LABEL_DURATION)
        for _ in range(label_duration_frames):
            out.write(blank_frame)

        # Resize frame to the standard size
        frame = cv2.resize(frame, frame_size)

        # Add label text to the frame
        text = label
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2.5
        font_thickness = 6

        (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, font_thickness)
        text_x = int((frame.shape[1] - text_width) / 2)
        text_y = frame.shape[0] - int(text_height * 1.5)  # Place text at the bottom center

        cv2.putText(frame, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)

        duration = int(fps * FRAME_CONSTANT)
        for _ in range(duration):
            out.write(frame)

        # Release the VideoCapture object if a video is being used as input
        if frame_path.endswith(".mp4"):
            cap.release()

    # Release the VideoWriter
    if out is not None:
        out.release()

if __name__ == "__main__":
    memoryspace_path = "databank/userbank_1/memoryspace_memory_in_the_park"  # Replace with the path to your memoryspace directory
    output_path = "output_video.mp4"

    create_memoryspace_video(memoryspace_path, output_path)
