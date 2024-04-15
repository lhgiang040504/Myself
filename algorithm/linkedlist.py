class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:  
            self.tail = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.tail is None: 
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_after(self, value_a, value_b):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == value_a:
                found = True
                new_node = Node(value_b)
                new_node.next = current.next
                current.next = new_node
                if new_node.next is None: 
                    self.tail = new_node
            else:
                current = current.next
        if not found:
            self.add_first(value_b)
    
    def del_first(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is None:  
                self.tail = None

    def del_after(self, value_a):
        current = self.head
        previous = Node(None)
        found = False
        while current is not None and not found:
            if current.data == value_a:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous.data == None:
                self.head = current.next
            else:
                previous.next = current.next
                if previous.next is None:
                    self.tail = previous

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

linked_list = LinkedList()

while True:
    line = input().strip()
    if line == "6":
        break
    command, *values = map(int, line.split())

    if command == 0:
        linked_list.add_first(values[0])
    elif command == 1:
        linked_list.add_last(values[0])
    elif command == 2:
        linked_list.add_after(values[0], values[1])
    elif command == 3:
        linked_list.del_after(values[0])
    elif command == 5:
        linked_list.del_first()

    print('-', end=' ')
    linked_list.print_list()


linked_list.print_list()
