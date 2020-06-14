import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QWidget, QApplication, QFileSystemModel, QListView, QVBoxLayout


class Main(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.setFixedSize(300, 250)

        layout = QVBoxLayout()

        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())

        list = QListView()
        list.setModel(model)
        list.setRootIndex(model.index(QDir.rootPath()))  # фильтруем данные из модели!!!

        layout.addWidget(list)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()
