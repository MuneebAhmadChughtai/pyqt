import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle('Labels Tutorial')

        self.UI()

    def UI(self):
        text1 = QLabel('Text 1', self)
        text2 = QLabel('Text 2', self)

        text1.move(50, 50)
        text2.move(200, 50)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
