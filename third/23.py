from PyQt5.QtGui import QPicture, QPixmap, QMovie, QPalette, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QApplication
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        layout = QVBoxLayout()

        self.label = QLabel()

        self.button_text = QPushButton("Текст")
        self.button_picture = QPushButton("Картинка")
        self.button_movie = QPushButton("Гифка")

        layout.addWidget(self.label)
        layout.addWidget(self.button_text)
        layout.addWidget(self.button_picture)
        layout.addWidget(self.button_movie)

        self.button_text.clicked.connect(self.text)
        self.button_picture.clicked.connect(self.picture)
        self.button_movie.clicked.connect(self.movie)
        self.setLayout(layout)

    def text(self):
        font = QFont('sans-serif', 100)
        self.label.setText('Text')
        self.label.setStyleSheet('color:green')
        self.label.setFont(font)

    def picture(self):
        picture = QPixmap('bob.png')
        self.label.setPixmap(picture.scaled(100, 100))

    def movie(self):
        movie = QMovie('RNSD.gif')
        self.label.setMovie(movie)
        movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
