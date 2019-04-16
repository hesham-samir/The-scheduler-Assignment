from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel


class PriorityPreemptiveClass(QWidget):
    def __init__(self):

        super().__init__()

        label = QLabel("/* implementation of PriorityPreemptiveClas")

        ftablayout = QVBoxLayout()
        ftablayout.addWidget(label)

        self.setLayout(ftablayout)