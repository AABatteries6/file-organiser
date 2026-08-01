from pathlib import Path
import shutil

def get_folder():
    # This method takes a filepath input and converts to Path object
    folder = Path(input("Enter folder path:  "))
    return folder

def validate_folder(folder: Path):
    # Validates inputted filepath
    if (folder.exists() and folder.is_dir()):
        return True
    elif (not folder.exists()):
        print("Folder cannot be found.")
        return False
    else:
        print("Path points to file, not folder.")
        return False

def main():
    folder = get_folder()
    print(folder)
    print(type(folder))
    validate_folder(folder)


if __name__ == "__main__":
    main()