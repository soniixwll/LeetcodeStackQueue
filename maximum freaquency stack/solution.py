from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if len(self.queue) != 0:
            return self.queue.popleft()
        return False

    def peek(self):
        if len(self.queue) != 0:
            return self.queue[0]
        return False

    def size(self):
        return len(self.queue)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

class FreqStack:

    def __init__(self):


    def push(self, val: int) -> None:


    def pop(self) -> int:



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
