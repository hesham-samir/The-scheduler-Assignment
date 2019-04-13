class process:
    def __init__(self, name, arrival, priority, burst):
        self.name = name
        self.arrival = arrival
        self.priority = priority
        self.burst = burst
    def stringify(self):
        return '('+str(self.name)+','+str(self.arrival)+','+str(self.priority)+','+str(self.burst)+')'+"\n"

def csort(p):
    return p.arrival

class process_list:
    def __init__(self, list):
        self.list=list


    def insert(self, name, arrival, priority, burst):
        p = process(name, arrival, priority, burst)
        self.list.append(p)
        self.list.sort(key=csort)

    def __str__(self):
        ls = ""
        for p in self.list:
            ls += p.stringify()
        return ls

'''p1 = process('p1',1,2,3)
p2 = process('p2',2,3,4)
plist = [p1, p2]'''
pro=[]
pro_queue = process_list(pro)
pro_queue.insert('p1',2,2,3)
pro_queue.insert('p2',4,5,6)
pro_queue.insert('p2',4,5,6)
pro_queue.insert('p3',1,8,9)
pro_queue.insert('p4',10,11,12)
print(pro_queue)
