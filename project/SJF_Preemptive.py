from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel


class SJFPreemptiveClass(QWidget):
    def __init__(self):

        super().__init__()

        label = QLabel("/* implementation of SJFPreemptiveClass")

        ftablayout = QVBoxLayout()
        ftablayout.addWidget(label)

        self.setLayout(ftablayout)