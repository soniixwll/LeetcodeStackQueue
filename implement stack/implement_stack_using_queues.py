from collections import deque

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
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

class MyStack:

    def __init__(self):
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def empty(self) -> bool:
        pass


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
