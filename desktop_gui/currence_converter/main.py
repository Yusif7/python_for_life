from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests

"""
QVBoxLayout - add vertical layout from up to down 
QHBoxLayout - add layouts in horizontal line
"""


def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find('span', class_='ccOutputRslt').get_text()
    currency = currency[:-4]
    return currency


def currency_converter():
    # Access to our widgets in our application
    input_text = text.text()
    in_cur = in_combo.currentText()
    tar_cur = target_combo.currentText()
    rate = get_currency(in_cur, tar_cur)
    # Convert currency
    output = round(float(input_text) * float(rate), 2)
    message = f'{input_text} {in_cur} is {output} {tar_cur}'
    output_label.setText(str(message))


# Create instance of application
app = QApplication([])
# Create view window of application
window = QWidget()
window.setWindowTitle("Currency Converter")

# Create layout
layout = QVBoxLayout()

# Create horizontal layout
layout1 = QHBoxLayout()

# Add layout1 to layout
layout.addLayout(layout1)

# Create output label
output_label = QLabel('')
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)

# Input Currency dropdown list
in_combo = QComboBox()
currencies = ['USD', 'EUR', 'RUB', 'INR', 'TRY']
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

# Input Currency dropdown list
target_combo = QComboBox()
target_combo.addItems(currencies)
layout2.addWidget(target_combo)

# Create text layout
text = QLineEdit()
# Add text widget to layout
layout3.addWidget(text)

# Create button
btn = QPushButton("Convert")
# Attribute for control buttons place
layout3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
# btn - layout , clicked
btn.clicked.connect(currency_converter)

# Add layout widget to window
window.setLayout(layout)
window.show()
app.exec()
