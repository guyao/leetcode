"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
# Solution 1
"""
To reach nth step,
A advance one step from n - 1
B advance two steps from n -2
"""

# will exceed time limit when n is big
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

"""
Therefore, f(n) = f(n-1) + f(n-2)
Storeing previous values in array
Even optimize this further by storing just the previous two values
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        p = 1 # f(n - 1)
        q = 2 # f(n - 2)
        for i in range(3, n+1):
            p, q = q, p + q
        return q

# Combinatorics


        


