import sys
import requests

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1200,800)
        self.setWindowTitle('Line Edit Tutorial')
        self.UI()
    def UI(self):
        vbox = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(100)
        self.slider.setMinimum(1)
        self.slider.setRange(10, 100)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.valueChanged.connect(self.getValueFromSliderChange)
        self.text1 = QLabel("0")
        self.text1.setAlignment(Qt.AlignCenter)
        self.text2 = QLabel("Hello")

        vbox.addStretch()
        vbox.addWidget(self.text1)
        vbox.addWidget(self.text2)
        vbox.addWidget(self.slider)

        self.setLayout(vbox)

        self.show()

    def getValueFromSliderChange(self):
        value = self.slider.value()
        print(value)
        self.text1.setText(str(value))
        fontSize = self.slider.value()
        font = QFont('Times', fontSize)
        self.text2.setFont(font)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()