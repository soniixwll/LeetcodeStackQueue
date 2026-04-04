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
        if len(self.queue) != 0:
            return self.queue[0]
        return False

    def size(self):
        return len(self.queue)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

class MyStack:

    def __init__(self):
        self.queue_in = Queue()
        self.queue_out = Queue()

    def push(self, x: int) -> None:
        self.queue_in.push(x)

    def pop(self) -> int:
        if not self.queue_in.is_empty():
            while self.queue_in.size() > 1:
                self.queue_out.push(self.queue_in.pop())

        answear = self.queue_in.pop()

        self.queue_out, self.queue_in = self.queue_in, self.queue_out

        return answear

    def top(self) -> int:
        if not self.queue_in.is_empty():
            while self.queue_in.size() > 1:
                self.queue_out.push(self.queue_in.pop())

        answear = self.queue_in.peek()
        self.queue_out.push(self.queue_in.pop())
        self.queue_out, self.queue_in = self.queue_in, self.queue_out

        return answear

    def empty(self) -> bool:
        return  self.queue_in.is_empty() and self.queue_out.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
