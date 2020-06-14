from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QLayout, QApplication, QVBoxLayout, QGroupBox, QRadioButton
import sys


class Wimdow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.label = QLabel('Text')
        self.label1 = QLabel('Text1')

        self.box = QGroupBox()
        self.check = QCheckBox('check1')
        self.check1 = QCheckBox('check2')

        self.check.setChecked(True)
        self.check.stateChanged.connect(self.check_func)

        self.box_layout = QVBoxLayout()
        self.box_layout.addWidget(self.check)
        self.box_layout.addWidget(self.check1)

        self.box.setLayout(self.box_layout)

        # radiobutton
        self.radio1 = QRadioButton('radio1')
        self.radio2 = QRadioButton('radio2')

        self.radio1.toggled.connect(self.radio_func)

        box1 = QGroupBox()
        layout_box1 = QVBoxLayout()

        layout_box1.addWidget(self.radio1)
        layout_box1.addWidget(self.radio2)

        box1.setLayout(layout_box1)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.box)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(box1)

        self.setLayout(self.layout)

    def check_func(self, i: int):
        self.label.setText(str(i))

    def radio_func(self, bool):
        self.label1.setText(str(bool))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wimdow = Wimdow()
    wimdow.show()
    app.exec_()
