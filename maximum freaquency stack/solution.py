"""Module frequent stack"""
from collections import defaultdict

class Node:
    """Class Node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    """Class Stack"""
    def __init__(self):
        self.head = None
        # self.stack = None

        self._size = 0

    def is_empty(self):
        """Checks if stack is empty"""
        if self._size == 0:
            return True
        return False

    def push(self, item):
        """Adds an element to the stack"""
        new_node = Node(item)

        new_node.next = self.head
        self.head = new_node

        self._size += 1

    def pop(self):
        """Removes an element from the """
        if self.head is None:
            return False

        removed_thing = self.head.val
        self.head = self.head.next

        self._size -= 1

        return removed_thing

    def peek(self):
        """Shows the peek of the stack"""
        if self.head is None:
            return False
        peek = self.head.val

        return peek
    def size(self):
        """Shows the length of the stack"""
        return self._size

class FreqStack:
    """Class frequent stack"""
    def __init__(self):
        self.stack = Stack()
        self.freq_dict = defaultdict(int)

    def push(self, val: int) -> None:
        """Adds an element"""
        self.stack.push(val)
        self.freq_dict[val] += 1

    def pop(self):
        """Removes the most frequent element which is the closest to the top of an stack"""
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
