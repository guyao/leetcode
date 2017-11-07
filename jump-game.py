"""
Jump Game
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

# O(n^2)
# Time Limit Exceeded


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [False for _ in nums]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
        return dp[-1]
# Greedy


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        reach = 0
        for i in range(len(nums)):
            if i <= reach and nums[i] + i >= reach:
                reach = nums[i] + i
        return reach >= len(nums) - 1


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        i = 0
        while i <= reach and i < len(nums):
            reach = max(i + nums[i], reach)
            i += 1
        return i == len(nums)

# Dynamic Programming


t = [2, 3, 1, 1, 4]
t = [3, 2, 1, 0, 4]
t = [0, 1]  # False
# t = [2, 5, 0, 0] # True
t = [0]  # True

r = Solution().canJump(t)
