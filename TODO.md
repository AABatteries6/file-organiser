# TODO - File Organiser

## Version 1 - Basic File Organiser

### Core functionality
- [x] Accept folder path from user
- [x] Validate that the folder exists
- [x] Scan only files directly inside the selected folder
- [x] Ignore subfolders
- [X] Identify file extensions
- [x] Categorise supported file types:
    - [x] Images
    - [x] Videos
    - [x] Audio
    - [x] Documents
- [x] Ignore unsupported file types
- [x] Build move plan before performing any moves
- [x] Create destination folders only when required
- [x] Execute planned file moves
- [x] Display completion message when finished

### Safety checks
- [x] Do not move folders
- [x] Do not overwrite existing files
- [x] Handle files that cannot be moved
- [x] Handle empty folders correctly

## V1.1 Summary and Information for User 
- [x] Handle empty folder with an appropriate message
- [x] Handle folders containing only sub-folders with an appropriate message
- [x] Provide a concise, tidied summary of the organisation results
- [x] Offer the user the option to view more detailed information about files that could not be organised
- [x] Provide clear explanations for why files could not be organised

## V1.2 Exception Handling
- [ ] Handle permission/os errors while scanning folder
- [ ] Handle os errors while creating folders
- [ ] Handle os errors when moving files
- [ ] Decide how errors affecting only parts of program are represented in summary

---