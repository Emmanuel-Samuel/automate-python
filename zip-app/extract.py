# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 11/03/2023
# REVISED DATE: 11/03/2023
# PURPOSE: Create a GUI Zip Extractor App

# import modules
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.QtCore import Qt
from pathlib import Path
import zipfile

# define function to open directory
def open_files():
    # sets root_dir as global variable
    global root_dir
    # gets directory
    path = QFileDialog.getExistingDirectory(window, 'Select Folder')
    if path:
        root_dir = Path(path)
        message.setText(path)

# define function for finding zip files and extract
def extract_files():
    # iterates over all the files in directory
    for path in root_dir.glob("*.zip"):
        # read file woth zipfile library
        with zipfile.ZipFile(path, 'r') as zf:
            # path.stem get the first part without the extension
            final_path = root_dir / Path(path.stem)
            # method that extracts the files
            zf.extractall(path=final_path)
    # shows if extraction was successfull
    message.setText('<font color="green">Extraction Successful!</font>')

# main GUI window defined
app = QApplication([])
window = QWidget()
window.setWindowTitle('Zip Extractor App')
layout = QVBoxLayout()

# sends a description about what the app does 
description = QLabel('Select the folder containing the zip files. The files will be <font color="red">extracted</font>')
layout.addWidget(description)

# layout for first option defined
open_btn = QPushButton('Open Folder')
open_btn.setToolTip('Open File')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

# layout for second option defined
destroy_btn = QPushButton('Extract Files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(extract_files)

# aligns the Qlabel
message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

# executes app
window.setLayout(layout)
window.show()
app.exec()
