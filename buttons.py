import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle('Labels Tutorial')

        self.UI()

    def UI(self):
        self.text= QLabel('Hello', self)
        enterButton = QPushButton('enter', self)
        exitButton = QPushButton('Exit', self)
        enterButton.move(50, 50)
        exitButton.move(200, 50)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    def enterFunc(self):
        self.text.setText('Enter clicked')
        self.text.resize(200, 40)

    def exitFunc(self):
        self.text.setText('Exit Clicked')
        self.text.resize(200,40)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
