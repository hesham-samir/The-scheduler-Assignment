from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel


class PriorityNonPreemptiveClass(QWidget):
    def __init__(self):

        super().__init__()

        label = QLabel("/* implementation of PriorityNonPreemptiveClass")

        ftablayout = QVBoxLayout()
        ftablayout.addWidget(label)

        self.setLayout(ftablayout)