# from collections import deque
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        # self.stack = None

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

class MyQueue:

    def __init__(self):
        self.stack_for_in = Stack()
        self.stack_for_out = Stack()
    def push(self, x: int) -> None:
        self.stack_for_in.push(x)

    def pop(self) -> int:
        if  self.stack_for_out.size() == 0:
            while not self.stack_for_in.is_empty():
                self.stack_for_out.push(self.stack_for_in.pop())

        return self.stack_for_out.pop()

    def peek(self) -> int:
        if  self.stack_for_out.size() == 0:
            while not self.stack_for_in.is_empty():
                self.stack_for_out.push(self.stack_for_in.pop())

        return self.stack_for_out.peek()

    def empty(self) -> bool:
        return self.stack_for_in.is_empty() and self.stack_for_out.is_empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
