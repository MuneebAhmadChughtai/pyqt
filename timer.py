import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle('checkbox Tutorial')
        self.UI()

    def UI(self):
        self.colorLabel = QLabel(self)
        self.colorLabel.resize(250, 250)
        self.colorLabel.setStyleSheet('background-color: green')
        self.colorLabel.move(200,200)
        startButton = QPushButton('Start', self)
        startButton.move(500, 450)
        startButton.clicked.connect(self.start)
        stopButton = QPushButton('Stop', self)
        stopButton.move(400,450)
        stopButton.clicked.connect(self.stop)

        self.timer = QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.colorChange)
        self.value = 0
        self.show()

    def colorChange(self):
        if self.value == 0:
            self.colorLabel.setStyleSheet('background-color:yellow')
            self.value = 1
        else:
            self.colorLabel.setStyleSheet('background-color: green')
            self.value = 0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
