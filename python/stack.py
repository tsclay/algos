class Stack():

    size = 0

    def push(self, item):
        self.items[self.size] = item
        self.size += 1
        return self

    def pop(self):
        if self.size == 0:
            return
        self.items.pop(self.size - 1)
        self.size -= 1
        return self

    def peek(self):
        if self.size == 0:
            return self.items[self.size]
        return self.items[self.size - 1]

    def is_empty(self):
        if self.items.__len__() == 0:
            return True
        return False

    def __init__(self):
        self.items = {}


test = Stack()
test.push("one")
test.push('second')
test.push('third')
print(test.items, test.size)  # {0: 'one', 1: 'second', 2: 'third'} 3
print(test.peek())  # third
print(test.is_empty())  # False
test.pop()
print(test.items, test.size)  # {0: 'one', 1: 'second'} 2
test.pop()
print(test.items, test.size)  # {0: 'one'} 1
test.push('second')
print(test.items, test.size)  # {0: 'one', 1: 'second'} 2
test.pop()
print(test.items, test.size)  # {0: 'one'} 1
print(test.is_empty())  # False
test.pop()
print(test.is_empty())  # True
