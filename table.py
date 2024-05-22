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
        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton("GET")
        self.table.setColumnCount(3)
        self.table.setRowCount(5)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem("Age"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem("Address"))
        self.table.setItem(0,0,QTableWidgetItem("Item at position 0,0"))
        self.table.setItem(0,1,QTableWidgetItem("Item at position 0,1"))
        self.table.setItem(1,0,QTableWidgetItem("Item at position 1,0"))
        self.table.setItem(4,2,QTableWidgetItem("Item at position 4,4"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.doubleClicked.connect(self.doubleClick)
        btn.clicked.connect(self.getValues)
        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        vbox.addWidget(btn)
        self.setLayout(vbox)
        self.show()

    def getValues(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

    def doubleClick(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())





def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()