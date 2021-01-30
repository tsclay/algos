class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"<Node> data: {self.data}, next: {self.next}"


class Stack():

    size = 0
    top = None

    def peek(self):
        if self.top is None:
            return
        return self.top.data

    def is_empty(self):
        return self.top is None

    def push(self, data):
        node = Node(data)
        if self.top is not None:
            node.next = self.top
        self.top = node
        self.items[self.size] = node
        self.size += 1

    def pop(self):
        if self.top is None:
            return
        self.top = self.top.next
        self.size -= 1

    def __init__(self) -> None:
        self.items = {}

    def __repr__(self) -> str:
        return f"<Stack>\nTop: {self.top}\nSize: {self.size}\nEmpty?: {self.is_empty()}\nPeek: {self.peek()}"


test = Stack()

test.push(0)
print(test)

test.push(1)
print(test)

test.push(2)
print(test)

test.pop()
print(test)

test.pop()
print(test)

test.pop()
print(test)


"""
<Stack>
Top: <Node> data: 0, next: None
Size: 1
Empty?: False
Peek: 0
<Stack>
Top: <Node> data: 1, next: <Node> data: 0, next: None
Size: 2
Empty?: False
Peek: 1
<Stack>
Top: <Node> data: 2, next: <Node> data: 1, next: <Node> data: 0, next: None
Size: 3
Empty?: False
Peek: 2
<Stack>
Top: <Node> data: 1, next: <Node> data: 0, next: None
Size: 2
Empty?: False
Peek: 1
<Stack>
Top: <Node> data: 0, next: None
Size: 1
Empty?: False
Peek: 0
<Stack>
Top: None
Size: 0
Empty?: True
Peek: None
"""
