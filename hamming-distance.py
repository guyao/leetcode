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

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = x ^ y
        dist = 0
        while ans:
            ans = ans & ans - 1
            dist += 1
        return dist

def bit_count(x):
    count = 0
    while x != 0:
        if x%2 != 0:
            count += 1
        x >>= 1
    return count

def bit_count(x):
    count = 0
    while x != 0:
        count += x & 1
        x = x >> 1
    return count

def bit_count(x):
    count = 0
    while x != 0:
        x = x & (x-1)
        count += 1
    return count