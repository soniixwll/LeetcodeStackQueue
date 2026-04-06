# from collections import deque
"""Module which implements queue"""
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

class MyQueue:
    """Class queue implemented by stacks"""

    def __init__(self):
        self.stack_for_in = Stack()
        self.stack_for_out = Stack()

    def push(self, x: int) -> None:
        """Adds an element"""
        self.stack_for_in.push(x)

    def pop(self) -> int:
        """Removes an element"""
        if  self.stack_for_out.size() == 0:
            while not self.stack_for_in.is_empty():
                self.stack_for_out.push(self.stack_for_in.pop())

        return self.stack_for_out.pop()

    def peek(self) -> int:
        """Shows the peek of the queue"""
        if  self.stack_for_out.size() == 0:
            while not self.stack_for_in.is_empty():
                self.stack_for_out.push(self.stack_for_in.pop())

        return self.stack_for_out.peek()

    def empty(self) -> bool:
        """Checks if empty"""
        return self.stack_for_in.is_empty() and self.stack_for_out.is_empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
