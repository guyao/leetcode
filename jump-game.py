"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        i = 0
        while i <= reach and i <len(nums):
            reach = max(i+nums[i], reach)
            i += 1
        return i == len(nums)


t = [2,3,1,1,4]
t = [3, 2, 1, 0, 4]
t = [0, 1] # False
# t = [2, 5, 0, 0] # True
t = [0] # True

r = Solution().canJump(t)

