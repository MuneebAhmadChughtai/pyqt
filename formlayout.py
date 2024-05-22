from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Form Layout')
        self.setGeometry(100,100, 800, 800)
        self.UI()


    def UI(self):
        formlayout = QFormLayout()
        # formlayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        name_text = QLabel("Name :")
        name_input = QLineEdit()
        password_text = QLabel("Password :")
        password_input = QLineEdit()
        countriesCombo = QComboBox()
        countriesCombo.addItems(["USA", "Germany"])
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())

        formlayout.addRow(name_text, hbox1)
        formlayout.addRow(password_text, password_input)
        formlayout.addRow("Country :",countriesCombo )
        formlayout.addRow(hbox)

        self.setLayout(formlayout)

        self.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()





