import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle('checkbox Tutorial')
        self.UI()

    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(300,300)
        self.editor.setAcceptRichText(False)
        button = QPushButton("Submit", self)
        button.move(300,600)
        button.clicked.connect(self.getValue)
        self.show()

    def getValue(self):
        text = self.editor.toPlainText()
        print(text)



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
