import os
import time

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

if __name__ == "__main__":
    print(create_userbank())