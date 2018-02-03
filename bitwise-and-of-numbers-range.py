"""
Solution:
Find the common prefix of m, n
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        fac = 1
        while m != n:
            m >>= 1
            n >>= 1
            fac <<= 1
        return m * fac