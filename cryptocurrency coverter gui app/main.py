# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 21/03/2023
# REVISED DATE: 21/03/2023
# PURPOSE: Create a live crypto converter app


# import modules
# libraries for gui interface
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
# library for web scraping
from bs4 import BeautifulSoup
# library to get requests
import requests


# function to web scrape 1 cryptocurrency rate from coin base
def get_crypto(in_crypto):
    url = f'https://www.coindesk.com/price/{in_crypto}/'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_="currency-pricestyles_Price-sc-1rux8hj-0 jIzQOt").get_text()
    rate = float(rate[1:])
    return rate


# function to calculate and display the final converted output
def show_crypto():
    input_text = float(text.text())
    in_cry = in_combo.currentText()
    rate = get_crypto(in_cry)
    output = round(input_text * rate, 2)
    message = f'{input_text} {in_cry} is {output} USD'
    output_label.setText(str(message))


# creates the app instance
app = QApplication([])
window = QWidget()
window.setWindowTitle('CryptoCurrency Converter')

# d layout is vertical
layout = QVBoxLayout()

# description to aid usage
description = QLabel('Enter the amount of crypto in the box below to be <font color="green">converted</font>')
layout.addWidget(description)

# first layout horizontal
layout1 = QHBoxLayout()
layout.addLayout(layout1)

# text widget
output_label = QLabel('')
layout.addWidget(output_label)

# internal layout vertical
layout2 = QVBoxLayout()
layout1.addLayout(layout2)

# internal layout vertical
layout3 = QVBoxLayout()
layout1.addLayout(layout3)

# drop down menu
in_combo = QComboBox()
currencies = ['bitcoin', 'ethereum', 'matic', 'shibainu', 'bnb', 'sol']
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

# gets input text widget
text = QLineEdit()
layout3.addWidget(text)

# action button for conversion
btn = QPushButton('Convert')
layout3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
# widgets, signals, slots
btn.clicked.connect(show_crypto)

# Source defined
info = QLabel('<font color="blue">Live rates gotten from coinbase</font>')
layout.addWidget(info)

# runs the app
window.setLayout(layout)
window.show()
app.exec()