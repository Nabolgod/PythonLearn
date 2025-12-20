class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if self.is_empty():
            raise IndexError('Стек пуст')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Стек пуст')
        return self.stack[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

