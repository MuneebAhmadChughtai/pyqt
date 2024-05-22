import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle('checkbox Tutorial')
        self.UI()

    def UI(self):
        self.male = QRadioButton('Male', self)
        self.male.move(200,200)
        self.female = QRadioButton('Female', self)
        self.female.move(200, 300)
        self.male.setChecked(True)

        button = QPushButton('Submit', self)
        button.move(300, 400)
        button.clicked.connect(self.handleSubmit)
        self.show()

    def handleSubmit(self):
        if self.male.isChecked():
            print(self.male.text())
        else:
            print(self.female.text())

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
