"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

#Time Exceeded
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        res = 0
        for n in nums:
            if not m.get(n):
                left = m[n-1] if m.get(n-1) else 0
                right = m[n+1] if m.get(n+1) else 0
                length = left + right + 1
                m[n] = length
                res = max(res, length)
                for i in range(left):
                    t = i + 1
                    m[n-t] = length
                for i in range(right):
                    t = i + 1
                    m[n+t] = length
            else:
                # duplicates
                continue
        return res

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        res = 0
        for n in nums:
            if not m.get(n):
                left = m[n-1] if m.get(n-1) else 0
                right = m[n+1] if m.get(n+1) else 0
                length = left + right + 1
                m[n] = length
                res = max(res, length)
                m[n-left] = length
                m[n+right] = length
            else:
                # duplicates
                continue
        return res


t = [100, 4, 200, 1, 3, 2]
t = [1, 2, 0, 1] #3
t = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
r = Solution().longestConsecutive(t)