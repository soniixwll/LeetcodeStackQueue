class Stack:
    def __init__(self):
        self.stack = []

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

    def __len__(self):
        return len(self.stack)

class MyQueue:

    def __init__(self):


    def push(self, x: int) -> None:


    def pop(self) -> int:


    def peek(self) -> int:


    def empty(self) -> bool:



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
