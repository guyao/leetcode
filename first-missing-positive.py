"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = []
        import heapq
        s = set()
        for i in nums:
            if i > 0:
                s.add(i)
        for i in s:
            heapq.heappush(h, i)
        start = 0
        p = start
        while len(h) != 0:
            p = heapq.heappop(h)
            if p == start + 1:
                start = start + 1
            else:
                return start + 1
        return p + 1


t = [3, 4, -1 ,1]
t = [0, 1, 2]
t = [0]
t = []
t = [1]
t = [0, 2, 2, 1, 1]
r = Solution().firstMissingPositive(t)