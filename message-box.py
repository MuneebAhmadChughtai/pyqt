import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle('checkbox Tutorial')
        self.UI()

    def UI(self):
        button = QPushButton('exit', self)
        button.move(300, 400)
        button.clicked.connect(self.handleExit)
        self.show()

    def handleExit(self):
        mbox = QMessageBox.information(self,"Information","Are you sure you want to exit??")
        if mbox == QMessageBox.Yes:
            sys.exit()
        elif mbox == QMessageBox.No:
            print("You clicked No")



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()