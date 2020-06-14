import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QAction, QWidget, QDialog, \
    QLineEdit, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('main_window')
        self.resize(300, 150)
        self.setFixedSize(300, 150)

        self.statusBar().showMessage('StatusBar')

        menu = self.menuBar().addMenu('Menu')

        say_menu = menu.addMenu('Say')
        say_menu.addAction('Hello')
        say_menu.addAction('GoodBay')

        say_menu.triggered.connect(self.say)

        action = QAction('modal_dialog', self)

        action.triggered.connect(self.dialog)

        action_menu = self.menuBar().addMenu('Action')
        action_menu.addAction(action)

        # add widget
        button = QPushButton('message_box')
        button.clicked.connect(self.msg_box)

        layout = QVBoxLayout()
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        # qdialog
        self.modal_dialog = QDialog()
        self.modal_dialog.setWindowTitle('modal_dialog')
        self.modal_dialog.setModal(True)

        self.line = QLineEdit()

        b = QPushButton('yes')

        b.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.line)
        layout.addWidget(b)
        self.modal_dialog.setLayout(layout)

        self.modal_dialog.accepted.connect(self.accepted)

    def msg_box(self):
        msg = QMessageBox()
        msg.setText('message_box')
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('message_box')
        msg.exec()

    def accepted(self):
        print('acepted')

    def close(self):
        print(self.line.text())
        self.modal_dialog.accept()

    def dialog(self):
        self.modal_dialog.show()

    def say(self, action):
        print(action.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
