class Stack(list):
    def push(self, x):
        self.append(x)

    def peek(self):
        return self[-1]

    def empty(self):
        return len(self) == 0

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = Stack()
        self.output = Stack()


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.input.push(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.output.empty():
            self.move()
        return self.output.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.output.empty():
            self.move()
        return self.output.peek()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.input.empty() and self.output.empty()

    def move(self):
        while self.input:
            self.output.push(self.input.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()