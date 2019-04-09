from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel


class FCFSClass(QWidget):
    def __init__(self):

        super().__init__()

        label = QLabel("/* implementation of FCFS")

        ftablayout = QVBoxLayout()
        ftablayout.addWidget(label)

        self.setLayout(ftablayout)