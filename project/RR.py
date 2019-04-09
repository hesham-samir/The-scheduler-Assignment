from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot


class RRClass(QWidget):
    def __init__(self):
        super().__init__()
        self.queue = []
        self.b = QPushButton('Push Me')
        self.l = QLabel('I have not been clicked yet')
        self.x = QLabel("enter process time  : ")
        self.i = QLineEdit()
        self.tableWidget = QTableWidget()
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addWidget(self.x)
        v_box.addWidget(self.i)
        v_box.addWidget(self.b)
        v_box.addWidget(self.tableWidget)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.b.clicked.connect(self.btn_click)
        self.show()
    
    def btn_click(self):
        self.queue.append(int(self.i.text()))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["1                "])
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (0,1)"))
        print(self.queue)
        self.l.setText('I have been clicked')
