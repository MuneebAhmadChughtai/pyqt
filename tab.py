import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1200,800)
        self.setWindowTitle('Line Edit Tutorial')
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "First Tab")
        self.tabs.addTab(self.tab2, "2nd Tab")
        self.tabs.addTab(self.tab3, "3rd Tab")
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.text = QLabel("Hello Python")
        self.btn1 = QPushButton("First Tab")
        self.btn1.clicked.connect(self.changeText)
        self.btn2 = QPushButton("2nd Tab")

        vbox.addWidget(self.text)
        vbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)

        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

        self.show()

    def changeText(self):
        self.text.setText("Hello EveryOne!!!!!")



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()