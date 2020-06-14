from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QApplication, QMenuBar, QListWidget, QComboBox

import sys

from third.person import Person


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        b = QPushButton('delete')
        b.clicked.connect(self.delete)

        self.list = QListWidget()

        names = ['Sasha','Masha','Pasha']

        self.list.addItems(names)
        self.list.itemClicked.connect(self.one_click)
        self.list.doubleClicked.connect(self.double_click)

        layout = QVBoxLayout()

        layout.addWidget(self.list)
        layout.addWidget(b)

        # combobox

        button = QPushButton('Получить возраст')
        button.clicked.connect(self.get_age)

        self.combo = QComboBox()
        self.combo.setEditable(True)

        person = Person('Sasha', 19)
        person1 = Person('Masha', 21)
        self.combo.addItem(person.get_name(),person)
        self.combo.addItem(person1.get_name(), person1)

        layout.addWidget(self.combo)
        layout.addWidget(button)

        self.setLayout(layout)

    def one_click(self):
        print("Нажали один раз")

    def double_click(self):
        print('Нажали 2 раза')

    def delete(self):
        items = self.list.selectedItems()
        for i in items:
            self.list.takeItem(self.list.row(i))

    def get_age(self):
        p = self.combo.currentData()
        print(p.get_age())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
