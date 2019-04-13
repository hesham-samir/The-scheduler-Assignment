from PyQt5.QtWidgets import QVBoxLayout, QWidget, QFrame, QLabel, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem
import graph
import process
from PyQt5 import QtGui

class RRClass(QWidget):
    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("process"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Arrival Time"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Burst Time"))


        self.main_label = QLabel("Round Robin")
        self.main_label.setFont(QtGui.QFont("sanserif", 30))
        self.main_label.setStyleSheet("color : #800000")
        self.process_name_label = QLabel("Enter process name  : ")
        self.Process_name_input = QLineEdit()
        self.burst_time_label = QLabel("Enter burst time  : ")
        self.burst_time_input = QLineEdit()
        self.arrival_time_label = QLabel("Enter arrival time  : ")
        self.arrival_time_input = QLineEdit()
        self.quantum_time_label = QLabel("Enter Quantum time  : ")
        self.quantum_time_input = QLineEdit()

        self.next_btn = QPushButton('Next')
        self.add_btn = QPushButton('Add Process')
        self.plot_btn = QPushButton('Plot')
        self.back_btn = QPushButton('Back')

        self.count = 0
        self.sorted_list = process.processList()

        self.h_box1 = QHBoxLayout()
        self.h_box1.addStretch()
        self.h_box1.addWidget(self.add_btn)
        self.h_box1.addStretch()

        self.h_box2 = QHBoxLayout()
        self.h_box2.addStretch()
        self.h_box2.addWidget(self.next_btn)
        self.h_box2.addStretch()

        self.h_box3 = QHBoxLayout()
        self.main_init()

        self.h_box4 = QHBoxLayout()
        self.h_box4.addStretch()
        self.h_box4.addWidget(self.plot_btn)
        self.h_box4.addStretch()

        self.h_box_back = QHBoxLayout()
        self.h_box_back.addStretch()
        self.h_box_back.addWidget(self.back_btn)
        self.h_box_back.addStretch()

        self.v_box1 = QVBoxLayout()
        self.v_box1.addLayout(self.h_box3)
        self.v_box1.addWidget(self.process_name_label)
        self.v_box1.addWidget(self.Process_name_input)

        self.v_box1.addWidget(self.burst_time_label)
        self.v_box1.addWidget(self.burst_time_input)

        self.v_box1.addWidget(self.arrival_time_label)
        self.v_box1.addWidget(self.arrival_time_input)
        self.v_box1.addWidget(self.quantum_time_label)
        self.v_box1.addWidget(self.quantum_time_input)
        self.v_box1.addLayout(self.h_box1)
        self.v_box1.addLayout(self.h_box2)
        self.v_box1.addLayout(self.h_box4)
        self.v_box1.addLayout(self.h_box_back)
        self.v_box1.addWidget(self.tableWidget)
        self.v_box1.addStretch()
        self.setLayout(self.v_box1)
        self.show_main()

        self.next_btn.clicked.connect(self.next_btn_click)
        self.add_btn.clicked.connect(self.add_btn_click)
        self.plot_btn.clicked.connect(self.plot_btn_click)
        self.back_btn.clicked.connect(self.back_btn_click)
        self.show()

    def main_init(self):
        self.h_box3.addStretch()
        self.h_box3.addWidget(self.main_label)
        self.h_box3.addStretch()

    def add_btn_click(self):
        self.sorted_list.insert(self.Process_name_input.text(), int(self.arrival_time_input.text()),0, int(self.burst_time_input.text()))
        print(self.sorted_list)
        self.count = self.count + 1

    def next_btn_click(self):
        self.show_next()


    def back_btn_click(self):
        self.show_main()


    def show_next(self):
        self.process_name_label.hide()
        self.Process_name_input.hide()
        self.burst_time_label.hide()
        self.burst_time_input.hide()
        self.arrival_time_label.hide()
        self.arrival_time_input.hide()
        self.quantum_time_label.show()
        self.quantum_time_input.show()
        self.next_btn.hide()
        self.add_btn .hide()
        self.plot_btn.show()
        self.back_btn.show()
        self.tableWidget.show()

    def show_main(self):
        self.process_name_label.show()
        self.Process_name_input.show()
        self.burst_time_label.show()
        self.burst_time_input.show()
        self.arrival_time_label.show()
        self.arrival_time_input.show()
        self.quantum_time_label.hide()
        self.quantum_time_input.hide()
        self.next_btn.show()
        self.add_btn .show()
        self.plot_btn.hide()
        self.back_btn.hide()
        self.tableWidget.hide()

    def plot_btn_click(self):
        plot_graph = graph.GraphClass(self.count + 1)
        colors_list = plot_graph.get_color_list()
        self.tableWidget.setRowCount(self.count)
        for row in range(self.count):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(self.sorted_list.list[row].name))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(self.sorted_list.list[row].arrival)))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(self.sorted_list.list[row].burst)))
            self.tableWidget.item(row, 0).setBackground(QtGui.QColor(colors_list[row + 1]))

        self.sorted_list.RR_sort(int(self.quantum_time_input.text()))
        no = self.sorted_list.processes_ids
        bursts = self.sorted_list.processes_bursts
        for i in range(0, len(no)):
            plot_graph.add_bar(no[i], bursts[i])

        plot_graph.plot_graph()
