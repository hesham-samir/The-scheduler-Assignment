from PyQt5.QtWidgets import QMainWindow,QDialog,QApplication , QListWidget, QCheckBox ,QComboBox, QGroupBox ,QDialogButtonBox , QVBoxLayout , QFrame,QTabWidget, QWidget, QLabel, QLineEdit
import sys
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
import RR
import FCFS
import SJF_NonPreemptive
import SJF_Preemptive
import Priority_NonPreemptive
import Priority_Preemptive


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'The scheduler Assignment'
        self.left = 300
        self.top = 60
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("home.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = TabDialog()
        self.setCentralWidget(self.table_widget)

        self.show()


class TabDialog(QDialog):
    def __init__(self):
        super().__init__()

        tabwidget = QTabWidget()
        tabwidget.addTab(RR.RRClass(), "RR")
        tabwidget.addTab(FCFS.FCFSClass(), "FCFS")
        tabwidget.addTab(SJF_Preemptive.SJFPreemptiveClass(), "SJF Preemptive")
        tabwidget.addTab(SJF_NonPreemptive.SJFNonPreemptiveClass(), "SJF Non Preemptive")
        tabwidget.addTab(Priority_Preemptive.PriorityPreemptiveClass(), "Priority Preemptive")
        tabwidget.addTab(Priority_NonPreemptive.PriorityNonPreemptiveClass(), "Priority Non Preemptive")

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(tabwidget)

        self.setLayout(vboxLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())