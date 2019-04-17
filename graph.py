##############################################################################
#   module name : GraphClass                                                 #                           #
#   function : 1 - takes number of process at initialization                 #
#              2 - use add_bar function to add graph burst time              #
#                    - the function takes process number and burst tim       #
#                    - each process is assigned to unique random color       #
#                                                                            #
##############################################################################
import matplotlib.pyplot as plt
import matplotlib as mpl
import random


class GraphClass:
    # initializing the class by taking number of processes
    def __init__(self, processes_number):
        # list of unique color for each process (ie p1 has color colors_list[1], p2 has color colors_list[2], ........)
        self.colors_list = ['#ffffff']
        # list of all burst time required on graph
        # it should start with zero to start Gantt chart from zero, but it gives error;
        self.burst_list = [0.000000000001]
        # list of all processes in the Gantt chart
        self.processes_list = []
        # mapping random color for each process
        r = lambda: random.randint(0, 255)
        for i in range(processes_number):
            self.colors_list.append('#%02X%02X%02X' % (r(), r(), r()))

    def add_bar(self, processes_no, burst_time):
        last_burst_time = self.burst_list[-1]
        self.burst_list.append(burst_time + last_burst_time)
        self.processes_list.append(self.colors_list[processes_no])

    def get_color_list(self):
        return self.colors_list

    def plot_graph(self):
        fig, ax = plt.subplots(figsize=(6, 1))
        fig.subplots_adjust(bottom=0.5)

        cmap = mpl.colors.ListedColormap(self.processes_list)
        cmap.set_over('0.25')
        cmap.set_under('0.75')

        bounds = self.burst_list
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        cb2 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, boundaries=[0] + bounds + [13], extend='both', ticks=bounds, spacing='proportional',orientation='horizontal')
        cb2.set_label('Discrete intervals, some other units')
        plt.show()

    def reset(self):
        self.burst_list = []
        self.colors_list = ['#ffffff']
        self.processes_list = []
# testing graph
# p = GraphClass(3)
# p.add_bar(0,3)
# p.add_bar(1,3)
# p.add_bar(2,3)
# p.add_bar(0,3)
# p.add_bar(1,3)
# p.add_bar(2,3)
# p.plot_graph()
