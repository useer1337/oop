import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QApplication, QLayout, QLineEdit, QVBoxLayout, QPushButton, QTextEdit


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.line = QLineEdit()
        self.line.textChanged.connect(self.text_change)

        self.text = QTextEdit()

        self.text.setDisabled(True)

        self.line.setValidator(QRegExpValidator(QRegExp(r"^[A-Za-z]*$")))
        # self.line.setEchoMode(QLineEdit.Password)
        self.line.setMaxLength(6)

        b = QPushButton('click')
        b1 = QPushButton('click1')
        b.clicked.connect(self.push)
        b1.clicked.connect(self.push1)

        layout = QVBoxLayout()
        layout.addWidget(self.line)
        layout.addWidget(self.text)
        layout.addWidget(b)
        layout.addWidget(b1)

        self.setLayout(layout)

    def push(self):
        print(self.line.text())

    def push1(self):
        print(self.text.toPlainText())

    def text_change(self):
        print('TextChanged')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()