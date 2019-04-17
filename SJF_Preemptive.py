from PyQt5.QtWidgets import QVBoxLayout, QWidget, QErrorMessage, QMessageBox , QFrame, QLabel, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem
import graph
import process
from PyQt5 import QtGui

class SJFPreemptiveClass(QWidget):
    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("process"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Arrival Time"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Burst Time"))

        self.main_label = QLabel("SJF (Preemptive)")
        self.main_label.setFont(QtGui.QFont("sanserif", 30))
        self.main_label.setStyleSheet("color : #800000")

        self.TA = QLabel("")
        self.TA.setFont(QtGui.QFont("sanserif", 20))
        self.TA.setStyleSheet("color : #800000")

        self.WT = QLabel("")
        self.WT.setFont(QtGui.QFont("sanserif", 20))
        self.WT.setStyleSheet("color : #800000")

        self.plot_graph = 0
        self.colors_list = 0
        self.process_name_label = QLabel("Enter process name  : ")
        self.Process_name_input = QLineEdit()
        self.process_number_label = QLabel("Enter number of processes  : ")
        self.Process_number_input = QLineEdit()
        self.burst_time_label = QLabel("Enter burst time  : ")
        self.burst_time_input = QLineEdit()
        self.arrival_time_label = QLabel("Enter arrival time  : ")
        self.arrival_time_input = QLineEdit()

        self.add_btn = QPushButton('Add Process')
        self.plot_btn = QPushButton('Plot')
        self.back_btn = QPushButton('Back')
        self.process_number_added_btn = QPushButton('Next')

        self.count = 0
        self.sorted_list = process.processList()

        self.h_box1 = QHBoxLayout()
        self.h_box1.addStretch()
        self.h_box1.addWidget(self.add_btn)
        self.h_box1.addStretch()

        self.h_box3 = QHBoxLayout()
        self.main_init()

        self.h_box4 = QHBoxLayout()
        self.h_box4.addStretch()
        self.h_box4.addWidget(self.plot_btn)
        self.h_box4.addStretch()

        self.h_box5 = QHBoxLayout()
        self.h_box5.addStretch()
        self.h_box5.addWidget(self.process_number_added_btn)
        self.h_box5.addStretch()

        self.h_box_back = QHBoxLayout()
        self.h_box_back.addStretch()
        self.h_box_back.addWidget(self.back_btn)
        self.h_box_back.addStretch()

        self.v_box1 = QVBoxLayout()
        self.v_box1.addLayout(self.h_box3)

        self.v_box1.addWidget(self.process_number_label)
        self.v_box1.addWidget(self.Process_number_input)

        self.v_box1.addWidget(self.process_name_label)
        self.v_box1.addWidget(self.Process_name_input)

        self.v_box1.addWidget(self.burst_time_label)
        self.v_box1.addWidget(self.burst_time_input)

        self.v_box1.addWidget(self.arrival_time_label)
        self.v_box1.addWidget(self.arrival_time_input)
        self.v_box1.addLayout(self.h_box1)
        self.v_box1.addLayout(self.h_box4)
        self.v_box1.addLayout(self.h_box5)
        self.v_box1.addLayout(self.h_box_back)
        self.v_box1.addWidget(self.tableWidget)
        self.v_box1.addWidget(self.TA)
        self.v_box1.addWidget(self.WT)
        self.v_box1.addStretch()
        self.setLayout(self.v_box1)
        self.show_process_number_input()

        self.add_btn.clicked.connect(self.add_btn_click)
        self.plot_btn.clicked.connect(self.plot_btn_click)
        self.back_btn.clicked.connect(self.back_btn_click)
        self.process_number_added_btn.clicked.connect(self.process_number_added_btn_click)

        self.show()

    def main_init(self):
        self.h_box3.addStretch()
        self.h_box3.addWidget(self.main_label)
        self.h_box3.addStretch()

    def add_btn_click(self):
        if self.arrival_time_input.text().isdigit() and self.burst_time_input.text().isdigit() and self.count < int(
                self.Process_number_input.text()):
            self.sorted_list.insert(self.Process_name_input.text(), int(self.arrival_time_input.text()), 0,
                                    int(self.burst_time_input.text()))
            print(self.sorted_list)
            self.count = self.count + 1
            for row in range(self.count):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(self.sorted_list.list[row].name))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(self.sorted_list.list[row].arrival)))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(self.sorted_list.list[row].burst)))
                self.tableWidget.item(row, 0).setBackground(QtGui.QColor(self.colors_list[row + 1]))
        elif self.count >= int(self.Process_number_input.text()):
            self.show_error("You reached the limit of process")
        else:
            self.show_error("enter valid data")

    def back_btn_click(self):
        self.sorted_list.delete()
        self.count = 0
        self.show_process_number_input()
        self.tableWidget.clear()
        self.TA.setText("")
        self.WT.setText("")

    def process_number_added_btn_click(self):
        if self.Process_number_input.text().isdigit() and int(self.Process_number_input.text()) > 0:
            self.show_main()
        else:
            self.show_error("please enter valid data")

    def show_main(self):
        self.process_name_label.show()
        self.Process_name_input.show()
        self.process_number_label.hide()
        self.Process_number_input.hide()
        self.burst_time_label.show()
        self.burst_time_input.show()
        self.arrival_time_label.show()
        self.arrival_time_input.show()
        self.add_btn.show()
        self.plot_btn.show()
        self.back_btn.show()
        self.tableWidget.show()
        self.TA.show()
        self.WT.show()
        self.process_number_added_btn.hide()
        self.plot_graph = graph.GraphClass(int(self.Process_number_input.text()) + 1)
        self.colors_list = self.plot_graph.get_color_list()
        self.tableWidget.setRowCount(int(self.Process_number_input.text()))

    def show_process_number_input(self):
        self.process_name_label.hide()
        self.Process_name_input.hide()
        self.process_number_label.show()
        self.Process_number_input.show()
        self.burst_time_label.hide()
        self.burst_time_input.hide()
        self.arrival_time_label.hide()
        self.arrival_time_input.hide()
        self.add_btn.hide()
        self.plot_btn.hide()
        self.back_btn.hide()
        self.tableWidget.hide()
        self.TA.hide()
        self.WT.hide()
        self.process_number_added_btn.show()

    def plot_btn_click(self):
        if self.count == int(self.Process_number_input.text()):
            self.sorted_list.SJF_P_Sort()
            no = self.sorted_list.processes_ids
            bursts = self.sorted_list.processes_bursts
            for i in range(0, len(no)):
                self.plot_graph.add_bar(no[i], bursts[i])
            self.TA.setText("average TAT:" + str(self.sorted_list.ta_time_avg))
            self.WT.setText("average WT:" + str(self.sorted_list.wt_time_avg))
            self.plot_graph.plot_graph()
        else:
            self.show_error("please enter remaining process")

    def show_error( self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
