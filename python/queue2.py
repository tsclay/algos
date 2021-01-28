class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"<Node> data: {self.data}, next: {self.next}"


class Queue():

    head = None
    tail = None

    size = 0

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return
        return self.head.data

    def add(self, data):
        node = Node(data)
        self.items[self.size] = node
        self.size += 1
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def remove(self):
        if self.head is None:
            return
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def __init__(self):
        self.items = {}

    def __repr__(self):
        return f"<Queue>\nHead: {self.head}\nTail: {self.tail}\nEmpty?: {self.is_empty()}"


test = Queue()

test.add(0)
print(test)

test.add(1)
print(test)

test.add(2)
print(test)

test.add(3)
print(test)

test.remove()
print(test)

test.remove()
print(test)

test.remove()
print(test)

test.remove()
print(test)
