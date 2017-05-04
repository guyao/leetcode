# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

target = 6
def guess(num):
    if num > target:
        return -1
    elif num < target:
        return 1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        while True:
            m = (lo+hi) // 2
            if guess(m) == 1:
                lo = m + 1
            elif guess(m) == -1:
                hi = m - 1
            else:
                return m

r = Solution().guessNumber(10)