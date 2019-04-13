from PyQt5.QtWidgets import QVBoxLayout, QWidget,QFrame, QLabel, QLineEdit, QPushButton, QHBoxLayout, QGridLayout,QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QRect

class RRClass(QWidget):
    def __init__(self):
        super().__init__()
        self.queue = []
        self.add_btn = QPushButton('add process')
        self.label = QLabel('I have not been clicked yet')
        self.x = QLabel("enter process time  : ")
        self.i = QLineEdit()
        self.tableWidget = QTableWidget()
        self.plot_btn = QPushButton('plot')
        self.count = 0;


        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.label)
        h_box.addStretch()

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.x)
        self.v_box.addWidget(self.i)
        self.v_box.addWidget(self.add_btn)
        self.v_box.addStretch()
        self.v_box.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.v_box)

        self.add_btn.clicked.connect(self.add_btn_click)
        self.show()

    def add_btn_click(self):
        self.queue.append(int(self.i.text()))
        print(self.queue)
        self.count = self.count + 1
        self.label.setText('I have been clicked')
        added = QPushButton('p'+str(self.count))
        self.v_box.addWidget(added)

