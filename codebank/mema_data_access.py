import cv2
import os
import time
import json

def create_userbank() -> str:

    # Define directory path
    directory_path:str
    directory_path = os.getcwd() + "/databank/"

    # Getting list of subfolders
    subfolders: list(str)
    subfolders = [f.path for f in os.scandir(directory_path) if f.is_dir()]
    subfolders = [path_string.rsplit('/', 1)[1] for path_string in subfolders]
    
    # Generating userbank name (userbank_ + next iteration)
    directory_name: str
    directory_name = "userbank_" + str(int(max(subfolders)[-1]) + 1)

    # Create the directory in the parent directory
    os.makedirs((directory_path + directory_name), exist_ok=True)
    print("Directory '%s' created" % directory_name)

    return directory_path + directory_name

def new_user(name: str, photo) -> None:

    user_dir = create_userbank()
    # Data to be written

    dictionary = {
       "user_id": user_dir[-1],
       "photo": "face.jpg",
       "first_name": name
    }
    
    with open(user_dir + "/header.json", "w") as outfile:
        json.dump(dictionary, outfile)
    
    cv2.imwrite(user_dir + "/face.jpg", cv2.cvtColor(photo, cv2.COLOR_BGR2RGB))

def get_user(id: int) -> dict:

    directory_path:str
    directory_path = os.getcwd() + "/databank/userbank_" + str(id) + "/header.json"
     
    # Opening JSON file
    with open(directory_path, 'r') as openfile:
        file = json.load(openfile)
    openfile.close()

    print(file)

    return file


if __name__ == "__main__":
    print(create_userbank())

    