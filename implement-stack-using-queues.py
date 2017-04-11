"""
#Solution

modify push()
queue [newer...older]

`deque` pop left

def push(x):
    q.enque(x)
    do len(q) - 1 times
        q.enque(q.deque())

loop invariant:
if q[0..i-1] has been [newer...older] order
in push
q[i] = [qi] + [newer...older]
"""
class Queue(list):
    def enque(self, x):
        self.append(x)

    def deque(self):
        return self.pop(0) if len(self) != 0 else None

    def empty(self):
        return len(self) == 0

    def peek(self):
        return self[0]

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.enque(x)
        for _ in range(len(self.q) - 1):
            self.q.enque(self.q.deque())
        print(self.q)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.deque()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q.peek()

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()