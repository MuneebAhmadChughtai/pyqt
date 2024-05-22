import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800,800)
        self.setWindowTitle('checkbox Tutorial')
        self.UI()
    def UI(self):
        self.firstName = QLineEdit(self)
        self.firstName.setPlaceholderText('First Name')
        self.firstName.move(200,200)
        self.lastName = QLineEdit(self)
        self.lastName.setPlaceholderText('Last Name')
        self.lastName.move(200,250)
        self.remember = QCheckBox("required",self)
        self.remember.move(200, 300)
        submitButton = QPushButton('Submit', self)
        submitButton.move(200, 350)
        submitButton.clicked.connect(self.handleSubmit)
        self.show()

    def handleSubmit(self):

        firstName = self.firstName.text()
        lastName = self.lastName.text()

        if self.remember.isChecked():
            self.setWindowTitle(firstName + " " + lastName + "has checked remember")
        else:
            self.setWindowTitle(firstName + " " + lastName + " has not checked remember" )

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()