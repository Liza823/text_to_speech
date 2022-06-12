import pyttsx3
engine = pyttsx3.init()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit
app = QApplication([])
win = QWidget()
win.setWindowTitle("мое окно")
win.move(300, 20)
win.resize(500,500)
win.show()
v_line = QVBoxLayout()
win.setLayout(v_line)
text = QTextEdit()
v_line.addWidget(text)

button = QPushButton("Cказать")
v_line.addWidget(button, alignment = Qt.AlignCenter)
def say():
    texttosay = text.toPlainText()
    engine.say(texttosay)
    engine.runAndWait()
button.clicked.connect(say)
app.exec_()