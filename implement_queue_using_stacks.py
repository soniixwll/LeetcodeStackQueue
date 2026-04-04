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
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

class MyQueue:

    def __init__(self):
        self.stack_for_in = Stack()
        self.stack_for_out = Stack()
    def push(self, x: int) -> None:
        self.stack_for_in.push(x)

    def pop(self) -> int:
        if  self.stack_for_out.size() == 0:
            while self.stack_for_in:
                self.stack_for_out.push(self.stack_for_in.pop())

        return self.stack_for_out.pop()

    def peek(self) -> int:
        if  self.stack_for_out.size() == 0:
            while self.stack_for_in:
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
