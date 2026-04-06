"""Implementing Stack using Queues"""
class Node:
    """Class Node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    """Class queue"""
    def __init__(self):
        self.queue = None
        self.head = None
        self._size = 0

    def push(self, x):
        """Adds en element to the queue"""
        new_node = Node(x)

        if self.head is None:
            self.head = new_node
            self.queue = new_node
        else:
            # while self.queue.next:
            #     self.queue = self.queue.next
            self.queue.next = new_node
            self.queue = self.queue.next

        self._size += 1

    def pop(self):
        """Removes an element from the queue"""
        if self.head is None:
            self.queue = None
        removed_thing = self.head.val

        self.head = self.head.next

        self._size -= 1

        return removed_thing

    def peek(self):
        """Shows the peek of the element"""
        return self.head.val

    def size(self):
        """Returns the length of the queue"""
        return self._size

    def is_empty(self):
        """Checks if queue is empty"""
        if self._size == 0:
            return True
        return False

class MyStack:
    """Class Stack"""
    def __init__(self):
        self.queue_in = Queue()
        self.queue_out = Queue()

    def push(self, x: int) -> None:
        """Adds en element to the queue"""
        self.queue_in.push(x)

    def pop(self) -> int:
        """Removes an element from the queue"""
        if not self.queue_in.is_empty():
            while self.queue_in.size() > 1:
                self.queue_out.push(self.queue_in.pop())

        answear = self.queue_in.pop()

        self.queue_out, self.queue_in = self.queue_in, self.queue_out

        return answear

    def top(self) -> int:
        """Shows the top of an elemnet"""
        if not self.queue_in.is_empty():
            while self.queue_in.size() > 1:
                self.queue_out.push(self.queue_in.pop())

        answear = self.queue_in.peek()
        self.queue_out.push(self.queue_in.pop())
        self.queue_out, self.queue_in = self.queue_in, self.queue_out

        return answear

    def empty(self) -> bool:
        """Checks if is empty"""
        return  self.queue_in.is_empty() and self.queue_out.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
