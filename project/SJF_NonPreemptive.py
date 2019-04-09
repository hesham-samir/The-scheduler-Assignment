from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel


class SJFNonPreemptiveClass(QWidget):
    def __init__(self):

        super().__init__()

        label = QLabel("/* implementation of SJFNonPreemptiveClass")

        ftablayout = QVBoxLayout()
        ftablayout.addWidget(label)

        self.setLayout(ftablayout)