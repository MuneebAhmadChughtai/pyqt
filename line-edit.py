import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800,800)
        self.setWindowTitle('Line Edit Tutorial')
        self.UI()
    def UI(self):
        self.userNamelineEdit = QLineEdit(self)
        self.userNamelineEdit.setPlaceholderText('Enter UserName')
        self.userNamelineEdit.move(120,50)
        self.passwordlineEdit = QLineEdit(self)
        self.passwordlineEdit.setPlaceholderText('Enter Password')
        self.passwordlineEdit.setEchoMode(QLineEdit.Password)
        self.passwordlineEdit.move(120,100)
        submitButton = QPushButton('Submit', self)
        submitButton.move(120, 140)
        submitButton.clicked.connect(self.handleSubmit)
        self.show()


    def handleSubmit(self):
        userName = self.userNamelineEdit.text()
        password = self.passwordlineEdit.text()
        self.setWindowTitle("Welcome :" + userName + "you password is" + password )


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()