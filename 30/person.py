import sys

from PyQt5.QtCore import QAbstractItemModel, Qt, QAbstractListModel, QAbstractTableModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QApplication, QTableView


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonModel(QAbstractTableModel):
    def __init__(self, persons, *args, **kwargs):
        super(PersonModel, self).__init__(*args, **kwargs)
        self.persons = persons or []  # список людей

    def rowCount(self, index):
        return len(self.persons)

    def columnCount(self, index):
        return 2

    def data(self, index, role):
        # role - это то как будут пердоставляться данные(DisplayRole - в видет текста)
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return self.persons[index.row()].name
            if index.column() == 1:
                return self.persons[index.row()].age


class PersonModelList(QAbstractListModel):
    def __init__(self, persons, *args, **kwargs):
        super(PersonModelList, self).__init__(*args, **kwargs)
        self.persons = persons or []  # список людей

    def rowCount(self, index):
        return len(self.persons)

    def data(self, index, role):
        # role - это то как будут пердоставляться данные(DisplayRole - в видет текста)
        if role == Qt.DisplayRole:
            name = self.persons[index.row()].name
            age = str(self.persons[index.row()].age)
            return name + " " + age


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setFixedSize(300, 250)

        layout = QVBoxLayout()

        persons = [Person('Sasha', 20), Person('Masha', 21)]

        model = PersonModel(persons)
        tabel = QTableView()
        tabel.setModel(model)

        # second model
        model1 = PersonModelList(persons)
        list = QListView()
        list.setModel(model1)

        layout.addWidget(tabel)
        layout.addWidget(list)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
