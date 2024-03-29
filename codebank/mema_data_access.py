# Operating system interaction library
# os is a library that provides functions for interacting with the operating system.
# It is used in this code for performing operating system-related tasks, such as directory operations.
import os

# JSON library
# json is a library for working with JSON (JavaScript Object Notation) data.
# It provides functionality for reading and writing JSON files.
# json is used in this code for loading and saving data in JSON format.
# Documentation: https://docs.python.org/3/library/json.html
import json

# OpenCV library
# cv2 is the OpenCV library for computer vision tasks.
# It provides functionality for image processing, video capture, and more.
# cv2 is used in this code for image-related tasks, such as reading and writing images.
# Documentation: https://docs.opencv.org/
import cv2


def create_userbank() -> str:
    """
    Creates a new userbank directory and returns a string of the full path to the new directory. Directory
    name is incremented from the previous and is representative of user ID, should be called from the new_user()
    function.

    Returns:
        str: Directory path of the created user bank.
    """

    # Define directory path
    directory_path = os.getcwd() + "/databank/"

    # Getting list of subfolders
    subfolders = [file.path for file in os.scandir(directory_path) if file.is_dir()]
    subfolders = [path_string.rsplit('/', 1)[1] for path_string in subfolders]
    
    # Generating userbank name (userbank_ + next iteration)
    directory_name = "userbank_" + str(int(max(subfolders)[-1]) + 1)

    # Create the directory in the parent directory
    os.makedirs((directory_path + directory_name), exist_ok=True)
    print("Directory '%s' created" % directory_name)

    return directory_path + directory_name

def new_user(name: str, photo) -> int:
    """
    Creates a new userbank, stores the passed photograph and name in the generated header file. Uses the
    create_userbank() function to create the new userbank. Automatically generates a new user ID. Writes
    the image using the cv2 library (converts from BGR to RGB first)

    Args:
        name (str): Name of the user.
        photo:      Photo of the user.
    """

    # Get the directory path for the new user bank
    user_dir = create_userbank()

    # Data to be written
    dictionary = {
       "user_id": user_dir[-1],
       "photo": "face.jpg",
       "first_name": name
    }

    # Write the dictionary as JSON to a file
    with open(user_dir + "/header.json", "w") as outfile:
        json.dump(dictionary, outfile)
    
    # Save the photo as an image file
    cv2.imwrite(user_dir + "/face.jpg", cv2.cvtColor(photo, cv2.COLOR_BGR2RGB))

    return int(user_dir[-1])

def get_user(id: int) -> dict:
    """
    Retrieves the user information for the given ID. Opens JSON Header of selected user and
    returns the relevant information as a dictionary.

    Args:
        id (int): User ID.

    Returns:
        dict: User information stored in a dictionary.
    """

    # Construct the directory path for the user's header file
    directory_path = os.getcwd() + "/databank/userbank_" + str(id) + "/header.json"
     
    # Opening JSON file & retrieving data
    with open(directory_path, 'r') as openfile:
        file = json.load(openfile)
    openfile.close()

    return file

def create_memoryspace(id: int, memory_name: str) -> str:
    """
    Creates a new memoryspace in the passed users ID, with the passed memory name string
    """

    # Make a new directory for the memory to be stored in
    directory_path = os.getcwd() + "/databank/userbank_" + str(id) + "/memoryspace_" + str(memory_name).replace(" ", "_").lower()
    os.makedirs(directory_path, exist_ok = True)
    
    print(f"data_access: created memoryspace @ {directory_path}")
    return directory_path

def write_image_to_memoryspace(image, memoryspace_path) -> None:
    pass