class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = 1
        while r * r <= x:
            r = r * 2
        while l < r:
            m = (l + r + 1) // 2
            if m * m <= x:
                l = m
            else:
                r = m - 1
        return l