from pathlib import Path
import shutil

def get_folder():
    folder = Path(input("Enter folder path:  "))
    return folder