class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = x ^ y
        count = 0
        for i in range(32):
            if 1 << i & ans:
                count += 1
        return count

