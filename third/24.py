from PyQt5.QtGui import QPicture, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QApplication, QToolBar, QAction
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        layout = QVBoxLayout()

        self.button = QPushButton()
        self.button.setText("click")

        pixmap = QPixmap('bob.png')
        icon = QIcon(pixmap)
        self.button.setIcon(icon)

        self.label = QLabel()

        self.toolbar = QToolBar()
        tool = QAction(QIcon('bob.png'),'text',self)

        self.toolbar.addAction(tool)
        tool.triggered.connect(self.tool_click)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.click)
        self.setLayout(layout)

    def click(self):
        self.label.setText('Hello')

    def tool_click(self):
        self.label.setText('toolbar clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
