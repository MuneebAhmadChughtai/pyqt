import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 16)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle('checkbox Tutorial')
        self.UI()

    def UI(self):
        self.spinbox = QSpinBox(self)
        self.spinbox.move(300,300)
        self.spinbox.setFont(font)
        # self.spinbox.setMinimum(1)
        # self.spinbox.setMaximum(100)
        self.spinbox.setRange(10,110)
        # self.spinbox.valueChanged.connect(self.getValue)
        button = QPushButton('Send', self)
        button.move( 300, 500 )
        button.clicked.connect(self.getValue)
        self.show()

    def getValue(self):
        value = self.spinbox.value()
        print(value)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
