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

def scan_folder(folder: Path):
    # Returns exclusively a list of all files from the folder
    files = []
    for item in folder.iterdir():
        if (item.is_file()):
            files.append(item)

    return files

def main():
    folder = get_folder()
    print(folder)
    print(type(folder))
    if validate_folder(folder):
        file_list = scan_folder(folder)
        print(file_list)


if __name__ == "__main__":
    main()