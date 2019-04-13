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

        while self.is_finished() == 0:
            no_process_at_time = 1
            for index in range(len(self.list)):
                if self.list[index].burst == 0:
                    continue
                elif self.list[index].arrival <= i:
                    if self.list[index].burst >= quantum_time:
                        i = i + quantum_time
                        self.list[index].burst = self.list[index].burst - quantum_time
                        self.processes_ids.append(index + 1)
                        self.processes_bursts.append(quantum_time)
                        no_process_at_time = 0
                    else:
                        i = i + self.list[index].burst
                        self.processes_ids.append(index + 1)
                        self.processes_bursts.append(self.list[index].burst)
                        self.list[index].burst = 0
                        no_process_at_time = 0
            if no_process_at_time:
                i = i + 1
                self.processes_ids.append(0)
                self.processes_bursts.append(1)


# '''p1 = process('p1',1,2,3)
# p2 = process('p2',2,3,4)
# plist = [p1, p2]'''
# pro_queue = processList()
# pro_queue.insert('p1',0,0,3)
# pro_queue.insert('p2',10,0,6)
# pro_queue.insert('p3',10,0,9)
# pro_queue.RR_sort(2)
# print(pro_queue.processes_ids)
# print(pro_queue.processes_bursts)
# print(pro_queue)
