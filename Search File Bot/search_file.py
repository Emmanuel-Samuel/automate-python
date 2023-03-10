# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 13/02/2023
# REVISED DATE: 13/02/2023
# PURPOSE: Create a Python Script that automates searching of files/folders 

# import module
from pathlib import Path

#
direc = str(input("Enter the Directory To Search\n"))

search_name = str(input("Enter search name\n"))

# defines the root directory
home_dir = Path(direc)

# method to find files in directories and sub-directories
for paths in home_dir.rglob("*"):
    # checks for the item
    if search_name in paths.stem:
        # prints the path of object
        print(paths.absolute())
