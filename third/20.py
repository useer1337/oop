from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QApplication
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)

        layout = QVBoxLayout()
        layout.setSpacing(100)

        self.button = QPushButton()
        self.label = QLabel()
        self.label1 = QLabel()

        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.click)
        self.button.clicked.connect(self.click1)
        self.setLayout(layout)

    def click(self):
        self.label.setText('1 сигнал')

    def click1(self):
        self.label1.setText('2 сигнал')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
