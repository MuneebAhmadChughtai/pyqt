import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle('This is the window title')
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
