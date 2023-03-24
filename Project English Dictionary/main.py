# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 21/03/2023
# REVISED DATE: 22/03/2023
# PURPOSE: Create an English Dictionary


# import modules
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
import json


# load json file containing data as data
data = json.load(open("data.json"))


# function for finding the word in the data
def translate():
    # gets text and assign to w
    w = text.text()
    # makes text lower case
    w = w.lower()
    # condition for checking text in data
    if w in data:
        results = data[w]
        output_label.setText("\n".join(results))
    # if text found, then do this
    else:
        output_label.setText("This word doesn't exist. Please try again.")


# design for GUI layout
app = QApplication([])
window = QWidget()
window.setWindowTitle('English Dictionary')

layout = QVBoxLayout()

# description to aid usage
description = QLabel('Enter the word to be <font color="green">searched</font>')
layout.addWidget(description)

layout1 = QHBoxLayout()
layout.addLayout(layout1)

layout2 = QVBoxLayout()
layout.addLayout(layout2)

# widget to get text input
text = QLineEdit()
layout1.addWidget(text)

# adds button to search
btn = QPushButton('Search')
layout1.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(translate)

output = QWidget()

# defines app dimensions
output_label = QLabel('')
output_label.setFixedSize(800, 100)
layout2.addWidget(output_label)

# set layout and run
window.setLayout(layout)
window.show()
app.exec()