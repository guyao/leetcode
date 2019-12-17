# https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.prev = [None for _ in range(size)]
        self.index = -1
        self.size = size
        self.current_sum = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.index += 1
        
        self.current_sum = self.current_sum - (self.prev[self.index % self.size] if self.prev[(self.index) % self.size] else 0) + val
        self.prev[self.index % self.size] = val
        
        if self.index < self.size:
            return self.current_sum / (self.index + 1)
        else:
            return self.current_sum / self.size



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)