# from collections import deque
from collections import defaultdict

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

        self._size = 0

    def is_empty(self):
        if self._size == 0:
            return True
        return False

    def push(self, item):
        new_node = Node(item)

        new_node.next = self.head
        self.head = new_node

        self._size += 1

    def pop(self):
        if self.head is None:
            return False

        removed_thing = self.head.val
        self.head = self.head.next

        self._size -= 1

        return removed_thing

    def peek(self):
        if self.head is None:
            return False
        peek = self.head.val

        return peek
    def size(self):
        return self._size

class FreqStack:

    def __init__(self):
        self.stack = Stack()
        self.freq_dict = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.push(val)
        self.freq_dict[val] += 1

    def pop(self):
        freq = max(self.freq_dict.values())

        probe = Stack()

        while not self.stack.is_empty():
            thing = self.stack.pop()

            if self.freq_dict[thing] == freq:
                self.freq_dict[thing] -= 1
                break

            probe.push(thing)

        while not probe.is_empty():
            self.stack.push(probe.pop())

        return thing



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
