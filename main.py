from pathlib import Path
import shutil

EXTENSION_CATEGORIES = {
    "Images": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".tif", ".tiff", ".svg", ".ico",
        ".heic", ".heif", ".avif", ".raw",
        ".cr2", ".cr3", ".nef", ".arw", ".dng",
        ".orf", ".rw2", ".raf", ".pef", ".srw"
    },

    "Documents": {
        ".pdf", ".doc", ".docx", ".docm", 
        ".dot", ".dotx", ".odt", ".ott", 
        ".rtf", ".txt", ".md", ".markdown",
        ".pages", ".tex", ".wpd", ".wps"
    },

    "Videos": {
        ".mp4", ".m4v", ".mov", ".avi", ".mkv",
        ".wmv", ".flv", ".webm", ".mpeg", ".mpg",
        ".m2v", ".3gp", ".3g2", ".ts", ".mts",
        ".m2ts", ".vob", ".ogv"
    },

    "Audio": {
        ".mp3", ".wav", ".flac", ".aac", ".m4a",
        ".ogg", ".oga", ".opus", ".wma", ".aiff",
        ".aif", ".aiff", ".alac", ".amr", ".mid",
        ".midi", ".ape", ".mka"
    }
}

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

def get_extension(file: Path):
    return file.suffix.lower()

def categorise_extension(extension: str):
    for category, extensions in EXTENSION_CATEGORIES.items():
        if extension in extensions:
            return category

    return None

def main():
    folder = get_folder()
    print(folder)
    print(type(folder))
    if validate_folder(folder):
        file_list = scan_folder(folder)
        print(file_list)

        for file in file_list:
            ext = get_extension(file)
            print(ext)
            cat = categorise_extension(ext)
            print(cat)


if __name__ == "__main__":
    main()