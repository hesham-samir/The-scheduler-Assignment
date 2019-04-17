class processClass:
    def __init__(self, name, arrival, priority=0, burst=0):
        self.name = name
        self.arrival = arrival
        self.priority = priority
        self.burst = burst

    def stringify(self):
        return '('+str(self.name)+','+str(self.arrival)+','+str(self.priority)+','+str(self.burst)+')'+"\n"

def csort(p):
    return p.arrival

class processList():
    def __init__(self):
        self.list=[]

        self.processes_ids = []
        self.processes_bursts = []
        self.wt_time_avg = 0
        self.ta_time_avg = 0

    def get_list(self):
        return self.list

    def insert(self, name, arrival, priority, burst):
        p = processClass(name, arrival, priority, burst)
        self.list.append(p)
        self.list.sort(key=csort)

    def __str__(self):
        ls = ""
        for p in self.list:
            ls += p.stringify()
        return ls

    def is_finished(self):
        flag = 1
        for p in self.list:
            if p.burst > 0:
                flag = 0
        return flag

    def RR_sort(self, quantum_time):
        i = 0
        ta_time = []
        wt_time = []
        burst = []
        for k in range(len(self.list)):
            burst.insert(k, self.list[k].burst)
        while self.is_finished() == 0:
            no_process_at_time = 1
            for index in range(len(self.list)):
                if self.list[index].burst == 0:
                    continue
                elif self.list[index].arrival <= i:
                    if self.list[index].burst > quantum_time:
                        i = i + quantum_time
                        self.list[index].burst = self.list[index].burst - quantum_time
                        self.processes_ids.append(index + 1)
                        self.processes_bursts.append(quantum_time)
                        no_process_at_time = 0
                    else:
                        i = i + self.list[index].burst
                        self.processes_ids.append(index + 1)
                        self.processes_bursts.append(self.list[index].burst)
                        ta_time.insert(index, i - self.list[index].arrival)
                        self.list[index].burst = 0
                        no_process_at_time = 0
            if no_process_at_time:
                i = i + 1
                self.processes_ids.append(0)
                self.processes_bursts.append(1)
        for j in range (len(self.list)):
                wt_time.insert(j,ta_time[j] - burst[j])
        self.ta_time_avg = sum(ta_time) / len(self.list)
        self.wt_time_avg = sum(wt_time) / len(self.list)

    def nonPreemptivePriority_sort(self):
        wt_time = 0
        turnaround_time = 0
        time = self.list[0].arrival
        for i in range(0, len(self.list)):
            for j in range(i + 1, len(self.list)):
                if self.list[j].arrival <= time:
                    if self.list[j].priority < self.list[i].priority:
                        self.list[j], self.list[i] = self.list[i], self.list[j]
            time += self.list[i].burst
            turnaround_time = time - self.list[i].arrival
            wt_time = wt_time + (turnaround_time - self.list[i].burst)
            self.ta_time_avg = (self.ta_time_avg + turnaround_time) / len(self.list)
        self.wt_time_avg = wt_time / len(self.list)
        #print(wt_time/len(self.list))

    def priority_graph(self):
        current_time = 0
        i = 0

        while i < len(self.list):
            if self.list[i].arrival <= current_time:
                self.processes_ids.append(i + 1)
                self.processes_bursts.append(self.list[i].burst)
                current_time = current_time + self.list[i].burst
                i = i + 1
            else:
                self.processes_ids.append(0)
                self.processes_bursts.append(1)
                current_time = current_time + 1

    def FCFS_sort(self):
        time = 0
        while self.is_finished() == 0:
            for index in range(len(self.list)):
                if self.list[index].burst == 0:
                    continue
                elif self.list[index].arrival == 0:
                    self.processes_ids.append(index + 1)
                    self.processes_bursts.append(self.list[index].burst)
                else:
                    self.processes_ids.append(0)
                    self.processes_bursts.append(1)

    def delete(self):
        self.list = []
        self.processes_ids = []
        self.processes_bursts = []

    def SJF_NP_Sort(self):
        i = 0
        current_time = 0
        first_time = 1
        no_process_at_time = 1
        min_id = 0
        min_burst = self.min_burst()
        flag_to_queue = 0

        ta_time = []
        wt_time = []
        burst = []
        for k in range(len(self.list)):
            burst.insert(k, self.list[k].burst)

        while self.is_finished() == 0:
            no_process_at_time = 1
            for i in range(len(self.list)):
                if self.list[i].burst == 0:
                    continue
                elif self.list[i].arrival <= current_time:
                    no_process_at_time = 0
                    if first_time:
                        first_time = 0
                        min_burst = self.list[i].burst
                        min_id = i
                        flag_to_queue = 1
                    else:
                        if self.list[i].burst < min_burst:
                            min_burst = self.list[i].burst
                            min_id = i
                            flag_to_queue = 1
            if self.list[min_id].burst != 0 and flag_to_queue == 1:
                self.processes_ids.append(min_id + 1)
                self.processes_bursts.append(self.list[min_id].burst)
                current_time = current_time + self.list[min_id].burst
                ta_time.insert(min_id, current_time - self.list[min_id].arrival)
                self.list[min_id].burst = 0
                flag_to_queue = 0
            first_time = 1
            if no_process_at_time:
                current_time = current_time + 1
                self.processes_ids.append(0)
                self.processes_bursts.append(1)

        for j in range (len(self.list)):
                wt_time.insert(j,ta_time[j] - burst[j])
        self.ta_time_avg = sum(ta_time) / len(self.list)
        self.wt_time_avg = sum(wt_time) / len(self.list)


    def min_burst(self):
        min_burst = 1
        i = 0
        for i in self.list:
            if i.burst < min_burst:
                min_burst = i.burst
        return min_burst

    def max_priority(self):
        max_par = 1
        i = 0
        for i in self.list:
            if i.priority < max_par:
                max_par = i.priority
        return max_par

    def SJF_P_Sort(self):
        i = 0
        current_time = 0
        first_time = 1
        no_process_at_time = 1
        min_id = 0
        min_burst = self.min_burst()
        flag_to_queue = 0

        ta_time = []
        wt_time = []
        burst = []
        for k in range(len(self.list)):
            burst.insert(k, self.list[k].burst)

        while self.is_finished() == 0:
            no_process_at_time = 1
            for i in range(len(self.list)):
                if self.list[i].burst == 0:
                    continue
                elif self.list[i].arrival <= current_time:
                    no_process_at_time = 0
                    if first_time:
                        first_time = 0
                        min_burst = self.list[i].burst
                        min_id = i
                        flag_to_queue = 1
                    else:
                        if self.list[i].burst < min_burst:
                            min_burst = self.list[i].burst
                            min_id = i
                            flag_to_queue = 1
            if self.list[min_id].burst != 0 and flag_to_queue == 1:
                self.list[min_id].burst = self.list[min_id].burst - 1
                self.processes_ids.append(min_id + 1)
                self.processes_bursts.append(1)
                current_time = current_time + 1
                #self.list[min_id].burst = 0
                flag_to_queue = 0
                if self.list[min_id].burst == 0:
                    ta_time.insert(min_id, current_time - self.list[min_id].arrival)

            first_time = 1
            if no_process_at_time:
                current_time = current_time + 1
                self.processes_ids.append(0)
                self.processes_bursts.append(1)

        for j in range (len(self.list)):
                wt_time.insert(j, ta_time[j] - burst[j])
        self.ta_time_avg = sum(ta_time) / len(self.list)
        self.wt_time_avg = sum(wt_time) / len(self.list)

    def FCFS(self):
        ta_time = []
        wt_time = []
        burst = []
        flag_to_queue = 0
        for k in range(len(self.list)):
            burst.insert(k, self.list[k].burst)
        time = 0
        while self.is_finished() == 0:
            for i in range(len(self.list)):
                if self.list[i].burst == 0:
                    continue
                no_process_at_time = 1
                if self.list[i].arrival <= time:
                    time += self.list[i].burst
                    self.processes_ids.append(i+1)
                    self.processes_bursts.append(self.list[i].burst)
                    self.list[i].burst = 0
                    no_process_at_time = 0
                    if self.list[i].burst == 0:
                        ta_time.insert(i, time - self.list[i].arrival)
            if no_process_at_time:
                time = time + 1
                self.processes_ids.append(0)
                self.processes_bursts.append(1)
        for j in range(len(self.list)):
                wt_time.insert(j, ta_time[j] - burst[j])
        self.ta_time_avg = sum(ta_time) / len(self.list)
        self.wt_time_avg = sum(wt_time) / len(self.list)


    '''def ta_wt_pre_calc(self):
        wt_time = 0
        count = []
        turnaround_time = 0
        total_time = self.list[0].arrival
        for i in range(0, len(self.list)):
            count.append(0)
            total_time += self.list[i].burst

        for i in range(self.list[0].arrival, total_time):
            #print(i, " to ", i + 1)
            flag = 0
            for j in range(1, len(self.list)):

                if self.list[0].arrival <= i and self.list[j].arrival <= i and self.list[0].burst >= 0 and self.list[j].burst > 0:

                    if self.list[j].priority < self.list[0].priority or self.list[0].burst == 0:
                        self.list[0], self.list[j] = self.list[j], self.list[0]
                        count[0], count[j] = count[j], count[0]
                        count[j] += 1

            if self.list[0].burst > 0:
                self.list[0].burst -= 1
            if self.list[0].burst is 0:
                turnaround_time = (i + 1) - self.list[0].arrival
                wt_time = wt_time + (turnaround_time - count[0])
        self.ta_time_avg = (self.ta_time_avg + turnaround_time) / len(self.list)
        self.wt_time_avg = wt_time / len(self.list)
        print(self.ta_time_avg)
        print(self.wt_time_avg)'''

    def preemptivePriority(self):
        i = 0
        current_time = 0
        first_time = 1
        no_process_at_time = 1
        max_id = 0
        max_priority = self.max_priority()
        flag_to_queue = 0

        ta_time = []
        wt_time = []
        burst = []
        for k in range(len(self.list)):
            burst.insert(k, self.list[k].burst)

        while self.is_finished() == 0:
            no_process_at_time = 1
            for i in range(len(self.list)):
                if self.list[i].burst == 0:
                    continue
                elif self.list[i].arrival <= current_time:
                    no_process_at_time = 0
                    if first_time:
                        first_time = 0
                        max_priority = self.list[i].priority
                        max_id = i
                        flag_to_queue = 1
                    else:
                        if self.list[i].priority < max_priority:
                            max_priority = self.list[i].priority
                            max_id = i
                            flag_to_queue = 1
            if self.list[max_id].burst != 0 and flag_to_queue == 1:
                self.list[max_id].burst = self.list[max_id].burst - 1
                self.processes_ids.append(max_id + 1)
                self.processes_bursts.append(1)
                current_time = current_time + 1
                flag_to_queue = 0
                if self.list[max_id].burst == 0:
                    ta_time.insert(max_id, current_time - self.list[max_id].arrival)

            first_time = 1
            if no_process_at_time:
                current_time = current_time + 1
                self.processes_ids.append(0)
                self.processes_bursts.append(1)
        for j in range (len(self.list)):
                wt_time.insert(j, ta_time[j] - burst[j])
        self.ta_time_avg = sum(ta_time) / len(self.list)
        self.wt_time_avg = sum(wt_time) / len(self.list)

# '''p1 = process('p1',1,2,3)
# p2 = process('p2',2,3,4)
# plist = [p1, p2]'''
'''pro_queue = processList()
pro_queue.insert('p1',0,0,3)
pro_queue.insert('p2',10,0,6)
pro_queue.insert('p3',4,0,9)
pro_queue.SJF_P_Sort()
print(pro_queue.processes_ids)
print(pro_queue.processes_bursts)
print(pro_queue)'''

'''p1 = process('p1',1,2,3)
p2 = process('p2',2,3,4)
plist = [p1, p2]'''
#pro=[]
#pro_queue = processList()
'''pro_queue.insert('p1', 0, 2, 3)
pro_queue.insert('p2', 0, 0, 6)
pro_queue.insert('p5', 20, 3, 6)
pro_queue.insert('p3', 20, 8, 9)'''
'''pro_queue.insert('p1', 4, 3, 3)
pro_queue.insert('p2', 1, 1, 6)
pro_queue.insert('p5', 2, 2, 6)
# pro_queue.insert('p4', 10, 11, 12)
#new_list.ta_wt_pre_calc()
pro_queue.FCFS()
#pro_queue.priority_graph()
print(pro_queue.processes_ids)
print(pro_queue.processes_bursts)
print(pro_queue.wt_time_avg)
print(pro_queue.ta_time_avg)
#print(pro_queue)
#pro_queue.preemptivePriority()
#pro_queue.FCFS()'''
