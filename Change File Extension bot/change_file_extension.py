# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 13/02/2023
# REVISED DATE: 13/02/2023
# PURPOSE: Create a Python Script that changes the file extension of files to csv

# import module
from pathlib import Path

# main function
def main():
    # asks user for input
    direc = str(input("Enter the Directory that contains the files to be coverted\n"))
    file_prev = str(input("Enter the file format(e.g txt,csv)\n"))
    file_next = str(input("Enter the file format to be converted to\n"))
    
    # defines file directory
    file_dir = Path(direc)
    
    for path in file_dir.rglob("*." + file_prev):
        if path.is_file():
            new_ext_file = path.with_suffix("." + file_next)
            path.rename(new_ext_file)

print(main())
print("Done!!!")
