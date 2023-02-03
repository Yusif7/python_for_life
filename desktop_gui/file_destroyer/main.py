from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


def open_files():
    global filenames
    # Select files from system
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select File')
    # Access to text area of widget
    message.setText('\n'.join(filenames))


def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            # Clear inside selecting files
            file.write(b'')
        path.unlink()
    message.setText('Destruction Successfully')

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")

layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. The files will be permanently deleted!')
layout.addWidget(description)

open_btn = QPushButton('Select files')
# Add comment in mouse over
open_btn.setToolTip('Select files')
# Change buttons size
open_btn.setFixedWidth(120)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton('Destroy files')
# Add comment in mouse over
destroy_btn.setToolTip('Destroy files')
# Change buttons size
destroy_btn.setFixedWidth(120)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel()
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()
