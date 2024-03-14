import sys
#inputs = list(map(str.str, sys.stdin.readlines()))
inputs = ['20 4',
'380 left',
'720 left',
'1340 right',
'1040 left']
length_ferries, num_waits = map(int, inputs[0].split())
length_ferries *= 100
class Queue():
    def __init__(self, l):
        self.frontier = []
        self.length_ferries = l
    def push(self, point):
        self.frontier.append(point)
    def isEmpty(self):
        return len(self.frontier) == 0
    def get(self):
        return 0 if self.isEmpty() else self.frontier[0]
    def pop(self):
        if not self.isEmpty():
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
    def remove(self):
        temp = 0
        while True:
            node = self.get()
            if node == 0:
                break
            temp += node
            if temp > self.length_ferries:
                break
            self.pop()
        
right_side = Queue(length_ferries)
left_side = Queue(length_ferries)
for i in range(1, num_waits+1):
    infor = inputs[i].split()
    if infor[1] == 'left':
        left_side.push(int(infor[0]))
    else:
        right_side.push(int(infor[0]))

count = 0
while True:
    if left_side.isEmpty() and right_side.isEmpty():
        break
    count += 1   
    left_side.remove()

    if left_side.isEmpty() and right_side.isEmpty():
        break
    count += 1
    right_side.remove()
    
sys.stdout.write(str(count))