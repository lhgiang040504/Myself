class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.items.pop()

def neighbors(curr):
    return [
        (curr[0] + 1, curr[1]),
        (curr[0] - 1, curr[1]),
        (curr[0], curr[1] + 1),
        (curr[0], curr[1] - 1)
    ]

def solve(avail):
    stack = Stack()
    stack.push(avail[0])
    while not stack.isEmpty():
        curr = stack.pop()
        if curr in avail:
            avail.remove(curr)
        for neighbor in neighbors(curr):
            if neighbor in avail:
                stack.push(neighbor)
    return 'Yes' if avail == [] else 'No'

# Declare matrix
avail = []
# Input matrix
for x in range(2):
    row = input()
    for y in range(2):
        if row[y] == '#':
            avail.append((x, y))

if avail == []:
    print('No')
else:
    print(solve(avail))
