from collections import deque
from collections import defaultdict

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
        self.stack = Stack()
        self.freq_dict = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.push(val)
        self.freq_dict[val] += 1

    def pop(self):
        freq = max(self.freq_dict.values())
        for key in self.freq_dict.keys():
            if self.freq_dict[key] == freq:
                freq_number = key
                break

        probe = Stack()

        while not self.stack.is_empty():
            thing = self.stack.pop()

            if thing == freq_number:
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
