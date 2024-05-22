import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle('checkbox Tutorial')
        self.UI()

    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(300, 300)
        self.combo.addItem('1')
        self.combo.addItems(['1', '2', '3'])
        list1 = ['4', '5', '6']

        for i in list1:
            self.combo.addItem(i)

        for i in range(7, 20):
            self.combo.addItem(str(i))

        button = QPushButton('print', self)
        button.move(300, 400)
        button.clicked.connect(self.handleSubmit)
        self.show()

    def handleSubmit(self):
        print(self.combo.currentText())


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
