from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

"""
QVBoxLayout - add vertical layout from up to down 
QHBoxLayout - add layouts in horizontal line
"""


def make_sentence():
    # Text extract from text layout
    input_text = text.text()
    # Add to our output(result) the ending format of inputting text
    output_label.setText(input_text.capitalize())
    if input_text[-1] != '.':
        output_label.setText(input_text + '.')


# Create instance of application
app = QApplication([])
# Create view window of application
window = QWidget()
window.setWindowTitle("Sentence Maker")

# Create layout
layout = QVBoxLayout()

# Create text layout
text = QLineEdit()
# Add text widget to layout
layout.addWidget(text)

# Create button
btn = QPushButton("Submit")
layout.addWidget(btn)
# btn - layout , clicked
btn.clicked.connect(make_sentence)

# Create output label(result)
output_label = QLabel('')
layout.addWidget(output_label)

# Add layout widget to window
window.setLayout(layout)
window.show()
app.exec()
