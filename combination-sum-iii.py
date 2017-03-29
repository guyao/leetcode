"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        r = self.comb(k, n, 1)
        return r
    
    def comb(self, k, n, start):
        pass
        ret = []
        if n < 0:
            return
        for i in range(start, 9 + 1):
            if k == 1 and n == i:
                return [[i]]
            r = self.comb(k - 1, n - i, i + 1)
            if r:
                for l in r:
                    ret.append([i] + l)
        return ret
r = Solution().combinationSum3(3, 9)
