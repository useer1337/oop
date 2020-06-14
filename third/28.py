import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QTableWidget, QPushButton, QLineEdit, QComboBox

from third.person import Person


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        layout = QVBoxLayout()

        button = QPushButton('click')
        self.combo = QComboBox()

        person = Person('sasha',19)
        person1 = Person('masha', 21)

        self.combo.addItem(person.name,person)
        self.combo.addItem(person1.name,person1)


        button.clicked.connect(self.get_age)

        self.table = QTableWidget(1,2)
        self.table.setCellWidget(0,0,self.combo)
        self.table.setCellWidget(0,1,button)

        layout.addWidget(self.table)

        self.setLayout(layout)

    def get_age(self):
        print(self.combo.currentData().age)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
