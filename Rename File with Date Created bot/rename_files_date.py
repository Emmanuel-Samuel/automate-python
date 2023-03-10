# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 13/02/2023
# REVISED DATE: 13/02/2023
# PURPOSE: Create a Python Script that renames files with date created added to the filenames

# import module pathlib
from pathlib import Path
from datetime import datetime

# asks the user for the directory path
direc = str(input('Enter the directory containing the folder of the files to be renamed\n'))

# defines root directory of file folder
file_origin = Path(direc)

# main function iteration
for path in file_origin.glob("**/*"):
    # checks if it's a file
    if path.is_file():
        # gets the stats of the time created
        date_created = datetime.fromtimestamp(path.stat().st_ctime)
        # coverts the value to a string
        date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
        # defines the new name for the files
        new_name = date_created_str + '_' + path.name
        # defines the new path for the files
        new_path = path.with_name(new_name)
        # performs the rename method
        path.rename(new_path)

