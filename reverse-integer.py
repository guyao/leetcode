"""
Hint: overflow?
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        ret = 0
        if x < 0:
            positive = False
            x = -x
        while x != 0:
            ret = ret * 10 + x % 10
            x = x // 10
        return ret if ret <= 0x7fffffff else 0

r = Solution().reverse(10000)
print(r)