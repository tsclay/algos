import json

# Based on "Data Structure: Stacks and Queues" by HackerRank on YouTube
# https://www.youtube.com/watch?v=wjI1WNcIntg


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"<Node> data: {self.data}, next: {self.next}"


class Queue():

    size = 0
    max_size = 10

    head = None
    tail = None

    def add(self, data):
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        self.items[self.size] = node
        self.size += 1
        return self

    def remove(self):
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_data

    def is_empty(self):
        return self.head is None

    def peek(self):
        return self.head.data

    def __init__(self):
        self.items = {}


def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))


test = Queue()
test.add(1)
print("Add 1")
print("Head: ", test.head)
print("Tail: ", test.tail)

test.add(2)
print("Add 2")
print("Head: ", test.head)
print("Tail: ", test.tail)

test.add(3)
print("Add 3")
print("Head: ", test.head)
print("Tail: ", test.tail)

test.add(4)
print("Add 4")
print("Head: ", test.head)
print("Tail: ", test.tail)

test.remove()
print("Remove 1")
print("Head: ", test.head)
print("Tail: ", test.tail)

test.remove()
print("Remove 2")
print("Head: ", test.head)
print("Tail: ", test.tail)

test.remove()
print("Remove 3")
print("Head: ", test.head)
print("Tail: ", test.tail)
