class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Стек пуст')
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.value

    def peek(self):
        if self.is_empty():
            raise IndexError('Стек пуст')
        return self.top.value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def __str__(self):
        if self.is_empty():
            return "Стек пуст"

        result = []
        current_node = self.top

        while current_node is not None:
            result.append(str(current_node.value))
            current_node = current_node.next

        stack_representation = "Вершина -> " + " -> ".join(result) + " -> Основание"

        return stack_representation
