import sys
import requests

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *

image = QImage()
image.loadFromData(requests.get('https://images.deliveryhero.io/image/darsktores-pk/8964000834749.jpg?height=480').content)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1200,800)
        self.setWindowTitle('Line Edit Tutorial')
        self.UI()
    def UI(self):
        self.image = QLabel(self)
        # self.image.setPixmap(QPixmap('./images/logo.png'))
        # self.image.setPixmap(QPixmap('https://images.deliveryhero.io/image/darsktores-pk/8964000834749.jpg'))
        self.image.setPixmap(QPixmap(image))
        self.image.move(100,100)
        removeButton = QPushButton('Remove', self)
        removeButton.move(100, 600)
        showButton = QPushButton('Show', self)
        showButton.move(200, 600)
        removeButton.clicked.connect(self.removeImage)
        showButton.clicked.connect(self.showImage)

        self.show()

    def removeImage(self):
        self.image.close()
    def showImage(self):
        self.image.show()



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()