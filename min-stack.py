"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
Subscribe to see which companies asked this question.
"""

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Solution: store the gap between the min val and the current val

data: 
store the gap between min val and current val
negative when min value change

"""
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        INF = 0x11111111111111111111111111111111
        self.data = []
        self.min = INF
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x - self.min) #Could be negative if min value needs to change (x < current min val)
        if x < self.min:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if self.isEmpty():
            return
        pop_val = self.data.pop()
        if pop_val < 0:
            self.min = self.min - pop_val

    def top(self):
        """
        :rtype: int
        """
        if len(self.data) == 0:
            return
        top = self.data[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

    def isEmpty(self):
        return len(self.data) == 0

#Solution II store data structure in stack
#Ex: Node(val, cur_min)

"""
Note:
Input value might be duplicate.
Any solution based on comparision (Two Stack/ Push min in data when have new min val) might cause fault

Example:

    #Double Stack
    def push(self, x):
        self.data.append(x)
        if not self.min_vals or x < self.getMin():
            self.min_vals.append(x)

    def pop(self):
        if self.isEmpty():
            return
        pop_val = self.data.pop()
        if pop_val == self.min_vals[-1]:
            self.min_vals.pop()

Test case:

push(0)
push(1)
push(0)
pop()
getMin() #Err, index out of range. stack-ii that store the min val has poped 0 but the first 0 is still in the stack

"""
