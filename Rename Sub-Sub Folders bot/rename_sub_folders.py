# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 13/02/2023
# REVISED DATE: 13/02/2023
# PURPOSE: Create a Python Script that renames files prefix with sub-sub folders names

# import module pathlib
from pathlib import Path

# asks the user for path diectory
file_origin = str(input("Enter path to directory, containing the 2 sub folders\n"))

# main function
for path in file_origin.glob("**/*"):
    # checks if it's a file
    if path.is_file():
         # defines the main folder
         main_folder = path.parts
         # defines the sub main folder
         sub_main_folder = path.parts[1:-1]
         # defines the new name for the files
         new_name = '-'.join(subfolders) + '-' + son_folder + '-' + path.name
         # defines the new path for the files
         new_path = path.with_name(new_name)
         # performs the rename
         path.rename(new_path)
