from pathlib import Path
import shutil

# Dictionary of categories and supported extensions
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
    folder = Path(input("Enter folder path:  ").strip())
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
    # Returns an exclusive list of all files from the folder, and whether the folder contains items
    files = []
    contains_items = False
    for item in folder.iterdir():
        contains_items = True
        if (item.is_file()):
            files.append(item)

    return files, contains_items

def get_extension(file: Path):
    # Returns extension of file in lowercase
    return file.suffix.lower()

def categorise_extension(extension: str):
    # Returns category of given extension
    for category, extensions in EXTENSION_CATEGORIES.items():
        if extension in extensions:
            return category

    return None


def build_move_plan(files: list[Path]):
    # Returns a dictionary of filepaths and their category and the number of unsupported files
    move_plan = {}
    unsupported_files_counter = 0
    for file in files:
        ext = get_extension(file)
        cat = categorise_extension(ext)

        if cat is not None:
            move_plan[file] = cat

        else:
            unsupported_files_counter +=1

    return move_plan, unsupported_files_counter

def validate_destinations(folder: Path, move_plan: dict[Path, str]):
    # Checks whether the category destinations can be made
    # Returns a list of folders that can, and another of conflicts
    valid_categories = set()
    conflicting_categories = set()

    for cat in set(move_plan.values()):
        destination = folder / cat

        if destination.exists() and not destination.is_dir():
            conflicting_categories.add(cat)  

        else:
            valid_categories.add(cat)

    return valid_categories, conflicting_categories

def create_valid_move_plan(move_plan: dict[Path, str], valid_categories: set[str]):
    # Creates a valid move plan accounting for conflicts, and also returns counters for category and filename conflicts
    valid_move_plan = {}
    conflicting_category_files_counter = 0
    conflicting_name_files_counter = 0

    for file, category in move_plan.items():
        if category in valid_categories:
            parent_folder = file.parent
            destination = parent_folder / category / file.name
            if destination.exists():
                conflicting_name_files_counter +=1

            else:
                valid_move_plan[file] = category


        else:
            conflicting_category_files_counter +=1

    return valid_move_plan, conflicting_category_files_counter, conflicting_name_files_counter

def create_category_folders(folder: Path, valid_move_plan: dict[Path, str]):
    # Creates only the necessary category folders
    categories = set(valid_move_plan.values())

    for category in categories:
        destination = folder / category
        destination.mkdir(exist_ok=True)

def move_files(valid_move_plan: dict[Path, str]):
    # This moves files from original position to their intended destination
    for file, category in valid_move_plan.items():
        destination = file.parent / category / file.name
        shutil.move(file, destination)



def main():

    folder = get_folder()

    if validate_folder(folder):
        file_list, contains_items = scan_folder(folder)

        if not contains_items:
            print("This folder is empty.")
            return

        if not file_list:
            print("This folder contains only sub-folders.")
            return
        
        move_plan, unsupported_files_counter = build_move_plan(file_list)
        valid_categories, conflicting_categories = validate_destinations(folder, move_plan)
            
        valid_move_plan, conflicting_category_files_counter, conflicting_name_files_counter = create_valid_move_plan(move_plan, valid_categories)
        create_category_folders(folder, valid_move_plan)

        if valid_move_plan:
            move_files(valid_move_plan)
            print("Organisation completed!")
            move_counter=len(valid_move_plan)
            print(f"{move_counter} files moved.")
        else:
            print("No moves could be made. Program finished")

        unmovable_files_no = conflicting_category_files_counter + conflicting_name_files_counter + unsupported_files_counter
        if unmovable_files_no > 0:
            print(f"{unmovable_files_no} file(s) could not be organised.")

            further_information = input("If you want information regarding why some files could not be moved, type yes, else hit enter: ")
            if further_information.strip().lower() == "yes":

                if conflicting_categories:
                            conflicting_categories_no = len(conflicting_categories)
                            print(f"{conflicting_categories_no} category folder(s) could not be made due to other files in {folder}" 
                                  f" having identical names. The categories are: ")
                            for category in conflicting_categories:
                                print(category)
                            print(f"{conflicting_category_files_counter} file(s) could not be moved due to this issue.")

                if conflicting_name_files_counter>0:
                    print(f"{conflicting_name_files_counter} file(s) could not be moved due to files in the category destination folder having the same name.")

                if unsupported_files_counter>0:
                    print(f"{unsupported_files_counter} filetype(s) are unsupported in this version of the file organiser, so could not be moved.")




if __name__ == "__main__":
    main()